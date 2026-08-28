// Deterministic animation: clips only the original raster artwork, never redraws it.
import fs from 'node:fs/promises';
import path from 'node:path';
import {createRequire} from 'node:module';
import {spawn} from 'node:child_process';
import {once} from 'node:events';
const require=createRequire(process.env.RUNTIME_NODE_MODULES+'/package.json');
const sharp=require('sharp');
const root=process.cwd(),out=path.join(root,'public/presentations/artwork-pilot');
await fs.mkdir(out,{recursive:true});
const original=await fs.readFile('courses/Visual Course 01/diagrams/01-agent-architecture.png');
await fs.writeFile(path.join(out,'original.png'),original);
const uri='data:image/png;base64,'+original.toString('base64');
const fps=15,duration=75;
const clamp=x=>Math.max(0,Math.min(1,x));
const ease=x=>{x=clamp(x);return x*x*(3-2*x)};
const lerp=(a,b,t)=>a+(b-a)*ease(t);
const blocks=[
 {id:'person',x:165,start:0,end:10,p:'110,282 235,282 241,495 304,537 304,651 22,651 22,537 110,495'},
 {id:'app',x:485,start:6.5,end:15.4,p:'346,285 610,285 638,550 638,694 337,694'},
 {id:'tools',x:825,start:15.4,end:25.5,p:'695,330 952,330 952,536 986,555 986,698 651,698 651,555 695,530'},
 {id:'agents',x:1165,start:25.5,end:37.5,p:'1026,286 1258,286 1311,550 1311,698 1006,698'},
 {id:'policy',x:1490,start:37.5,end:52.3,p:'1324,287 1638,287 1660,550 1660,703 1320,703'}
];
const titles=[['FOLLOW THE REQUEST',0],['A request is not permission',6.5],['MCP: facts come back',15.4],['A2A: delegate a bounded task',25.5],['Policy controls the change',37.5],['Return evidence to the person',52.3],['One possible route — not a required sequence',62.8]];
const sprites={};
async function sprite(id,box,d){
 const [left,top,width,height]=box;
 let pipeline=sharp(original).extract({left,top,width,height}).ensureAlpha();
 if(d){const mask=Buffer.from(`<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="${left} ${top} ${width} ${height}"><path fill="white" fill-rule="evenodd" d="${d}"/></svg>`);pipeline=pipeline.composite([{input:mask,blend:'dest-in'}]);}
 const data=await pipeline.png().toBuffer();
 sprites[id]=`<image x="${left}" y="${top}" width="${width}" height="${height}" href="data:image/png;base64,${data.toString('base64')}"/>`;
}
for(const [i,b] of blocks.entries()){
 const points=b.p.split(' ').map(p=>p.split(',').map(Number)),xs=points.map(p=>p[0]),ys=points.map(p=>p[1]);
 const left=Math.min(...xs),top=Math.min(...ys);
 await sprite(b.id,[left,top,Math.max(...xs)-left,Math.max(...ys)-top],`M${b.p.replaceAll(' ',' L')} Z`);
 await sprite('label'+i,[[55,340,690,1040,1340][i],150,[235,290,275,240,300][i],97]);
}
await sprite('receipt',[1510,470,115,169],'M1536 473 L1612 497 L1619 591 L1590 620 L1520 598 L1515 491 Z');
const esc=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;');
function pill(x,y,text,color='#35dadd'){const w=Math.max(170,text.length*14+42);return `<g transform="translate(${x-w/2} ${y})"><rect width="${w}" height="48" rx="15" fill="#0b2541" stroke="${color}" stroke-width="2"/><text x="${w/2}" y="32" text-anchor="middle" fill="${color}" font-size="24" font-weight="700">${esc(text)}</text></g>`}
function packet(x,y,label,color='#35dadd'){return `<g transform="translate(${x} ${y})"><circle r="20" fill="${color}" opacity=".12"/><circle r="9" fill="${color}"/>${label?pill(0,-75,label,color):''}</g>`}
function frame(t){
 const final=t>=58;
 let body='';
 for(const [i,b] of blocks.entries()){
  const active=(t>=b.start&&t<b.end)||final;
  const enter=ease((t-i*.45)/1.2);
  const scale=active?1+.015*Math.sin(t*2):1;
  const dy=(1-enter)*42+(active?-7*Math.sin(t*2):0);
  body+=`<g opacity="${enter*(active?1:.25)}" transform="translate(${b.x} 510) scale(${scale}) translate(${-b.x} ${-510+dy})">${sprites[b.id]}</g>`;
  // Original labels remain original pixels, not generated lettering.
  body+=`<g opacity="${active?1:.42}">${sprites['label'+i]}</g>`;
 }
 const title=titles.filter(x=>t>=x[1]).at(-1)[0];
 let lines='';
 for(const [a,b,begin,end] of [[295,363,6.5,10],[610,693,15.4,20],[960,1042,25.5,30],[1250,1354,37.5,45]]){
  const active=t>=begin&&t<end;
  lines+=`<path d="M${a} 446 H${b}" stroke="#35dadd" stroke-width="5" opacity="${active?.9:.15}" marker-end="url(#arrow)"/>`;
 }
 if(t>=1&&t<6.5)body+=pill(320,710,'Late shipment. Credit?');
 if(t>=6.5&&t<10)body+=packet(lerp(220,460,(t-6.5)/3.3),446,'Request');
 if(t>=10&&t<15.4){body+=pill(480,710,'Find facts → check terms');body+=pill(900,795,'Planning ≠ permission','#9dc9ff');}
 if(t>=15.4&&t<20){body+=packet(lerp(500,820,(t-15.4)/3),446,'Read request');body+=pill(820,710,'Shipment + contract');}
 if(t>=20&&t<22.8)body+=packet(lerp(820,480,(t-20)/2.8),735,'Facts returned');
 if(t>=22.8&&t<25.5)body+=pill(820,740,'Read permission checked','#9dc9ff');
 if(t>=25.5&&t<30.8){body+=`<path d="M490 732 Q820 865 1160 728" fill="none" stroke="#35dadd" stroke-width="4" stroke-dasharray="9 9" stroke-dashoffset="${-t*35}"/>`;body+=packet(lerp(490,1160,(t-25.5)/4.6),760,'Assessment task');}
 if(t>=30.8&&t<37.5){body+=pill(1150,735,t<33?'Assessing…':'Recommendation');if(t>=34.9)body+=pill(750,808,'Not an automatic payment','#ffd291');}
 if(t>=37.5&&t<52.3){
  const rejected=t>=45.65&&t<48.8,color=rejected?'#ff927a':'#35dadd';
  body+=`<path d="M1324 365 V690" stroke="${color}" stroke-width="8"/><circle cx="1324" cy="446" r="25" fill="#0b2541" stroke="${color}" stroke-width="4"/>`;
  body+=pill(1150,710,rejected?'$900 · APPROVAL NEEDED':t<45.65?'$340 · within $500 limit':'Authorization checked',color);
  body+=pill(1470,796,'Fictional example','#9dc9ff');
  if(t>=41&&t<45.65)body+=packet(lerp(1175,1300,(t-41)/3),446,'$340');
  if(t>=45.65&&t<48.8)body+=packet(1290,446,'$900 · STOP','#ff927a');
  if(t>=48.8)body+=packet(lerp(1324,1488,(t-48.8)/2.8),446,'Authorized');
 }
 if(t>=52.3){
  const q=ease((t-52.3)/5.3),x=1535+(180-1535)*q,y=570+195*Math.sin(Math.PI*q);
  body+=`<path d="M1500 698 V771 Q1500 790 1470 790 H198 Q168 790 168 760 V682" fill="none" stroke="#35dadd" opacity=".75" stroke-width="5" stroke-dasharray="9 12" stroke-dashoffset="${-t*55}" marker-end="url(#arrow)"/>`;
  body+=`<g transform="translate(${x-1540} ${y-520})">${sprites.receipt}</g>`;
  if(t<62.8)body+=pill(830,827,'Receipt + evidence returned');
 }
 if(t>=68.8)body+=pill(835,827,t<70.2?'Useful work':t<71.9?'Controlled actions':'Evidence');
 return `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1280" height="720" viewBox="0 0 1672 941"><defs><marker id="arrow" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6" fill="none" stroke="#35dadd" stroke-width="1.6"/></marker></defs><rect width="1672" height="941" fill="#031126"/><g font-family="Arial, sans-serif"><text x="835" y="75" text-anchor="middle" fill="#e6f4ff" font-size="38" font-weight="700">${esc(title)}</text><text x="835" y="113" text-anchor="middle" fill="#86aecb" font-size="19">ORIGINAL ARTICLE ARTWORK · ANIMATED PILOT</text>${lines}${body}<text x="42" y="919" fill="#668bab" font-size="17">Course 01 · Agent Architecture</text><text x="1630" y="919" text-anchor="end" fill="#668bab" font-size="17">${Math.floor(t)} / 75 s</text></g></svg>`;
}
const proc=spawn('ffmpeg',['-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1280x720','-r',String(fps),'-i','pipe:0','-i',path.join(out,'narration.wav'),'-af','apad','-t',String(duration),'-c:v','libx264','-preset','veryfast','-crf','21','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k','-movflags','+faststart',path.join(out,'original-artwork-pilot.mp4')],{stdio:['pipe','inherit','inherit']});
const done=once(proc,'close');
for(let n=0;n<duration*fps;n++){
 const svg=frame(n/fps);
 const raster=sharp(Buffer.from(svg));
 if([0,135,315,465,698,818,1050].includes(n))await raster.clone().png().toFile(path.join(root,'.slide-build/lesson-01',`artwork-check-${n}.png`));
 const pixels=await raster.removeAlpha().raw().toBuffer();
 if(!proc.stdin.write(pixels))await once(proc.stdin,'drain');
 if(n%(fps*5)===0)console.log(`Rendered ${n/fps} / ${duration}s`);
}
proc.stdin.end();const [code]=await done;if(code!==0)throw Error(`ffmpeg: ${code}`);
console.log('Finished original-artwork-pilot.mp4');
