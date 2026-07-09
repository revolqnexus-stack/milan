import { NextRequest, NextResponse } from "next/server";
import { getSql } from "@/lib/db";

export const runtime = "nodejs";

export async function POST(req: NextRequest) {
  try {
    const body = (await req.json()) as { loginId?: string; deviceId?: string };
    const loginId = (body.loginId || "").trim().toLowerCase();
    const deviceId = (body.deviceId || "").trim();

    if (!loginId || !deviceId) {
      return NextResponse.json({ ok: false }, { status: 400 });
    }

    const sql = getSql();
    const rows = await sql`
      SELECT login_id, device_id, active
      FROM licences
      WHERE lower(login_id) = ${loginId}
      LIMIT 1
    `;
    const row = rows[0] as
      | { login_id: string; device_id: string | null; active: boolean }
      | undefined;

    if (!row || !row.active || !row.device_id || row.device_id !== deviceId) {
      return NextResponse.json({ ok: false });
    }

    return NextResponse.json({ ok: true, loginId: row.login_id, deviceId });
  } catch (err) {
    console.error("session error", err);
    return NextResponse.json({ ok: false }, { status: 500 });
  }
}
