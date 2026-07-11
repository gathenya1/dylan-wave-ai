from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
import uuid
from datetime import timedelta

from app.core.database import get_db
from app.core.security import SecurityUtils, get_current_user
from app.models import User, Portfolio
from app.schemas import UserRegister, UserLogin, AuthResponse, UserResponse

router = APIRouter()

@router.post("/register", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserRegister, db: Session = Depends(get_db)):
    """Register a new user."""
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user
    user_id = str(uuid.uuid4())
    user = User(
        id=user_id,
        email=user_data.email,
        name=user_data.name,
        password_hash=SecurityUtils.hash_password(user_data.password),
    )
    
    # Create portfolio for user
    portfolio = Portfolio(
        id=str(uuid.uuid4()),
        user_id=user_id,
        demo_balance=10000.0,
        live_balance=0.0,
        total_value=10000.0,
    )
    
    db.add(user)
    db.add(portfolio)
    db.commit()
    db.refresh(user)
    
    # Generate token
    access_token = SecurityUtils.create_access_token(
        data={"sub": user.id, "email": user.email}
    )
    
    return AuthResponse(
        access_token=access_token,
        user=UserResponse.model_validate(user)
    )

@router.post("/login", response_model=AuthResponse)
async def login(credentials: UserLogin, db: Session = Depends(get_db)):
    """Login user."""
    # Find user by email
    user = db.query(User).filter(User.email == credentials.email).first()
    
    if not user or not SecurityUtils.verify_password(credentials.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive"
        )
    
    # Generate token
    access_token = SecurityUtils.create_access_token(
        data={"sub": user.id, "email": user.email}
    )
    
    return AuthResponse(
        access_token=access_token,
        user=UserResponse.model_validate(user)
    )

@router.get("/me", response_model=UserResponse)
async def get_current_user_info(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get current user information."""
    user = db.query(User).filter(User.id == current_user["user_id"]).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return UserResponse.model_validate(user)

@router.post("/logout", status_code=status.HTTP_200_OK)
async def logout(current_user: dict = Depends(get_current_user)):
    """Logout user (token invalidation handled on frontend)."""
    return {"message": "Logged out successfully"}
