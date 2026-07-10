'use client';

import { motion, AnimatePresence } from 'framer-motion';
import { useEffect } from 'react';

export type ToastType = 'success' | 'error' | 'info' | 'warning';

interface ToastProps {
  id: string;
  type: ToastType;
  message: string;
  duration?: number;
  onClose: (id: string) => void;
}

const typeStyles = {
  success: 'bg-dylan-success',
  error: 'bg-dylan-danger',
  info: 'bg-dylan-info',
  warning: 'bg-dylan-warning',
};

const typeIcons = {
  success: '✓',
  error: '✕',
  info: 'ℹ',
  warning: '⚠',
};

export default function Toast({
  id,
  type,
  message,
  duration = 3000,
  onClose,
}: ToastProps) {
  useEffect(() => {
    const timer = setTimeout(() => onClose(id), duration);
    return () => clearTimeout(timer);
  }, [id, duration, onClose]);

  return (
    <motion.div
      initial={{ opacity: 0, x: 100 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: 100 }}
      className={`${typeStyles[type]} text-white px-4 py-3 rounded-lg shadow-lg flex items-center gap-3`}
    >
      <span className="font-bold text-lg">{typeIcons[type]}</span>
      <p>{message}</p>
    </motion.div>
  );
}
