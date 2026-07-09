"use client";

import type { ButtonHTMLAttributes, ReactNode } from "react";
import styles from "./VaultButton.module.css";

type Variant = "primary" | "secondary" | "ghost" | "danger";

export function VaultButton({
  variant = "primary",
  children,
  className = "",
  orb = false,
  ...rest
}: {
  variant?: Variant;
  children: ReactNode;
  className?: string;
  orb?: boolean;
} & ButtonHTMLAttributes<HTMLButtonElement>) {
  return (
    <button
      className={`${styles.btn} ${styles[variant]} ${className}`.trim()}
      {...rest}
    >
      <span>{children}</span>
      {orb && variant === "primary" ? <span className={styles.orb} aria-hidden>→</span> : null}
    </button>
  );
}
