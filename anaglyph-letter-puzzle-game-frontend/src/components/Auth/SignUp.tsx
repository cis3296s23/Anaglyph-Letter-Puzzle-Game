import { getAuth } from "firebase/auth";
import React, { useRef } from "react";
import SignInWithGoogle from "./SignInWithGoogle";

export default function SignUp() {
    const auth = getAuth();

    const emailInput = useRef<HTMLInputElement>(null);
    const pwInput = useRef<HTMLInputElement>(null);
    const pwInputdup = useRef<HTMLInputElement>(null);

    // handle a user creating an account with email and pw
    const handleSubmit: React.FormEventHandler<HTMLFormElement> = (e) => {
        // prevent page refresh
        e.preventDefault();

        // read values from input boxes
        const email = emailInput.current?.value;
        const pword = pwInput.current?.value;
        const pwDup = pwInputdup.current?.value;

        // reject empty attempt
        if (!email || !pword || !pwDup) return;
    };

    return (
        <div className="rounded-lg w-10/12 border max-w-[640px] px-8 py-5 shadow-lg bg-white">
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
                <div className="flex flex-col gap-1">
                    <label htmlFor="password-input">Retype Password</label>
                    <input className="rounded border py-1 px-3 text-lg" id="password-input" ref={pwInputdup} type="password" required />
                </div>
                <button id="hover-rm-bg" type="submit" className="rounded-full p-2 font-bold text-white animated-gradient-bg text-xl hover:bg-sp1">
                    Submit
                </button>
            </form>
            <div className="flex gap-3 items-center py-4">
                <hr className="w-full" />
                or
                <hr className="w-full" />
            </div>
            <SignInWithGoogle />
        </div>
    );
}
