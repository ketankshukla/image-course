# Agent Architecture — Presentation Review Package

Course 1, Lesson 1 adapted into 15 slides with 1,795 spoken words. A synchronized MP4 now accompanies the slide package, using the installed Microsoft Zira Desktop synthetic English voice. There is no on-screen presenter. The original script estimate was 13–15 minutes; the video's measured timing is recorded alongside the MP4.

- [Watch the narrated video](https://course.ketanshukla.dev/presentations/course-01-lesson-01-video.html)
- [Download MP4](https://course.ketanshukla.dev/presentations/course-01-lesson-01.mp4)

To rebuild on Windows, install FFmpeg, retain the final slide PNGs in `.slide-build/lesson-01`, then run `pwsh -File scripts/render_lesson_video.ps1`. This speaks each narration and holds its slide through the complete audio, with a short gap between slides and extra thinking time at the checkpoint. `public/presentations/course-01-lesson-01-timing.json` supplies the chapter shortcuts.

- [Review slides and narration together](SLIDES-AND-NARRATION.html)
- [Editable PowerPoint with narration in speaker notes](AGENT-ARCHITECTURE.pptx)
- [Narration script](NARRATION-SCRIPT.md)
- [Website review edition](https://course.ketanshukla.dev/presentations/course-01-lesson-01.html)

The original diagrams remain embedded and unchanged. Text and the simple retry diagram are editable PowerPoint objects. The fictional Northwind Freight story is identified as a teaching scenario, not a measured deployment. Protocol references are in the narration script and speaker notes.

The review edition shows every final slide with its narration below it. Use “Show slides only” to evaluate the visual pacing separately. Visual cues are optional production directions, not words to be spoken.

`slides.json` is the structured content source. Authoring and QA intermediates are kept outside the deliverables in the ignored `.slide-build/lesson-01` folder. The public HTML contains flattened WebP previews and does not require any model credentials or external image requests.
