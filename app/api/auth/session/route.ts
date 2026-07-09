import { NextResponse } from "next/server";
import { getStudentAuth } from "@/lib/auth/student-session";

export const runtime = "nodejs";

export async function GET() {
  const auth = await getStudentAuth();
  if (!auth) {
    return NextResponse.json({ ok: false });
  }
  return NextResponse.json({
    ok: true,
    studentId: auth.studentId,
    name: auth.name,
    deviceId: auth.deviceId,
  });
}
