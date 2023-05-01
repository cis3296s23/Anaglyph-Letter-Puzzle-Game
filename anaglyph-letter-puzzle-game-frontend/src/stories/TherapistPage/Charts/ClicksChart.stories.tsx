import ClicksChart, { ClickCartDataDtype } from "../../../components/TherapistPage/Charts/ClicksChart";

export default {
    title: "ClicksChart",
    component: ClicksChart,
    tags: ["autodocs"],
};

const data = [
    {
        correct: 5,
        total: 8,
    },
    {
        correct: 4,
        total: 7,
    },
    {
        correct: 6,
        total: 8,
    },
    {
        correct: 7,
        total: 9,
    },
    {
        correct: 11,
        total: 12,
    },
    {
        correct: 12,
        total: 13,
    },
];

/**
 * Chart filled with random increasing data
 */
export const ExampleChart = ({ data }: { data: ClickCartDataDtype[] }) => <ClicksChart data={data} />;
ExampleChart.args = {
    data,
};
