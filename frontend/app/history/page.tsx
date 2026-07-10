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

export default function HistoryPage() {
  return (
    <motion.div
      initial="hidden"
      animate="show"
      variants={container}
      className="space-y-8"
    >
      <motion.div variants={item}>
        <h1 className="text-3xl font-bold">Trade History</h1>
        <p className="text-gray-400 mt-2">View all your trading activity</p>
      </motion.div>

      <motion.div variants={item}>
        <Card>
          <div className="p-8 text-center">
            <div className="text-6xl mb-4">📈</div>
            <h2 className="text-2xl font-bold mb-4">Trade History</h2>
            <p className="text-gray-400">Coming soon - Detailed trade analytics and reports</p>
          </div>
        </Card>
      </motion.div>
    </motion.div>
  );
}
