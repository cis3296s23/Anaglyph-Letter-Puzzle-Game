import React from "react";

export interface FeatureCardProps {
    statement: string;
    icon: React.ReactNode;
    name: string;
}

// Component card that displays a feature
export default function FeatureCard(props: FeatureCardProps) {
    return (
        <div className="shadow-main border w-96 min-h-48 rounded shadow py-2 px-4 mid-max:w-[356px] md-max:w-[412px] xs1-max:w-[324px] xs2-max:w-[300px]">
            <div className="flex relative">
                <div className="tranform-icon bg-white p-4 rounded-lg shadow-md border">{props.icon}</div>
                <h3 className="pl-11 text-2xl font-semibold">{props.name}</h3>
            </div>
            <p className="py-2">{props.statement}</p>
        </div>
    );
}
