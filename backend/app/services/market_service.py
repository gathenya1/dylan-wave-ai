"""Market data service for fetching and caching market information."""
from typing import List, Optional
from app.schemas import MarketResponse

class MarketService:
    """Service for market operations."""
    
    @staticmethod
    def get_mock_markets() -> List[dict]:
        """Get mock market data for demonstration."""
        return [
            {
                "symbol": "BTC/USD",
                "name": "Bitcoin",
                "price": 43200.50,
                "change_24h": 2.5,
                "volume": 1500000000,
                "market_cap": 845000000000,
            },
            {
                "symbol": "ETH/USD",
                "name": "Ethereum",
                "price": 1900.75,
                "change_24h": 1.2,
                "volume": 800000000,
                "market_cap": 228000000000,
            },
            {
                "symbol": "SOL/USD",
                "name": "Solana",
                "price": 210.45,
                "change_24h": -1.5,
                "volume": 250000000,
                "market_cap": 75000000000,
            },
        ]
