"""Ehliyet Rehberi sayfalarını (rehber/) sss/index.html şablonundan üretir.

İçerik tek kaynak: scripts/rehber_icerik.py. Bir yazıyı değiştirmek için oradaki
metni düzenleyip `python3 scripts/rehber-uret.py` çalıştırın; görünen SSS ile
FAQPage yapısal verisi birlikte güncellenir. Sonra `npm run build` ve check.
"""
import re, json, sys, os, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rehber_icerik import PAGES, HUB, SRC, R, GROUPS, FOOTER, HOME_FEATURED

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
BASE = 'https://uslusurucukursu.com'
BY_KEY = {p['key']: p for p in PAGES}
SUFFIX = ' - Ankara Sincan Uslu Sürücü Kursu'
ORDER = [k for _, ks in GROUPS for k in ks]

def group_id(name):
    tr = str.maketrans('çğıöşüÇĞİÖŞÜ', 'cgiosuCGIOSU')
    return re.sub(r'[^a-z0-9]+', '-', name.translate(tr).lower()).strip('-')

GROUP_OF = {k: name for name, ks in GROUPS for k in ks}

def img_base(key):
    # Görsel dosya adı arama odaklı: <yazı>-ankara-sincan (scripts/rehber-gorsel.mjs ile aynı kural)
    return 'ehliyet-rehberi-ankara-sincan' if key == 'hub' else R[key].strip('/').split('/')[-1] + '-ankara-sincan'

def img_alt(h1):
    return '%s: Ankara Sincan Uslu Sürücü Kursu ehliyet rehberi görseli' % h1

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
    return pages + ['error/404/index.html']  # e-sinav/ tam ekran gömme, menü/footer yok

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

