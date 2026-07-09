import Link from "next/link";
import { redirect } from "next/navigation";
import { sql, eq, isNull } from "drizzle-orm";
import { getAdminAuth } from "@/lib/auth/admin-session";
import { getDb, users, content, payments, devices, entitlements } from "@/lib/db";
import { GlassPanel } from "@/components/ui/GlassPanel";
import { PageEyebrow } from "@/components/ui/PageEyebrow";
import { VaultButton } from "@/components/ui/VaultButton";

export const dynamic = "force-dynamic";

export default async function AdminDashboard() {
  const auth = await getAdminAuth();
  if (!auth) redirect("/admin/login");

  const db = getDb();
  const [{ students }] = await db
    .select({ students: sql<number>`count(*)::int` })
    .from(users)
    .where(eq(users.status, "ACTIVE"));
  const [{ activeContent }] = await db
    .select({ activeContent: sql<number>`count(*)::int` })
    .from(content)
    .where(eq(content.isActive, true));
  const [{ activeEntitlements }] = await db
    .select({ activeEntitlements: sql<number>`count(*)::int` })
    .from(entitlements)
    .where(isNull(entitlements.revokedAt));
  const [{ boundDevices }] = await db
    .select({ boundDevices: sql<number>`count(*)::int` })
    .from(devices)
    .where(isNull(devices.revokedAt));
  const [{ confirmedPay }] = await db
    .select({ confirmedPay: sql<number>`coalesce(sum(${payments.amountPaise}),0)::int` })
    .from(payments)
    .where(eq(payments.status, "CONFIRMED"));

  return (
    <div>
      <PageEyebrow>Dashboard</PageEyebrow>
      <h1 className="admin-h1">Vault overview.</h1>
      <p className="admin-lead">REVOLQNEXUS · Neon-backed private study vault</p>

      <div className="admin-stats">
        <GlassPanel variant="card" className="admin-stat">
          <strong>{students}</strong>
          <span>Active students</span>
        </GlassPanel>
        <GlassPanel variant="card" className="admin-stat">
          <strong>{activeContent}</strong>
          <span>Published packs</span>
        </GlassPanel>
        <GlassPanel variant="card" className="admin-stat">
          <strong>{activeEntitlements}</strong>
          <span>Active entitlements</span>
        </GlassPanel>
        <GlassPanel variant="card" className="admin-stat">
          <strong>{boundDevices}</strong>
          <span>Bound devices</span>
        </GlassPanel>
        <GlassPanel variant="card" className="admin-stat">
          <strong>₹{Math.round((confirmedPay || 0) / 100)}</strong>
          <span>Confirmed revenue</span>
        </GlassPanel>
      </div>

      <div className="admin-actions">
        <Link href="/admin/students" className="inline-link-btn">
          <VaultButton type="button">Create student</VaultButton>
        </Link>
        <Link href="/admin/content/new" className="inline-link-btn">
          <VaultButton type="button" variant="secondary">
            Upload HTML
          </VaultButton>
        </Link>
        <Link href="/admin/payments" className="inline-link-btn">
          <VaultButton type="button" variant="secondary">
            Record payment
          </VaultButton>
        </Link>
      </div>
    </div>
  );
}
