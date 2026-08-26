"use client";

import { CourseData, CourseSummary, SiteManifest } from "@/lib/types";
import { cn } from "@/lib/utils";

interface SiteWelcomeProps {
  manifest: SiteManifest;
  completedByCourse: Record<string, number[]>;
  completedTotal: number;
  totalChapters: number;
  onSelectCourse: (id: string) => void;
}

export function SiteWelcome({
  manifest,
  completedByCourse,
  completedTotal,
  totalChapters,
  onSelectCourse,
}: SiteWelcomeProps) {
  const overallProgress = totalChapters > 0 ? Math.round((completedTotal / totalChapters) * 100) : 0;

  return (
    <div className="welcome-screen text-center py-12">
      <div className="welcome-icon text-6xl mb-5">🎓</div>
      <h1 className="text-3xl md:text-4xl font-serif text-primary mb-4">
        {manifest.siteTitle}
      </h1>
      <p className="subtitle text-lg text-gray-500 mb-6 max-w-2xl mx-auto">
        {manifest.siteSubtitle}
      </p>

      <div className="course-stats flex justify-center gap-6 mb-8 flex-wrap">
        <div className="stat-box text-center px-8 py-5 bg-gray-100 rounded-xl">
          <span className="number block text-3xl font-bold text-primary">
            {manifest.courses.length}
          </span>
          <span className="label text-sm text-gray-500">Courses</span>
        </div>
        <div className="stat-box text-center px-8 py-5 bg-gray-100 rounded-xl">
          <span className="number block text-3xl font-bold text-primary">
            {totalChapters}
          </span>
          <span className="label text-sm text-gray-500">Diagrams</span>
        </div>
      </div>

      <div className="w-full max-w-xl mx-auto mb-10">
        <div className="flex items-center justify-between text-sm text-gray-500 mb-2">
          <span>Overall progress</span>
          <span>{overallProgress}%</span>
        </div>
        <div className="w-full h-3 bg-gray-200 rounded-full overflow-hidden">
          <div
            className="h-full bg-secondary rounded-full transition-all duration-300"
            style={{ width: `${overallProgress}%` }}
          />
        </div>
        <p className="text-sm text-gray-400 mt-2">
          {completedTotal} of {totalChapters} completed
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto text-left">
        {manifest.courses.map((course) => (
          <CourseCard
            key={course.id}
            course={course}
            completed={(completedByCourse[course.id] || []).length}
            onStart={() => onSelectCourse(course.id)}
          />
        ))}
      </div>
    </div>
  );
}

interface CourseCardProps {
  course: CourseSummary;
  completed: number;
  onStart: () => void;
}

function CourseCard({ course, completed, onStart }: CourseCardProps) {
  const progress = course.chaptersCount > 0 ? Math.round((completed / course.chaptersCount) * 100) : 0;

  return (
    <div className="bg-white rounded-2xl shadow p-6 border border-gray-100 hover:shadow-lg transition-shadow">
      <div className="flex items-start gap-4 mb-4">
        <span className="text-3xl">{course.icon}</span>
        <div className="flex-1">
          <h3 className="text-xl font-serif font-bold text-gray-900 mb-1">
            {course.title}
          </h3>
          <p className="text-sm text-gray-500">{course.modules.length} modules • {course.chaptersCount} diagrams</p>
        </div>
      </div>
      <p className="text-gray-600 text-sm mb-4 line-clamp-3">{course.subtitle}</p>
      <div className="mb-4">
        <div className="flex items-center justify-between text-xs text-gray-500 mb-1">
          <span>Progress</span>
          <span>{progress}%</span>
        </div>
        <div className="w-full h-2 bg-gray-100 rounded-full overflow-hidden">
          <div
            className="h-full bg-primary rounded-full transition-all duration-300"
            style={{ width: `${progress}%` }}
          />
        </div>
      </div>
      <button
        onClick={onStart}
        className="w-full py-2.5 bg-secondary hover:bg-secondary-dark text-white rounded-lg font-semibold transition-colors"
      >
        Start Course
      </button>
    </div>
  );
}

interface CourseWelcomeProps {
  course: CourseData;
  completed: number[];
  onStart: () => void;
}

export function CourseWelcome({ course, completed, onStart }: CourseWelcomeProps) {
  const progress = course.chaptersCount > 0 ? Math.round((completed.length / course.chaptersCount) * 100) : 0;

  return (
    <div className="welcome-screen text-center py-12">
      <div className="welcome-icon text-5xl mb-4">{course.icon || "📚"}</div>
      <h1 className="text-3xl md:text-4xl font-serif text-primary mb-4">
        {course.title}
      </h1>
      <p className="subtitle text-lg text-gray-500 mb-8 max-w-2xl mx-auto">
        {course.subtitle}
      </p>
      <div className="course-stats flex justify-center gap-6 mb-8 flex-wrap">
        <div className="stat-box text-center px-8 py-5 bg-gray-100 rounded-xl">
          <span className="number block text-3xl font-bold text-primary">
            {course.modules.length}
          </span>
          <span className="label text-sm text-gray-500">Modules</span>
        </div>
        <div className="stat-box text-center px-8 py-5 bg-gray-100 rounded-xl">
          <span className="number block text-3xl font-bold text-primary">
            {course.chaptersCount}
          </span>
          <span className="label text-sm text-gray-500">Diagrams</span>
        </div>
      </div>

      <div className="w-full max-w-xl mx-auto mb-10">
        <div className="flex items-center justify-between text-sm text-gray-500 mb-2">
          <span>Course progress</span>
          <span>{progress}%</span>
        </div>
        <div className="w-full h-3 bg-gray-200 rounded-full overflow-hidden">
          <div
            className="h-full bg-secondary rounded-full transition-all duration-300"
            style={{ width: `${progress}%` }}
          />
        </div>
        <p className="text-sm text-gray-400 mt-2">
          {completed.length} of {course.chaptersCount} completed
        </p>
      </div>

      <button
        onClick={onStart}
        className="start-btn inline-flex items-center gap-2 px-8 py-4 bg-secondary hover:bg-secondary-dark text-white rounded-xl font-semibold text-lg transition-all hover:-translate-y-0.5 shadow-lg hover:shadow-xl"
      >
        Start Learning →
      </button>

      <div className="mt-12 max-w-3xl mx-auto text-left">
        <h2 className="text-xl font-serif font-bold text-gray-900 mb-4 text-center">Modules</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {course.modules.map((m) => (
            <div
              key={m.number}
              className="flex items-center gap-3 p-4 bg-gray-50 rounded-xl"
            >
              <span className="text-2xl">{m.icon}</span>
              <div>
                <p className="font-semibold text-gray-900 text-sm">{m.title}</p>
                <p className="text-xs text-gray-500">{m.chapters.length} diagrams</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
