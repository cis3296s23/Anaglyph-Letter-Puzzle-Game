import React from "react";

import FeatureCard, { FeatureCardProps } from "./FeatureCard";

import { ImEyePlus } from "react-icons/im";
import { BsGraphUp } from "react-icons/bs";
import { BiTable } from "react-icons/bi";
import { TfiLayoutGrid4 } from "react-icons/tfi";

const features: FeatureCardProps[] = [
    {
        name: "Changing Color",
        statement: "Use the color picker to target different color ranges to address weaknesses",
        icon: <ImEyePlus size={36} />,
    },
    {
        name: "Visualize Data",
        statement: "Use charts to visualize data about patients",
        icon: <BsGraphUp size={36} />,
    },
    {
        name: "Tracking Users",
        statement: "Keep tabs on all your uses in once place!",
        icon: <BiTable size={36} />,
    },
    {
        name: "Varying Difficulty",
        statement: "Increase the difficulty by increasing the grid size",
        icon: <TfiLayoutGrid4 size={36} />,
    },
];

// uses <FeatureCard /> and displays it in a grid
// represents the Feature part of the landing page
export default function Features() {
    return (
        <section className="font-inter border-b" id="features">
            <div className="mx-auto w-[1200px] lg-max:grid-cols-1 lg-max:w-full xl-max:w-[1000px]">
                <h2 className="text-4xl font-bold pt-10 text-gray-700 xl-max:pl-8">Features</h2>
                <section className="my-10 grid grid-cols-3 gap-10 justify-items-center xl-max:grid-cols-2 md-max:grid-cols-1">
                    {features.map((feature, i) => (
                        <FeatureCard name={feature.name} statement={feature.statement} icon={feature.icon} key={i} />
                    ))}
                </section>
            </div>
        </section>
    );
}
