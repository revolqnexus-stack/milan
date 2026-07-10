"use client";

import { FormEvent, useState } from "react";

type Props = {
  contentId: number;
  packTitle: string;
  priceRupees: number;
};

export default function AccessRequestForm({ contentId, packTitle, priceRupees }: Props) {
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [college, setCollege] = useState("");
  const [state, setState] = useState<"idle" | "loading" | "done" | "error">("idle");
  const [errMsg, setErrMsg] = useState("");

  async function submit(e: FormEvent) {
    e.preventDefault();
    setState("loading");
    setErrMsg("");

    try {
      const res = await fetch("/api/access", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ contentId, name, phone, college: college || undefined }),
      });
      const data = await res.json();
      if (!data.ok) {
        setErrMsg(data.error || "something went wrong");
        setState("error");
        return;
      }
      setState("done");
    } catch {
      setErrMsg("connection failed. try again.");
      setState("error");
    }
  }

  if (state === "done") {
    return (
      <div className="access-success">
        <p className="access-success-big">done.</p>
        <p className="access-success-sub">we got you.</p>
        <p className="access-success-body">
          we&apos;ll sort the access part. you&apos;ll hear from us.
        </p>
        <p className="access-success-note">
          already got your credentials?{" "}
          <a href="/login" className="access-footer-link">login →</a>
        </p>
      </div>
    );
  }

  return (
    <form className="access-form" onSubmit={submit}>
      <p className="access-form-heading">
        just drop your details. that&apos;s it.
      </p>

      <div className="access-field">
        <label htmlFor="ar-name">your name</label>
        <input
          id="ar-name"
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="what do we call you"
          required
          minLength={2}
          maxLength={120}
          autoComplete="name"
        />
      </div>

      <div className="access-field">
        <label htmlFor="ar-phone">phone number</label>
        <input
          id="ar-phone"
          type="tel"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
          placeholder="we&apos;ll reach you here"
          required
          minLength={7}
          maxLength={30}
          autoComplete="tel"
        />
      </div>

      <div className="access-field">
        <label htmlFor="ar-college">
          college <span className="access-field-optional">(optional)</span>
        </label>
        <input
          id="ar-college"
          type="text"
          value={college}
          onChange={(e) => setCollege(e.target.value)}
          placeholder="where are you studying"
          maxLength={200}
          autoComplete="organization"
        />
      </div>

      {state === "error" && (
        <p className="access-form-error">{errMsg}</p>
      )}

      <button
        type="submit"
        className="access-submit"
        disabled={state === "loading"}
      >
        {state === "loading" ? "sending…" : `GET ACCESS · ₹${priceRupees} →`}
      </button>

      <p className="access-form-note">
        you pay. we give access. you study. hopefully you pass.{" "}
        <span className="access-form-note-em">beautiful system.</span> 😭
      </p>
    </form>
  );
}
