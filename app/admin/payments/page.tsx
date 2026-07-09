"use client";

import { FormEvent, useEffect, useState } from "react";
import { GlassPanel } from "@/components/ui/GlassPanel";
import { VaultButton } from "@/components/ui/VaultButton";
import { PageEyebrow } from "@/components/ui/PageEyebrow";

export default function PaymentsPage() {
  const [payments, setPayments] = useState<any[]>([]);
  const [students, setStudents] = useState<any[]>([]);
  const [msg, setMsg] = useState("");

  async function load() {
    const p = await fetch("/api/admin/payments").then((r) => r.json());
    const s = await fetch("/api/admin/students").then((r) => r.json());
    if (p.ok) setPayments(p.payments);
    if (s.ok) setStudents(s.students);
  }

  useEffect(() => {
    load();
  }, []);

  async function create(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setMsg("");
    const form = new FormData(e.currentTarget);
    const res = await fetch("/api/admin/payments", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        userId: Number(form.get("userId")),
        amountRupees: Number(form.get("amountRupees")),
        paymentMethod: form.get("paymentMethod"),
        paymentReference: form.get("paymentReference") || undefined,
        notes: form.get("notes") || undefined,
        status: "CONFIRMED",
      }),
    });
    const data = await res.json();
    if (!data.ok) setMsg(data.error || "Failed");
    else {
      setMsg("Payment recorded. Grant entitlement on the student page.");
      e.currentTarget.reset();
      load();
    }
  }

  return (
    <div>
      <PageEyebrow>Payments</PageEyebrow>
      <h1 className="admin-h1">Manual confirmations.</h1>
      <p className="admin-lead">
        UPI / cash confirmation. Does not auto-grant content.
      </p>

      <GlassPanel variant="form" className="admin-form">
        <form onSubmit={create}>
          <div className="vault-field">
            <label>Student</label>
            <select name="userId" required>
              <option value="">Select…</option>
              {students.map((s) => (
                <option key={s.id} value={s.id}>
                  {s.studentId} · {s.name}
                </option>
              ))}
            </select>
          </div>
          <div className="vault-field">
            <label>Amount ₹</label>
            <input name="amountRupees" type="number" defaultValue={299} required />
          </div>
          <div className="vault-field">
            <label>Method</label>
            <select name="paymentMethod" defaultValue="UPI">
              <option value="UPI">UPI</option>
              <option value="BANK_TRANSFER">Bank transfer</option>
              <option value="CASH">Cash</option>
              <option value="RAZORPAY">Razorpay</option>
            </select>
          </div>
          <div className="vault-field">
            <label>Transaction reference</label>
            <input name="paymentReference" />
          </div>
          <div className="vault-field">
            <label>Notes</label>
            <input name="notes" />
          </div>
          <VaultButton type="submit">Confirm payment</VaultButton>
          {msg && <p className="ok-msg">{msg}</p>}
        </form>
      </GlassPanel>

      <div className="admin-list">
        {payments.map((p) => (
          <div key={p.id} className="admin-row">
            <div>
              <strong>
                {p.studentId} · ₹{Math.round(p.amountPaise / 100)}
              </strong>
              <div className="muted">
                {p.status} · {p.paymentMethod} · {p.paymentReference || "—"} ·{" "}
                {new Date(p.createdAt).toLocaleString()}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
