"use client";

import { useEffect, useRef } from "react";
import { CourseSummary, ModuleSummary, ChapterSummary, SiteManifest } from "@/lib/types";
import { cn } from "@/lib/utils";

interface SidebarProps {
  manifest: SiteManifest;
  open: boolean;
  currentCourseId: string | null;
  currentChapterNumber: number | null;
  expandedCourses: Set<string>;
  expandedModules: Record<string, Set<number>>;
  completedByCourse: Record<string, number[]>;
  searchQuery: string;
  onSearch: (query: string) => void;
  onToggleCourse: (id: string) => void;
  onToggleModule: (courseId: string, moduleNumber: number) => void;
  onSelectChapter: (courseId: string, chapterNumber: number) => void;
  onCloseSidebar: () => void;
}

export default function Sidebar({
  manifest,
  open,
  currentCourseId,
  currentChapterNumber,
  expandedCourses,
  expandedModules,
  completedByCourse,
  searchQuery,
  onSearch,
  onToggleCourse,
  onToggleModule,
  onSelectChapter,
  onCloseSidebar,
}: SidebarProps) {
  const totalChapters = manifest.courses.reduce((a, c) => a + c.chaptersCount, 0);

  return (
    <aside
      className={cn(
        "sidebar fixed top-[60px] left-0 bottom-0 z-40 bg-white border-r border-gray-200 overflow-y-auto transition-transform duration-300",
        "w-[var(--sidebar-width)]",
        open ? "translate-x-0" : "-translate-x-full",
        "md:translate-x-0"
      )}
    >
      <div className="sidebar-header p-6 bg-gradient-to-r from-primary-light to-primary text-white">
        <h2 className="text-lg font-bold mb-1">🎓 Course Navigation</h2>
        <p className="text-sm opacity-90">
          {manifest.courses.length} Courses • {totalChapters} Diagrams
        </p>
      </div>
      <SearchBox query={searchQuery} onSearch={onSearch} />
      <nav className="py-4">
        {manifest.courses.map((course) => (
          <CourseGroup
            key={course.id}
            course={course}
            currentCourseId={currentCourseId}
            currentChapterNumber={currentChapterNumber}
            expanded={expandedCourses.has(course.id)}
            expandedModules={expandedModules[course.id] || new Set()}
            completed={completedByCourse[course.id] || []}
            onToggle={() => onToggleCourse(course.id)}
            onToggleModule={(moduleNumber) => onToggleModule(course.id, moduleNumber)}
            onSelectChapter={onSelectChapter}
            onCloseSidebar={onCloseSidebar}
          />
        ))}
      </nav>
    </aside>
  );
}

function SearchBox({
  query,
  onSearch,
}: {
  query: string;
  onSearch: (query: string) => void;
}) {
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (inputRef.current && typeof window !== "undefined" && window.innerWidth >= 768) {
      inputRef.current.focus();
    }
  }, []);

  return (
    <div className="px-5 py-3 border-b border-gray-200">
      <div className="relative">
        <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 text-sm">🔍</span>
        <input
          ref={inputRef}
          type="text"
          value={query}
          onChange={(e) => onSearch(e.target.value)}
          placeholder="Find a diagram..."
          className="w-full pl-9 pr-9 py-2 text-sm border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent"
        />
        {query && (
          <button
            onClick={() => onSearch("")}
            className="absolute right-2 top-1/2 -translate-y-1/2 w-6 h-6 flex items-center justify-center text-gray-400 hover:text-gray-600 hover:bg-gray-100 rounded-full transition-colors"
            aria-label="Clear search"
          >
            ✕
          </button>
        )}
      </div>
    </div>
  );
}

interface CourseGroupProps {
  course: CourseSummary;
  currentCourseId: string | null;
  currentChapterNumber: number | null;
  expanded: boolean;
  expandedModules: Set<number>;
  completed: number[];
  onToggle: () => void;
  onToggleModule: (moduleNumber: number) => void;
  onSelectChapter: (courseId: string, chapterNumber: number) => void;
  onCloseSidebar: () => void;
}

