import Link from "next/link";
import { GlassPanel } from "@/components/ui/GlassPanel";
import { VaultButton } from "@/components/ui/VaultButton";
import { ThemeToggle } from "@/components/ui/ThemeToggle";
import { PageEyebrow } from "@/components/ui/PageEyebrow";
import { DisplayHeading } from "@/components/ui/DisplayHeading";

function enquiryUrl() {
  const base = process.env.NEXT_PUBLIC_WHATSAPP_URL || "https://wa.me/";
  const message =
    "Hi REVOLQNEXUS, I need study material for: [your course / exam / subject]";
  const joiner = base.includes("?") ? "&" : "?";
  return `${base}${joiner}text=${encodeURIComponent(message)}`;
}

export default function HomePage() {
  const whatsappEnquiry = enquiryUrl();

  return (
    <main className="vault-page">
      <div className="landing-shell">
        <nav className="glass-panel glass-nav landing-nav">
          <Link href="/" className="brand-mark">
            REVOLQ<span>NEXUS</span>
          </Link>
          <div className="landing-nav-links">
            <ThemeToggle />
            <Link href="/login" className="inline-link-btn">
              <VaultButton type="button" variant="ghost">
                Student login
              </VaultButton>
            </Link>
          </div>
        </nav>

        <section className="landing-hero">
          <div className="motion-fade-up">
            <PageEyebrow>Built for the paper</PageEyebrow>
            <DisplayHeading>
              Don&apos;t study the whole book.{"\n"}Study the exam.
            </DisplayHeading>
            <p className="body-copy">
              Previous-paper patterns, mark-scoring answers, mocks and last-minute
              revision systems — for any course or exam. Message us what you need.
            </p>
            <div className="admin-actions" style={{ marginTop: 22 }}>
              <a
                href={whatsappEnquiry}
                target="_blank"
                rel="noreferrer"
                className="inline-link-btn"
              >
                <VaultButton type="button" orb>
                  Send enquiry
                </VaultButton>
              </a>
              <Link href="/login" className="inline-link-btn">
                <VaultButton type="button" variant="secondary">
                  Student login
                </VaultButton>
              </Link>
            </div>
            <div className="proof-strip">
              <span className="proof-chip">Any course · any exam</span>
              <span className="proof-chip">Device-bound private access</span>
              <span className="proof-chip">Built from past papers</span>
            </div>
          </div>

          <div className="preview-stack" aria-hidden>
            <GlassPanel variant="card" featured className="preview-card">
              <p className="pc-eyebrow">Your subject</p>
              <p className="pc-title">Exam-ready packs</p>
              <p className="pc-meta">Past papers · mark patterns · year tags</p>
            </GlassPanel>
            <GlassPanel variant="card" className="preview-card">
              <p className="pc-eyebrow">Quick revision</p>
              <p className="pc-title">195 drills</p>
              <p className="pc-meta">Definitions · blanks · T/F traps</p>
            </GlassPanel>
            <GlassPanel variant="muted" className="preview-card">
              <p className="pc-eyebrow">Mock paper</p>
              <p className="pc-title">75 marks</p>
              <p className="pc-meta">Timed survival structure</p>
            </GlassPanel>
          </div>
        </section>

        <section className="landing-section">
          <PageEyebrow>Built from the paper</PageEyebrow>
          <DisplayHeading size="md" as="h2">
            Exam intelligence, not textbook noise.
          </DisplayHeading>
          <div className="feature-grid" style={{ marginTop: 22 }}>
            <GlassPanel variant="card" className="feature-card">
              <p className="fn">01</p>
              <h3>Previous paper intelligence</h3>
              <p className="body-copy muted">
                Repeated topics, year tags and high-yield question patterns.
              </p>
            </GlassPanel>
            <GlassPanel variant="card" className="feature-card">
              <p className="fn">02</p>
              <h3>Mark-scoring answers</h3>
              <p className="body-copy muted">
                Answers structured around actual 1, 4, 7, 8 and 9 mark formats.
              </p>
            </GlassPanel>
            <GlassPanel variant="card" className="feature-card">
              <p className="fn">03</p>
              <h3>Last-minute revision</h3>
              <p className="body-copy muted">
                Definitions, blanks, true/false traps and rapid drills.
              </p>
            </GlassPanel>
            <GlassPanel variant="card" className="feature-card">
              <p className="fn">04</p>
              <h3>Private access</h3>
              <p className="body-copy muted">
                One student account linked to one authorised device.
              </p>
            </GlassPanel>
          </div>
        </section>

        <section className="landing-section">
          <PageEyebrow>How access works</PageEyebrow>
          <DisplayHeading size="md" as="h2">
            Pay once. Study privately.
          </DisplayHeading>
          <div className="feature-grid" style={{ marginTop: 22 }}>
            <GlassPanel variant="muted" className="feature-card">
              <p className="fn">Step 1</p>
              <h3>Message us on WhatsApp</h3>
              <p className="body-copy muted">
                Tell us your course, exam and subjects — we&apos;ll confirm what we can build.
              </p>
            </GlassPanel>
            <GlassPanel variant="muted" className="feature-card">
              <p className="fn">Step 2</p>
              <h3>Pay via UPI</h3>
              <p className="body-copy muted">Once we confirm your pack, pay and we activate access.</p>
            </GlassPanel>
            <GlassPanel variant="muted" className="feature-card">
              <p className="fn">Step 3</p>
              <h3>Receive Student ID</h3>
              <p className="body-copy muted">Credentials arrive on WhatsApp.</p>
            </GlassPanel>
            <GlassPanel variant="muted" className="feature-card">
              <p className="fn">Step 4</p>
              <h3>Bind &amp; study</h3>
              <p className="body-copy muted">First login binds your device. Your library unlocks.</p>
            </GlassPanel>
          </div>
        </section>

        <GlassPanel variant="portal" className="login-panel" style={{ marginTop: 20 }}>
          <PageEyebrow>Already purchased?</PageEyebrow>
          <DisplayHeading size="sm" as="h2">
            Enter the study vault.
          </DisplayHeading>
          <p className="body-copy muted" style={{ marginBottom: 18 }}>
            Student ID and password only. No email login.
          </p>
          <Link href="/login" style={{ textDecoration: "none" }}>
            <VaultButton type="button" orb>
              Student login
            </VaultButton>
          </Link>
        </GlassPanel>

        <footer className="landing-footer">
          <span>REVOLQNEXUS · Private study vault</span>
          <Link href="/admin/login">Admin</Link>
        </footer>
      </div>
    </main>
  );
}
