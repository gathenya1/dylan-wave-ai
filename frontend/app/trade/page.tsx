'use client';

import { motion } from 'framer-motion';
import Card from '@/components/ui/Card';

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

export default function TradePage() {
  return (
    <motion.div
      initial="hidden"
      animate="show"
      variants={container}
      className="space-y-8"
    >
      <motion.div variants={item}>
        <h1 className="text-3xl font-bold">Trade</h1>
        <p className="text-gray-400 mt-2">Execute demo trades with AI insights</p>
      </motion.div>

      <motion.div variants={item}>
        <Card>
          <div className="p-8 text-center">
            <div className="text-6xl mb-4">📊</div>
            <h2 className="text-2xl font-bold mb-4">Trading Platform</h2>
            <p className="text-gray-400">Coming soon - Advanced trading interface with real-time charts</p>
          </div>
        </Card>
      </motion.div>
    </motion.div>
  );
}
