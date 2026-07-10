"use client";

import { useEffect, useRef, useState } from "react";
import Link from "next/link";
import { motion, AnimatePresence, useReducedMotion } from "framer-motion";
import "@/app/styles/landing-funnel.css";

/* ─── helpers ─────────────────────────────────────────────── */
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
const overshoot: Variants = {
  hidden: { x: -80, opacity: 0 },
  show:   { x: 0, opacity: 1, transition: { type: "spring", stiffness: 500, damping: 18 } },
};
const fadeUp: Variants = {
  hidden: { y: 14, opacity: 0 },
  show:   { y: 0, opacity: 1, transition: { duration: 0.38, ease: "easeOut" } },
};
const noteIn: Variants = {
  hidden: { rotate: -4, scale: 0.8, opacity: 0 },
  show:   { rotate: 0, scale: 1, opacity: 1, transition: { type: "spring", stiffness: 400, damping: 20, delay: 0.18 } },
};
const ctaBounce: Variants = {
  hidden: { scale: 0.94, opacity: 0 },
  show:   { scale: 1, opacity: 1, transition: { type: "spring", stiffness: 500, damping: 22, delay: 0.1 } },
};

/* fragment entry — thrown-notes effect */
const frag = (deg: number, delay: number): Variants => ({
  hidden: { rotate: deg * 2, y: -24, opacity: 0, scale: 0.88 },
  show:   { rotate: deg, y: 0, opacity: 1, scale: 1,
            transition: { type: "spring", stiffness: 360, damping: 20, delay } },
});

