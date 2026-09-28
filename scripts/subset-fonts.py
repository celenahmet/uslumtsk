"""Keep the Font Awesome glyphs used by the generated CSS. Run after build-css.mjs."""
from pathlib import Path
import re
from fontTools import subset
from fontTools.ttLib import TTFont
p = Path('assets/css/site.min.css')
css = p.read_text()
points = {int(c, 16) for c in re.findall(r'''content:["']\\([0-9a-fA-F]+)''', css)}
for name in sorted(set(re.findall(r'''\.\./fonts/(fa-[^)"']+\.woff2)''', css))):
    font = TTFont(Path('assets/fonts') / name)
    sub = subset.Subsetter()
    sub.populate(unicodes=points)
    sub.subset(font)
    name_out = name.replace('.woff2', '-subset.woff2')
    font.flavor = 'woff2'
    font.save(Path('assets/fonts') / name_out)
    css = css.replace('../fonts/' + name, '../fonts/' + name_out)
# Modern browsers use WOFF2; old source variants stay available in original CSS.
def modern_face(match):
    face = match[0]
    if 'Font Awesome' not in face:
        return face
    face = re.sub(r'src:[^;}]*;?', '', face)
    original = match[0]
    url = re.search(r'url\([^)]*\.woff2\)[^,;}]*', original)
    return face[:-1] + ';src:' + url[0] + '}' if url else original
css = re.sub(r'@font-face\{[^}]+\}', modern_face, css)
p.write_text(css)
print(f'Subset icon fonts: {len(points)} codepoints')
