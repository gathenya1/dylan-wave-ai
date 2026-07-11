import os
from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App
    APP_NAME: str = "Dylan Wave AI"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    
    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/dylan_wave_ai"
    DATABASE_TEST_URL: str = "postgresql://user:password@localhost:5432/dylan_wave_ai_test"
    
    # JWT
    JWT_SECRET_KEY: str = "your-super-secret-jwt-key-change-this-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24
    
    # Google OAuth
    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""
    GOOGLE_REDIRECT_URI: str = "http://localhost:3000/auth/callback/google"
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:3001"]
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
