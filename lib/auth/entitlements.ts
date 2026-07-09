import { and, asc, eq, gt, isNull, or } from "drizzle-orm";
import { getDb, entitlements, content } from "@/lib/db";

export async function hasValidEntitlement(userId: number, contentId: number) {
  const db = getDb();
  const now = new Date();
  const rows = await db
    .select({ id: entitlements.id })
    .from(entitlements)
    .innerJoin(content, eq(entitlements.contentId, content.id))
    .where(
      and(
        eq(entitlements.userId, userId),
        eq(entitlements.contentId, contentId),
        isNull(entitlements.revokedAt),
        eq(content.isActive, true),
        or(isNull(entitlements.expiresAt), gt(entitlements.expiresAt, now))
      )
    )
    .limit(1);
  return !!rows[0];
}

export async function listLibraryForUser(userId: number) {
  const db = getDb();
  const now = new Date();

  const allContent = await db
    .select()
    .from(content)
    .where(eq(content.isActive, true))
    .orderBy(
      asc(content.course),
      asc(content.studyYear),
      asc(content.sortOrder),
      asc(content.title)
    );

  const ents = await db
    .select()
    .from(entitlements)
    .where(
      and(
        eq(entitlements.userId, userId),
        isNull(entitlements.revokedAt),
        or(isNull(entitlements.expiresAt), gt(entitlements.expiresAt, now))
      )
    );

  const entitled = new Set(ents.map((e) => e.contentId));

  return allContent.map((c) => ({
    id: c.id,
    title: c.title,
    slug: c.slug,
    course: c.course,
    studyYear: c.studyYear,
    subject: c.subject,
    paperCode: c.paperCode,
    description: c.description,
    priceInrPaise: c.priceInrPaise,
    entitled: entitled.has(c.id),
  }));
}
