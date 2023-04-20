import { User } from "firebase/auth";
import { DocumentData } from "firebase/firestore";
import React, { useEffect, useState } from "react";
import axios, { AxiosResponse } from "axios";
import { GetUserResponse } from "@/pages/api/get-users";
import { PatientUser } from "@/types/db";
import PatientCard from "./PatientCard";
import AddPatientForm from "./AddPatientForm";

interface PatientsProps {
    user: User | undefined | null;
}

export default function Patients(props: PatientsProps) {
    // undefined signifies loading
    const [users, setUsers] = useState<PatientUser[] | undefined | null>(null);

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
    }, [props.user]);

    if (!props.user) {
        return null;
    }

    return (
        <div className="flex gap-10 mt-10">
            <AddPatientForm therapistUid={props.user?.uid} />
            {users?.map((user) => (
                <PatientCard user={user} key={user.username} />
            ))}
        </div>
    );
}
