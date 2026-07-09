import { asc, eq } from "drizzle-orm";
import { getDb, content } from "@/lib/db";
import { uploadPrivateHtml, uploadPrivateThumbnail } from "@/lib/blob/storage";

function slugify(input: string): string {
  return input
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "")
    .slice(0, 80);
}

export async function listAllContent() {
  const db = getDb();
  return db.select().from(content).orderBy(asc(content.sortOrder), asc(content.title));
}

export async function getContentById(id: number) {
  const db = getDb();
  const [row] = await db.select().from(content).where(eq(content.id, id)).limit(1);
  return row || null;
}

export async function getContentBySlug(slug: string) {
  const db = getDb();
  const [row] = await db.select().from(content).where(eq(content.slug, slug)).limit(1);
  return row || null;
}

export async function createContent(opts: {
  title: string;
  course: string;
  studyYear: number;
  subject: string;
  paperCode?: string;
  description?: string;
  priceInrPaise: number;
  sortOrder?: number;
  isActive: boolean;
  htmlFile: File;
  thumbFile?: File | null;
}) {
  const db = getDb();
  let slug = slugify(opts.title);
  if (!slug) slug = `content-${Date.now()}`;

  const existing = await getContentBySlug(slug);
  if (existing) slug = `${slug}-${Date.now().toString(36)}`;

  const htmlBuf = Buffer.from(await opts.htmlFile.arrayBuffer());
  const uploaded = await uploadPrivateHtml({ slug, bytes: htmlBuf });

  let thumbPath: string | null = null;
  if (opts.thumbFile) {
    const ext =
      opts.thumbFile.name.split(".").pop()?.toLowerCase().replace(/[^a-z0-9]/g, "") ||
      "png";
    const t = await uploadPrivateThumbnail({
      slug,
      bytes: Buffer.from(await opts.thumbFile.arrayBuffer()),
      contentType: opts.thumbFile.type || "image/png",
      ext,
    });
    thumbPath = t.pathname;
  }

  const [row] = await db
    .insert(content)
    .values({
      title: opts.title.trim(),
      slug,
      course: opts.course.trim() || "GNM",
      studyYear: opts.studyYear,
      subject: opts.subject.trim() || opts.title.trim(),
      paperCode: opts.paperCode?.trim() || null,
      description: opts.description?.trim() || null,
      htmlBlobPath: uploaded.pathname,
      thumbnailBlobPath: thumbPath,
      priceInrPaise: opts.priceInrPaise,
      isActive: opts.isActive,
      sortOrder: opts.sortOrder ?? 0,
    })
    .returning();

  return row!;
}

export async function updateContentMeta(
  id: number,
  patch: Partial<{
    title: string;
    course: string;
    studyYear: number;
    subject: string;
    paperCode: string | null;
    description: string | null;
    priceInrPaise: number;
    sortOrder: number;
    isActive: boolean;
  }>
) {
  const db = getDb();
  const [row] = await db
    .update(content)
    .set({ ...patch, updatedAt: new Date() })
    .where(eq(content.id, id))
    .returning();
  return row || null;
}

export async function replaceContentHtml(id: number, htmlFile: File) {
  const existing = await getContentById(id);
  if (!existing) return null;
  const htmlBuf = Buffer.from(await htmlFile.arrayBuffer());
  const uploaded = await uploadPrivateHtml({
    slug: existing.slug,
    bytes: htmlBuf,
  });
  const db = getDb();
  const [row] = await db
    .update(content)
    .set({ htmlBlobPath: uploaded.pathname, updatedAt: new Date() })
    .where(eq(content.id, id))
    .returning();
  return row || null;
}
