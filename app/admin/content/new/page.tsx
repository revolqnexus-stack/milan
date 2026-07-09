"use client";

import { FormEvent, useState } from "react";
import { useRouter } from "next/navigation";
import { GlassPanel } from "@/components/ui/GlassPanel";
import { VaultButton } from "@/components/ui/VaultButton";
import { PageEyebrow } from "@/components/ui/PageEyebrow";

export default function NewContentPage() {
  const router = useRouter();
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setBusy(true);
    setError("");
    const form = new FormData(e.currentTarget);
    form.set("isActive", form.get("publish") === "on" ? "true" : "false");
    try {
      const res = await fetch("/api/admin/content", { method: "POST", body: form });
      const data = await res.json();
      if (!data.ok) {
        setError(data.error || "Upload failed");
        setBusy(false);
        return;
      }
      router.replace(`/admin/content/${data.content.id}`);
    } catch {
      setError("Network / Blob error — is BLOB_READ_WRITE_TOKEN set?");
      setBusy(false);
    }
  }

  return (
    <div>
      <PageEyebrow>Study content</PageEyebrow>
      <h1 className="admin-h1">Add study material.</h1>
      <p className="admin-lead">Upload a standalone HTML study app to Private Blob.</p>

      <GlassPanel variant="form" className="admin-form">
        <form onSubmit={onSubmit}>
          <div className="vault-field">
            <label>Title</label>
            <input name="title" required placeholder="Community Health Nursing I" />
          </div>
          <div className="vault-field">
            <label>Course</label>
            <input name="course" defaultValue="GNM" required />
          </div>
          <div className="vault-field">
            <label>Study year</label>
            <input name="studyYear" type="number" defaultValue={1} min={1} max={5} required />
          </div>
          <div className="vault-field">
            <label>Subject</label>
            <input name="subject" required />
          </div>
          <div className="vault-field">
            <label>Paper code</label>
            <input name="paperCode" placeholder="9114" />
          </div>
          <div className="vault-field">
            <label>Description</label>
            <textarea name="description" rows={3} />
          </div>
          <div className="vault-field">
            <label>Price (₹)</label>
            <input name="priceRupees" type="number" defaultValue={299} required />
          </div>
          <div className="vault-field">
            <label>Sort order</label>
            <input name="sortOrder" type="number" defaultValue={0} />
          </div>
          <div className="vault-field">
            <label>HTML file</label>
            <input name="html" type="file" accept=".html,text/html" required />
          </div>
          <div className="vault-field">
            <label>Thumbnail (optional)</label>
            <input name="thumbnail" type="file" accept="image/*" />
          </div>
          <label className="check-row">
            <input type="checkbox" name="publish" defaultChecked /> Publish now
          </label>
          <VaultButton type="submit" disabled={busy}>
            {busy ? "Uploading to Private Blob…" : "Publish study material"}
          </VaultButton>
          {error && <p className="vault-error">{error}</p>}
        </form>
      </GlassPanel>
    </div>
  );
}
