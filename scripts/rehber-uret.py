"""Ehliyet Rehberi sayfalarını (rehber/) sss/index.html şablonundan üretir.

İçerik tek kaynak: scripts/rehber_icerik.py. Bir yazıyı değiştirmek için oradaki
metni düzenleyip `python3 scripts/rehber-uret.py` çalıştırın; görünen SSS ile
FAQPage yapısal verisi birlikte güncellenir. Sonra `npm run build` ve check.
"""
import re, json, sys, os, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rehber_icerik import PAGES, HUB, SRC, R, GROUPS, FOOTER

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
BASE = 'https://uslusurucukursu.com'
BY_KEY = {p['key']: p for p in PAGES}

# ── Menü ve footer: rehber dışındaki tüm TR sayfalarda tek kaynaktan ──
NAV_OLD = '<li class="nav-item"><a class="nav-link" href="/rehber/">EHLİYET REHBERİ</a></li>'
NAV_NEW = '<li class="nav-item"><a class="nav-link" href="/rehber/">REHBER</a></li>'
FT_OLD_LINK = '<li><a href="/rehber/"><i aria-hidden="true" class="fas fa-caret-right"></i> Ehliyet Rehberi</a></li>\n'
FT_START, FT_END = '<!-- rehber footer -->', '<!-- rehber footer end -->'
FT_ANCHOR = '</div>\n</div>\n<center>'

def footer_block():
    lis = ''.join('<li><a href="%s">%s</a></li>' % (R[k], BY_KEY[k]['h1']) for k in FOOTER)
    return (FT_START + '<div class="footer-guide"><h2 class="footer-widget-title">Rehber</h2>'
            '<ul class="footer-guide-list">%s<li><a class="footer-guide-all" href="/rehber/">Tüm rehber yazıları</a></li></ul></div>' % lis + FT_END + '\n')

def tr_pages():
    urls = re.findall(r'<loc>https://uslusurucukursu\.com/([^<]*)</loc>', open(ROOT + 'sitemap.xml', encoding='utf-8').read())
    pages = [u + 'index.html' if u else 'index.html' for u in urls if not u.startswith('en/') and not u.startswith('rehber/')]
    return pages + ['error/404/index.html', 'e-sinav/index.html']

def sync_site_chrome():
    for rel in tr_pages():
        path = ROOT + rel
        s = open(path, encoding='utf-8').read()
        s = s.replace(NAV_OLD, NAV_NEW).replace(FT_OLD_LINK, '')
        assert s.count(NAV_NEW) == 1, rel
        if FT_START in s:
            s = re.sub(re.escape(FT_START) + '.*?' + re.escape(FT_END) + '\n', lambda m: footer_block(), s, count=1, flags=re.S)
        else:
            assert s.count(FT_ANCHOR) == 1, rel
            i = s.index(FT_ANCHOR)
            s = s[:i] + footer_block() + s[i:]
        assert s.count(FT_START) == 1, rel
        open(path, 'w', encoding='utf-8').write(s)

sync_site_chrome()
TEMPLATE = open(ROOT + 'sss/index.html', encoding='utf-8').read()
DATE = '2026-09-29'
DATE_TR = '29 Eylül 2026'
HUB_URL = BASE + '/rehber/'
SCHOOL = {"@type": "DrivingSchool", "@id": BASE + "/#school", "name": "Uslu Sürücü Kursu", "url": BASE + "/",
          "logo": BASE + "/assets/img/logo/logo.webp", "telephone": "+905320685647"}

