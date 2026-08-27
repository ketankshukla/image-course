import type { Metadata } from "next";
import "./globals.css";

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
      <body className="antialiased">{children}</body>
    </html>
  );
}
