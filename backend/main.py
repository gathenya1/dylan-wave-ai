from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging

from app.core.config import settings
from app.api import auth, users, trades, markets
from app.api import market_data
from app.websocket import routes as ws_routes
from app.services.price_scheduler import PriceScheduler
import asyncio

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Dylan Wave AI API",
    description="AI-powered trading platform API",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routes
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(trades.router, prefix="/api/trades", tags=["Trades"])
app.include_router(markets.router, prefix="/api/markets", tags=["Markets"])
app.include_router(market_data.router, prefix="/api/market-data", tags=["Market Data"])
app.include_router(ws_routes.router, tags=["WebSocket"])

# Health check
@app.get("/health", tags=["Health"])
async def health_check():
    return JSONResponse(
        status_code=200,
        content={
            "status": "ok",
            "service": "Dylan Wave AI API",
            "version": "2.0.0",
        }
    )

# Root endpoint
@app.get("/", tags=["Info"])
async def root():
    return JSONResponse(
        status_code=200,
        content={
            "message": "Welcome to Dylan Wave AI API",
            "version": "2.0.0",
            "docs": "/docs",
            "redoc": "/redoc",
            "features": [
                "Authentication & Authorization",
                "User Management",
                "Trading Engine",
                "Market Data with Real-time Updates",
                "WebSocket Support",
                "Price Tracking",
                "Watchlist Management",
            ],
        },
    )

# Startup event
@app.on_event("startup")
async def startup_event():
    logger.info("Dylan Wave AI API starting up...")
    # Start price scheduler
    # asyncio.create_task(PriceScheduler.start(interval=60))
    logger.info("API startup complete")

# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Dylan Wave AI API shutting down...")
    await PriceScheduler.stop()
    logger.info("API shutdown complete")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
