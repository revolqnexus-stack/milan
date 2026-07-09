import { cookies } from "next/headers";

export const STUDENT_COOKIE = "milan_student_session";
export const ADMIN_COOKIE = "milan_admin_session";

const isProd = process.env.NODE_ENV === "production";

export function sessionCookieOptions(maxAgeSec: number) {
  return {
    httpOnly: true,
    secure: isProd,
    sameSite: "lax" as const,
    path: "/",
    maxAge: maxAgeSec,
  };
}

export async function setStudentSessionCookie(token: string, maxAgeSec: number) {
  const jar = await cookies();
  jar.set(STUDENT_COOKIE, token, sessionCookieOptions(maxAgeSec));
}

export async function clearStudentSessionCookie() {
  const jar = await cookies();
  jar.set(STUDENT_COOKIE, "", { ...sessionCookieOptions(0), maxAge: 0 });
}

export async function setAdminSessionCookie(token: string, maxAgeSec: number) {
  const jar = await cookies();
  jar.set(ADMIN_COOKIE, token, sessionCookieOptions(maxAgeSec));
}

export async function clearAdminSessionCookie() {
  const jar = await cookies();
  jar.set(ADMIN_COOKIE, "", { ...sessionCookieOptions(0), maxAge: 0 });
}

export async function getStudentSessionToken(): Promise<string | null> {
  const jar = await cookies();
  return jar.get(STUDENT_COOKIE)?.value ?? null;
}

export async function getAdminSessionToken(): Promise<string | null> {
  const jar = await cookies();
  return jar.get(ADMIN_COOKIE)?.value ?? null;
}
