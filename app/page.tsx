import CourseClient from "@/app/components/CourseClient";
import rawManifest from "@/data/manifest.json";
import { SiteManifest } from "@/lib/types";

export default function Home() {
  const manifest = rawManifest as unknown as SiteManifest;

  return <CourseClient manifest={manifest} />;
}
