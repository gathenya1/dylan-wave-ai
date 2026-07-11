"""WebSocket connection manager for real-time price updates."""
import logging
from typing import Dict, List, Set
from fastapi import WebSocket
import json
from datetime import datetime

logger = logging.getLogger(__name__)

class ConnectionManager:
    """Manage WebSocket connections for real-time updates."""
    
    def __init__(self):
        # Map of symbol -> set of active connections
        self.active_connections: Dict[str, Set[WebSocket]] = {}
        # Map of connection -> subscribed symbols
        self.subscriptions: Dict[WebSocket, Set[str]] = {}
    
    async def connect(self, websocket: WebSocket, symbol: str) -> None:
        """Connect a WebSocket to a symbol channel."""
        await websocket.accept()
        
        if symbol not in self.active_connections:
            self.active_connections[symbol] = set()
        
        self.active_connections[symbol].add(websocket)
        self.subscriptions[websocket] = self.subscriptions.get(websocket, set())
        self.subscriptions[websocket].add(symbol)
        
        logger.info(f"WebSocket connected to {symbol}. Total connections: {len(self.active_connections[symbol])}")
    
    async def disconnect(self, websocket: WebSocket) -> None:
        """Disconnect a WebSocket and cleanup subscriptions."""
        symbols_to_clean = self.subscriptions.get(websocket, set()).copy()
        
        for symbol in symbols_to_clean:
            if symbol in self.active_connections:
                self.active_connections[symbol].discard(websocket)
                if not self.active_connections[symbol]:
                    del self.active_connections[symbol]
                    logger.info(f"No more connections for {symbol}")
        
        del self.subscriptions[websocket]
        logger.info(f"WebSocket disconnected. Remaining symbols: {list(self.active_connections.keys())}")
    
    async def subscribe(self, websocket: WebSocket, symbol: str) -> None:
        """Subscribe to a symbol channel."""
        if symbol not in self.active_connections:
            self.active_connections[symbol] = set()
        
        self.active_connections[symbol].add(websocket)
        self.subscriptions[websocket].add(symbol)
        
        logger.info(f"Subscribed to {symbol}")
    
    async def unsubscribe(self, websocket: WebSocket, symbol: str) -> None:
        """Unsubscribe from a symbol channel."""
        if symbol in self.active_connections:
            self.active_connections[symbol].discard(websocket)
            if not self.active_connections[symbol]:
                del self.active_connections[symbol]
        
        self.subscriptions[websocket].discard(symbol)
        logger.info(f"Unsubscribed from {symbol}")
    
    async def broadcast_price_update(self, symbol: str, price_data: dict) -> None:
        """Broadcast price update to all connections on a symbol."""
        if symbol not in self.active_connections:
            return
        
        message = {
            "type": "price_update",
            "symbol": symbol,
            "data": price_data,
            "timestamp": datetime.utcnow().isoformat(),
        }
        
        disconnected = []
        for connection in self.active_connections[symbol]:
            try:
                await connection.send_json(message)
            except Exception as e:
                logger.error(f"Error sending message: {e}")
                disconnected.append(connection)
        
        # Clean up disconnected connections
        for connection in disconnected:
            await self.disconnect(connection)
    
    async def broadcast_to_user(self, websocket: WebSocket, message: dict) -> None:
        """Send a message to a specific user."""
        try:
            await websocket.send_json(message)
        except Exception as e:
            logger.error(f"Error sending message to user: {e}")
            await self.disconnect(websocket)
    
    def get_active_symbols(self) -> List[str]:
        """Get list of symbols with active connections."""
        return list(self.active_connections.keys())
    
    def get_connection_count(self, symbol: str) -> int:
        """Get number of active connections for a symbol."""
        return len(self.active_connections.get(symbol, set()))
    
    def get_total_connections(self) -> int:
        """Get total number of active connections."""
        total = 0
        for connections in self.active_connections.values():
            total += len(connections)
        return total

# Global connection manager
manager = ConnectionManager()
