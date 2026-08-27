import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./data/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "rgb(var(--primary-rgb) / <alpha-value>)",
          dark: "rgb(var(--primary-dark-rgb) / <alpha-value>)",
          light: "rgb(var(--primary-light-rgb) / <alpha-value>)",
        },
        secondary: "rgb(var(--primary-rgb) / <alpha-value>)",
        accent: "rgb(var(--accent-rgb) / <alpha-value>)",
        dark: "rgb(var(--navy-rgb) / <alpha-value>)",
        gray: Object.fromEntries([50, 100, 200, 300, 400, 500, 600, 700, 800, 900].map(shade => [shade, `rgb(var(--gray-${shade}-rgb) / <alpha-value>)`])),
      },
      fontFamily: {
        sans: ["var(--reading-font)"],
        serif: ["var(--reading-font)"],
      },
    },
  },
  plugins: [],
};

export default config;
