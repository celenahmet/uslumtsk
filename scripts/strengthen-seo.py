"""Generate reviewed course copy and contextual guide links from one content source.
Run with python3 scripts/strengthen-seo.py; build calls it before sidebar export.
"""
from pathlib import Path
import html,json,re
BASE='https://uslusurucukursu.com'
data=json.loads(Path('content/course-seo.json').read_text())
def esc(s):return html.escape(s,quote=True)
def link(path,title):return '<a href="'+path+'">'+esc(title)+'</a>'
def guide(slug):
 s=Path('rehber/'+slug+'/index.html').read_text()
 title=re.sub('<[^>]+>','',re.search(r'<h1[^>]*>(.*?)</h1>',s,re.S)[1])
 return link('/rehber/'+slug+'/',html.unescape(title))
def meta(s,title,desc,h1=None):
 s=re.sub(r'<title>.*?</title>','<title>'+esc(title)+'</title>',s,count=1,flags=re.S)
 for attr,key,value in [('name','description',desc),('property','og:title',title),('property','og:description',desc)]:
  pattern=r'<meta\b(?=[^>]*\b'+attr+'="'+re.escape(key)+'")[^>]*>'
  s=re.sub(pattern,lambda m:re.sub(r'content="[^"]*"','content="'+esc(value)+'"',m[0]),s)
 if h1:s=re.sub(r'(<h1\b[^>]*>).*?(</h1>)',lambda m:m[1]+esc(h1)+m[2],s,count=1,flags=re.S)
 return s
SOURCE='https://www.nvi.gov.tr/sss-surucu-belgeleri-hizmetleri'
for slug,p in data.items():
 path=Path('egitim/'+('' if slug=='index' else slug+'/')+'index.html');s=path.read_text()
 first=s.index('<div class="col-xl-8 col-lg-8">');end=s.index('<!-- course-single-area end -->')
 hero=re.search(r'<div class="course-details-img mb-30">[\s\S]*?</div>',s[first:])[0]
 related={'manuel-b':['otomatik-b','ozel'],'otomatik-b':['manuel-b','ozel'],'motor-a1':['motor-a2'],'motor-a2':['motor-a1'],'ozel':['manuel-b','otomatik-b'],'diger':['manuel-b'],'ozel-ab':['otomatik-b'],'index':['manuel-b','otomatik-b','motor-a1','motor-a2','ozel','ozel-ab','diger']}[slug]
 html_parts=[hero,'<article class="course-seo" aria-labelledby="course-overview">','<h2 id="course-overview">'+esc(p['h1'])+'</h2>','<p class="course-seo-lead">'+esc(p['intro'])+'</p>']
 for title,body in p['sections']:html_parts+=['<section><h2>'+esc(title)+'</h2><p>'+esc(body)+'</p></section>']
 if slug in ['manuel-b','otomatik-b','motor-a1','motor-a2']:
  age=16 if slug=='motor-a1' else 18
  html_parts+=['<p class="course-seo-source">Başvuru notu: '+str(age)+' yaşın doldurulması ilgili sınıfın yaş koşuludur; diğer başvuru şartları ayrıca değerlendirilir. '+link(SOURCE,'NVİ sürücü belgesi başvuru koşulları')+'.</p>']
 if slug=='ozel':
  registration=('Özel ders görüşmesinde ne paylaşmalısınız?','Mevcut ehliyetinizin sınıfı, manuel veya otomatik araç tercihiniz ve çalışmak istediğiniz konularla başlayın. Son araç kullanma tarihinizi ve ders için uygun günlerinizi belirtin. Ücret, araç ve buluşma koşullarını ders planını kabul etmeden önce öğrenin.')
 else:
  registration=('Kayıt belgeleri ve başvuru hazırlığı','Kursumuzun kayıt için paylaştığı listede biyometrik fotoğraf, sürücü olur raporu, diploma veya öğrenci belgesi ve adli sicil kaydı bulunur. Sağlık raporunu yetkili sağlık kuruluşundan alın; ücret ve işlem koşullarını ilgili kuruma sorun. Güncel belge listesini kayıt öncesinde kursla doğrulayın.')
 html_parts+=['<section><h2>'+registration[0]+'</h2><p>'+registration[1]+'</p><p>'+guide('ehliyet-icin-gerekli-belgeler')+' · '+guide('surucu-olur-raporu')+'</p></section>']
 html_parts+=['<section><h2>'+esc(p['h1'].replace('Sincan ','',1))+' hakkında sorular</h2><div class="course-seo-faq">']
 for question,answer in p['faqs']:html_parts+=['<details><summary>'+esc(question)+'</summary><p>'+esc(answer)+'</p></details>']
 html_parts+=['</div></section>','<section><h2>İlgili eğitimleri karşılaştırın</h2><ul class="course-seo-related">']
 for other in related:html_parts+=['<li>'+link('/egitim/'+other+'/',data[other]['h1'])+'</li>']
 html_parts+=['</ul></section>','<section><h2>Başvuru öncesi okuyabileceğiniz rehberler</h2><ul class="course-seo-related">']
 for item in p['guides']:html_parts+=['<li>'+guide(item)+'</li>']
 html_parts+=['</ul></section>','<section class="course-seo-contact"><h2>Ders planı ve kayıt için bize ulaşın</h2><p>Atatürk Mah. Atatürk Cd. No:2/17 (2. Noterin üst katı), Sincan/Ankara. Görüşme saatleri: Pazartesi–Perşembe 09.00–19.30, Cuma–Pazar 09.00–20.30.</p><div><a href="tel:+905320685647">Telefonla ara: 0532 068 56 47</a><a href="/iletisim/">Kayıt ve program bilgisi al</a></div><p class="course-seo-contact-links">'+link('/galeri/araclar/','Eğitim araçlarımız')+' · '+link('/hakkimizda/','Kursumuz ve eğitmenlerimiz')+' · '+link('https://g.co/kgs/MfyA3BT','Haritada yol tarifi')+'</p></section>','</article>']
 right='<div class="col-xl-8 col-lg-8">\n<div class="course-details">\n'+'\n'.join(html_parts)+'\n</div>\n</div>\n'
 # Four containers remain open: row, course-single-wrapper, container, course-single-area.
 s=s[:first]+right+'</div>\n</div>\n</div>\n</div>\n'+s[end:]
 s=meta(s,p['title'],p['description'],p['h1'])
 if '/assets/css/course-seo.css' not in s:s=s.replace('</head>','<link href="/assets/css/course-seo.css" rel="stylesheet"/>\n</head>')
 url=BASE+'/egitim/'+('' if slug=='index' else slug+'/')
 def structured(m):
  doc=json.loads(m[1]);graph=doc.get('@graph',[])
  graph[:]=[n for n in graph if n.get('@type') not in ['Service','FAQPage']]
  for n in graph:
   if n.get('@type')=='WebPage':n.update(name=p['title'],description=p['description'],mainEntity={'@id':url+'#service'})
   if n.get('@type')=='BreadcrumbList':n['itemListElement'][-1]['name']=p['h1']
  graph.append({'@type':'Service','@id':url+'#service','name':p['h1'],'serviceType':p['h1'].replace('Sincan ',''),'description':p['intro'],'url':url,'provider':{'@id':BASE+'/#school'},'areaServed':{'@type':'AdministrativeArea','name':'Sincan, Ankara'},'mainEntityOfPage':{'@id':url+'#webpage'}})
  # Visible Q&A is useful on its own; no FAQ rich-result eligibility is promised.
  return '<script type="application/ld+json">'+json.dumps(doc,ensure_ascii=False,separators=(',',':'))+'</script>'
 s=re.sub(r'<script type="application/ld\+json">(.*?)</script>',structured,s,flags=re.S);path.write_text(s)

