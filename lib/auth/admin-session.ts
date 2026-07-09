import { and, eq, gt, isNull } from "drizzle-orm";
import { getDb, adminSessions, admins } from "@/lib/db";
import { hashToken } from "@/lib/crypto/tokens";
import {
  clearAdminSessionCookie,
  getAdminSessionToken,
} from "@/lib/auth/cookies";

export const ADMIN_SESSION_DAYS = 7;
export const ADMIN_SESSION_MAX_AGE = ADMIN_SESSION_DAYS * 24 * 60 * 60;

export type AdminAuth = {
  adminId: number;
  email: string;
  name: string;
  role: "OWNER" | "ADMIN" | "SUPPORT";
  sessionId: number;
};

export async function getAdminAuth(): Promise<AdminAuth | null> {
  const token = await getAdminSessionToken();
  if (!token) return null;

  const tokenHash = hashToken(token);
  const db = getDb();
  const now = new Date();

  const rows = await db
    .select({
      sessionId: adminSessions.id,
      adminId: adminSessions.adminId,
      email: admins.email,
      name: admins.name,
      role: admins.role,
    })
    .from(adminSessions)
    .innerJoin(admins, eq(adminSessions.adminId, admins.id))
    .where(
      and(
        eq(adminSessions.sessionTokenHash, tokenHash),
        isNull(adminSessions.revokedAt),
        gt(adminSessions.expiresAt, now),
        eq(admins.status, "ACTIVE")
      )
    )
    .limit(1);

  const row = rows[0];
  if (!row) {
    await clearAdminSessionCookie();
    return null;
  }

  await db
    .update(adminSessions)
    .set({ lastSeenAt: now })
    .where(eq(adminSessions.id, row.sessionId));

  return {
    adminId: row.adminId,
    email: row.email,
    name: row.name,
    role: row.role,
    sessionId: row.sessionId,
  };
}

export async function requireAdminAuth(): Promise<AdminAuth> {
  const auth = await getAdminAuth();
  if (!auth) throw new Error("UNAUTHORIZED");
  return auth;
}
