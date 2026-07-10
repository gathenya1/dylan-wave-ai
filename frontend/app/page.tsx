'use client';

import Link from 'next/link';
import { motion } from 'framer-motion';
import Button from '@/components/ui/Button';
import Navbar from '@/components/common/Navbar';
import Footer from '@/components/common/Footer';

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

export default function Home() {
  return (
    <>
      <Navbar />
      <main className="flex-1">
        {/* Hero Section */}
        <motion.section
          initial="hidden"
          whileInView="show"
          viewport={{ once: true }}
          variants={container}
          className="relative py-24 px-4 sm:px-6 lg:px-8 overflow-hidden"
        >
          <div className="absolute inset-0 overflow-hidden">
            <div className="absolute -top-40 -right-40 w-80 h-80 bg-dylan-primary opacity-20 rounded-full blur-3xl" />
            <div className="absolute -bottom-40 -left-40 w-80 h-80 bg-dylan-info opacity-20 rounded-full blur-3xl" />
          </div>

          <div className="relative max-w-6xl mx-auto text-center">
            <motion.h1
              variants={item}
              className="text-5xl sm:text-6xl font-bold mb-6 bg-gradient-to-r from-dylan-primary via-dylan-info to-dylan-success bg-clip-text text-transparent"
            >
              Dylan Wave AI
            </motion.h1>

            <motion.p
              variants={item}
              className="text-xl sm:text-2xl text-gray-300 mb-8 max-w-2xl mx-auto"
            >
              The future of trading is intelligent, secure, and accessible to everyone
            </motion.p>

            <motion.p
              variants={item}
              className="text-lg text-gray-400 mb-12 max-w-2xl mx-auto"
            >
              Experience AI-powered market analysis, demo trading with $10,000 virtual capital, and
              intelligent portfolio management.
            </motion.p>

            <motion.div
              variants={item}
              className="flex flex-col sm:flex-row gap-4 justify-center"
            >
              <Link href="/dashboard">
                <Button variant="primary" size="lg" className="w-full sm:w-auto">
                  Start Trading Now
                </Button>
              </Link>
              <Link href="/login">
                <Button variant="secondary" size="lg" className="w-full sm:w-auto">
                  Sign In
                </Button>
              </Link>
            </motion.div>
          </div>
        </motion.section>

        {/* Features Section */}
        <motion.section
          initial="hidden"
          whileInView="show"
          viewport={{ once: true }}
          variants={container}
          className="py-24 px-4 sm:px-6 lg:px-8 bg-dylan-surface/50"
        >
          <div className="max-w-6xl mx-auto">
            <motion.h2
              variants={item}
              className="text-3xl sm:text-4xl font-bold mb-16 text-center"
            >
              Why Choose Dylan Wave AI?
            </motion.h2>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              {[
                {
                  icon: '🤖',
                  title: 'AI-Powered Analysis',
                  description:
                    'Advanced machine learning algorithms analyze market trends and provide actionable insights.',
                },
                {
                  icon: '💼',
                  title: 'Demo Trading',
                  description:
                    'Practice with $10,000 virtual capital. No real money required to learn and experiment.',
                },
                {
                  icon: '🔒',
                  title: 'Secure & Reliable',
                  description:
                    'Bank-level security with JWT authentication, encrypted data, and secure wallet management.',
                },
              ].map((feature, index) => (
                <motion.div
                  key={index}
                  variants={item}
                  className="bg-dylan-bg border border-dylan-primary/20 rounded-lg p-8 hover:border-dylan-primary/50 transition-colors"
                >
                  <div className="text-4xl mb-4">{feature.icon}</div>
                  <h3 className="text-xl font-bold mb-3">{feature.title}</h3>
                  <p className="text-gray-400">{feature.description}</p>
                </motion.div>
              ))}
            </div>
          </div>
        </motion.section>

        {/* CTA Section */}
        <motion.section
          initial="hidden"
          whileInView="show"
          viewport={{ once: true }}
          variants={container}
          className="py-24 px-4 sm:px-6 lg:px-8"
        >
          <div className="max-w-4xl mx-auto text-center">
            <motion.h2
              variants={item}
              className="text-3xl sm:text-4xl font-bold mb-8"
            >
              Ready to Start Your Trading Journey?
            </motion.h2>

            <motion.p
              variants={item}
              className="text-xl text-gray-400 mb-12"
            >
              Join thousands of traders using Dylan Wave AI for intelligent market insights and
              risk-free demo trading.
            </motion.p>

            <motion.div variants={item}>
              <Link href="/register">
                <Button variant="primary" size="lg">
                  Get Started Free
                </Button>
              </Link>
            </motion.div>
          </div>
        </motion.section>
      </main>
      <Footer />
    </>
  );
}