# Every guide has explicit, relevant paths to an existing course, inside the article.
motor={'16-yasinda-ehliyet','motosiklet-ehliyeti','motosiklet-direksiyon-sinavi','b-ehliyetle-motosiklet'}
heavy={'kamyon-ehliyeti','otobus-ehliyeti','traktor-ehliyeti','b-ehliyetle-romork','is-makinesi-ehliyeti','psikoteknik-degerlendirme'}
private={'ehliyetim-var-araba-kullanamiyorum','direksiyon-dersi','direksiyon-sinavi-geri-park'}
for path in Path('rehber').glob('*/index.html'):
 slug=path.parent.name;s=path.read_text()
 s=re.sub(r'\s*<!-- related course start -->[\s\S]*?<!-- related course end -->\s*','',s)
 if slug in motor:targets=['motor-a1','motor-a2'];intro='Motosiklet ehliyeti için sınıf seçimini eğitim programıyla birlikte değerlendirin. Yaşınızı, mevcut belgenizi ve deneyiminizi belirterek bilgi alabilirsiniz.'
 elif slug in heavy:targets=['diger'];intro='Hedeflediğiniz araç için doğru ehliyet sınıfını, mevcut belgenizi ve güncel eğitim uygunluğunu kursla görüşün.'
 elif slug in private:targets=['ozel'];intro='Park, araç kontrolü veya trafiğe yeniden çıkma hedefinizi paylaşarak mevcut belgenize uygun direksiyon dersi hakkında bilgi alın.'
 elif slug=='otomatik-vites-ehliyet':targets=['otomatik-b','manuel-b'];intro='Araç tercihiniz ve kullanım hedefiniz için manuel ve otomatik B eğitimlerini karşılaştırın.'
 elif slug in {'ozel-gereksinimli-surucu-adaylari','surucu-olur-raporu'}:targets=['ozel-ab'];intro='Sağlık ve belge koşulları kişiye göre değerlendirilir. Eğitim ve araç uygunluğunu kayıt öncesinde kursla netleştirin.'
 else:targets=['index'];intro='Sincan’da kurs kaydı düşünüyorsanız kullanmak istediğiniz araç türüne ve mevcut belgenize uygun eğitim seçeneklerini inceleyin.'
 block='<section class="guide-course-path"><h2>Sincan’da ilgili eğitim seçenekleri</h2><p>'+intro+'</p><ul>'
 for target in targets:block+='<li>'+link('/egitim/'+('' if target=='index' else target+'/'),data[target]['h1'])+'</li>'
 block+='</ul></section>'
 s=s.replace('</article>','\n<!-- related course start -->'+block+'<!-- related course end -->\n</article>')
 if '/assets/css/course-seo.css' not in s:s=s.replace('</head>','<link href="/assets/css/course-seo.css" rel="stylesheet"/>\n</head>')
 path.write_text(s)
