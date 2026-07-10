# Dylan Wave AI - Development Guide

## Quick Start

### Prerequisites
- Node.js 18+ (for frontend)
- Python 3.11+ (for backend)
- Docker & Docker Compose
- PostgreSQL 14+
- Git

### Setup

1. **Clone and Setup Environment**
   ```bash
   git clone https://github.com/gathenya1/dylan-wave-ai.git
   cd dylan-wave-ai
   cp .env.example .env
   ```

2. **Using Docker Compose (Recommended)**
   ```bash
   docker-compose up -d
   ```

3. **Manual Setup**

   **Frontend:**
   ```bash
   cd frontend
   npm install
   npm run dev
   # Open http://localhost:3000
   ```

   **Backend:**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   # Open http://localhost:8000/docs
   ```

## Development Commands

### Frontend
```bash
cd frontend

# Development server
npm run dev

# Build for production
npm run build

# Run production build
npm start

# Linting
npm run lint

# Type checking
npm run type-check

# Format code
npm run format
```

### Backend
```bash
cd backend
source venv/bin/activate

# Development server with auto-reload
uvicorn main:app --reload

# Run tests
pytest

# Lint and format
flake8 .
black .

# Database migrations
alembic revision --autogenerate -m "description"
alembic upgrade head
```

## Project Structure Details

### Frontend (`frontend/`)
```
frontend/
├── app/                    # Next.js app directory
│   ├── layout.tsx         # Root layout with Dylan Wave AI branding
│   ├── page.tsx           # Home page
│   ├── dashboard/         # Dashboard routes
│   ├── auth/              # Authentication routes
│   ├── admin/             # Admin routes
│   └── api/               # Next.js API routes (optional)
├── components/            # Reusable React components
│   ├── common/           # Common components (Header, Footer, etc.)
│   ├── auth/             # Authentication components
│   ├── dashboard/        # Dashboard components
│   ├── charts/           # Chart components
│   └── ui/               # UI elements (Button, Input, etc.)
├── hooks/                # Custom React hooks
├── stores/               # Zustand state management
├── types/                # TypeScript type definitions
├── styles/               # Global styles
├── utils/                # Utility functions
├── lib/                  # External library integrations
├── public/               # Static assets
├── next.config.js        # Next.js configuration
├── tsconfig.json         # TypeScript configuration
├── tailwind.config.js    # Tailwind CSS configuration
└── package.json          # Dependencies
```

### Backend (`backend/`)
```
backend/
├── app/
│   ├── api/              # API route handlers
│   │   ├── auth/        # Authentication endpoints
│   │   ├── users/       # User endpoints
��   │   ├── trades/      # Trading endpoints
│   │   ├── markets/     # Market data endpoints
│   │   └── admin/       # Admin endpoints
│   ├── models/          # SQLAlchemy ORM models
│   ├── schemas/         # Pydantic request/response schemas
│   ├── services/        # Business logic
│   ├── middleware/      # Custom middleware
│   ├── utils/           # Utility functions
│   ├── core/            # Core configuration
│   │   ├── config.py    # App configuration
│   │   ├── security.py  # JWT and security
│   │   └── database.py  # Database setup
│   └── __init__.py
├── migrations/          # Alembic database migrations
├── tests/               # Test suite
├── main.py              # FastAPI app entry point
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (local)
└── alembic.ini          # Alembic configuration
```

## Database Setup

### Create Database
```bash
# Via Docker Compose (automatic)
docker-compose up postgres

# Manual with PostgreSQL CLI
psql -U postgres
CREATE DATABASE dylan_wave_ai;
CREATE DATABASE dylan_wave_ai_test;
```

### Run Migrations
```bash
cd backend
alembic upgrade head
```

### Reset Database
```bash
alembic downgrade base  # Reset to initial state
alembic upgrade head    # Apply all migrations
```

## Environment Variables

See `.env.example` for all available variables. Key ones:

- `DATABASE_URL` - PostgreSQL connection string
- `JWT_SECRET_KEY` - Secret key for JWT tokens
- `GOOGLE_CLIENT_ID` - Google OAuth client ID
- `GOOGLE_CLIENT_SECRET` - Google OAuth client secret
- `NEXT_PUBLIC_API_URL` - Backend API URL (visible to frontend)

## Debugging

### Frontend
- Chrome DevTools: `F12` or `Cmd+Option+I`
- React DevTools browser extension
- Console logs: `console.log()`, `console.error()`
- Network tab: Check API requests/responses

### Backend
- FastAPI Swagger UI: `http://localhost:8000/docs`
- FastAPI ReDoc: `http://localhost:8000/redoc`
- Print debugging: `print()` statements
- Logging: Use Python `logging` module
- Breakpoints: Use `pdb` debugger

## Testing

### Frontend
```bash
cd frontend
npm run test
```

### Backend
```bash
cd backend
pytest
pytest --cov=app tests/  # With coverage
```

## Code Style

### Frontend
- ESLint configuration: `.eslintrc.json`
- Prettier configuration: `.prettierrc`
- TypeScript strict mode enabled

### Backend
- Black formatter
- Flake8 linter
- isort for import sorting

## Troubleshooting

### Port Already in Use
```bash
# Frontend (3000)
lsof -i :3000
kill -9 <PID>

# Backend (8000)
lsof -i :8000
kill -9 <PID>
```

### Database Connection Issues
- Check `DATABASE_URL` in `.env`
- Verify PostgreSQL is running
- Check database credentials
- Review server logs

### Module Not Found
```bash
# Frontend
rm -rf node_modules package-lock.json
npm install

# Backend
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Git Workflow

1. Create feature branch: `git checkout -b feature/feature-name`
2. Make changes and commit: `git commit -m "Description"`
3. Push to remote: `git push origin feature/feature-name`
4. Create Pull Request on GitHub
5. Code review and merge to main

## Performance Tips

- Frontend: Use React.memo for expensive components
- Backend: Add database indexes for frequently queried fields
- Caching: Implement Redis caching for market data
- Images: Optimize and use Next.js Image component
- API: Implement pagination for large datasets

## Security Reminders

- Never commit `.env` file with real secrets
- Always use HTTPS in production
- Validate and sanitize user inputs
- Keep dependencies updated: `npm audit`, `pip audit`
- Use environment variables for sensitive data
- Implement rate limiting on backend

## Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Zustand Documentation](https://github.com/pmndrs/zustand)
- [TradingView Lightweight Charts](https://www.tradingview.com/lightweight-charts/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
