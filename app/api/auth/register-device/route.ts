import { NextRequest, NextResponse } from "next/server";
import { z } from "zod";
import { registerDeviceAndSession } from "@/lib/auth/student-login";

export const runtime = "nodejs";

const bodySchema = z.object({
  registrationToken: z.string().min(10),
  publicKeySpkiB64: z.string().min(40),
  publicKeyAlgorithm: z.string().default("ECDSA_P256"),
  deviceLabel: z.string().max(120).optional(),
});

export async function POST(req: NextRequest) {
  try {
    const parsed = bodySchema.safeParse(await req.json());
    if (!parsed.success) {
      return NextResponse.json(
        { ok: false, error: "Invalid device registration payload." },
        { status: 400 }
      );
    }

    const result = await registerDeviceAndSession({
      registrationToken: parsed.data.registrationToken,
      publicKeySpkiB64: parsed.data.publicKeySpkiB64,
      publicKeyAlgorithm: parsed.data.publicKeyAlgorithm,
      deviceLabel: parsed.data.deviceLabel || "Browser",
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
    console.error("register device", err);
    return NextResponse.json(
      { ok: false, error: "Could not register device." },
      { status: 500 }
    );
  }
}
