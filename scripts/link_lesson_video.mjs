import fs from 'node:fs/promises';
const paths=['docs/presentations/course-01/lesson-01/SLIDES-AND-NARRATION.html','public/presentations/course-01-lesson-01.html'];
for(const path of paths){
 let html=await fs.readFile(path,'utf8');
 html=html.replace('No voice recording, presenter or video has been generated.','A narrated video version is now available; no on-screen presenter is included.');
 if(!html.includes('Watch the narrated video'))html=html.replace('</header>','<p><a href="https://course.ketanshukla.dev/presentations/course-01-lesson-01-video.html">Watch the narrated video →</a></p></header>');
 await fs.writeFile(path,html);
}
for(const path of [...paths,'public/presentations/course-01-lesson-01-video.html']){
 let html=await fs.readFile(path,'utf8');
 if(!html.includes('original-artwork-pilot.html')){
  const link='<p><a href="https://course.ketanshukla.dev/presentations/original-artwork-pilot.html">New: watch the original artwork animation pilot →</a></p>';
  html=html.includes('</header>')?html.replace('</header>',link+'</header>'):html.replace('</h1>','</h1>'+link);
  await fs.writeFile(path,html);
 }
}
