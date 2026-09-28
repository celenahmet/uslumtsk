// Publish an allowlisted static site. Never copy the WordPress installation.
import fs from 'node:fs';
import path from 'node:path';
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
for (const file of [...pages,'robots.txt','sitemap.xml','google05c43e8ce47e9840.html','assets/fonts/Barlow-OFL.txt']) copy(file);
for (const dir of ['qr','en/qr','e-sinav','en/e-sinav','whatsapp','galeri','en/gallery']) {
 // Public redirect tools are intentional; gallery content is already in sitemap.
 const candidate=path.join(dir,'index.html');if(fs.existsSync(candidate))copy(candidate);
 if(dir.endsWith('qr'))for(const entry of fs.readdirSync(dir,{withFileTypes:true}))if(entry.isDirectory()&&entry.name!=='error')copy(path.join(dir,entry.name,'index.html'));
}
fs.writeFileSync(path.join(out,'404.html'),'<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Sayfa bulunamadı | Uslu Sürücü Kursu</title></head><body style="font:18px/1.7 system-ui;max-width:700px;margin:10vh auto;padding:24px"><h1>Sayfa bulunamadı</h1><p>Aradığınız sayfa taşınmış veya kaldırılmış olabilir.</p><p><a href="/">Ana sayfaya dönün</a> veya <a href="/iletisim/">bizimle iletişime geçin</a>.</p></body></html>');
let bytes=0;for(const file of copied)bytes+=fs.statSync(file).size;
console.log(`Static export: ${copied.size+1} files, ${(bytes/1024/1024).toFixed(2)} MiB. No WordPress, PHP, demos or source tooling.`);
