"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

export function LogoutButton() {
  const router = useRouter();
  const [busy, setBusy] = useState(false);

  async function logout() {
    setBusy(true);
    await fetch("/api/auth/logout", { method: "POST" });
    router.replace("/login");
  }

  return (
    <button
      type="button"
      className="sb-btn sb-btn-ghost"
      onClick={logout}
      disabled={busy}
    >
      {busy ? "…" : "Logout"}
    </button>
  );
}
