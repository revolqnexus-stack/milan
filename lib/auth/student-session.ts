import { and, eq, gt, isNull } from "drizzle-orm";
import { getDb, sessions, users, devices } from "@/lib/db";
import { hashToken } from "@/lib/crypto/tokens";
import {
  clearStudentSessionCookie,
  getStudentSessionToken,
} from "@/lib/auth/cookies";

export const STUDENT_SESSION_DAYS = 30;
export const STUDENT_SESSION_MAX_AGE = STUDENT_SESSION_DAYS * 24 * 60 * 60;

export type StudentAuth = {
  userId: number;
  studentId: string;
  name: string;
  deviceId: number;
  sessionId: number;
};

export async function getStudentAuth(): Promise<StudentAuth | null> {
  const token = await getStudentSessionToken();
  if (!token) return null;

  const tokenHash = hashToken(token);
  const db = getDb();
  const now = new Date();

  const rows = await db
    .select({
      sessionId: sessions.id,
      userId: sessions.userId,
      deviceId: sessions.deviceId,
      studentId: users.studentId,
      name: users.name,
      userStatus: users.status,
      sessionRevoked: sessions.revokedAt,
      sessionExpires: sessions.expiresAt,
      deviceRevoked: devices.revokedAt,
    })
    .from(sessions)
    .innerJoin(users, eq(sessions.userId, users.id))
    .innerJoin(devices, eq(sessions.deviceId, devices.id))
    .where(
      and(
        eq(sessions.sessionTokenHash, tokenHash),
        isNull(sessions.revokedAt),
        gt(sessions.expiresAt, now),
        isNull(devices.revokedAt),
        eq(users.status, "ACTIVE")
      )
    )
    .limit(1);

  const row = rows[0];
  if (!row) {
    await clearStudentSessionCookie();
    return null;
  }

  // Touch last_seen (best-effort)
  await db
    .update(sessions)
    .set({ lastSeenAt: now })
    .where(eq(sessions.id, row.sessionId));
  await db
    .update(devices)
    .set({ lastSeenAt: now })
    .where(eq(devices.id, row.deviceId));

  return {
    userId: row.userId,
    studentId: row.studentId,
    name: row.name,
    deviceId: row.deviceId,
    sessionId: row.sessionId,
  };
}

export async function requireStudentAuth(): Promise<StudentAuth> {
  const auth = await getStudentAuth();
  if (!auth) throw new Error("UNAUTHORIZED");
  return auth;
}
