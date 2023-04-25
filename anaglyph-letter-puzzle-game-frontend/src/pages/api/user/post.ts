import { doc, DocumentData, getDoc, setDoc } from "firebase/firestore";
import type { NextApiRequest, NextApiResponse } from "next";
import { db } from "../../../../firebase.config";

export interface PostUserResponse {
    message: string;
    code: number;
    data?: DocumentData;
}

export type PostUserRequest = DocumentData;

/**
 * API endpoint for updating user data via query params
 */
export default async function handler(req: NextApiRequest, res: NextApiResponse<PostUserResponse>) {
    // reject all requests with no data
    const { username } = req.query;

    if (req.method !== "POST" || !req.body) {
        return res.status(400).json({ message: "Request should be of type POST, missing request body", code: 400 });
    }

    // reject if no query points are provided
    if (!username) return res.status(400).json({ message: "Request missing username param", code: 400 });

    const userData = doc(db, process.env.NEXT_PUBLIC_ROOT_USER_COLLECTION as string, username as string);

    // check if document even exists
    try {
        const userDocument = await getDoc(userData);
        if (!userDocument.exists()) return res.status(404).json({ message: `${username} does not exist`, code: 404 });
    } catch (error) {
        return res.status(500).json({ message: "Firebase Error", code: 500 });
    }

    // set document
    try {
        const { body } = req;
        await setDoc(userData, { ...body, lastUpdated: Date.now() }, { merge: true });
        return res.status(200).json({ message: "OK", code: 200, data: body });
    } catch (error) {
        return res.status(500).json({ message: "Firebase Error", code: 500 });
    }
}
