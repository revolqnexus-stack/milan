export function EmptyLibrary() {
  const whatsappUrl = process.env.NEXT_PUBLIC_WHATSAPP_URL || "https://wa.me/";
  
  return (
    <div style={{
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
      padding: "80px 20px",
      textAlign: "center",
      maxWidth: "420px",
      margin: "0 auto"
    }}>
      {/* Animated exam papers */}
      <img 
        src="/media/animations/exam-paper-shuffle.svg" 
        alt=""
        width="180"
        height="200"
        style={{ marginBottom: "24px", opacity: 0.9 }}
      />
      
      <h3 style={{
        fontSize: "1.3rem",
        fontWeight: 800,
        color: "var(--sb-text)",
        margin: "0 0 8px",
        letterSpacing: "-0.02em"
      }}>
        Your study board is empty
      </h3>
      
      <p style={{
        fontSize: "14px",
        color: "var(--sb-text-muted)",
        lineHeight: 1.6,
        margin: "0 0 24px"
      }}>
        No study materials yet. Contact us after payment and we'll activate your packs.
      </p>
      
      <a
        href={whatsappUrl}
        target="_blank"
        rel="noreferrer"
        className="sb-btn sb-btn-primary"
        style={{ textDecoration: "none" }}
      >
        Contact on WhatsApp
      </a>
    </div>
  );
}
