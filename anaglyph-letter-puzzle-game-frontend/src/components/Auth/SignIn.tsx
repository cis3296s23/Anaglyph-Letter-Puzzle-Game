import React, { useRef } from "react";

export default function SignIn() {
    //
    const emailInput = useRef<HTMLInputElement>(null);
    const pwInput = useRef<HTMLInputElement>(null);

    return (
        <div className="rounded-lg w-10/12 border max-w-[640px] px-8 py-5 shadow-lg bg-white">
            <h2 className="font-bold text-3xl mid-max:text-2xl border-b-4 pb-2">Sign In</h2>
            <form className="flex flex-col gap-5 text-gray-600 mt-4">
                <div className="flex flex-col gap-1">
                    <label htmlFor="email-input">E-mail</label>
                    <input className="rounded border py-1 px-3 text-lg" id="email-input" ref={emailInput} type="email" />
                </div>
                <div className="flex flex-col gap-1">
                    <label htmlFor="password-input">Password</label>
                    <input className="rounded border py-1 px-3 text-lg" id="password-input" ref={pwInput} type="password" />
                </div>
            </form>
        </div>
    );
}
