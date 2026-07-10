'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import clsx from 'clsx';

const menuItems = [
  { href: '/dashboard', label: 'Dashboard', icon: '📊' },
  { href: '/trade', label: 'Trade', icon: '💼' },
  { href: '/wallet', label: 'Wallet', icon: '💰' },
  { href: '/history', label: 'History', icon: '📈' },
  { href: '/profile', label: 'Profile', icon: '👤' },
];

export default function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="w-64 bg-dylan-surface border-r border-dylan-primary/10 min-h-screen flex flex-col">
      {/* Logo */}
      <div className="p-6 border-b border-dylan-primary/10">
        <Link href="/" className="flex items-center gap-2 font-bold">
          <div className="w-8 h-8 bg-gradient-to-br from-dylan-primary to-dylan-info rounded-lg flex items-center justify-center">
            <span className="text-white font-bold text-sm">DW</span>
          </div>
          <span>Dylan Wave AI</span>
        </Link>
      </div>

      {/* Menu Items */}
      <nav className="flex-1 p-4 space-y-2">
        {menuItems.map((item) => {
          const isActive = pathname === item.href;
          return (
            <Link
              key={item.href}
              href={item.href}
              className={clsx(
                'flex items-center gap-3 px-4 py-3 rounded-lg transition',
                isActive
                  ? 'bg-dylan-primary text-white'
                  : 'text-gray-400 hover:text-white hover:bg-dylan-primary/20'
              )}
            >
              <span className="text-lg">{item.icon}</span>
              <span>{item.label}</span>
            </Link>
          );
        })}
      </nav>

      {/* User Section */}
      <div className="p-4 border-t border-dylan-primary/10">
        <button className="w-full px-4 py-2 bg-dylan-primary/20 hover:bg-dylan-primary/30 rounded-lg transition text-gray-300 hover:text-white">
          Sign Out
        </button>
      </div>
    </aside>
  );
}
