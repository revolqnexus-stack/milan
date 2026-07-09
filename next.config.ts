import type { NextConfig } from "next";
import path from "path";

const nextConfig: NextConfig = {
  outputFileTracingRoot: path.join(__dirname),
  async redirects() {
    return [
      { source: "/chn", destination: "/app.html", permanent: false },
      { source: "/study", destination: "/app.html", permanent: false },
    ];
  },
};

export default nextConfig;
