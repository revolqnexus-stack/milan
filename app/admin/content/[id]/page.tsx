"use client";

import { FormEvent, useEffect, useState } from "react";
import { useParams } from "next/navigation";
import { GlassPanel } from "@/components/ui/GlassPanel";
import { VaultButton } from "@/components/ui/VaultButton";
import { PageEyebrow } from "@/components/ui/PageEyebrow";

export default function EditContentPage() {
  const params = useParams<{ id: string }>();
  const [item, setItem] = useState<any>(null);
  const [msg, setMsg] = useState("");
  const [error, setError] = useState("");

  async function load() {
    const res = await fetch(`/api/admin/content/${params.id}`);
    const data = await res.json();
    if (data.ok) setItem(data.content);
  }

  useEffect(() => {
    load();
  }, [params.id]);

  async function saveMeta(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    if (!item) return;
    setMsg("");
    setError("");
    const form = new FormData(e.currentTarget);
    const res = await fetch(`/api/admin/content/${params.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        title: form.get("title"),
        course: form.get("course"),
        studyYear: Number(form.get("studyYear")),
        subject: form.get("subject"),
        paperCode: String(form.get("paperCode") || "") || null,
        description: String(form.get("description") || "") || null,
        priceInrPaise: Math.round(Number(form.get("priceRupees")) * 100),
        sortOrder: Number(form.get("sortOrder") || 0),
        isActive: form.get("isActive") === "on",
      }),
    });
    const data = await res.json();
    if (!data.ok) setError(data.error || "Failed");
    else {
      setMsg("Saved");
      setItem(data.content);
    }
  }

  async function replaceHtml(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setMsg("");
    setError("");
    const form = new FormData(e.currentTarget);
    const res = await fetch(`/api/admin/content/${params.id}`, {
      method: "PATCH",
      body: form,
    });
    const data = await res.json();
    if (!data.ok) setError(data.error || "Replace failed");
    else {
      setMsg("HTML replaced — entitlements unchanged");
      setItem(data.content);
    }
  }

  if (!item) return <p className="muted">Loading…</p>;

  return (
    <div>
      <PageEyebrow>Edit content</PageEyebrow>
      <h1 className="admin-h1">{item.title}</h1>
      <p className="muted">
        slug: {item.slug} · blob: {item.htmlBlobPath || "—"}
      </p>

      <GlassPanel variant="form" className="admin-form">
        <h2>Metadata</h2>
        <form onSubmit={saveMeta}>
          <div className="vault-field">
            <label>Title</label>
            <input name="title" defaultValue={item.title} required />
          </div>
          <div className="vault-field">
            <label>Course</label>
            <input name="course" defaultValue={item.course} required />
          </div>
          <div className="vault-field">
            <label>Year</label>
            <input name="studyYear" type="number" defaultValue={item.studyYear} />
          </div>
          <div className="vault-field">
            <label>Subject</label>
            <input name="subject" defaultValue={item.subject} />
          </div>
          <div className="vault-field">
            <label>Paper code</label>
            <input name="paperCode" defaultValue={item.paperCode || ""} />
          </div>
          <div className="vault-field">
            <label>Description</label>
            <textarea name="description" defaultValue={item.description || ""} rows={3} />
          </div>
          <div className="vault-field">
            <label>Price ₹</label>
            <input
              name="priceRupees"
              type="number"
              defaultValue={Math.round(item.priceInrPaise / 100)}
            />
          </div>
          <div className="vault-field">
            <label>Sort order</label>
            <input name="sortOrder" type="number" defaultValue={item.sortOrder} />
          </div>
          <label className="check-row">
            <input type="checkbox" name="isActive" defaultChecked={item.isActive} /> Published
          </label>
          <VaultButton type="submit">Save metadata</VaultButton>
        </form>
      </GlassPanel>

      <GlassPanel variant="form" className="admin-form">
        <h2>Replace HTML</h2>
        <p className="muted">Existing entitlements stay valid.</p>
        <form onSubmit={replaceHtml}>
          <div className="vault-field">
            <label>HTML file</label>
            <input name="html" type="file" accept=".html,text/html" required />
          </div>
          <VaultButton type="submit" variant="secondary">
            Upload replacement
          </VaultButton>
        </form>
      </GlassPanel>

      {msg && <p className="ok-msg">{msg}</p>}
      {error && <p className="vault-error">{error}</p>}
    </div>
  );
}
