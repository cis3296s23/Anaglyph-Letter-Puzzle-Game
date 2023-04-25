import { DeleteUserResponse } from "@/pages/api/delete-user";
import { PatientUser } from "@/types/db";
import axios, { AxiosResponse } from "axios";
import React from "react";

import { TbTrashXFilled } from "react-icons/tb";
import { FaUserEdit } from "react-icons/fa";
import { AiFillEye } from "react-icons/ai";
import Link from "next/link";

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
            <table className="w-full text-sm text-left text-gray-500">
                <thead className="text-xs text-gray-700 uppercase bg-gray-50">
                    <tr>
                        <th scope="col" className="px-6 py-3 xs2-max:px-3">
                            Username
                        </th>
                        <th scope="col" className="px-6 py-3 md-max:hidden">
                            Password
                        </th>
                        <th scope="col" className="px-6 py-3 md-max:hidden">
                            Date Created
                        </th>
                        <th scope="col" className="px-6 py-3 xs2-max:px-3">
                            Delete
                        </th>
                        <th scope="col" className="px-6 py-3 xs2-max:px-3">
                            Edit
                        </th>
                        <th scope="col" className="px-6 py-3 xs2-max:px-3">
                            View Info
                        </th>
                    </tr>
                </thead>
                <tbody>
                    {props.users.map((user) => (
                        <tr className="bg-white border-b" key={user.username}>
                            <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap xs2-max:px-3">
                                {user.username}
                            </th>
                            <td className="px-6 py-4 md-max:hidden xs2-max:px-3">{user.password}</td>
                            <td className="px-6 py-4 md-max:hidden xs2-max:px-3">{new Date(user.created).toLocaleDateString()}</td>
                            <td className="px-6 py-4 text-center xs2-max:px-3">
                                <button type="button" onClick={() => handleDelete(user.username)}>
                                    <TbTrashXFilled size={20} className="text-rose-500 hover:text-rose-700" />
                                </button>
                            </td>
                            <td className="px-6 py-4 text-center xs2-max:px-3">
                                <button type="button" onClick={() => props.handleEditUser(user.username)}>
                                    <FaUserEdit size={20} className="text-blue-500 hover:text-blue-700" />
                                </button>
                            </td>
                            <td className="px-6 py-4 text-center xs2-max:px-3">
                                <Link type="button" href={`/my-patients/${user.username}`} className="w-full flex justify-center">
                                    <AiFillEye size={20} className="text-gray-500 hover:text-black" />
                                </Link>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}