def plain(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()

def build(url, title, desc, h1, crumbs, main, ld_nodes):
    s = TEMPLATE
    def once(a, b):
        nonlocal s
        assert s.count(a) == 1, (a[:70], s.count(a))
        s = s.replace(a, b)
    once('<title>Sincan Ehliyet Kursu: Sık Sorulan Sorular | Uslu</title>', '<title>%s</title>' % html.escape(title, quote=False))
    old_desc = 'Sincan’da ehliyet kursuna kayıt ve sürücü eğitimi hakkında sık sorulan soruları inceleyin. Size uygun eğitim için Uslu Sürücü Kursu ile görüşün.'
    assert s.count(old_desc) == 3, s.count(old_desc)
    s = s.replace(old_desc, html.escape(desc))
    once('<meta content="Sincan Ehliyet Kursu: Sık Sorulan Sorular | Uslu" property="og:title"/>',
         '<meta content="%s" property="og:title"/>' % html.escape(title))
    once('<link href="https://uslusurucukursu.com/sss/" rel="canonical"/><link href="https://uslusurucukursu.com/sss/" hreflang="tr" rel="alternate"/><link href="https://uslusurucukursu.com/en/faq/" hreflang="en" rel="alternate"/><link href="https://uslusurucukursu.com/sss/" hreflang="x-default" rel="alternate"/>',
         '<link href="%s" rel="canonical"/>' % url)
    once('<meta content="https://uslusurucukursu.com/sss/" property="og:url"/>', '<meta content="%s" property="og:url"/>' % url)
    once('<meta content="website" property="og:type"/>', '<meta content="article" property="og:type"/>' if url != HUB_URL else '<meta content="website" property="og:type"/>')
    bc = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]}
    ld = {"@context": "https://schema.org", "@graph": ld_nodes + [bc]}
    s, n = re.subn(r'(<script type="application/ld\+json">).*?(</script>)',
                   lambda m: m.group(1) + json.dumps(ld, ensure_ascii=False) + m.group(2), s, count=1, flags=re.S)
    assert n == 1
    b = s.find('<main'); e = s.find('</main>')
    assert b > 0 and e > b
    s = s[:b] + main + s[e:]
    # Çevirisi olmayan sayfa: dil değiştirici İngilizce ana sayfaya gider.
    s = s.replace('href="/en/faq/"', 'href="/en/"')
    assert s.count('<h1') == 1
    return s

def breadcrumb_html(h1, items):
    lis = ['<li><a href="/"><i aria-hidden="true" class="far fa-home"></i> Ana Sayfa</a></li>']
    for name, href in items[:-1]:
        lis.append('<li><a href="%s">%s</a></li>' % (href, name))
    lis.append('<li class="active">%s</li>' % items[-1][0])
    return ('<main class="main" id="main-content">\n<!-- breadcrumb -->\n'
            '<div class="site-breadcrumb" style="background: url(/assets/img/breadcrumb/breadcrumb.webp)">\n'
            '<div class="container">\n<h1 class="breadcrumb-title">%s</h1>\n<ul class="breadcrumb-menu">\n%s\n</ul>\n</div>\n</div>\n'
            '<!-- breadcrumb end -->\n') % (h1, '\n'.join(lis))

def sources_html(keys):
    lis = ''.join('<li><a href="%s" rel="noopener noreferrer" target="_blank">%s</a></li>' % (SRC[k][1], SRC[k][0]) for k in keys)
    return ('<h2>Kaynaklar</h2>\n<ul class="guide-sources">%s</ul>\n'
            '<p class="guide-note">Bu yazı bilgilendirme amaçlıdır ve %s tarihindeki resmî metinlere dayanır. Mevzuat ve ücretler değişebilir; işlem yapmadan önce güncel resmî kaynaklara bakın.</p>\n') % (lis, DATE_TR)

CTA = ('<div class="guide-cta">\n<p><strong>Sincan’da ehliyet kursu mu arıyorsunuz?</strong> Kayıt, ders programı ve ücret için Uslu Sürücü Kursu’na ulaşabilirsiniz. '
       'Pazartesi-Perşembe 09.00-19.30, Cuma-Pazar 09.00-20.30 arasında açığız.</p>\n'
       '<a class="theme-btn" href="/iletisim/">Bilgi alın <i aria-hidden="true" class="far fa-arrow-right"></i></a>'
       '<a class="guide-cta-tel" href="tel:+905320685647">0532 068 56 47</a>\n</div>\n')

def related_html(current):
    group = next(ks for _, ks in GROUPS if current in ks)
    lis = ''.join('<li><a href="%s">%s</a></li>' % (R[k], BY_KEY[k]['h1']) for k in group if k != current)
    return ('<nav aria-label="Rehberdeki diğer yazılar" class="guide-related">\n<h2>Rehberdeki diğer yazılar</h2>\n<ul>%s</ul>\n'
            '<p><a href="/rehber/">Ehliyet Rehberi ana sayfası</a></p>\n</nav>\n') % lis

