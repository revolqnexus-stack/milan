import { and, eq, isNull } from "drizzle-orm";
import {
  getDb,
  devices,
  sessions,
  deviceResetLogs,
} from "@/lib/db";

export async function resetStudentDevice(opts: {
  userId: number;
  adminId: number;
  reason: string;
}) {
  const db = getDb();
  const [active] = await db
    .select()
    .from(devices)
    .where(and(eq(devices.userId, opts.userId), isNull(devices.revokedAt)))
    .limit(1);

  const now = new Date();

  if (active) {
    await db
      .update(devices)
      .set({ revokedAt: now })
      .where(eq(devices.id, active.id));

    await db
      .update(sessions)
      .set({ revokedAt: now })
      .where(
        and(eq(sessions.deviceId, active.id), isNull(sessions.revokedAt))
      );
  }

  // Revoke all sessions for user for safety
  await db
    .update(sessions)
    .set({ revokedAt: now })
    .where(and(eq(sessions.userId, opts.userId), isNull(sessions.revokedAt)));

  await db.insert(deviceResetLogs).values({
    userId: opts.userId,
    oldDeviceId: active?.id ?? null,
    adminId: opts.adminId,
    reason: opts.reason.trim() || "Admin reset",
  });

  return { ok: true as const, oldDeviceId: active?.id ?? null };
}
