import { User } from "firebase/auth";
import { DocumentData } from "firebase/firestore";
import React, { useEffect, useState } from "react";
import axios from "axios";
import { GetUserResponse } from "@/pages/api/get-users";

interface PatientsProps {
    user: User | undefined | null;
}

export default function Patients(props: PatientsProps) {
    const [users, setUsers] = useState<DocumentData[]>([]);

    useEffect(() => {
        // dont send request on empty user
        if (!props.user) {
            return;
        }

        const getUsers = axios.get(`/api/get-users?creator=${props.user.uid}`);

        // update state if data was received
        getUsers.then((response) => {
            setUsers(response.data.users);
        });
    }, [props.user]);

    return <div>Patients</div>;
}
