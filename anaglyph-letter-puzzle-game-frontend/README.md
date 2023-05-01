# Website Documentation

The website is powered by NextJS which is a wrapper over ReactJS to provide alternate hydration methods rather than just client-side rendering. NextJS also provides a ready-to-use API layer to setup serverless functions for your website to call.

## Install Dependencies

To run this website you must have node and NPM installed. You can get Node from their [website](https://nodejs.org/en/download) and it should come with NPM.

```
npm i
```

## Run the development server

You can run the development server with:

```
npm run dev
```

## Run the Docs Server

To see the docs for the React Components Used. Run the docs server on localhost via:

```
npm run storybook
```

## UML Diagram

Here is a UML CLass Diagram based on the Website's Frontend. Many imports are left out because they are usually assumed with react usage or they would just clutter up the diagram.

![UML_DIAGRAM](./public/FE-UML.svg)

> If the above SVG image does not load you can obtain the PNG image from [here](./public/FE-UML.png)