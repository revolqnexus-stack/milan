import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { adminLogin } from "@/lib/auth/admin-login";

export const runtime = "nodejs";

const schema = z.object({
  // Admin ID (or legacy email) — not student ID
  email: z.string().min(3).max(120),
  password: z.string().min(1),
});

export async function POST(req: NextRequest) {
  try {
    const parsed = schema.safeParse(await req.json());
    if (!parsed.success) {
      return NextResponse.json(
        { ok: false, error: "Enter Admin ID and password." },
        { status: 400 }
      );
    }
    const result = await adminLogin(parsed.data.email, parsed.data.password);
    if (!result.ok) {
      return NextResponse.json(
        { ok: false, error: result.error },
        { status: 401 }
      );
    }
    return NextResponse.json({ ok: true, name: result.name, email: result.email });
  } catch (err) {
    console.error("admin login", err);
    return NextResponse.json({ ok: false, error: "Server error." }, { status: 500 });
  }
}
