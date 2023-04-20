import { FirebaseError } from "firebase/app";
import ErrorPane from "./ErrorPane";

interface FirebaseErrorPaneProps {
    err: unknown;
}

// extracts the auth error
const re = new RegExp("auth/([^)]+)");

export default function FirebaseErrorPane(props: FirebaseErrorPaneProps) {
    const { err } = props;

    // parse out error if its a firebase error
    if (err instanceof FirebaseError) {
        const regexOutput = re.exec(err.message);
        if (!regexOutput || !regexOutput.length) {
            return null;
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
