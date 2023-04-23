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
        const ModalJSX = <div className="overlay">{props.show && props.children}</div>;
        return ReactDOM.createPortal(ModalJSX, document.getElementById("modal-root") as Element);
    } else {
        return null;
    }
}
