import { redirect, notFound } from "next/navigation";
import Link from "next/link";
import { getStudentAuth } from "@/lib/auth/student-session";
import { hasValidEntitlement } from "@/lib/auth/entitlements";
import { getContentBySlug } from "@/lib/admin/content";
import { fetchPrivateBlob } from "@/lib/blob/storage";
import { GlassPanel } from "@/components/ui/GlassPanel";
import { DisplayHeading } from "@/components/ui/DisplayHeading";
import { PageEyebrow } from "@/components/ui/PageEyebrow";
import { VaultButton } from "@/components/ui/VaultButton";

export const dynamic = "force-dynamic";

export default async function StudyPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const auth = await getStudentAuth();
  if (!auth) redirect(`/login?next=/study/${slug}`);

  const item = await getContentBySlug(slug);
  if (!item || !item.isActive || !item.htmlBlobPath) notFound();

  const entitled = await hasValidEntitlement(auth.userId, item.id);
  if (!entitled) {
    return (
      <main className="vault-page">
        <GlassPanel variant="portal" className="device-state">
          <PageEyebrow>Access</PageEyebrow>
          <DisplayHeading size="sm">This pack isn&apos;t in your library.</DisplayHeading>
          <p className="body-copy muted">
            You do not have access to <strong>{item.title}</strong>. Pay and ask
            admin to grant entitlement.
          </p>
          <div className="device-actions">
            <Link href="/library" style={{ textDecoration: "none" }}>
              <VaultButton type="button">Back to library</VaultButton>
            </Link>
          </div>
        </GlassPanel>
      </main>
    );
  }

  let html = "";
  try {
    html = await fetchPrivateBlob(item.htmlBlobPath);
  } catch (err) {
    console.error("blob fetch", err);
    return (
      <main className="vault-page">
        <GlassPanel variant="portal" className="device-state">
          <PageEyebrow>Content</PageEyebrow>
          <DisplayHeading size="sm">Content unavailable.</DisplayHeading>
          <p className="body-copy muted">Could not load study HTML. Contact admin.</p>
          <div className="device-actions">
            <Link href="/library" style={{ textDecoration: "none" }}>
              <VaultButton type="button">Back to library</VaultButton>
            </Link>
          </div>
        </GlassPanel>
      </main>
    );
  }

  // Compact floating back control — maximises viewport for the uploaded HTML app.
  return (
    <div className="study-shell">
      <Link
        href="/library"
        className="study-float-back"
        aria-label={`Back to library from ${item.title}`}
      >
        ← Library
      </Link>
      <iframe
        className="study-frame"
        title={item.title}
        sandbox="allow-scripts allow-same-origin allow-forms allow-modals allow-popups"
        srcDoc={html}
      />
    </div>
  );
}
