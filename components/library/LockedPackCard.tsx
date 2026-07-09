const ORDINAL = (n: number) =>
  n === 1 ? "st" : n === 2 ? "nd" : n === 3 ? "rd" : "th";

function formatPrice(paise: number) {
  return `₹${Math.round(paise / 100)}`;
}

export function LockedPackCard({
  title,
  paperCode,
  course,
  studyYear,
  priceInrPaise,
  contactUrl,
}: {
  title: string;
  paperCode?: string | null;
  course: string;
  studyYear: number;
  priceInrPaise: number;
  contactUrl?: string;
}) {
  const href =
    contactUrl ||
    process.env.NEXT_PUBLIC_WHATSAPP_URL ||
    "https://wa.me/";

  return (
    <article className="sb-card sb-card-locked">
      {/* Tag floats on top */}
      <div className="sb-card-tag-float">
        <span className="sb-tag sb-tag-locked">Locked</span>
      </div>

      {/* Gradient visual with light overlay */}
      <div 
        className="sb-card-visual"
        style={{
          background: "linear-gradient(135deg, #fef3c7 0%, #fde68a 100%)",
        }}
      >
        <div className="sb-card-overlay-light" />
        <div className="sb-card-content-overlay">
          <h3 className="sb-card-title">{title}</h3>
          <p className="sb-card-meta">
            {paperCode ? `Q.P. ${paperCode} · ` : ""}
            {course} · {studyYear}
            {ORDINAL(studyYear)} Year
          </p>
        </div>
      </div>

      {/* Compact footer */}
      <div className="sb-card-text-compact" style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
        <span className="sb-card-price">{formatPrice(priceInrPaise)}</span>
        <a
          className="sb-card-enquire"
          href={href}
          target="_blank"
          rel="noreferrer"
        >
          Get access
        </a>
      </div>
    </article>
  );
}
