import ErrorPane from "../../components/ErrorPane/ErrorPane";

export default {
    title: "ErrorPane",
    component: ErrorPane,
    tags: ["autodocs"],
};

export const Default = () => <ErrorPane error="This is what an error component looks like!" />;
