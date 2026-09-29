// Ehliyet Rehberi görsel serisi: her yazı için tek şablondan kapak üretir.
//   Dosya adı arama odaklı: <yazı>-ankara-sincan (rehber-uret.py img_base ile aynı kural)
//   assets/img/rehber/<slug>.jpg         1200x630 paylaşım görseli (og:image)
//   assets/img/rehber/<slug>.webp        1200x630 sayfa içi kapak
//   assets/img/rehber/<slug>-800.webp    export-site.mjs bunları srcset'e ekler
//   assets/img/rehber/<slug>-480.webp    (rehber sayfasındaki kartlar da bunu kullanır)
// İçerik tek kaynak: scripts/rehber_icerik.py (başlık = h1, alt satır = card).
// Kullanım: node scripts/rehber-gorsel.mjs   (Google Chrome kurulu olmalı)
import { execFileSync, spawn } from 'node:child_process';
import fs from 'node:fs';
import http from 'node:http';
import path from 'node:path';

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const OUT = path.join(ROOT, 'assets/img/rehber');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const PORT = 8791, DEBUG = 9361;

const items = JSON.parse(execFileSync('python3', ['-c', `
import json, sys
sys.path.insert(0, 'scripts')
from rehber_icerik import PAGES, GROUPS, R, HUB
by = {p['key']: p for p in PAGES}
order = [k for _, ks in GROUPS for k in ks]
out = [{'slug': R[k].strip('/').split('/')[-1] + '-ankara-sincan', 'title': by[k]['h1'], 'sub': by[k]['card'],
        'label': 'REHBER · %02d/%02d' % (i + 1, len(order))} for i, k in enumerate(order)]
out.append({'slug': 'ehliyet-rehberi-ankara-sincan', 'title': HUB['h1'], 'sub': 'Belgeler, sınavlar, masraflar ve ehliyet sonrası: resmî kaynaklı %d yazı.' % len(order),
            'label': 'REHBER · %d YAZI' % len(order)})
print(json.dumps(out, ensure_ascii=False))
`], { cwd: ROOT, encoding: 'utf8' }));

const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const page = (it) => `<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>
*{margin:0;box-sizing:border-box}
html,body{width:1200px;height:630px;overflow:hidden;background:#041e37;color:#fff;font-family:-apple-system,system-ui,"Segoe UI",sans-serif}
.k{position:relative;width:1200px;height:630px;padding:54px 72px 0 92px}
.bar{position:absolute;left:0;top:0;bottom:0;width:18px;background:#cb1643}
.top{display:flex;justify-content:space-between;align-items:center}
.logo{height:78px;width:auto}
.seri{font-size:21px;font-weight:700;letter-spacing:3px;background:#cb1643;padding:10px 18px;border-radius:4px}
h1{font-size:70px;line-height:1.08;font-weight:800;letter-spacing:-.5px;margin-top:64px;max-width:1010px;text-wrap:balance}
.cizgi{width:96px;height:6px;background:#cb1643;margin-top:26px}
p{font-size:30px;line-height:1.35;color:#c9d4e0;margin-top:22px;max-width:930px}
.alt{position:absolute;left:92px;right:72px;bottom:42px;display:flex;justify-content:space-between;align-items:center;border-top:2px solid rgba(255,255,255,.16);padding-top:20px;font-size:24px;color:#9fb1c4}
.alt b{color:#fff;font-weight:700}
</style></head><body><div class="k"><div class="bar"></div>
<div class="top"><img class="logo" src="/assets/img/logo/logo-white.webp" alt=""><div class="seri">${esc(it.label)}</div></div>
<h1 id="t">${esc(it.title)}</h1><div class="cizgi"></div><p>${esc(it.sub)}</p>
<div class="alt"><span>Kaynak: <b>uslusurucukursu.com</b></span><span>Ankara Sincan · Uslu Sürücü Kursu</span></div>
</div><script>const t=document.getElementById('t');let f=70;while(t.offsetHeight>165&&f>44){f-=2;t.style.fontSize=f+'px'}</script></body></html>`;

const server = http.createServer((req, res) => {
  const u = new URL(req.url, 'http://x');
  if (u.pathname === '/__sablon') { res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' }); return res.end(page(items[Number(u.searchParams.get('i'))])); }
  const file = path.join(ROOT, decodeURIComponent(u.pathname));
  if (!file.startsWith(ROOT + '/assets/') || !fs.existsSync(file)) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'content-type': 'image/webp' }); fs.createReadStream(file).pipe(res);
}).listen(PORT, '127.0.0.1');

const chrome = spawn(CHROME, ['--headless=new', `--remote-debugging-port=${DEBUG}`, '--no-first-run', '--user-data-dir=/tmp/uslu-rehber-gorsel', 'about:blank'], { stdio: 'ignore' });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let tabs;
for (let i = 0; i < 40 && !tabs; i++) { await sleep(250); tabs = await fetch(`http://127.0.0.1:${DEBUG}/json`).then((r) => r.json()).catch(() => null); }
const ws = new WebSocket(tabs.find((t) => t.type === 'page').webSocketDebuggerUrl);
await new Promise((r) => ws.addEventListener('open', r));
let id = 0; const pending = new Map();
ws.addEventListener('message', (e) => { const m = JSON.parse(e.data); if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); } });
const send = (method, params = {}) => new Promise((r) => { const i = ++id; pending.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
await send('Page.enable');
await send('Emulation.setDeviceMetricsOverride', { width: 1200, height: 630, deviceScaleFactor: 1, mobile: false });
fs.mkdirSync(OUT, { recursive: true });
const shot = async (format, scale, quality) => {
  const r = await send('Page.captureScreenshot', { format, quality, clip: { x: 0, y: 0, width: 1200, height: 630, scale } });
  return Buffer.from(r.result.data, 'base64');
};
for (let i = 0; i < items.length; i++) {
  await send('Page.navigate', { url: `http://127.0.0.1:${PORT}/__sablon?i=${i}` });
  await sleep(700);
  const s = items[i].slug;
  fs.writeFileSync(path.join(OUT, `${s}.jpg`), await shot('jpeg', 1, 86));
  fs.writeFileSync(path.join(OUT, `${s}.webp`), await shot('webp', 1, 82));
  fs.writeFileSync(path.join(OUT, `${s}-800.webp`), await shot('webp', 800 / 1200, 82));
  fs.writeFileSync(path.join(OUT, `${s}-480.webp`), await shot('webp', 480 / 1200, 82));
}
ws.close(); chrome.kill(); server.close();
console.log(`Rehber görselleri: ${items.length} × 4 dosya -> assets/img/rehber/`);
