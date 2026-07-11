'use client';

import Card from '@/components/ui/Card';
import { motion } from 'framer-motion';

export default function MarketPreview() {
  const markets = [
    { symbol: 'BTC/USD', price: 43200, change: 2.5 },
    { symbol: 'ETH/USD', price: 1900, change: 1.2 },
    { symbol: 'SOL/USD', price: 210, change: -1.5 },
  ];

  return (
    <Card>
      <div className="p-6">
        <h3 className="text-xl font-bold mb-6">Top Markets</h3>

        <div className="space-y-3">
          {markets.map((market, index) => (
            <motion.div
              key={market.symbol}
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1 }}
              className="flex items-center justify-between p-3 bg-dylan-bg/50 rounded-lg hover:bg-dylan-bg transition"
            >
              <span className="font-medium text-sm">{market.symbol}</span>
              <div className="text-right">
                <div className="font-semibold text-sm">${market.price.toLocaleString()}</div>
                <div className={`text-xs ${
                  market.change >= 0 ? 'text-dylan-success' : 'text-dylan-danger'
                }`}>
                  {market.change >= 0 ? '↑' : '↓'} {Math.abs(market.change)}%
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </Card>
  );
}
