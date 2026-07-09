import Link from "next/link";
import { GlassPanel } from "@/components/ui/GlassPanel";
import { StatusChip } from "@/components/ui/StatusChip";

export function LibraryContentCard({
  title,
  slug,
  paperCode,
  course,
  studyYear,
  description,
  featured,
}: {
  title: string;
  slug: string;
  paperCode?: string | null;
  course: string;
  studyYear: number;
  description?: string | null;
  featured?: boolean;
}) {
  return (
    <Link href={`/study/${slug}`} className="content-card-link">
      <GlassPanel variant="card" featured={featured} className="content-card">
        <StatusChip status="granted" />
        <h3 className="card-title">{title}</h3>
        <p className="card-meta">
          {paperCode ? `Q.P. ${paperCode} · ` : ""}
          {course} · {studyYear}
          {studyYear === 1 ? "st" : studyYear === 2 ? "nd" : studyYear === 3 ? "rd" : "th"}{" "}
          Year
        </p>
        <p className="card-desc">
          {description ||
            "Previous-paper intelligence, mark-scoring answers, mocks and revision system."}
        </p>
        <div className="card-footer">
          <span className="card-cta">Open study pack</span>
          <span className="card-orb" aria-hidden>
            →
          </span>
        </div>
      </GlassPanel>
    </Link>
  );
}
