import { createUserWithEmailAndPassword, getAuth } from "firebase/auth";
import Link from "next/link";
import { useRouter } from "next/router";
import React, { useRef, useState } from "react";
import FirebaseErrorPane from "../ErrorPane/FirebaseErrorPane";
import SignInWithGoogle from "./SignInWithGoogle";
import PasswordValidationDisplay from "./Validation/PasswordValidationDisplay";

const re = new RegExp("auth/([^)]+)");

/**
 * Sign Up Component that takes in user input and submits it to be validated and to the database
 */
export default function SignUp() {
    const auth = getAuth();

    // to reroute users on sign in
    const router = useRouter();

    // read input without re-renders
    const emailInput = useRef<HTMLInputElement>(null);
    const [password, setPassword] = useState("");
    const pwInputdup = useRef<HTMLInputElement>(null);

    // show user errors
    const [error, setError] = useState<unknown>(null);

    // validator state
    const [isValidPassword, setIsValidPassword] = useState(false);

    // handle a user creating an account with email and pw
    const handleSubmit: React.FormEventHandler<HTMLFormElement> = async (e) => {
        // prevent page refresh
        e.preventDefault();
        setError(null);

        // read values from input boxes
        const email = emailInput.current?.value;
        const pwDup = pwInputdup.current?.value;

        // reject empty attempt
        if (!email || !password || !pwDup) return;

        // reject with password not confirmed
        if (password !== pwDup) return setError("Passwords do not match");

        // create user if possible
        const createUserPromise = createUserWithEmailAndPassword(auth, email, password);

        // error handle
        try {
            await createUserPromise;
            setError(null);
            router.push("/");
        } catch (err: unknown) {
            setError(err);
        }
    };

    return (
        <div className="rounded-lg w-10/12 border max-w-[640px] px-8 py-5 shadow-lg bg-white xs1-max:px-4">
            <h2 className="font-bold text-3xl mid-max:text-2xl border-b-4 pb-2">Create an account</h2>
            <form className="flex flex-col gap-5 text-gray-600 mt-4" onSubmit={handleSubmit}>
                <div className="flex flex-col gap-1">
                    <label htmlFor="email-input">E-mail</label>
                    <input className="rounded border py-1 px-3 text-lg" id="email-input" ref={emailInput} type="email" required />
                </div>
                <div className="flex flex-col gap-1">
                    <label htmlFor="password-input">Password</label>
                    <input
                        className="rounded border py-1 px-3 text-lg"
                        id="password-input"
                        onChange={(e) => setPassword(e.target.value)}
                        type="password"
                        pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"
                        required
                    />
                </div>
                <div className="flex flex-col gap-1">
                    <label htmlFor="password-input">Retype Password</label>
                    <input className="rounded border py-1 px-3 text-lg" id="password-input" ref={pwInputdup} type="password" required />
                </div>
                {password && (
                    <PasswordValidationDisplay
                        password={password}
                        numCapital={0}
                        numSymbols={1}
                        numNumbers={1}
                        lengthMin={8}
                        setIsValidPassword={setIsValidPassword}
                    />
                )}
                <FirebaseErrorPane err={error} />
                <button
                    id="hover-rm-bg"
                    type="submit"
                    className="rounded-full p-2 font-bold text-white animated-gradient-bg text-xl"
                    disabled={!isValidPassword}
                >
                    Submit
                </button>
            </form>
            <div className="flex gap-3 items-center py-4">
                <hr className="w-full" />
                or
                <hr className="w-full" />
            </div>
            <SignInWithGoogle />
            <div className="pt-4">
                Already have an account?{" "}
                <Link className="text-blue-600 hover:underline font-semibold" href="/sign-in">
                    Sign in
                </Link>
            </div>
        </div>
    );
}
