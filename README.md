# Dylan Wave AI

**The Future of Intelligent Trading** 🚀

Dylan Wave AI is a cutting-edge, AI-powered trading platform featuring demo trading, intelligent market analysis, secure wallets, user authentication, and an admin dashboard. Built with modern technologies and designed for scalability, security, and user experience.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Frontend: Next.js 15](https://img.shields.io/badge/Frontend-Next.js_15-black?logo=next.js)](https://nextjs.org)
[![Backend: FastAPI](https://img.shields.io/badge/Backend-FastAPI-009485?logo=fastapi)](https://fastapi.tiangolo.com)
[![Database: PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791?logo=postgresql)](https://www.postgresql.org)
[![Status: Phase 1 Foundation](https://img.shields.io/badge/Status-Phase_1_Foundation-success)](./ARCHITECTURE.md)

## 🎯 Overview

Dylan Wave AI is an innovative trading platform that combines cutting-edge AI technology with an intuitive user interface. Whether you're a seasoned trader or just getting started, Dylan Wave AI provides the tools you need for intelligent trading decisions.

### Key Features

- 🤖 **AI-Powered Analysis** - Machine learning algorithms analyze market trends and provide actionable insights
- 💼 **Demo Trading** - Practice with $10,000 virtual capital without risking real money
- 🔐 **Secure Authentication** - JWT tokens and Google OAuth integration
- 📊 **Live Charts** - Real-time market data with TradingView Lightweight Charts
- 💰 **Wallet Management** - Secure wallet system with multi-currency support
- 👨‍💼 **Admin Dashboard** - Complete platform management and analytics
- 📱 **Responsive Design** - Works seamlessly on desktop, tablet, and mobile

## 🏗️ Project Structure

```
dylan-wave-ai/
├── frontend/                 # Next.js 15 React application
│   ├── app/                  # App router pages
│   ├── components/           # Reusable React components
│   ├── hooks/                # Custom React hooks
│   ├── lib/                  # Utility libraries
│   ├── public/               # Static assets
│   ├── services/             # API service layer
│   ├── store/                # Zustand state management
│   ├── styles/               # Global styles
│   ├── types/                # TypeScript types
│   └── utils/                # Helper functions
│
├── backend/                  # FastAPI Python application
│   ├── app/
│   │   ├── api/              # API route handlers
│   │   ├── core/             # Configuration & security
│   │   ├── models.py         # SQLAlchemy ORM models
│   │   ├── schemas.py        # Pydantic validation schemas
│   │   ├── services/         # Business logic
│   │   ├── utils/            # Utilities
│   │   └── middleware.py     # Custom middleware
│   ├── tests/                # Test suite
│   ├── main.py               # Application entry point
│   └── requirements.txt      # Python dependencies
│
├── docker-compose.yml        # Multi-container orchestration
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore rules
├── README.md                 # This file
├── ARCHITECTURE.md           # System architecture documentation
├── DEVELOPMENT.md            # Development guide
└── LICENSE                   # MIT License
```

## 🚀 Quick Start

### Prerequisites

- **Docker & Docker Compose** (recommended)
- **Node.js 18+** (for local frontend development)
- **Python 3.11+** (for local backend development)
- **PostgreSQL 14+** (for local database)

### Using Docker Compose (Recommended)

1. **Clone the Repository**
   ```bash
   git clone https://github.com/gathenya1/dylan-wave-ai.git
   cd dylan-wave-ai
   ```

2. **Configure Environment**
   ```bash
   cp .env.example .env
   ```

3. **Build and Start Services**
   ```bash
   docker compose up --build
   ```

4. **Access the Application**
   - **Frontend**: http://localhost:3000
   - **Backend API**: http://localhost:8000
   - **API Docs**: http://localhost:8000/docs
   - **Database UI**: http://localhost:8080 (Adminer)

### Manual Setup (Local Development)

#### Frontend

```bash
cd frontend
npm install
npm run dev
# Open http://localhost:3000
```

#### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
# Open http://localhost:8000/docs
```

## 💻 Technology Stack

### Frontend
- **Next.js 15** - React framework with App Router
- **React 19** - UI library
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework
- **Zustand** - State management
- **Framer Motion** - Animation library
- **React Hook Form** - Form handling
- **Zod** - Schema validation
- **TradingView Lightweight Charts** - Advanced charting
- **Axios** - HTTP client

### Backend
- **FastAPI** - Modern async Python web framework
- **PostgreSQL** - Relational database
- **SQLAlchemy** - ORM
- **Alembic** - Database migrations
- **Pydantic** - Data validation
- **JWT** - Authentication tokens
- **bcrypt** - Password hashing
- **Pytest** - Testing framework

### Infrastructure
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **PostgreSQL** - Database server
- **Redis** - Caching and sessions
- **Nginx** - Reverse proxy (production)

## 📚 Documentation

- **[ARCHITECTURE.md](./ARCHITECTURE.md)** - System architecture and design
- **[DEVELOPMENT.md](./DEVELOPMENT.md)** - Development setup and workflow
- **[Frontend README](./frontend/README.md)** - Frontend-specific documentation
- **[Backend README](./backend/README.md)** - Backend-specific documentation

## 🔄 Development Workflow

### Using Docker Compose

```bash
# Start all services
docker compose up

# Stop all services
docker compose down

# View logs
docker compose logs -f backend
docker compose logs -f frontend

# Run migrations
docker compose exec backend alembic upgrade head

# Run tests
docker compose exec backend pytest
```

### Git Workflow

1. Create feature branch: `git checkout -b feature/feature-name`
2. Make changes and commit: `git commit -m "Description"`
3. Push to remote: `git push origin feature/feature-name`
4. Create Pull Request on GitHub
5. Code review and merge to main

## 🧪 Testing

### Frontend Tests
```bash
cd frontend
npm run test
```

### Backend Tests
```bash
cd backend
pytest
pytest --cov=app tests/  # With coverage
```

## 📊 API Endpoints

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

## 🔐 Security

- JWT token-based authentication
- Password hashing with bcrypt
- CORS configuration
- Input validation on server and client
- SQL injection prevention via ORM
- Environment-based secrets management
- HTTPS ready for production

## 📈 Project Phases

### Phase 1: Foundation ✅
- Project structure and configuration
- Frontend with Next.js 15 and React 19
- Backend with FastAPI
- Database models
- Authentication system
- Basic API endpoints
- Docker setup

### Phase 2: Core Features (Coming)
- Dashboard implementation
- Market data integration
- Demo trading functionality
- Portfolio management
- Real-time updates (WebSocket)

### Phase 3: Advanced Features (Coming)
- AI market analysis
- Advanced charting
- Risk analysis tools
- Admin dashboard
- Notifications system

### Phase 4: Production (Coming)
- Performance optimization
- Security hardening
- Monitoring and logging
- Deployment automation
- Production documentation

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write/update tests
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 👥 Team

- **Dylan Wave AI** - AI-powered trading platform by the community

## 🙏 Acknowledgments

- Next.js team for the amazing framework
- FastAPI creators for the high-performance web framework
- PostgreSQL community for the robust database
- All contributors and supporters

## 📞 Support

For questions and support:
- Open an issue on GitHub
- Check existing documentation
- Review the development guide

## 🎉 Getting Started

Ready to start trading? Follow the **[Quick Start](#-quick-start)** section above!

---

**Made with ❤️ for traders everywhere**
