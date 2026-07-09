"use client";

import Link from "next/link";
import { FormEvent, useEffect, useState } from "react";
import { GlassPanel } from "@/components/ui/GlassPanel";
import { VaultButton } from "@/components/ui/VaultButton";
import { PageEyebrow } from "@/components/ui/PageEyebrow";
import { StatusChip } from "@/components/ui/StatusChip";

type Student = {
  id: number;
  studentId: string;
  name: string;
  status: string;
  device: { deviceLabel: string | null } | null;
  entitlements: { title: string }[];
};

export default function AdminStudentsPage() {
  const [students, setStudents] = useState<Student[]>([]);
  const [name, setName] = useState("");
  const [studentId, setStudentId] = useState("");
  const [created, setCreated] = useState<{
    studentId: string;
    temporaryPassword: string;
  } | null>(null);
  const [error, setError] = useState("");

  async function load() {
    const res = await fetch("/api/admin/students");
    const data = await res.json();
    if (data.ok) setStudents(data.students);
  }

  useEffect(() => {
    load();
  }, []);

  async function create(e: FormEvent) {
    e.preventDefault();
    setError("");
    setCreated(null);
    const res = await fetch("/api/admin/students", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name,
        studentId: studentId || undefined,
      }),
    });
    const data = await res.json();
    if (!data.ok) {
      setError(data.error || "Failed");
      return;
    }
    setCreated({
      studentId: data.user.studentId,
      temporaryPassword: data.temporaryPassword,
    });
    setName("");
    setStudentId("");
    load();
  }

  return (
    <div>
      <PageEyebrow>Students</PageEyebrow>
      <h1 className="admin-h1">Student access.</h1>
      <p className="admin-lead">Create credentials, bind devices, grant packs.</p>

      <GlassPanel variant="form" className="admin-form">
        <h2>Create student</h2>
        <form onSubmit={create}>
          <div className="vault-field">
            <label>Name</label>
            <input value={name} onChange={(e) => setName(e.target.value)} required />
          </div>
          <div className="vault-field">
            <label>Student ID (optional — auto GNM#####)</label>
            <input
              value={studentId}
              onChange={(e) => setStudentId(e.target.value.toUpperCase())}
              placeholder="GNM10483"
            />
          </div>
          <VaultButton type="submit">Create + generate password</VaultButton>
        </form>
        {error && <p className="vault-error">{error}</p>}
        {created && (
          <div className="cred-box">
            <strong>STUDENT CREATED — copy now</strong>
            <p>
              ID: <code>{created.studentId}</code>
            </p>
            <p>
              TEMPORARY PASSWORD: <code>{created.temporaryPassword}</code>
            </p>
            <div style={{ marginTop: 10 }}>
              <VaultButton
                type="button"
                variant="secondary"
                onClick={() =>
                  navigator.clipboard.writeText(
                    `Student ID: ${created.studentId}\nPassword: ${created.temporaryPassword}`
                  )
                }
              >
                Copy credentials
              </VaultButton>
            </div>
          </div>
        )}
      </GlassPanel>

      <div className="admin-list">
        {students.map((s) => (
          <Link key={s.id} href={`/admin/students/${s.id}`} className="admin-row">
            <div>
              <strong>
                {s.studentId} · {s.name}
              </strong>
              <div className="muted" style={{ marginTop: 4 }}>
                {s.device ? `Device: ${s.device.deviceLabel || "bound"}` : "No device"} ·{" "}
                {s.entitlements.length} access
              </div>
            </div>
            <StatusChip
              status={s.status === "ACTIVE" ? "active" : "locked"}
            >
              {s.status}
            </StatusChip>
          </Link>
        ))}
      </div>
    </div>
  );
}
