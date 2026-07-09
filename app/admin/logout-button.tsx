"use client";

import { useRouter } from "next/navigation";
import { VaultButton } from "@/components/ui/VaultButton";

export function AdminLogoutButton() {
  const router = useRouter();
  return (
    <VaultButton
      type="button"
      variant="ghost"
      onClick={async () => {
        await fetch("/api/admin/auth/logout", { method: "POST" });
        router.replace("/admin/login");
      }}
    >
      Logout
    </VaultButton>
  );
}
