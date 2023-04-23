import { CreateUserRequest, CreateUserResponse } from "@/pages/api/create-user";
import axios, { AxiosResponse } from "axios";
import React, { useRef, useState } from "react";
import FirebaseErrorPane from "../ErrorPane/FirebaseErrorPane";

interface AddPatientFormProps {
    therapistUid: string;
    refresh: () => void;
}

export default function AddPatientForm(props: AddPatientFormProps) {
    const usernameInput = useRef<HTMLInputElement>(null);
    const passwordInput1 = useRef<HTMLInputElement>(null);
    const passwordInput2 = useRef<HTMLInputElement>(null);

    const [error, setError] = useState<unknown>(null);

    const handleNewPatient: React.FormEventHandler<HTMLFormElement> = async (e) => {
        e.preventDefault();
        setError(null);

        // grab input values
        const username = usernameInput.current?.value;
        const password = passwordInput1.current?.value;
        const password2 = passwordInput2.current?.value;

        if (!username || !password || !password2) return setError("All fields are required");
        if (password !== password2) return setError("Passwords do not match");
        if (/\s/.test(username)) return setError("Username should not contain whitespace");

        const createUserPromise = axios.post<any, AxiosResponse<CreateUserResponse>, CreateUserRequest>(
            "/api/create-user",
            {
                username,
                password,
                creator: props.therapistUid,
            },
            {
                validateStatus: (status) => true,
            }
        );

        const { data } = await createUserPromise;

        // display error if present
        if (data.code < 200 || data.code > 299) {
            setError(data.message);
        } else {
            props.refresh();

            // reset form
            usernameInput.current.value = "";
            passwordInput1.current.value = "";
            passwordInput2.current.value = "";
        }
    };

    return (
        <div className="w-full max-w-sm p-4 bg-white border border-gray-200 rounded-lg shadow sm:p-6 md:p-8 ">
            <form className="space-y-6" onSubmit={handleNewPatient}>
                <h5 className="text-xl font-medium text-gray-900">Add a Patient</h5>
                <div>
                    <label htmlFor="username" className="block mb-2 text-sm font-medium text-gray-900">
                        Username
                    </label>
                    <input
                        ref={usernameInput}
                        type="text"
                        name="username"
                        id="username"
                        className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                        placeholder="cool-white-lamp"
                        required
                    />
                </div>
                <div>
                    <label htmlFor="password" className="block mb-2 text-sm font-medium text-gray-900">
                        Your password
                    </label>
                    <input
                        ref={passwordInput1}
                        type="password"
                        name="password"
                        id="password"
                        placeholder="••••••••"
                        className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                        required
                    />
                </div>
                <div>
                    <label htmlFor="password" className="block mb-2 text-sm font-medium text-gray-900">
                        Retype password
                    </label>
                    <input
                        ref={passwordInput2}
                        type="password"
                        name="password"
                        id="password"
                        placeholder="••••••••"
                        className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                        required
                    />
                </div>
                <FirebaseErrorPane err={error} />
                <button
                    type="submit"
                    className="w-full text-white bg-sp1 hover:bg-green-800 focus:ring-4 focus:outline-none focus:bg-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                >
                    Create
                </button>
            </form>
        </div>
    );
}
