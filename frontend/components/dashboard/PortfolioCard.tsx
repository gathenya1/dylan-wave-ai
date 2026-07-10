'use client';

import Card from '@/components/ui/Card';
import { motion } from 'framer-motion';

export default function PortfolioCard() {
  const portfolio = [
    { symbol: 'BTC', name: 'Bitcoin', amount: 0.5, value: 21500, change: 5.2 },
    { symbol: 'ETH', name: 'Ethereum', amount: 5, value: 9500, change: 3.8 },
    { symbol: 'SOL', name: 'Solana', amount: 20, value: 4200, change: -2.1 },
  ];

  return (
    <Card>
      <div className="p-6">
        <h3 className="text-xl font-bold mb-6">Portfolio</h3>

        <div className="space-y-4">
          {portfolio.map((asset, index) => (
            <motion.div
              key={asset.symbol}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.1 }}
              className="flex items-center justify-between p-4 bg-dylan-bg/50 rounded-lg hover:bg-dylan-bg transition"
            >
              <div>
                <div className="font-semibold">{asset.symbol}</div>
                <div className="text-sm text-gray-400">{asset.amount} {asset.symbol}</div>
              </div>
              <div className="text-right">
                <div className="font-semibold">${asset.value.toLocaleString()}</div>
                <div className={`text-sm ${
                  asset.change >= 0 ? 'text-dylan-success' : 'text-dylan-danger'
                }`}>
                  {asset.change >= 0 ? '+' : ''}{asset.change}%
                </div>
              </div>
            </motion.div>
          ))}
        </div>

        <div className="mt-6 pt-6 border-t border-dylan-primary/10">
          <div className="flex justify-between items-center">
            <span className="text-gray-400">Total Value</span>
            <span className="text-2xl font-bold text-dylan-success">$35,200.00</span>
          </div>
        </div>
      </div>
    </Card>
  );
}
