import { NextRequest, NextResponse } from "next/server";
import bcrypt from "bcryptjs";
import { getSql } from "@/lib/db";

export const runtime = "nodejs";

type Body = {
  loginId?: string;
  password?: string;
  deviceId?: string;
};

export async function POST(req: NextRequest) {
  try {
    const body = (await req.json()) as Body;
    const loginId = (body.loginId || "").trim().toLowerCase();
    const password = body.password || "";
    const deviceId = (body.deviceId || "").trim();

    if (!loginId || !password || !deviceId) {
      return NextResponse.json(
        { ok: false, error: "Login ID, password and device are required." },
        { status: 400 }
      );
    }

    if (deviceId.length < 8 || deviceId.length > 120) {
      return NextResponse.json({ ok: false, error: "Invalid device." }, { status: 400 });
    }

    const sql = getSql();
    const rows = await sql`
      SELECT id, login_id, password_hash, device_id, active
      FROM licences
      WHERE lower(login_id) = ${loginId}
      LIMIT 1
    `;

    const row = rows[0] as
      | {
          id: number;
          login_id: string;
          password_hash: string;
          device_id: string | null;
          active: boolean;
        }
      | undefined;

    if (!row || !row.active) {
      return NextResponse.json(
        { ok: false, error: "Wrong Login ID or password." },
        { status: 401 }
      );
    }

    const passOk = await bcrypt.compare(password, row.password_hash);
    if (!passOk) {
      return NextResponse.json(
        { ok: false, error: "Wrong Login ID or password." },
        { status: 401 }
      );
    }

    if (row.device_id && row.device_id !== deviceId) {
      return NextResponse.json(
        {
          ok: false,
          error:
            "This licence is locked to another device. Contact seller for reset (₹200 = 1 device).",
        },
        { status: 403 }
      );
    }

    if (!row.device_id) {
      await sql`
        UPDATE licences
        SET device_id = ${deviceId}, unlocked_at = NOW()
        WHERE id = ${row.id} AND device_id IS NULL
      `;
      // Re-check in case of race
      const again = await sql`
        SELECT device_id FROM licences WHERE id = ${row.id} LIMIT 1
      `;
      const bound = (again[0] as { device_id: string | null } | undefined)?.device_id;
      if (bound && bound !== deviceId) {
        return NextResponse.json(
          {
            ok: false,
            error:
              "This licence is locked to another device. Contact seller for reset (₹200 = 1 device).",
          },
          { status: 403 }
        );
      }
    } else {
      await sql`
        UPDATE licences SET unlocked_at = NOW() WHERE id = ${row.id}
      `;
    }

    return NextResponse.json({
      ok: true,
      loginId: row.login_id,
      deviceId,
      message: "Unlocked on this device.",
    });
  } catch (err) {
    console.error("login error", err);
    return NextResponse.json(
      { ok: false, error: "Server error. Try again in a moment." },
      { status: 500 }
    );
  }
}
