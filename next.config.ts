import type { NextConfig } from "next";
const pages = ["administration", "entretien", "services-generaux", "realisations", "a-propos", "soumission"];
const config: NextConfig = {
 output: "standalone",
 async redirects() { return [
 { source: "/index.html", destination: "/", permanent: true },
 { source: "/site/index.html", destination: "/", permanent: true },
 ...pages.flatMap(page => [
 { source: `/${page}.html`, destination: `/${page}`, permanent: true },
 { source: `/site/${page}.html`, destination: `/${page}`, permanent: true },
 ]),
 { source: "/:path*", has: [{ type: "host", value: "www.gnhorizon.ca" }], destination: "https://gnhorizon.ca/:path*", permanent: true },
 ]; },
 async rewrites() { return { beforeFiles: [
 { source: "/", destination: "/site/index.html" },
 ...pages.map(page => ({ source: `/${page}`, destination: `/site/${page}.html` })),
 ] }; },
};
export default config;
