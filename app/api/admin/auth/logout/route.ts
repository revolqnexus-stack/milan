import { NextResponse } from "next/server";
import { and, eq, isNull } from "drizzle-orm";
import { getDb, adminSessions } from "@/lib/db";
import { hashToken } from "@/lib/crypto/tokens";
import {
  clearAdminSessionCookie,
  getAdminSessionToken,
} from "@/lib/auth/cookies";

export const runtime = "nodejs";

export async function POST() {
  const token = await getAdminSessionToken();
  if (token) {
    const db = getDb();
    await db
      .update(adminSessions)
      .set({ revokedAt: new Date() })
      .where(
        and(
          eq(adminSessions.sessionTokenHash, hashToken(token)),
          isNull(adminSessions.revokedAt)
        )
      );
  }
  await clearAdminSessionCookie();
  return NextResponse.json({ ok: true });
}
