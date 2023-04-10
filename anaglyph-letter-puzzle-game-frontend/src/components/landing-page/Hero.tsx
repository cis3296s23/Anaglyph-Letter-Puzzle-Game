import Image from "next/image";
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
        height: 250,
    },
];

// The "eye grabbing part of the page"
const Hero = () => {
    return (
        <main className="font-inter min-h-[600px] custom-bg-blur border-b py-10">
            <section className="grid grid-cols-2 mx-auto pt-4 w-[1200px] lg-max:grid-cols-1 lg-max:w-full xl-max:w-[1000px]">
                <div className="flex flex-col justify-center lg-max:items-center">
                    <h2 className="text-2xl font-medium mt-10">Product Line 1</h2>
                    <h2 className="text-4xl font-semibold mt-10">This is a sentence</h2>
                    <h2 className="text-5xl font-black">Keyword</h2>
                    <small className="font-normal mt-1">Some random Platitude</small>
                </div>
                <div className="lg-max:hidden">
                    <Gallery images={images} enableImageSelection={false} />
                </div>
                <div className="lg:hidden mt-10 flex justify-center ">
                    <Image
                        alt="placeholder"
                        src="https://c8.staticflickr.com/9/8104/28973555735_ae7c208970_b.jpg"
                        height={562}
                        width={842}
                        className="w-[450px] rounded-md shadow-2xl sm-max:w-96"
                    />
                </div>
            </section>
        </main>
    );
};

export default Hero;
