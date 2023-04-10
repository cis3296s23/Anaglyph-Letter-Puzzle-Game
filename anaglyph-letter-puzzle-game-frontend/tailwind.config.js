/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./src/pages/**/*.{js,ts,jsx,tsx}", "./src/components/**/*.{js,ts,jsx,tsx}", "./src/app/**/*.{js,ts,jsx,tsx}"],
    theme: {
        extend: {
            backgroundImage: {
                "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
                "gradient-conic": "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
            },
            fontFamily: {
                inter: ["var(--font-inter)", "Helvetica"],
            },
            colors: {
                sp1: "#20B486",
            },
            screens: {
                "2xl-max": { max: "1535px" },
                "xl-max": { max: "1279px" },
                "lg-max": { max: "1023px" },
                "mid-max": { max: "900px" },
                "md-max": { max: "767px" },
                "sm-max": { max: "639px" },
            },
        },
    },
    plugins: [],
};
