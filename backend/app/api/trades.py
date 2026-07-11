from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
import uuid

from app.core.database import get_db
from app.core.security import get_current_user
from app.models import Trade, Portfolio
from app.schemas import TradeCreate, TradeResponse

router = APIRouter()

@router.post("", response_model=TradeResponse, status_code=status.HTTP_201_CREATED)
async def create_trade(
    trade_data: TradeCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new demo trade."""
    user_id = current_user["user_id"]
    
    # Get user's portfolio
    portfolio = db.query(Portfolio).filter(Portfolio.user_id == user_id).first()
    if not portfolio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Portfolio not found"
        )
    
    # Validate balance for demo trades
    trade_cost = trade_data.price * trade_data.amount
    if trade_data.is_demo and trade_cost > portfolio.demo_balance:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient demo balance"
        )
    
    # Create trade
    trade = Trade(
        id=str(uuid.uuid4()),
        user_id=user_id,
        pair=trade_data.pair,
        trade_type=trade_data.trade_type,
        price=trade_data.price,
        amount=trade_data.amount,
        is_demo=trade_data.is_demo,
    )
    
    # Update portfolio balance
    if trade_data.is_demo:
        if trade_data.trade_type == "BUY":
            portfolio.demo_balance -= trade_cost
        # For SELL, we'd need to check if user has the asset (simplified for now)
    
    db.add(trade)
    db.commit()
    db.refresh(trade)
    
    return TradeResponse.model_validate(trade)

@router.get("", response_model=list[TradeResponse])
async def get_user_trades(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 50
):
    """Get user's trades with pagination."""
    trades = db.query(Trade).filter(
        Trade.user_id == current_user["user_id"]
    ).order_by(
        Trade.created_at.desc()
    ).offset(skip).limit(limit).all()
    
    return [TradeResponse.model_validate(t) for t in trades]

@router.get("/{trade_id}", response_model=TradeResponse)
async def get_trade(
    trade_id: str,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get specific trade."""
    trade = db.query(Trade).filter(
        Trade.id == trade_id,
        Trade.user_id == current_user["user_id"]
    ).first()
    
    if not trade:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Trade not found"
        )
    
    return TradeResponse.model_validate(trade)
