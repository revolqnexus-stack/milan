"use client";

import { FormEvent, useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import {
  createAndStoreDeviceKeyPair,
  deviceLabelGuess,
  signChallenge,
} from "@/lib/device/webcrypto-client";

type UiPhase = "form" | "verifying" | "register" | "unauthorized";

/* ── Device state sub-views ── */
function DeviceVerifying() {
  return (
    <div className="sb-login-body" style={{ justifyContent: "center" }}>
      <div className="sb-device-state">
        <div className="sb-device-ring" aria-hidden />
        <p style={{ fontSize: 11, fontWeight: 700, letterSpacing: "0.1em", textTransform: "uppercase", color: "var(--sb-accent-indigo)", margin: "0 0 8px" }}>
          Device check
        </p>
        <h2 className="sb-device-heading">Checking this device.</h2>
        <p className="sb-device-body">
          Your study access is linked to one authorised browser.
        </p>
      </div>
    </div>
  );
}

function DeviceRegister({ onSecure, busy }: { onSecure: () => void; busy: boolean }) {
  return (
    <div className="sb-login-body" style={{ justifyContent: "center" }}>
      <div className="sb-device-state">
        <p style={{ fontSize: 11, fontWeight: 700, letterSpacing: "0.1em", textTransform: "uppercase", color: "var(--sb-accent-indigo)", margin: "0 0 8px" }}>
          First login
        </p>
        <h2 className="sb-device-heading">Secure this device.</h2>
        <p className="sb-device-body">
          Your first authorised browser becomes the device linked to this student
          account. Other phones cannot access your library.
        </p>
        <div className="sb-device-actions">
          <button
            type="button"
            className="sb-btn sb-btn-primary sb-btn-full"
            onClick={onSecure}
            disabled={busy}
          >
            {busy ? "Securing…" : "Secure this device"}
          </button>
        </div>
        <p className="sb-note">Changing devices later requires an admin reset.</p>
      </div>
    </div>
  );
}

function DeviceUnauthorized() {
  return (
    <div className="sb-login-body" style={{ justifyContent: "center" }}>
      <div className="sb-device-state error">
        <p style={{ fontSize: 11, fontWeight: 700, letterSpacing: "0.1em", textTransform: "uppercase", color: "#b91c1c", margin: "0 0 8px" }}>
          Device
        </p>
        <h2 className="sb-device-heading">Not your registered device.</h2>
        <p className="sb-device-body">
          This account is already linked to another browser. Contact support if
          you&apos;ve switched phones or cleared browser data.
        </p>
        <div className="sb-device-actions">
          <a
            href={process.env.NEXT_PUBLIC_WHATSAPP_URL || "https://wa.me/"}
            target="_blank"
            rel="noreferrer"
            className="sb-btn sb-btn-primary sb-btn-full"
            style={{ textDecoration: "none" }}
          >
            Contact support
          </a>
          <Link
            href="/login"
            className="sb-btn sb-btn-secondary sb-btn-full"
            style={{ textDecoration: "none" }}
          >
            Back to login
          </Link>
        </div>
      </div>
    </div>
  );
}

/* ── Main login page ── */
export default function StudentLoginPage() {
  const router = useRouter();
  const [studentId, setStudentId] = useState("");
  const [password, setPassword] = useState("");
  const [showPass, setShowPass] = useState(false);
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);
  const [phase, setPhase] = useState<UiPhase>("form");
  const [registrationToken, setRegistrationToken] = useState("");

  async function secureDevice() {
    if (!registrationToken) return;
    setBusy(true);
    setError("");
    try {
      const { publicKeySpkiB64, algorithm } = await createAndStoreDeviceKeyPair();
      const reg = await fetch("/api/auth/register-device", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          registrationToken,
          publicKeySpkiB64,
          publicKeyAlgorithm: algorithm,
          deviceLabel: deviceLabelGuess(),
        }),
      });
      const regData = await reg.json();
      if (!regData.ok) {
        setError(regData.error || "Could not secure this device.");
        setPhase("form");
        setBusy(false);
        return;
      }
      router.replace("/library");
    } catch {
      setError("Device security setup failed on this browser.");
      setPhase("form");
      setBusy(false);
    }
  }

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    setError("");
    setBusy(true);
    setPhase("verifying");
    try {
      const res = await fetch("/api/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ studentId, password }),
      });
      const data = await res.json();
      if (!data.ok) {
        setError(data.error || "Login failed");
        setPhase("form");
        setBusy(false);
        return;
      }
      if (data.next === "REGISTER_DEVICE") {
        setRegistrationToken(data.registrationToken);
        setPhase("register");
        setBusy(false);
        return;
      }
      if (data.next === "CHALLENGE") {
        let signatureB64: string;
        try {
          signatureB64 = await signChallenge(data.challenge);
        } catch {
          setPhase("unauthorized");
          setBusy(false);
          return;
        }
        const ver = await fetch("/api/auth/verify-device", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ challengeId: data.challengeId, signatureB64 }),
        });
        const verData = await ver.json();
        if (!verData.ok) {
          setPhase("unauthorized");
          setBusy(false);
          return;
        }
        router.replace("/library");
        return;
      }
      setError("Unexpected login response");
      setPhase("form");
    } catch {
      setError("Network error");
      setPhase("form");
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="sb-page sb-login-wrap">
      {/* Top bar */}
      <header className="sb-topbar">
        <Link href="/" className="sb-brand">
          REVOLQ<span>NEXUS</span>
        </Link>
      </header>

      {/* Phase views */}
      {phase === "verifying" && <DeviceVerifying />}
      {phase === "register" && (
        <DeviceRegister onSecure={secureDevice} busy={busy} />
      )}
      {phase === "unauthorized" && <DeviceUnauthorized />}

      {phase === "form" && (
        <div className="sb-login-body">
          <div className="sb-login-grid sb-fade-up">
            {/* Copy side */}
            <section>
              <h1 className="sb-login-copy-heading">
                {"Your study stuff\nis here."}
              </h1>
              <p className="sb-login-copy-body">
                Your purchased exam packs, predictions, revision systems and mock
                papers — in one private library. Log in and get back to it.
              </p>
              <div className="sb-login-trust">
                <span className="sb-tag sb-tag-sky">Device-bound access</span>
                <span className="sb-tag sb-tag-mint">Private library</span>
                <span className="sb-tag sb-tag-lilac">Progress on your device</span>
              </div>
            </section>

            {/* Form panel */}
            <div className="sb-login-form-panel">
              <p className="sb-login-form-eyebrow">Welcome back</p>
              <h2 className="sb-login-form-heading">Log in</h2>
              <p className="sb-login-form-sub">
                Use the Student ID and password sent on WhatsApp.
              </p>

              <form onSubmit={onSubmit}>
                <div className="sb-field">
                  <label htmlFor="studentId">Student ID</label>
                  <input
                    id="studentId"
                    value={studentId}
                    onChange={(e) => setStudentId(e.target.value.toUpperCase())}
                    placeholder="STU10483"
                    autoComplete="username"
                    required
                  />
                </div>

                <div className="sb-field">
                  <label htmlFor="password">Password</label>
                  <div className="sb-pw-wrap">
                    <input
                      id="password"
                      type={showPass ? "text" : "password"}
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                      placeholder="••••••••"
                      autoComplete="current-password"
                      required
                    />
                    <button
                      type="button"
                      className="sb-pw-toggle"
                      onClick={() => setShowPass((v) => !v)}
                      aria-label={showPass ? "Hide password" : "Show password"}
                    >
                      {showPass ? "Hide" : "Show"}
                    </button>
                  </div>
                </div>

                <button
                  type="submit"
                  className="sb-btn sb-btn-primary sb-btn-full"
                  disabled={busy}
                >
                  {busy ? "Please wait…" : "Log in to my library"}
                </button>
              </form>

              {error && <p className="sb-error">{error}</p>}

              <p className="sb-note">
                First login binds this browser. Other phones cannot open your
                account.
              </p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
