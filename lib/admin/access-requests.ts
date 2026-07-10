import { and, desc, eq } from "drizzle-orm";
import { getDb, accessRequests, content, users } from "@/lib/db";

export async function listAccessRequests() {
  const db = getDb();
  return db
    .select({
      id: accessRequests.id,
      name: accessRequests.name,
      phone: accessRequests.phone,
      college: accessRequests.college,
      status: accessRequests.status,
      adminNotes: accessRequests.adminNotes,
      linkedUserId: accessRequests.linkedUserId,
      createdAt: accessRequests.createdAt,
      updatedAt: accessRequests.updatedAt,
      contentId: content.id,
      contentTitle: content.title,
      contentPaperCode: content.paperCode,
      priceInrPaise: content.priceInrPaise,
    })
    .from(accessRequests)
    .innerJoin(content, eq(accessRequests.contentId, content.id))
    .orderBy(desc(accessRequests.createdAt));
}

export async function getAccessRequestById(id: number) {
  const db = getDb();
  const [row] = await db
    .select()
    .from(accessRequests)
    .where(eq(accessRequests.id, id))
    .limit(1);
  return row ?? null;
}

export async function createAccessRequest(opts: {
  contentId: number;
  name: string;
  phone: string;
  college?: string;
}) {
  const db = getDb();
  const [row] = await db
    .insert(accessRequests)
    .values({
      contentId: opts.contentId,
      name: opts.name.trim(),
      phone: opts.phone.trim(),
      college: opts.college?.trim() || null,
    })
    .returning();
  return row!;
}

export async function updateAccessRequestStatus(
  id: number,
  patch: {
    status?: "PENDING" | "CONTACTED" | "PAID" | "APPROVED" | "REJECTED";
    adminNotes?: string | null;
    linkedUserId?: number | null;
  }
) {
  const db = getDb();
  const [row] = await db
    .update(accessRequests)
    .set({ ...patch, updatedAt: new Date() })
    .where(eq(accessRequests.id, id))
    .returning();
  return row ?? null;
}
