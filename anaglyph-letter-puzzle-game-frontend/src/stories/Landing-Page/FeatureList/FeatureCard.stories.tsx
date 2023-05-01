import FeatureCard from "../../../components/landing-page/FeatureList/FeatureCard";

import { FaReact } from "react-icons/fa";

export default {
    title: "FeatureCard",
    component: FeatureCard,
    tags: ["autodocs"],
};

interface DefaultArgs {
    statement: string;
}

export const Default = ({ statement }: DefaultArgs) => <FeatureCard name="Feature" statement={statement} icon={<FaReact size={36} />} />;

Default.args = {
    statement: "This is a simple statement describing your features",
    icon: { control: null },
};
