import { User } from "firebase/auth";
import { DocumentData } from "firebase/firestore";
import React, { useEffect, useState } from "react";
import axios, { AxiosResponse } from "axios";
import { GetUserResponse } from "@/pages/api/get-users";
import { PatientUser } from "@/types/db";
import PatientCards from "./PatientCard";
import AddPatientForm from "./AddPatientForm";

export interface PatientsProps {
    user: User | undefined | null;
}

export default function Patients(props: PatientsProps) {
    // undefined signifies loading
    const [users, setUsers] = useState<PatientUser[] | undefined | null>(null);
    const [count, setCount] = useState(0);

    useEffect(() => {
        // dont send request on empty user
        if (!props.user) {
            return;
        }

        const getUsers = axios.get<never, AxiosResponse<GetUserResponse>>(`/api/get-users?creator=${props.user.uid}`);

        // update state if data was received
        getUsers.then((response) => {
            if (response.data.users) return setUsers(response.data.users as PatientUser[]);
            else return setUsers(undefined);
        });
    }, [props.user, count]);

    if (!props.user) {
        return null;
    }

    // function reloads the user data
    const refresh = () => setCount((count) => count + 1);

    return (
        <div className="flex gap-10 mt-10 justify-center mid-max:flex-col mid-max:items-center mb-20">
            <AddPatientForm therapistUid={props.user?.uid} refresh={refresh} />
            <div className="flex flex-col gap-4">
                <h2 className="font-semibold text-2xl">Your Patients</h2>
                {users && <PatientCards users={users} refresh={refresh} />}
            </div>
        </div>
    );
}
