import { redirect, notFound } from "next/navigation";
import Link from "next/link";
import { getStudentAuth } from "@/lib/auth/student-session";
import { hasValidEntitlement } from "@/lib/auth/entitlements";
import { getContentBySlug } from "@/lib/admin/content";
import { fetchPrivateBlob } from "@/lib/blob/storage";

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
      <div className="sb-page" style={{ display: "flex", alignItems: "center", justifyContent: "center", minHeight: "100vh" }}>
        <div className="sb-device-state">
          <p style={{ fontSize: 11, fontWeight: 700, letterSpacing: "0.1em", textTransform: "uppercase", color: "var(--sb-accent-indigo)", margin: "0 0 8px" }}>Access</p>
          <h2 className="sb-device-heading">This pack isn&apos;t in your library.</h2>
          <p className="sb-device-body">
            You don&apos;t have access to <strong>{item.title}</strong>. Pay and ask
            admin to grant entitlement.
          </p>
          <div className="sb-device-actions">
            <Link href="/library" className="sb-btn sb-btn-primary sb-btn-full" style={{ textDecoration: "none" }}>
              Back to library
            </Link>
          </div>
        </div>
      </div>
    );
  }

  let html = "";
  try {
    html = await fetchPrivateBlob(item.htmlBlobPath);
  } catch (err) {
    console.error("blob fetch", err);
    return (
      <div className="sb-page" style={{ display: "flex", alignItems: "center", justifyContent: "center", minHeight: "100vh" }}>
        <div className="sb-device-state">
          <p style={{ fontSize: 11, fontWeight: 700, letterSpacing: "0.1em", textTransform: "uppercase", color: "var(--sb-accent-indigo)", margin: "0 0 8px" }}>Content</p>
          <h2 className="sb-device-heading">Content unavailable.</h2>
          <p className="sb-device-body">Could not load study HTML. Contact admin.</p>
          <div className="sb-device-actions">
            <Link href="/library" className="sb-btn sb-btn-primary sb-btn-full" style={{ textDecoration: "none" }}>
              Back to library
            </Link>
          </div>
        </div>
      </div>
    );
  }

  // Compact floating back control — maximises viewport for the uploaded HTML app.
  return (
    <div className="sb-page sb-study-shell">
      <Link
        href="/library"
        className="sb-study-back"
        aria-label={`Back to library from ${item.title}`}
      >
        ← Library
      </Link>
      <iframe
        className="sb-study-frame"
        title={item.title}
        sandbox="allow-scripts allow-same-origin allow-forms allow-modals allow-popups"
        srcDoc={html}
      />
    </div>
  );
}
