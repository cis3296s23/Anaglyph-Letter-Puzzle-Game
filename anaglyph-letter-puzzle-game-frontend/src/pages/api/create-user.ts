import type { NextApiRequest, NextApiResponse } from "next";

// service account cred (secret)
// import SV from "../../../credentials/ServiceAccount";

// firebase admin to help create users
// import { initializeApp, ServiceAccount, getApps } from "firebase-admin/app";
// import { credential } from "firebase-admin";

// used to create users
// import { getAuth } from "firebase-admin/auth";

// if the firebase-admin SDK is already active in the current instance of the edge function DO NOT recreate it
// if (!getApps()) initializeApp({ credential: credential.cert(SV as ServiceAccount) });

import { doc, getDoc, setDoc } from "firebase/firestore";
import { db } from "../../../firebase.config";

export interface CreateUserResponse {
    message: string;
    code: number;
}

export interface CreateUserRequest {
    username: string;
    password: string;
    creator: string;
}

/**
 * Api endpoint to create a user via a Post Request
 * Post body should be
 *      {username, password, creator}
 */
export default async function handler(req: NextApiRequest, res: NextApiResponse<CreateUserResponse>) {
    // reject all requests with no data
    if (req.method != "POST") return res.status(400).json({ message: "Request should be method=Post", code: 400 });

    const { body } = req;

    // reject all invalid requests with invalid fields
    if (!body.username) return res.status(400).json({ message: "username not presented", code: 400 });
    if (!body.password) return res.status(400).json({ message: "password not presented", code: 400 });
    if (!body.creator) return res.status(400).json({ message: "creator-email not presented", code: 400 });
    // send data to firebase
    const userRef = doc(db, process.env.NEXT_PUBLIC_ROOT_USER_COLLECTION as string, body.username as string);

    // check if username exists
    try {
        const userData = await getDoc(userRef);
        if (userData.exists()) return res.status(418).json({ message: "Username already exists", code: 418 });
    } catch (err) {
        return res.status(500).json({ message: "Firebase Error", code: 500 });
    }

    // catch firebase errors
    try {
        await setDoc(userRef, { username: body.username, password: body.password, creator: body.creator, created: Date.now() });
    } catch (err) {
        return res.status(500).json({ message: "Firebase Error", code: 500 });
    }

    // send success message
    return res.status(201).json({ message: "User Created", code: 201 });
}
