export function InfoCard({
  title,
  subtitle,
  variant = "default",
  imageUrl,
  bgColor,
}: {
  title: string;
  subtitle?: string;
  variant?: "default" | "meme";
  imageUrl?: string;
  bgColor?: string;
}) {
  if (variant === "meme") {
    return (
      <article className="sb-card sb-card-meme sb-card-compact">
        {imageUrl ? (
          <div style={{ 
            width: "calc(100% + 26px)", 
            height: 100, 
            margin: "-14px -13px 10px",
            backgroundImage: `url(${imageUrl})`,
            backgroundSize: "cover",
            backgroundPosition: "center",
            borderRadius: "20px 20px 0 0"
          }} />
        ) : null}
        <h3 className="sb-card-title" style={{ fontSize: "0.95rem" }}>{title}</h3>
        {subtitle && <p className="sb-card-desc">{subtitle}</p>}
      </article>
    );
  }

  return (
    <article className="sb-card sb-card-compact">
      {imageUrl ? (
        <div style={{ 
          width: "calc(100% + 26px)", 
          height: 90, 
          margin: "-14px -13px 10px",
          backgroundImage: `url(${imageUrl})`,
          backgroundSize: "cover",
          backgroundPosition: "center",
          borderRadius: "20px 20px 0 0",
          border: "1.5px solid var(--sb-border)",
          borderBottom: "none"
        }} />
      ) : (
        <div className="sb-card-preview" style={{ 
          height: 80, 
          margin: "-14px -13px 8px",
          background: bgColor || "linear-gradient(135deg, #fef3c7 0%, #fde68a 100%)"
        }}>
          <div style={{ 
            fontSize: "0.65rem", 
            fontWeight: 800, 
            color: "rgba(146, 64, 14, 0.5)", 
            textTransform: "uppercase", 
            letterSpacing: "0.15em" 
          }}>
            Tip
          </div>
        </div>
      )}
      <h3 className="sb-card-title">{title}</h3>
      {subtitle && <p className="sb-card-desc">{subtitle}</p>}
    </article>
  );
}
