import FirebaseErrorPane from "../../components/ErrorPane/FirebaseErrorPane";
import { FirebaseError } from "@firebase/util";

export default {
    title: "FirebaseErrorPane",
    component: FirebaseErrorPane,
    tags: ["autodocs"],
};

export const FirebaseErr = () => <FirebaseErrorPane err={new FirebaseError("auth/", "auth/invalid-password")} />;
export const StringErr = () => <FirebaseErrorPane err="Show to user this error" />;
