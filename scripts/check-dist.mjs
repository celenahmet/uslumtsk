import fs from 'node:fs';
import path from 'node:path';
function walk(dir) {return fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(dir,e.name)):[path.join(dir,e.name)]);}
const files=walk('dist');
for(const file of files){
 if (/\.(php|sql|env)$/i.test(file)||/\/(blog|privacy|node_modules|\.git|scripts)\//.test(file))throw new Error(`Non-public file: ${file}`);
 if(!file.endsWith('.html'))continue;
 const html=fs.readFileSync(file,'utf8');
 for(const match of html.matchAll(/(?:href|src|data-background)=["'](\/[^"'#?]*)["']/g)) {
  const target=path.join('dist',decodeURI(match[1]));
  if(!fs.existsSync(target))throw new Error(`${file}: missing exported link ${match[1]}`);
 }
}
if(!fs.existsSync('dist/404.html'))throw new Error('Missing custom 404');
if(fs.readFileSync('dist/robots.txt','utf8').includes('/blog/'))throw new Error('Blog still in robots');
console.log(`PASS: ${files.length} exported files, local links and deployment exclusions.`);
