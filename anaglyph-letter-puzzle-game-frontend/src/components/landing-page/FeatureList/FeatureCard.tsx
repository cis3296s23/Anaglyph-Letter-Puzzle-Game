import React from "react";

interface FeatureCardProps {
    statement: string;
    icon: React.ReactNode;
    name: string;
}

export default function FeatureCard(props: FeatureCardProps) {
    return (
        <div className="shadow-main border-[1px] w-96 h-48 rounded shadow-lg p-4 mid-max:w-[324px] md-max:w-[400px]">
            <div className="flex gap-4">
                {props.icon}
                <h3 className="text-2xl font-semibold">{props.name}</h3>
            </div>
            <p className="pt-3">{props.statement}</p>
        </div>
    );
}
