import Link from "next/link";

export default function HomePage() {
  return (
    <main
      style={{
        maxWidth: 480,
        margin: "0 auto",
        padding: "48px 20px 40px",
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
      }}
    >
      <p
        style={{
          fontSize: 12,
          fontWeight: 700,
          letterSpacing: "0.08em",
          textTransform: "uppercase",
          color: "var(--subtext)",
          marginBottom: 10,
        }}
      >
        GNM · Karnataka · Q.P. 9114
      </p>
      <h1
        style={{
          fontSize: 34,
          fontWeight: 800,
          lineHeight: 1.15,
          color: "var(--primary)",
          marginBottom: 12,
        }}
      >
        CHN Study Pack
      </h1>
      <p style={{ fontSize: 16, color: "var(--subtext)", lineHeight: 1.5, marginBottom: 22 }}>
        Community Health Nursing–I — mark-wise answers, mocks, templates & drills.
        One licence unlocks <strong style={{ color: "var(--text)" }}>one device only</strong>.
      </p>
      <div
        style={{
          display: "inline-flex",
          alignSelf: "flex-start",
          background: "#E8F5E9",
          color: "var(--green)",
          fontWeight: 700,
          fontSize: 13,
          padding: "6px 12px",
          borderRadius: 20,
          marginBottom: 28,
        }}
      >
        ₹200 · 1 phone / browser
      </div>
      <Link
        href="/app.html"
        style={{
          display: "block",
          textAlign: "center",
          background: "var(--primary)",
          color: "#fff",
          fontWeight: 700,
          fontSize: 17,
          padding: "16px 20px",
          borderRadius: 14,
          textDecoration: "none",
          marginBottom: 12,
        }}
      >
        Open study app →
      </Link>
      <Link
        href="/admin"
        style={{
          display: "block",
          textAlign: "center",
          fontSize: 13,
          color: "var(--subtext)",
          padding: "10px",
        }}
      >
        Seller admin
      </Link>
    </main>
  );
}
