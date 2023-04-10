import Navbar from "@/components/landing-page/Navbar";
import "@/styles/globals.css";
import type { AppProps } from "next/app";
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"], variable: "--inter" });



export default function App({ Component, pageProps }: AppProps) {
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
