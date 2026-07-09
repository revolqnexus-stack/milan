import type { ReactNode } from "react";

export function DisplayHeading({
  children,
  size = "lg",
  as: Tag = "h1",
  className = "",
}: {
  children: ReactNode;
  size?: "lg" | "md" | "sm";
  as?: "h1" | "h2" | "h3";
  className?: string;
}) {
  const sizeClass = size === "lg" ? "" : size;
  return (
    <Tag className={`display-heading ${sizeClass} ${className}`.trim()}>
      {children}
    </Tag>
  );
}
