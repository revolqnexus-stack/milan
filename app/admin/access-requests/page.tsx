"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { GlassPanel } from "@/components/ui/GlassPanel";
import { VaultButton } from "@/components/ui/VaultButton";
import { PageEyebrow } from "@/components/ui/PageEyebrow";
import { StatusChip } from "@/components/ui/StatusChip";

type AccessRequest = {
  id: number;
  name: string;
  phone: string;
  college: string | null;
  status: "PENDING" | "CONTACTED" | "PAID" | "APPROVED" | "REJECTED";
  adminNotes: string | null;
  linkedUserId: number | null;
  createdAt: string;
  contentId: number;
  contentTitle: string;
  contentPaperCode: string | null;
  priceInrPaise: number;
};

const STATUS_LABELS: Record<AccessRequest["status"], string> = {
  PENDING: "pending",
  CONTACTED: "contacted",
  PAID: "paid",
  APPROVED: "approved",
  REJECTED: "rejected",
};

const STATUS_CHIP: Record<AccessRequest["status"], "active" | "locked" | "pending" | "info" | "muted"> = {
  PENDING: "pending",
  CONTACTED: "info",
  PAID: "info",
  APPROVED: "active",
  REJECTED: "muted",
};

export default function AccessRequestsPage() {
  const [requests, setRequests] = useState<AccessRequest[]>([]);
  const [selected, setSelected] = useState<AccessRequest | null>(null);
  const [msg, setMsg] = useState("");
  const [notes, setNotes] = useState("");
  const [linkedUserId, setLinkedUserId] = useState("");

  async function load() {
    const res = await fetch("/api/admin/access-requests");
    const data = await res.json();
    if (data.ok) setRequests(data.requests);
  }

  useEffect(() => {
    load();
  }, []);

  function openDetail(r: AccessRequest) {
    setSelected(r);
    setMsg("");
    setNotes(r.adminNotes || "");
    setLinkedUserId(r.linkedUserId ? String(r.linkedUserId) : "");
  }

  async function updateStatus(status: AccessRequest["status"]) {
    if (!selected) return;
    setMsg("");
    const res = await fetch("/api/admin/access-requests", {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        id: selected.id,
        status,
        adminNotes: notes || null,
        linkedUserId: linkedUserId ? Number(linkedUserId) : null,
      }),
    });
    const data = await res.json();
    if (!data.ok) {
      setMsg(data.error || "Failed");
      return;
    }
    setMsg("Updated.");
    load();
    // refresh selected
    setSelected((prev) =>
      prev ? { ...prev, status, adminNotes: notes || null } : null
    );
  }

  const pending = requests.filter((r) => r.status === "PENDING");
  const others = requests.filter((r) => r.status !== "PENDING");

  return (
    <div>
      <PageEyebrow>Access Requests</PageEyebrow>
      <h1 className="admin-h1">Access requests.</h1>
      <p className="admin-lead">
        Students who asked for a pack. {pending.length > 0 && (
          <strong style={{ color: "var(--theme-warning)" }}>
            {pending.length} pending
          </strong>
        )}
      </p>

      {selected && (
        <GlassPanel variant="form" className="admin-form" style={{ marginBottom: 28 }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", gap: 12 }}>
            <h2 style={{ margin: 0 }}>{selected.name}</h2>
            <button
              onClick={() => setSelected(null)}
              style={{ background: "none", border: "none", color: "var(--theme-text-muted)", cursor: "pointer", fontSize: 20 }}
              aria-label="Close"
            >
              ×
            </button>
          </div>

          <div className="muted" style={{ marginTop: 6, marginBottom: 16 }}>
            <div>📱 <a href={`tel:${selected.phone}`} style={{ color: "var(--theme-label)" }}>{selected.phone}</a></div>
            {selected.college && <div>🏫 {selected.college}</div>}
            <div style={{ marginTop: 6 }}>
              Pack: <strong>{selected.contentTitle}</strong>
              {selected.contentPaperCode && ` · Q.P. ${selected.contentPaperCode}`}
              {" "}· ₹{Math.round(selected.priceInrPaise / 100)}
            </div>
            <div>Requested: {new Date(selected.createdAt).toLocaleString()}</div>
          </div>

          <div className="vault-field">
            <label>Admin notes</label>
            <input
              value={notes}
              onChange={(e) => setNotes(e.target.value)}
              placeholder="payment ref, UPI ID, etc."
            />
          </div>

          <div className="vault-field">
            <label>Link to student user ID (once created)</label>
            <input
              type="number"
              value={linkedUserId}
              onChange={(e) => setLinkedUserId(e.target.value)}
              placeholder="student DB id"
            />
          </div>

          <div className="admin-actions" style={{ flexWrap: "wrap" }}>
            <VaultButton type="button" variant="secondary" onClick={() => updateStatus("CONTACTED")}>
              Mark Contacted
            </VaultButton>
            <VaultButton type="button" variant="secondary" onClick={() => updateStatus("PAID")}>
              Mark Paid
            </VaultButton>
            <VaultButton type="button" onClick={() => updateStatus("APPROVED")}>
              Approve
            </VaultButton>
            <VaultButton type="button" variant="ghost" onClick={() => updateStatus("REJECTED")}>
              Reject
            </VaultButton>
          </div>

          {selected.linkedUserId && (
            <div style={{ marginTop: 10 }}>
              <Link href={`/admin/students/${selected.linkedUserId}`} className="muted" style={{ color: "var(--theme-label)" }}>
                → go to student profile to grant entitlement
              </Link>
            </div>
          )}

          {msg && <p className="ok-msg">{msg}</p>}
        </GlassPanel>
      )}

      {pending.length > 0 && (
        <>
          <p className="muted" style={{ marginBottom: 8, fontWeight: 700, textTransform: "uppercase", letterSpacing: "0.08em", fontSize: 11 }}>
            New requests
          </p>
          <div className="admin-list" style={{ marginBottom: 24 }}>
            {pending.map((r) => (
              <button
                key={r.id}
                className="admin-row"
                style={{ width: "100%", textAlign: "left", cursor: "pointer", border: selected?.id === r.id ? "1px solid var(--vault-blue)" : undefined }}
                onClick={() => openDetail(r)}
              >
                <div>
                  <strong>{r.name}</strong>
                  <div className="muted">
                    {r.phone} · {r.contentTitle}
                    {r.contentPaperCode && ` · Q.P. ${r.contentPaperCode}`}
                    {" · ₹"}{Math.round(r.priceInrPaise / 100)}
                  </div>
                  <div className="muted">{new Date(r.createdAt).toLocaleString()}{r.college && ` · ${r.college}`}</div>
                </div>
                <StatusChip status="pending">PENDING</StatusChip>
              </button>
            ))}
          </div>
        </>
      )}

      {others.length > 0 && (
        <>
          <p className="muted" style={{ marginBottom: 8, fontWeight: 700, textTransform: "uppercase", letterSpacing: "0.08em", fontSize: 11 }}>
            Previous
          </p>
          <div className="admin-list">
            {others.map((r) => (
              <button
                key={r.id}
                className="admin-row"
                style={{ width: "100%", textAlign: "left", cursor: "pointer", opacity: r.status === "REJECTED" ? 0.6 : 1, border: selected?.id === r.id ? "1px solid var(--vault-blue)" : undefined }}
                onClick={() => openDetail(r)}
              >
                <div>
                  <strong>{r.name}</strong>
                  <div className="muted">
                    {r.phone} · {r.contentTitle}
                    {r.contentPaperCode && ` · Q.P. ${r.contentPaperCode}`}
                  </div>
                  {r.adminNotes && <div className="muted">📝 {r.adminNotes}</div>}
                </div>
                <StatusChip status={STATUS_CHIP[r.status]}>
                  {STATUS_LABELS[r.status]}
                </StatusChip>
              </button>
            ))}
          </div>
        </>
      )}

      {requests.length === 0 && (
        <p className="muted">no requests yet. once a student hits the landing page and fills the form, they&apos;ll show up here.</p>
      )}
    </div>
  );
}