def sync_sitemap():
    path = ROOT + 'sitemap.xml'
    sm = open(path, encoding='utf-8').read()
    if 'xmlns:image=' not in sm:
        sm = sm.replace('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
                        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">', 1)
        assert 'xmlns:image=' in sm
    sm = re.sub(r'  <url><loc>https://uslusurucukursu\.com/rehber/.*?</url>\n', '', sm)
    def entry(url, key):
        return ('  <url><loc>%s</loc><lastmod>%s</lastmod><image:image><image:loc>%s/assets/img/rehber/%s.jpg</image:loc></image:image></url>\n'
                % (url, DATE, BASE, img_base(key)))
    lines = entry(HUB_URL, 'hub') + ''.join(entry(BASE + R[k], k) for k in ORDER)
    sm = sm.replace('</urlset>', lines + '</urlset>')
    open(path, 'w', encoding='utf-8').write(sm)

TEMPLATE = open(ROOT + 'sss/index.html', encoding='utf-8').read()
DATE = '2026-09-29'
DATE_TR = '29 Eylül 2026'
HUB_URL = BASE + '/rehber/'
SCHOOL = {"@type": "DrivingSchool", "@id": BASE + "/#school", "name": "Uslu Sürücü Kursu", "url": BASE + "/",
          "logo": BASE + "/assets/img/logo/logo.webp", "telephone": "+905320685647"}

def plain(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()

def build(url, title, desc, h1, crumbs, main, ld_nodes, ikey):
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
    img = BASE + '/assets/img/rehber/%s.jpg' % img_base(ikey)
    assert s.count('https://uslusurucukursu.com/assets/img/og/uslu-og.jpg') == 2
    s = s.replace('https://uslusurucukursu.com/assets/img/og/uslu-og.jpg', img)
    once('<meta content="630" property="og:image:height"/>', '<meta content="630" property="og:image:height"/><meta content="%s" property="og:image:alt"/>' % html.escape(img_alt(h1)))
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

CTA = ('<div class="guide-cta">\n<p><strong>Ankara’da ehliyet kursu mu arıyorsunuz?</strong> Kayıt, ders programı ve ücret için Ankara Sincan’daki Uslu Sürücü Kursu’na ulaşabilirsiniz. '
       'Pazartesi-Perşembe 09.00-19.30, Cuma-Pazar 09.00-20.30 arasında açığız.</p>\n'
       '<a class="theme-btn" href="/iletisim/">Bilgi alın <i aria-hidden="true" class="far fa-arrow-right"></i></a>'
       '<a class="guide-cta-tel" href="tel:+905320685647">0532 068 56 47</a>\n</div>\n')

def cover_html(key, h1, caption):
    return ('<figure class="guide-cover"><img alt="%s" decoding="async" height="630" src="/assets/img/rehber/%s.webp" width="1200"/>'
            '<figcaption>%s Kaynak: uslusurucukursu.com</figcaption></figure>\n') % (html.escape(img_alt(h1)), img_base(key), caption)

def image_obj(key, h1):
    return {"@type": "ImageObject", "url": BASE + '/assets/img/rehber/%s.jpg' % img_base(key), "width": 1200, "height": 630,
            "caption": img_alt(h1), "creditText": "Uslu Sürücü Kursu", "creator": SCHOOL,
            "copyrightNotice": "Uslu Sürücü Kursu", "contentLocation": {"@type": "Place", "name": "Sincan, Ankara"}}

PLACE = {"@type": "Place", "name": "Ankara, Türkiye"}

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
            '<p class="guide-meta">Son güncelleme: %s · Hazırlayan: Ankara Sincan Uslu Sürücü Kursu · Resmî kaynaklara dayanır</p>\n' % DATE_TR +
            cover_html(p['key'], p['h1'], p['card']) +
            '<p class="legal-lead">%s</p>\n' % p['lead'] + summary + p['body'].strip() + '\n' + faq_html + CTA +
            sources_html(p['sources']) + related_html(p['key']) +
            '</article>\n</div>\n</div>\n')
    nodes = [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p['h1'] + SUFFIX, "description": p['desc'],
         "inLanguage": "tr", "isPartOf": {"@id": BASE + "/#website"}, "dateModified": DATE},
        {"@type": "Article", "@id": url + "#article", "headline": p['h1'], "description": p['desc'], "inLanguage": "tr",
         "datePublished": DATE, "dateModified": DATE, "mainEntityOfPage": {"@id": url + "#webpage"},
         "image": image_obj(p['key'], p['h1']), "spatialCoverage": PLACE, "author": SCHOOL, "publisher": SCHOOL,
         "isPartOf": {"@id": HUB_URL + "#webpage"}, "citation": [SRC[k][1] for k in p['sources']]},
        {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(ans)}} for q, ans in p['faq']]},
    ]
    out = build(url, p['h1'] + SUFFIX, p['desc'], p['h1'],
                [('Ana Sayfa', BASE + '/'), ('Ehliyet Rehberi', HUB_URL), (p['crumb'], url)], main, nodes, p['key'])
    path = ROOT + R[p['key']].strip('/') + '/index.html'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(out)
    written.append(path)

SEARCH_FORM = ('<form action="/rehber/" class="guide-search" id="guide-search" method="get" role="search">'
               '<input aria-label="Rehberde ara" autocomplete="off" maxlength="100" name="q" placeholder="Örneğin: ehliyet yenileme" type="search"/>'
               '<button aria-label="Ara" type="submit"><svg aria-hidden="true" height="18" viewBox="0 0 24 24" width="18"><circle cx="11" cy="11" fill="none" r="7" stroke="currentColor" stroke-width="2.4"/>'
               '<path d="M20 20l-4-4" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="2.4"/></svg><span>Ara</span></button></form>')

