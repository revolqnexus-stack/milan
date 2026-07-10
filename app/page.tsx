"use client";

import { useEffect, useRef, useState } from "react";
import Link from "next/link";
import { motion, useReducedMotion, useInView } from "framer-motion";
import "@/app/styles/landing-funnel.css";

/* ─── helpers ──────────────────────────────────────────────── */
function useMediaQuery(q: string) {
  const [m, setM] = useState(false);
  useEffect(() => {
    const mq = window.matchMedia(q);
    setM(mq.matches);
    const h = (e: MediaQueryListEvent) => setM(e.matches);
    mq.addEventListener("change", h);
    return () => mq.removeEventListener("change", h);
  }, [q]);
  return m;
}

import type { Variants } from "framer-motion";

/* ─── framer variants ──────────────────────────────────────── */
const stamp: Variants = {
  hidden: { scale: 0.65, opacity: 0 },
  show:   { scale: 1, opacity: 1, transition: { type: "spring", stiffness: 700, damping: 22 } },
};
const slideLeft: Variants = {
  hidden: { x: -60, opacity: 0 },
  show:   { x: 0, opacity: 1, transition: { type: "spring", stiffness: 380, damping: 28 } },
};
const fadeUp: Variants = {
  hidden: { y: 18, opacity: 0 },
  show:   { y: 0, opacity: 1, transition: { duration: 0.42, ease: "easeOut" } },
};
const noteIn: Variants = {
  hidden: { rotate: -4, scale: 0.82, opacity: 0 },
  show:   { rotate: 0, scale: 1, opacity: 1,
            transition: { type: "spring", stiffness: 400, damping: 20, delay: 0.2 } },
};
const ctaBounce: Variants = {
  hidden: { scale: 0.94, opacity: 0 },
  show:   { scale: 1, opacity: 1, transition: { type: "spring", stiffness: 500, damping: 22 } },
};
const frag = (deg: number, delay: number): Variants => ({
  hidden: { rotate: deg * 2, y: -20, opacity: 0, scale: 0.88 },
  show:   { rotate: deg, y: 0, opacity: 1, scale: 1,
            transition: { type: "spring", stiffness: 360, damping: 20, delay } },
});

/* ─── InView wrapper for scroll-triggered entrance ────────── */
function InView({
  children, delay = 0, variants = fadeUp, className,
}: {
  children: React.ReactNode;
  delay?: number;
  variants?: Variants;
  className?: string;
}) {
  const ref = useRef<HTMLDivElement>(null);
  const inView = useInView(ref, { once: true, margin: "-60px" });
  const reduced = useReducedMotion();
  return (
    <motion.div
      ref={ref}
      className={className}
      variants={reduced ? undefined : variants}
      initial="hidden"
      animate={inView ? "show" : "hidden"}
      transition={delay ? { delay } : undefined}
    >
      {children}
    </motion.div>
  );
}

