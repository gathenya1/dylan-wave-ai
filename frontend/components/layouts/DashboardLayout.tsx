'use client';

import { ReactNode } from 'react';
import Sidebar from '@/components/common/Sidebar';
import Footer from '@/components/common/Footer';

interface DashboardLayoutProps {
  children: ReactNode;
}

export default function DashboardLayout({ children }: DashboardLayoutProps) {
  return (
    <div className="flex min-h-screen bg-dylan-dark">
      <Sidebar />
      <main className="flex-1 flex flex-col">
        <div className="flex-1 p-8 overflow-y-auto">
          {children}
        </div>
        <Footer />
      </main>
    </div>
  );
}
