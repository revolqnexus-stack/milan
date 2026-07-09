export function InfoCard({
  title,
  subtitle,
  imageUrl,
  bgColor,
}: {
  title: string;
  subtitle?: string;
  imageUrl?: string;
  bgColor?: string;
}) {
  if (imageUrl) {
    // Full image card with overlay
    return (
      <article className="sb-card sb-card-compact">
        <div 
          className="sb-card-visual sb-card-visual-short"
          style={{
            backgroundImage: `url(${imageUrl})`,
          }}
        >
          <div className="sb-card-overlay" />
          <div className="sb-card-content-overlay">
            <h3 className="sb-card-title">{title}</h3>
            {subtitle && <p className="sb-card-meta">{subtitle}</p>}
          </div>
        </div>
      </article>
    );
  }

  // Text-only card with colored background
  return (
    <article className="sb-card sb-card-text-only" style={{ 
      background: bgColor || "linear-gradient(135deg, #fef3c7 0%, #fde68a 100%)",
      borderColor: bgColor ? "rgba(0,0,0,0.08)" : "rgba(245, 158, 11, 0.3)"
    }}>
      <h3 className="sb-card-title" style={{ color: bgColor ? "var(--sb-text)" : "#92400e" }}>
        {title}
      </h3>
      {subtitle && (
        <p className="sb-card-desc" style={{ color: bgColor ? "var(--sb-text-muted)" : "#b45309" }}>
          {subtitle}
        </p>
      )}
    </article>
  );
}

