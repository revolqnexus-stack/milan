import Link from "next/link";

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
    <div className="sb-page">
      {/* Top bar */}
      <header className="sb-topbar">
        <Link href="/" className="sb-brand">
          REVOLQ<span>NEXUS</span>
        </Link>
        <div className="sb-topbar-right">
          <Link
            href="/login"
            className="sb-btn sb-btn-secondary"
            style={{ fontSize: 13, padding: "7px 16px" }}
          >
            Student login
          </Link>
        </div>
      </header>

      <main className="sb-inner sb-landing-body">
        {/* ── Hero ── */}
        <section className="sb-hero sb-fade-up">
          <div>
            <p className="sb-hero-eyebrow">Built for the paper</p>
            <h1 className="sb-hero-heading">
              Scroll less.{" "}
              <mark>Score more.</mark>
            </h1>
            <p className="sb-hero-body">
              Previous-paper packs, mark-scoring answers, mocks and last-minute
              revision systems — for GNM and other nursing exams. Study what
              actually comes.
            </p>
            <div className="sb-hero-actions">
              <a
                href={whatsappEnquiry}
                target="_blank"
                rel="noreferrer"
                className="sb-btn sb-btn-primary"
              >
                Send enquiry →
              </a>
              <Link href="/login" className="sb-btn sb-btn-secondary">
                Student login
              </Link>
            </div>
            <div className="sb-hero-proof">
              <span className="sb-tag sb-tag-sky">Any course · any exam</span>
              <span className="sb-tag sb-tag-mint">Device-bound access</span>
              <span className="sb-tag sb-tag-lilac">Built from past papers</span>
            </div>
          </div>

          {/* Preview card stack */}
          <div className="sb-preview-stack" aria-hidden>
            <div className="sb-preview-card">
              <div style={{ 
                width: "calc(100% + 32px)", 
                height: 60, 
                margin: "-16px -16px 10px",
                background: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
                borderRadius: "18px 18px 0 0",
                display: "flex",
                alignItems: "center",
                justifyContent: "center"
              }}>
                <span style={{ fontSize: "0.65rem", fontWeight: 800, color: "rgba(255,255,255,0.5)", textTransform: "uppercase", letterSpacing: "0.15em" }}>Q.P. 9114</span>
              </div>
              <p className="sb-pc-title">Community Health Nursing I</p>
              <div style={{ display: "flex", gap: 6, flexWrap: "wrap", marginTop: 8 }}>
                <span className="sb-tag sb-tag-mint">Access granted</span>
                <span className="sb-tag sb-tag-peach">High yield</span>
              </div>
            </div>
            <div className="sb-preview-card">
              <div style={{ 
                width: "calc(100% + 32px)", 
                height: 60, 
                margin: "-16px -16px 10px",
                background: "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
                borderRadius: "18px 18px 0 0"
              }} />
              <p className="sb-pc-title">195 rapid drills</p>
              <p className="sb-pc-meta">Definitions · blanks · T/F traps</p>
            </div>
            <div className="sb-preview-card" style={{ background: "linear-gradient(135deg, #fef3c7 0%, #fde68a 100%)", borderColor: "rgba(245, 158, 11, 0.3)" }}>
              <p className="sb-pc-title" style={{ color: "#92400e", marginTop: 8 }}>Exam in 3 days?</p>
              <div style={{ display: "flex", gap: 6, marginTop: 10 }}>
                <span className="sb-tag sb-tag-blush">Last-minute pack</span>
              </div>
            </div>
            <div className="sb-preview-card">
              <div style={{ 
                width: "calc(100% + 32px)", 
                height: 60, 
                margin: "-16px -16px 10px",
                background: "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)",
                borderRadius: "18px 18px 0 0"
              }} />
              <p className="sb-pc-title">96% coverage</p>
              <p className="sb-pc-meta">Most repeated · Priority tracker</p>
            </div>
          </div>
        </section>

        {/* ── Features ── */}
        <section className="sb-section">
          <p className="sb-section-eyebrow">Built from the paper</p>
          <h2 className="sb-section-heading">
            Exam intelligence, not textbook noise.
          </h2>
          <div className="sb-feature-grid">
            <div className="sb-feature-card">
              <p className="sb-feature-num">01</p>
              <h3>Previous paper intelligence</h3>
              <p>Repeated topics, year tags and high-yield question patterns extracted from past papers.</p>
            </div>
            <div className="sb-feature-card">
              <p className="sb-feature-num">02</p>
              <h3>Mark-scoring answers</h3>
              <p>Answers structured around actual 1, 4, 7, 8 and 9 mark formats. No filler.</p>
            </div>
            <div className="sb-feature-card">
              <p className="sb-feature-num">03</p>
              <h3>Last-minute revision</h3>
              <p>Definitions, blanks, true/false traps and rapid drills. Exam-night ready.</p>
            </div>
            <div className="sb-feature-card">
              <p className="sb-feature-num">04</p>
              <h3>Private access</h3>
              <p>One student account linked to one authorised device. Secure and yours.</p>
            </div>
          </div>
        </section>

        {/* ── How it works ── */}
        <section className="sb-section">
          <p className="sb-section-eyebrow">How access works</p>
          <h2 className="sb-section-heading">Pay once. Study privately.</h2>
          <div className="sb-feature-grid">
            <div className="sb-feature-card">
              <p className="sb-feature-num">Step 1</p>
              <h3>Message us on WhatsApp</h3>
              <p>Tell us your course, exam and subjects. We&apos;ll confirm what we can build.</p>
            </div>
            <div className="sb-feature-card">
              <p className="sb-feature-num">Step 2</p>
              <h3>Pay via UPI</h3>
              <p>Once we confirm your pack, pay and we activate access same day.</p>
            </div>
            <div className="sb-feature-card">
              <p className="sb-feature-num">Step 3</p>
              <h3>Receive Student ID</h3>
              <p>Your credentials arrive on WhatsApp. No email needed.</p>
            </div>
            <div className="sb-feature-card">
              <p className="sb-feature-num">Step 4</p>
              <h3>Bind &amp; study</h3>
              <p>First login binds your device. Your study board unlocks instantly.</p>
            </div>
          </div>
        </section>

        {/* ── CTA panel ── */}
        <div className="sb-cta-panel">
          <h2>Already purchased?</h2>
          <p>Your study board is waiting. Log in and get back to it.</p>
          <div style={{ display: "flex", gap: 10, justifyContent: "center", flexWrap: "wrap" }}>
            <Link href="/login" className="sb-btn sb-btn-white">
              Student login →
            </Link>
            <a
              href={whatsappEnquiry}
              target="_blank"
              rel="noreferrer"
              className="sb-btn sb-btn-white-ghost"
            >
              Send enquiry
            </a>
          </div>
        </div>

        {/* ── Footer ── */}
        <footer className="sb-footer">
          <span>REVOLQNEXUS · Private study board</span>
          <Link href="/admin/login">Admin</Link>
        </footer>
      </main>
    </div>
  );
}
