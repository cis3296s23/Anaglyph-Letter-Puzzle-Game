import React from "react";

interface FeatureCardProps {
    statement: string;
    icon: React.ReactNode;
    name: string;
}

// Component card that displays a feature
export default function FeatureCard(props: FeatureCardProps) {
    return (
        <div className="shadow-main border-[1px] w-96 h-48 rounded shadow-lg p-4 mid-max:w-[356px] md-max:w-[412px] border-b">
            <div className="flex">
                <div className="tranform-icon relative bg-white p-4 rounded-lg shadow-lg border">{props.icon}</div>
                <h3 className="text-2xl font-semibold">{props.name}</h3>
            </div>
            <p className="pt-3">{props.statement}</p>
        </div>
    );
}
