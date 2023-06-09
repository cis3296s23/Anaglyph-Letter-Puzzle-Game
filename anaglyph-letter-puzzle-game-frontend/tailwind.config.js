/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./src/pages/**/*.{js,ts,jsx,tsx}", "./src/components/**/*.{js,ts,jsx,tsx}", "./src/app/**/*.{js,ts,jsx,tsx}"],
    theme: {
        extend: {
            backgroundImage: {},
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
                "md-max": { max: "750px" },
                "sm-max": { max: "639px" },
                "xs1-max": { max: "464px" },
                "xs2-max": { max: "380px" },
                "xs3-max": { max: "320px" },
            },
        },
    },
    plugins: [],
};
