import { ReactNode } from 'react';
import clsx from 'clsx';

interface CardProps {
  children: ReactNode;
  className?: string;
  variant?: 'default' | 'bordered';
}

export default function Card({
  children,
  className,
  variant = 'default',
}: CardProps) {
  const variantStyles = {
    default: 'bg-dylan-surface border border-dylan-primary/20',
    bordered: 'bg-dylan-bg border-2 border-dylan-primary/30',
  };

  return (
    <div
      className={clsx(
        'rounded-lg overflow-hidden transition-all hover:border-dylan-primary/50',
        variantStyles[variant],
        className
      )}
    >
      {children}
    </div>
  );
}