# Merkez sayfa: tam genişlik. Üstte açıklama + kategori düğmeleri ve kapak, sonra en çok aranan 3 yazı,
# her kategori için iki sütunlu soru listesi (data-ara: aramanın da baktığı SSS soruları), kısa cevaplar; en altta solda kaynaklar, sağda iletişim.
esc_attr = lambda t: html.escape(t, quote=True)
hub_chips = ''.join('<a href="#%s">%s <small>%d</small></a>' % (group_id(name), name, len(keys)) for name, keys in GROUPS)
hub_featured = ''.join(
    '<a class="home-guide-feature" href="%s"><img alt="%s" decoding="async" height="630" loading="lazy" src="/assets/img/rehber/%s.webp" width="1200"/>'
    '<span class="home-guide-body"><span class="home-guide-cat">%s</span><strong>%s</strong><span class="home-guide-text">%s</span></span></a>'
    % (R[k], esc_attr(img_alt(BY_KEY[k]['h1'])), img_base(k), GROUP_OF[k], BY_KEY[k]['h1'], BY_KEY[k]['card']) for k in HOME_FEATURED[:3])
hub_groups = ''.join(
    '<section class="guide-hub-group"><div class="guide-hub-group-head"><h2 id="%s">%s</h2><span>%d yazı</span></div><ul class="guide-hub-list">%s</ul></section>\n'
    % (group_id(name), name, len(keys),
       ''.join('<li data-ara="%s"><a href="%s"><span><strong>%s</strong><small>%s</small></span></a></li>'
               % (esc_attr(' '.join(q for q, _ in BY_KEY[k]['faq'])), R[k], BY_KEY[k]['h1'], BY_KEY[k]['card']) for k in keys))
    for name, keys in GROUPS)
quick = ''.join('<div><h3>%s</h3>\n<p>%s <a href="%s">Ayrıntılar</a></p></div>\n' % (q, ans, R[k]) for q, ans, k in HUB['quick'])
main = (breadcrumb_html(HUB['h1'], [('Ehliyet Rehberi', '/rehber/')]) +
        '<div class="guide-hub">\n<div class="container">\n'
        '<div class="guide-hub-intro"><div>'
        '<h2 class="guide-hub-title">Aradığınız sorunun <span>cevabı burada</span></h2>\n'
        '<p class="guide-meta">Son güncelleme: %s · Hazırlayan: Ankara Sincan Uslu Sürücü Kursu</p>\n' % DATE_TR +
        '<p class="guide-hub-lead">%s</p>\n' % HUB['lead'] + SEARCH_FORM + '\n' +
        '<nav aria-label="Rehber kategorileri" class="home-guide-chips guide-hub-chips">%s</nav></div>\n' % hub_chips +
        '<div class="guide-hub-cover"><img alt="%s" decoding="async" height="630" src="/assets/img/rehber/%s.webp" width="1200"/></div></div>\n'
        % (esc_attr(img_alt(HUB['h1'])), img_base('hub')) +
        '<section class="guide-hub-top"><h2 class="guide-hub-h">En çok aranan sorular</h2>\n<div class="guide-hub-featured">%s</div></section>\n' % hub_featured +
        '<p aria-live="polite" class="guide-search-info" hidden id="guide-search-info"></p>\n' +
        hub_groups +
        '<section class="guide-hub-quick"><h2 class="guide-hub-h">Kısa cevaplar</h2>\n<div class="guide-hub-qa">\n%s</div></section>\n' % quick +
        '<div class="legal-text guide-text guide-hub-end">\n<div>' + sources_html(HUB['sources']) + '</div>\n' + CTA + '</div>\n'
        '</div>\n</div>\n<script defer src="/assets/js/rehber-arama.js"></script>\n')
nodes = [
    {"@type": "CollectionPage", "@id": HUB_URL + "#webpage", "url": HUB_URL, "name": HUB['h1'] + SUFFIX, "description": HUB['desc'],
     "image": image_obj('hub', HUB['h1']), "spatialCoverage": PLACE,
     "inLanguage": "tr", "isPartOf": {"@id": BASE + "/#website"}, "dateModified": DATE, "publisher": SCHOOL,
     "mainEntity": {"@type": "ItemList", "itemListElement": [
         {"@type": "ListItem", "position": i + 1, "url": BASE + R[p['key']], "name": p['h1']} for i, p in enumerate(PAGES)]}},
]
out = build(HUB_URL, HUB['h1'] + SUFFIX, HUB['desc'], HUB['h1'], [('Ana Sayfa', BASE + '/'), ('Ehliyet Rehberi', HUB_URL)], main, nodes, 'hub')
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

