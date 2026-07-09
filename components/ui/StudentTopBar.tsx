import Link from "next/link";
import type { ReactNode } from "react";

export function StudentTopBar({
  right,
}: {
  right?: ReactNode;
}) {
  return (
    <header className="sb-topbar">
      <Link href="/" className="sb-brand">
        REVOLQ<span>NEXUS</span>
      </Link>
      {right && <div className="sb-topbar-right">{right}</div>}
    </header>
  );
}
