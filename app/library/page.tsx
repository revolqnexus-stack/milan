import Link from "next/link";
import { redirect } from "next/navigation";
import { getStudentAuth } from "@/lib/auth/student-session";
import { listLibraryForUser } from "@/lib/auth/entitlements";
import { LogoutButton } from "./logout-button";
import { ThemeToggle } from "@/components/ui/ThemeToggle";
import { PageEyebrow } from "@/components/ui/PageEyebrow";
import { DisplayHeading } from "@/components/ui/DisplayHeading";
import { LibraryContentCard } from "@/components/library/LibraryContentCard";
import { LockedContentCard } from "@/components/library/LockedContentCard";

export const dynamic = "force-dynamic";

export default async function LibraryPage() {
  const auth = await getStudentAuth();
  if (!auth) redirect("/login");

  const items = await listLibraryForUser(auth.userId);
  const unlocked = items.filter((i) => i.entitled).length;

  const grouped = new Map<string, Map<number, typeof items>>();
  for (const item of items) {
    if (!grouped.has(item.course)) grouped.set(item.course, new Map());
    const years = grouped.get(item.course)!;
    if (!years.has(item.studyYear)) years.set(item.studyYear, []);
    years.get(item.studyYear)!.push(item);
  }

  return (
    <main className="vault-page">
      <div className="lib-shell">
        <div className="glass-panel glass-nav lib-nav">
          <Link href="/library" className="brand-mark">
            REVOLQ<span>NEXUS</span>
          </Link>
          <div className="lib-nav-actions">
            <span className="account-chip">{auth.studentId}</span>
            <ThemeToggle />
            <LogoutButton />
          </div>
        </div>

        <header className="motion-fade-up">
          <PageEyebrow>Your library</PageEyebrow>
          <DisplayHeading>Study what matters.</DisplayHeading>
          <p className="body-copy">
            Your exam packs, organised by course and year.
          </p>
          <div className="lib-stats">
            <span className="lib-stat">{unlocked} packs unlocked</span>
            <span className="lib-stat">{items.length} subjects listed</span>
            <span className="lib-stat">Hi, {auth.name}</span>
          </div>
        </header>

        {items.length === 0 && (
          <p className="body-copy muted">
            No study materials yet. Contact us after payment.
          </p>
        )}

        {[...grouped.entries()].map(([course, years]) => (
          <section key={course} className="lib-course">
            <h2 className="lib-course-title">{course}</h2>
            {[...years.entries()]
              .sort((a, b) => a[0] - b[0])
              .map(([year, list]) => (
                <div key={year}>
                  <p className="lib-year-label">
                    {year}
                    {year === 1 ? "st" : year === 2 ? "nd" : year === 3 ? "rd" : "th"}{" "}
                    Year
                  </p>
                  <div className="lib-grid">
                    {list.map((item, idx) =>
                      item.entitled ? (
                        <LibraryContentCard
                          key={item.id}
                          title={item.title}
                          slug={item.slug}
                          paperCode={item.paperCode}
                          course={item.course}
                          studyYear={item.studyYear}
                          description={item.description}
                          featured={idx === 0}
                        />
                      ) : (
                        <LockedContentCard
                          key={item.id}
                          title={item.title}
                          paperCode={item.paperCode}
                          course={item.course}
                          studyYear={item.studyYear}
                          priceInrPaise={item.priceInrPaise}
                        />
                      )
                    )}
                  </div>
                </div>
              ))}
          </section>
        ))}
      </div>
    </main>
  );
}
