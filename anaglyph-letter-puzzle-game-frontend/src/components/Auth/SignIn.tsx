import React, { useRef } from "react";

import { FcGoogle } from "react-icons/fc";

export default function SignIn() {
    //
    const emailInput = useRef<HTMLInputElement>(null);
    const pwInput = useRef<HTMLInputElement>(null);

    // handle a user creating an account with email and pw
    const handleSubmit: React.FormEventHandler<HTMLFormElement> = (e) => {
        // prevent page refresh
        e.preventDefault();
    };

    return (
        <div className="rounded-lg w-10/12 border max-w-[640px] px-8 py-5 shadow-lg bg-white">
            <h2 className="font-bold text-3xl mid-max:text-2xl border-b-4 pb-2">Sign In</h2>
            <form className="flex flex-col gap-5 text-gray-600 mt-4" onSubmit={handleSubmit}>
                <div className="flex flex-col gap-1">
                    <label htmlFor="email-input">E-mail</label>
                    <input className="rounded border py-1 px-3 text-lg" id="email-input" ref={emailInput} type="email" />
                </div>
                <div className="flex flex-col gap-1">
                    <label htmlFor="password-input">Password</label>
                    <input className="rounded border py-1 px-3 text-lg" id="password-input" ref={pwInput} type="password" />
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
            <button type="button" className="p-2 flex justify-center items-center w-full gap-3 text-xl bg-black text-white rounded-lg hover:bg-gray-700">
                <FcGoogle size={32}/> <p className="font-semibold">Continue with Google</p>
            </button>
        </div>
    );
}
