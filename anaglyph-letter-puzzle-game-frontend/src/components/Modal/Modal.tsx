import React, { useEffect, useRef, useState } from "react";
import ReactDOM from "react-dom";

export interface ModalProps {
    show: boolean;
    children: React.ReactNode;
}

export default function Modal(props: ModalProps) {
    const [isBrowser, setIsBrowser] = useState(false);

    useEffect(() => {
        setIsBrowser(true);
    }, []);

    if (isBrowser) {
        // I know #modal-root will exist
        const ModalJSX = props.show && (
            <div className="bg-gray-500/50 fixed top-0 left-0 right-0 z-20 w-full p-4 h-full flex items-center justify-center">
                {props.children}
            </div>
        );
        return ReactDOM.createPortal(ModalJSX, document.getElementById("modal-root") as Element);
    } else {
        return null;
    }
}
