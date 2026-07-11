'use client';

import { useState } from 'react';
import Link from 'next/link';
import { motion } from 'framer-motion';
import AuthForm from '@/components/auth/AuthForm';

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

export default function RegisterPage() {
  const [isLoading, setIsLoading] = useState(false);

  return (
    <div className="min-h-screen flex items-center justify-center px-4 py-12">
      <motion.div
        initial="hidden"
        animate="show"
        variants={container}
        className="w-full max-w-md"
      >
        <motion.div variants={item} className="text-center mb-8">
          <h1 className="text-3xl font-bold mb-2">Dylan Wave AI</h1>
          <p className="text-gray-400">Create your trading account</p>
        </motion.div>

        <motion.div variants={item}>
          <AuthForm type="register" isLoading={isLoading} setIsLoading={setIsLoading} />
        </motion.div>

        <motion.p variants={item} className="text-center mt-6 text-gray-400">
          Already have an account?{' '}
          <Link href="/login" className="text-dylan-primary hover:text-dylan-info transition">
            Sign in
          </Link>
        </motion.p>
      </motion.div>
    </div>
  );
}
