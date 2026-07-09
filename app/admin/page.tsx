"use client";

import { useCallback, useState, type CSSProperties, type FormEvent } from "react";

type Licence = {
  id: number;
  login_id: string;
  device_id: string | null;
  buyer_note: string | null;
  active: boolean;
  unlocked_at: string | null;
  created_at: string;
};

export default function AdminPage() {
  const [secret, setSecret] = useState("");
  const [licences, setLicences] = useState<Licence[]>([]);
  const [error, setError] = useState("");
  const [msg, setMsg] = useState("");
  const [loginId, setLoginId] = useState("");
  const [password, setPassword] = useState("");
  const [buyerNote, setBuyerNote] = useState("");
  const [busy, setBusy] = useState(false);

  const headers = useCallback(
    () => ({
      "Content-Type": "application/json",
      "x-admin-secret": secret,
    }),
    [secret]
  );

  async function load() {
    setError("");
    setMsg("");
    setBusy(true);
    try {
      const res = await fetch("/api/admin/licences", { headers: headers() });
      const data = await res.json();
      if (!res.ok || !data.ok) {
        setError(data.error || "Unauthorized — check ADMIN_SECRET");
        setLicences([]);
        return;
      }
      setLicences(data.licences || []);
      setMsg(`Loaded ${data.licences?.length || 0} licences`);
    } catch {
      setError("Network error");
    } finally {
      setBusy(false);
    }
  }

  async function createLicence(e: FormEvent) {
    e.preventDefault();
    setError("");
    setMsg("");
    setBusy(true);
    try {
      const res = await fetch("/api/admin/licences", {
        method: "POST",
        headers: headers(),
        body: JSON.stringify({ loginId, password, buyerNote }),
      });
      const data = await res.json();
      if (!res.ok || !data.ok) {
        setError(data.error || "Create failed");
        return;
      }
      setMsg(`Created ${data.loginId} — send ID + password to buyer (₹200)`);
      setLoginId("");
      setPassword("");
      setBuyerNote("");
      await load();
    } catch {
      setError("Network error");
    } finally {
      setBusy(false);
    }
  }

  async function patch(login: string, action: "reset_device" | "deactivate" | "activate") {
    setBusy(true);
    setError("");
    try {
      const res = await fetch("/api/admin/licences", {
        method: "PATCH",
        headers: headers(),
        body: JSON.stringify({ loginId: login, action }),
      });
      const data = await res.json();
      if (!res.ok || !data.ok) {
        setError(data.error || "Action failed");
        return;
      }
      setMsg(data.message || "Done");
      await load();
    } catch {
      setError("Network error");
    } finally {
      setBusy(false);
    }
  }

  return (
    <main style={{ maxWidth: 560, margin: "0 auto", padding: "28px 16px 60px" }}>
      <h1 style={{ fontSize: 24, fontWeight: 800, color: "var(--primary)", marginBottom: 6 }}>
        Seller admin
      </h1>
      <p style={{ fontSize: 13, color: "var(--subtext)", marginBottom: 20 }}>
        Create ₹200 licences. First login locks to that phone. Reset device if buyer changes phone.
      </p>

      <label style={labelStyle}>Admin secret</label>
      <input
        style={inputStyle}
        type="password"
        value={secret}
        onChange={(e) => setSecret(e.target.value)}
        placeholder="ADMIN_SECRET from Vercel / .env.local"
      />
      <button style={btnStyle} type="button" onClick={load} disabled={busy || !secret}>
        Load licences
      </button>

      <form onSubmit={createLicence} style={{ marginTop: 28 }}>
        <h2 style={{ fontSize: 16, marginBottom: 12 }}>New buyer licence</h2>
        <label style={labelStyle}>Login ID</label>
        <input
          style={inputStyle}
          value={loginId}
          onChange={(e) => setLoginId(e.target.value)}
          placeholder="e.g. stu014"
          required
        />
        <label style={labelStyle}>Password</label>
        <input
          style={inputStyle}
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="min 6 chars"
          required
        />
        <label style={labelStyle}>Buyer note (optional)</label>
        <input
          style={inputStyle}
          value={buyerNote}
          onChange={(e) => setBuyerNote(e.target.value)}
          placeholder="WhatsApp name / college"
        />
        <button style={btnStyle} type="submit" disabled={busy || !secret}>
          Create licence
        </button>
      </form>

      {error && <p style={{ ...bannerStyle, background: "#FDECEA", color: "var(--red)" }}>{error}</p>}
      {msg && <p style={{ ...bannerStyle, background: "#E8F5E9", color: "var(--green)" }}>{msg}</p>}

      <div style={{ marginTop: 28 }}>
        <h2 style={{ fontSize: 16, marginBottom: 12 }}>Licences</h2>
        {licences.length === 0 && (
          <p style={{ fontSize: 13, color: "var(--subtext)" }}>None loaded yet.</p>
        )}
        {licences.map((l) => (
          <div
            key={l.id}
            style={{
              background: "var(--card)",
              border: "1px solid var(--border)",
              borderRadius: 14,
              padding: 14,
              marginBottom: 10,
            }}
          >
            <div style={{ fontWeight: 700, marginBottom: 4 }}>{l.login_id}</div>
            <div style={{ fontSize: 12, color: "var(--subtext)", lineHeight: 1.45 }}>
              {l.active ? "Active" : "Inactive"} · Device:{" "}
              {l.device_id ? <code>{l.device_id}</code> : "not bound yet"}
              {l.buyer_note ? ` · ${l.buyer_note}` : ""}
            </div>
            <div style={{ display: "flex", gap: 8, marginTop: 10, flexWrap: "wrap" }}>
              <button
                type="button"
                style={smallBtn}
                disabled={busy}
                onClick={() => patch(l.login_id, "reset_device")}
              >
                Reset device
              </button>
              {l.active ? (
                <button
                  type="button"
                  style={smallBtn}
                  disabled={busy}
                  onClick={() => patch(l.login_id, "deactivate")}
                >
                  Deactivate
                </button>
              ) : (
                <button
                  type="button"
                  style={smallBtn}
                  disabled={busy}
                  onClick={() => patch(l.login_id, "activate")}
                >
                  Activate
                </button>
              )}
            </div>
          </div>
        ))}
      </div>
    </main>
  );
}

const labelStyle: CSSProperties = {
  display: "block",
  fontSize: 12,
  fontWeight: 600,
  color: "var(--subtext)",
  marginBottom: 6,
};

const inputStyle: CSSProperties = {
  width: "100%",
  padding: "12px 14px",
  marginBottom: 12,
  borderRadius: 12,
  border: "1.5px solid var(--border)",
  fontSize: 16,
  background: "#fff",
};

const btnStyle: CSSProperties = {
  width: "100%",
  padding: 14,
  border: "none",
  borderRadius: 12,
  background: "var(--primary)",
  color: "#fff",
  fontWeight: 700,
  fontSize: 15,
  cursor: "pointer",
};

const smallBtn: CSSProperties = {
  padding: "8px 12px",
  borderRadius: 10,
  border: "1px solid var(--border)",
  background: "#fff",
  fontSize: 12,
  fontWeight: 600,
  cursor: "pointer",
};

const bannerStyle: CSSProperties = {
  marginTop: 14,
  padding: "10px 12px",
  borderRadius: 10,
  fontSize: 13,
};
