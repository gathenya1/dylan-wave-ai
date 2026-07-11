export interface User {
  id: string;
  email: string;
  name: string;
  avatar?: string;
  createdAt: Date;
}

export interface Portfolio {
  id: string;
  userId: string;
  assets: Asset[];
  totalValue: number;
  updatedAt: Date;
}

export interface Asset {
  id: string;
  symbol: string;
  amount: number;
  purchasePrice: number;
  currentPrice: number;
}

export interface Trade {
  id: string;
  userId: string;
  pair: string;
  type: 'BUY' | 'SELL';
  price: number;
  amount: number;
  date: Date;
  status: 'OPEN' | 'CLOSED';
  profit?: number;
}

export interface Market {
  id: string;
  symbol: string;
  name: string;
  price: number;
  change24h: number;
  volume: number;
  marketCap: number;
}

export interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
  message?: string;
}

export interface AuthResponse {
  token: string;
  user: User;
}
