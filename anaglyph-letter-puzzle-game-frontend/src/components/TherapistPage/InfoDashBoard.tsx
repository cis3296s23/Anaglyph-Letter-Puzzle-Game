import { DocumentData } from "firebase/firestore";
import React from "react";
import PatientInfoToTableView from "../Util/ObjectToTableView";
import ClicksChart from "./Charts/ClicksChart";

export interface InfoDashBoardProps {
    user: DocumentData;
}

export default function InfoDashBoard({ user }: InfoDashBoardProps) {
    console.log(user.clicks);
    return (
        <div className="lg-max:p-4">
            <h1 className="font-semibold text-2xl py-6">Patient Info: {user.username}</h1>
            <PatientInfoToTableView obj={user} />
            {user.clicks && <ClicksChart data={user.clicks} />}
        </div>
    );
}
