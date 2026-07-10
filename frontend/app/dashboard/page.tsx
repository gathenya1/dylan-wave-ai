'use client';

import { motion } from 'framer-motion';
import Card from '@/components/ui/Card';
import PortfolioCard from '@/components/dashboard/PortfolioCard';
import MarketPreview from '@/components/dashboard/MarketPreview';
import TradeHistory from '@/components/dashboard/TradeHistory';

const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1,
    },
  },
};

const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0, transition: { duration: 0.5 } },
};

export default function Dashboard() {
  return (
    <motion.div
      initial="hidden"
      animate="show"
      variants={container}
      className="space-y-8"
    >
      {/* Header */}
      <motion.div variants={item}>
        <h1 className="text-3xl font-bold">Dashboard</h1>
        <p className="text-gray-400 mt-2">Welcome back to Dylan Wave AI</p>
      </motion.div>

      {/* Stats Grid */}
      <motion.div variants={item} className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Card>
          <div className="p-6">
            <div className="text-sm font-medium text-gray-400 mb-2">Live Balance</div>
            <div className="text-3xl font-bold mb-2">$0.00</div>
            <div className="text-sm text-gray-500">Connected Wallets</div>
          </div>
        </Card>

        <Card>
          <div className="p-6">
            <div className="text-sm font-medium text-gray-400 mb-2">Demo Balance</div>
            <div className="text-3xl font-bold text-dylan-success mb-2">$10,000.00</div>
            <div className="text-sm text-gray-500">Practice Trading</div>
          </div>
        </Card>

        <Card>
          <div className="p-6">
            <div className="text-sm font-medium text-gray-400 mb-2">AI Status</div>
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 bg-dylan-success rounded-full animate-pulse" />
              <span className="font-bold">Active</span>
            </div>
            <div className="text-sm text-gray-500 mt-3">Analyzing markets</div>
          </div>
        </Card>
      </motion.div>

      {/* Portfolio and Markets */}
      <motion.div variants={item} className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2">
          <PortfolioCard />
        </div>
        <div>
          <MarketPreview />
        </div>
      </motion.div>

      {/* Trade History */}
      <motion.div variants={item}>
        <TradeHistory />
      </motion.div>
    </motion.div>
  );
}
