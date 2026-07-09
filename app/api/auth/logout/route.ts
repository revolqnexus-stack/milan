import { NextResponse } from "next/server";
import { and, eq, isNull } from "drizzle-orm";
import { getDb, sessions } from "@/lib/db";
import { hashToken } from "@/lib/crypto/tokens";
import {
  clearStudentSessionCookie,
  getStudentSessionToken,
} from "@/lib/auth/cookies";

export const runtime = "nodejs";

export async function POST() {
  const token = await getStudentSessionToken();
  if (token) {
    const db = getDb();
    await db
      .update(sessions)
      .set({ revokedAt: new Date() })
      .where(
        and(
          eq(sessions.sessionTokenHash, hashToken(token)),
          isNull(sessions.revokedAt)
        )
      );
  }
  await clearStudentSessionCookie();
  return NextResponse.json({ ok: true });
}
