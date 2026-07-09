import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { and, eq, isNull } from "drizzle-orm";
import { requireAdminAuth } from "@/lib/auth/admin-session";
import { getDb, entitlements } from "@/lib/db";

export const runtime = "nodejs";

const grantSchema = z.object({
  userId: z.number().int().positive(),
  contentId: z.number().int().positive(),
  expiresAt: z.string().datetime().nullable().optional(),
});

export async function POST(req: NextRequest) {
  try {
    const admin = await requireAdminAuth();
    const parsed = grantSchema.safeParse(await req.json());
    if (!parsed.success) {
      return NextResponse.json({ ok: false, error: "Invalid" }, { status: 400 });
    }

    const db = getDb();
    // Revoke any prior active entitlement for same pair, then grant fresh
    await db
      .update(entitlements)
      .set({ revokedAt: new Date() })
      .where(
        and(
          eq(entitlements.userId, parsed.data.userId),
          eq(entitlements.contentId, parsed.data.contentId),
          isNull(entitlements.revokedAt)
        )
      );

    const [row] = await db
      .insert(entitlements)
      .values({
        userId: parsed.data.userId,
        contentId: parsed.data.contentId,
        expiresAt: parsed.data.expiresAt ? new Date(parsed.data.expiresAt) : null,
        grantedByAdminId: admin.adminId,
      })
      .returning();

    return NextResponse.json({ ok: true, entitlement: row });
  } catch {
    return NextResponse.json({ ok: false, error: "Unauthorized" }, { status: 401 });
  }
}

const revokeSchema = z.object({
  entitlementId: z.number().int().positive(),
});

export async function DELETE(req: NextRequest) {
  try {
    await requireAdminAuth();
    const parsed = revokeSchema.safeParse(await req.json());
    if (!parsed.success) {
      return NextResponse.json({ ok: false, error: "Invalid" }, { status: 400 });
    }
    const db = getDb();
    await db
      .update(entitlements)
      .set({ revokedAt: new Date() })
      .where(eq(entitlements.id, parsed.data.entitlementId));
    return NextResponse.json({ ok: true });
  } catch {
    return NextResponse.json({ ok: false, error: "Unauthorized" }, { status: 401 });
  }
}
