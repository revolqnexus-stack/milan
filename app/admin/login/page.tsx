"use client";

import { FormEvent, useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import { GlassPanel } from "@/components/ui/GlassPanel";
import { VaultButton } from "@/components/ui/VaultButton";
import { ThemeToggle } from "@/components/ui/ThemeToggle";
import { PageEyebrow } from "@/components/ui/PageEyebrow";
import { DisplayHeading } from "@/components/ui/DisplayHeading";

export default function AdminLoginPage() {
  const router = useRouter();
  const [adminId, setAdminId] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    setBusy(true);
    setError("");
    try {
      const res = await fetch("/api/admin/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: adminId, password }),
      });
      const data = await res.json();
      if (!data.ok) {
        setError(data.error || "Login failed");
        setBusy(false);
        return;
      }
      router.replace("/admin");
    } catch {
      setError("Network error");
      setBusy(false);
    }
  }

  return (
    <main className="vault-page">
      <div className="landing-shell" style={{ maxWidth: 480 }}>
        <div className="glass-panel glass-nav lib-nav">
          <Link href="/" className="brand-mark">
            REVOLQ<span>NEXUS</span>
          </Link>
          <ThemeToggle />
        </div>

        <GlassPanel variant="form" className="login-panel motion-fade-up">
          <PageEyebrow>Admin</PageEyebrow>
          <DisplayHeading size="sm">Vault control.</DisplayHeading>
          <p className="body-copy muted" style={{ marginBottom: 18 }}>
            Separate admin access. Not Student ID login.
          </p>
          <form onSubmit={onSubmit}>
            <div className="vault-field">
              <label htmlFor="adminId">Admin ID</label>
              <input
                id="adminId"
                type="text"
                autoComplete="username"
                value={adminId}
                onChange={(e) => setAdminId(e.target.value)}
                placeholder="Admin ID"
                required
              />
            </div>
            <div className="vault-field">
              <label htmlFor="password">Password</label>
              <input
                id="password"
                type="password"
                autoComplete="current-password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
            <VaultButton type="submit" disabled={busy}>
              {busy ? "…" : "Enter admin"}
            </VaultButton>
          </form>
          {error && <p className="vault-error">{error}</p>}
        </GlassPanel>
      </div>
    </main>
  );
}
