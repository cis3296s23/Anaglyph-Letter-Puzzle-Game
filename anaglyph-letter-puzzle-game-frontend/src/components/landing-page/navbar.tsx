import Link from "next/link";
import React, { useState } from "react";

import { GiHamburgerMenu } from "react-icons/gi";
import { IoMdClose } from "react-icons/io";

const Navbar = () => {
    const [toggle, setToggle] = useState(false);
    const handleClick = () => setToggle(!toggle);

    // links to render based on auth status
    const Links = (
        <>
            <li className="p-4 hover:bg-gray-100">Home</li>
            <li className="p-4 hover:bg-gray-100">About</li>
            <li className="p-4 hover:bg-gray-100">Support</li>
            <li className="p-4 hover:bg-gray-100">Platform</li>
            <li className="p-4 hover:bg-gray-100">Pricing</li>
        </>
    );

    const AuthButton = <Link href={"#"} className="px-8 py-3 rounded-md bg-sp-green text-white font-bold">Sign Up or Log in</Link>;

    return (
        <div className="w-full h-[80px] bg-white border-b font-inter sticky">
            <div className="md:max-w-[1480px] max-w-[600px] m-auto w-full h-full flex justify-between items-center md:px-4 px-4">
                <h1 className="text-xl font-bold text-sp-green border-b-2 border-t-2 border-sp-green">{process.env.NEXT_PUBLIC_SITENAME}</h1>
                <div className="hidden md:flex items-center ">
                    <ul className="flex gap-4">{Links}</ul>
                </div>

                <div className="hidden md:flex">{AuthButton}</div>

                <div className="md:hidden" onClick={handleClick}>
                    {toggle ? <IoMdClose size={25} /> : <GiHamburgerMenu size={25} />}
                </div>
            </div>

            <div className={toggle ? "absolute z-10 p-4  bg-white w-full px-8 md:hidden border-b" : "hidden"}>
                <ul>
                    {Links}
                    <div className="flex flex-col my-4 gap-4">{AuthButton}</div>
                </ul>
            </div>
        </div>
    );
};

export default Navbar;
