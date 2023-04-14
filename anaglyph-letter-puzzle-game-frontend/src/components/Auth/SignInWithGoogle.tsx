import { FcGoogle } from "react-icons/fc";
import { getAuth, GoogleAuthProvider, signInWithPopup } from "firebase/auth";
import app from "../../../firebase.config";
import { useRouter } from "next/router";

export default function SignInWithGoogle() {
    // obtain auth status
    const auth = getAuth(app);
    const router = useRouter();

    // function to initialize google sign in procedure
    const handleGoogleSignIn = () => {
        const provider = new GoogleAuthProvider();

        // no need for a .then we are not doing anything with the resulting cred
        signInWithPopup(auth, provider)
            .then((cred) => console.log(cred))
            .catch((err) => {
                console.error(err);
            })
            .finally(() => router.push("/"));
    };

    return (
        <button
            onClick={handleGoogleSignIn}
            type="button"
            className="p-2 flex justify-center items-center w-full gap-3 text-xl bg-black text-white rounded-lg hover:bg-gray-700"
        >
            <FcGoogle size={32} /> <p className="font-semibold">Continue with Google</p>
        </button>
    );
}
