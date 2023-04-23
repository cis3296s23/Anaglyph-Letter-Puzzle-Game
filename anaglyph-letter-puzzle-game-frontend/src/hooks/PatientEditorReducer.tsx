import { DocumentData } from "firebase/firestore";

interface ActionType {
    type: string | "REPLACE";
    payload: any;
}

// loosely typed reducer
export function PatientEditorReducer(state: DocumentData, action: ActionType) {
    // replace state
    if (action.type === "REPLACE") {
        return { ...action.payload };
    }

    return { ...state, [action.type]: action.payload };
}
