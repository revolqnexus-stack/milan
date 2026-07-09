import { and, eq, gt, sql } from "drizzle-orm";
import { getDb, loginAttempts } from "@/lib/db";
import { hashIp } from "@/lib/crypto/tokens";

const WINDOW_MS = 15 * 60 * 1000;
const MAX_FAILURES = 12;

export async function assertLoginAllowed(studentId: string, ip: string | null) {
  const db = getDb();
  const since = new Date(Date.now() - WINDOW_MS);
  const key = studentId.trim().toLowerCase();

  const [{ count }] = await db
    .select({ count: sql<number>`count(*)::int` })
    .from(loginAttempts)
    .where(
      and(
        eq(loginAttempts.studentIdAttempt, key),
        eq(loginAttempts.success, false),
        gt(loginAttempts.createdAt, since)
      )
    );

  if ((count ?? 0) >= MAX_FAILURES) {
    throw new Error("RATE_LIMITED");
  }

  return hashIp(ip);
}

export async function recordLoginAttempt(opts: {
  studentId: string;
  ipHash: string | null;
  success: boolean;
}) {
  const db = getDb();
  await db.insert(loginAttempts).values({
    studentIdAttempt: opts.studentId.trim().toLowerCase(),
    ipHash: opts.ipHash,
    success: opts.success,
  });
}
