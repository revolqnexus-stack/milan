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
      {/* Locked preview with subtle pattern */}
      <div className="sb-card-preview" style={{ 
        background: "linear-gradient(135deg, #fef3c7 0%, #fde68a 100%)",
        opacity: 0.8 
      }}>
        <div style={{ 
          fontSize: "0.7rem", 
          fontWeight: 800, 
          color: "rgba(146, 64, 14, 0.4)", 
          textTransform: "uppercase", 
          letterSpacing: "0.15em" 
        }}>
          Locked
        </div>
      </div>

      <span className="sb-tag sb-tag-locked">Locked</span>
      <h3 className="sb-card-title">{title}</h3>
      <p className="sb-card-meta">
        {paperCode ? `Q.P. ${paperCode} · ` : ""}
        {course} · {studyYear}
        {ORDINAL(studyYear)} Year
      </p>
      <p className="sb-card-desc">
        Get access to past papers, answers and revision materials for this subject.
      </p>
      <div className="sb-card-footer">
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
