import PatientEditor from "@/components/TherapistPage/PatientEditor";
import PatientsDisplay from "@/components/TherapistPage/PatientsDisplay";
import { getAuth } from "firebase/auth";
import { useRouter } from "next/router";
import { useAuthState } from "react-firebase-hooks/auth";
import app from "../../firebase.config";

export default function MyPatients() {
    const router = useRouter();
    // need auth status to display the login status
    const auth = getAuth(app);
    const [user, loading, error] = useAuthState(auth);

    // reject if there is an error loading or the load results in no user
    if (!loading && (error || !user)) {
        router.push("/");
        return null;
    }

    return (
        <section className="mx-auto w-[1200px] lg-max:w-full xl-max:w-[1000px] font-inter">
            <PatientsDisplay user={user} />
        </section>
    );
}
