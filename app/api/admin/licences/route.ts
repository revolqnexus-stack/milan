import { NextRequest, NextResponse } from "next/server";
import bcrypt from "bcryptjs";
import { getSql } from "@/lib/db";

export const runtime = "nodejs";

function assertAdmin(req: NextRequest) {
  const secret = process.env.ADMIN_SECRET;
  if (!secret) return false;
  const header = req.headers.get("x-admin-secret") || "";
  return header === secret;
}

export async function GET(req: NextRequest) {
  if (!assertAdmin(req)) {
    return NextResponse.json({ ok: false, error: "Unauthorized" }, { status: 401 });
  }
  const sql = getSql();
  const rows = await sql`
    SELECT id, login_id, device_id, buyer_note, active, unlocked_at, created_at
    FROM licences
    ORDER BY id DESC
  `;
  return NextResponse.json({ ok: true, licences: rows });
}

export async function POST(req: NextRequest) {
  if (!assertAdmin(req)) {
    return NextResponse.json({ ok: false, error: "Unauthorized" }, { status: 401 });
  }

  try {
    const body = (await req.json()) as {
      loginId?: string;
      password?: string;
      buyerNote?: string;
    };
    const loginId = (body.loginId || "").trim().toLowerCase();
    const password = body.password || "";
    const buyerNote = (body.buyerNote || "").trim() || null;

    if (!loginId || loginId.length < 3) {
      return NextResponse.json({ ok: false, error: "Login ID too short." }, { status: 400 });
    }
    if (!password || password.length < 6) {
      return NextResponse.json(
        { ok: false, error: "Password must be at least 6 characters." },
        { status: 400 }
      );
    }

    const hash = await bcrypt.hash(password, 10);
    const sql = getSql();

    await sql`
      INSERT INTO licences (login_id, password_hash, buyer_note, active)
      VALUES (${loginId}, ${hash}, ${buyerNote}, TRUE)
    `;

    return NextResponse.json({ ok: true, loginId });
  } catch (err: unknown) {
    const msg = err instanceof Error ? err.message : String(err);
    if (msg.includes("unique") || msg.includes("duplicate")) {
      return NextResponse.json(
        { ok: false, error: "That Login ID already exists." },
        { status: 409 }
      );
    }
    console.error("create licence", err);
    return NextResponse.json({ ok: false, error: "Could not create licence." }, { status: 500 });
  }
}

export async function PATCH(req: NextRequest) {
  if (!assertAdmin(req)) {
    return NextResponse.json({ ok: false, error: "Unauthorized" }, { status: 401 });
  }

  const body = (await req.json()) as {
    loginId?: string;
    action?: "reset_device" | "deactivate" | "activate";
  };
  const loginId = (body.loginId || "").trim().toLowerCase();
  const action = body.action;

  if (!loginId || !action) {
    return NextResponse.json({ ok: false, error: "Missing fields." }, { status: 400 });
  }

  const sql = getSql();

  if (action === "reset_device") {
    await sql`
      UPDATE licences
      SET device_id = NULL, unlocked_at = NULL
      WHERE lower(login_id) = ${loginId}
    `;
    return NextResponse.json({ ok: true, message: "Device unlocked. Buyer can bind a new phone." });
  }

  if (action === "deactivate") {
    await sql`UPDATE licences SET active = FALSE WHERE lower(login_id) = ${loginId}`;
    return NextResponse.json({ ok: true });
  }

  if (action === "activate") {
    await sql`UPDATE licences SET active = TRUE WHERE lower(login_id) = ${loginId}`;
    return NextResponse.json({ ok: true });
  }

  return NextResponse.json({ ok: false, error: "Unknown action." }, { status: 400 });
}
