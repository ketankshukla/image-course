import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    // Build-time flattened WebP assets already have dimensions and CDN caching.
    // Avoid runtime image transformations and their deployment cost.
    unoptimized: true,
  },
};

export default nextConfig;
