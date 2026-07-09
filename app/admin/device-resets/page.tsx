import { redirect } from "next/navigation";
import { desc, eq } from "drizzle-orm";
import { getAdminAuth } from "@/lib/auth/admin-session";
import { getDb, deviceResetLogs, users, admins } from "@/lib/db";
import { PageEyebrow } from "@/components/ui/PageEyebrow";

export const dynamic = "force-dynamic";

export default async function DeviceResetsPage() {
  const auth = await getAdminAuth();
  if (!auth) redirect("/admin/login");

  const db = getDb();
  const logs = await db
    .select({
      id: deviceResetLogs.id,
      reason: deviceResetLogs.reason,
      createdAt: deviceResetLogs.createdAt,
      oldDeviceId: deviceResetLogs.oldDeviceId,
      studentId: users.studentId,
      studentName: users.name,
      adminName: admins.name,
    })
    .from(deviceResetLogs)
    .innerJoin(users, eq(deviceResetLogs.userId, users.id))
    .leftJoin(admins, eq(deviceResetLogs.adminId, admins.id))
    .orderBy(desc(deviceResetLogs.createdAt));

  return (
    <div>
      <PageEyebrow>Device resets</PageEyebrow>
      <h1 className="admin-h1">Reset history.</h1>
      <p className="admin-lead">Audit log of every admin device reset.</p>
      <div className="admin-list">
        {logs.map((l) => (
          <div key={l.id} className="admin-row">
            <div>
              <strong>
                {l.studentId} · {l.studentName}
              </strong>
              <div className="muted">
                {new Date(l.createdAt).toLocaleString()} · {l.adminName || "Admin"} ·{" "}
                {l.reason}
                {l.oldDeviceId ? ` · old device #${l.oldDeviceId}` : ""}
              </div>
            </div>
          </div>
        ))}
        {logs.length === 0 && <p className="muted">No resets yet.</p>}
      </div>
    </div>
  );
}
