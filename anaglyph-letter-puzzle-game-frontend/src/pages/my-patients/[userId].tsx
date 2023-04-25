import FirebaseErrorPane from "@/components/ErrorPane/FirebaseErrorPane";
import LoadingSpinner from "@/components/Loading/LoadingSpinner";
import InfoDashBoard from "@/components/TherapistPage/InfoDashBoard";
import axios, { AxiosResponse } from "axios";
import { getAuth } from "firebase/auth";
import { DocumentData } from "firebase/firestore";
import { useRouter } from "next/router";
import React, { useEffect, useState } from "react";
import { useAuthState } from "react-firebase-hooks/auth";
import app from "../../../firebase.config";
import { GetUserResponse } from "../api/user/get";

export default function UserId() {
    // reject invalid users
    const auth = getAuth(app);
    const [authUser] = useAuthState(auth);

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
        setIsLoading(true);
        if (!userId || !authUser) return;

        // attempt to get user data
        const __userData = axios.get<never, AxiosResponse<GetUserResponse>>(`/api/user/get?username=${userId}`, {
            validateStatus: (status) => true,
        });

        // validate and save to local state
        __userData.then((resp) => {
            const response = resp.data;

            // if the resp was valid check if current user should be able to see it
            if (response.code === 200 && response.data) {
                // uncomment if you want people NOT TO BE ABLE to view patient data just by sharing URLs
                // if (response.data.creator === authUser.uid) setUser(response.data);
                // else setError(`Nice try editing the URL`);
                setUser(response.data);
            } else {
                setError(`${response.code} ${response.message}`);
            }

            setIsLoading(false);
        });
    }, [userId, authUser]);

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
