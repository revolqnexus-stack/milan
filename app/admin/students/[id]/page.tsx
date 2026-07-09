"use client";

import { useParams } from "next/navigation";
import { useEffect, useState } from "react";
import { GlassPanel } from "@/components/ui/GlassPanel";
import { VaultButton } from "@/components/ui/VaultButton";
import { PageEyebrow } from "@/components/ui/PageEyebrow";
import { StatusChip } from "@/components/ui/StatusChip";

export default function StudentDetailPage() {
  const params = useParams<{ id: string }>();
  const [data, setData] = useState<any>(null);
  const [tempPass, setTempPass] = useState("");
  const [msg, setMsg] = useState("");
  const [content, setContent] = useState<any[]>([]);

  async function load() {
    const res = await fetch(`/api/admin/students/${params.id}`);
    const json = await res.json();
    if (json.ok) setData(json);
    const c = await fetch("/api/admin/content");
    const cj = await c.json();
    if (cj.ok) setContent(cj.content);
  }

  useEffect(() => {
    load();
  }, [params.id]);

  async function action(action: string, reason?: string) {
    setMsg("");
    setTempPass("");
    const res = await fetch(`/api/admin/students/${params.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action, reason }),
    });
    const json = await res.json();
    if (!json.ok) {
      setMsg(json.error || "Failed");
      return;
    }
    if (json.temporaryPassword) setTempPass(json.temporaryPassword);
    setMsg("Done");
    load();
  }

  async function grant(contentId: number) {
    await fetch("/api/admin/entitlements", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ userId: Number(params.id), contentId }),
    });
    load();
  }

  async function revoke(entitlementId: number) {
    await fetch("/api/admin/entitlements", {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ entitlementId }),
    });
    load();
  }

  if (!data) return <p className="muted">Loading…</p>;
  const u = data.user;
  const activeDevice = (data.devices || []).find((d: any) => !d.revokedAt);

  return (
    <div>
      <PageEyebrow>Student</PageEyebrow>
      <h1 className="admin-h1">
        {u.studentId} · {u.name}
      </h1>
      <p className="admin-lead">
        Status: <StatusChip status={u.status === "ACTIVE" ? "active" : "locked"}>{u.status}</StatusChip>
      </p>

      <div className="admin-actions">
        <VaultButton type="button" variant="secondary" onClick={() => action("activate")}>
          Activate
        </VaultButton>
        <VaultButton type="button" variant="secondary" onClick={() => action("disable")}>
          Disable
        </VaultButton>
        <VaultButton type="button" variant="secondary" onClick={() => action("reset_password")}>
          Reset password
        </VaultButton>
        <VaultButton
          type="button"
          onClick={() => {
            const reason = prompt("Reset reason?") || "Admin reset";
            action("reset_device", reason);
          }}
        >
          Reset device
        </VaultButton>
      </div>

      {tempPass && (
        <div className="cred-box">
          New temporary password: <code>{tempPass}</code>
        </div>
      )}
      {msg && <p className="muted">{msg}</p>}

      <h2 className="admin-h2">Device</h2>
      {activeDevice ? (
        <GlassPanel variant="card" className="admin-card" style={{ display: "block" }}>
          <p style={{ color: "var(--theme-heading)", fontWeight: 600 }}>
            {activeDevice.deviceLabel || "Bound device"}
          </p>
          <p className="muted">
            Activated {new Date(activeDevice.activatedAt).toLocaleString()} · Last seen{" "}
            {new Date(activeDevice.lastSeenAt).toLocaleString()}
          </p>
        </GlassPanel>
      ) : (
        <p className="muted">No active device — next login will bind a new one.</p>
      )}

      <h2 className="admin-h2">Entitlements</h2>
      <div className="admin-list">
        {content.map((c) => {
          const ent = (data.entitlements || []).find(
            (e: any) => e.contentId === c.id && !e.revokedAt
          );
          return (
            <div key={c.id} className="admin-row">
              <div>
                <strong>{c.title}</strong>
                <div className="muted">{ent ? "ACCESS GRANTED" : "No access"}</div>
              </div>
              {ent ? (
                <VaultButton type="button" variant="ghost" onClick={() => revoke(ent.id)}>
                  Remove
                </VaultButton>
              ) : (
                <VaultButton type="button" variant="secondary" onClick={() => grant(c.id)}>
                  Grant
                </VaultButton>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
