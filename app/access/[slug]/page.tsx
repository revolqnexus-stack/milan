import { notFound } from "next/navigation";
import { eq } from "drizzle-orm";
import { getDb, content } from "@/lib/db";
import AccessRequestForm from "./AccessRequestForm";

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const db = getDb();
  const [pack] = await db
    .select({ title: content.title })
    .from(content)
    .where(eq(content.slug, slug))
    .limit(1);
  return {
    title: pack ? `Get Access · ${pack.title}` : "Get Access · REVOLQNEXUS",
  };
}

export default async function AccessPackPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const db = getDb();
  const [pack] = await db
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
      isActive: content.isActive,
    })
    .from(content)
    .where(eq(content.slug, slug))
    .limit(1);

  if (!pack || !pack.isActive) notFound();

  return (
    <div className="sb-page access-page">
      <a href="/login" className="access-already-paid">
        i already paid 🙄
      </a>

      <main className="access-shell access-shell-narrow">
        <a href="/access" className="access-back">← back</a>

        <div className="access-pack-detail">
          <div className="access-pack-meta">
            <span className="access-pack-course">
              {pack.course} · Year {pack.studyYear}
            </span>
            {pack.paperCode && (
              <span className="access-pack-code">Q.P. {pack.paperCode}</span>
            )}
          </div>
          <h1 className="access-pack-title access-pack-title-lg">{pack.title}</h1>
          {pack.description && (
            <p className="access-pack-desc">{pack.description}</p>
          )}
          <p className="access-pack-price-lg">
            ₹{Math.round(pack.priceInrPaise / 100)}
          </p>
        </div>

        <AccessRequestForm
          contentId={pack.id}
          packTitle={pack.title}
          priceRupees={Math.round(pack.priceInrPaise / 100)}
        />
      </main>
    </div>
  );
}
