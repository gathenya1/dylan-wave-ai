from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

# Auth Schemas
class UserRegister(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=2, max_length=255)
    password: str = Field(..., min_length=6, max_length=255)
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "name": "John Doe",
                "password": "securepassword123"
            }
        }

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "securepassword123"
            }
        }

class UserResponse(BaseModel):
    id: str
    email: str
    name: str
    avatar: Optional[str] = None
    is_verified: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse

# Portfolio Schemas
class PortfolioResponse(BaseModel):
    id: str
    user_id: str
    demo_balance: float
    live_balance: float
    total_value: float
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Trade Schemas
class TradeCreate(BaseModel):
    pair: str
    trade_type: str = Field(..., pattern="^(BUY|SELL)$")
    price: float = Field(..., gt=0)
    amount: float = Field(..., gt=0)
    is_demo: bool = True
    
    class Config:
        json_schema_extra = {
            "example": {
                "pair": "BTC/USD",
                "trade_type": "BUY",
                "price": 43200.50,
                "amount": 0.5,
                "is_demo": True
            }
        }

class TradeResponse(BaseModel):
    id: str
    user_id: str
    pair: str
    trade_type: str
    price: float
    amount: float
    status: str
    profit: Optional[float] = None
    is_demo: bool
    created_at: datetime
    closed_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# Market Schemas
class MarketResponse(BaseModel):
    id: str
    symbol: str
    name: str
    price: float
    change_24h: float
    volume: float
    market_cap: Optional[float] = None
    updated_at: datetime
    
    class Config:
        from_attributes = True

class MarketCreate(BaseModel):
    symbol: str = Field(..., min_length=1, max_length=20)
    name: str = Field(..., min_length=1, max_length=255)
    price: float = Field(..., gt=0)
    change_24h: float
    volume: float = Field(..., ge=0)
    market_cap: Optional[float] = None

# Price History Schemas
class PriceHistoryResponse(BaseModel):
    id: str
    market_id: str
    symbol: str
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    volume: float
    timestamp: datetime
    created_at: datetime
    
    class Config:
        from_attributes = True

class PriceHistoryCreate(BaseModel):
    market_id: str
    symbol: str
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    volume: float
    timestamp: datetime

# Market Snapshot Schemas
class MarketSnapshotResponse(BaseModel):
    id: str
    market_id: str
    symbol: str
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    volume: float
    change_percent: float
    change_amount: float
    timestamp: datetime
    created_at: datetime
    
    class Config:
        from_attributes = True

# Watchlist Schemas
class WatchlistCreate(BaseModel):
    market_id: str
    symbol: str

class WatchlistResponse(BaseModel):
    id: str
    user_id: str
    market_id: str
    symbol: str
    added_at: datetime
    
    class Config:
        from_attributes = True

# Error Response
class ErrorResponse(BaseModel):
    detail: str
    status_code: int

    class Config:
        json_schema_extra = {
            "example": {
                "detail": "Error message",
                "status_code": 400
            }
        }

# WebSocket Message Schemas
class PriceUpdateMessage(BaseModel):
    symbol: str
    price: float
    change_24h: float
    volume: float
    timestamp: datetime
    
    class Config:
        json_schema_extra = {
            "example": {
                "symbol": "BTC",
                "price": 43250.50,
                "change_24h": 2.5,
                "volume": 28500000000,
                "timestamp": "2026-07-11T12:00:00Z"
            }
        }
