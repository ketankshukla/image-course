"use client";

import { useEffect, useMemo, useRef, useState, type CSSProperties } from "react";
import Link from "next/link";
import dynamic from "next/dynamic";
import { CourseData, SiteManifest } from "@/lib/types";
import { chapterByNumber } from "@/lib/utils";
import Sidebar from "./Sidebar";
import ChapterContent from "./ChapterContent";
import { SiteWelcome, CourseWelcome } from "./WelcomeScreens";
const SearchResults = dynamic(() => import("./SearchResults"), { loading: () => <p role="status">Loading search…</p> });

type Shelf = "course" | "case-study" | "guide";
type Selection = { courseId: string | null; number: number | null; anchor: string | null };

export default function CourseClient({ manifest }: { manifest: SiteManifest }) {
  const [loaded, setLoaded] = useState<Record<string, CourseData>>({});
  const cache = useRef<Record<string, Promise<CourseData>>>({});
  const [selection, setSelection] = useState<Selection>({ courseId: null, number: null, anchor: null });
  const [shelf, setShelf] = useState<Shelf>("course");
  const [expandedCourses, setExpandedCourses] = useState<Set<string>>(new Set());
  const [expandedModules, setExpandedModules] = useState<Record<string, Set<number>>>({});
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");
  const [highlightQuery, setHighlightQuery] = useState("");
  const [error, setError] = useState("");
  const [retry, setRetry] = useState(0);
  const [readingSize, setReadingSize] = useState(24);
  useEffect(() => {
    try {
      const saved = Number(localStorage.getItem("libraryReadingSize"));
      if ([22, 24, 28].includes(saved)) setReadingSize(saved);
    } catch { /* Reading controls also work when storage is unavailable. */ }
  }, []);
  function changeReadingSize(size: number) {
    if (![22, 24, 28].includes(size)) return;
    setReadingSize(size);
    try { localStorage.setItem("libraryReadingSize", String(size)); } catch { /* Optional preference persistence. */ }
  }
  const currentSummary = manifest.courses.find(c => c.id === selection.courseId);
  const currentCourse = selection.courseId ? loaded[selection.courseId] : undefined;
  const currentChapter = currentCourse && selection.number ? chapterByNumber(currentCourse.modules).get(selection.number) : undefined;

  useEffect(() => {
    const parse = () => {
      const hash = window.location.hash.slice(1);
      const params = new URLSearchParams(hash);
      const legacy = hash.match(/^chapter-(\d+)$/);
      const numberText = params.get("chapter") || legacy?.[1];
      const number = numberText ? Number(numberText) : null;
      const id = params.get("course") || (number ? manifest.courses.find(c => c.kind === "course" && c.modules.some(m => m.chapters.some(ch => ch.number === number)))?.id : null);
      const collection = manifest.courses.find(c => c.id === id);
      if (id && (!collection || (number !== null && !collection.modules.some(m => m.chapters.some(c => c.number === number))))) {
        setError("That article is not available. Choose a collection from the library.");
        setSelection({ courseId: null, number: null, anchor: null });
        return;
      }
      setError("");
      setSearchQuery("");
      setSelection({ courseId: id || null, number, anchor: params.get("anchor") });
      if (collection) {
        setShelf(collection.kind);
        setExpandedCourses(prev => new Set(prev).add(collection.id));
        const section = collection.modules.find(m => m.chapters.some(c => c.number === number));
        if (section) setExpandedModules(prev => ({ ...prev, [collection.id]: new Set(prev[collection.id]).add(section.number) }));
      } else {
        const requestedShelf = params.get("shelf");
        setShelf(requestedShelf === "case-study" || requestedShelf === "guide" ? requestedShelf : "course");
      }
      setSidebarOpen(false);
    };
    parse();
    window.addEventListener("popstate", parse);
    window.addEventListener("hashchange", parse);
    return () => { window.removeEventListener("popstate", parse); window.removeEventListener("hashchange", parse); };
  }, [manifest]);

  useEffect(() => {
    if (!currentSummary || loaded[currentSummary.id]) return;
    let cancelled = false;
    const { id, dataUrl } = currentSummary;
    if (!cache.current[id]) cache.current[id] = fetch(dataUrl).then(async response => {
      if (!response.ok) throw Error("Unable to load this collection. Please try again.");
      const data: CourseData = await response.json();
      if (data.id !== id) throw Error("Unexpected collection response.");
      return data;
    });
    cache.current[id].then(data => {
      if (!cancelled) setLoaded(prev => ({ ...prev, [id]: data }));
    }).catch(() => {
      delete cache.current[id];
      if (!cancelled) setError("Unable to load this collection. Please try again.");
    });
    return () => { cancelled = true; };
  }, [currentSummary, loaded, retry]);

  useEffect(() => {
    document.title = currentChapter ? `${currentChapter.title} | ${currentCourse?.title}` : currentSummary?.title || manifest.siteTitle;
    if (selection.anchor && currentChapter) {
      document.getElementById(selection.anchor)?.scrollIntoView({ block: "start" });
    } else if (!highlightQuery) window.scrollTo(0, 0);
  }, [currentChapter, currentCourse, currentSummary, selection.anchor, highlightQuery, manifest.siteTitle]);

  function navigate(id: string | null, number?: number, highlight = "") {
    const url = id ? `#course=${id}${number ? `&chapter=${number}` : ""}` : window.location.pathname;
    history.pushState(null, "", url);
    setHighlightQuery(highlight);
    window.dispatchEvent(new PopStateEvent("popstate"));
  }
  function toggleCourse(id: string) {
    setExpandedCourses(prev => { const next = new Set(prev); if (next.has(id)) next.delete(id); else next.add(id); return next; });
  }
  function toggleModule(id: string, number: number) {
    setExpandedModules(prev => { const next = new Set(prev[id]); if (next.has(number)) next.delete(number); else next.add(number); return { ...prev, [id]: next }; });
  }
  function changeShelf(next: Shelf) {
    history.pushState(null, "", `#shelf=${next}`);
    setHighlightQuery("");
    window.dispatchEvent(new PopStateEvent("popstate"));
  }
  const visibleManifest = useMemo(() => ({ ...manifest, courses: manifest.courses.filter(c => c.kind === shelf) }), [manifest, shelf]);

  return (
    <div className="min-h-screen" style={{ "--reading-size": `${readingSize}px` } as CSSProperties}>
      <a className="sr-only focus:not-sr-only focus:fixed focus:top-2 focus:left-2 z-[60] bg-white p-3" href="#main-content" onClick={event => { event.preventDefault(); document.getElementById("main-content")?.focus(); }}>Skip to content</a>
      <header className="site-header course-header fixed top-0 left-0 right-0 z-50 h-[60px] text-white shadow-lg flex items-center justify-between px-5">
        <Link href="/" onClick={e => { e.preventDefault(); navigate(null); }} className="flex items-center gap-3 no-underline text-white">
          <span className="text-2xl">🎓</span><span className="font-serif text-xl font-bold">Visual <span className="text-accent">Library</span></span>
        </Link>
        <span className="hidden lg:block text-sm truncate max-w-md">{currentSummary?.title || "Concepts → Case studies → Working projects"}</span>
        <div className="flex items-center gap-4">
          <button onClick={() => setSidebarOpen(s => !s)} className="md:hidden bg-white/20 px-3 py-2 rounded-md" aria-label="Toggle menu" aria-expanded={sidebarOpen}>☰</button>
        </div>
      </header>
      {sidebarOpen && <div className="fixed inset-0 top-[60px] bg-black/50 z-30 md:hidden" onClick={() => setSidebarOpen(false)} />}
      <div className="flex mt-[60px] min-h-[calc(100vh-60px)]">
        <Sidebar manifest={manifest} shelf={shelf} onShelfChange={changeShelf} open={sidebarOpen}
          currentCourseId={selection.courseId} currentChapterNumber={selection.number}
          expandedCourses={expandedCourses} expandedModules={expandedModules}
          searchQuery={searchQuery} onSearch={setSearchQuery} onToggleCourse={toggleCourse}
          onToggleModule={toggleModule} onSelectChapter={navigate} onCloseSidebar={() => setSidebarOpen(false)} />
        <main id="main-content" tabIndex={-1} className="main-content min-w-0 flex-1 p-4 md:p-8 md:ml-[var(--sidebar-width)]">
          <div className="reading-surface bg-white rounded-2xl p-5 md:p-10 min-h-[calc(100vh-140px)]">
            {searchQuery.trim() ? <SearchResults query={searchQuery} searchUrl={manifest.searchUrl} onSelect={(id, n) => navigate(id, n, searchQuery.trim())} />
              : error ? <div role="alert" className="p-8"><h1 className="text-2xl mb-4">Something needs attention</h1><p>{error}</p><button className="mt-4 underline" onClick={() => { setError(""); setRetry(n => n + 1); }}>Try again</button></div>
              : currentSummary && !currentCourse ? <p role="status" className="p-12 text-center">Loading collection…</p>
              : currentChapter && currentCourse ? <ChapterContent key={`${currentCourse.id}:${currentChapter.number}`} chapter={currentChapter} course={currentCourse} onNavigate={navigate} highlightQuery={highlightQuery} readingSize={readingSize} onReadingSizeChange={changeReadingSize} />
              : currentCourse ? <CourseWelcome course={currentCourse} onStart={() => { const first = currentCourse.modules[0]?.chapters[0]; if (first) navigate(currentCourse.id, first.number); }} />
              : <SiteWelcome manifest={visibleManifest} shelf={shelf} allCollections={manifest.courses} onShelfChange={changeShelf} onSelectCourse={navigate} />}
          </div>
        </main>
      </div>
    </div>
  );
}
