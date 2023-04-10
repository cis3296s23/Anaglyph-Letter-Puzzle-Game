import React from "react";

import { GrReactjs } from "react-icons/gr";
import FeatureCard from "./FeatureCard";

var x = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus pariatur quis nostrum corrupti, eum at";
export default function Features() {
    return (
        <section className="font-inter border-b">
            <div className="mx-auto w-[1200px] lg-max:grid-cols-1 lg-max:w-full xl-max:w-[1000px]">
                <h2 className="text-4xl font-bold pt-10 text-gray-700 xl-max:pl-8">Features</h2>
                <section className="my-10 grid grid-cols-3 gap-10 justify-items-center xl-max:grid-cols-2 md-max:grid-cols-1">
                    <FeatureCard name="Feature 1" statement={x} icon={<GrReactjs size={36} />} />
                    <FeatureCard name="Feature 1" statement={x} icon={<GrReactjs size={36} />} />
                    <FeatureCard name="Feature 1" statement={x} icon={<GrReactjs size={36} />} />
                    <FeatureCard name="Feature 1" statement={x} icon={<GrReactjs size={36} />} />
                    <FeatureCard name="Feature 1" statement={x} icon={<GrReactjs size={36} />} />
                </section>
            </div>
        </section>
    );
}
