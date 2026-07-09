import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "CHN Study Pack · GNM Karnataka",
  description: "Community Health Nursing–I exam pack · Q.P. 9114 · ₹200 · 1 device",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
