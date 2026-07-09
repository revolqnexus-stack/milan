import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { requireAdminAuth } from "@/lib/auth/admin-session";
import { createStudent, listStudents } from "@/lib/admin/students";

export const runtime = "nodejs";

export async function GET() {
  try {
    await requireAdminAuth();
    const students = await listStudents();
    return NextResponse.json({ ok: true, students });
  } catch {
    return NextResponse.json({ ok: false, error: "Unauthorized" }, { status: 401 });
  }
}

const createSchema = z.object({
  name: z.string().min(2).max(120),
  studentId: z.string().min(3).max(40).optional(),
});

export async function POST(req: NextRequest) {
  try {
    await requireAdminAuth();
    const parsed = createSchema.safeParse(await req.json());
    if (!parsed.success) {
      return NextResponse.json({ ok: false, error: "Invalid fields" }, { status: 400 });
    }
    const result = await createStudent(parsed.data);
    if (!result.ok) {
      return NextResponse.json({ ok: false, error: result.error }, { status: 409 });
    }
    return NextResponse.json({
      ok: true,
      user: result.user,
      temporaryPassword: result.temporaryPassword,
    });
  } catch {
    return NextResponse.json({ ok: false, error: "Unauthorized" }, { status: 401 });
  }
}
