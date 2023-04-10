import React from "react";
import { Gallery } from "react-grid-gallery";

const images = [
    {
        src: "https://c2.staticflickr.com/9/8817/28973449265_07e3aa5d2e_b.jpg",
        width: 320,
        height: 174,
        caption: "After Rain (Jeshu John - designerspics.com)",
    },
    {
        src: "https://c2.staticflickr.com/9/8356/28897120681_3b2c0f43e0_b.jpg",
        width: 320,
        height: 212,
        alt: "Boats (Jeshu John - designerspics.com)",
    },

    {
        src: "https://c4.staticflickr.com/9/8887/28897124891_98c4fdd82b_b.jpg",
        width: 320,
        height: 212,
    },
    {
        src: "https://c8.staticflickr.com/9/8104/28973555735_ae7c208970_b.jpg",
        width: 450,
        height: 212,
    },
];

const Hero = () => {
    return (
        <main className="font-inter min-h-[600px] custom-bg-blur border-b">
            <section className="z-10 grid grid-cols-2 w-[1200px] mx-auto pt-4 xl-max:w-[1000px] lg-max:grid-cols-1 lg-max:w-full">
                <div className="flex flex-col justify-center lg-max:items-center">
                    <h2 className="text-2xl font-medium mt-10">Product Line 1</h2>
                    <h2 className="text-4xl font-semibold mt-10">This is a sentence</h2>
                    <h2 className="text-5xl font-black">Keyword</h2>
                    <small className="font-normal mt-1">Some random Platitude</small>
                </div>
                <div className="mt-10">
                    <Gallery images={images} enableImageSelection={false} />
                </div>
            </section>
        </main>
    );
};

export default Hero;
