import React from "react";

import { FaCheck } from "react-icons/fa";
import { RxCross2 } from "react-icons/rx";

interface PasswordValidationDisplayProps {
    password: string;
    lengthMin: number;
    numCapital?: number;
    numNumbers?: number;
    numSymbols?: number;
    setIsValidPassword: (b: boolean) => void;
}

/**
 * Validates password based on props and sets the valid var using `setIsValidPassword`.
 */
export default function PasswordValidationDisplay(props: PasswordValidationDisplayProps) {
    const { password } = props;

    // Patterns
    //----------------------------------------------------------------------

    const numCapitalReq = new RegExp(`[A-Z]{${props.numCapital ?? 0}}`, "gs");
    const numNumbersReq = new RegExp(`\\d{${props.numNumbers ?? 0}}`, "gs");
    const numSymbols = new RegExp(`[\\W\\_]{${props.numSymbols ?? 0}}`, "gs");

    // Validations
    //----------------------------------------------------------------------
    // `|| !Boolean(props.numCapital)` controls for props.numCapital = 0
    const meetsCapitals = numCapitalReq.test(password) || !Boolean(props.numCapital);
    const meetsNumbers = numNumbersReq.test(password) || !Boolean(props.numNumbers);
    const meetsSymbols = numSymbols.test(password) || !Boolean(props.numSymbols);
    const meetsLength = password.length >= props.lengthMin;

    props.setIsValidPassword(meetsCapitals && meetsNumbers && meetsSymbols && meetsLength);

    return (
        <div className="flex flex-col pl-8 bg-blue-100 rounded-lg py-3">
            {Boolean(props.numCapital) && (
                <div className="flex gap-2 items-center text-lg">
                    {meetsCapitals ? <FaCheck className="text-sp1" /> : <RxCross2 className="text-red-500" />}{" "}
                    <p>
                        Has at atleast {props.numCapital} <strong>capital</strong> letter(s)
                    </p>
                </div>
            )}
            {Boolean(props.numNumbers) && (
                <div className="flex gap-2 items-center text-lg">
                    {meetsNumbers ? <FaCheck className="text-sp1" /> : <RxCross2 className="text-red-500" />}{" "}
                    <p>Has at atleast {props.numNumbers} Number(s)</p>
                </div>
            )}
            {Boolean(props.numSymbols) && (
                <div className="flex gap-2 items-center text-lg">
                    {meetsSymbols ? <FaCheck className="text-sp1" /> : <RxCross2 className="text-red-500" />}{" "}
                    <p>Has at atleast {props.numSymbols} Symbol(s)</p>
                </div>
            )}
            <div className="flex gap-2 items-center text-lg">
                {meetsLength ? <FaCheck className="text-sp1" /> : <RxCross2 className="text-red-500" />}{" "}
                <p>Password contains atleast {props.lengthMin} characters</p>
            </div>
        </div>
    );
}
