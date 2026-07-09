import { ImageResponse } from "next/og";

export const size = { width: 180, height: 180 };
export const contentType = "image/png";

export const dynamic = "force-dynamic";

export default function AppleIcon() {
  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          background: "linear-gradient(160deg, #0f172a 0%, #070b16 100%)",
          borderRadius: 40,
          border: "3px solid rgba(61,125,255,0.38)",
        }}
      >
        <div
          style={{
            fontSize: 120,
            fontWeight: 700,
            color: "#3d7dff",
            fontFamily: "sans-serif",
            letterSpacing: "-0.06em",
          }}
        >
          R
        </div>
      </div>
    ),
    { ...size }
  );
}
