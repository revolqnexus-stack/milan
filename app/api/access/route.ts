import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { eq } from "drizzle-orm";
import { getDb, content } from "@/lib/db";
import { createAccessRequest } from "@/lib/admin/access-requests";

export const runtime = "nodejs";

const schema = z.object({
  contentId: z.number().int().positive(),
  name: z.string().min(2).max(120),
  phone: z.string().min(7).max(30),
  college: z.string().max(200).optional(),
});

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const parsed = schema.safeParse(body);
    if (!parsed.success) {
      return NextResponse.json(
        { ok: false, error: "Invalid fields" },
        { status: 400 }
      );
    }

    // Confirm content exists and is active
    const db = getDb();
    const [pack] = await db
      .select({ id: content.id })
      .from(content)
      .where(eq(content.id, parsed.data.contentId))
      .limit(1);

    if (!pack) {
      return NextResponse.json(
        { ok: false, error: "Study pack not found" },
        { status: 404 }
      );
    }

    const request = await createAccessRequest({
      contentId: parsed.data.contentId,
      name: parsed.data.name,
      phone: parsed.data.phone,
      college: parsed.data.college,
    });

    return NextResponse.json({ ok: true, id: request.id });
  } catch (err) {
    console.error("access request create", err);
    return NextResponse.json({ ok: false, error: "Failed" }, { status: 500 });
  }
}
