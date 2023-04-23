import { PatientEditorReducer } from "@/hooks/PatientEditorReducer";
import { GetUserResponse } from "@/pages/api/user/get";
import { PostUserRequest, PostUserResponse } from "@/pages/api/user/post";
import { filterAndReorderUserData } from "@/util";
import axios, { AxiosResponse } from "axios";
import { DocumentData } from "firebase/firestore";
import React, { useEffect, useReducer, useState } from "react";
import FirebaseErrorPane from "../ErrorPane/FirebaseErrorPane";

import { GrClose } from "react-icons/gr";
import LoadingOverlaySpinner from "../Loading/LoadingOverlaySpinner";

interface PatientEditorProps {
    username: string | null;
    closeModel: () => void;
    refresh: () => void;
}

export default function PatientEditor({ username, closeModel, refresh }: PatientEditorProps) {
    const [userState, dispatch] = useReducer(PatientEditorReducer, {});
    const [error, setError] = useState<unknown>(null);

    const [isLoading, setIsLoading] = useState(true);

    // re-render component on user changes
    useEffect(() => {
        if (!username) return;

        setIsLoading(true);
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
            setIsLoading(false);
        });
    }, [username]);

    // render nothing on no data
    if (!Object.keys(userState) || !username) {
        return null;
    }

    const handleEditorSubmit: React.FormEventHandler<HTMLFormElement> = async (e) => {
        e.preventDefault(); // no page refresh
        setIsLoading(true);
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
        setIsLoading(false);
        refresh()
    };

    return (
        <section className="bg-white rounded-lg shadow-lg font-inter w-96 relative min-h-[324px]">
            {isLoading && <LoadingOverlaySpinner />}
            <form onSubmit={handleEditorSubmit} className="px-4 py-6">
                <h2 className="font-semibold text-xl pb-3">
                    Editing User: <span className="font-bold">{userState.username}</span>
                </h2>
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
                            id={"x"}
                            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                            placeholder={`${isLoading ? "Loading..." : userState[key]}`}
                            onChange={(e) => dispatch({ type: key, payload: e.target.value })}
                        />
                    </div>
                ))}
                <FirebaseErrorPane err={error} />
                <button
                    type="submit"
                    className="w-full focus:outline-none text-white bg-sp1 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2"
                >
                    Save Patient Data
                </button>
            </form>
            <GrClose size={20} color="black" onClick={closeModel} className="absolute top-4 right-4 hover:cursor-pointer" />
        </section>
    );
}
