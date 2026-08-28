import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";
import "./theme.css";

export const metadata: Metadata = {
  title: "Visual Agent Learning Library",
  description: "Ten visual courses, complete Acme and HarborCare case studies, and step-by-step guides to MCP, RAG and agent systems.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased"><Link href="/how-to-use" className="site-help-link" aria-label="How to use this website"><span className="help-long-label">How to use this website</span><span className="help-short-label">How to use</span></Link>{children}</body>
    </html>
  );
}
