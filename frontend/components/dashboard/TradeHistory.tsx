'use client';

import Card from '@/components/ui/Card';
import { motion } from 'framer-motion';

export default function TradeHistory() {
  const trades = [
    {
      id: '1',
      pair: 'BTC/USD',
      type: 'BUY',
      price: 42000,
      amount: 0.1,
      date: '2024-01-15 14:30',
      status: 'CLOSED',
      profit: 1200,
    },
    {
      id: '2',
      pair: 'ETH/USD',
      type: 'SELL',
      price: 1850,
      amount: 2,
      date: '2024-01-15 13:45',
      status: 'CLOSED',
      profit: -150,
    },
  ];

  return (
    <Card>
      <div className="p-6">
        <h3 className="text-xl font-bold mb-6">Recent Trades</h3>

        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b border-dylan-primary/10 text-gray-400">
                <th className="text-left py-3 px-4">Pair</th>
                <th className="text-left py-3 px-4">Type</th>
                <th className="text-right py-3 px-4">Price</th>
                <th className="text-right py-3 px-4">Amount</th>
                <th className="text-left py-3 px-4">Date</th>
                <th className="text-right py-3 px-4">P&L</th>
              </tr>
            </thead>
            <tbody>
              {trades.map((trade, index) => (
                <motion.tr
                  key={trade.id}
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  transition={{ delay: index * 0.1 }}
                  className="border-b border-dylan-primary/10 hover:bg-dylan-surface/50 transition"
                >
                  <td className="py-4 px-4 font-medium">{trade.pair}</td>
                  <td className="py-4 px-4">
                    <span className={`px-2 py-1 rounded text-xs font-semibold ${
                      trade.type === 'BUY'
                        ? 'bg-dylan-success/20 text-dylan-success'
                        : 'bg-dylan-danger/20 text-dylan-danger'
                    }`}>
                      {trade.type}
                    </span>
                  </td>
                  <td className="py-4 px-4 text-right">${trade.price.toLocaleString()}</td>
                  <td className="py-4 px-4 text-right">{trade.amount}</td>
                  <td className="py-4 px-4">{trade.date}</td>
                  <td className={`py-4 px-4 text-right font-semibold ${
                    trade.profit >= 0 ? 'text-dylan-success' : 'text-dylan-danger'
                  }`}>
                    ${Math.abs(trade.profit).toLocaleString()}
                  </td>
                </motion.tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </Card>
  );
}