HOME_START, HOME_END = '<!-- rehber home -->', '<!-- rehber home end -->'

def home_section():
    # Kompakt vitrin: solda görselli öne çıkan yazı, sağda en çok aranan 6 soru, altta kategoriler.
    esc = lambda t: html.escape(t, quote=True)
    lead, rest = HOME_FEATURED[0], HOME_FEATURED[1:7]
    p = BY_KEY[lead]
    feature = ('<a class="home-guide-feature" href="%s"><img alt="%s" decoding="async" height="630" loading="lazy" src="/assets/img/rehber/%s.webp" width="1200"/>'
               '<span class="home-guide-body"><span class="home-guide-cat">%s</span><strong>%s</strong><span class="home-guide-text">%s</span><span class="home-guide-go">Okumaya başla</span></span></a>'
               % (R[lead], esc(img_alt(p['h1'])), img_base(lead), GROUP_OF[lead], p['h1'], p['card']))
    top = ''.join('<li><a href="%s"><span class="home-guide-q"><span class="home-guide-cat">%s</span><strong>%s</strong></span></a></li>'
                  % (R[k], GROUP_OF[k], BY_KEY[k]['h1']) for k in rest)
    chips = ''.join('<a href="/rehber/#%s">%s <small>%d</small></a>' % (group_id(name), name, len(ks)) for name, ks in GROUPS)
    return (HOME_START + '\n<section aria-labelledby="home-guide-title" class="home-guide"><div class="container">'
            '<div class="site-heading text-center"><span class="site-title-tagline">Ehliyet Rehberi</span>'
            '<h2 class="site-title" id="home-guide-title">Aradığınız sorunun <span>cevabı burada</span></h2>'
            '<p class="home-guide-lead">Ehliyetle ilgili %d soruya resmî kaynaklara dayanan kısa cevaplar.</p>%s</div>'
            '<div class="home-guide-main">%s<div class="home-guide-top"><h3 class="home-guide-sub">En çok aranan sorular</h3><ol class="home-guide-list">%s</ol></div></div>'
            '<div class="home-guide-foot"><nav aria-label="Rehber kategorileri" class="home-guide-chips">%s</nav>'
            '<a class="theme-btn" href="/rehber/">%d sorunun tümü <i aria-hidden="true" class="far fa-arrow-right"></i></a></div>'
            '</div></section>\n' % (len(PAGES), SEARCH_FORM, feature, top, chips, len(PAGES)) + HOME_END)

def sync_home():
    # Bölüm eğitmenlerin (son team-area) altında durur; yeri değişirse eskisi kaldırılıp yeniden eklenir.
    path = ROOT + 'index.html'
    h = open(path, encoding='utf-8').read()
    h = re.sub('\n?' + re.escape(HOME_START) + '.*?' + re.escape(HOME_END), '', h, count=1, flags=re.S)
    anchor = '<!-- team-area end -->'
    assert h.count(anchor) == 2
    i = h.rindex(anchor) + len(anchor)
    h = h[:i] + '\n' + home_section() + h[i:]
    assert h.count(HOME_START) == 1
    open(path, 'w', encoding='utf-8').write(h)

def sync_report_names():
    # Haftalık e-posta raporu rehber sayfalarını adres yerine başlığıyla yazar (api/haftalik-rapor.js).
    names = {R[p['key']]: p['h1'] for p in PAGES}
    open(ROOT + 'api/_rehber-adlari.json', 'w', encoding='utf-8').write(json.dumps(names, ensure_ascii=False, indent=0, sort_keys=True) + '\n')

sync_home()
sync_sitemap()
sync_report_names()
