import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import '@/styles/globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Dylan Wave AI | AI-Powered Trading Platform',
  description:
    'Experience intelligent trading with Dylan Wave AI. Demo trading, market analysis, secure wallets, and admin dashboard.',
  keywords: [
    'trading',
    'AI',
    'finance',
    'crypto',
    'demo trading',
    'market analysis',
  ],
  viewport: 'width=device-width, initial-scale=1',
  themeColor: '#1e40af',
  authors: [{ name: 'Dylan Wave AI' }],
  openGraph: {
    title: 'Dylan Wave AI | AI-Powered Trading Platform',
    description:
      'Experience intelligent trading with Dylan Wave AI. Demo trading, market analysis, secure wallets, and admin dashboard.',
    type: 'website',
    locale: 'en_US',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="scroll-smooth">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </head>
      <body className={`${inter.className} bg-dylan-dark text-white antialiased`}>
        <div className="min-h-screen flex flex-col">
          {children}
        </div>
      </body>
    </html>
  );
}