/* ─── main component ───────────────────────────────────────── */
export default function HomePage() {
  const reduced = useReducedMotion();

  return (
    <div className="lf-page">

      {/* ════ NAV ════ */}
      <nav className="lf-nav" aria-label="Main navigation">
        <span className="lf-nav-brand">REVOLQNEXUS</span>
        <Link href="/login" className="lf-already-paid">i already paid 🙄</Link>
      </nav>

      {/* ════ HERO ════ */}
      <section className="lf-scene lf-hero">
        <div className="lf-hero-inner">

          {/* Copy column */}
          <div className="lf-hero-copy">
            <motion.h1
              className="lf-hero-headline"
              variants={reduced ? undefined : stamp}
              initial="hidden" animate="show"
            >
              <span className="lf-headline-em">Pass</span>{" "}the paper.{" "}
              <br className="lf-hero-br" />
              Study what{" "}
              <span className="lf-headline-em">repeats.</span>
            </motion.h1>

            <motion.p
              className="lf-hero-sub lf-dm"
              variants={reduced ? undefined : fadeUp}
              initial="hidden" animate="show"
              transition={{ delay: 0.3 }}
            >
              We analyse previous-year nursing question papers, find recurring
              exam patterns and turn them into mark-scoring study packs.
            </motion.p>

            <motion.div
              className="lf-hero-actions"
              variants={reduced ? undefined : fadeUp}
              initial="hidden" animate="show"
              transition={{ delay: 0.48 }}
            >
              <motion.a
                href="#packs"
                className="lf-btn-primary"
                whileHover={reduced ? undefined : { rotate: -1, scale: 1.03 }}
                whileTap={reduced ? undefined : { scale: 0.93 }}
              >
                SEE STUDY PACKS →
              </motion.a>
              <motion.a
                href="#what-you-get"
                className="lf-btn-ghost lf-dm"
                whileHover={reduced ? undefined : { scale: 1.02 }}
                whileTap={reduced ? undefined : { scale: 0.96 }}
              >
                HOW IT WORKS
              </motion.a>
            </motion.div>
          </div>

          {/* GIF 1 — study frustration */}
          <motion.div
            className="lf-hero-media"
            variants={reduced ? undefined : { hidden: { rotate: -4, scale: 0.9, opacity: 0 }, show: { rotate: -2.5, scale: 1, opacity: 1, transition: { type: "spring", stiffness: 280, damping: 22, delay: 0.18 } } }}
            initial="hidden" animate="show"
          >
            <div className="lf-meme-frame lf-meme-frame-tilt">
              <img
                src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeDMzZHlpdHA0Nm5tYmxqaGNnZDNsZHAwNHU3emw2YTZnczdrZXQ4dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/O5YkfFsYBRIbJMSxwr/giphy.gif"
                alt="student staring at books not working"
                width={340} height={300}
                fetchPriority="high"
              />
              <span className="lf-annotation lf-ann-hero">studying everything is crazy btw</span>
              <svg className="lf-ann-arrow lf-ann-arrow-hero" viewBox="0 0 70 50" aria-hidden="true">
                <path d="M 60 8 C 50 5, 30 12, 18 28 C 10 38, 12 44, 16 46" stroke="currentColor" strokeWidth="2.5" fill="none" strokeLinecap="round"/>
                <path d="M 10 43 L 16 46 L 14 39" stroke="currentColor" strokeWidth="2.5" fill="none" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
            </div>
          </motion.div>
        </div>
      </section>

      {/* ════ SECTION 2 — WHAT YOU GET ════ */}
      <section className="lf-scene lf-what" id="what-you-get">
        <div className="lf-section-inner">

          <InView className="lf-section-header">
            <h2 className="lf-section-heading">This is what you get.</h2>
            <p className="lf-section-sub lf-dm">
              Not notes dumped into a PDF. A study system built around how the paper is actually asked.
            </p>
          </InView>

          <div className="lf-features-grid">
            {[
              { n: "01", title: "PREVIOUS PAPER ANALYSIS",  body: "We go through years of question papers and group repeated questions by topic.", meta: "2011–2025 analysed", deg: -1.5, delay: 0 },
              { n: "02", title: "HIGH-YIELD PRIORITY",       body: "Topics ranked by repetition, recent appearances and the marks they're usually asked for.", meta: "MUST · HIGH · MEDIUM", deg: 1, delay: 0.07 },
              { n: "03", title: "MARK-SCORING ANSWERS",      body: "Answers structured around the marks actually asked.", meta: "1 mark · 4 marks · 7–9 marks", deg: -0.8, delay: 0.14 },
              { n: "04", title: "RAPID REVISION",            body: "Definitions, fill-in-the-blanks, true/false traps and rapid drills.", meta: "195 drills", deg: 1.5, delay: 0.21 },
              { n: "05", title: "MOCK PAPERS",               body: "Predicted papers built from recurring examiner patterns.", meta: "3 full mocks", deg: -1, delay: 0.28 },
            ].map((f) => (
              <FeatureCard key={f.n} {...f} />
            ))}
          </div>

          {/* GIF 2 — shocked cat */}
          <div className="lf-what-gif-row">
            <InView>
              <div className="lf-meme-frame lf-meme-frame-tight">
                <img
                  src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGw2Z2R4aW02ZnF4ZmJpeGRzdnZsOXRhZGUwcHBtZWJlZDgwdDY0bSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oFvXciCA8px11faKJS/giphy.gif"
                  alt="shocked reaction"
                  width={260} height={240}
                  loading="lazy"
                />
              </div>
            </InView>
            <motion.span
              className="lf-annotation lf-ann-what"
              variants={reduced ? undefined : noteIn}
              initial="hidden"
              whileInView="show"
              viewport={{ once: true, margin: "-40px" }}
            >
              yeah. we actually read the papers.
            </motion.span>
          </div>
        </div>
      </section>

      {/* ════ SECTION 3 — REAL PRODUCT PREVIEW ════ */}
      <section className="lf-scene lf-product" id="product">
        <div className="lf-section-inner">

          <InView className="lf-section-header">
            <h2 className="lf-section-heading">Not another PDF.</h2>
            <p className="lf-section-sub lf-dm">A system built around the paper.</p>
          </InView>

          <div className="lf-previews-grid">

            {/* Preview 1 — Priority score */}
            <InView variants={frag(-1.5, 0)} className="lf-preview-wrap">
              <div className="lf-preview-card lf-preview-priority">
                <span className="lf-preview-label lf-dm">PRIORITY SCORE</span>
                <div className="lf-priority-score">96<span className="lf-priority-pct">%</span></div>
                <p className="lf-preview-title">Community Health Nursing</p>
                <div className="lf-preview-meta-row lf-dm">
                  <span className="lf-meta-chip lf-meta-chip-red">MUST</span>
                  <span className="lf-preview-meta-text">Asked in 12 supplied papers</span>
                </div>
                <p className="lf-preview-expected lf-dm">Expected: 7–9 marks</p>
              </div>
            </InView>

            {/* Preview 2 — Answer structure */}
            <InView variants={frag(1, 0.08)} className="lf-preview-wrap">
              <div className="lf-preview-card lf-preview-answer">
                <span className="lf-preview-label lf-dm">INSIDE EVERY TOPIC</span>
                {[
                  { icon: "◈", text: "WHY EXAMINERS ASK THIS" },
                  { icon: "✎", text: "WHAT YOU MUST WRITE" },
                  { icon: "⚠", text: "COMMON MARK KILLERS" },
                  { icon: "⚡", text: "2-MINUTE REVISION" },
                  { icon: "✓", text: "FULL EXAM ANSWER" },
                ].map((r) => (
                  <div className="lf-answer-row lf-dm" key={r.text}>
                    <span className="lf-answer-icon">{r.icon}</span>
                    <span className="lf-answer-text">{r.text}</span>
                  </div>
                ))}
              </div>
            </InView>

            {/* Preview 3 — Mock paper */}
            <InView variants={frag(-0.8, 0.16)} className="lf-preview-wrap">
              <div className="lf-preview-card lf-preview-mock">
                <span className="lf-preview-label lf-dm">INCLUDED</span>
                <p className="lf-mock-title">MOCK PAPER 01</p>
                <p className="lf-mock-marks lf-dm">75 MARKS</p>
                <div className="lf-mock-parts lf-dm">
                  <span className="lf-mock-part">QUESTIONS</span>
                  <span className="lf-mock-divider">+</span>
                  <span className="lf-mock-part">MODEL ANSWERS</span>
                </div>
                <p className="lf-mock-count lf-dm">3 predicted papers total</p>
              </div>
            </InView>

          </div>

          {/* GIF 3 — you came to the right place */}
          <div className="lf-product-gif-row">
            <InView>
              <div className="lf-meme-frame lf-meme-frame-center">
                <img
                  src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXJibGhjcmduNGp0YjVndXUzZmh0c2NrbjYybm9uaTl3M3hrb2p1biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oxHQG9Ks6OtIIMX8A/giphy.gif"
                  alt="You came to the right place"
                  width={280} height={210}
                  loading="lazy"
                />
              </div>
            </InView>
            <motion.span
              className="lf-annotation lf-ann-product"
              variants={reduced ? undefined : noteIn}
              initial="hidden"
              whileInView="show"
              viewport={{ once: true, margin: "-40px" }}
            >
              yeah. pretty much. 😭
            </motion.span>
          </div>
        </div>
      </section>

      {/* ════ SECTION 4 — COMPARISON ════ */}
      <section className="lf-scene lf-compare" id="compare">
        <div className="lf-section-inner">

          <InView className="lf-section-header">
            <h2 className="lf-section-heading">You could keep doing this.</h2>
          </InView>

          <div className="lf-compare-grid">

            {/* Old way */}
            <InView variants={frag(-1.5, 0)} className="lf-compare-side lf-compare-old">
              <div className="lf-compare-card lf-compare-card-messy">
                <p className="lf-compare-label lf-dm">THE OLD WAY</p>
                {[
                  "700-page textbook",
                  "random YouTube lectures",
                  "WhatsApp PDFs",
                  '"important questions 100% sure bro"',
                  "trying to read everything",
                ].map((item) => (
                  <div className="lf-compare-item lf-compare-item-old lf-dm" key={item}>
                    <span className="lf-compare-x">✕</span>
                    <span>{item}</span>
                  </div>
                ))}
              </div>
            </InView>

            {/* Divider label — purely textual, arrow is overlay */}
            <div className="lf-compare-or" aria-hidden="true">
              <p className="lf-or-text">or</p>
            </div>

            {/* New way */}
            <InView variants={frag(1, 0.1)} className="lf-compare-side lf-compare-new">
              <div className="lf-compare-card lf-compare-card-clean">
                <p className="lf-compare-label lf-dm">STUDY AROUND THE PAPER</p>
                {[
                  "past-paper evidence",
                  "topic priority",
                  "marks-specific answers",
                  "rapid revision",
                  "predicted mock papers",
                ].map((item) => (
                  <div className="lf-compare-item lf-compare-item-new lf-dm" key={item}>
                    <span className="lf-compare-check">✓</span>
                    <span>{item}</span>
                  </div>
                ))}
              </div>
            </InView>

            {/* Bridge arrow — spans full grid width as absolute overlay */}
            <CompareArrow />

          </div>

          <InView>
            <span className="lf-annotation lf-ann-compare">one of these sounds less painful</span>
          </InView>

        </div>
      </section>

      {/* ════ SECTION 5 — CTA ════ */}
      <section className="lf-scene lf-cta-section" id="packs">
        {/* Arrow is position:absolute, spans the entire section */}
        <div className="lf-s4-arrow-zone" aria-hidden="true">
          <CtaArrow />
        </div>

        <div className="lf-cta-inner">

          {/* GIF 4 — come here */}
          <div className="lf-cta-gif-col">
            <InView>
              <div className="lf-meme-frame lf-meme-frame-asym">
                <img
                  src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHhwMTNiNGFpZWtoemJ3bDM3bXB4NjZ1czc2cmd2dW03ZGs0amZ3dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/t6Q2oJ8BWcvyE/giphy.gif"
                  alt="beckoning come here gesture"
                  width={260} height={260}
                  loading="lazy"
                />
              </div>
            </InView>

            <motion.h2
              className="lf-come-here"
              variants={reduced ? undefined : { hidden: { letterSpacing: "0.12em", opacity: 0 }, show: { letterSpacing: "-0.04em", opacity: 1, transition: { duration: 0.55, ease: [0.2, 1, 0.4, 1] } } }}
              initial="hidden"
              whileInView="show"
              viewport={{ once: true, margin: "-60px" }}
            >
              Come<br />here.
            </motion.h2>
          </div>

          {/* Pack card */}
          <InView variants={ctaBounce} className="lf-pack-card-wrap">
            <div className="lf-pack-card">
              <div className="lf-pack-card-top lf-dm">
                <span className="lf-pack-course">GNM · 1st Year · Q.P. 9114</span>
              </div>
              <h3 className="lf-pack-title">Community Health Nursing I</h3>

              <ul className="lf-pack-features lf-dm">
                {[
                  "Previous-paper analysis",
                  "24 high-yield topics",
                  "Mark-scoring answers",
                  "195 rapid drills",
                  "3 full mock papers",
                  "Private device-bound access",
                ].map((f) => (
                  <li key={f} className="lf-pack-feature">
                    <span className="lf-pack-check">✓</span> {f}
                  </li>
                ))}
              </ul>

              <div className="lf-pack-pricing">
                <span className="lf-pack-price">₹299</span>
                <span className="lf-annotation lf-ann-price">less than the food you order while &quot;studying&quot;</span>
              </div>

              <motion.div
                whileHover={reduced ? undefined : { scale: 1.03, rotate: -0.5 }}
                whileTap={reduced ? undefined : { scale: 0.96 }}
              >
                <Link href="/access" className="lf-btn-get-access">
                  GET ACCESS →
                </Link>
              </motion.div>

              <p className="lf-pack-tagline lf-dm">Pay once. Get access to this study pack.</p>
            </div>
          </InView>
        </div>
      </section>

      <footer className="lf-footer">
        <span className="lf-dm">REVOLQNEXUS · private study board</span>
        <Link href="/admin/login" className="lf-footer-link lf-dm">admin</Link>
      </footer>
    </div>
  );
}

