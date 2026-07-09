import { NextRequest, NextResponse } from "next/server";
import { requireAdminAuth } from "@/lib/auth/admin-session";
import { createContent, listAllContent } from "@/lib/admin/content";

export const runtime = "nodejs";

export async function GET() {
  try {
    await requireAdminAuth();
    const items = await listAllContent();
    return NextResponse.json({ ok: true, content: items });
  } catch {
    return NextResponse.json({ ok: false, error: "Unauthorized" }, { status: 401 });
  }
}

export async function POST(req: NextRequest) {
  try {
    await requireAdminAuth();
    const form = await req.formData();
    const title = String(form.get("title") || "");
    const course = String(form.get("course") || "GNM");
    const studyYear = Number(form.get("studyYear") || 1);
    const subject = String(form.get("subject") || title);
    const paperCode = String(form.get("paperCode") || "");
    const description = String(form.get("description") || "");
    const priceRupees = Number(form.get("priceRupees") || 299);
    const sortOrder = Number(form.get("sortOrder") || 0);
    const isActive = String(form.get("isActive") || "true") === "true";
    const htmlFile = form.get("html");
    const thumbFile = form.get("thumbnail");

    if (!title || !(htmlFile instanceof File) || htmlFile.size === 0) {
      return NextResponse.json(
        { ok: false, error: "Title and HTML file are required." },
        { status: 400 }
      );
    }

    const row = await createContent({
      title,
      course,
      studyYear,
      subject,
      paperCode: paperCode || undefined,
      description: description || undefined,
      priceInrPaise: Math.round(priceRupees * 100),
      sortOrder,
      isActive,
      htmlFile,
      thumbFile: thumbFile instanceof File && thumbFile.size > 0 ? thumbFile : null,
    });

    return NextResponse.json({ ok: true, content: row });
  } catch (err) {
    console.error("create content", err);
    const msg = err instanceof Error ? err.message : "Failed";
    return NextResponse.json({ ok: false, error: msg }, { status: 500 });
  }
}
