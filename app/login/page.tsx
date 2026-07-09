"use client";

import { FormEvent, useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import {
  createAndStoreDeviceKeyPair,
  deviceLabelGuess,
  signChallenge,
} from "@/lib/device/webcrypto-client";
import { GlassPanel } from "@/components/ui/GlassPanel";
import { VaultButton } from "@/components/ui/VaultButton";
import { ThemeToggle } from "@/components/ui/ThemeToggle";
import { PageEyebrow } from "@/components/ui/PageEyebrow";
import { DisplayHeading } from "@/components/ui/DisplayHeading";
import { DeviceStatePanel } from "@/components/auth/DeviceStatePanel";

type UiPhase = "form" | "verifying" | "register" | "unauthorized";

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
          body: JSON.stringify({
            challengeId: data.challengeId,
            signatureB64,
          }),
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
    <main className="vault-page">
      <div className="landing-shell">
        <div className="glass-panel glass-nav lib-nav" style={{ marginBottom: 28 }}>
          <Link href="/" className="brand-mark">
            REVOLQ<span>NEXUS</span>
          </Link>
          <div className="lib-nav-actions">
            <ThemeToggle />
          </div>
        </div>

        {phase === "verifying" && <DeviceStatePanel kind="verifying" />}
        {phase === "register" && (
          <DeviceStatePanel kind="register" onSecure={secureDevice} busy={busy} />
        )}
        {phase === "unauthorized" && <DeviceStatePanel kind="unauthorized" />}

        {phase === "form" && (
          <div className="login-layout motion-fade-up">
            <section className="login-copy">
              <PageEyebrow>Private study access</PageEyebrow>
              <DisplayHeading>
                Everything you need.{"\n"}Nothing you don&apos;t.
              </DisplayHeading>
              <p className="body-copy">
                Your purchased exam packs, predictions, revision systems and mock
                papers — in one private library.
              </p>
              <div className="trust-row">
                <span className="trust-chip">Device-bound access</span>
                <span className="trust-chip">Private study library</span>
                <span className="trust-chip">Progress stays on your device</span>
              </div>
            </section>

            <GlassPanel variant="form" className="login-panel">
              <PageEyebrow>Welcome back</PageEyebrow>
              <DisplayHeading size="sm" as="h2">
                Enter your vault.
              </DisplayHeading>
              <p className="body-copy muted" style={{ marginBottom: 20 }}>
                Use the Student ID and password sent on WhatsApp.
              </p>

              <form onSubmit={onSubmit}>
                <div className="vault-field">
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

                <div className="vault-field">
                  <label htmlFor="password">Password</label>
                  <div className="password-wrap">
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
                      className="password-toggle"
                      onClick={() => setShowPass((v) => !v)}
                      aria-label={showPass ? "Hide password" : "Show password"}
                    >
                      {showPass ? "Hide" : "Show"}
                    </button>
                  </div>
                </div>

                <VaultButton type="submit" orb disabled={busy}>
                  {busy ? "Please wait…" : "Enter study vault"}
                </VaultButton>
              </form>

              {error && <p className="vault-error">{error}</p>}
              <p className="vault-note">
                First login binds this browser. Other phones cannot open your account.
              </p>
            </GlassPanel>
          </div>
        )}
      </div>
    </main>
  );
}
