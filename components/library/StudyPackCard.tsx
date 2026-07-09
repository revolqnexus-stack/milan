import Link from "next/link";

const ORDINAL = (n: number) =>
  n === 1 ? "st" : n === 2 ? "nd" : n === 3 ? "rd" : "th";

// Gradient palette for cards (no external images)
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
        {/* Tag floats on top */}
        <div className="sb-card-tag-float">
          <span className="sb-tag sb-tag-granted">Unlocked</span>
        </div>

        {/* Gradient visual with text overlay */}
        <div 
          className="sb-card-visual"
          style={{
            background: gradient,
          }}
        >
          <div className="sb-card-overlay" />
          <div className="sb-card-content-overlay">
            <h3 className="sb-card-title">{title}</h3>
            <p className="sb-card-meta">
              {paperCode ? `Q.P. ${paperCode} · ` : ""}
              {course} · {studyYear}
              {ORDINAL(studyYear)} Year
            </p>
          </div>
        </div>

        {/* Optional compact text section */}
        {description && (
          <div className="sb-card-text-compact">
            <p className="sb-card-desc">{description}</p>
          </div>
        )}
      </article>
    </Link>
  );
}
