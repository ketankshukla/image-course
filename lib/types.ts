export interface ChapterSummary {
  number: number;
  slug: string;
  title: string;
}

export interface Chapter extends ChapterSummary {
  toc?: { id: string; title: string }[];
  imageWidth?: number;
  imageHeight?: number;
  fullTitle: string;
  image: string;
  imageAlt: string;
  moduleNumber: number;
  moduleTitle: string;
  role: string;
  layout: string;
  readTime: number;
  body: string;
  prev: number | null;
  next: number | null;
}

export interface ModuleSummary {
  number: number;
  title: string;
  icon: string;
  chapters: ChapterSummary[];
}

export interface Module extends ModuleSummary {
  chapters: Chapter[];
}

export interface CourseSummary {
  kind: "course" | "case-study" | "guide";
  dataUrl: string;
  id: string;
  slug: string;
  title: string;
  subtitle: string;
  icon: string;
  chaptersCount: number;
  modules: ModuleSummary[];
}

export interface CourseData {
  kind: "course" | "case-study" | "guide";
  id: string;
  slug: string;
  title: string;
  subtitle: string;
  icon?: string;
  chaptersCount: number;
  modules: Module[];
}

export interface SiteManifest {
  searchUrl: string;
  siteTitle: string;
  siteSubtitle: string;
  courses: CourseSummary[];
}

export interface SearchIndexEntry {
  courseId: string;
  courseTitle: string;
  courseIcon: string;
  courseSubtitle: string;
  moduleTitle: string;
  chapterNumber: number;
  chapterTitle: string;
  number: number;
  plainText: string;
  snippet: string;
}
