import { NextResponse } from "next/server";
import { desc, eq } from "drizzle-orm";
import { requireAdminAuth } from "@/lib/auth/admin-session";
import { getDb, deviceResetLogs, users, admins } from "@/lib/db";

export const runtime = "nodejs";

export async function GET() {
  try {
    await requireAdminAuth();
    const db = getDb();
    const rows = await db
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
    return NextResponse.json({ ok: true, logs: rows });
  } catch {
    return NextResponse.json({ ok: false, error: "Unauthorized" }, { status: 401 });
  }
}
