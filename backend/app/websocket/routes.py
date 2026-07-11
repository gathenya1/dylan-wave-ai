"""WebSocket routes for real-time price updates."""
import logging
import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query, HTTPException, status
from typing import Optional

from app.websocket.manager import manager
from app.core.database import SessionLocal
from app.models import Market

logger = logging.getLogger(__name__)
router = APIRouter()

@router.websocket("/ws/market/{symbol}")
async def websocket_market_updates(websocket: WebSocket, symbol: str):
    """WebSocket endpoint for real-time price updates.
    
    Usage:
        ws://localhost:8000/ws/market/BTC
        
    Messages:
        Subscribe:
            {"type": "subscribe", "symbol": "BTC"}
        Unsubscribe:
            {"type": "unsubscribe", "symbol": "BTC"}
        
        Receives:
            {
                "type": "price_update",
                "symbol": "BTC",
                "data": {
                    "price": 43250.50,
                    "change_24h": 2.5,
                    "volume": 28500000000,
                    "updated_at": "2026-07-11T12:00:00Z"
                },
                "timestamp": "2026-07-11T12:00:00Z"
            }
    """
    db = SessionLocal()
    
    try:
        # Verify market exists
        market = db.query(Market).filter(
            Market.symbol.ilike(symbol)
        ).first()
        
        if not market:
            await websocket.close(code=4000, reason="Market not found")
            return
        
        # Connect to the symbol channel
        await manager.connect(websocket, symbol.upper())
        
        # Send initial connection message
        await manager.broadcast_to_user(websocket, {
            "type": "connected",
            "symbol": symbol.upper(),
            "message": f"Connected to {symbol.upper()} price updates",
        })
        
        # Handle incoming messages
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            message_type = message.get("type")
            
            if message_type == "subscribe":
                target_symbol = message.get("symbol", "")
                # Verify symbol exists
                target_market = db.query(Market).filter(
                    Market.symbol.ilike(target_symbol)
                ).first()
                
                if target_market:
                    await manager.subscribe(websocket, target_symbol.upper())
                    await manager.broadcast_to_user(websocket, {
                        "type": "subscribed",
                        "symbol": target_symbol.upper(),
                    })
                else:
                    await manager.broadcast_to_user(websocket, {
                        "type": "error",
                        "message": f"Symbol {target_symbol} not found",
                    })
            
            elif message_type == "unsubscribe":
                target_symbol = message.get("symbol", "")
                await manager.unsubscribe(websocket, target_symbol.upper())
                await manager.broadcast_to_user(websocket, {
                    "type": "unsubscribed",
                    "symbol": target_symbol.upper(),
                })
            
            elif message_type == "ping":
                await manager.broadcast_to_user(websocket, {
                    "type": "pong",
                })
    
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        logger.info(f"Client disconnected from {symbol}")
    
    except json.JSONDecodeError as e:
        await manager.broadcast_to_user(websocket, {
            "type": "error",
            "message": f"Invalid JSON: {str(e)}",
        })
    
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        await manager.disconnect(websocket)
    
    finally:
        db.close()

@router.websocket("/ws/market")
async def websocket_multi_market(websocket: WebSocket):
    """Multi-symbol WebSocket endpoint for price updates.
    
    Usage:
        ws://localhost:8000/ws/market
        
    Messages:
        Subscribe to multiple symbols:
            {"type": "subscribe", "symbols": ["BTC", "ETH", "BNB"]}
        Unsubscribe:
            {"type": "unsubscribe", "symbol": "BTC"}
    """
    db = SessionLocal()
    
    try:
        await websocket.accept()
        
        # Send connection message
        await websocket.send_json({
            "type": "connected",
            "message": "Connected to multi-market price updates",
        })
        
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            message_type = message.get("type")
            
            if message_type == "subscribe":
                symbols = message.get("symbols", [])
                subscribed = []
                
                for symbol in symbols:
                    # Verify symbol exists
                    market = db.query(Market).filter(
                        Market.symbol.ilike(symbol)
                    ).first()
                    
                    if market:
                        await manager.subscribe(websocket, symbol.upper())
                        subscribed.append(symbol.upper())
                
                await websocket.send_json({
                    "type": "subscribed",
                    "symbols": subscribed,
                })
            
            elif message_type == "unsubscribe":
                symbol = message.get("symbol", "")
                await manager.unsubscribe(websocket, symbol.upper())
                await websocket.send_json({
                    "type": "unsubscribed",
                    "symbol": symbol.upper(),
                })
            
            elif message_type == "ping":
                await websocket.send_json({"type": "pong"})
    
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        logger.info("Client disconnected from multi-market")
    
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        await manager.disconnect(websocket)
    
    finally:
        db.close()
