import { PurgeCSS } from 'purgecss';
import CleanCSS from 'clean-css';
import fs from 'node:fs';
const urls = [...fs.readFileSync('sitemap.xml', 'utf8').matchAll(/<loc>https:\/\/uslusurucukursu\.com([^<]*)<\/loc>/g)].map(m => m[1].replace(/^\//, '') + 'index.html');
const result = await new PurgeCSS().purge({
  content: [...urls, 'assets/js/main.js'],
  css: ['assets/css/bootstrap.min.css', 'assets/css/all-fontawesome.min.css', 'assets/css/magnific-popup.min.css', 'assets/css/owl.carousel.min.css', 'assets/css/style.css'],
  safelist: {
    standard: [/^mfp-/, /^owl-/, /^collaps/, /^show$/, /^active$/, /^dropdown/, /^modal/, /^fade$/, /^navbar/],
    deep: [/^mfp-/, /^owl-/, /^collaps/, /^show$/, /^dropdown/, /^navbar/]
  }
});
const output = new CleanCSS({level: 1}).minify(result.map(r => r.css).join('\n'));
if (output.errors.length) throw new Error(output.errors.join('\n'));
fs.writeFileSync('assets/css/site.min.css', output.styles);
console.log(`Built CSS: ${output.styles.length} bytes`);
