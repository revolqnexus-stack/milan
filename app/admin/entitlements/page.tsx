import Link from "next/link";
import { redirect } from "next/navigation";
import { getAdminAuth } from "@/lib/auth/admin-session";
import { PageEyebrow } from "@/components/ui/PageEyebrow";
import { VaultButton } from "@/components/ui/VaultButton";
import { GlassPanel } from "@/components/ui/GlassPanel";

export default async function EntitlementsHubPage() {
  const auth = await getAdminAuth();
  if (!auth) redirect("/admin/login");
  return (
    <div>
      <PageEyebrow>Entitlements</PageEyebrow>
      <h1 className="admin-h1">Grant access.</h1>
      <GlassPanel variant="card" className="admin-form">
        <p className="body-copy muted">
          Open a student → grant or revoke packs from their detail page.
        </p>
        <div style={{ marginTop: 16 }}>
          <Link href="/admin/students" className="inline-link-btn">
            <VaultButton type="button">Go to students</VaultButton>
          </Link>
        </div>
      </GlassPanel>
    </div>
  );
}
