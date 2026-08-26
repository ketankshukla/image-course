"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { Chapter, CourseData } from "@/lib/types";
import { chapterByNumber, cn, highlightInHtml } from "@/lib/utils";

interface ChapterContentProps {
  chapter: Chapter;
  course: CourseData;
  completed: number[];
  onMarkComplete: (n: number) => void;
  onNavigate: (courseId: string, chapterNumber: number) => void;
  highlightQuery?: string;
}

export default function ChapterContent({
  chapter,
  course,
  completed,
  onMarkComplete,
  onNavigate,
  highlightQuery = "",
}: ChapterContentProps) {
  const map = chapterByNumber(course.modules);
  const prev = chapter.prev;
  const next = chapter.next;
  const rootRef = useRef<HTMLDivElement>(null);
  const bodyRef = useRef<HTMLDivElement>(null);
  const [matchIndex, setMatchIndex] = useState(0);

  const { highlightedHtml, matchCount } = useMemo(
    () => highlightInHtml(chapter.body, highlightQuery),
    [chapter.body, highlightQuery]
  );

  // Reset to the first match whenever the chapter or query changes.
  useEffect(() => {
    setMatchIndex(0);
  }, [chapter.body, highlightQuery]);

  // Mark the active hit and scroll it into view.
  useEffect(() => {
    if (!bodyRef.current || matchCount === 0) return;
    const marks = Array.from(
      bodyRef.current.querySelectorAll("mark.search-highlight")
    ) as HTMLElement[];

    marks.forEach((m, i) => m.classList.toggle("is-active", i === matchIndex));

    const active = marks[matchIndex];
    if (!active) return;

    let cancelled = false;
    const scroll = (behavior: ScrollBehavior) => {
      if (!cancelled) active.scrollIntoView({ behavior, block: "center" });
    };

    // Images above the body shift the layout as they load, so scroll again
    // once any pending image in the chapter has settled.
    const images = Array.from(
      rootRef.current?.querySelectorAll("img") ?? []
    ).filter((img) => !img.complete);

    scroll("smooth");

    if (images.length === 0) return;

    let remaining = images.length;
    const onSettled = () => {
      remaining -= 1;
      if (remaining === 0) scroll("auto");
    };
    images.forEach((img) => {
      img.addEventListener("load", onSettled, { once: true });
      img.addEventListener("error", onSettled, { once: true });
    });

    return () => {
      cancelled = true;
      images.forEach((img) => {
        img.removeEventListener("load", onSettled);
        img.removeEventListener("error", onSettled);
      });
    };
  }, [matchIndex, matchCount, highlightedHtml]);

  return (
    <div className="chapter-content" ref={rootRef}>
      <div className="chapter-header mb-10 pb-6 border-b-2 border-gray-200">
        <h1 className="text-2xl md:text-3xl font-serif text-gray-900 mb-2">
          {chapter.fullTitle}
        </h1>

        <figure className="hero-figure my-6">
          <img
            src={chapter.image}
            alt={chapter.imageAlt}
            className="w-full h-auto rounded-xl shadow-md"
          />
        </figure>

        <div className="chapter-meta flex flex-wrap items-center gap-3 mb-3">
          <span className="chapter-badge px-3 py-1 bg-primary text-white rounded-full text-xs font-semibold">
            Module {chapter.moduleNumber}: {chapter.moduleTitle}
          </span>
          <span className="chapter-time text-sm text-gray-500 flex items-center gap-1">
            📖 {chapter.readTime} min read
          </span>
        </div>
        {chapter.role && (
          <p className="chapter-intro text-gray-500 text-lg mb-1">
            {chapter.role}
          </p>
        )}
        {chapter.layout && (
          <p className="text-sm text-gray-400">
            <span className="font-semibold text-gray-500">Layout:</span>{" "}
            {chapter.layout}
          </p>
        )}
      </div>

      {matchCount > 0 && (
        <div className="match-nav sticky top-[70px] z-30 flex items-center gap-2 mb-6 px-3 py-2 bg-white rounded-lg border border-gray-200 shadow-sm">
          <button
            onClick={() => setMatchIndex((i) => (i - 1 + matchCount) % matchCount)}
            className="px-2 py-1 text-sm rounded text-gray-700 hover:bg-gray-100 hover:text-primary transition-colors"
          >
            ← Previous
          </button>
          <span className="text-sm text-gray-600 min-w-[110px] text-center">
            Match {matchIndex + 1} of {matchCount}
          </span>
          <button
            onClick={() => setMatchIndex((i) => (i + 1) % matchCount)}
            className="px-2 py-1 text-sm rounded text-gray-700 hover:bg-gray-100 hover:text-primary transition-colors"
          >
            Next →
          </button>
        </div>
      )}

      <div
        ref={bodyRef}
        className="content-body"
        dangerouslySetInnerHTML={{ __html: highlightedHtml }}
      />

      <div className="chapter-nav flex flex-col sm:flex-row justify-between mt-12 pt-8 border-t-2 border-gray-200 gap-3">
        {prev ? (
          <button
            onClick={() => onNavigate(course.id, prev)}
            className="nav-btn flex items-center justify-center gap-2 px-5 py-3 bg-gray-100 hover:bg-primary hover:text-white text-gray-700 rounded-lg font-medium transition-colors"
          >
            ← Previous
          </button>
        ) : (
          <span />
        )}
        {next ? (
          <button
            onClick={() => {
              onMarkComplete(chapter.number);
              onNavigate(course.id, next);
            }}
            className="nav-btn next flex items-center justify-center gap-2 px-5 py-3 bg-primary hover:bg-primary-dark text-white rounded-lg font-medium transition-colors"
          >
            Next: {map.get(next)?.title} →
          </button>
        ) : (
          <button
            onClick={() => onMarkComplete(chapter.number)}
            className={cn(
              "nav-btn next flex items-center justify-center gap-2 px-5 py-3 rounded-lg font-medium transition-colors",
              completed.includes(chapter.number)
                ? "bg-secondary text-white cursor-default"
                : "bg-primary hover:bg-primary-dark text-white"
            )}
          >
            {completed.includes(chapter.number)
              ? "Completed ✓"
              : "Mark Complete ✓"}
          </button>
        )}
      </div>
    </div>
  );
}