function CourseGroup({
  course,
  currentCourseId,
  currentChapterNumber,
  expanded,
  expandedModules,
  completed,
  onToggle,
  onToggleModule,
  onSelectChapter,
  onCloseSidebar,
}: CourseGroupProps) {
  const progress = course.chaptersCount > 0 ? Math.round((completed.length / course.chaptersCount) * 100) : 0;
  const isCurrent = currentCourseId === course.id;

  return (
    <div className={cn("course-group", expanded && "expanded")}>
      <button
        onClick={onToggle}
        className={cn(
          "course-header flex items-center justify-between w-full text-left px-5 py-3 transition-colors border-0 cursor-pointer",
          isCurrent ? "bg-primary/10 hover:bg-primary/20" : "bg-gray-50 hover:bg-gray-100"
        )}
      >
        <span className="flex items-center gap-2 flex-1 min-w-0">
          <span className="text-xl">{course.icon}</span>
          <span className="font-semibold text-sm text-gray-900 truncate">
            {course.title}
          </span>
        </span>
        <span className="text-xs text-gray-500 ml-2">{progress}%</span>
        <span
          className={cn(
            "chevron text-xs text-gray-500 transition-transform duration-300 ml-2",
            expanded && "rotate-90"
          )}
        >
          ▶
        </span>
      </button>
      <div
        className="course-modules overflow-hidden transition-all duration-300 bg-white border-l-4 border-gray-100"
        style={{ maxHeight: expanded ? "2000px" : "0" }}
      >
        {course.modules.map((module) => (
          <ModuleGroup
            key={module.number}
            course={course}
            module={module}
            currentCourseId={currentCourseId}
            currentChapterNumber={currentChapterNumber}
            expanded={expandedModules.has(module.number)}
            completed={completed}
            onToggle={() => onToggleModule(module.number)}
            onSelectChapter={onSelectChapter}
            onCloseSidebar={onCloseSidebar}
          />
        ))}
      </div>
    </div>
  );
}

interface ModuleGroupProps {
  course: CourseSummary;
  module: ModuleSummary;
  currentCourseId: string | null;
  currentChapterNumber: number | null;
  expanded: boolean;
  completed: number[];
  onToggle: () => void;
  onSelectChapter: (courseId: string, chapterNumber: number) => void;
  onCloseSidebar: () => void;
}

function ModuleGroup({
  course,
  module,
  currentCourseId,
  currentChapterNumber,
  expanded,
  completed,
  onToggle,
  onSelectChapter,
  onCloseSidebar,
}: ModuleGroupProps) {
  return (
    <div className={cn("module-group", expanded && "expanded")}>
      <button
        onClick={onToggle}
        className="module-header flex items-center justify-between w-full text-left pl-5 pr-4 py-2.5 bg-white hover:bg-gray-50 transition-colors border-0 cursor-pointer"
      >
        <span className="flex items-center gap-2 flex-1 min-w-0">
          <span className="text-base">{module.icon}</span>
          <span className="font-semibold text-sm text-gray-800 truncate">
            {module.title}
          </span>
        </span>
        <span
          className={cn(
            "chevron text-xs text-gray-400 transition-transform duration-300 ml-2",
            expanded && "rotate-90"
          )}
        >
          ▶
        </span>
      </button>
      <div
        className="module-chapters overflow-hidden transition-all duration-300 bg-white"
        style={{ maxHeight: expanded ? "1500px" : "0" }}
      >
        {module.chapters.map((chapter) => {
          const isActive = currentCourseId === course.id && currentChapterNumber === chapter.number;
          const isCompleted = completed.includes(chapter.number);
          return (
            <a
              key={chapter.number}
              href={`#course=${course.id}&chapter=${chapter.number}`}
              onClick={(e) => {
                e.preventDefault();
                onSelectChapter(course.id, chapter.number);
                if (typeof window !== "undefined" && window.innerWidth <= 768) {
                  onCloseSidebar();
                }
              }}
              className={cn(
                "chapter-link flex items-center gap-3 pl-12 pr-4 py-2 text-sm text-gray-700 no-underline transition-colors border-l-[3px] border-transparent hover:bg-gray-100 hover:text-primary",
                isActive && "bg-primary/10 text-primary border-l-primary font-semibold",
                isCompleted && "completed"
              )}
            >
              <span className="chapter-number text-xs text-gray-500 min-w-[24px]">
                {chapter.number.toString().padStart(2, "0")}
              </span>
              <span className="truncate">{chapter.title}</span>
              {isCompleted && (
                <span className="ml-auto text-secondary text-sm">✓</span>
              )}
            </a>
          );
        })}
      </div>
    </div>
  );
}