/* ─── main component ───────────────────────────────────────── */
export default function HomePage() {
  const reduced = useReducedMotion();
  const [scene, setScene]               = useState(1);
  const [nahClicked, setNahClicked]     = useState(false);
  const [nahShook, setNahShook]         = useState(false);
  const [yesFlash, setYesFlash]         = useState(false);
  // s2 staged reveals
  const [showReally, setShowReally]     = useState(false);
  const [showActually, setShowActually] = useState(false);
  const [showYesMf, setShowYesMf]       = useState(false);
  const [showS2Note, setShowS2Note]     = useState(false);
  // s4 arrow
  const [arrowPhase, setArrowPhase]     = useState(0); // 0=hidden 1=drawing 2=done

  const s2Ref = useRef<HTMLElement>(null);
  const s3Ref = useRef<HTMLElement>(null);
  const s4Ref = useRef<HTMLElement>(null);

  function scrollTo(ref: React.RefObject<HTMLElement | null>) {
    setTimeout(() => ref.current?.scrollIntoView({ behavior: reduced ? "auto" : "smooth", block: "start" }), 80);
  }

  function goToScene2() {
    if (reduced) { setScene(2); setShowReally(true); setShowActually(true); setShowYesMf(true); scrollTo(s2Ref); return; }
    setYesFlash(true);
    setTimeout(() => { setYesFlash(false); setScene(2); scrollTo(s2Ref); }, 220);
    setTimeout(() => setShowReally(true), 820);
    setTimeout(() => setShowActually(true), 1540);
    setTimeout(() => setShowYesMf(true), 2200);
    setTimeout(() => setShowS2Note(true), 2500);
  }

  function goToScene3() { setScene(3); scrollTo(s3Ref); }

  function goToScene4() {
    setScene(4); scrollTo(s4Ref);
    if (reduced) { setArrowPhase(2); return; }
    setTimeout(() => setArrowPhase(1), 500);
    setTimeout(() => setArrowPhase(2), 2800);
  }

  function handleNah() {
    setNahShook(true); setNahClicked(true);
    setTimeout(() => setNahShook(false), 500);
  }

  return (
    <div className="lf-page">
      <Link href="/login" className="lf-already-paid">i already paid 🙄</Link>

      {/* ════════════════ SCENE 1 ════════════════ */}
      <section className="lf-scene lf-s1">
        <div className="lf-s1-inner">

          {/* GIF — slightly rotated frame, annotated */}
          <div className="lf-s1-media-col">
            <div className="lf-meme-frame lf-meme-frame-tilt">
              <img
                src="/media/study-culture/scene1-study-stress.gif"
                alt="stressed student staring at books"
                width={340} height={300}
                fetchPriority="high"
              />
              {/* annotation */}
              <span className="lf-annotation lf-ann-s1">studying btw</span>
              {/* wonky arrow pointing at gif */}
              <svg className="lf-ann-arrow lf-ann-arrow-s1" viewBox="0 0 70 50" aria-hidden="true">
                <path d="M 60 8 C 50 5, 30 12, 18 28 C 10 38, 12 44, 16 46" stroke="currentColor" strokeWidth="2.5" fill="none" strokeLinecap="round"/>
                <path d="M 10 43 L 16 46 L 14 39" stroke="currentColor" strokeWidth="2.5" fill="none" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
            </div>
          </div>

          {/* Copy column */}
          <div className="lf-s1-copy">
            <motion.h1
              className="lf-bruh"
              variants={reduced ? undefined : stamp}
              initial="hidden" animate="show"
            >
              bruh.
            </motion.h1>

            <motion.div
              className="lf-question-wrap"
              variants={reduced ? undefined : fadeUp}
              initial="hidden" animate="show"
              transition={{ delay: 0.25 }}
            >
              <p className="lf-question-line lf-dm">do you actually wanna</p>
              <p className="lf-question-line">
                <span className="lf-dm">pass</span>
                <motion.span
                  className="lf-pass-slam"
                  variants={reduced ? undefined : stamp}
                  initial="hidden" animate="show"
                  transition={{ delay: 0.55 }}
                >
                  PASS?
                </motion.span>
              </p>
              <p className="lf-question-line lf-dm">or are we just opening books for decoration?</p>
            </motion.div>

            <motion.div
              className="lf-actions"
              variants={reduced ? undefined : fadeUp}
              initial="hidden" animate="show"
              transition={{ delay: 0.7 }}
            >
              <motion.button
                className={`lf-btn-yes${yesFlash ? " lf-btn-flash" : ""}`}
                onClick={goToScene2}
                whileHover={reduced ? undefined : { rotate: -1, scale: 1.03 }}
                whileTap={reduced ? undefined : { scale: 0.93 }}
              >
                yeah i wanna pass 😭
              </motion.button>

              <motion.button
                className={`lf-btn-nah${nahShook ? " shook" : ""}`}
                onClick={handleNah}
                initial="rest"
                whileHover={reduced ? undefined : "hover"}
                variants={reduced ? undefined : {
                  rest:  { x: 0 },
                  hover: { x: nahClicked ? 0 : 10, rotate: 1.5, transition: { type: "spring", stiffness: 500 } },
                }}
              >
                nah i&apos;m cooked
              </motion.button>

              <AnimatePresence>
                {nahClicked && (
                  <motion.div
                    className="lf-nah-response-wrap"
                    initial={{ opacity: 0, y: 6 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0 }}
                  >
                    <span className="lf-dm lf-nah-response">valid.&nbsp; but click the other one. 😭</span>
                    {/* tiny arrow pointing back at yes button */}
                    <svg className="lf-nah-arrow" viewBox="0 0 60 28" aria-hidden="true">
                      <path d="M 56 24 C 40 26, 20 20, 8 8" stroke="currentColor" strokeWidth="2.5" fill="none" strokeLinecap="round"/>
                      <path d="M 4 12 L 8 8 L 14 12" stroke="currentColor" strokeWidth="2.5" fill="none" strokeLinecap="round" strokeLinejoin="round"/>
                    </svg>
                  </motion.div>
                )}
              </AnimatePresence>
            </motion.div>
          </div>
        </div>

        {/* scene connector squiggle */}
        <div className="lf-connector" aria-hidden="true">
          <svg viewBox="0 0 40 80" className="lf-connector-squiggle">
            <path d="M 20 0 C 30 15, 10 25, 20 40 C 30 55, 10 65, 20 80" stroke="currentColor" strokeWidth="2" fill="none" strokeLinecap="round"/>
          </svg>
          <span className="lf-annotation lf-connector-note">bro actually clicked yes</span>
        </div>
      </section>

      {/* ════════════════ SCENE 2 ════════════════ */}
      <section
        ref={s2Ref}
        className={`lf-scene lf-s2${scene < 2 ? " lf-scene-hidden" : ""}`}
        aria-hidden={scene < 2}
      >
        <div className="lf-s2-inner">
          <div className="lf-big-text">
            <AnimatePresence>
              {showReally && (
                <motion.h2
                  className="lf-really"
                  variants={reduced ? undefined : overshoot}
                  initial="hidden" animate="show"
                >
                  really<br />bruh?
                </motion.h2>
              )}
            </AnimatePresence>

            <AnimatePresence>
              {showActually && (
                <motion.p
                  className="lf-like-actually lf-dm"
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0, transition: { duration: 0.45, ease: [0.2, 1, 0.4, 1] } }}
                >
                  like actually?
                </motion.p>
              )}
            </AnimatePresence>

            <AnimatePresence>
              {showYesMf && (
                <motion.div
                  className="lf-s2-actions"
                  variants={reduced ? undefined : ctaBounce}
                  initial="hidden" animate="show"
                >
                  {/* burst doodle behind YES MF */}
                  <div className="lf-yes-wrap">
                    <YesBurst />
                    <motion.button
                      className="lf-btn-big"
                      onClick={goToScene3}
                      whileHover={reduced ? undefined : { rotate: 1, scale: 1.04 }}
                      whileTap={reduced ? undefined : { scale: 0.91 }}
                    >
                      YES MF
                    </motion.button>
                  </div>
                </motion.div>
              )}
            </AnimatePresence>

            <AnimatePresence>
              {showS2Note && (
                <motion.span
                  className="lf-annotation lf-ann-s2"
                  variants={reduced ? undefined : noteIn}
                  initial="hidden" animate="show"
                >
                  bro said yes 💀
                </motion.span>
              )}
            </AnimatePresence>
          </div>

          <div className="lf-meme-right">
            <div className="lf-meme-frame lf-meme-frame-tight">
              <img
                src="/media/study-culture/scene2-suspicious.gif"
                alt="suspicious reaction"
                width={300} height={280}
                loading="lazy"
              />
            </div>
          </div>
        </div>

        {/* scene 2→3 connector */}
        <div className="lf-connector lf-connector-center" aria-hidden="true">
          <span className="lf-annotation">. . .</span>
          <span className="lf-annotation lf-connector-anyway">anyway</span>
        </div>
      </section>

      {/* ════════════════ SCENE 3 ════════════════ */}
      <section
        ref={s3Ref}
        className={`lf-scene lf-s3${scene < 3 ? " lf-scene-hidden" : ""}`}
        aria-hidden={scene < 3}
      >
        <div className="lf-s3-inner">
          <div className="lf-meme-frame lf-meme-frame-center">
            <img
              src="/media/study-culture/scene3-celebration.gif"
              alt="celebration welcome"
              className="lf-s3-meme"
              width={220} height={220}
              loading="lazy"
            />
          </div>

          <motion.h2
            className="lf-yo"
            variants={reduced ? undefined : overshoot}
            initial="hidden" animate={scene >= 3 ? "show" : "hidden"}
          >
            yo.
          </motion.h2>

          <motion.p
            className="lf-right-place"
            variants={reduced ? undefined : stamp}
            initial="hidden" animate={scene >= 3 ? "show" : "hidden"}
            transition={{ delay: 0.18 }}
          >
            right place, biatch.
            {/* underline doodle */}
            <svg className="lf-underline-doodle" viewBox="0 0 240 10" aria-hidden="true">
              <path d="M 2 5 C 30 2, 60 8, 100 4 C 140 1, 180 7, 238 5" stroke="currentColor" strokeWidth="3" fill="none" strokeLinecap="round"/>
            </svg>
          </motion.p>

          <motion.p
            className="lf-body-copy lf-dm"
            variants={reduced ? undefined : fadeUp}
            initial="hidden" animate={scene >= 3 ? "show" : "hidden"}
            transition={{ delay: 0.35 }}
          >
            we took{" "}
            <span className="lf-highlight-word">old question papers</span>
            , found what these exam people keep asking,
            and turned the useful shit into study packs.
          </motion.p>

          {/* fragments — thrown notes */}
          <div className="lf-fragments">
            <motion.div
              className="lf-fragment-wrap"
              variants={reduced ? undefined : frag(-2, 0.1)}
              initial="hidden" animate={scene >= 3 ? "show" : "hidden"}
            >
              <span className="lf-fragment lf-fragment-green">24 high-yield topics</span>
            </motion.div>

            <motion.div
              className="lf-fragment-wrap lf-fragment-mid"
              variants={reduced ? undefined : frag(1.5, 0.22)}
              initial="hidden" animate={scene >= 3 ? "show" : "hidden"}
            >
              <span className="lf-fragment lf-fragment-blue">195 rapid drills</span>
              <span className="lf-annotation lf-ann-drills">sorry</span>
            </motion.div>

            <motion.div
              className="lf-fragment-wrap"
              variants={reduced ? undefined : frag(-1, 0.34)}
              initial="hidden" animate={scene >= 3 ? "show" : "hidden"}
            >
              <span className="lf-fragment lf-fragment-orange">3 mocks to humble you</span>
              <span className="lf-annotation lf-ann-mocks">character development</span>
            </motion.div>
          </div>

          <motion.button
            className="lf-btn-yes lf-btn-s3"
            onClick={goToScene4}
            variants={reduced ? undefined : fadeUp}
            initial="hidden" animate={scene >= 3 ? "show" : "hidden"}
            transition={{ delay: 0.55 }}
            whileHover={reduced ? undefined : { rotate: -1, scale: 1.03 }}
            whileTap={reduced ? undefined : { scale: 0.93 }}
          >
            okay i&apos;m in →
          </motion.button>
        </div>
      </section>

      {/* ════════════════ SCENE 4 ════════════════ */}
      <section
        ref={s4Ref}
        className={`lf-scene lf-s4${scene < 4 ? " lf-scene-hidden" : ""}`}
        aria-hidden={scene < 4}
      >
        <div className="lf-s4-inner">
          <div className="lf-s4-left">
            <div className="lf-meme-frame lf-meme-frame-asym">
              <img
                src="/media/study-culture/scene4-come-here.gif"
                alt="beckoning come here gesture"
                width={260} height={260}
                loading="lazy"
              />
            </div>
            <motion.h2
              className="lf-come-here"
              variants={reduced ? undefined : { hidden: { letterSpacing: "0.12em", opacity: 0 }, show: { letterSpacing: "-0.04em", opacity: 1, transition: { duration: 0.6, ease: [0.2, 1, 0.4, 1] } } }}
              initial="hidden" animate={scene >= 4 ? "show" : "hidden"}
            >
              come<br />here.
            </motion.h2>
          </div>

          {/* The unnecessarily long arrow */}
          <div className="lf-s4-arrow-zone" aria-hidden="true">
            <EpicArrow phase={arrowPhase} />
          </div>

          {/* CTA card */}
          <motion.div
            className="lf-cta-card"
            variants={reduced ? undefined : ctaBounce}
            initial="hidden"
            animate={arrowPhase >= 2 ? "show" : "hidden"}
          >
            <p className="lf-boring-money lf-dm">okay here&apos;s the boring money part</p>
            {/* capitalism jumpscare annotation */}
            <span className="lf-annotation lf-ann-capitalism">capitalism jumpscare</span>
            <motion.div
              whileHover={reduced ? undefined : { scale: 1.03, rotate: -0.5 }}
              whileTap={reduced ? undefined : { scale: 0.96 }}
            >
              <Link href="/access" className="lf-cta-btn">
                GET ACCESS →
              </Link>
            </motion.div>
            <p className="lf-cta-tagline lf-dm">
              you pay. we give access. you study.<br />
              hopefully you pass. beautiful system. 😭
            </p>
          </motion.div>
        </div>
      </section>

      <footer className="lf-footer">
        <span className="lf-dm">REVOLQNEXUS · private study board</span>
        <Link href="/admin/login" className="lf-footer-link lf-dm">admin</Link>
      </footer>
    </div>
  );
}

