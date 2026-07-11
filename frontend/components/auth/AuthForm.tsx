'use client';

import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import Input from '@/components/ui/Input';
import Button from '@/components/ui/Button';
import Toast from '@/components/ui/Toast';

const loginSchema = z.object({
  email: z.string().email('Invalid email address'),
  password: z.string().min(6, 'Password must be at least 6 characters'),
});

const registerSchema = loginSchema.extend({
  name: z.string().min(2, 'Name must be at least 2 characters'),
  confirmPassword: z.string(),
}).refine((data) => data.password === data.confirmPassword, {
  message: 'Passwords do not match',
  path: ['confirmPassword'],
});

type LoginFormData = z.infer<typeof loginSchema>;
type RegisterFormData = z.infer<typeof registerSchema>;

interface AuthFormProps {
  type: 'login' | 'register';
  isLoading: boolean;
  setIsLoading: (loading: boolean) => void;
}

export default function AuthForm({ type, isLoading, setIsLoading }: AuthFormProps) {
  const schema = type === 'login' ? loginSchema : registerSchema;
  const [toasts, setToasts] = useState<Array<{ id: string; type: 'success' | 'error'; message: string }>>([]);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(schema),
  });

  const addToast = (type: 'success' | 'error', message: string) => {
    const id = Date.now().toString();
    setToasts((prev) => [...prev, { id, type, message }]);
    setTimeout(() => {
      setToasts((prev) => prev.filter((t) => t.id !== id));
    }, 3000);
  };

  const onSubmit = async (data: LoginFormData | RegisterFormData) => {
    try {
      setIsLoading(true);
      // Simulate API call
      await new Promise((resolve) => setTimeout(resolve, 1000));
      addToast('success', `${type === 'login' ? 'Login' : 'Registration'} successful!`);
      console.log(`${type} data:`, data);
    } catch (error) {
      addToast('error', `${type === 'login' ? 'Login' : 'Registration'} failed!`);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
        {type === 'register' && (
          <Input
            label="Full Name"
            placeholder="John Doe"
            error={errors.name?.message}
            {...register('name' as any)}
          />
        )}

        <Input
          label="Email"
          type="email"
          placeholder="your@email.com"
          error={errors.email?.message}
          {...register('email')}
        />

        <Input
          label="Password"
          type="password"
          placeholder="Enter your password"
          error={errors.password?.message}
          {...register('password')}
        />

        {type === 'register' && (
          <Input
            label="Confirm Password"
            type="password"
            placeholder="Confirm your password"
            error={(errors.confirmPassword as any)?.message}
            {...register('confirmPassword' as any)}
          />
        )}

        <Button type="submit" variant="primary" size="lg" isLoading={isLoading} className="w-full">
          {type === 'login' ? 'Sign In' : 'Sign Up'}
        </Button>
      </form>

      {/* Toast Container */}
      <div className="fixed top-4 right-4 z-50 space-y-2">
        {toasts.map((toast) => (
          <Toast
            key={toast.id}
            id={toast.id}
            type={toast.type}
            message={toast.message}
            onClose={() => setToasts((prev) => prev.filter((t) => t.id !== toast.id))}
          />
        ))}
      </div>
    </>
  );
}
