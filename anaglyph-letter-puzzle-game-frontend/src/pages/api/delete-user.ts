import type { NextApiRequest, NextApiResponse } from "next";
import { deleteDoc, doc, getDoc } from "firebase/firestore";
import { db } from "../../../firebase.config";

export type DeleteUserResponse = {
    message: string;
    code: number;
};

/**
 * Api endpoint to create a user via a Get Request
 * Get should include a creator
 */
export default async function handler(req: NextApiRequest, res: NextApiResponse<DeleteUserResponse>) {
    // reject all requests with no data
    const { username } = req.query;

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

    // del document
    try {
        await deleteDoc(userData);
        return res.status(200).json({ message: "Deleted", code: 200 });
    } catch (error) {
        return res.status(500).json({ message: "Firebase Error", code: 500 });
    }
}