print('SEO content: 8 distinct course pages, 50 contextual guide-to-course sections')

english=json.loads(Path('content/course-seo-en.json').read_text())
for slug,p in english.items():
 route='/en/train/'+(p['route']+'/' if p['route'] else '');path=Path(route.lstrip('/')+'index.html');s=path.read_text()
 first=s.index('<div class="col-xl-8 col-lg-8">');end=s.index('<!-- course-single-area end -->')
 hero=re.search(r'<div class="course-details-img mb-30">[\s\S]*?</div>',s[first:])[0]
 body=hero+'<article class="course-seo"><h2>'+esc(p['name'])+'</h2><p class="course-seo-lead">'+esc(p['intro'])+'</p>'
 for title,text in p['sections']:body+='<section><h2>'+esc(title)+'</h2><p>'+esc(text)+'</p></section>'
 body+='<section><h2>Prepare your registration questions</h2><p>Ask about the current programme, required documents, vehicle options and quotation. Explain your licence status and practical goals. Training fees and official examination or licence payments should be considered separately.</p><ul class="course-seo-related">'
 for g in data[slug]['guides']:body+='<li>'+guide(g)+' (Turkish guide)</li>'
 body+='</ul></section><section class="course-seo-contact"><h2>Contact Uslu Driving School</h2><p>Atatürk Cd. No:2/17, Sincan/Ankara, above the 2nd Notary. Monday–Thursday 09:00–19:30; Friday–Sunday 09:00–20:30.</p><div><a href="tel:+905320685647">Call +90 532 068 56 47</a><a href="/en/contact/">Ask about registration</a></div></section></article>'
 s=s[:first]+'<div class="col-xl-8 col-lg-8">\n<div class="course-details">'+body+'</div>\n</div>\n</div>\n</div>\n</div>\n</div>\n'+s[end:]
 desc=p['description'];title=p.get('metaTitle',p['name']+' | Uslu')
 s=meta(s,title,desc,p['name'])
 if '/assets/css/course-seo.css' not in s:s=s.replace('</head>','<link href="/assets/css/course-seo.css" rel="stylesheet"/>\n</head>')
 def en_schema(m):
  doc=json.loads(m[1]);graph=doc.get('@graph',[]);graph[:]=[n for n in graph if n.get('@type')!='Service']
  for n in graph:
   if n.get('@type')=='WebPage':n.update(name=title,description=desc,mainEntity={'@id':BASE+route+'#service'})
  graph.append({'@type':'Service','@id':BASE+route+'#service','name':p['name'],'description':desc,'url':BASE+route,'provider':{'@id':BASE+'/#school','name':'Uslu Sürücü Kursu','url':BASE+'/'},'areaServed':{'@type':'AdministrativeArea','name':'Sincan, Ankara'}})
  return '<script type="application/ld+json">'+json.dumps(doc,ensure_ascii=False,separators=(',',':'))+'</script>'
 s=re.sub(r'<script type="application/ld\+json">(.*?)</script>',en_schema,s,flags=re.S);path.write_text(s)
print('English: 8 corresponding course pages refreshed without unsupported service claims')

# Refresh the fixed measurement page catalogue without storing query strings.
sm=Path('sitemap.xml').read_text()
routes=re.findall(r'<loc>https://uslusurucukursu.com([^<]*)</loc>',sm)
Path('api/_seo-pages.json').write_text(json.dumps(routes,ensure_ascii=False,indent=2)+'\n')
p=Path('assets/js/seo-events.js');text=p.read_text()
text=re.sub(r'/\* pages start \*/[\s\S]*?/\* pages end \*/', '/* pages start */\nvar pages='+json.dumps(routes)+';\n/* pages end */',text)
p.write_text(text)
for route in routes:
    p=Path(route.lstrip('/')+'index.html');text=p.read_text()
    if '/assets/js/seo-events.js' not in text:
        text=text.replace('</body>','<script defer src="/assets/js/seo-events.js"></script>\n</body>')
        p.write_text(text)
