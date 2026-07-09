import { GlassPanel } from "@/components/ui/GlassPanel";
import { StatusChip } from "@/components/ui/StatusChip";

function formatPrice(paise: number) {
  return `₹${Math.round(paise / 100)}`;
}

export function LockedContentCard({
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
    <GlassPanel variant="muted" className="content-card locked">
      <StatusChip status="locked" />
      <h3 className="card-title">{title}</h3>
      <p className="card-meta">
        {paperCode ? `Q.P. ${paperCode} · ` : ""}
        {course} · {studyYear}
        {studyYear === 1 ? "st" : studyYear === 2 ? "nd" : studyYear === 3 ? "rd" : "th"}{" "}
        Year
      </p>
      <div className="card-footer">
        <span className="card-price">{formatPrice(priceInrPaise)}</span>
        <a className="card-cta" href={href} target="_blank" rel="noreferrer">
          Enquire
        </a>
      </div>
    </GlassPanel>
  );
}
