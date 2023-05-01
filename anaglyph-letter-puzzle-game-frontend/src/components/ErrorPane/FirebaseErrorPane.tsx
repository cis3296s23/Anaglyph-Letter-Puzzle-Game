import { FirebaseError } from "@firebase/util";
import ErrorPane from "./ErrorPane";

interface FirebaseErrorPaneProps {
    err: unknown;
}

// extracts the auth error
const re = new RegExp("auth/([^)]+)");

/**
 * Wrapper for <ErrorPane /> as it transforms Firebase Auth errors into String based errors.
 * The prop `err` is of type `unknown` as it uses `if-else` logic to determine its type and extract the error.
 */
export default function FirebaseErrorPane(props: FirebaseErrorPaneProps) {
    const { err } = props;

    // parse out error if its a firebase error
    if (err instanceof FirebaseError) {
        const regexOutput = re.exec(err.message);
        if (!regexOutput || !regexOutput.length) {
            return <ErrorPane error="Unknown Firebase Error" />;
        }
        const error = regexOutput[regexOutput.length - 1];
        return <ErrorPane error={error} />;
    }

    // display regularly if just string
    if (typeof err === "string") {
        return <ErrorPane error={err} />;
    }

    return null;
}
