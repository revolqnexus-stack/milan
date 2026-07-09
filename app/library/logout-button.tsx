"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import { VaultButton } from "@/components/ui/VaultButton";

export function LogoutButton() {
  const router = useRouter();
  const [busy, setBusy] = useState(false);

  async function logout() {
    setBusy(true);
    await fetch("/api/auth/logout", { method: "POST" });
    router.replace("/login");
  }

  return (
    <VaultButton type="button" variant="ghost" onClick={logout} disabled={busy}>
      {busy ? "…" : "Logout"}
    </VaultButton>
  );
}
