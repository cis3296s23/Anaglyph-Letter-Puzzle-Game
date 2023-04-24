import { filterAndReorderUserData, filterUserData, reorderUserData } from "@/util";
import React from "react";

export default function PatientInfoToTableView({ obj }: { obj: Record<any, any> }) {
    const used = ["username", "password", "created", "lastUpdated"];

    return (
        <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
            <thead className="text-xs text-gray-700 uppercase bg-gray-100 dark:bg-gray-700 dark:text-gray-400">
                <tr>
                    <th scope="col" className="px-6 py-3 rounded-l-lg">
                        Attribute
                    </th>
                    <th scope="col" className="px-6 py-3">
                        Saved Value
                    </th>
                </tr>
            </thead>
            <tbody className="border-b-[1px]">
                <tr className="bg-white dark:bg-gray-800">
                    <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                        Username
                    </th>
                    <td className="px-6 py-4 whitespace-pre-wrap">{obj.username ?? "error"}</td>
                </tr>
            </tbody>
            <tbody className="border-b-[1px]">
                <tr className="bg-white dark:bg-gray-800">
                    <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                        Password
                    </th>
                    <td className="px-6 py-4 whitespace-pre-wrap">{obj.password ?? "error"}</td>
                </tr>
            </tbody>
            <tbody className="border-b-[1px]">
                <tr className="bg-white dark:bg-gray-800">
                    <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                        Date Created
                    </th>
                    <td className="px-6 py-4 whitespace-pre-wrap">{new Date(obj.created).toLocaleDateString()}</td>
                </tr>
            </tbody>
            <tbody className="border-b-[1px]">
                <tr className="bg-white dark:bg-gray-800">
                    <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                        LastUpdated
                    </th>
                    <td className="px-6 py-4 whitespace-pre-wrap">{new Date(obj.lastUpdated).toLocaleDateString()}</td>
                </tr>
            </tbody>
            {filterUserData(Object.keys(obj), used).map((key) => (
                <tbody className="border-b-[1px]" key={key}>
                    <tr className="bg-white dark:bg-gray-800">
                        <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            {key}
                        </th>
                        <td className="px-6 py-4 whitespace-pre-wrap">{obj[key]}</td>
                    </tr>
                </tbody>
            ))}
        </table>
    );
}
