module.exports = {
  content: [
    './docs_src/**/*.{vue,js,ts,jsx,tsx,md}',
    './.vitepress/**/*.{vue,js,ts}'
  ],
  theme: {
    extend: {
      colors: {
        'electric-teal': '#00F5D4',
      },
    },
  },
  plugins: [],
};
