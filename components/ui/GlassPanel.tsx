import type { HTMLAttributes, ReactNode } from "react";

type Variant = "card" | "portal" | "form" | "nav" | "highlight" | "modal" | "muted";

const map: Record<Variant, string> = {
  card: "glass-panel glass-card",
  portal: "glass-panel glass-portal",
  form: "glass-panel glass-form",
  nav: "glass-panel glass-nav",
  highlight: "glass-panel glass-highlight",
  modal: "glass-panel glass-modal",
  muted: "glass-panel glass-muted",
};

export function GlassPanel({
  variant = "card",
  className = "",
  children,
  featured,
  ...rest
}: {
  variant?: Variant;
  className?: string;
  children: ReactNode;
  featured?: boolean;
} & HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      className={`${map[variant]} ${featured ? "is-featured" : ""} ${className}`.trim()}
      {...rest}
    >
      {children}
    </div>
  );
}
