export function MemeCard({
  imageUrl,
  title,
  subtitle,
  overlay = true,
}: {
  imageUrl: string;
  title?: string;
  subtitle?: string;
  overlay?: boolean;
}) {
  return (
    <article className="sb-card sb-card-compact" style={{ padding: 0, overflow: "hidden" }}>
      <div
        style={{
          width: "100%",
          height: 180,
          backgroundImage: `url(${imageUrl})`,
          backgroundSize: "cover",
          backgroundPosition: "center",
          position: "relative",
          display: "flex",
          flexDirection: "column",
          justifyContent: "flex-end",
          padding: "12px 14px",
        }}
      >
        {overlay && (
          <div
            style={{
              position: "absolute",
              inset: 0,
              background: "linear-gradient(to top, rgba(0,0,0,0.65) 0%, transparent 50%)",
            }}
          />
        )}
        {(title || subtitle) && (
          <div style={{ position: "relative", zIndex: 1 }}>
            {title && (
              <h3
                style={{
                  fontSize: "0.95rem",
                  fontWeight: 800,
                  color: "#fff",
                  margin: "0 0 3px",
                  textShadow: "0 1px 3px rgba(0,0,0,0.5)",
                  lineHeight: 1.25,
                }}
              >
                {title}
              </h3>
            )}
            {subtitle && (
              <p
                style={{
                  fontSize: "11px",
                  color: "rgba(255,255,255,0.9)",
                  margin: 0,
                  textShadow: "0 1px 2px rgba(0,0,0,0.5)",
                }}
              >
                {subtitle}
              </p>
            )}
          </div>
        )}
      </div>
    </article>
  );
}
