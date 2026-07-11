"""Middleware for logging and request/response handling."""
from fastapi import Request
import time

class LoggingMiddleware:
    """Middleware for logging requests and responses."""
    
    def __init__(self, app):
        self.app = app
    
    async def __call__(self, request: Request, call_next):
        start_time = time.time()
        
        # Log request
        print(f"[{request.method}] {request.url.path} - {request.client.host}")
        
        response = await call_next(request)
        
        # Log response
        duration = time.time() - start_time
        print(f"[{response.status_code}] {request.url.path} - {duration:.2f}s")
        
        return response
