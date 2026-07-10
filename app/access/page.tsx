import Link from "next/link";
import { getDb, content } from "@/lib/db";
import { eq, asc } from "drizzle-orm";

export const metadata = {
  title: "Get Access · REVOLQNEXUS",
  description: "Choose a study pack and get access.",
};

async function getActivePacks() {
  const db = getDb();
  return db
    .select({
      id: content.id,
      title: content.title,
      slug: content.slug,
      course: content.course,
      studyYear: content.studyYear,
      subject: content.subject,
      paperCode: content.paperCode,
      description: content.description,
      priceInrPaise: content.priceInrPaise,
    })
    .from(content)
    .where(eq(content.isActive, true))
    .orderBy(asc(content.sortOrder), asc(content.title));
}

export default async function AccessPage() {
  const packs = await getActivePacks();

  return (
    <div className="sb-page access-page">
      {/* Sticky login hint */}
      <a href="/login" className="access-already-paid">
        i already paid 🙄
      </a>

      <main className="access-shell">
        <div className="access-header">
          <p className="access-eyebrow">okay here&apos;s the boring part</p>
          <h1 className="access-heading">what do you need?</h1>
          <p className="access-sub">pick the pack. we sort the rest.</p>
        </div>

        {packs.length === 0 ? (
          <div className="access-empty">
            <p>no packs live yet.</p>
            <p className="access-empty-sub">check back soon — or just login if you already have access.</p>
          </div>
        ) : (
          <div className="access-packs">
            {packs.map((pack) => (
              <div key={pack.id} className="access-pack-card">
                <div className="access-pack-meta">
                  <span className="access-pack-course">
                    {pack.course} · Year {pack.studyYear}
                  </span>
                  {pack.paperCode && (
                    <span className="access-pack-code">Q.P. {pack.paperCode}</span>
                  )}
                </div>
                <h2 className="access-pack-title">{pack.title}</h2>
                {pack.description && (
                  <p className="access-pack-desc">{pack.description}</p>
                )}
                <div className="access-pack-footer">
                  <span className="access-pack-price">
                    ₹{Math.round(pack.priceInrPaise / 100)}
                  </span>
                  <Link
                    href={`/access/${pack.slug}`}
                    className="access-pack-cta"
                  >
                    GET ACCESS →
                  </Link>
                </div>
              </div>
            ))}
          </div>
        )}

        <p className="access-footer-note">
          already have access?{" "}
          <Link href="/login" className="access-footer-link">
            login here →
          </Link>
        </p>
      </main>
    </div>
  );
}
