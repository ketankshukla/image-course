"use client";

import { useEffect, useMemo, useState } from "react";
import { SearchIndexEntry } from "@/lib/types";
import { fuzzyMatch, buildSnippet, highlightMatches, cn } from "@/lib/utils";

interface ScoredResult extends SearchIndexEntry {
  score: number;
  occurrences: number;
}

interface SearchResultsProps {
  searchUrl: string;
  query: string;
  onSelect: (courseId: string, chapterNumber: number) => void;
}

export default function SearchResults({
  query,
  searchUrl,
  onSelect,
}: SearchResultsProps) {
  const [index, setIndex] = useState<SearchIndexEntry[] | null>(null);
  const [error, setError] = useState(false);
  const [attempt, setAttempt] = useState(0);

  useEffect(() => {
    let cancelled = false;
    setError(false);
    fetch(searchUrl)
      .then((res) => { if (!res.ok) throw Error("Search unavailable"); return res.json(); })
      .then((data: SearchIndexEntry[]) => {
        if (!cancelled) setIndex(data);
      })
      .catch((err) => {
        if (!cancelled) setError(true);
        console.error("Failed to load search index:", err);
      });
    return () => {
      cancelled = true;
    };
  }, [searchUrl, attempt]);

  const { results, totalMatches } = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q || !index) return { results: [] as ScoredResult[], totalMatches: 0 };

    const matches: ScoredResult[] = [];

    for (const entry of index) {
      let score = 0;

      const titleMatch = fuzzyMatch(q, entry.chapterTitle);
      const moduleMatch = fuzzyMatch(q, entry.moduleTitle);
      const courseMatch = fuzzyMatch(q, entry.courseTitle);
      const subtitleMatch = fuzzyMatch(q, entry.courseSubtitle);
      const numberMatch = fuzzyMatch(q, entry.number.toString());

      if (titleMatch) score += titleMatch.score * 4;
      if (moduleMatch) score += moduleMatch.score * 1.5;
      if (courseMatch) score += courseMatch.score * 1;
      if (subtitleMatch) score += subtitleMatch.score * 0.5;
      if (numberMatch) score += numberMatch.score * 5;

      const bodyLower = entry.plainText.toLowerCase();
      let occurrences = 0;
      let pos = bodyLower.indexOf(q);
      while (pos !== -1) {
        occurrences++;
        pos = bodyLower.indexOf(q, pos + q.length);
      }

      if (occurrences > 0) {
        score += 200 + occurrences * 30;
      }

      // Only keep results that have a real match (exact body, title/module fuzzy,
      // course/subtitle fuzzy, or chapter number). Drop weak body-only fuzzy matches.
      if (score >= 10) {
        matches.push({ ...entry, score, occurrences });
      }
    }

    const all = matches.sort((a, b) => b.score - a.score);
    return { results: all.slice(0, 30), totalMatches: all.length };
  }, [query, index]);

  if (error) return <div role="alert"><p>Search could not load.</p><button className="underline mt-3" onClick={() => setAttempt(a => a + 1)}>Retry search</button></div>;

  if (!index) {
    return (
      <div className="flex items-center justify-center h-64 text-gray-500">
        <div className="text-center">
          <div className="text-3xl mb-3">⏳</div>
          <p>Loading search index...</p>
        </div>
      </div>
    );
  }

  const q = query.trim();

  return (
    <div className="search-results">
      <h1 className="text-2xl md:text-3xl font-serif text-gray-900 mb-2">
        Search results
      </h1>
      <p className="text-gray-500 mb-6">
        {q
          ? `Found ${totalMatches} result${totalMatches === 1 ? "" : "s"} for “${q}”`
          : "Enter a term to search"}
      </p>

      {results.length === 0 ? (
        <div className="text-center py-16 text-gray-500">
          <div className="text-3xl mb-3">🔍</div>
          <p>No matching articles found.</p>
        </div>
      ) : (
        <ul className="space-y-4">
          {results.map((r) => (
            <li key={`${r.courseId}-${r.chapterNumber}`}>
              <a
                href={`#course=${r.courseId}&chapter=${r.chapterNumber}`}
                onClick={(e) => {
                  e.preventDefault();
                  onSelect(r.courseId, r.chapterNumber);
                }}
                className={cn(
                  "result-link block p-4 rounded-xl border border-gray-200 bg-white hover:bg-gray-50 hover:border-primary transition-colors no-underline group"
                )}
              >
                <div className="flex items-center gap-2 text-sm text-gray-500 mb-1">
                  <span>{r.courseIcon}</span>
                  <span className="truncate">{r.courseTitle}</span>
                  <span className="text-gray-300">/</span>
                  <span className="truncate">{r.moduleTitle}</span>
                </div>
                <div className="flex items-start gap-3 mb-2">
                  <span className="text-xs font-semibold text-primary bg-primary/10 px-2 py-0.5 rounded shrink-0">
                    {r.chapterNumber.toString().padStart(2, "0")}
                  </span>
                  <span
                    className="text-lg font-medium text-gray-900 group-hover:text-primary"
                    dangerouslySetInnerHTML={{
                      __html: highlightMatches(r.chapterTitle, q),
                    }}
                  />
                </div>
                <div className="text-xs text-gray-400 mb-2">
                  {r.occurrences} match{r.occurrences === 1 ? "" : "es"} in article
                </div>
                <p
                  className="text-sm text-gray-600 leading-relaxed"
                  dangerouslySetInnerHTML={{
                    __html: buildSnippet(r.plainText, q),
                  }}
                />
              </a>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
