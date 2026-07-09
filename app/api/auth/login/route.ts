import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { startStudentLogin } from "@/lib/auth/student-login";

export const runtime = "nodejs";

const bodySchema = z.object({
  studentId: z.string().min(3).max(40),
  password: z.string().min(1).max(200),
});

export async function POST(req: NextRequest) {
  try {
    const json = await req.json();
    const parsed = bodySchema.safeParse(json);
    if (!parsed.success) {
      return NextResponse.json(
        { ok: false, error: "Enter Student ID and password." },
        { status: 400 }
      );
    }

    const ip =
      req.headers.get("x-forwarded-for")?.split(",")[0]?.trim() ||
      req.headers.get("x-real-ip") ||
      null;

    const result = await startStudentLogin({
      studentId: parsed.data.studentId,
      password: parsed.data.password,
      ip,
    });

    if (result.status === "ERROR") {
      const status = result.code === "RATE_LIMITED" ? 429 : 401;
      return NextResponse.json(
        { ok: false, error: result.error, code: result.code },
        { status }
      );
    }

    if (result.status === "REGISTER_DEVICE") {
      return NextResponse.json({
        ok: true,
        next: "REGISTER_DEVICE",
        registrationToken: result.registrationToken,
        studentId: result.studentId,
        name: result.name,
      });
    }

    return NextResponse.json({
      ok: true,
      next: "CHALLENGE",
      challengeId: result.challengeId,
      challenge: result.challenge,
      studentId: result.studentId,
      name: result.name,
    });
  } catch (err) {
    console.error("login start", err);
    return NextResponse.json(
      { ok: false, error: "Server error. Try again." },
      { status: 500 }
    );
  }
}
