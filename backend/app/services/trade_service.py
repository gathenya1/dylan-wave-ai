"""Trade service for trade operations."""
from typing import Optional

class TradeService:
    """Service for trade operations."""
    
    @staticmethod
    def calculate_profit(entry_price: float, exit_price: float, amount: float, trade_type: str) -> float:
        """Calculate profit/loss for a trade."""
        if trade_type == "BUY":
            profit = (exit_price - entry_price) * amount
        else:  # SELL
            profit = (entry_price - exit_price) * amount
        return profit
    
    @staticmethod
    def calculate_roi(profit: float, investment: float) -> float:
        """Calculate return on investment percentage."""
        if investment == 0:
            return 0.0
        return (profit / investment) * 100
