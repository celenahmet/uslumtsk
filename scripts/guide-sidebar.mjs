// Derive sidebar content from the published guide hub on every build.
import fs from 'node:fs';
const hub = fs.readFileSync('rehber/index.html', 'utf8');
const groups = [...hub.matchAll(/<section class="guide-hub-group">([\s\S]*?)<\/section>/g)].map(m => {
 const [, id, name] = m[1].match(/<h2 id="([^"]+)">([^<]+)<\/h2>/);
 const articles = [...m[1].matchAll(/<a href="([^"]+)"><span><strong>([^<]+)<\/strong>/g)].map(a => ({url:a[1], title:a[2]}));
 return {id, name, articles};
});
if (!groups.length) throw new Error('Guide categories missing');
const articles = groups.flatMap(g => g.articles);
const featured = [...hub.matchAll(/<a class="home-guide-feature" href="([^"]+)">[\s\S]*?<strong>([^<]+)<\/strong>/g)].slice(0,3);
const popularSlugs = ['ehliyet-icin-gerekli-belgeler', 'motosiklet-ehliyeti', 'ehliyet-yenileme', 'otomatik-vites-ehliyet', 'sinavda-kalirsam'];
const popular = popularSlugs.map(slug => articles.find(a => a.url === `/rehber/${slug}/`)).filter(Boolean);
const widget = (title, body) => `<section class="widget guide-sidebar-widget"><h2 class="widget-title heading-size-4">${title}</h2>${body}</section>`;
const block = '<!-- guide sidebar -->\n<div class="guide-sidebar">' +
 widget('Rehberde Ara', '<form action="/rehber/" class="guide-sidebar-search" role="search"><label class="guide-sidebar-label" for="sidebar-guide-query">Ehliyet hakkında ne arıyorsunuz?</label><div><input id="sidebar-guide-query" name="q" type="search" maxlength="100" placeholder="Örn. sınav, belgeler…" required/><button type="submit" aria-label="Rehberde ara">Ara</button></div></form>') +
 widget('Rehber Kategorileri', '<nav aria-label="Rehber kategorileri" class="guide-sidebar-categories">' + groups.map(g=>`<a href="/rehber/#${g.id}"><span>${g.name}</span><small>${g.articles.length}</small></a>`).join('')+'</nav>') +
 widget('Popüler Yazılar', '<div class="guide-sidebar-posts">'+popular.map((a,i)=>`<a href="${a.url}"><span class="guide-sidebar-number">0${i+1}</span><span>${a.title}</span></a>`).join('')+'</div>') +
 widget('Öne Çıkan Yazılar', '<div class="guide-sidebar-posts">'+featured.map((m,i)=>`<a href="${m[1]}"><span class="guide-sidebar-number">0${i+1}</span><span>${m[2]}</span></a>`).join('')+'</div>') +
 widget('En Çok Arananlar', '<nav aria-label="Sık aranan rehber konuları" class="guide-sidebar-topics">'+['Ehliyet masrafları','Gerekli belgeler','Direksiyon sınavı','Motosiklet ehliyeti','Ehliyet yenileme'].map(q=>`<a href="/rehber/?q=${encodeURIComponent(q)}">${q}</a>`).join('')+'</nav>') +
 '<section class="widget guide-sidebar-widget" id="guide-recent" hidden><h2 class="widget-title heading-size-4">Son Okuduklarınız</h2><div class="guide-sidebar-posts" id="guide-recent-list"></div></section>' +
 '<a class="guide-sidebar-all" href="/rehber/">Tüm rehber yazıları <span aria-hidden="true">→</span></a></div>\n<!-- guide sidebar end -->';
