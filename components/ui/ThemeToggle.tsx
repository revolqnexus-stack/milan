"use client";

import { useEffect, useState } from "react";
import styles from "./ThemeToggle.module.css";

type Theme = "dark" | "light";

function applyTheme(theme: Theme) {
  document.documentElement.setAttribute("data-theme", theme);
  localStorage.setItem("revolqnexus-theme", theme);
}

export function ThemeToggle() {
  const [theme, setTheme] = useState<Theme>("dark");

  useEffect(() => {
    const stored = localStorage.getItem("revolqnexus-theme") as Theme | null;
    const current =
      (document.documentElement.getAttribute("data-theme") as Theme | null) ||
      stored ||
      "dark";
    setTheme(current === "light" ? "light" : "dark");
  }, []);

  function toggle() {
    const next: Theme = theme === "dark" ? "light" : "dark";
    setTheme(next);
    applyTheme(next);
  }

  const pressed = theme === "dark";

  return (
    <button
      type="button"
      className={styles.toggle}
      onClick={toggle}
      aria-pressed={pressed}
      aria-label={theme === "dark" ? "Dark mode active" : "Light mode active"}
    >
      {theme === "dark" ? "Dark" : "Light"}
    </button>
  );
}
