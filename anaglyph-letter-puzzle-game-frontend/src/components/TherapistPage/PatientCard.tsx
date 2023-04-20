import { PatientUser } from "@/types/db";
import { userAgent } from "next/server";
import React from "react";

export interface PatientCardProps {
    user: PatientUser;
}

export default function PatientCard(props: PatientCardProps) {
    return (
        <section>
            <p>{props.user.username}</p>
            <p>{props.user.password}</p>
        </section>
    );
}
