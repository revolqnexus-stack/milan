import type { NextConfig } from "next";
import path from "path";

const nextConfig: NextConfig = {
  outputFileTracingRoot: path.join(__dirname),
  serverExternalPackages: ["@node-rs/argon2"],
  async redirects() {
    return [
      { source: "/app.html", destination: "/library", permanent: false },
      { source: "/chn", destination: "/library", permanent: false },
    ];
  },
};

export default nextConfig;
