import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from "recharts";
import React, { useEffect, useState } from "react";
import { DocumentData } from "firebase/firestore";

export interface ClickCartDataDtype {
    correct: number;
    total: number;
}

export interface ClicksChartProps {
    data: DocumentData[];
}

interface DBClickArrayElement {
    Day: number;
    total: number | undefined;
    correct: number | undefined;
}

interface DBAccArrayElement {
    Day: number;
    acc: number;
}

const Title = ({ title }: { title: string }) => <h2 className="text-xl font-medium mt-3 mb-4 xs1-max:px-4">{title} </h2>;

/**
 * Generates a chart given an array of `{correct: number, total: number}` objects
 */
export default function ClicksChart(props: ClicksChartProps) {
    const [clickData, setClickData] = useState<DBClickArrayElement[]>([]);
    const [accData, setAccData] = useState<DBAccArrayElement[]>([]);

    useEffect(() => {
        const __clickData: DBClickArrayElement[] = [];
        const __accData: DBAccArrayElement[] = [];

        // reject if not array type
        if (!Array.isArray(props.data)) return;

        props.data.forEach((clickDetail, i) => {
            // reject if entries are missing
            if (!clickDetail.correct || !clickDetail.total) return;

            // convert types
            const correct = parseInt(clickDetail.correct);
            const total = parseInt(clickDetail.total);

            // check if type was coerced correctly
            if (isNaN(correct) || isNaN(total)) return;

            __clickData.push({ Day: i, correct, total });

            if (total > 0) __accData.push({ Day: i, acc: correct / total });
        });

        setClickData(__clickData);
        setAccData(__accData);
    }, [props.data]);

    return (
        <section className="">
            {clickData && (
                <div className="my-6">
                    <Title title="Total Clicks vs Correct Clicks" />
                    <ResponsiveContainer minWidth={250} minHeight={300}>
                        <LineChart
                            width={500}
                            height={300}
                            data={clickData}
                            margin={{
                                top: 5,
                                right: 30,
                                left: 20,
                                bottom: 5,
                            }}
                        >
                            <CartesianGrid strokeDasharray="3 3" />
                            <XAxis dataKey="Day" />
                            <YAxis />
                            <Tooltip />
                            <Legend />
                            <Line type="monotone" dataKey="total" stroke="#8884d8" />
                            <Line type="monotone" dataKey="correct" stroke="#82ca9d" />
                        </LineChart>
                    </ResponsiveContainer>
                </div>
            )}
            {accData && (
                <div className="my-6">
                    <Title title="Accuracy" />
                    <ResponsiveContainer minWidth={250} minHeight={300}>
                        <LineChart
                            width={500}
                            height={300}
                            data={accData}
                            margin={{
                                top: 5,
                                right: 30,
                                left: 20,
                                bottom: 5,
                            }}
                        >
                            <CartesianGrid strokeDasharray="3 3" />
                            <XAxis dataKey="Day" />
                            <YAxis />
                            <Tooltip />
                            <Legend />
                            <Line type="monotone" dataKey="acc" stroke="#8884d8" />
                        </LineChart>
                    </ResponsiveContainer>
                </div>
            )}
        </section>
    );
}
