import type { Metadata } from "next";
import Link from "next/link";
import "./wiki.css";

export const metadata: Metadata = {
  title: { default: "Visual Engineering Wiki", template: "%s | Visual Engineering Wiki" },
  description: "Plain-English explanations, visual flows, and practical examples from FilePilot, Acme, and Hospital case studies.",
};

export default function WikiLayout({ children }: { children: React.ReactNode }) {
  return <div className="wiki-shell"><a className="wiki-skip" href="#wiki-content">Skip to wiki content</a><header className="wiki-header"><Link prefetch={false} href="/wiki">Visual Engineering Wiki</Link><a href="https://course.ketanshukla.dev">Courses &amp; mission labs ↗</a></header>{children}<footer className="wiki-footer">A companion to the Visual Library. Examples are fictional teaching scenarios, not live integrations or compliance advice. No sign-in or progress tracking.</footer></div>;
}
