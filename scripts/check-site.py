"""Dependency-free checks of every indexable static page and its local links."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://uslusurucukursu.com'
class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.tags=[]; self.json_blocks=[]; self.in_json=False; self.chunk=''; self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs); self.tags.append((tag,attrs))
        if tag=='script' and attrs.get('type')=='application/ld+json': self.in_json=True;self.chunk=''
    def handle_data(self, data):
        if self.in_json:self.chunk+=data
    def handle_endtag(self, tag):
        if tag=='script' and self.in_json:self.json_blocks.append(json.loads(self.chunk));self.in_json=False

errors=[]
def check(ok, message):
    if not ok:errors.append(message)
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls=[e.text for e in ET.parse(ROOT/'sitemap.xml').findall('s:url/s:loc',ns)]
check(len(urls)==len(set(urls)), 'Duplicate sitemap URL')
for url in urls:
    path=ROOT/urlparse(url).path.lstrip('/')/'index.html'
    check(path.is_file(),f'Missing sitemap page: {path}')
    if not path.is_file():continue
    d=Document(path.read_text());tags=d.tags
    check(sum(t=='h1' for t,a in tags)==1,f'{path}: expected exactly one H1')
    check(any(t=='html' and a.get('lang')==('en' if '/en/' in url else 'tr') for t,a in tags),f'{path}: language')
    check(any(t=='meta' and a.get('name')=='description' and a.get('content') for t,a in tags),f'{path}: description')
    check(sum(t=='link' and a.get('rel')=='canonical' and a.get('href')==url for t,a in tags)==1,f'{path}: canonical')
    check(not any(t=='meta' and a.get('name')=='robots' and 'noindex' in a.get('content','') for t,a in tags),f'{path}: noindex sitemap page')
    check(bool(d.json_blocks),f'{path}: missing structured data')
    for tag,a in tags:
        if tag=='img':
            check('alt' in a,f'{path}: missing alt')
            check('width' in a and 'height' in a,f'{path}: missing dimensions {a.get("src")}')
        if tag=='iframe':check(bool(a.get('title')),f'{path}: untitled frame')
        for attr in ('href','src'):
            value=a.get(attr,'');parsed=urlparse(value)
            if parsed.scheme or parsed.netloc or not parsed.path:continue
            target=ROOT/unquote(parsed.path).lstrip('/') if parsed.path.startswith('/') else path.parent/unquote(parsed.path)
            check(target.exists(),f'{path.relative_to(ROOT)}: missing {value}')
        if tag=='link' and a.get('rel')=='alternate':check(a.get('href') in urls,f'{path}: invalid alternate')
check(BASE+'/sitemap.xml' in (ROOT/'robots.txt').read_text(),'robots sitemap mismatch')
if errors:
    print('\n'.join(errors));raise SystemExit(1)
print(f'PASS: {len(urls)} pages; H1, language, metadata, canonical, hreflang, JSON-LD, image dimensions, frames and local links.')
