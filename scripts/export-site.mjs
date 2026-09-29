// Publish an allowlisted static site. Never copy the WordPress installation.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { minify } from 'terser';
const out=path.resolve('dist');
fs.rmSync(out,{recursive:true,force:true});fs.mkdirSync(out,{recursive:true});
const copied=new Set();
function copy(file) {
 file=path.normalize(file);
 if (file.startsWith('..') || path.isAbsolute(file)) throw new Error(`Unsafe export path: ${file}`);
 if (copied.has(file)) return;
 if (!fs.existsSync(file) || !fs.statSync(file).isFile()) throw new Error(`Missing export dependency: ${file}`);
 if (/\.(php|sql|env)$/i.test(file) || file.startsWith('blog/')) throw new Error(`Forbidden export: ${file}`);
 copied.add(file);
 const dest=path.join(out,file);fs.mkdirSync(path.dirname(dest),{recursive:true});fs.copyFileSync(file,dest);
 if (/\.(html|css|js)$/.test(file)) {
  const text=fs.readFileSync(file,'utf8');
  const refs=[...text.matchAll(/(?:src|href|data-background)=["']([^"'#?]+)["']/g)].map(m=>m[1]);
  refs.push(...[...text.matchAll(/url\(["']?([^)'"?#]+)["']?\)/g)].map(m=>m[1]));
  // Deferred plugin URLs are explicit, not discoverable as script tags.
  if (file==='assets/js/main.js') refs.push('/assets/js/jquery-3.6.0.min.js','/assets/js/owl.carousel.min.js','/assets/js/jquery.magnific-popup.min.js','/assets/js/isotope.pkgd.min.js');
  for (const ref of refs) {
   if (/^(?:[a-z]+:|\/\/)/i.test(ref)) continue;
   const local=ref.startsWith('/')?ref.slice(1):path.join(path.dirname(file),ref);
   if (fs.existsSync(local) && fs.statSync(local).isFile()) copy(local);
  }
 }
}
const pages=[...fs.readFileSync('sitemap.xml','utf8').matchAll(/<loc>https:\/\/uslusurucukursu\.com([^<]*)<\/loc>/g)].map(m=>m[1].replace(/^\//,'')+'index.html');
for (const file of [...pages,'robots.txt','llms.txt','sitemap.xml','assets/img/og/uslu-og.jpg','8112ebbbc2e42aa3bdf1fc9431c1158a.txt','google05c43e8ce47e9840.html','assets/fonts/Barlow-OFL.txt']) copy(file);
for (const dir of ['qr','en/qr','e-sinav','en/e-sinav','whatsapp','galeri','en/gallery']) {
 // Public redirect tools are intentional; gallery content is already in sitemap.
 const candidate=path.join(dir,'index.html');if(fs.existsSync(candidate))copy(candidate);
 if(dir.endsWith('qr'))for(const entry of fs.readdirSync(dir,{withFileTypes:true}))if(entry.isDirectory()&&entry.name!=='error')copy(path.join(dir,entry.name,'index.html'));
}
// Designed 404 (TR, and EN under /en/). Copy collects its assets, then it is served
// only as /404.html: the source path itself is not published.
copy('error/404/index.html');
fs.renameSync(path.join(out,'error/404/index.html'),path.join(out,'404.html'));
fs.rmSync(path.join(out,'error'),{recursive:true,force:true});
// Performance (Lighthouse, 29.09.2026): the three savings it still reported.
// 1) Responsive images: an <img src="/x.webp"> gets srcset/sizes when x-480.webp or
//    x-800.webp exists beside it (made once with cwebp and committed). Phones then
//    download a copy close to their screen width instead of the 1024-1100px original.
// The designed 404 was renamed to 404.html above; every HTML pass reads it there.
const exportedHtml=()=>[...copied].map(f=>f==='error/404/index.html'?'404.html':f).filter(f=>f.endsWith('.html'));
const SIZES='(max-width: 767px) 100vw, 50vw';
let responsive=0;
for(const file of exportedHtml()){
 const dest=path.join(out,file);
 const html=fs.readFileSync(dest,'utf8').replace(/<img\b[^>]*>/g,(tag)=>{
  if(/\ssrcset=/.test(tag))return tag;
  const src=/\ssrc="(\/[^"?#]+)\.webp"/.exec(tag);
  const width=/\swidth="(\d+)"/.exec(tag);
  if(!src||!width)return tag;
  const set=[];
  for(const w of [480,800]){
   const v=`${src[1]}-${w}.webp`;
   if(w<Number(width[1])&&fs.existsSync(v.slice(1))){copy(v.slice(1));set.push(`${v} ${w}w`);}
  }
  if(!set.length)return tag;
  set.push(`${src[1]}.webp ${width[1]}w`);
  responsive++;
  return tag.replace(/\ssrc="/,` srcset="${set.join(', ')}" sizes="${SIZES}" src="`);
 });
 fs.writeFileSync(dest,html);
}
if(!responsive)throw new Error('Responsive image step matched nothing');
// 2) The contact form stylesheet is small and only on two pages: inline it so it no
//    longer blocks the first paint.
const formCss=fs.readFileSync('assets/css/iletisim-form.css','utf8').replace(/\/\*[\s\S]*?\*\//g,'').replace(/\s*\n\s*/g,'');
let inlined=0;
for(const file of exportedHtml()){
 const dest=path.join(out,file);
 const html=fs.readFileSync(dest,'utf8');
 if(!html.includes('<link href="/assets/css/iletisim-form.css" rel="stylesheet"/>'))continue;
 fs.writeFileSync(dest,html.replace('<link href="/assets/css/iletisim-form.css" rel="stylesheet"/>',`<style id="iletisim-form-css">${formCss}</style>`));
 inlined++;
}
if(inlined!==2)throw new Error(`Contact form CSS inlined on ${inlined} pages, expected 2`);
// 3) Our own scripts ship minified (vendor *.min.js already are). Source stays readable.
for(const file of [...copied]){
 if(!/^assets\/js\/[^/]+\.js$/.test(file)||file.endsWith('.min.js'))continue;
 const dest=path.join(out,file);
 const result=await minify(fs.readFileSync(dest,'utf8'),{compress:true,mangle:true,format:{comments:false}});
 if(!result.code)throw new Error(`Minify failed: ${file}`);
 fs.writeFileSync(dest,result.code);
}
// Version stamp: /assets css/js get ?v=<content hash> in the exported HTML only, so the
// one-day browser cache (vercel.json max-age=86400) never serves last release's file.
const hashes=new Map();
function version(ref){
 if(!hashes.has(ref)){const f=ref.slice(1);hashes.set(ref,fs.existsSync(f)?crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex').slice(0,10):null);}
 return hashes.get(ref);
}
let stamped=0;
for(const file of [...copied].map(f=>f==='error/404/index.html'?'404.html':f)){
 if(!file.endsWith('.html'))continue;
 const dest=path.join(out,file);
 const html=fs.readFileSync(dest,'utf8').replace(/((?:src|href)=["'])(\/assets\/[^"'#?]+\.(?:css|js))(["'])/g,(m,a,ref,b)=>{const v=version(ref);if(!v)return m;stamped++;return `${a}${ref}?v=${v}${b}`;});
 fs.writeFileSync(dest,html);
}
if(!stamped)throw new Error('Version stamp matched no asset reference');
let bytes=0;for(const file of copied)bytes+=fs.statSync(file).size;
console.log(`Static export: ${copied.size+1} files, ${(bytes/1024/1024).toFixed(2)} MiB. No WordPress, PHP, demos or source tooling.`);
