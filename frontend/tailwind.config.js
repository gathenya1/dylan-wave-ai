/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        'dylan-primary': '#1e40af',      // Royal Blue
        'dylan-dark': '#0f172a',         // Dark Navy
        'dylan-success': '#10b981',      // Emerald Green
        'dylan-danger': '#ef4444',       // Red
        'dylan-warning': '#f59e0b',      // Amber
        'dylan-info': '#06b6d4',         // Cyan
        'dylan-bg': '#0f172a',           // Dark Navy for backgrounds
        'dylan-surface': '#1e293b',      // Slate for surfaces
      },
      fontFamily: {
        'dylan': ['Inter', 'system-ui', 'sans-serif'],
      },
      spacing: {
        'dylan-xs': '0.25rem',
        'dylan-sm': '0.5rem',
        'dylan-md': '1rem',
        'dylan-lg': '1.5rem',
        'dylan-xl': '2rem',
      },
      borderRadius: {
        'dylan': '0.375rem',
        'dylan-lg': '0.5rem',
      },
    },
  },
  plugins: [],
};
