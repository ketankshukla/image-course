import fs from 'node:fs/promises';
const paths=['docs/presentations/course-01/lesson-01/SLIDES-AND-NARRATION.html','public/presentations/course-01-lesson-01.html'];
for(const path of paths){
 let html=await fs.readFile(path,'utf8');
 html=html.replace('No voice recording, presenter or video has been generated.','A narrated video version is now available; no on-screen presenter is included.');
 if(!html.includes('Watch the narrated video'))html=html.replace('</header>','<p><a href="https://course.ketanshukla.dev/presentations/course-01-lesson-01-video.html">Watch the narrated video →</a></p></header>');
 await fs.writeFile(path,html);
}
