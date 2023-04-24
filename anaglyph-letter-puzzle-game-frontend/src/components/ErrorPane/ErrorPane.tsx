import React from "react";

interface ErrorPaneProps {
    error: string;
}

export default function ErrorPane(props: ErrorPaneProps) {
    const { error } = props;

    return (
        <div className="p-4 text-sm text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400 my-2" role="alert">
            <span className="font-medium">Error:</span> {error}
        </div>
    );
}
