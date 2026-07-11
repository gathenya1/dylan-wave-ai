from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.api import auth, users, trades, markets

# Create FastAPI app
app = FastAPI(
    title="Dylan Wave AI API",
    description="AI-powered trading platform API",
    version="1.0.0",
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

# Health check
@app.get("/health", tags=["Health"])
async def health_check():
    return JSONResponse(status_code=200, content={"status": "ok", "service": "Dylan Wave AI API"})

# Root endpoint
@app.get("/", tags=["Info"])
async def root():
    return JSONResponse(
        status_code=200,
        content={
            "message": "Welcome to Dylan Wave AI API",
            "version": "1.0.0",
            "docs": "/docs",
            "redoc": "/redoc",
        },
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
