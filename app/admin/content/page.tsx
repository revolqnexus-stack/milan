import Link from "next/link";
import { redirect } from "next/navigation";
import { getAdminAuth } from "@/lib/auth/admin-session";
import { listAllContent } from "@/lib/admin/content";
import { PageEyebrow } from "@/components/ui/PageEyebrow";
import { VaultButton } from "@/components/ui/VaultButton";
import { StatusChip } from "@/components/ui/StatusChip";

export const dynamic = "force-dynamic";

export default async function AdminContentPage() {
  const auth = await getAdminAuth();
  if (!auth) redirect("/admin/login");
  const items = await listAllContent();

  return (
    <div>
      <div className="admin-top-row">
        <div>
          <PageEyebrow>Study content</PageEyebrow>
          <h1 className="admin-h1">Study packs.</h1>
        </div>
        <Link href="/admin/content/new" className="inline-link-btn">
          <VaultButton type="button">+ Add study material</VaultButton>
        </Link>
      </div>
      <div className="admin-list">
        {items.map((c) => (
          <Link key={c.id} href={`/admin/content/${c.id}`} className="admin-row">
            <div>
              <strong>{c.title}</strong>
              <div className="muted">
                {c.course} · Year {c.studyYear} · {c.slug} · ₹
                {Math.round(c.priceInrPaise / 100)}
              </div>
            </div>
            <StatusChip status={c.isActive ? "granted" : "muted"}>
              {c.isActive ? "Published" : "Draft"}
            </StatusChip>
          </Link>
        ))}
        {items.length === 0 && (
          <p className="muted">No content yet. Upload your first HTML.</p>
        )}
      </div>
    </div>
  );
}
