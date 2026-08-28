import { filterLessons, type Category, type Lesson } from './filter.js';

const lessons: Lesson[] = [
  { title: 'MCP foundations', category: 'course' },
  { title: 'FilePilot', category: 'case-study' },
  { title: 'HarborCare', category: 'case-study' }
];
const picker = document.querySelector<HTMLSelectElement>('#category')!;
const list = document.querySelector<HTMLUListElement>('#results')!;
function render() {
  const selection = picker.value as Category;
  const items = filterLessons(lessons, selection).map(lesson => {
    const item = document.createElement('li');
    item.textContent = lesson.title;
    return item;
  });
  list.replaceChildren(...items);
}
picker.addEventListener('change', render);
render();
