// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from "next";

// service account cred (secret)
import SV from "../../../credentials/ServiceAccount";

// firebase admin to help create users
import { initializeApp, ServiceAccount, getApps } from "firebase-admin/app";
import { credential } from "firebase-admin";

// if the firebase-admin SDK is already active in the current instance of the edge function DO NOT recreate it
if (!getApps()) initializeApp({ credential: credential.cert(SV as ServiceAccount) });

type Data = {
    name: string;
};

export default function handler(req: NextApiRequest, res: NextApiResponse<Data>) {
    res.status(200).json({ name: "hi" });
}
