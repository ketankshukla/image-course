"use client";

import { CourseData, CourseSummary, SiteManifest } from "@/lib/types";

const labels = { course: "Courses", "case-study": "Case Studies", guide: "Library Guides" };
const descriptions = {
  course: "Understand the concepts through 244 diagrams across ten visual courses.",
  "case-study": "Follow one complete project from plain-English explanation to architecture, tests and build workbooks.",
  guide: "Understand the workspace and learn how to add the next case study."
};

export function SiteWelcome({ manifest, shelf, allCollections, onShelfChange, onSelectCourse }: {
  manifest: SiteManifest; shelf: CourseSummary["kind"]; allCollections: CourseSummary[];
  onShelfChange: (kind: CourseSummary["kind"]) => void;
  onSelectCourse: (id: string) => void;
}) {
  return <div className="py-4 md:py-8">
    <p className="text-xs font-semibold tracking-widest uppercase text-primary mb-3">Your agent engineering bookshelf</p>
    <h1 className="text-3xl md:text-4xl font-serif mb-4">{manifest.siteTitle}</h1>
    <p className="text-gray-500 text-lg max-w-3xl mb-8">{manifest.siteSubtitle}</p>
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-3 mb-10">
      {(Object.keys(labels) as CourseSummary["kind"][]).map((kind, i) => <button key={kind} onClick={() => onShelfChange(kind)} aria-pressed={kind === shelf}
        className={`text-left rounded-xl border p-5 transition-colors ${kind === shelf ? "border-primary bg-primary/10" : "border-gray-200 hover:bg-gray-50"}`}>
        <span className="text-xs uppercase tracking-wide text-primary">{i === 0 ? "01 · Learn" : i === 1 ? "02 · Apply" : "03 · Extend"}</span>
        <span className="block text-lg font-semibold mt-1">{labels[kind]}</span>
        <span className="block text-sm text-gray-500 mt-1">{allCollections.filter(c => c.kind === kind).length} {kind === "guide" ? "collection" : "collections"}</span>
      </button>)}
    </div>
    <div className="flex flex-wrap items-end justify-between gap-3 mb-6">
      <div><h2 className="text-2xl font-serif mb-2">{labels[shelf]}</h2><p className="text-gray-500 max-w-2xl">{descriptions[shelf]}</p></div>
    </div>
    <div className="grid grid-cols-1 xl:grid-cols-2 gap-5">
      {manifest.courses.map(course => <div key={course.id} className="rounded-xl border border-gray-200 p-6 hover:border-primary transition-colors">
        <div className="flex gap-3 items-start mb-3"><span className="text-3xl">{course.icon}</span><h3 className="font-serif text-xl">{course.title}</h3></div>
        <p className="text-gray-500 mb-4">{course.subtitle}</p>
        <p className="text-xs text-gray-500 mb-4">{course.modules.length} {course.kind === "course" ? "modules" : "sections"} · {course.chaptersCount} {course.kind === "course" ? "lessons" : "guides"}</p>
        <button className="rounded-lg bg-primary text-white font-semibold px-5 py-3 hover:bg-primary-dark" onClick={() => onSelectCourse(course.id)}>Explore {course.kind === "course" ? "course" : "collection"} →</button>
      </div>)}
    </div>
  </div>;
}

export function CourseWelcome({ course, onStart }: { course: CourseData; onStart: () => void }) {
  return <div className="py-6">
    <p className="uppercase tracking-widest text-xs text-primary mb-3">{labels[course.kind]}</p>
    <h1 className="text-3xl md:text-4xl font-serif mb-4">{course.icon} {course.title}</h1>
    <p className="text-lg text-gray-500 max-w-3xl mb-5">{course.subtitle}</p>
    <p className="text-sm text-gray-500 mb-7">{course.chaptersCount} articles</p>
    {course.id === "hospital" && <p className="bg-amber-50 border border-amber-200 rounded-lg p-4 mb-6 text-sm">Synthetic learning case only. These guides do not describe a deployed clinical system or certify compliance.</p>}
    <button onClick={onStart} className="bg-primary text-white px-6 py-3 rounded-lg font-semibold mb-10">Start reading →</button>
    <div className="space-y-6">{course.modules.map(module => <section key={module.number}>
      <h2 className="font-serif text-xl mb-3">{module.icon} {module.title}</h2>
      <ul className="divide-y border rounded-xl">{module.chapters.map(chapter => <li key={chapter.number}>
        <a className="block p-4 hover:bg-gray-50 text-primary" href={`#course=${course.id}&chapter=${chapter.number}`}>{chapter.title} <span className="text-gray-400 text-xs ml-2">{chapter.readTime} min</span></a>
      </li>)}</ul>
    </section>)}</div>
  </div>;
}