const relatedSlugs = {
 'motor-a1': ['16-yasinda-ehliyet', 'motosiklet-direksiyon-sinavi', 'b-ehliyetle-motosiklet'],
 'motor-a2': ['motosiklet-direksiyon-sinavi', 'ehliyete-sinif-ekleme', 'direksiyon-dersi'],
 'manuel-b': ['direksiyon-dersi', 'direksiyon-sinavi-geri-park', 'aday-surucu-belgesi'],
 'otomatik-b': ['direksiyon-sinavi-geri-park', 'ehliyetim-var-araba-kullanamiyorum', 'direksiyon-dersi'],
 'ozel': ['ehliyetim-var-araba-kullanamiyorum', 'direksiyon-dersi', 'trafik-kazasinda-ne-yapilmali'],
 'diger': ['kamyon-ehliyeti', 'otobus-ehliyeti', 'ehliyete-sinif-ekleme'],
 'ozel-ab': ['ozel-gereksinimli-surucu-adaylari', 'surucu-olur-raporu', 'otomatik-vites-ehliyet']
};
function extraContent(course) {
 const related = (relatedSlugs[course] || ['surucu-kursu-kayit-donemleri', 'direksiyon-dersi', 'surucu-olur-raporu'])
  .map(slug => articles.find(a => a.url === `/rehber/${slug}/`)).filter(Boolean);
 return widget('Bu Eğitim İçin Rehberler', '<div class="guide-sidebar-posts">'+related.map(a=>`<a href="${a.url}">${a.title}<span aria-hidden="true">→</span></a>`).join('')+'</div>') +
 '<section class="guide-sidebar-contact"><span class="guide-sidebar-eyebrow">BİRLİKTE PLANLAYALIM</span><h2>Ehliyet yolculuğunuz<br/>buradan başlasın</h2><p>Kayıt, ders programı ve eğitim seçenekleri hakkında bize ulaşın.</p><a class="guide-sidebar-call" href="tel:+905320685647">Telefonla ara <strong>0532 068 56 47</strong></a><a class="guide-sidebar-whatsapp" href="https://wa.me/905320685647?text=Merhaba%2C%20ehliyet%20e%C4%9Fitimleri%20hakk%C4%B1nda%20bilgi%20almak%20istiyorum." target="_blank" rel="noopener noreferrer">WhatsApp’tan yazın <span aria-hidden="true">↗</span></a><small>Atatürk Cd. No:2/17, Sincan/Ankara<br/>2. Noterin üst katı</small></section>';
}
for (const dir of fs.readdirSync('egitim', {withFileTypes:true})) {
 const file = dir.isDirectory() ? `egitim/${dir.name}/index.html` : dir.name === 'index.html' ? 'egitim/index.html' : null;
 if (!file || !fs.existsSync(file)) continue;
 let html = fs.readFileSync(file,'utf8').replace(/\n?<!-- guide sidebar -->[\s\S]*?<!-- guide sidebar end -->/g,'');
 const anchor = '</div>\n</div>\n</div>\n</div>\n<div class="col-xl-8 col-lg-8">';
 if (!html.includes(anchor)) throw new Error(`Sidebar anchor missing: ${file}`);
 html = html.replace(anchor, '</div>\n</div>\n'+block.replace('</div>\n<!-- guide sidebar end -->', extraContent(dir.name)+'</div>\n<!-- guide sidebar end -->')+'\n</div>\n</div>\n<div class="col-xl-8 col-lg-8">');
 if (!html.includes('/assets/css/guide-sidebar.css')) html=html.replace('</head>','<link href="/assets/css/guide-sidebar.css" rel="stylesheet"/>\n</head>');
 if (!html.includes('/assets/js/guide-reader.js')) html=html.replace('</body>','<script defer src="/assets/js/guide-reader.js"></script>\n</body>');
 fs.writeFileSync(file,html);
}
for (const a of articles) {
 const file = a.url.slice(1)+'index.html';
 let html=fs.readFileSync(file,'utf8');
 html=html.replace(/<!-- guide article sidebar -->[\s\S]*?<!-- guide article sidebar end -->/g,'').replace(/<!-- guide layout end -->[\s\S]*?<!-- guide layout end marker -->/g,'');
 const courseWidget = fs.readFileSync('egitim/motor-a2/index.html','utf8').match(/<div class="widget category">[\s\S]*?<\/div>\n<\/div>/)[0];
 const articleSidebar = '<!-- guide article sidebar --><div class="guide-reading-layout"><aside class="course-sidebar guide-reading-sidebar" aria-label="Rehber ve eğitim menüsü">'+courseWidget+block.replace('</div>\n<!-- guide sidebar end -->',extraContent('index.html')+'</div>\n<!-- guide sidebar end -->')+'</aside><!-- guide article sidebar end -->';
 html=html.replace('<article class="legal-text guide-text">',articleSidebar+'<article class="legal-text guide-text">').replace('</article>','</article><!-- guide layout end --></div><!-- guide layout end marker -->');
 if (!html.includes('/assets/css/guide-sidebar.css')) html=html.replace('</head>','<link href="/assets/css/guide-sidebar.css" rel="stylesheet"/>\n</head>');
 if (!html.includes('/assets/js/guide-reader.js')) html=html.replace('</body>','<script defer src="/assets/js/guide-reader.js"></script>\n</body>');
 fs.writeFileSync(file,html);
}
fs.writeFileSync('assets/js/guide-reader-data.js', 'window.usluGuideArticles = '+JSON.stringify(articles)+';\n');
// Keep catalog embedded in reader script; no runtime request or global dependency.
const reader = fs.readFileSync('assets/js/guide-reader.js','utf8').replace(/\/\* catalog start \*\/[\s\S]*?\/\* catalog end \*\//, '/* catalog start */\nvar catalog = '+JSON.stringify(articles)+';\n/* catalog end */');
fs.writeFileSync('assets/js/guide-reader.js',reader);
fs.unlinkSync('assets/js/guide-reader-data.js');
console.log(`Guide sidebar: ${groups.length} categories, ${articles.length} articles`);
