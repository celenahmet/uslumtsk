"""Switch public guide cover references after the entire approved set exists."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://uslusurucukursu.com'
ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
sitemap = ROOT / 'sitemap.xml'
urls = [e.text for e in ET.parse(sitemap).findall('s:url/s:loc', ns)]
pattern = re.compile(r'(/assets/img/rehber/[a-z0-9-]+-ankara-sincan)(?!-cover-v2)((?:-(?:480|800))?\.(?:jpg|webp))')
targets = [ROOT / (urlparse(url).path.lstrip('/') + 'index.html') for url in urls]
targets.append(sitemap)
pending = []
changed_urls = []
for file in targets:
    before = file.read_text()
    after = pattern.sub(r'\1-cover-v2\2', before)
    if file == sitemap:
        for url in changed_urls:
            entry = r'(<url>\s*<loc>' + re.escape(url) + r'</loc>\s*<lastmod>)[^<]+(</lastmod>)'
            after = re.sub(entry, lambda m: m[1] + '2026-10-28' + m[2], after)
    for image in re.findall(r'/assets/img/rehber/[a-z0-9-]+-cover-v2(?:-(?:480|800))?\.(?:jpg|webp)', after):
        if not (ROOT / image.lstrip('/')).is_file():
            raise SystemExit(f'Missing new cover: {image}; no references changed')
    if before != after:
        pending.append((file, after))
        if file != sitemap:
            route = '/' + str(file.relative_to(ROOT)).removesuffix('index.html')
            changed_urls.append(BASE + route)
for file, after in pending:
    file.write_text(after)
print(f'Installed approved guide cover references in {len(pending)} public HTML/sitemap files')
