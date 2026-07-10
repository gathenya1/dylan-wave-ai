import { InputHTMLAttributes, forwardRef } from 'react';
import clsx from 'clsx';

interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
  helperText?: string;
}

const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ label, error, helperText, className, ...props }, ref) => {
    return (
      <div className="w-full">
        {label && (
          <label className="block text-sm font-medium text-gray-300 mb-2">
            {label}
          </label>
        )}
        <input
          ref={ref}
          className={clsx(
            'w-full px-4 py-2.5 bg-dylan-surface border rounded-lg transition-colors',
            'text-white placeholder-gray-500',
            'focus:outline-none focus:ring-2 focus:ring-dylan-primary/50',
            error
              ? 'border-dylan-danger focus:ring-dylan-danger/50'
              : 'border-dylan-primary/20 hover:border-dylan-primary/40',
            className
          )}
          {...props}
        />
        {error && <p className="mt-1 text-sm text-dylan-danger">{error}</p>}
        {helperText && !error && (
          <p className="mt-1 text-sm text-gray-400">{helperText}</p>
        )}
      </div>
    );
  }
);

Input.displayName = 'Input';

export default Input;
