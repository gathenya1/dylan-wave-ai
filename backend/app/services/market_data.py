"""Market data service for fetching and managing market information."""
import asyncio
import logging
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any
from sqlalchemy.orm import Session
import uuid
import requests

from app.models import Market, PriceHistory, MarketSnapshot, Watchlist
from app.schemas import PriceHistoryCreate, MarketSnapshotResponse

logger = logging.getLogger(__name__)

class MarketDataService:
    """Service for managing market data from external APIs."""
    
    # Using CoinGecko API (free, no auth required) as example
    BASE_URL = "https://api.coingecko.com/api/v3"
    
    # Sample market symbols
    SAMPLE_MARKETS = [
        {"symbol": "BTC", "name": "Bitcoin", "id": "bitcoin"},
        {"symbol": "ETH", "name": "Ethereum", "id": "ethereum"},
        {"symbol": "BNB", "name": "Binance Coin", "id": "binancecoin"},
        {"symbol": "XRP", "name": "XRP", "id": "ripple"},
        {"symbol": "ADA", "name": "Cardano", "id": "cardano"},
        {"symbol": "SOL", "name": "Solana", "id": "solana"},
        {"symbol": "DOGE", "name": "Dogecoin", "id": "dogecoin"},
        {"symbol": "MATIC", "name": "Polygon", "id": "matic-network"},
    ]
    
    @staticmethod
    async def fetch_market_price(symbol: str) -> Optional[Dict[str, Any]]:
        """Fetch current price from CoinGecko API."""
        try:
            # Find market ID from symbol
            market = next((m for m in MarketDataService.SAMPLE_MARKETS if m["symbol"] == symbol), None)
            if not market:
                logger.warning(f"Market not found for symbol: {symbol}")
                return None
            
            params = {
                "ids": market["id"],
                "vs_currencies": "usd",
                "include_market_cap": "true",
                "include_24hr_vol": "true",
                "include_24hr_change": "true",
            }
            
            response = requests.get(
                f"{MarketDataService.BASE_URL}/simple/price",
                params=params,
                timeout=10
            )
            response.raise_for_status()
            
            data = response.json()
            if market["id"] in data:
                price_data = data[market["id"]]
                return {
                    "symbol": symbol,
                    "name": market["name"],
                    "price": price_data.get("usd", 0),
                    "change_24h": price_data.get("usd_24h_change", 0),
                    "volume": price_data.get("usd_24h_vol", 0),
                    "market_cap": price_data.get("usd_market_cap", None),
                }
            
            logger.warning(f"No price data for {symbol}")
            return None
            
        except requests.RequestException as e:
            logger.error(f"Error fetching price for {symbol}: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error fetching price: {e}")
            return None
    
    @staticmethod
    async def fetch_all_market_prices(symbols: List[str]) -> Dict[str, Dict[str, Any]]:
        """Fetch prices for multiple markets."""
        prices = {}
        for symbol in symbols:
            price_data = await MarketDataService.fetch_market_price(symbol)
            if price_data:
                prices[symbol] = price_data
        return prices
    
    @staticmethod
    def create_market(db: Session, symbol: str, name: str, price: float, 
                     change_24h: float, volume: float, market_cap: Optional[float] = None) -> Market:
        """Create or update a market in the database."""
        # Check if market exists
        existing = db.query(Market).filter(Market.symbol == symbol).first()
        
        if existing:
            # Update existing market
            existing.price = price
            existing.change_24h = change_24h
            existing.volume = volume
            existing.market_cap = market_cap
            existing.updated_at = datetime.utcnow()
            db.commit()
            db.refresh(existing)
            return existing
        
        # Create new market
        market = Market(
            id=str(uuid.uuid4()),
            symbol=symbol,
            name=name,
            price=price,
            change_24h=change_24h,
            volume=volume,
            market_cap=market_cap,
        )
        db.add(market)
        db.commit()
        db.refresh(market)
        return market
    
    @staticmethod
    def add_price_history(db: Session, market_id: str, symbol: str, 
                         open_price: float, high_price: float, low_price: float,
                         close_price: float, volume: float, timestamp: datetime) -> PriceHistory:
        """Add price history record."""
        price_history = PriceHistory(
            id=str(uuid.uuid4()),
            market_id=market_id,
            symbol=symbol,
            open_price=open_price,
            high_price=high_price,
            low_price=low_price,
            close_price=close_price,
            volume=volume,
            timestamp=timestamp,
        )
        db.add(price_history)
        db.commit()
        db.refresh(price_history)
        return price_history
    
    @staticmethod
    def get_price_history(db: Session, symbol: str, limit: int = 100,
                         hours: int = 24) -> List[PriceHistory]:
        """Get price history for a symbol."""
        since = datetime.utcnow() - timedelta(hours=hours)
        return db.query(PriceHistory).filter(
            PriceHistory.symbol == symbol,
            PriceHistory.timestamp >= since
        ).order_by(PriceHistory.timestamp.desc()).limit(limit).all()
    
    @staticmethod
    def create_market_snapshot(db: Session, market_id: str, symbol: str,
                              open_price: float, high_price: float, low_price: float,
                              close_price: float, volume: float, 
                              change_percent: float, change_amount: float) -> MarketSnapshot:
        """Create a market snapshot."""
        snapshot = MarketSnapshot(
            id=str(uuid.uuid4()),
            market_id=market_id,
            symbol=symbol,
            open_price=open_price,
            high_price=high_price,
            low_price=low_price,
            close_price=close_price,
            volume=volume,
            change_percent=change_percent,
            change_amount=change_amount,
            timestamp=datetime.utcnow(),
        )
        db.add(snapshot)
        db.commit()
        db.refresh(snapshot)
        return snapshot
    
    @staticmethod
    def get_latest_snapshot(db: Session, symbol: str) -> Optional[MarketSnapshot]:
        """Get the latest market snapshot for a symbol."""
        return db.query(MarketSnapshot).filter(
            MarketSnapshot.symbol == symbol
        ).order_by(MarketSnapshot.timestamp.desc()).first()

class WatchlistService:
    """Service for managing user watchlists."""
    
    @staticmethod
    def add_to_watchlist(db: Session, user_id: str, market_id: str, symbol: str) -> Watchlist:
        """Add a market to user's watchlist."""
        # Check if already in watchlist
        existing = db.query(Watchlist).filter(
            Watchlist.user_id == user_id,
            Watchlist.market_id == market_id
        ).first()
        
        if existing:
            return existing
        
        watchlist = Watchlist(
            id=str(uuid.uuid4()),
            user_id=user_id,
            market_id=market_id,
            symbol=symbol,
        )
        db.add(watchlist)
        db.commit()
        db.refresh(watchlist)
        return watchlist
    
    @staticmethod
    def remove_from_watchlist(db: Session, user_id: str, market_id: str) -> bool:
        """Remove a market from user's watchlist."""
        watchlist = db.query(Watchlist).filter(
            Watchlist.user_id == user_id,
            Watchlist.market_id == market_id
        ).first()
        
        if watchlist:
            db.delete(watchlist)
            db.commit()
            return True
        return False
    
    @staticmethod
    def get_user_watchlist(db: Session, user_id: str) -> List[Watchlist]:
        """Get user's watchlist."""
        return db.query(Watchlist).filter(Watchlist.user_id == user_id).all()
    
    @staticmethod
    def is_in_watchlist(db: Session, user_id: str, market_id: str) -> bool:
        """Check if market is in user's watchlist."""
        return db.query(Watchlist).filter(
            Watchlist.user_id == user_id,
            Watchlist.market_id == market_id
        ).first() is not None
