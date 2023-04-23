import type { NextApiRequest, NextApiResponse } from "next";
import { query, collection, where, getDocs, DocumentData } from "firebase/firestore";
import { db } from "../../../firebase.config";

export type GetUsersResponse = {
    message: string;
    code: number;
    users?: DocumentData[];
};

/**
 * Api endpoint to create a user via a Get Request
 * Get should include a creator
 */
export default async function handler(req: NextApiRequest, res: NextApiResponse<GetUsersResponse>) {
    // reject all requests with no data
    const { creator } = req.query;

    // reject if no query points are provided
    if (!creator) return res.status(400).json({ message: "Request missing creator param", code: 400 });

    const usersColl = collection(db, process.env.NEXT_PUBLIC_ROOT_USER_COLLECTION as string);
    const creatorQuery = query(usersColl, where("creator", "==", creator));

    try {
        // attempt to fetch all documents
        const querySnapShot = await getDocs(creatorQuery);

        // save all to array and send it
        const users: DocumentData[] = [];
        querySnapShot.forEach((doc) => users.push(doc.data()));

        // send back data
        return res.status(200).json({ message: "OK", code: 200, users });
    } catch (err) {
        return res.status(500).json({ message: "Firebase Error", code: 500 });
    }
}
