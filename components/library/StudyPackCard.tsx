import Link from "next/link";

const ORDINAL = (n: number) =>
  n === 1 ? "st" : n === 2 ? "nd" : n === 3 ? "rd" : "th";

// Gradient palette for visual variety
const GRADIENTS = [
  "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
  "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
  "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
  "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)",
  "linear-gradient(135deg, #fa709a 0%, #fee140 100%)",
  "linear-gradient(135deg, #30cfd0 0%, #330867 100%)",
  "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)",
  "linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)",
];

function pickGradient(title: string) {
  const hash = title.split("").reduce((acc, char) => acc + char.charCodeAt(0), 0);
  return GRADIENTS[hash % GRADIENTS.length];
}

export function StudyPackCard({
  title,
  slug,
  paperCode,
  course,
  studyYear,
  description,
}: {
  title: string;
  slug: string;
  paperCode?: string | null;
  course: string;
  studyYear: number;
  description?: string | null;
}) {
  const gradient = pickGradient(title);

  return (
    <Link href={`/study/${slug}`} className="sb-card-link">
      <article className="sb-card">
        {/* Visual preview with gradient */}
        <div className="sb-card-preview" style={{ background: gradient }}>
          <div style={{ 
            fontSize: "0.7rem", 
            fontWeight: 800, 
            color: "rgba(255,255,255,0.4)", 
            textTransform: "uppercase", 
            letterSpacing: "0.15em" 
          }}>
            {paperCode || "Study Pack"}
          </div>
        </div>

        <span className="sb-tag sb-tag-granted">Access granted</span>
        <h3 className="sb-card-title">{title}</h3>
        <p className="sb-card-meta">
          {paperCode ? `Q.P. ${paperCode} · ` : ""}
          {course} · {studyYear}
          {ORDINAL(studyYear)} Year
        </p>
        <p className="sb-card-desc">
          {description ||
            "Previous-paper intelligence, mark-scoring answers, mocks and revision system."}
        </p>
        <div className="sb-card-footer">
          <span className="sb-card-open">Open</span>
          <span className="sb-card-arrow" aria-hidden>→</span>
        </div>
      </article>
    </Link>
  );
}
