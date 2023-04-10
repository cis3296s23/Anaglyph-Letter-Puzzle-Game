import Hero from "@/components/landing-page/hero";
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
    return (
        <>
            <Hero />
        </>
    );
}
