import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { eq } from "drizzle-orm";
import { requireAdminAuth } from "@/lib/auth/admin-session";
import {
  getStudentDetail,
  resetStudentPassword,
} from "@/lib/admin/students";
import { resetStudentDevice } from "@/lib/admin/devices";
import { getDb, users } from "@/lib/db";

export const runtime = "nodejs";

export async function GET(
  _req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  try {
    await requireAdminAuth();
    const { id } = await ctx.params;
    const detail = await getStudentDetail(Number(id));
    if (!detail) {
      return NextResponse.json({ ok: false, error: "Not found" }, { status: 404 });
    }
    return NextResponse.json({ ok: true, ...detail });
  } catch {
    return NextResponse.json({ ok: false, error: "Unauthorized" }, { status: 401 });
  }
}

const patchSchema = z.object({
  action: z.enum([
    "disable",
    "activate",
    "suspend",
    "reset_password",
    "reset_device",
  ]),
  reason: z.string().max(500).optional(),
});

export async function PATCH(
  req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  try {
    const admin = await requireAdminAuth();
    const { id } = await ctx.params;
    const userId = Number(id);
    const parsed = patchSchema.safeParse(await req.json());
    if (!parsed.success) {
      return NextResponse.json({ ok: false, error: "Invalid action" }, { status: 400 });
    }

    const db = getDb();
    const action = parsed.data.action;

    if (action === "disable") {
      await db
        .update(users)
        .set({ status: "DISABLED", updatedAt: new Date() })
        .where(eq(users.id, userId));
      return NextResponse.json({ ok: true });
    }
    if (action === "activate") {
      await db
        .update(users)
        .set({ status: "ACTIVE", updatedAt: new Date() })
        .where(eq(users.id, userId));
      return NextResponse.json({ ok: true });
    }
    if (action === "suspend") {
      await db
        .update(users)
        .set({ status: "SUSPENDED", updatedAt: new Date() })
        .where(eq(users.id, userId));
      return NextResponse.json({ ok: true });
    }
    if (action === "reset_password") {
      const { temporaryPassword } = await resetStudentPassword(userId);
      return NextResponse.json({ ok: true, temporaryPassword });
    }
    if (action === "reset_device") {
      await resetStudentDevice({
        userId,
        adminId: admin.adminId,
        reason: parsed.data.reason || "Admin reset",
      });
      return NextResponse.json({ ok: true });
    }

    return NextResponse.json({ ok: false, error: "Unknown" }, { status: 400 });
  } catch {
    return NextResponse.json({ ok: false, error: "Unauthorized" }, { status: 401 });
  }
}
