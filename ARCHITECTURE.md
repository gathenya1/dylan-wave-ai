# Dylan Wave AI - Architecture Overview

## Project Structure

```
dylan-wave-ai/
├── frontend/              # Next.js 15 React application
├── backend/               # FastAPI Python application
├── docker-compose.yml     # Multi-container orchestration
├── README.md              # Project documentation
├── ARCHITECTURE.md        # This file
└── package.json           # Root workspace configuration
```

## Technology Stack

### Frontend
- **Framework**: Next.js 15 with React 18+
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State Management**: Zustand
- **Charts**: TradingView Lightweight Charts
- **HTTP Client**: Axios or Fetch API
- **Form Handling**: React Hook Form
- **Validation**: Zod

### Backend
- **Framework**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT + Google OAuth 2.0
- **API Documentation**: Swagger/OpenAPI
- **Task Queue**: Celery (optional, for async tasks)
- **Caching**: Redis (optional)

### Infrastructure
- **Containerization**: Docker & Docker Compose
- **Database**: PostgreSQL
- **Reverse Proxy**: Nginx (optional)
- **Environment Management**: dotenv

## Data Flow

### Authentication Flow
1. User initiates login via Google OAuth
2. Frontend redirects to Google consent screen
3. Google returns authorization code
4. Backend exchanges code for tokens
5. Backend creates/updates user record
6. Backend issues JWT token
7. Frontend stores JWT in secure cookie/localStorage
8. Frontend includes JWT in API requests

### Trading Flow
1. User accesses dashboard
2. Frontend requests market data from backend
3. Backend fetches real-time data from external API
4. Backend caches data in Redis (if enabled)
5. Frontend receives data and renders charts
6. User executes demo trade
7. Backend processes trade and updates user portfolio
8. Frontend updates UI in real-time via WebSocket (optional)

## API Endpoints

### Authentication
- `POST /api/auth/login` - Google OAuth login
- `POST /api/auth/logout` - Logout user
- `GET /api/auth/me` - Get current user
- `POST /api/auth/refresh` - Refresh JWT token

### Users
- `GET /api/users/{user_id}` - Get user profile
- `PUT /api/users/{user_id}` - Update user profile
- `GET /api/users/{user_id}/portfolio` - Get user portfolio

### Trading
- `GET /api/markets` - List available markets
- `GET /api/markets/{market_id}/data` - Get market data
- `POST /api/trades` - Create demo trade
- `GET /api/trades` - List user trades
- `GET /api/trades/{trade_id}` - Get trade details

### Admin
- `GET /api/admin/users` - List all users
- `GET /api/admin/trades` - List all trades
- `GET /api/admin/statistics` - Get platform statistics

## Database Schema

### Core Tables
- `users` - User accounts and profiles
- `portfolios` - User trading portfolios
- `trades` - Demo trades history
- `market_data` - Cached market data
- `audit_logs` - System audit trail

## Deployment Architecture

### Development
- Single machine with Docker Compose
- Frontend on port 3000
- Backend on port 8000
- PostgreSQL on port 5432
- Redis on port 6379 (optional)

### Production
- Kubernetes or traditional VPS deployment
- Separate frontend (CDN) and backend (API)
- Managed database service
- Environment-based configuration
- HTTPS/SSL encryption

## Security Considerations

1. **JWT Tokens**: Secure, HTTP-only cookies
2. **CORS**: Configured for allowed origins
3. **Input Validation**: Server-side and client-side
4. **SQL Injection Prevention**: SQLAlchemy ORM
5. **Rate Limiting**: Implement on backend API
6. **HTTPS**: Required in production
7. **Secrets Management**: Environment variables

## Development Workflow

1. Clone repository
2. Copy `.env.example` to `.env` and configure
3. Run `docker-compose up` for services
4. Install frontend dependencies: `cd frontend && npm install`
5. Install backend dependencies: `cd backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
6. Start frontend: `cd frontend && npm run dev`
7. Start backend: `cd backend && uvicorn main:app --reload`

## Phase Implementation

### Phase 1: Foundation (Current)
- Project structure and configuration
- Reusable UI components
- Database models and migrations
- Authentication system
- Basic API endpoints

### Phase 2: Core Features
- Dashboard implementation
- Market data integration
- Demo trading functionality
- Portfolio management
- Real-time updates

### Phase 3: Advanced Features
- AI market analysis
- Advanced charting
- Risk analysis tools
- Admin dashboard
- Notifications system

### Phase 4: Production
- Performance optimization
- Security hardening
- Monitoring and logging
- Deployment automation
- Documentation
