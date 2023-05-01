import { FirebaseError } from "firebase/app";
import { getAuth, signInWithEmailAndPassword } from "firebase/auth";
import Link from "next/link";
import { useRouter } from "next/router";
import React, { useRef, useState } from "react";
import FirebaseErrorPane from "../ErrorPane/FirebaseErrorPane";
import SignInWithGoogle from "./SignInWithGoogle";

/**
 * Sign in Component to help users sign in via email/password or Google OAuth
 */
export default function SignIn() {
    const auth = getAuth();
    const router = useRouter();

    const emailInput = useRef<HTMLInputElement>(null);
    const pwInput = useRef<HTMLInputElement>(null);

    const [error, setError] = useState<unknown>(null);

    // handle a user creating an account with email and pw
    const handleSubmit: React.FormEventHandler<HTMLFormElement> = async (e) => {
        // prevent page refresh
        e.preventDefault();
        setError(null);

        // read values from input boxes
        const email = emailInput.current?.value;
        const pword = pwInput.current?.value;

        // reject empty attempt
        if (!email || !pword) return;

        // send to databases
        const authUserPromise = signInWithEmailAndPassword(auth, email, pword);

        // error handle
        try {
            await authUserPromise;
            setError(null);
            router.push("/");
        } catch (err: unknown) {
            setError(err);
        }
    };

    return (
        <div className="rounded-lg w-10/12 border max-w-[640px] px-8 py-5 shadow-lg bg-white xs1-max:px-4">
            <h2 className="font-bold text-3xl mid-max:text-2xl border-b-4 pb-2">Sign In</h2>
            <form className="flex flex-col gap-5 text-gray-600 mt-4" onSubmit={handleSubmit}>
                <div className="flex flex-col gap-1">
                    <label htmlFor="email-input">E-mail</label>
                    <input className="rounded border py-1 px-3 text-lg" id="email-input" ref={emailInput} type="email" required />
                </div>
                <div className="flex flex-col gap-1">
                    <label htmlFor="password-input">Password</label>
                    <input className="rounded border py-1 px-3 text-lg" id="password-input" ref={pwInput} type="password" required />
                </div>
                <FirebaseErrorPane err={error} />
                <button id="hover-rm-bg" type="submit" className="rounded-full p-2 font-bold text-white animated-gradient-bg text-xl">
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
                Dont have an account?{" "}
                <Link className="text-blue-600 hover:underline font-semibold" href="/sign-up">
                    Create one
                </Link>
            </div>
        </div>
    );
}
