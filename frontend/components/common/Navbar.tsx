'use client';

import Link from 'next/link';
import { useState } from 'react';
import { motion } from 'framer-motion';

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="sticky top-0 z-50 bg-dylan-dark/80 backdrop-blur-md border-b border-dylan-primary/10">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-2 font-bold text-xl">
            <div className="w-8 h-8 bg-gradient-to-br from-dylan-primary to-dylan-info rounded-lg flex items-center justify-center">
              <span className="text-white font-bold">DW</span>
            </div>
            <span className="text-white">Dylan Wave AI</span>
          </Link>

          {/* Desktop Menu */}
          <div className="hidden md:flex items-center gap-8">
            <Link href="/" className="text-gray-300 hover:text-white transition">
              Home
            </Link>
            <Link href="/dashboard" className="text-gray-300 hover:text-white transition">
              Dashboard
            </Link>
            <Link href="/login" className="px-4 py-2 rounded-lg bg-dylan-primary hover:bg-dylan-primary/80 transition">
              Sign In
            </Link>
          </div>

          {/* Mobile Menu Button */}
          <button
            onClick={() => setIsOpen(!isOpen)}
            className="md:hidden p-2 hover:bg-dylan-surface rounded-lg transition"
          >
            <svg
              className="w-6 h-6"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M4 6h16M4 12h16M4 18h16"
              />
            </svg>
          </button>
        </div>

        {/* Mobile Menu */}
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            className="md:hidden pb-4 border-t border-dylan-primary/10"
          >
            <Link href="/" className="block px-4 py-2 text-gray-300 hover:text-white transition">
              Home
            </Link>
            <Link href="/dashboard" className="block px-4 py-2 text-gray-300 hover:text-white transition">
              Dashboard
            </Link>
            <Link href="/login" className="block px-4 py-2 text-gray-300 hover:text-white transition">
              Sign In
            </Link>
          </motion.div>
        )}
      </div>
    </nav>
  );
}
