import { NextRequest, NextResponse } from "next/server";

const STUDENT_COOKIE = "milan_student_session";
const ADMIN_COOKIE = "milan_admin_session";

export function middleware(req: NextRequest) {
  const { pathname } = req.nextUrl;

  // Block legacy public study HTML if still present
  if (pathname === "/app.html" || pathname.startsWith("/study-content/")) {
    return NextResponse.redirect(new URL("/library", req.url));
  }

  if (pathname.startsWith("/library") || pathname.startsWith("/study/")) {
    const token = req.cookies.get(STUDENT_COOKIE)?.value;
    if (!token) {
      const login = new URL("/login", req.url);
      login.searchParams.set("next", pathname);
      return NextResponse.redirect(login);
    }
  }

  if (
    pathname.startsWith("/admin") &&
    !pathname.startsWith("/admin/login") &&
    !pathname.startsWith("/api/admin/auth")
  ) {
    const token = req.cookies.get(ADMIN_COOKIE)?.value;
    if (!token) {
      return NextResponse.redirect(new URL("/admin/login", req.url));
    }
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/library/:path*", "/study/:path*", "/admin/:path*", "/app.html"],
};
