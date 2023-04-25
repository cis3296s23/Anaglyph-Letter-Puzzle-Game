import { useState } from "react";

export type ToggleFunction = () => void;

const useModal = (initial = false): [boolean, ToggleFunction] => {
    const [modal, useModal] = useState(initial);

    // eslint-disable-next-line react-hooks/rules-of-hooks
    const toggle = () => useModal((show) => !show);

    return [modal, toggle];
};

export default useModal;
