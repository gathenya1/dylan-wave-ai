# Dylan Wave AI - Frontend

Next.js 15 frontend for the Dylan Wave AI trading platform.

## Quick Start

### Prerequisites
- Node.js 18+
- npm or yarn

### Installation

```bash
npm install
```

### Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

### Build

```bash
npm run build
npm start
```

### Linting

```bash
npm run lint
npm run format
```

## Project Structure

- `/app` - Next.js app directory with routes
- `/components` - Reusable React components
- `/lib` - Utility libraries
- `/public` - Static assets
- `/styles` - Global styles
- `/types` - TypeScript types
- `/utils` - Helper functions

## Features

- ✅ Next.js 15 with App Router
- ✅ React 19 with TypeScript
- ✅ Tailwind CSS
- ✅ Zustand for state management
- ✅ Framer Motion for animations
- ✅ React Hook Form for forms
- ✅ Zod for validation
- ✅ Dark theme with Dylan Wave AI branding
- ✅ Responsive design
- ✅ Accessible components

## Available Routes

- `/` - Landing page
- `/login` - Login page
- `/register` - Registration page
- `/dashboard` - Main dashboard
- `/trade` - Trading interface
- `/wallet` - Wallet management
- `/history` - Trade history
- `/profile` - User profile

## Styling

Tailwind CSS with custom Dylan Wave AI theme:
- Primary: Royal Blue (#1e40af)
- Background: Dark Navy (#0f172a)
- Success: Emerald Green (#10b981)
- Danger: Red (#ef4444)

## State Management

Zustand stores in `/store` directory.

## API Integration

Axios client with interceptors in `/utils/api.ts`

Base URL: `http://localhost:8000/api`
