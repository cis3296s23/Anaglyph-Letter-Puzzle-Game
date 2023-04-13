import SignUp from "@/components/Auth/SignUp";
import React from "react";

export default function SignInPage() {
    return (
        <section className="mx-auto w-[1200px] lg-max:grid-cols-1 lg-max:w-full xl-max:w-[1000px] font-inter">
            <div className="animated-gradient-bg full-page z-0"></div>
            <div className="auth-container flex justify-center mt-12 z-10 relative">
                <SignUp />
            </div>
        </section>
    );
}
