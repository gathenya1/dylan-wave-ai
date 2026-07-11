"""API endpoints for market data and price information."""
from fastapi import APIRouter, HTTPException, Depends, status, Query
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List, Optional

from app.core.database import get_db
from app.core.security import get_current_user
from app.models import Market, PriceHistory, MarketSnapshot
from app.schemas import (
    MarketResponse,
    MarketCreate,
    PriceHistoryResponse,
    MarketSnapshotResponse,
    WatchlistCreate,
    WatchlistResponse,
)
from app.services.market_data import MarketDataService, WatchlistService
from app.services.price_scheduler import PriceScheduler

router = APIRouter()

# ============================================================================
# Market Endpoints
# ============================================================================

@router.get("/symbols", response_model=List[str])
async def get_all_symbols(db: Session = Depends(get_db)):
    """Get list of all available market symbols."""
    markets = db.query(Market.symbol).all()
    return [m[0] for m in markets]

@router.get("", response_model=List[MarketResponse])
async def get_markets(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
):
    """Get all available markets with pagination."""
    markets = db.query(Market).offset(skip).limit(limit).all()
    return [MarketResponse.model_validate(m) for m in markets]

@router.get("/{market_id}", response_model=MarketResponse)
async def get_market(market_id: str, db: Session = Depends(get_db)):
    """Get specific market data by ID."""
    market = db.query(Market).filter(Market.id == market_id).first()
    
    if not market:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Market not found"
        )
    
    return MarketResponse.model_validate(market)

@router.get("/symbol/{symbol}", response_model=MarketResponse)
async def get_market_by_symbol(symbol: str, db: Session = Depends(get_db)):
    """Get market data by symbol."""
    market = db.query(Market).filter(
        Market.symbol.ilike(symbol)
    ).first()
    
    if not market:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Market not found for symbol: {symbol}"
        )
    
    return MarketResponse.model_validate(market)

@router.post("/admin/seed", response_model=List[MarketResponse], status_code=status.HTTP_201_CREATED)
async def seed_markets(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Seed database with sample markets (admin only)."""
    # In production, check for admin role
    created_markets = []
    
    for market_data in MarketDataService.SAMPLE_MARKETS:
        market = MarketDataService.create_market(
            db,
            symbol=market_data["symbol"],
            name=market_data["name"],
            price=0.0,  # Will be updated by scheduler
            change_24h=0.0,
            volume=0.0,
        )
        created_markets.append(market)
    
    return [MarketResponse.model_validate(m) for m in created_markets]

@router.post("/admin/update-single/{symbol}", response_model=MarketResponse)
async def update_market_price(
    symbol: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Update price for a single market (admin only)."""
    # Fetch latest price from API
    price_data = await MarketDataService.fetch_market_price(symbol)
    
    if not price_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Could not fetch price for {symbol}"
        )
    
    market = MarketDataService.create_market(
        db,
        symbol=price_data["symbol"],
        name=price_data["name"],
        price=price_data["price"],
        change_24h=price_data["change_24h"],
        volume=price_data["volume"],
        market_cap=price_data.get("market_cap"),
    )
    
    return MarketResponse.model_validate(market)

# ============================================================================
# Price History Endpoints
# ============================================================================

@router.get("/history/{symbol}", response_model=List[PriceHistoryResponse])
async def get_price_history(
    symbol: str,
    db: Session = Depends(get_db),
    limit: int = Query(100, ge=1, le=1000),
    hours: int = Query(24, ge=1, le=720),
):
    """Get price history for a symbol."""
    history = MarketDataService.get_price_history(
        db,
        symbol=symbol.upper(),
        limit=limit,
        hours=hours,
    )
    
    if not history:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No price history found for {symbol}"
        )
    
    return [PriceHistoryResponse.model_validate(h) for h in history]

@router.get("/snapshot/{symbol}", response_model=MarketSnapshotResponse)
async def get_latest_snapshot(
    symbol: str,
    db: Session = Depends(get_db),
):
    """Get the latest market snapshot for a symbol."""
    snapshot = MarketDataService.get_latest_snapshot(db, symbol.upper())
    
    if not snapshot:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No snapshot found for {symbol}"
        )
    
    return MarketSnapshotResponse.model_validate(snapshot)

# ============================================================================
# Watchlist Endpoints
# ============================================================================

@router.get("/watchlist", response_model=List[WatchlistResponse])
async def get_watchlist(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get user's watchlist."""
    watchlist = WatchlistService.get_user_watchlist(db, current_user["user_id"])
    return [WatchlistResponse.model_validate(w) for w in watchlist]

@router.post("/watchlist", response_model=WatchlistResponse, status_code=status.HTTP_201_CREATED)
async def add_to_watchlist(
    data: WatchlistCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Add a market to user's watchlist."""
    # Verify market exists
    market = db.query(Market).filter(Market.id == data.market_id).first()
    if not market:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Market not found"
        )
    
    watchlist = WatchlistService.add_to_watchlist(
        db,
        user_id=current_user["user_id"],
        market_id=data.market_id,
        symbol=data.symbol,
    )
    
    return WatchlistResponse.model_validate(watchlist)

@router.delete("/watchlist/{market_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_from_watchlist(
    market_id: str,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Remove a market from user's watchlist."""
    success = WatchlistService.remove_from_watchlist(
        db,
        user_id=current_user["user_id"],
        market_id=market_id,
    )
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Market not in watchlist"
        )

@router.get("/watchlist/{market_id}/is-watching")
async def is_in_watchlist(
    market_id: str,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Check if market is in user's watchlist."""
    is_watching = WatchlistService.is_in_watchlist(
        db,
        user_id=current_user["user_id"],
        market_id=market_id,
    )
    return {"is_watching": is_watching}
