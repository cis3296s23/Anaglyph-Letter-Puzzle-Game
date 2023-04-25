import FirebaseErrorPane from "@/components/ErrorPane/FirebaseErrorPane";
import LoadingSpinner from "@/components/Loading/LoadingSpinner";
import InfoDashBoard from "@/components/TherapistPage/InfoDashBoard";
import axios, { AxiosResponse } from "axios";
import { DocumentData } from "firebase/firestore";
import { useRouter } from "next/router";
import React, { useEffect, useState } from "react";
import { GetUserResponse } from "../api/user/get";

export default function UserId() {
    // read url params
    const router = useRouter();
    const { userId } = router.query;

    // control display
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState<unknown>(null);

    // save user data
    const [user, setUser] = useState<DocumentData | undefined>(undefined);

    // re-render component on user changes
    useEffect(() => {
        if (!userId) return;

        setIsLoading(true);
        // attempt to get user data
        const __userData = axios.get<never, AxiosResponse<GetUserResponse>>(`/api/user/get?username=${userId}`, {
            validateStatus: (status) => true,
        });

        // validate and save to local state
        __userData.then((resp) => {
            const response = resp.data;

            if (response.code === 200) {
                setUser(response.data);
            } else {
                setError(`${response.code} ${response.message}`);
            }

            setIsLoading(false);
        });
    }, [userId]);

    const LoadingState = isLoading && (
        <div className="absolute top-0 left-0 w-full min-h-screen flex justify-center items-center">
            <LoadingSpinner />
        </div>
    );

    return (
        <section className="mx-auto w-[1200px] lg-max:w-full xl-max:w-[1000px] font-inter">
            {LoadingState}
            <FirebaseErrorPane err={error} />
            {!isLoading && user && <InfoDashBoard user={user} />}
        </section>
    );
}
