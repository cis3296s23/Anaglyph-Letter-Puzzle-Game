import SignIn from "@/components/Auth/SignIn";
import React from "react";

export default function SignInPage() {
    return (
        <main className="animated-gradient-bg pt-12 min-h-screen">
            <section className="mx-auto w-[1200px] lg-max:grid-cols-1 lg-max:w-full xl-max:w-[1000px] font-inter">
                <div className="auth-container flex justify-center  z-10 relative">
                    <SignIn />
                </div>
            </section>
        </main>
    );
}
