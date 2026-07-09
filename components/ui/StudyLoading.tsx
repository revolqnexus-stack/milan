"use client";

import { useEffect, useState } from "react";

export function StudyLoading({ text = "Loading your study board..." }: { text?: string }) {
  const [show, setShow] = useState(false);

  useEffect(() => {
    setShow(true);
  }, []);

  if (!show) return null;

  return (
    <div style={{
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
      padding: "60px 20px",
      gap: "20px"
    }}>
      {/* Animated floating books */}
      <img 
        src="/media/animations/floating-books.svg" 
        alt=""
        width="200"
        height="200"
        style={{ opacity: 0.9 }}
      />
      
      <p style={{
        fontSize: "14px",
        color: "var(--sb-text-muted)",
        fontWeight: 600,
        textAlign: "center"
      }}>
        {text}
      </p>
    </div>
  );
}
