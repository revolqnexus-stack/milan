import { GlassPanel } from "@/components/ui/GlassPanel";
import { DisplayHeading } from "@/components/ui/DisplayHeading";
import { PageEyebrow } from "@/components/ui/PageEyebrow";
import { VaultButton } from "@/components/ui/VaultButton";
import Link from "next/link";

type Kind = "verifying" | "register" | "unauthorized";

export function DeviceStatePanel({
  kind,
  onSecure,
  busy,
}: {
  kind: Kind;
  onSecure?: () => void;
  busy?: boolean;
}) {
  if (kind === "verifying") {
    return (
      <GlassPanel variant="portal" className="device-state">
        <div className="device-ring" aria-hidden />
        <PageEyebrow>Device check</PageEyebrow>
        <DisplayHeading size="sm">Checking this device.</DisplayHeading>
        <p className="body-copy muted">
          Your study access is linked to one authorised browser.
        </p>
      </GlassPanel>
    );
  }

  if (kind === "register") {
    return (
      <GlassPanel variant="portal" className="device-state">
        <PageEyebrow>First login</PageEyebrow>
        <DisplayHeading size="sm">Secure this device.</DisplayHeading>
        <p className="body-copy muted">
          Your first authorised browser becomes the device linked to this student
          account.
        </p>
        <div className="device-actions">
          <VaultButton type="button" orb onClick={onSecure} disabled={busy}>
            {busy ? "Securing…" : "Secure this device"}
          </VaultButton>
        </div>
        <p className="vault-note">
          Changing devices later requires an admin reset.
        </p>
      </GlassPanel>
    );
  }

  return (
    <GlassPanel variant="portal" className="device-state error">
      <PageEyebrow>Device</PageEyebrow>
      <DisplayHeading size="sm">This isn&apos;t your registered device.</DisplayHeading>
      <p className="body-copy muted">
        Your account is already linked to another browser. Contact support if
        you&apos;ve changed phones or cleared browser data.
      </p>
      <div className="device-actions">
        <a
          href={process.env.NEXT_PUBLIC_WHATSAPP_URL || "https://wa.me/"}
          target="_blank"
          rel="noreferrer"
          style={{ textDecoration: "none" }}
        >
          <VaultButton type="button" variant="primary">
            Contact support
          </VaultButton>
        </a>
        <Link href="/login" style={{ textDecoration: "none" }}>
          <VaultButton type="button" variant="secondary">
            Back to login
          </VaultButton>
        </Link>
      </div>
    </GlassPanel>
  );
}
