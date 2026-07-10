import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { requireAdminAuth } from "@/lib/auth/admin-session";
import {
  listAccessRequests,
  updateAccessRequestStatus,
} from "@/lib/admin/access-requests";

export const runtime = "nodejs";

export async function GET() {
  try {
    await requireAdminAuth();
    const requests = await listAccessRequests();
    return NextResponse.json({ ok: true, requests });
  } catch {
    return NextResponse.json({ ok: false, error: "Unauthorized" }, { status: 401 });
  }
}

const patchSchema = z.object({
  id: z.number().int().positive(),
  status: z
    .enum(["PENDING", "CONTACTED", "PAID", "APPROVED", "REJECTED"])
    .optional(),
  adminNotes: z.string().max(1000).nullable().optional(),
  linkedUserId: z.number().int().positive().nullable().optional(),
});

export async function PATCH(req: NextRequest) {
  try {
    await requireAdminAuth();
    const parsed = patchSchema.safeParse(await req.json());
    if (!parsed.success) {
      return NextResponse.json({ ok: false, error: "Invalid" }, { status: 400 });
    }
    const { id, ...patch } = parsed.data;
    const row = await updateAccessRequestStatus(id, patch);
    if (!row) {
      return NextResponse.json({ ok: false, error: "Not found" }, { status: 404 });
    }
    return NextResponse.json({ ok: true, request: row });
  } catch {
    return NextResponse.json({ ok: false, error: "Unauthorized" }, { status: 401 });
  }
}