/* ─── YES burst SVG doodle ─────────────────────────────────── */
function YesBurst() {
  return (
    <svg className="lf-yes-burst" viewBox="0 0 120 120" aria-hidden="true">
      {/* 8 hand-drawn burst lines radiating out */}
      <path d="M 60 60 L 60 12" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round"/>
      <path d="M 60 60 L 60 108" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
      <path d="M 60 60 L 12 60" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round"/>
      <path d="M 60 60 L 108 60" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
      <path d="M 60 60 L 26 26" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
      <path d="M 60 60 L 94 26" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round"/>
      <path d="M 60 60 L 94 94" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
      <path d="M 60 60 L 26 94" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round"/>
    </svg>
  );
}

/* ─── The epic unnecessarily long arrow ─────────────────────── */
function EpicArrow({ phase }: { phase: number }) {
  const isDesktop = useMediaQuery("(min-width: 860px)");
  const reduced = useReducedMotion();

  // path lengths (approximate, measured after authoring)
  const DESKTOP_LEN = 820;
  const MOBILE_LEN  = 380;

  const drawing = phase >= 1;
  const done    = phase >= 2;
  const instant = reduced;

  if (isDesktop) {
    return (
      <svg
        className="lf-epic-arrow lf-epic-arrow-desktop"
        viewBox="0 0 700 220"
        xmlns="http://www.w3.org/2000/svg"
        aria-hidden="true"
      >
        {/* ghost stroke for pen-drawn texture */}
        <path
          className="lf-arrow-ghost"
          d="M 30 30 C 80 10, 140 80, 200 65 C 260 50, 290 120, 360 100 C 420 84, 440 140, 380 175 C 330 205, 440 210, 520 190 C 580 175, 620 155, 660 170 C 680 178, 688 190, 686 200"
          strokeDasharray={DESKTOP_LEN}
          strokeDashoffset={instant || drawing ? 0 : DESKTOP_LEN}
          style={instant ? {} : { transition: drawing ? `stroke-dashoffset 2s cubic-bezier(0.32,0,0.2,1)` : "none" }}
        />
        {/* main path */}
        <path
          className="lf-arrow-main"
          d="M 30 30 C 80 10, 140 80, 200 65 C 260 50, 290 120, 360 100 C 420 84, 440 140, 380 175 C 330 205, 440 210, 520 190 C 580 175, 620 155, 660 170 C 680 178, 688 190, 686 200"
          strokeDasharray={DESKTOP_LEN}
          strokeDashoffset={instant || drawing ? 0 : DESKTOP_LEN}
          style={instant ? {} : { transition: drawing ? `stroke-dashoffset 2s cubic-bezier(0.32,0,0.2,1)` : "none" }}
        />
        {/* arrowhead — two hand-drawn strokes */}
        <path
          className="lf-arrowhead-stroke"
          d="M 672 188 L 686 200 L 674 210"
          strokeDasharray={40}
          strokeDashoffset={instant || done ? 0 : 40}
          style={instant ? {} : { transition: done ? "stroke-dashoffset 300ms ease 0.1s" : "none" }}
        />
        {/* midpoint annotation */}
        <text
          className="lf-arrow-note"
          x="355" y="92"
          style={{ opacity: instant || done ? 1 : 0, transition: done ? "opacity 300ms ease 0.2s" : "none" }}
        >
          this way genius
        </text>
      </svg>
    );
  }

  // mobile — vertical drop arrow
  return (
    <svg
      className="lf-epic-arrow lf-epic-arrow-mobile"
      viewBox="0 0 120 200"
      xmlns="http://www.w3.org/2000/svg"
      aria-hidden="true"
    >
      <path
        className="lf-arrow-ghost"
        d="M 60 10 C 80 30, 30 50, 55 80 C 75 105, 35 130, 60 160 C 75 178, 70 188, 62 196"
        strokeDasharray={MOBILE_LEN}
        strokeDashoffset={instant || drawing ? 0 : MOBILE_LEN}
        style={instant ? {} : { transition: drawing ? `stroke-dashoffset 1.4s cubic-bezier(0.32,0,0.2,1)` : "none" }}
      />
      <path
        className="lf-arrow-main"
        d="M 60 10 C 80 30, 30 50, 55 80 C 75 105, 35 130, 60 160 C 75 178, 70 188, 62 196"
        strokeDasharray={MOBILE_LEN}
        strokeDashoffset={instant || drawing ? 0 : MOBILE_LEN}
        style={instant ? {} : { transition: drawing ? `stroke-dashoffset 1.4s cubic-bezier(0.32,0,0.2,1)` : "none" }}
      />
      <path
        className="lf-arrowhead-stroke"
        d="M 50 190 L 62 196 L 56 206"
        strokeDasharray={30}
        strokeDashoffset={instant || done ? 0 : 30}
        style={instant ? {} : { transition: done ? "stroke-dashoffset 300ms ease 0.1s" : "none" }}
      />
      <text
        className="lf-arrow-note"
        x="72" y="108"
        style={{ opacity: instant || done ? 1 : 0, transition: done ? "opacity 300ms ease 0.15s" : "none" }}
      >
        this way genius
      </text>
    </svg>
  );
}
