module.exports = {
  content: [
    './docs_src/**/*.{vue,js,ts,jsx,tsx,md}',
    './.vitepress/**/*.{vue,js,ts}'
  ],
  theme: {
    extend: {
      colors: {
        'vp-bg': 'var(--vp-c-bg)',
        'vp-bg-soft': 'var(--vp-c-bg-soft)',
        'vp-border': 'var(--vp-c-divider)',
        'vp-text': 'var(--vp-c-text-1)',
        'vp-text-2': 'var(--vp-c-text-2)',
        'vp-brand': 'var(--vp-c-brand-1)',
        'vp-brand-light': 'var(--vp-c-brand-2)'
      },
    },
  },
  plugins: [],
};
