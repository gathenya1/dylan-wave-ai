'use client';

import { ReactNode } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import Button from './Button';

interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  children: ReactNode;
  primaryAction?: {
    label: string;
    onClick: () => void;
    isLoading?: boolean;
  };
  secondaryAction?: {
    label: string;
    onClick: () => void;
  };
}

export default function Modal({
  isOpen,
  onClose,
  title,
  children,
  primaryAction,
  secondaryAction,
}: ModalProps) {
  return (
    <AnimatePresence>
      {isOpen && (
        <>
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="fixed inset-0 bg-black/50 backdrop-blur-sm z-40"
          />
          <motion.div
            initial={{ opacity: 0, scale: 0.95, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: 20 }}
            className="fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-50 w-full max-w-md mx-4"
          >
            <div className="bg-dylan-surface border border-dylan-primary/20 rounded-lg shadow-2xl">
              {/* Header */}
              <div className="flex items-center justify-between p-6 border-b border-dylan-primary/10">
                <h2 className="text-xl font-bold">{title}</h2>
                <button
                  onClick={onClose}
                  className="text-gray-400 hover:text-white transition"
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
                      d="M6 18L18 6M6 6l12 12"
                    />
                  </svg>
                </button>
              </div>

              {/* Content */}
              <div className="p-6">{children}</div>

              {/* Footer */}
              {(primaryAction || secondaryAction) && (
                <div className="flex items-center gap-3 p-6 border-t border-dylan-primary/10">
                  {secondaryAction && (
                    <Button
                      variant="ghost"
                      onClick={secondaryAction.onClick}
                      className="flex-1"
                    >
                      {secondaryAction.label}
                    </Button>
                  )}
                  {primaryAction && (
                    <Button
                      variant="primary"
                      onClick={primaryAction.onClick}
                      isLoading={primaryAction.isLoading}
                      className="flex-1"
                    >
                      {primaryAction.label}
                    </Button>
                  )}
                </div>
              )}
            </div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
}