written = []
for p in PAGES:
    url = BASE + R[p['key']]
    crumbs_html = [('Ehliyet Rehberi', '/rehber/'), (p['crumb'], R[p['key']])]
    faq_html = '<h2>Sık sorulan sorular</h2>\n' + ''.join('<h3>%s</h3>\n<p>%s</p>\n' % (q, ans) for q, ans in p['faq'])
    summary = '<div class="guide-summary">\n<h2>Kısaca</h2>\n<ul>%s</ul>\n</div>\n' % ''.join('<li>%s</li>' % x for x in p['summary'])
    main = (breadcrumb_html(p['h1'], crumbs_html) +
            '<div class="guide-area py-120">\n<div class="container">\n<article class="legal-text guide-text">\n'
            '<p class="guide-meta">Son güncelleme: %s · Hazırlayan: Uslu Sürücü Kursu · Resmî kaynaklara dayanır</p>\n' % DATE_TR +
            '<p class="legal-lead">%s</p>\n' % p['lead'] + summary + p['body'].strip() + '\n' + faq_html + CTA +
            sources_html(p['sources']) + related_html(p['key']) +
            '</article>\n</div>\n</div>\n')
    nodes = [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p['title'], "description": p['desc'],
         "inLanguage": "tr", "isPartOf": {"@id": BASE + "/#website"}, "dateModified": DATE},
        {"@type": "Article", "@id": url + "#article", "headline": p['h1'], "description": p['desc'], "inLanguage": "tr",
         "datePublished": DATE, "dateModified": DATE, "mainEntityOfPage": {"@id": url + "#webpage"},
         "image": BASE + "/assets/img/og/uslu-og.jpg", "author": SCHOOL, "publisher": SCHOOL,
         "isPartOf": {"@id": HUB_URL + "#webpage"}, "citation": [SRC[k][1] for k in p['sources']]},
        {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(ans)}} for q, ans in p['faq']]},
    ]
    out = build(url, p['title'], p['desc'], p['h1'],
                [('Ana Sayfa', BASE + '/'), ('Ehliyet Rehberi', HUB_URL), (p['crumb'], url)], main, nodes)
    path = ROOT + R[p['key']].strip('/') + '/index.html'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(out)
    written.append(path)

# Merkez sayfa
def cards_for(keys):
    return ''.join('<li><a href="%s"><strong>%s</strong><span>%s</span></a></li>' % (R[k], BY_KEY[k]['h1'], BY_KEY[k]['card']) for k in keys)
cards = ''.join('<h2>%s</h2>\n<ul class="guide-cards">%s</ul>\n' % (name, cards_for(keys)) for name, keys in GROUPS)
quick = ''.join('<h3>%s</h3>\n<p>%s <a href="%s">Ayrıntılar</a></p>\n' % (q, ans, R[k]) for q, ans, k in HUB['quick'])
main = (breadcrumb_html(HUB['h1'], [('Ehliyet Rehberi', '/rehber/')]) +
        '<div class="guide-area py-120">\n<div class="container">\n<div class="legal-text guide-text">\n'
        '<p class="guide-meta">Son güncelleme: %s · Hazırlayan: Uslu Sürücü Kursu</p>\n' % DATE_TR +
        '<p class="legal-lead">%s</p>\n' % HUB['lead'] +
        cards +
        '<h2>Kısa cevaplar</h2>\n' + quick + CTA + sources_html(HUB['sources']) +
        '</div>\n</div>\n</div>\n')
nodes = [
    {"@type": "CollectionPage", "@id": HUB_URL + "#webpage", "url": HUB_URL, "name": HUB['title'], "description": HUB['desc'],
     "inLanguage": "tr", "isPartOf": {"@id": BASE + "/#website"}, "dateModified": DATE, "publisher": SCHOOL,
     "mainEntity": {"@type": "ItemList", "itemListElement": [
         {"@type": "ListItem", "position": i + 1, "url": BASE + R[p['key']], "name": p['h1']} for i, p in enumerate(PAGES)]}},
]
out = build(HUB_URL, HUB['title'], HUB['desc'], HUB['h1'], [('Ana Sayfa', BASE + '/'), ('Ehliyet Rehberi', HUB_URL)], main, nodes)
os.makedirs(ROOT + 'rehber', exist_ok=True)
open(ROOT + 'rehber/index.html', 'w', encoding='utf-8').write(out)
written.append(ROOT + 'rehber/index.html')

# Denetim: uzun tire yok, başlık/açıklama uzunlukları
for path in written:
    s = open(path, encoding='utf-8').read()
    b = s.find('<main'); e = s.find('</main>')
    assert '—' not in s[b:e] and '–' not in s[b:e], path
    t = re.search(r'<title>(.*?)</title>', s).group(1)
    d = re.search(r'<meta content="([^"]*)" name="description"', s).group(1)
    print('%-58s title=%2d desc=%3d' % (path.replace(ROOT, ''), len(html.unescape(t)), len(html.unescape(d))))
