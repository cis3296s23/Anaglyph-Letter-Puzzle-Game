import { doc, DocumentData, getDoc } from "firebase/firestore";
import type { NextApiRequest, NextApiResponse } from "next";
import { db } from "../../../../firebase.config";

export interface GetUserResponse {
    message: string;
    code: number;
    data?: DocumentData;
}

export interface GetUserRequest {
    username: string;
}

/**
 * API endpoint for getting user data via query params
 */
export default async function handler(req: NextApiRequest, res: NextApiResponse<GetUserResponse>) {
    // reject all requests with no data
    const { username } = req.query;

    // reject if no query points are provided
    if (!username) return res.status(400).json({ message: "Request missing username param", code: 400 });

    const userData = doc(db, process.env.NEXT_PUBLIC_ROOT_USER_COLLECTION as string, username as string);

    // check if document even exists
    try {
        const userDocument = await getDoc(userData);
        // if it exists return to user
        if (userDocument.exists()) return res.status(200).json({ message: "OK", code: 200, data: userDocument.data() });

        // report error if it doesnt exist
        return res.status(404).json({ message: `${username} does not exist`, code: 404 });
    } catch (error) {
        return res.status(500).json({ message: "Firebase Error", code: 500 });
    }
}
