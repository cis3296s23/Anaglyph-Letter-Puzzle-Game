import { DeleteUserResponse } from "@/pages/api/delete-user";
import { PatientUser } from "@/types/db";
import axios, { AxiosResponse } from "axios";
import React from "react";

import { TbTrashXFilled } from "react-icons/tb";
import { FaUserEdit } from "react-icons/fa";

export interface PatientCardProps {
    users: PatientUser[];
    refresh: () => void;
    handleEditUser: (username: string | null) => void;
}

export default function PatientCards(props: PatientCardProps) {
    const handleDelete = async (username: string) => {
        // props.refresh()
        const deleteUserPromise = axios.delete<any, AxiosResponse<DeleteUserResponse>>(`/api/delete-user?username=${username}`, {
            validateStatus: (status) => true,
        });

        const { data } = await deleteUserPromise;

        if (data.code > 199 || data.code < 300) {
            props.refresh();
        }
    };

    return (
        <div className="relative overflow-x-auto shadow-md sm:rounded-lg">
            <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" className="px-6 py-3">
                            Username
                        </th>
                        <th scope="col" className="px-6 py-3">
                            Password
                        </th>
                        <th scope="col" className="px-6 py-3">
                            Date Created
                        </th>
                        <th scope="col" className="px-6 py-3">
                            Delete
                        </th>
                        <th scope="col" className="px-6 py-3">
                            Edit
                        </th>
                    </tr>
                </thead>
                <tbody>
                    {props.users.map((user) => (
                        <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700" key={user.username}>
                            <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                {user.username}
                            </th>
                            <td className="px-6 py-4">{user.password}</td>
                            <td className="px-6 py-4">{new Date(user.created).toLocaleDateString()}</td>
                            <td className="px-6 py-4 text-center">
                                <button type="button" onClick={() => handleDelete(user.username)}>
                                    <TbTrashXFilled size={20} className="text-rose-500 hover:text-rose-700" />
                                </button>
                            </td>
                            <td className="px-6 py-4 text-center">
                                <button type="button" onClick={() => props.handleEditUser(user.username)}>
                                    <FaUserEdit size={20} className="text-blue-500 hover:text-blue-700" />
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}
