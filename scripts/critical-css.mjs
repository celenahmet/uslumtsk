// Inline only the shared first viewport; keep the complete stylesheet cacheable.
import {PurgeCSS} from 'purgecss';
import CleanCSS from 'clean-css';
import fs from 'node:fs';
const pages = [...fs.readFileSync('sitemap.xml','utf8').matchAll(/<loc>https:\/\/uslusurucukursu\.com([^<]*)<\/loc>/g)].map(m=>m[1].replace(/^\//,'')+'index.html');
const content = pages.map(path=>{
 const html=fs.readFileSync(path,'utf8');
 const body=html.slice(html.indexOf('<body'));
 const marker=body.includes('<!-- hero slider end -->')?'<!-- hero slider end -->':'<!-- breadcrumb end -->';
 return {raw:body.slice(0,body.indexOf(marker)+marker.length),extension:'html'};
});
const result=await new PurgeCSS().purge({content,css:['assets/css/site.min.css'],safelist:{standard:[/^navbar/,/^collaps/,/^show$/, /^dropdown/],deep:[/^navbar/,/^collaps/,/^show$/, /^dropdown/]}});
const critical=new CleanCSS({level:1}).minify(result.map(r=>r.css).join('\n')).styles.replaceAll('../fonts/', '/assets/fonts/').replaceAll('../img/', '/assets/img/');
fs.writeFileSync('assets/css/critical.min.css',critical);
for (const path of pages) {
 let html=fs.readFileSync(path,'utf8');
 html=html.replace(/<style id="critical-css">[\s\S]*?<\/style>/g,'');
 html=html.replace(/<link[^>]*href="\/assets\/css\/site.min.css"[^>]*\/>/g,'');
 html=html.replace(/<noscript>\s*<\/noscript>/g,'');
 const styles=`<style id="critical-css">${critical}</style><link rel="preload" as="style" href="/assets/css/site.min.css" onload="this.onload=null;this.rel='stylesheet'"><noscript><link href="/assets/css/site.min.css" rel="stylesheet"/></noscript>`;
 // Delete an earlier generated preload on rebuild.
 html=html.replace(/<link[^>]*href="\/assets\/css\/site.min.css"[^>]*>/g,'').replace(/<noscript>\s*<\/noscript>/g,'');
 html=html.replace('</head>',styles+'</head>');
 fs.writeFileSync(path,html);
}
console.log(`Inlined first-viewport CSS: ${critical.length} bytes`);
