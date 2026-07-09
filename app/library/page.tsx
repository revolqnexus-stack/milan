import Link from "next/link";
import { redirect } from "next/navigation";
import { getStudentAuth } from "@/lib/auth/student-session";
import { listLibraryForUser } from "@/lib/auth/entitlements";
import { LogoutButton } from "./logout-button";
import { StudyPackCard } from "@/components/library/StudyPackCard";
import { LockedPackCard } from "@/components/library/LockedPackCard";
import { LibraryFilters } from "@/components/library/LibraryFilters";
import { InfoCard } from "@/components/library/InfoCard";
import { MemeCard } from "@/components/library/MemeCard";
import { EmptyLibrary } from "@/components/library/EmptyLibrary";
import { LIBRARY_MEMES, INFO_MESSAGES } from "@/lib/library-memes";

export const dynamic = "force-dynamic";

export default async function LibraryPage() {
  const auth = await getStudentAuth();
  if (!auth) redirect("/login");

  const items = await listLibraryForUser(auth.userId);
  const unlocked = items.filter((i) => i.entitled).length;
  const total = items.length;

  const grouped = new Map<string, Map<number, typeof items>>();
  for (const item of items) {
    if (!grouped.has(item.course)) grouped.set(item.course, new Map());
    const years = grouped.get(item.course)!;
    if (!years.has(item.studyYear)) years.set(item.studyYear, []);
    years.get(item.studyYear)!.push(item);
  }

  return (
    <div className="sb-page">
      {/* Top bar */}
      <header className="sb-topbar">
        <Link href="/library" className="sb-brand">
          REVOLQ<span>NEXUS</span>
        </Link>
        <div className="sb-topbar-right">
          <span className="sb-account-pill">{auth.studentId}</span>
          <LogoutButton />
        </div>
      </header>

      {/* Main content */}
      <main className="sb-inner sb-lib-content">
        {/* Header */}
        <div className="sb-lib-header sb-fade-up">
          <h1 className="sb-lib-heading">
            Hey, {auth.name.split(" ")[0]} 👋
          </h1>
          <p className="sb-lib-subhead">
            Your study board — browse, tap, and get to work.
          </p>

          {/* Quick stats */}
          <div className="sb-stats-row">
            <div className="sb-stat-card">
              <span className="sb-stat-num">{unlocked}</span>
              <span className="sb-stat-label">Packs unlocked</span>
            </div>
            <div className="sb-stat-card">
              <span className="sb-stat-num">{total}</span>
              <span className="sb-stat-label">Total listed</span>
            </div>
            <div className="sb-stat-card">
              <span className="sb-stat-num">{total - unlocked}</span>
              <span className="sb-stat-label">Available to unlock</span>
            </div>
          </div>
        </div>

        {/* Filter chips (client island) */}
        <LibraryFilters />

        {items.length === 0 ? (
          <EmptyLibrary />
        ) : (
          <>
            {/* Course sections */}
            {[...grouped.entries()].map(([course, years]) => (
          <section key={course} className="sb-course-section">
            <h2 className="sb-course-heading">{course}</h2>

            {[...years.entries()]
              .sort((a, b) => a[0] - b[0])
              .map(([year, list]) => {
                const ordinal =
                  year === 1
                    ? "st"
                    : year === 2
                    ? "nd"
                    : year === 3
                    ? "rd"
                    : "th";
                return (
                  <div key={year}>
                    <p className="sb-year-label">
                      {year}
                      {ordinal} Year
                    </p>
                    <div className="sb-grid">
                      {/* Inject meme/info cards at strategic positions (only if available) */}
                      {list.length > 2 && list.map((_, idx) => idx).includes(1) && LIBRARY_MEMES[0] && (
                        <MemeCard
                          key="meme-1"
                          imageUrl={LIBRARY_MEMES[0].imageUrl}
                          title={LIBRARY_MEMES[0].title}
                          subtitle={LIBRARY_MEMES[0].subtitle}
                        />
                      )}
                      {list.length > 3 && list.map((_, idx) => idx).includes(2) && (
                        <InfoCard
                          key="info-1"
                          title={INFO_MESSAGES[0].title}
                          subtitle={INFO_MESSAGES[0].subtitle}
                        />
                      )}
                      {list.length > 5 && list.map((_, idx) => idx).includes(4) && (
                        <InfoCard
                          key="info-2"
                          title={INFO_MESSAGES[1].title}
                          subtitle={INFO_MESSAGES[1].subtitle}
                          bgColor="linear-gradient(135deg, #e0e7ff 0%, #c7d2fe 100%)"
                        />
                      )}
                      {list.length > 7 && list.map((_, idx) => idx).includes(6) && LIBRARY_MEMES[1] && (
                        <MemeCard
                          key="meme-2"
                          imageUrl={LIBRARY_MEMES[1].imageUrl}
                          title={LIBRARY_MEMES[1].title}
                          subtitle={LIBRARY_MEMES[1].subtitle}
                        />
                      )}
                      {list.map((item) =>
                        item.entitled ? (
                          <StudyPackCard
                            key={item.id}
                            title={item.title}
                            slug={item.slug}
                            paperCode={item.paperCode}
                            course={item.course}
                            studyYear={item.studyYear}
                            description={item.description}
                          />
                        ) : (
                          <LockedPackCard
                            key={item.id}
                            title={item.title}
                            paperCode={item.paperCode}
                            course={item.course}
                            studyYear={item.studyYear}
                            priceInrPaise={item.priceInrPaise}
                          />
                        )
                      )}
                      {list.length > 8 && list.map((_, idx) => idx).includes(8) && (
                        <InfoCard
                          key="info-3"
                          title={INFO_MESSAGES[2].title}
                          subtitle={INFO_MESSAGES[2].subtitle}
                        />
                      )}
                    </div>
                  </div>
                );
              })}
          </section>
        ))}
          </>
        )}
      </main>
    </div>
  );
}
