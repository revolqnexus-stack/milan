import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { desc } from "drizzle-orm";
import { requireAdminAuth } from "@/lib/auth/admin-session";
import { getDb, payments, users } from "@/lib/db";
import { eq } from "drizzle-orm";

export const runtime = "nodejs";

export async function GET() {
  try {
    await requireAdminAuth();
    const db = getDb();
    const rows = await db
      .select({
        id: payments.id,
        amountPaise: payments.amountPaise,
        paymentReference: payments.paymentReference,
        paymentMethod: payments.paymentMethod,
        status: payments.status,
        notes: payments.notes,
        createdAt: payments.createdAt,
        confirmedAt: payments.confirmedAt,
        studentId: users.studentId,
        name: users.name,
        userId: users.id,
      })
      .from(payments)
      .innerJoin(users, eq(payments.userId, users.id))
      .orderBy(desc(payments.createdAt));
    return NextResponse.json({ ok: true, payments: rows });
  } catch {
    return NextResponse.json({ ok: false, error: "Unauthorized" }, { status: 401 });
  }
}

const createSchema = z.object({
  userId: z.number().int().positive(),
  amountRupees: z.number().positive(),
  paymentMethod: z.enum(["UPI", "BANK_TRANSFER", "CASH", "RAZORPAY"]),
  paymentReference: z.string().max(200).optional(),
  notes: z.string().max(1000).optional(),
  status: z.enum(["PENDING", "CONFIRMED", "FAILED", "REFUNDED"]).default("CONFIRMED"),
});

export async function POST(req: NextRequest) {
  try {
    await requireAdminAuth();
    const parsed = createSchema.safeParse(await req.json());
    if (!parsed.success) {
      return NextResponse.json({ ok: false, error: "Invalid" }, { status: 400 });
    }
    const db = getDb();
    const [row] = await db
      .insert(payments)
      .values({
        userId: parsed.data.userId,
        amountPaise: Math.round(parsed.data.amountRupees * 100),
        paymentMethod: parsed.data.paymentMethod,
        paymentReference: parsed.data.paymentReference || null,
        notes: parsed.data.notes || null,
        status: parsed.data.status,
        confirmedAt:
          parsed.data.status === "CONFIRMED" ? new Date() : null,
      })
      .returning();
    return NextResponse.json({ ok: true, payment: row });
  } catch {
    return NextResponse.json({ ok: false, error: "Unauthorized" }, { status: 401 });
  }
}
