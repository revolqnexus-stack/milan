import { and, eq } from "drizzle-orm";
import { getDb, admins, adminSessions } from "@/lib/db";
import { verifyPassword } from "@/lib/crypto/password";
import { hashToken, randomToken } from "@/lib/crypto/tokens";
import {
  ADMIN_SESSION_DAYS,
  ADMIN_SESSION_MAX_AGE,
} from "@/lib/auth/admin-session";
import { setAdminSessionCookie } from "@/lib/auth/cookies";

export async function adminLogin(adminId: string, password: string) {
  const db = getDb();
  const normalized = adminId.trim().toLowerCase();
  const rows = await db
    .select()
    .from(admins)
    .where(and(eq(admins.email, normalized), eq(admins.status, "ACTIVE")))
    .limit(1);
  const admin = rows[0];
  if (!admin) return { ok: false as const, error: "Invalid Admin ID or password." };

  const ok = await verifyPassword(password, admin.passwordHash);
  if (!ok) return { ok: false as const, error: "Invalid Admin ID or password." };

  const token = randomToken(32);
  const expiresAt = new Date(
    Date.now() + ADMIN_SESSION_DAYS * 24 * 60 * 60 * 1000
  );
  await db.insert(adminSessions).values({
    adminId: admin.id,
    sessionTokenHash: hashToken(token),
    expiresAt,
  });
  await setAdminSessionCookie(token, ADMIN_SESSION_MAX_AGE);

  return {
    ok: true as const,
    email: admin.email,
    name: admin.name,
  };
}
