import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Visual Course Volume 1 — MCP, ACP, A2A and RAG",
  description: "A visual course on modern agent architecture, MCP, ACP, A2A, and RAG.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className="antialiased" suppressHydrationWarning>{children}</body>
    </html>
  );
}
