import { and, desc, eq, isNull, sql } from "drizzle-orm";
import { getDb, users, devices, entitlements, content } from "@/lib/db";
import {
  generateTempPassword,
  hashPassword,
} from "@/lib/crypto/password";

export async function nextStudentId(prefix = "GNM"): Promise<string> {
  const db = getDb();
  const rows = await db
    .select({ studentId: users.studentId })
    .from(users)
    .where(sql`${users.studentId} LIKE ${prefix + "%"}`)
    .orderBy(desc(users.id))
    .limit(50);

  let max = 10000;
  for (const r of rows) {
    const m = r.studentId.match(/(\d+)$/);
    if (m) max = Math.max(max, Number(m[1]));
  }
  return `${prefix}${max + 1}`;
}

export async function createStudent(opts: {
  name: string;
  studentId?: string;
}) {
  const db = getDb();
  const studentId = (opts.studentId?.trim() || (await nextStudentId())).toUpperCase();
  const tempPassword = generateTempPassword(10);
  const passwordHash = await hashPassword(tempPassword);

  const existing = await db
    .select({ id: users.id })
    .from(users)
    .where(eq(users.studentId, studentId))
    .limit(1);
  if (existing[0]) {
    return { ok: false as const, error: "Student ID already exists." };
  }

  const [row] = await db
    .insert(users)
    .values({
      studentId,
      name: opts.name.trim(),
      passwordHash,
      status: "ACTIVE",
    })
    .returning({ id: users.id, studentId: users.studentId, name: users.name });

  return {
    ok: true as const,
    user: row!,
    temporaryPassword: tempPassword,
  };
}

export async function resetStudentPassword(userId: number) {
  const db = getDb();
  const tempPassword = generateTempPassword(10);
  const passwordHash = await hashPassword(tempPassword);
  await db
    .update(users)
    .set({ passwordHash, updatedAt: new Date() })
    .where(eq(users.id, userId));
  return { temporaryPassword: tempPassword };
}

export async function listStudents() {
  const db = getDb();
  const rows = await db
    .select({
      id: users.id,
      studentId: users.studentId,
      name: users.name,
      status: users.status,
      createdAt: users.createdAt,
      lastLoginAt: users.lastLoginAt,
    })
    .from(users)
    .orderBy(desc(users.createdAt));

  const result = [];
  for (const u of rows) {
    const [dev] = await db
      .select({
        id: devices.id,
        deviceLabel: devices.deviceLabel,
        activatedAt: devices.activatedAt,
        lastSeenAt: devices.lastSeenAt,
      })
      .from(devices)
      .where(and(eq(devices.userId, u.id), isNull(devices.revokedAt)))
      .limit(1);

    const ents = await db
      .select({
        contentId: entitlements.contentId,
        title: content.title,
        slug: content.slug,
      })
      .from(entitlements)
      .innerJoin(content, eq(entitlements.contentId, content.id))
      .where(and(eq(entitlements.userId, u.id), isNull(entitlements.revokedAt)));

    result.push({
      ...u,
      device: dev || null,
      entitlements: ents,
    });
  }
  return result;
}

export async function getStudentDetail(userId: number) {
  const db = getDb();
  const [user] = await db.select().from(users).where(eq(users.id, userId)).limit(1);
  if (!user) return null;

  const deviceRows = await db
    .select()
    .from(devices)
    .where(eq(devices.userId, userId))
    .orderBy(desc(devices.createdAt));

  const ents = await db
    .select({
      id: entitlements.id,
      contentId: entitlements.contentId,
      title: content.title,
      slug: content.slug,
      grantedAt: entitlements.grantedAt,
      expiresAt: entitlements.expiresAt,
      revokedAt: entitlements.revokedAt,
    })
    .from(entitlements)
    .innerJoin(content, eq(entitlements.contentId, content.id))
    .where(eq(entitlements.userId, userId))
    .orderBy(desc(entitlements.createdAt));

  return { user, devices: deviceRows, entitlements: ents };
}
