import React from "react";
import LoadingSpinner from "./LoadingSpinner";

export default function LoadingOverlaySpinner() {
    return (
        <section className="z-20 absolute bg-gray-500/50 w-full h-full rounded-lg">
            <div role="status" className="absolute top-1/2 left-1/2 translate-x-[-50%] translate-y-[-50%]">
                <LoadingSpinner />
            </div>
        </section>
    );
}
