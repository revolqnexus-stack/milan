import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { requireAdminAuth } from "@/lib/auth/admin-session";
import {
  getContentById,
  replaceContentHtml,
  updateContentMeta,
} from "@/lib/admin/content";

export const runtime = "nodejs";

export async function GET(
  _req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  try {
    await requireAdminAuth();
    const { id } = await ctx.params;
    const row = await getContentById(Number(id));
    if (!row) {
      return NextResponse.json({ ok: false, error: "Not found" }, { status: 404 });
    }
    return NextResponse.json({ ok: true, content: row });
  } catch {
    return NextResponse.json({ ok: false, error: "Unauthorized" }, { status: 401 });
  }
}

const metaSchema = z.object({
  title: z.string().min(2).optional(),
  course: z.string().min(1).optional(),
  studyYear: z.number().int().min(1).max(5).optional(),
  subject: z.string().min(1).optional(),
  paperCode: z.string().nullable().optional(),
  description: z.string().nullable().optional(),
  priceInrPaise: z.number().int().positive().optional(),
  sortOrder: z.number().int().optional(),
  isActive: z.boolean().optional(),
});

export async function PATCH(
  req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  try {
    await requireAdminAuth();
    const { id } = await ctx.params;
    const contentType = req.headers.get("content-type") || "";

    if (contentType.includes("multipart/form-data")) {
      const form = await req.formData();
      const html = form.get("html");
      if (html instanceof File && html.size > 0) {
        const row = await replaceContentHtml(Number(id), html);
        return NextResponse.json({ ok: true, content: row });
      }
      return NextResponse.json({ ok: false, error: "HTML required" }, { status: 400 });
    }

    const parsed = metaSchema.safeParse(await req.json());
    if (!parsed.success) {
      return NextResponse.json({ ok: false, error: "Invalid" }, { status: 400 });
    }
    const row = await updateContentMeta(Number(id), parsed.data);
    return NextResponse.json({ ok: true, content: row });
  } catch (err) {
    console.error("patch content", err);
    return NextResponse.json({ ok: false, error: "Failed" }, { status: 500 });
  }
}
