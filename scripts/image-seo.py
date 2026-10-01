"""Describe actual photos, preserve decorative empty alts, and index displayed images."""
from pathlib import Path
import re, html, shutil
import xml.etree.ElementTree as ET
BASE='https://uslusurucukursu.com'
# Visually reviewed real school photos. Legacy URLs remain available.
photos={
 '/assets/img/gallery/uslu01.webp':('sincan-uslu-direksiyon-egitim-otomobilleri','Sincan Uslu Sürücü Kursu logolu direksiyon eğitim otomobilleri','Uslu Driving School training cars in Sincan'),
 '/assets/img/gallery/uslu02.webp':('uslu-surucu-kursu-egitim-minibusu','Uslu Sürücü Kursu logolu eğitim minibüsü','Uslu Driving School training minibus'),
 '/assets/img/gallery/uslu03.webp':('sincan-uslu-surucu-kursu-giris-tabelasi','Sincan Uslu Sürücü Kursu giriş tabelası','Uslu Driving School entrance sign in Sincan'),
 '/assets/img/gallery/uslu04.webp':('uslu-motosiklet-ehliyeti-egitim-motosikleti','Uslu Sürücü Kursu logolu motosiklet eğitimi aracı, yandan görünüm','Uslu Driving School training motorcycle, side view'),
 '/assets/img/gallery/uslu05.webp':('uslu-surucu-kursu-teorik-egitim-sinifi','Uslu Sürücü Kursu teorik trafik eğitimi sınıfı','Uslu Driving School traffic theory classroom'),
 '/assets/img/gallery/uslu06.webp':('sincan-uslu-surucu-kursu-egitim-araclari','Sincan Uslu Sürücü Kursu eğitim otomobilleri, park alanında','Uslu Driving School training cars in the parking area in Sincan'),
 '/egitim/motor-a1/motor2.webp':('uslu-motosiklet-egitim-araci-arka-gorunum','Uslu Sürücü Kursu motosiklet eğitim aracı, arkadan görünüm','Uslu Driving School training motorcycle, rear view'),
 '/egitim/manuel-b/tek.webp':('uslu-direksiyon-egitim-otomobili-aksam','Uslu Sürücü Kursu logolu direksiyon eğitim otomobili, gün batımında','Uslu Driving School training car at sunset'),
 '/egitim/diger/car.webp':('uslu-otobus-ehliyeti-egitim-otobusu','Uslu Sürücü Kursu yazılı otobüs ehliyeti eğitim aracı','Uslu Driving School bus used for bus licence training'),
}
other={
 '/assets/img/about/01.webp':('Araç içinde form dolduran sürücü, temsili eğitim fotoğrafı','Driver completing a form inside a car, illustrative training photo'),
 '/assets/img/course/01.webp':('Direksiyon başındaki kadın sürücü, temsili fotoğraf','Woman at the steering wheel, illustrative photo'),
 '/assets/img/course/02.webp':('Direksiyon başındaki sürücü, temsili sürüş fotoğrafı','Driver at the steering wheel, illustrative driving photo'),
 '/assets/img/course/03.webp':('Otomobil içinde eğitmen ve sürücü adayı, temsili direksiyon dersi','Instructor and learner inside a car, illustrative driving lesson'),
 '/assets/img/course/04.webp':('Otomobil içindeki iki kişi, temsili sürüş fotoğrafı','Two people inside a car, illustrative driving photo'),
 '/assets/img/course/05.webp':('Otomobil içinde sürücü, temsili fotoğraf','Driver inside a car, illustrative photo'),
 '/assets/img/course/06.webp':('Direksiyon başında telefonla konuşan sürücü, temsili fotoğraf','Driver using a phone at the wheel, illustrative photo'),
 '/assets/img/course/single.webp':('Otomobil penceresinden el sallayan sürücü, temsili fotoğraf','Driver waving from a car window, illustrative photo'),
 '/assets/img/logo/logo-white.webp':('Uslu Sürücü Kursu logosu','Uslu Driving School logo'),
 '/assets/img/partner/01.webp':('Uslu Sürücü Kursu logosu','Uslu Driving School logo'),
 '/assets/img/partner/02.webp':('T.C. Millî Eğitim Bakanlığı logosu','Republic of Türkiye Ministry of National Education logo'),
}
NS='http://www.sitemaps.org/schemas/sitemap/0.9';IMG='http://www.google.com/schemas/sitemap-image/1.1'
p=Path('sitemap.xml');sm=p.read_text();tree=ET.fromstring(sm)
for old,(slug,tr,en) in photos.items():
 dest='/assets/img/gallery/'+slug+'.webp'
 for suffix in ['', '-480','-800']:
  src=Path(old[1:]).with_name(Path(old).stem+suffix+'.webp')
  target=Path(dest[1:]).with_name(slug+suffix+'.webp')
  if src.exists() and not target.exists():shutil.copyfile(src,target)
 other[dest]=(tr,en)
for entry in tree.findall('{'+NS+'}url'):
 url=entry.find('{'+NS+'}loc').text;route=url[len(BASE):];file=Path(route.lstrip('/')+'index.html')
 s=file.read_text();en=route.startswith('/en/')
 for old,(slug,tr,eng) in photos.items():s=s.replace(old,'/assets/img/gallery/'+slug+'.webp')
 def replace(m):
  tag=m.group();src=re.search(r'\bsrc="([^"]+)"',tag)
  if src and src[1] in other:
   alt=other[src[1]][1 if en else 0]
   tag=re.sub(r'\balt="[^"]*"','alt="'+html.escape(alt,quote=True)+'"',tag)
  return tag
 s=re.sub(r'<img\b[^>]*>',replace,s);file.write_text(s)
 # Actual displayed src URLs, not only sharing JPEGs. Ignore decorative icons/logos.
 refs=[]
 for tag in re.findall(r'<img\b[^>]*>',s):
  src=re.search(r'\bsrc="([^"]+)"',tag);alt=re.search(r'\balt="([^"]*)"',tag)
  if not src or not alt or not alt[1]:continue
  path=src[1]
  if any(part in path for part in ['/logo/','/icon/','/partner/','/testimonial/','avatar']):continue
  if path.startswith('/') and Path(path[1:]).is_file() and path not in refs:refs.append(path)
 existing=[i.find('{'+IMG+'}loc').text for i in entry.findall('{'+IMG+'}image')]
 additions=''.join('<image:image><image:loc>'+BASE+html.escape(ref)+'</image:loc></image:image>' for ref in refs if BASE+ref not in existing)
 if additions:
  pattern=r'(<url>\s*<loc>'+re.escape(url)+r'</loc>[\s\S]*?)(</url>)'
  sm=re.sub(pattern,lambda m:m[1]+additions+m[2],sm,count=1)
p.write_text(sm)
print('Image SEO: reviewed photo descriptions, descriptive URLs and displayed-image sitemap entries updated')