/* ─── Feature card ──────────────────────────────────────────── */
function FeatureCard({
  n, title, body, meta, deg, delay,
}: {
  n: string; title: string; body: string; meta: string; deg: number; delay: number;
}) {
  const reduced = useReducedMotion();
  return (
    <motion.div
      className="lf-feature-card"
      variants={reduced ? undefined : frag(deg, delay)}
      initial="hidden"
      whileInView="show"
      viewport={{ once: true, margin: "-40px" }}
    >
      <span className="lf-feature-num lf-dm">{n}</span>
      <h3 className="lf-feature-title">{title}</h3>
      <p className="lf-feature-body lf-dm">{body}</p>
      <span className="lf-feature-meta lf-dm">{meta}</span>
    </motion.div>
  );
}

/* ─── Comparison bridge arrow — overlays the full grid ──────── */
function CompareArrow() {
  const isDesktop = useMediaQuery("(min-width: 760px)");

  if (isDesktop) {
    /*
     * Position: absolute, spanning the full compare-grid width.
     * Visually bridges old-way card (left) → new-way card (right).
     * viewBox 0 0 800 120. Path: starts mid-left, curves right-downward.
     */
    return (
      <svg
        className="lf-compare-arrow lf-compare-arrow-desktop"
        viewBox="0 0 800 120"
        preserveAspectRatio="none"
        aria-hidden="true"
      >
        <path
          stroke="currentColor" strokeWidth="2.5" fill="none"
          strokeLinecap="round" strokeDasharray="6 5" opacity="0.35"
          d="M 120 30 C 200 10, 300 80, 400 55 C 500 30, 600 90, 680 70 C 730 55, 760 75, 775 95"
        />
        <path
          className="lf-compare-bridge"
          d="M 120 30 C 200 10, 300 80, 400 55 C 500 30, 600 90, 680 70 C 730 55, 760 75, 775 95"
        />
        <path
          stroke="currentColor" strokeWidth="2.5" fill="none" strokeLinecap="round"
          d="M 760 88 L 775 95 L 763 106"
        />
      </svg>
    );
  }

  /* Mobile: vertical arrow between stacked cards */
  return (
    <svg
      className="lf-compare-arrow lf-compare-arrow-mobile"
      viewBox="0 0 120 80"
      aria-hidden="true"
    >
      <path
        className="lf-compare-bridge"
        d="M 60 8 C 80 20, 30 35, 55 52 C 72 64, 65 72, 60 76"
      />
      <path
        stroke="currentColor" strokeWidth="2.5" fill="none" strokeLinecap="round"
        d="M 50 70 L 60 76 L 54 84"
      />
    </svg>
  );
}

