from sqlalchemy import Column, String, DateTime, Boolean, Float
from sqlalchemy.sql import func
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(String(36), primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)
    avatar = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    google_id = Column(String(255), unique=True, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

class Portfolio(Base):
    __tablename__ = "portfolios"
    
    id = Column(String(36), primary_key=True, index=True)
    user_id = Column(String(36), nullable=False, index=True)
    demo_balance = Column(Float, default=10000.0, nullable=False)
    live_balance = Column(Float, default=0.0, nullable=False)
    total_value = Column(Float, default=10000.0, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

class Trade(Base):
    __tablename__ = "trades"
    
    id = Column(String(36), primary_key=True, index=True)
    user_id = Column(String(36), nullable=False, index=True)
    pair = Column(String(20), nullable=False)
    trade_type = Column(String(10), nullable=False)  # BUY or SELL
    price = Column(Float, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String(20), default="OPEN", nullable=False)  # OPEN or CLOSED
    profit = Column(Float, nullable=True)
    is_demo = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    closed_at = Column(DateTime(timezone=True), nullable=True)

class Market(Base):
    __tablename__ = "markets"
    
    id = Column(String(36), primary_key=True, index=True)
    symbol = Column(String(20), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    change_24h = Column(Float, nullable=False)
    volume = Column(Float, nullable=False)
    market_cap = Column(Float, nullable=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
