export interface ChapterSummary {
  number: number;
  slug: string;
  title: string;
}

export interface Chapter extends ChapterSummary {
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
  id: string;
  slug: string;
  title: string;
  subtitle: string;
  icon: string;
  chaptersCount: number;
  modules: ModuleSummary[];
}

export interface CourseData {
  id: string;
  slug: string;
  title: string;
  subtitle: string;
  icon?: string;
  chaptersCount: number;
  modules: Module[];
}

export interface SiteManifest {
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
