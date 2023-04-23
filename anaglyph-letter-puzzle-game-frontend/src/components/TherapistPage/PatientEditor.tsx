import { DocumentData } from "firebase/firestore";
import React, { useEffect, useState } from "react";
import { PatientsProps } from "./PatientsDisplay";

export default function PatientEditor({ user }: PatientsProps) {
    const [userData, setUserData] = useState<DocumentData | null>(null);

	// re-render component on user changes
    useEffect(() => {
        if (!user) return;

		

    }, [user]);

    return <div>PatientEditor</div>;
}
