import Link from "next/link";
import { getAdminAuth } from "@/lib/auth/admin-session";
import { AdminLogoutButton } from "./logout-button";
import { ThemeToggle } from "@/components/ui/ThemeToggle";

export default async function AdminLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const auth = await getAdminAuth();

  if (!auth) {
    return <>{children}</>;
  }

  return (
    <div className="admin-shell vault-atmosphere">
      <aside className="admin-nav">
        <div className="admin-brand">
          REVOLQ<span style={{ color: "var(--vault-blue)" }}>NEXUS</span>
        </div>
        <p className="admin-user">{auth.name} · Admin</p>
        <nav>
          <Link href="/admin">Dashboard</Link>
          <Link href="/admin/content">Study Content</Link>
          <Link href="/admin/content/new">+ Add material</Link>
          <Link href="/admin/students">Students</Link>
          <Link href="/admin/access-requests">Access Requests</Link>
          <Link href="/admin/entitlements">Entitlements</Link>
          <Link href="/admin/payments">Payments</Link>
          <Link href="/admin/device-resets">Device Resets</Link>
        </nav>
        <div style={{ display: "flex", gap: 8, alignItems: "center", marginTop: 12 }}>
          <ThemeToggle />
          <AdminLogoutButton />
        </div>
      </aside>
      <div className="admin-main">{children}</div>
    </div>
  );
}
