import PasswordValidationDisplay from "../../../components/Auth/Validation/PasswordValidationDisplay";

export default {
    title: "PasswordValidationDisplay",
    component: PasswordValidationDisplay,
};

const TemplateValidator = (password: string) => (
    <PasswordValidationDisplay password={password} lengthMin={5} numCapital={1} numNumbers={1} numSymbols={1} setIsValidPassword={() => {}} />
);

export const MissingSymbol = () => TemplateValidator("ABCD1234");
export const MissingCapital = () => TemplateValidator("aBc1234");
export const MissingNumbersAndSymbol = () => TemplateValidator("aAccart");

/**
 * Click on this Doc-Component to try this component in action!
 */
export const TryItYourself = ({ password }: { password: string }) => TemplateValidator(password);
TryItYourself.args = {
    password: "abcD**12",
};
TryItYourself.argTypes = {
    password: { control: { type: "text" } },
    lengthMin: { table: { disable: true } },
    numCapital: { table: { disable: true } },
    numNumbers: { table: { disable: true } },
    numSymbols: { table: { disable: true } },
    setIsValidPassword: { table: { disable: true } },
};
