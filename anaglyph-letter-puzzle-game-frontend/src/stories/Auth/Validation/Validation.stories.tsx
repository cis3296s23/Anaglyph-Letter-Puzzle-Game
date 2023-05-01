import PasswordValidationDisplay from "../../../components/Auth/Validation/PasswordValidationDisplay";

export default {
    title: "PasswordValidationDisplay",
    component: PasswordValidationDisplay,
    tags: ["autodocs"],
};


const TemplateValidator = (password: string) => (
    <PasswordValidationDisplay password={password} lengthMin={5} numCapital={1} numNumbers={1} numSymbols={1} setIsValidPassword={() => {}} />
);

/**
 * In Each example below, the password must be 5 chars long with at least:
 * + 1 Number
 * + 1 Symbol
 * + 1 Capital
 */
export const MissingSymbol = () => TemplateValidator("ABCD1234");
export const MissingCapital = () => TemplateValidator("aBc1234");
export const MissingNumbersAndSymbol = () => TemplateValidator("aAccart");