/* ─── CTA arrow — full-width overlay spanning GIF → GET ACCESS ── */
function CtaArrow() {
  const isDesktop = useMediaQuery("(min-width: 860px)");

  if (isDesktop) {
    /*
     * Desktop layout: two columns, GIF left, pack card right.
     * Arrow starts top-left (near GIF/Come Here), sweeps right and down,
     * loops back, and terminates bottom-right (near GET ACCESS button).
     * viewBox 0 0 1000 320 — matches the physical content width well.
     * SVG is position:absolute, pointer-events:none, overflow:visible.
     */
    return (
      <svg
        className="lf-epic-arrow lf-epic-arrow-desktop"
        viewBox="0 0 1000 320"
        preserveAspectRatio="none"
        aria-hidden="true"
      >
        {/* ghost — thick, very faint, gives hand-drawn ink texture */}
        <path
          className="lf-arrow-ghost"
          d="M 60 40
             C 160 10, 280 90, 380 60
             C 480 32, 520 130, 600 110
             C 670 92, 680 170, 620 210
             C 560 250, 680 255, 780 230
             C 860 210, 920 185, 960 210
             C 975 220, 982 238, 980 255"
        />
        {/* main visible stroke */}
        <path
          className="lf-arrow-main"
          d="M 60 40
             C 160 10, 280 90, 380 60
             C 480 32, 520 130, 600 110
             C 670 92, 680 170, 620 210
             C 560 250, 680 255, 780 230
             C 860 210, 920 185, 960 210
             C 975 220, 982 238, 980 255"
        />
        {/* arrowhead */}
        <path
          className="lf-arrowhead-stroke"
          d="M 964 244 L 980 255 L 968 266"
        />
        {/* annotation — sits mid-arc */}
        <text className="lf-arrow-note" x="500" y="104">yeah, this bit</text>
      </svg>
    );
  }

  /*
   * Mobile layout: stacked vertically. GIF/Come Here top, pack card bottom.
   * Arrow uses FULL content width (viewBox 0 0 360 260).
   * Starts top-right of content, snakes left-right across full width,
   * terminates at bottom-center near GET ACCESS.
   */
  return (
    <svg
      className="lf-epic-arrow lf-epic-arrow-mobile"
      viewBox="0 0 360 260"
      preserveAspectRatio="none"
      aria-hidden="true"
    >
      <path
        className="lf-arrow-ghost"
        d="M 300 20
           C 340 20, 350 60, 310 80
           C 260 105, 80 90, 50 120
           C 20 148, 80 175, 160 175
           C 230 175, 310 165, 330 200
           C 345 225, 310 248, 260 250"
      />
      <path
        className="lf-arrow-main"
        d="M 300 20
           C 340 20, 350 60, 310 80
           C 260 105, 80 90, 50 120
           C 20 148, 80 175, 160 175
           C 230 175, 310 165, 330 200
           C 345 225, 310 248, 260 250"
      />
      <path
        className="lf-arrowhead-stroke"
        d="M 246 240 L 260 250 L 250 262"
      />
      <text className="lf-arrow-note" x="70" y="148">this way genius</text>
    </svg>
  );
}
