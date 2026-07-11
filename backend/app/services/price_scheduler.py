"""Background scheduler for updating market prices."""
import asyncio
import logging
from datetime import datetime
from typing import List, Optional
from sqlalchemy.orm import Session

from app.services.market_data import MarketDataService
from app.core.database import SessionLocal
from app.models import Market

logger = logging.getLogger(__name__)

class PriceScheduler:
    """Background scheduler for updating market prices."""
    
    _is_running = False
    _update_interval = 60  # Update every 60 seconds
    
    @classmethod
    async def start(cls, interval: int = 60) -> None:
        """Start the price update scheduler."""
        cls._update_interval = interval
        cls._is_running = True
        logger.info(f"Starting price scheduler with {interval}s interval")
        
        try:
            while cls._is_running:
                await cls._update_all_prices()
                await asyncio.sleep(cls._update_interval)
        except Exception as e:
            logger.error(f"Price scheduler error: {e}")
            cls._is_running = False
    
    @classmethod
    async def stop(cls) -> None:
        """Stop the price update scheduler."""
        cls._is_running = False
        logger.info("Price scheduler stopped")
    
    @classmethod
    async def _update_all_prices(cls) -> None:
        """Update prices for all markets."""
        db = SessionLocal()
        try:
            # Get all markets
            markets = db.query(Market).all()
            if not markets:
                logger.warning("No markets in database")
                return
            
            symbols = [m.symbol for m in markets]
            logger.debug(f"Updating prices for {len(symbols)} markets")
            
            # Fetch prices
            prices = await MarketDataService.fetch_all_market_prices(symbols)
            
            # Update database
            for symbol, price_data in prices.items():
                try:
                    market = next(m for m in markets if m.symbol == symbol)
                    market.price = price_data["price"]
                    market.change_24h = price_data["change_24h"]
                    market.volume = price_data["volume"]
                    if price_data["market_cap"]:
                        market.market_cap = price_data["market_cap"]
                    market.updated_at = datetime.utcnow()
                except (StopIteration, KeyError) as e:
                    logger.error(f"Error processing price for {symbol}: {e}")
                    continue
            
            db.commit()
            logger.debug(f"Updated {len(prices)} market prices")
            
        except Exception as e:
            logger.error(f"Error updating prices: {e}")
            db.rollback()
        finally:
            db.close()
    
    @classmethod
    async def update_single_price(cls, symbol: str) -> Optional[dict]:
        """Update price for a single market."""
        db = SessionLocal()
        try:
            price_data = await MarketDataService.fetch_market_price(symbol)
            if not price_data:
                return None
            
            market = MarketDataService.create_market(
                db,
                symbol=price_data["symbol"],
                name=price_data["name"],
                price=price_data["price"],
                change_24h=price_data["change_24h"],
                volume=price_data["volume"],
                market_cap=price_data.get("market_cap"),
            )
            
            return {
                "symbol": market.symbol,
                "price": market.price,
                "change_24h": market.change_24h,
                "updated_at": market.updated_at.isoformat(),
            }
        except Exception as e:
            logger.error(f"Error updating {symbol}: {e}")
            return None
        finally:
            db.close()
