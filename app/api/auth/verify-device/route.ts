import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { verifyChallengeAndSession } from "@/lib/auth/student-login";

export const runtime = "nodejs";

const bodySchema = z.object({
  challengeId: z.number().int().positive(),
  signatureB64: z.string().min(20),
});

export async function POST(req: NextRequest) {
  try {
    const parsed = bodySchema.safeParse(await req.json());
    if (!parsed.success) {
      return NextResponse.json(
        { ok: false, error: "Invalid challenge response." },
        { status: 400 }
      );
    }

    const result = await verifyChallengeAndSession({
      challengeId: parsed.data.challengeId,
      signatureB64: parsed.data.signatureB64,
    });

    if (!result.ok) {
      return NextResponse.json(
        { ok: false, error: result.error },
        { status: 403 }
      );
    }

    return NextResponse.json({
      ok: true,
      studentId: result.studentId,
      name: result.name,
    });
  } catch (err) {
    console.error("verify device", err);
    return NextResponse.json(
      { ok: false, error: "Device verification failed." },
      { status: 500 }
    );
  }
}
