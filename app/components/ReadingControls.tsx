"use client";

export default function ReadingControls({ size, onChange }: { size: number; onChange: (size: number) => void }) {
  return <div className="reading-controls">
    <span>Make yourself comfortable</span>
    <fieldset>
      <legend className="sr-only">Reading text size</legend>
      <span aria-hidden="true">Text size</span>
      {[22, 24, 28].map(value => <button key={value} type="button" aria-label={`${value} pixel body text`} aria-pressed={size === value} onClick={() => onChange(value)}>{value}</button>)}
    </fieldset>
  </div>;
}
