import Navbar from "@/components/landing-page/Navbar";
import "@/styles/globals.css";
import type { AppProps } from "next/app";
import { Inter } from "next/font/google";

// font loading
const inter = Inter({ subsets: ["latin"], variable: "--inter" });

export default function App({ Component, pageProps }: AppProps) {
    // the style:jax part injects the font variable into the top of the file so other html.elements can access it
    // Navbar: persisant <Navbar/> component that renders on each page
    return (
        <>
            <style jsx global>
                {`
                    :root {
                        --font-inter: ${inter.style.fontFamily};
                    }
                `}
            </style>
            <Navbar />
            <Component {...pageProps} />
        </>
    );
}
