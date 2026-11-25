import type { NextConfig } from "next";
const pages = ["administration", "entretien", "services-generaux", "realisations", "a-propos", "soumission"];
const config: NextConfig = {
 output: "standalone",
 async rewrites() { return { beforeFiles: [
 { source: "/", destination: "/site/index.html" },
 ...pages.map(page => ({ source: `/${page}`, destination: `/site/${page}.html` })),
 ] }; },
};
export default config;
