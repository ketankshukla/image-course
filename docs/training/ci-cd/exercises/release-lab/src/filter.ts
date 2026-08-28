export type Category = 'all' | 'course' | 'case-study';
export type Lesson = { title: string; category: Exclude<Category, 'all'> };

// Deliberately incomplete: this compiles, but ignores the selected category.
export function filterLessons(lessons: Lesson[], category: Category): Lesson[] {
  return lessons;
}
