# Dylan Wave AI Backend

FastAPI backend for the Dylan Wave AI trading platform.

## Quick Start

### Prerequisites
- Python 3.11+
- PostgreSQL 14+
- Redis (optional)

### Installation

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Configuration

Copy `.env.example` to `.env` and update the values:

```bash
cp ../.env.example .env
```

### Database Setup

```bash
alembic upgrade head
```

### Run Development Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

API Documentation: http://localhost:8000/docs

### Run Tests

```bash
pytest
pytest --cov=app tests/
```

### Code Quality

```bash
black .
flake8 .
isort .
```

## Project Structure

- `/app/api` - API route handlers
- `/app/core` - Core configuration (database, security, config)
- `/app/models.py` - SQLAlchemy ORM models
- `/app/schemas.py` - Pydantic schemas for request/response
- `/app/services` - Business logic
- `/app/utils` - Utility functions
- `/app/middleware.py` - Custom middleware
- `/tests` - Test suite
- `main.py` - FastAPI application entry point

## Features

- ✅ FastAPI with async support
- ✅ PostgreSQL with SQLAlchemy ORM
- ✅ JWT authentication
- ✅ Google OAuth 2.0 (ready for integration)
- ✅ CORS middleware
- ✅ Request validation with Pydantic
- ✅ Comprehensive error handling
- ✅ API documentation with Swagger/ReDoc
- ✅ Database migrations with Alembic
- ✅ Unit and integration tests with pytest

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `GET /api/auth/me` - Get current user
- `POST /api/auth/logout` - Logout user

### Users
- `GET /api/users/{user_id}` - Get user profile
- `PUT /api/users/{user_id}` - Update user profile
- `GET /api/users/{user_id}/portfolio` - Get user portfolio

### Trading
- `POST /api/trades` - Create demo trade
- `GET /api/trades` - Get user trades
- `GET /api/trades/{trade_id}` - Get trade details

### Markets
- `GET /api/markets` - Get all markets
- `GET /api/markets/{market_id}` - Get market data
- `GET /api/markets/symbol/{symbol}` - Get market by symbol

## Environment Variables

See `../.env.example` for all available variables.

## Database Models

- `User` - User accounts and profiles
- `Portfolio` - User trading portfolios
- `Trade` - Demo and live trades
- `Market` - Market data cache

## Security

- JWT token-based authentication
- Password hashing with bcrypt
- CORS configuration
- Input validation
- SQL injection prevention via ORM

## Performance

- Async request handling
- Database connection pooling
- Pagination for list endpoints
- Ready for Redis caching

## Deployment

For production deployment:

1. Use environment variables for sensitive data
2. Enable HTTPS
3. Configure CORS properly
4. Use managed database service
5. Implement rate limiting
6. Set up monitoring and logging
