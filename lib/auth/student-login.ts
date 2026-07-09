import { createHmac, timingSafeEqual } from "crypto";
import { and, eq, isNull } from "drizzle-orm";
import { getDb, users, devices, deviceChallenges, sessions } from "@/lib/db";
import { verifyPassword } from "@/lib/crypto/password";
import { hashToken, randomChallenge, randomToken } from "@/lib/crypto/tokens";
import { verifyDeviceSignature } from "@/lib/crypto/device-verify";
import {
  assertLoginAllowed,
  recordLoginAttempt,
} from "@/lib/auth/rate-limit";
import {
  STUDENT_SESSION_DAYS,
  STUDENT_SESSION_MAX_AGE,
} from "@/lib/auth/student-session";
import { setStudentSessionCookie } from "@/lib/auth/cookies";

const CHALLENGE_TTL_MS = 2 * 60 * 1000;

export type LoginStartResult =
  | {
      status: "REGISTER_DEVICE";
      registrationToken: string;
      studentId: string;
      name: string;
    }
  | {
      status: "CHALLENGE";
      challengeId: number;
      challenge: string;
      studentId: string;
      name: string;
    }
  | { status: "ERROR"; error: string; code?: string };

function regSecret() {
  return process.env.SESSION_SECRET || process.env.ADMIN_SECRET || "dev-only-change-me";
}

export function makeRegistrationToken(userId: number): string {
  const exp = Date.now() + 5 * 60 * 1000;
  const payload = `${userId}.${exp}`;
  const sig = createHmac("sha256", regSecret()).update(payload).digest("base64url");
  return `${payload}.${sig}`;
}

export function parseRegistrationToken(token: string): number | null {
  const parts = token.split(".");
  if (parts.length !== 3) return null;
  const [userIdStr, expStr, sig] = parts;
  const payload = `${userIdStr}.${expStr}`;
  const expected = createHmac("sha256", regSecret()).update(payload).digest("base64url");
  try {
    const a = Buffer.from(sig);
    const b = Buffer.from(expected);
    if (a.length !== b.length || !timingSafeEqual(a, b)) return null;
  } catch {
    return null;
  }
  if (Date.now() > Number(expStr)) return null;
  const userId = Number(userIdStr);
  return Number.isFinite(userId) ? userId : null;
}

export async function startStudentLogin(opts: {
  studentId: string;
  password: string;
  ip: string | null;
}): Promise<LoginStartResult> {
  const studentId = opts.studentId.trim().toUpperCase();
  let ipHash: string | null = null;
  try {
    ipHash = await assertLoginAllowed(studentId, opts.ip);
  } catch {
    return {
      status: "ERROR",
      error: "Too many failed attempts. Try again in 15 minutes.",
      code: "RATE_LIMITED",
    };
  }

  const db = getDb();
  const rows = await db
    .select()
    .from(users)
    .where(eq(users.studentId, studentId))
    .limit(1);
  const user = rows[0];

  if (!user || user.status !== "ACTIVE") {
    await recordLoginAttempt({ studentId, ipHash, success: false });
    return { status: "ERROR", error: "Invalid Student ID or password." };
  }

  const ok = await verifyPassword(opts.password, user.passwordHash);
  if (!ok) {
    await recordLoginAttempt({ studentId, ipHash, success: false });
    return { status: "ERROR", error: "Invalid Student ID or password." };
  }

  await recordLoginAttempt({ studentId, ipHash, success: true });

  const activeDevices = await db
    .select()
    .from(devices)
    .where(and(eq(devices.userId, user.id), isNull(devices.revokedAt)))
    .limit(1);

  const device = activeDevices[0];

  if (!device) {
    return {
      status: "REGISTER_DEVICE",
      registrationToken: makeRegistrationToken(user.id),
      studentId: user.studentId,
      name: user.name,
    };
  }

  const challenge = randomChallenge(32);
  const expiresAt = new Date(Date.now() + CHALLENGE_TTL_MS);
  const [created] = await db
    .insert(deviceChallenges)
    .values({
      userId: user.id,
      deviceId: device.id,
      challenge,
      expiresAt,
    })
    .returning({ id: deviceChallenges.id });

  return {
    status: "CHALLENGE",
    challengeId: created!.id,
    challenge,
    studentId: user.studentId,
    name: user.name,
  };
}

