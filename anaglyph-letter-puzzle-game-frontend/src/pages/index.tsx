
import Features from "@/components/landing-page/FeatureList/FeatureGrid";
import Hero from "@/components/landing-page/Hero";
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
    return (
        <>
            <Hero />
            <Features />
        </>
    );
}
