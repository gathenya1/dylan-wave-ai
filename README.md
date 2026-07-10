# Dylan Wave AI - AI-Powered Trading Platform

A professional-grade AI trading platform built with modern technologies.

## Tech Stack

- **Frontend**: Next.js 15 + React 19 + TypeScript
- **Styling**: Tailwind CSS
- **Backend**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT + Google OAuth
- **Charts**: TradingView Lightweight Charts
- **State Management**: Zustand
- **Deployment**: Vercel (Frontend) + Railway (Backend)

## Project Structure

```
dylan-wave-ai/
├── frontend/                 # Next.js application
├── backend/                  # FastAPI application
├── database/                 # Database migrations and schemas
├── docs/                     # Project documentation
├── .github/                  # GitHub Actions workflows
└── docker-compose.yml        # Docker configuration
```

## Getting Started

### Prerequisites

- Node.js 18+ (Frontend)
- Python 3.11+ (Backend)
- PostgreSQL 15+
- Docker & Docker Compose (optional)

### Frontend Setup

```bash
cd frontend
npm install
cp .env.example .env.local
npm run dev
```

Frontend will be available at `http://localhost:3000`

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
uvicorn main:app --reload
```

Backend will be available at `http://localhost:8000`

### Database Setup with Docker

```bash
docker-compose up -d postgresql
```

## Development

### Code Quality

- **Linting**: ESLint (Frontend), Flake8 (Backend)
- **Formatting**: Prettier (Frontend), Black (Backend)
- **Type Checking**: TypeScript (Frontend), Mypy (Backend)

### Running Linters

**Frontend**:
```bash
cd frontend
npm run lint
npm run format
```

**Backend**:
```bash
cd backend
flake8 .
black .
```

## Features

### Authentication
- JWT-based authentication
- Google OAuth integration
- Two-Factor Authentication (2FA) framework
- Password hashing with bcrypt

### Dashboard
- Demo account with $10,000 virtual balance
- Live account support
- Real-time portfolio tracking
- AI trading status
- Open trades monitoring
- Trade history

### AI Trading
- Configurable trading strategies
- User-defined risk settings
- AI confidence metrics
- Take profit and stop loss controls
- Daily loss limits
- Multiple market support (Volatility indices, Forex, Crypto)

### Wallet
- M-Pesa integration
- Bank transfer support
- Cryptocurrency support
- Transaction history
- Secure fund management

### Admin Dashboard
- User management
- KYC verification
- Deposit/withdrawal monitoring
- Analytics and reporting
- Platform settings
- Notification management

## API Documentation

API documentation available at `http://localhost:8000/docs` (Swagger UI)

## Environment Variables

See `.env.example` files in `frontend/` and `backend/` directories.

## CI/CD

GitHub Actions workflows automatically:
- Run linting and type checks
- Execute tests
- Build Docker images
- Deploy to staging/production

## Security

- JWT token validation
- Password encryption (bcrypt)
- CORS configuration
- Rate limiting
- SQL injection prevention (SQLAlchemy ORM)
- XSS protection (Next.js)

## Deployment

### Frontend (Vercel)

1. Connect GitHub repository to Vercel
2. Set environment variables
3. Deploy with `vercel deploy`

### Backend (Railway)

1. Connect GitHub repository to Railway
2. Set environment variables
3. Configure PostgreSQL addon
4. Deploy automatically on push

## License

MIT License

## Support

For issues and questions, please open a GitHub issue.