export async function registerDeviceAndSession(opts: {
  registrationToken: string;
  publicKeySpkiB64: string;
  publicKeyAlgorithm: string;
  deviceLabel: string;
}) {
  const userId = parseRegistrationToken(opts.registrationToken);
  if (!userId) {
    return { ok: false as const, error: "Registration expired. Log in again." };
  }

  if (!opts.publicKeySpkiB64 || opts.publicKeySpkiB64.length < 40) {
    return { ok: false as const, error: "Invalid public key." };
  }

  const db = getDb();
  const userRows = await db
    .select()
    .from(users)
    .where(and(eq(users.id, userId), eq(users.status, "ACTIVE")))
    .limit(1);
  const user = userRows[0];
  if (!user) return { ok: false as const, error: "Account not found." };

  const existing = await db
    .select()
    .from(devices)
    .where(and(eq(devices.userId, user.id), isNull(devices.revokedAt)))
    .limit(1);
  if (existing[0]) {
    return {
      ok: false as const,
      error: "A device is already registered. Contact admin for reset.",
    };
  }

  const [device] = await db
    .insert(devices)
    .values({
      userId: user.id,
      publicKey: opts.publicKeySpkiB64,
      publicKeyAlgorithm: opts.publicKeyAlgorithm || "ECDSA_P256",
      deviceLabel: opts.deviceLabel || "Browser",
    })
    .returning();

  const session = await createStudentSession(user.id, device!.id);
  await db
    .update(users)
    .set({ lastLoginAt: new Date(), updatedAt: new Date() })
    .where(eq(users.id, user.id));

  return {
    ok: true as const,
    studentId: user.studentId,
    name: user.name,
    deviceId: device!.id,
    maxAge: STUDENT_SESSION_MAX_AGE,
  };
}

export async function verifyChallengeAndSession(opts: {
  challengeId: number;
  signatureB64: string;
}) {
  const db = getDb();
  const now = new Date();
  const rows = await db
    .select({
      challenge: deviceChallenges,
      device: devices,
      user: users,
    })
    .from(deviceChallenges)
    .innerJoin(devices, eq(deviceChallenges.deviceId, devices.id))
    .innerJoin(users, eq(deviceChallenges.userId, users.id))
    .where(eq(deviceChallenges.id, opts.challengeId))
    .limit(1);

  const row = rows[0];
  if (!row) return { ok: false as const, error: "Challenge not found." };
  if (row.challenge.consumedAt) {
    return { ok: false as const, error: "Challenge already used." };
  }
  if (row.challenge.expiresAt <= now) {
    return { ok: false as const, error: "Challenge expired. Log in again." };
  }
  if (row.device.revokedAt) {
    return { ok: false as const, error: "Device revoked. Contact admin." };
  }
  if (row.user.status !== "ACTIVE") {
    return { ok: false as const, error: "Account disabled." };
  }

  const valid = verifyDeviceSignature({
    publicKeySpkiB64: row.device.publicKey,
    challenge: row.challenge.challenge,
    signatureB64: opts.signatureB64,
    algorithm: row.device.publicKeyAlgorithm,
  });

  if (!valid) {
    return {
      ok: false as const,
      error: "Device not authorised. This account is locked to another browser.",
    };
  }

  await db
    .update(deviceChallenges)
    .set({ consumedAt: now })
    .where(eq(deviceChallenges.id, row.challenge.id));

  await createStudentSession(row.user.id, row.device.id);
  await db
    .update(users)
    .set({ lastLoginAt: now, updatedAt: now })
    .where(eq(users.id, row.user.id));
  await db
    .update(devices)
    .set({ lastSeenAt: now })
    .where(eq(devices.id, row.device.id));

  return {
    ok: true as const,
    studentId: row.user.studentId,
    name: row.user.name,
    deviceId: row.device.id,
  };
}

async function createStudentSession(userId: number, deviceId: number) {
  const db = getDb();
  const token = randomToken(32);
  const tokenHash = hashToken(token);
  const expiresAt = new Date(
    Date.now() + STUDENT_SESSION_DAYS * 24 * 60 * 60 * 1000
  );

  await db.insert(sessions).values({
    userId,
    deviceId,
    sessionTokenHash: tokenHash,
    expiresAt,
  });

  await setStudentSessionCookie(token, STUDENT_SESSION_MAX_AGE);
  return token;
}
