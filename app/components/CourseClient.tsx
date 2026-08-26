"use client";

import { useEffect, useMemo, useState } from "react";
import { CourseData, SiteManifest } from "@/lib/types";
import { chapterByNumber } from "@/lib/utils";
import Sidebar from "./Sidebar";
import ChapterContent from "./ChapterContent";
import { SiteWelcome, CourseWelcome } from "./WelcomeScreens";
import SearchResults from "./SearchResults";

export default function CourseClient({ manifest }: { manifest: SiteManifest }) {
  const [loadedCourses, setLoadedCourses] = useState<Record<string, CourseData>>({});
  const [currentCourseId, setCurrentCourseId] = useState<string | null>(null);
  const [currentChapterNumber, setCurrentChapterNumber] = useState<number | null>(null);
  const [expandedCourses, setExpandedCourses] = useState<Set<string>>(new Set());
  const [expandedModules, setExpandedModules] = useState<Record<string, Set<number>>>({});
  const [completedByCourse, setCompletedByCourse] = useState<Record<string, number[]>>({});
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [loadingCourseId, setLoadingCourseId] = useState<string | null>(null);
  const [searchQuery, setSearchQuery] = useState("");
  const [highlightQuery, setHighlightQuery] = useState("");

  const totalChapters = useMemo(
    () => manifest.courses.reduce((a, c) => a + c.chaptersCount, 0),
    [manifest.courses]
  );

  const completedTotal = useMemo(
    () => Object.values(completedByCourse).flat().length,
    [completedByCourse]
  );

  const overallProgress = totalChapters > 0 ? Math.round((completedTotal / totalChapters) * 100) : 0;

  // Load completed progress from localStorage.
  useEffect(() => {
    if (typeof window === "undefined") return;
    try {
      const saved = JSON.parse(localStorage.getItem("courseProgress") || "{}");
      if (typeof saved === "object" && saved !== null) {
        setCompletedByCourse(saved);
      }
    } catch {
      // ignore
    }
  }, []);

  // Persist completed progress.
  useEffect(() => {
    if (typeof window === "undefined") return;
    localStorage.setItem("courseProgress", JSON.stringify(completedByCourse));
  }, [completedByCourse]);

  // Parse URL hash on load and back/forward.
  useEffect(() => {
    if (typeof window === "undefined") return;

    const parseHash = () => {
      const hash = window.location.hash.slice(1);
      const params = new URLSearchParams(hash);
      const courseId = params.get("course");
      const chapterNum = params.get("chapter");

      if (courseId && manifest.courses.some((c) => c.id === courseId)) {
        if (chapterNum) {
          selectChapter(courseId, parseInt(chapterNum, 10));
        } else {
          selectCourse(courseId);
        }
      } else if (chapterNum && !courseId) {
        // Legacy hash from single-course version: #chapter-30
        const num = parseInt(chapterNum, 10);
        if (num <= 30) {
          selectChapter("01", num);
        } else {
          // Try course 02 if it exists and covers that number range.
          const has02 = manifest.courses.some((c) => c.id === "02");
          if (has02) selectChapter("02", num);
          else selectChapter("01", num);
        }
      }
    };

    parseHash();

    const onPop = () => parseHash();
    window.addEventListener("popstate", onPop);
    return () => window.removeEventListener("popstate", onPop);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [manifest.courses]);

  async function loadCourse(id: string): Promise<CourseData | null> {
    if (loadedCourses[id]) return loadedCourses[id];

    setLoadingCourseId(id);
    try {
      const res = await fetch(`/courses/${id}.json`);
      if (!res.ok) throw new Error(`Failed to load course ${id}: ${res.status}`);
      const data: CourseData = await res.json();
      setLoadedCourses((prev) => ({ ...prev, [id]: data }));
      return data;
    } catch (err) {
      console.error("Error loading course:", id, err);
      return null;
    } finally {
      setLoadingCourseId(null);
    }
  }

  async function selectCourse(id: string) {
    setCurrentCourseId(id);
    setCurrentChapterNumber(null);
    setExpandedCourses((prev) => new Set(prev).add(id));
    await loadCourse(id);
  }

  async function selectChapter(courseId: string, chapterNumber: number, highlightTerm = "") {
    const course = await loadCourse(courseId);
    if (!course) return;

    const chapter = chapterByNumber(course.modules).get(chapterNumber);
    if (!chapter) return;

    setCurrentCourseId(courseId);
    setCurrentChapterNumber(chapterNumber);
    setSearchQuery("");
    setHighlightQuery(highlightTerm);
    setExpandedCourses((prev) => new Set(prev).add(courseId));
    setExpandedModules((prev) => {
      const next: Record<string, Set<number>> = { ...prev };
      if (!next[courseId]) next[courseId] = new Set();
      else next[courseId] = new Set(next[courseId]);
      next[courseId].add(chapter.moduleNumber);
      return next;
    });

    if (typeof window !== "undefined") {
      if (!highlightTerm) {
        window.scrollTo(0, 0);
      }
      if (window.innerWidth <= 768) {
        setSidebarOpen(false);
      }
      history.pushState(
        null,
        "",
        `#course=${courseId}&chapter=${chapterNumber}`
      );
    }
  }

  function toggleCourse(id: string) {
    setExpandedCourses((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  }

  function toggleModule(courseId: string, moduleNumber: number) {
    setExpandedModules((prev) => {
      const next: Record<string, Set<number>> = { ...prev };
      if (!next[courseId]) next[courseId] = new Set();
      else next[courseId] = new Set(next[courseId]);

      if (next[courseId].has(moduleNumber)) {
        next[courseId].delete(moduleNumber);
      } else {
        next[courseId].add(moduleNumber);
      }
      return next;
    });
  }

  function markComplete(courseId: string, chapterNumber: number) {
    setCompletedByCourse((prev) => {
      const arr = prev[courseId] || [];
      if (arr.includes(chapterNumber)) return prev;
      return { ...prev, [courseId]: [...arr, chapterNumber] };
    });
  }

  const currentCourse = currentCourseId ? loadedCourses[currentCourseId] : null;
  const currentChapter =
    currentCourse && currentChapterNumber
      ? chapterByNumber(currentCourse.modules).get(currentChapterNumber)
      : null;

  useEffect(() => {
    if (currentChapter) {
      document.title = `${currentChapter.fullTitle} | ${currentCourse?.title || manifest.siteTitle}`;
    } else if (currentCourse) {
      document.title = `${currentCourse.title} | ${manifest.siteTitle}`;
    } else {
      document.title = manifest.siteTitle;
    }
  }, [currentChapter, currentCourse, manifest.siteTitle]);

  const headerTitle = currentCourse ? currentCourse.title : manifest.siteTitle;

  return (
    <div className="min-h-screen">
      <header className="course-header fixed top-0 left-0 right-0 z-50 h-[60px] bg-gradient-to-r from-primary to-primary-dark text-white shadow-lg flex items-center justify-between px-5">
        <a href="/" className="logo flex items-center gap-3 no-underline">
          <span className="text-2xl">🎓</span>
          <span className="font-serif text-xl font-bold">
            Visual <span className="text-accent">Course</span>
          </span>
        </a>
        <span className="course-title-header hidden lg:block font-medium opacity-90 text-sm truncate max-w-md text-center">
          {headerTitle}
        </span>
        <div className="header-actions flex items-center gap-4">
          <div className="progress-indicator hidden sm:flex items-center gap-2 text-sm">
            <span>Progress</span>
            <div className="w-[120px] h-[6px] bg-white/30 rounded-full overflow-hidden">
              <div
                className="h-full bg-accent rounded-full transition-all duration-300"
                style={{ width: `${overallProgress}%` }}
              />
            </div>
            <span className="w-8 text-right">{overallProgress}%</span>
          </div>
          <button
            onClick={() => setSidebarOpen((s) => !s)}
            className="menu-toggle md:hidden bg-white/20 hover:bg-white/30 border-0 text-white px-3 py-2 rounded-md text-lg cursor-pointer"
            aria-label="Toggle menu"
          >
            ☰
          </button>
        </div>
      </header>

      {sidebarOpen && (
        <div
          className="sidebar-overlay fixed inset-0 bg-black/50 z-40 md:hidden"
          style={{ top: "60px" }}
          onClick={() => setSidebarOpen(false)}
        />
      )}

      <div className="course-layout flex mt-[60px] min-h-[calc(100vh-60px)]">
        <Sidebar
          manifest={manifest}
          open={sidebarOpen}
          currentCourseId={currentCourseId}
          currentChapterNumber={currentChapterNumber}
          expandedCourses={expandedCourses}
          expandedModules={expandedModules}
          completedByCourse={completedByCourse}
          searchQuery={searchQuery}
          onSearch={setSearchQuery}
          onToggleCourse={toggleCourse}
          onToggleModule={toggleModule}
          onSelectChapter={selectChapter}
          onCloseSidebar={() => setSidebarOpen(false)}
        />

        <main
          className={cn(
            "main-content flex-1 p-6 md:p-10",
            "md:ml-[var(--sidebar-width)]"
          )}
        >
          <div className="content-wrapper bg-white rounded-2xl shadow p-6 md:p-12 min-h-[calc(100vh-140px)]">
            {searchQuery.trim() ? (
              <SearchResults
                query={searchQuery}
                onSelect={(courseId, chapterNumber) =>
                  selectChapter(courseId, chapterNumber, searchQuery.trim())
                }
              />
            ) : loadingCourseId && !currentCourse ? (
              <div className="flex items-center justify-center h-64 text-gray-500">
                <div className="text-center">
                  <div className="text-3xl mb-3">⏳</div>
                  <p>Loading course...</p>
                </div>
              </div>
            ) : currentChapter && currentCourse ? (
              <ChapterContent
                chapter={currentChapter}
                course={currentCourse}
                completed={completedByCourse[currentCourse.id] || []}
                onMarkComplete={(n) => markComplete(currentCourse.id, n)}
                onNavigate={selectChapter}
                highlightQuery={highlightQuery}
              />
            ) : currentCourse ? (
              <CourseWelcome
                course={currentCourse}
                completed={completedByCourse[currentCourse.id] || []}
                onStart={() => {
                  const first = currentCourse.modules[0]?.chapters[0];
                  if (first) selectChapter(currentCourse.id, first.number);
                }}
              />
            ) : (
              <SiteWelcome
                manifest={manifest}
                completedByCourse={completedByCourse}
                completedTotal={completedTotal}
                totalChapters={totalChapters}
                onSelectCourse={selectCourse}
              />
            )}
          </div>
        </main>
      </div>
    </div>
  );
}

function cn(...classes: (string | false | null | undefined)[]) {
  return classes.filter(Boolean).join(" ");
}
