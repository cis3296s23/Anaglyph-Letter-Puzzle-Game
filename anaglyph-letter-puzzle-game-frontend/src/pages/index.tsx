import Features from "@/components/landing-page/FeatureList/FeatureGrid";
import Hero from "@/components/landing-page/Hero";

export default function Home() {
    return (
        <main className="mb-4">
            <Hero />
            <Features />
        </main>
    );
}
