from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from fastapi import Depends

from app.core.database import get_db
from app.models import Market
from app.schemas import MarketResponse

router = APIRouter()

@router.get("", response_model=list[MarketResponse])
async def get_markets(db: Session = Depends(get_db)):
    """Get all available markets."""
    markets = db.query(Market).all()
    return [MarketResponse.model_validate(m) for m in markets]

@router.get("/{market_id}", response_model=MarketResponse)
async def get_market(market_id: str, db: Session = Depends(get_db)):
    """Get specific market data."""
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
        Market.symbol.ilike(f"%{symbol}%")
    ).first()
    
    if not market:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Market not found"
        )
    
    return MarketResponse.model_validate(market)
