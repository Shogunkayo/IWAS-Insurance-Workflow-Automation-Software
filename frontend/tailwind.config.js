/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
        colors: {
            'primary': '#963131',
            'secondary': '#C06D6D',
            'black': '#221C2A'
        },
        fontSize: {
            sm: '0.750rem',
            base: '1rem',
            xl: '1.333rem',
            '2xl': '1.777rem',
            '3xl': '2.369rem',
            '4xl': '3.158rem',
            '5xl': '4.210rem',
        },
        fontFamily: {
            heading: 'Noto Sans Tifinagh',
            body: 'Noto Sans Tifinagh',
        },
        fontWeight: {
            normal: '400',
            bold: '700',
        },
    },
  },
  plugins: [],
}

