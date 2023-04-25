import Image from "next/image";
import React from "react";
import { Gallery } from "react-grid-gallery";

const images = [
    {
        src: "/hero-1.png",
        width: 320,
        height: 174,
    },
    {
        src: "/hero-2.png",
        width: 320,
        height: 212,
    },

    {
        src: "https://c4.staticflickr.com/9/8887/28897124891_98c4fdd82b_b.jpg",
        width: 320,
        height: 212,
    },
    {
        src: "/hero-main.png",
        width: 450,
        height: 250,
    },
];

// The "eye grabbing part of the page"
const Hero = () => {
    return (
        <main className="font-inter min-h-[600px] custom-bg-blur border-b py-10">
            <section className="grid grid-cols-2 pt-4 mx-auto w-[1200px] lg-max:grid-cols-1 lg-max:w-full xl-max:w-[1000px]">
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
                        alt="Image of a Data Viz being generated from patient Data"
                        src="/hero-main.png"
                        height={562}
                        width={842}
                        className="w-[450px] rounded-md shadow-2xl sm-max:w-96 xs2-max:rounded-t-none"
                    />
                </div>
            </section>
        </main>
    );
};

export default Hero;
