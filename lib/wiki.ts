import entries from "@/data/wiki.json";

export type WikiEntry = (typeof entries)[number];
export const wikiEntries: WikiEntry[] = entries;
export const wikiUrl = (slug = "") => `https://wiki.ketanshukla.dev${slug ? `/${slug}` : ""}`;
export const courseUrl = "https://course.ketanshukla.dev";
export const wikiPath = (slug = "") => `/wiki${slug ? `/${slug}` : ""}`;
