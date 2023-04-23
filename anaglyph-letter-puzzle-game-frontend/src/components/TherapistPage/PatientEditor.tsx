import { PatientEditorReducer } from "@/hooks/PatientEditorReducer";
import { GetUserResponse } from "@/pages/api/user/get";
import { PostUserRequest, PostUserResponse } from "@/pages/api/user/post";
import { filterAndReorderUserData } from "@/util";
import axios, { AxiosResponse } from "axios";
import { FirebaseError } from "firebase/app";
import { DocumentData } from "firebase/firestore";
import React, { useEffect, useReducer, useState } from "react";
import FirebaseErrorPane from "../ErrorPane/FirebaseErrorPane";

interface PatientEditorProps {
    username: string;
}

export default function PatientEditor({ username }: PatientEditorProps) {
    const [userState, dispatch] = useReducer(PatientEditorReducer, {});
    const [error, setError] = useState<unknown>(null);

    // re-render component on user changes
    useEffect(() => {
        if (!username) return;

        // attempt to get user data
        const __userData = axios.get<never, AxiosResponse<GetUserResponse>>(`/api/user/get?username=${username}`, {
            validateStatus: (status) => true,
        });

        // validate and save to local state
        __userData.then((resp) => {
            const response = resp.data;

            if (response.code === 200) {
                // all 200 status codes will contain DocumentData
                dispatch({ type: "REPLACE", payload: response.data as DocumentData });
            }
        });
    }, [username]);

    // render nothing on no data
    if (!Object.keys(userState)) {
        return null;
    }

    const handleEditorSubmit: React.FormEventHandler<HTMLFormElement> = async (e) => {
        e.preventDefault(); // no page refresh
        const options = {
            validateStatus: (status: number) => true,
        };
        const saveAction = await axios.post<any, AxiosResponse<PostUserResponse>, PostUserRequest>(
            `/api/user/post?username=${username}`,
            userState,
            options
        );

        // display error message if needed
        const { code } = saveAction.data;
        if (code !== 200) {
            return setError(saveAction.data.message);
        }
    };

    return (
        <form onSubmit={handleEditorSubmit}>
            <label htmlFor="disabled-input" className="block mb-2 text-sm font-medium text-gray-900">
                Username
            </label>
            <input
                type="text"
                id="disabled-input"
                aria-label="disabled input"
                className="mb-6 bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 cursor-not-allowed "
                defaultValue={userState["username"]}
                disabled
                readOnly
            ></input>
            {filterAndReorderUserData(Object.keys(userState)).map((key) => (
                <div className="mb-6" key={key}>
                    <label htmlFor={key} className="block mb-2 text-sm font-medium text-gray-900">
                        {key}
                    </label>
                    <input
                        type="text"
                        id={key}
                        className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                        defaultValue={`${userState[key]}`}
                        onChange={(e) => dispatch({ type: key, payload: e.target.value })}
                    />
                </div>
            ))}
            <FirebaseErrorPane err={error} />
            <button
                type="submit"
                className="focus:outline-none text-white bg-sp1 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2"
            >
                Save Patient Data
            </button>
        </form>
    );
}
