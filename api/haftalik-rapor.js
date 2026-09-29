// Haftalık web sitesi özeti → e-posta (Resend). Vercel Cron her pazartesi çağırır.
//
// Okur teknik bilgisi olmayan kurs sahibi: rakamlar yuvarlak, terimler açıklamalı,
// her hafta tek bir uygulanabilir öneri. Veri kaynakları isteğe bağlı; bağlı olmayan
// kaynağın bölümü e-postada hiç görünmez:
//  - Cloudflare Web Analytics (çerezsiz ziyaret sayısı): CF_API_TOKEN, CF_ACCOUNT_ID, CF_SITE_TAG
//  - Google Search Console (Google aramasında görünme/tıklama): GSC_CLIENT_EMAIL,
//    GSC_PRIVATE_KEY, GSC_SITE (örn. "sc-domain:uslusurucukursu.com")
//
// Güvenlik:
//  - Yalnız GET ve yalnız `Authorization: Bearer <CRON_SECRET>` ile (Vercel Cron bu
//    başlığı kendisi ekler). Şifresiz istek 401; fonksiyon dışarıdan tetiklenemez.
//  - Alıcılar kodda değil ortam değişkeninde (depo herkese açık): REPORT_TO (virgüllü
//    liste). `?test=1` yalnız REPORT_TEST_TO adresine, konuya [Deneme] ekleyerek gider;
//    `&ornek=1` bağlı kaynak yokken tasarımı göstermek için ÖRNEK veriyle doldurur.
//  - Kişisel veri işlenmez: kaynaklar yalnız toplam sayılar ve sayfa/kelime listesi verir.
'use strict';

const crypto = require('node:crypto');

const FROM = 'Uslu Sürücü Kursu Web Sitesi <rapor@uslusurucukursu.com>';
const SITE = 'https://uslusurucukursu.com';
// Ziyaret sayımı (Cloudflare) bu tarihte başladı: öncesi için veri yok, karşılaştırma yapılmaz.
const CF_START = new Date('2026-09-28T21:00:00Z'); // 29 Eylül 2026, Türkiye gece yarısı

// Sayfa yolları → kurs sahibinin tanıdığı adlar
const PAGE_NAMES = {
  '/': 'Ana sayfa',
  '/hakkimizda/': 'Hakkımızda',
  '/iletisim/': 'İletişim',
  '/sss/': 'Sık sorulan sorular',
  '/yorumlar/': 'Öğrenci yorumları',
  '/egitim/': 'Eğitimler',
  '/egitim/manuel-b/': 'B sınıfı manuel ehliyet',
  '/egitim/otomatik-b/': 'B sınıfı otomatik ehliyet',
  '/egitim/motor-a1/': 'A1 motosiklet ehliyeti',
  '/egitim/motor-a2/': 'A2 motosiklet ehliyeti',
  '/egitim/ozel/': 'Özel direksiyon dersi',
  '/egitim/ozel-ab/': 'Özel gereksinimli A-B sınıfı',
  '/egitim/diger/': 'Büyük araç ehliyetleri',
  '/galeri/genel/': 'Fotoğraf galerisi',
  '/galeri/araclar/': 'Eğitim araçları',
  '/galeri/siniflar/': 'Eğitim sınıfları',
  '/e-sinav/': 'e-Sınav uygulaması',
  '/kvkk/': 'KVKK aydınlatma metni',
  '/en/': 'İngilizce ana sayfa',
  '/rehber/': 'Ehliyet Rehberi'
};
// Rehber yazılarının başlıkları; scripts/rehber-uret.py üretir.
const GUIDE_NAMES = require('./_rehber-adlari.json');
function pageName(path) {
  if (PAGE_NAMES[path]) return PAGE_NAMES[path];
  return GUIDE_NAMES[path] ? 'Rehber: ' + GUIDE_NAMES[path] : path;
}

// Her hafta sırayla bir öneri (ISO hafta numarasına göre döner).
const TIPS = [
  'Google İşletme Profilinizdeki yeni yorumlara kısa bir teşekkürle yanıt verin; yanıtlanan yorumlar yeni adaylara güven verir.',
  'Kursu bitiren memnun öğrencilerinizden Google’da yorum yazmalarını rica edin. Yorum sayısı, “Sincan sürücü kursu” aramalarında öne çıkmanıza yardım eder.',
  'Instagram biyografinize sitenizin adresini (uslusurucukursu.com) ekleyin; Instagram’dan gelen ziyaretçiler doğrudan teklif isteyebilir.',
  'Yeni bir kurs dönemi ya da kampanya başlıyorsa bize yazın; sitede duyuralım, sitenin asistanı da buna göre yönlendirsin.',
  'Sitedeki fotoğrafların güncel olması güven verir. Yeni araç ya da sınıf fotoğrafınız varsa gönderin, galeriye ekleyelim.',
  'Telefonla gelen sorulardan en sık tekrarlananları bize iletin; “Sık sorulan sorular” sayfasına ekleyelim, hem Google’da hem yapay zeka aramalarında görünürlüğünüz artar.'
];

/* ------------------------------------------------------------ yardımcılar */
function esc(v) {
  return String(v).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}
function fmt(n) {
  return Math.round(n).toLocaleString('tr-TR');
}
const MONTHS = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];
function trDate(d) {
  return d.getUTCDate() + ' ' + MONTHS[d.getUTCMonth()];
}
function isoDay(d) {
  return d.toISOString().slice(0, 10);
}
const TR_MS = 3 * 3600 * 1000;
const WEEKDAYS = ['Pazar', 'Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi'];
// Ortalama sıra tam sayıya yuvarlanır: 5,6 → "6."
function rank(pos) {
  return Math.max(1, Math.round(pos)) + '.';
}
function change(cur, prev) {
  if (!prev) return cur ? 'yeni' : '';
  const p = Math.round(((cur - prev) / prev) * 100);
  if (p === 0) return 'geçen haftayla aynı';
  return (p > 0 ? '▲ %' + p : '▼ %' + Math.abs(p)) + ' geçen haftaya göre';
}
function isoWeek(d) {
  const t = new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate()));
  t.setUTCDate(t.getUTCDate() + 4 - (t.getUTCDay() || 7));
  const y = new Date(Date.UTC(t.getUTCFullYear(), 0, 1));
  return Math.ceil(((t - y) / 86400000 + 1) / 7);
}
async function fetchJson(url, opts, ms) {
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), ms || 10000);
  try {
    const r = await fetch(url, Object.assign({}, opts, { signal: ctrl.signal }));
    const body = await r.json().catch(() => null);
    return { ok: r.ok, status: r.status, body };
  } finally {
    clearTimeout(timer);
  }
}

// Rapor haftası: Türkiye saatiyle bir önceki pazartesi 00.00 ile bu pazartesi 00.00 arası.
function weekRange(now) {
  const tr = new Date(now.getTime() + 3 * 3600 * 1000);
  const dow = tr.getUTCDay() || 7; // pazartesi 1
  const mondayTr = Date.UTC(tr.getUTCFullYear(), tr.getUTCMonth(), tr.getUTCDate() - (dow - 1));
  const end = new Date(mondayTr - 3 * 3600 * 1000); // TR pazartesi 00.00 → UTC
  const start = new Date(end.getTime() - 7 * 86400000);
  const prevStart = new Date(start.getTime() - 7 * 86400000);
  return { start, end, prevStart };
}

/* ------------------------------------------------ Cloudflare Web Analytics */
async function cloudflare(range) {
  const token = process.env.CF_API_TOKEN, account = process.env.CF_ACCOUNT_ID, site = process.env.CF_SITE_TAG;
  if (!token || !account || !site) return null;
  const query = `query($a: String!, $f: AccountRumPageloadEventsAdaptiveGroupsFilter_InputObject, $p: AccountRumPageloadEventsAdaptiveGroupsFilter_InputObject) {
    viewer { accounts(filter: { accountTag: $a }) {
      total: rumPageloadEventsAdaptiveGroups(limit: 1, filter: $f) { count sum { visits } }
      prev: rumPageloadEventsAdaptiveGroups(limit: 1, filter: $p) { count sum { visits } }
      pages: rumPageloadEventsAdaptiveGroups(limit: 100, filter: $f, orderBy: [count_DESC]) { count dimensions { requestPath } }
      refs: rumPageloadEventsAdaptiveGroups(limit: 8, filter: $f, orderBy: [sum_visits_DESC]) { sum { visits } dimensions { refererHost } }
      devices: rumPageloadEventsAdaptiveGroups(limit: 5, filter: $f, orderBy: [count_DESC]) { count dimensions { deviceType } }
    } }
  }`;
  // Sayımdan önceki günler aralıktan çıkarılır. Hafta tümüyle sayımdan önceyse (ilk özet)
  // sayımın başladığı günden bu yana olan ziyaretler gösterilir.
  const start = range.start < CF_START ? CF_START : range.start;
  const end = range.end > start ? range.end : new Date();
  const hasPrev = range.prevStart >= CF_START;
  const f = { AND: [{ siteTag: site }, { datetime_geq: start.toISOString(), datetime_lt: end.toISOString() }] };
  const p = { AND: [{ siteTag: site }, { datetime_geq: range.prevStart.toISOString(), datetime_lt: range.start.toISOString() }] };
  const r = await fetchJson('https://api.cloudflare.com/client/v4/graphql', {
    method: 'POST',
    headers: { Authorization: 'Bearer ' + token, 'Content-Type': 'application/json' },
    body: JSON.stringify({ query, variables: { a: account, f, p } })
  });
  const acc = r.body && r.body.data && r.body.data.viewer && r.body.data.viewer.accounts && r.body.data.viewer.accounts[0];
  if (!r.ok || !acc) {
    console.error('rapor: cloudflare durum ' + r.status);
    return null;
  }
  const tot = acc.total[0] || { count: 0, sum: { visits: 0 } };
  const prev = acc.prev[0] || { count: 0, sum: { visits: 0 } };
  // Kaynakları sade gruplara indir
  const groups = { Google: 0, Instagram: 0, 'Doğrudan / kayıtlı bağlantı': 0, Diğer: 0 };
  for (const x of acc.refs) {
    const h = String(x.dimensions.refererHost || '').toLowerCase();
    const v = x.sum.visits;
    if (!h || h.includes('uslusurucukursu')) groups['Doğrudan / kayıtlı bağlantı'] += v;
    else if (h.includes('google')) groups.Google += v;
    else if (h.includes('instagram')) groups.Instagram += v;
    else groups['Diğer'] += v;
  }
  const devTotal = acc.devices.reduce((s, x) => s + x.count, 0) || 1;
  const mobile = acc.devices.filter((x) => /mobile|tablet/i.test(x.dimensions.deviceType)).reduce((s, x) => s + x.count, 0);
  const pages = acc.pages.map((x) => [x.dimensions.requestPath, x.count]);
  const guide = pages.filter((x) => GUIDE_NAMES[x[0]]);
  const [hours, speed] = await Promise.all([
    cfHours(token, account, site, start, end).catch(() => null),
    cfSpeed(token, account, site, start, end).catch(() => null)
  ]);
  return {
    visits: tot.sum.visits,
    prevVisits: hasPrev ? prev.sum.visits : null,
    partial: start > range.start || end > range.end ? { from: start, to: end } : null,
    views: tot.count,
    pages,
    sources: Object.entries(groups).filter((e) => e[1] > 0).sort((a, b) => b[1] - a[1]),
    mobilePct: Math.round((mobile / devTotal) * 100),
    guideViews: guide.reduce((n, x) => n + x[1], 0),
    guideTop: guide.slice(0, 3).map((x) => [GUIDE_NAMES[x[0]], x[1]]),
    days: hours && hours.days,
    blocks: hours && hours.blocks,
    loadSec: speed
  };
}

// Ek sorgular temel sorgudan ayrıdır: biri alınamazsa yalnız o bölüm e-postadan düşer, sebebi günlüğe yazılır.
async function cfQuery(token, query, variables, label) {
  const r = await fetchJson('https://api.cloudflare.com/client/v4/graphql', {
    method: 'POST',
    headers: { Authorization: 'Bearer ' + token, 'Content-Type': 'application/json' },
    body: JSON.stringify({ query, variables })
  });
  const acc = r.body && r.body.data && r.body.data.viewer && r.body.data.viewer.accounts && r.body.data.viewer.accounts[0];
  if (!r.ok || !acc) {
    const why = r.body && r.body.errors && r.body.errors[0] && r.body.errors[0].message;
    console.error('rapor: cloudflare ' + label + ' durum ' + r.status + (why ? ' ' + String(why).slice(0, 160) : ''));
    return null;
  }
  return acc;
}
// Ziyaretler Türkiye saatine göre günlere ve dört zaman dilimine dağıtılır.
const BLOCKS = ['Sabah (06.00-12.00)', 'Öğleden sonra (12.00-17.00)', 'Akşam (17.00-22.00)', 'Gece (22.00-06.00)'];
async function cfHours(token, account, site, start, end) {
  const acc = await cfQuery(token, `query($a: String!, $f: AccountRumPageloadEventsAdaptiveGroupsFilter_InputObject) {
    viewer { accounts(filter: { accountTag: $a }) {
      hours: rumPageloadEventsAdaptiveGroups(limit: 200, filter: $f) { sum { visits } dimensions { datetimeHour } }
    } }
  }`, { a: account, f: { AND: [{ siteTag: site }, { datetime_geq: start.toISOString(), datetime_lt: end.toISOString() }] } }, 'saat');
  if (!acc) return null;
  const days = new Map();
  for (let t = new Date(start.getTime() + TR_MS); t < new Date(end.getTime() + TR_MS); t = new Date(t.getTime() + 86400000)) days.set(isoDay(t), 0);
  const blocks = [0, 0, 0, 0];
  for (const x of acc.hours) {
    const t = new Date(new Date(x.dimensions.datetimeHour).getTime() + TR_MS);
    const h = t.getUTCHours(), v = x.sum.visits;
    if (days.has(isoDay(t))) days.set(isoDay(t), days.get(isoDay(t)) + v);
    blocks[h >= 6 && h < 12 ? 0 : h >= 12 && h < 17 ? 1 : h >= 17 && h < 22 ? 2 : 3] += v;
  }
  return { days: [...days.entries()], blocks };
}
// Sayfanın açılma süresi: ziyaretlerin yarısı bu süreden kısa (medyan). Cloudflare mikro saniye verir.
async function cfSpeed(token, account, site, start, end) {
  const acc = await cfQuery(token, `query($a: String!, $f: AccountRumPerformanceEventsAdaptiveGroupsFilter_InputObject) {
    viewer { accounts(filter: { accountTag: $a }) {
      perf: rumPerformanceEventsAdaptiveGroups(limit: 1, filter: $f) { count quantiles { pageLoadTimeP50 } }
    } }
  }`, { a: account, f: { AND: [{ siteTag: site }, { datetime_geq: start.toISOString(), datetime_lt: end.toISOString() }] } }, 'hiz');
  const x = acc && acc.perf && acc.perf[0];
  return x && x.count && x.quantiles && x.quantiles.pageLoadTimeP50 ? x.quantiles.pageLoadTimeP50 / 1e6 : null;
}

/* ---------------------------------------------------- Google Search Console */
function b64url(v) {
  return Buffer.from(v).toString('base64').replace(/=+$/, '').replace(/\+/g, '-').replace(/\//g, '_');
}
async function googleToken() {
  const email = process.env.GSC_CLIENT_EMAIL, key = process.env.GSC_PRIVATE_KEY;
  if (!email || !key) return null;
  const now = Math.floor(Date.now() / 1000);
  const head = b64url(JSON.stringify({ alg: 'RS256', typ: 'JWT' }));
  const claim = b64url(JSON.stringify({
    iss: email,
    scope: 'https://www.googleapis.com/auth/webmasters.readonly',
    aud: 'https://oauth2.googleapis.com/token',
    iat: now,
    exp: now + 3600
  }));
  const signer = crypto.createSign('RSA-SHA256');
  signer.update(head + '.' + claim);
  const sig = signer.sign(key.replace(/\\n/g, '\n')).toString('base64').replace(/=+$/, '').replace(/\+/g, '-').replace(/\//g, '_');
  const r = await fetchJson('https://oauth2.googleapis.com/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({ grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer', assertion: head + '.' + claim + '.' + sig }).toString()
  });
  if (!r.ok || !r.body || !r.body.access_token) {
    console.error('rapor: google jeton durum ' + r.status);
    return null;
  }
  return r.body.access_token;
}
async function searchConsole() {
  const site = process.env.GSC_SITE;
  if (!site) return null;
  const token = await googleToken();
  if (!token) return null;
  // Google verisi 2-3 gün gecikmeli gelir: son hazır 7 gün ve ondan önceki 7 gün.
  const today = new Date();
  const end = new Date(today.getTime() - 3 * 86400000);
  const start = new Date(end.getTime() - 6 * 86400000);
  const pEnd = new Date(start.getTime() - 86400000);
  const pStart = new Date(pEnd.getTime() - 6 * 86400000);
  const url = 'https://www.googleapis.com/webmasters/v3/sites/' + encodeURIComponent(site) + '/searchAnalytics/query';
  const ask = (body) => fetchJson(url, { method: 'POST', headers: { Authorization: 'Bearer ' + token, 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
  const [cur, prev, queries, prevQueries, pages] = await Promise.all([
    ask({ startDate: isoDay(start), endDate: isoDay(end) }),
    ask({ startDate: isoDay(pStart), endDate: isoDay(pEnd) }),
    ask({ startDate: isoDay(start), endDate: isoDay(end), dimensions: ['query'], rowLimit: 250 }),
    ask({ startDate: isoDay(pStart), endDate: isoDay(pEnd), dimensions: ['query'], rowLimit: 250 }),
    ask({ startDate: isoDay(start), endDate: isoDay(end), dimensions: ['page'], rowLimit: 25 })
  ]);
  if (!cur.ok) {
    console.error('rapor: search console durum ' + cur.status);
    return null;
  }
  const row = (r) => (r.ok && r.body && r.body.rows && r.body.rows[0]) || { clicks: 0, impressions: 0, position: 0 };
  const rows = (r) => (r.ok && r.body && r.body.rows) || [];
  const c = row(cur), p = row(prev);
  // İçinde "sincan" ya da "ankara" geçen aramalar: toplam görünme/tık, görünmeye göre ağırlıklı ortalama sıra.
  // Google seyrek aramaları gizlediği için toplamlar yaklaşıktır.
  const local = (list, word) => {
    const m = list.filter((x) => x.keys[0].toLocaleLowerCase('tr').includes(word));
    const imp = m.reduce((n, x) => n + x.impressions, 0);
    return imp ? { impressions: imp, clicks: m.reduce((n, x) => n + x.clicks, 0), position: m.reduce((n, x) => n + x.position * x.impressions, 0) / imp } : null;
  };
  const localRows = [['Sincan', 'sincan'], ['Ankara', 'ankara']]
    .map((w) => ({ name: w[0], cur: local(rows(queries), w[1]), prev: local(rows(prevQueries), w[1]) }))
    .filter((x) => x.cur);
  return {
    from: start,
    to: end,
    impressions: c.impressions,
    prevImpressions: p.impressions,
    clicks: c.clicks,
    prevClicks: p.clicks,
    position: c.position,
    // En çok tıklanan, eşitlikte en çok görünen 5 arama
    queries: rows(queries)
      .map((x) => [x.keys[0], x.impressions, x.clicks, x.position])
      .sort((a, b) => b[2] - a[2] || b[1] - a[1])
      .slice(0, 5),
    local: localRows,
    // Google'da en çok görünen 5 sayfa
    pages: rows(pages)
      .map((x) => [x.keys[0].replace(SITE, '') || '/', x.impressions, x.clicks])
      .sort((a, b) => b[1] - a[1])
      .slice(0, 5)
  };
}

/* ------------------------------------------------------------------ ÖRNEK */
function sample(range) {
  return {
    cf: {
      visits: 312, prevVisits: 268, views: 845,
      pages: [['/', 402], ['/egitim/manuel-b/', 118], ['/iletisim/', 96], ['/egitim/otomatik-b/', 71], ['/hakkimizda/', 44]],
      sources: [['Google', 188], ['Doğrudan / kayıtlı bağlantı', 71], ['Instagram', 39], ['Diğer', 14]],
      mobilePct: 78,
      guideViews: 96,
      guideTop: [['Ehliyet Masrafları 2026', 31], ['Ehliyet Nasıl Alınır? Adım Adım 2026', 24], ['Ehliyet Sınavı Nasıl Yapılır?', 17]],
      days: [52, 47, 39, 44, 41, 58, 31].map((v, i) => [isoDay(new Date(range.start.getTime() + TR_MS + i * 86400000)), v]),
      blocks: [58, 84, 131, 39],
      loadSec: 1.4
    },
    gsc: {
      from: new Date(range.start.getTime() - 2 * 86400000), to: new Date(range.end.getTime() - 3 * 86400000),
      impressions: 1240, prevImpressions: 1105, clicks: 86, prevClicks: 71, position: 6.4,
      queries: [['sincan sürücü kursu', 410, 38, 3.2], ['uslu sürücü kursu', 96, 29, 1.1], ['sincan ehliyet kursu', 188, 9, 5.6], ['otomatik ehliyet sincan', 74, 4, 4.4], ['sürücü kursu fiyatları ankara', 131, 2, 12.3]],
      local: [{ name: 'Sincan', cur: { impressions: 820, clicks: 61, position: 4.6 }, prev: { impressions: 760, clicks: 52, position: 5.7 } },
        { name: 'Ankara', cur: { impressions: 214, clicks: 6, position: 13.8 }, prev: { impressions: 190, clicks: 4, position: 16.2 } }],
      pages: [['/', 640, 52], ['/rehber/ehliyet-masraflari/', 182, 9], ['/egitim/manuel-b/', 131, 11], ['/iletisim/', 88, 6], ['/rehber/ehliyet-nasil-alinir/', 76, 3]]
    }
  };
}

/* ------------------------------------------------------------------ e-posta */
// Apple Mail gibi istemciler koyu temayı desteklediğini bildirmeyen e-postanın renklerini kendisi
// ters çevirir (lacivert başlık açık maviye döner). Destek bildirilir, koyu renkler burada verilir.
const DARK_CSS = '@media (prefers-color-scheme: dark){' +
  '.dk-page{background:#121417!important}' +
  '.dk-card{background:#1c1f24!important}' +
  '.dk-head{background:#041e37!important;color:#fff!important}' +
  '.dk-text{color:#e8ecf1!important}' +
  '.dk-muted{color:#a3acb9!important}' +
  '.dk-line{border-color:#343a42!important}' +
  '.dk-note{background:#3a3000!important;color:#f3d98b!important}' +
  '.dk-link{color:#ff7a95!important}}';

function render(data, range, opts) {
  const NAVY = '#041e37', RED = '#cb1643', MUTED = '#6b7280', LINE = '#e6e9ee';
  const cf = data.cf, gsc = data.gsc;
  // Sınırlar Türkiye gece yarısı (UTC 21.00); etiket Türkiye tarihiyle yazılır.
  const TR = 3 * 3600 * 1000;
  const firstDay = new Date(range.start.getTime() + TR);
  const lastDay = new Date(range.end.getTime() + TR - 86400000);
  const weekLabel = trDate(firstDay) + ' - ' + trDate(lastDay) + ' ' + lastDay.getUTCFullYear();
  // Koyu tema: dk-* sınıfları yalnız DARK_CSS'te kullanılır; açık temada satır içi stiller geçerlidir.
  const tile = (value, label, note) =>
    '<td class="dk-card dk-line" style="width:33%;padding:14px 10px;text-align:center;border:1px solid ' + LINE + ';background:#fff">' +
    '<div class="dk-text" style="font-size:26px;font-weight:bold;color:' + NAVY + '">' + esc(value) + '</div>' +
    '<div class="dk-text" style="font-size:13px;color:' + NAVY + ';margin-top:2px">' + esc(label) + '</div>' +
    (note ? '<div class="dk-muted" style="font-size:12px;color:' + MUTED + ';margin-top:4px">' + esc(note) + '</div>' : '') + '</td>';
  const h2 = (t) => '<h2 class="dk-text" style="font-size:16px;color:' + NAVY + ';margin:26px 0 8px;border-bottom:2px solid ' + RED + ';padding-bottom:6px">' + esc(t) + '</h2>';
  const list = (rows) => '<table cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;font-size:14px">' +
    rows.map((r) => '<tr><td class="dk-text dk-line" style="padding:7px 0;border-bottom:1px solid ' + LINE + ';color:' + NAVY + '">' + esc(r[0]) + '</td><td class="dk-muted dk-line" style="padding:7px 0;border-bottom:1px solid ' + LINE + ';text-align:right;color:' + MUTED + ';white-space:nowrap">' + esc(r[1]) + '</td></tr>').join('') + '</table>';

  // Yatay çubuk listesi: [etiket, değer, sağdaki yazı]; en büyük değer tam genişlik.
  const bars = (rows) => {
    const max = Math.max.apply(null, rows.map((r) => r[1])) || 1;
    return '<table cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;font-size:14px">' +
      rows.map((r) => '<tr><td class="dk-text dk-line" style="padding:7px 12px 7px 0;border-bottom:1px solid ' + LINE + ';color:' + NAVY + ';white-space:nowrap;width:1%">' + esc(r[0]) + '</td>' +
        '<td class="dk-line" style="padding:7px 0;border-bottom:1px solid ' + LINE + '"><div style="background:' + RED + ';height:10px;border-radius:2px;width:' + (r[1] ? Math.max(3, Math.round((r[1] / max) * 100)) : 0) + '%"></div></td>' +
        '<td class="dk-muted dk-line" style="padding:7px 0 7px 12px;border-bottom:1px solid ' + LINE + ';text-align:right;color:' + MUTED + ';white-space:nowrap;width:1%">' + esc(r[2]) + '</td></tr>').join('') + '</table>';
  };
  // Sıra değişimi: küçük sayı daha iyi (yukarı çıkmak).
  const move = (cur, prev) => {
    const d = Math.round(prev) - Math.round(cur);
    return d > 0 ? ' (▲ ' + d + ')' : d < 0 ? ' (▼ ' + -d + ')' : '';
  };
  const note = (t) => '<p class="dk-muted" style="font-size:12px;color:' + MUTED + ';margin:8px 0 0;line-height:1.5">' + t + '</p>';

  let html = '<div class="dk-page" style="font-family:Arial,Helvetica,sans-serif;background:#f3f5f8;padding:20px 0"><div class="dk-card" style="max-width:600px;margin:0 auto;background:#fff;border-top:4px solid ' + RED + '">';
  html += '<div class="dk-head" style="background:' + NAVY + ';color:#fff;padding:20px 24px"><div style="font-size:13px;opacity:.8">Uslu Sürücü Kursu</div><div style="font-size:20px;font-weight:bold;margin-top:4px">Web sitenizin haftalık özeti</div><div style="font-size:13px;opacity:.8;margin-top:4px">' + esc(weekLabel) + '</div></div>';
  html += '<div style="padding:8px 24px 24px">';
  if (opts.sample) html += '<p class="dk-note" style="background:#fff7d6;border-left:3px solid #d4a300;padding:10px 12px;font-size:13px;color:#6a4b00">Bu bir <b>örnek</b> özettir; rakamlar gerçek değildir. Veri kaynakları bağlandığında bu e-posta sitenizin gerçek rakamlarıyla her pazartesi gelecek.</p>';

  const tiles = [];
  const cfNote = cf && (cf.prevVisits == null ? 'sayım 29 Eylül’de başladı' : change(cf.visits, cf.prevVisits));
  if (cf) tiles.push(tile(fmt(cf.visits), 'ziyaret', cfNote));
  if (gsc) tiles.push(tile(fmt(gsc.impressions), 'Google’da görünme', change(gsc.impressions, gsc.prevImpressions)));
  if (gsc) tiles.push(tile(fmt(gsc.clicks), 'Google’dan tıklama', change(gsc.clicks, gsc.prevClicks)));
  if (tiles.length) html += '<table cellpadding="0" cellspacing="6" style="width:100%;margin-top:14px"><tr>' + tiles.join('') + '</tr></table>';
  if (cf && cf.partial) {
    const a = trDate(new Date(cf.partial.from.getTime() + TR)), b = trDate(new Date(cf.partial.to.getTime() + TR - 1));
    html += '<p class="dk-muted" style="font-size:12px;color:' + MUTED + ';margin:8px 0 0">Ziyaret sayımı 29 Eylül’de başladı. Ziyaret rakamları ' + esc(a === b ? a + ' gününü' : a + ' - ' + b + ' arasını') + ' gösterir.</p>';
  }
  if (!cf && !gsc) html += '<p class="dk-text" style="font-size:14px;color:' + NAVY + '">Veri kaynakları henüz bağlanmadı. Bu e-posta yalnızca gönderim düzeninin çalıştığını doğrular.</p>';

  if (gsc && gsc.queries.length) {
    html += h2('İnsanlar sizi Google’da ne yazarak buldu?');
    html += list(gsc.queries.map((q) => [q[0], fmt(q[1]) + ' görünme · ' + fmt(q[2]) + ' tık · ' + rank(q[3]) + ' sıra']));
    html += '<p class="dk-muted" style="font-size:12px;color:' + MUTED + ';margin:8px 0 0">“Görünme”, sitenizin Google arama sonuçlarında listelenme sayısıdır. Google’ın verisi 2-3 gün geç geldiği için bu bölüm ' + esc(trDate(gsc.from)) + ' - ' + esc(trDate(gsc.to)) + ' arasını gösterir.' + (gsc.position ? ' Aramalarda ortalama ' + esc(rank(gsc.position)) + ' sıradasınız.' : '') + '</p>';
  }
  if (gsc && gsc.local && gsc.local.length) {
    html += h2('Sincan ve Ankara aramalarında yeriniz');
    html += list(gsc.local.map((l) => ['“' + l.name + '” geçen aramalar', fmt(l.cur.impressions) + ' görünme · ' + fmt(l.cur.clicks) + ' tık · ' + rank(l.cur.position) + ' sıra' + (l.prev ? move(l.cur.position, l.prev.position) : '')]));
    html += note('Sıra, sitenizin Google sonuçlarındaki ortalama yeridir; 1. sıra en üsttür. ▲ geçen haftaya göre yükseldiğinizi gösterir.');
  }
  if (gsc && gsc.pages && gsc.pages.length) {
    html += h2('Google’da en çok görünen sayfalarınız');
    html += list(gsc.pages.map((p) => [pageName(p[0]), fmt(p[1]) + ' görünme · ' + fmt(p[2]) + ' tık']));
  }
  if (cf && cf.pages.length) {
    html += h2('En çok bakılan sayfalar');
    html += list(cf.pages.slice(0, 5).map((p) => [pageName(p[0]), fmt(p[1]) + ' görüntülenme']));
  }
  if (cf && cf.sources.length) {
    const total = cf.sources.reduce((s, x) => s + x[1], 0) || 1;
    html += h2('Ziyaretçiler nereden geldi?');
    html += list(cf.sources.map((s) => [s[0], '%' + Math.round((s[1] / total) * 100)]));
    html += '<p class="dk-text" style="font-size:14px;color:' + NAVY + ';margin:10px 0 0;line-height:1.6">Ziyaretçilerin <b>%' + cf.mobilePct + '</b> kadarı siteye telefondan girdi.' +
      (cf.loadSec ? ' Sayfalar ziyaretçilerin yarısı için <b>' + esc(cf.loadSec.toFixed(1).replace('.', ',')) + ' saniyeden</b> kısa sürede açıldı.' : '') + '</p>';
  }
  if (cf && cf.days && cf.days.length > 1) {
    html += h2('Ziyaretler günlere göre');
    html += bars(cf.days.map((d) => {
      const t = new Date(d[0] + 'T00:00:00Z');
      return [WEEKDAYS[t.getUTCDay()] + ' ' + trDate(t), d[1], fmt(d[1])];
    }));
  }
  const blockSum = cf && cf.blocks ? cf.blocks.reduce((n, v) => n + v, 0) : 0;
  if (blockSum) {
    const top = cf.blocks.indexOf(Math.max.apply(null, cf.blocks));
    html += h2('Ziyaretçiler hangi saatlerde geldi?');
    html += bars(BLOCKS.map((b, i) => [b, cf.blocks[i], '%' + Math.round((cf.blocks[i] / blockSum) * 100)]));
    html += '<p class="dk-text" style="font-size:14px;color:' + NAVY + ';margin:10px 0 0">Ziyaretçiler en çok <b>' + esc(BLOCKS[top].split(' (')[0].toLocaleLowerCase('tr')) + '</b> saatlerinde geldi.</p>';
  }
  if (cf && cf.guideViews) {
    html += h2('Ehliyet Rehberi');
    html += '<p class="dk-text" style="font-size:14px;color:' + NAVY + ';margin:0 0 6px">Rehber yazıları bu dönemde <b>' + fmt(cf.guideViews) + '</b> kez okundu. En çok okunanlar:</p>';
    html += list(cf.guideTop.map((g) => [g[0], fmt(g[1]) + ' okunma']));
  }
  const tip = TIPS[(isoWeek(range.end) - 1) % TIPS.length];
  html += h2('Bu haftanın önerisi');
  html += '<p class="dk-text" style="font-size:14px;line-height:1.6;color:' + NAVY + ';margin:0">' + esc(tip) + '</p>';
  html += '<p class="dk-muted" style="font-size:12px;color:' + MUTED + ';margin:26px 0 0;line-height:1.5">Bu özet her pazartesi otomatik olarak gönderilir. Rakamlar yaklaşık değerlerdir; ziyaretçileri tanımlayan bir kayıt tutulmaz. Sorularınız için bu e-postayı yanıtlamanız yeterli.</p>';
  html += '<p style="font-size:12px;margin:8px 0 0"><a class="dk-link" href="' + SITE + '" style="color:' + RED + '">uslusurucukursu.com</a></p>';
  html += '</div></div></div>';
  html = '<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">' +
    '<meta name="color-scheme" content="light dark"><meta name="supported-color-schemes" content="light dark">' +
    '<style>:root{color-scheme:light dark;supported-color-schemes:light dark}' + DARK_CSS + '</style></head><body style="margin:0">' + html + '</body></html>';

  const text = ['Uslu Sürücü Kursu, web sitenizin haftalık özeti (' + weekLabel + ')', '']
    .concat(opts.sample ? ['ÖRNEK ÖZET: rakamlar gerçek değildir.', ''] : [])
    .concat(cf ? ['Ziyaret: ' + fmt(cf.visits) + ' (' + cfNote + ')'] : [])
    .concat(gsc ? ['Google’da görünme: ' + fmt(gsc.impressions), 'Google’dan tıklama: ' + fmt(gsc.clicks)] : [])
    .concat(gsc && gsc.local ? gsc.local.map((l) => '“' + l.name + '” geçen aramalarda ortalama ' + rank(l.cur.position) + ' sıra') : [])
    .concat(cf && cf.guideViews ? ['Rehber yazıları ' + fmt(cf.guideViews) + ' kez okundu'] : [])
    .concat(!cf && !gsc ? ['Veri kaynakları henüz bağlanmadı.'] : [])
    .concat(['', 'Bu haftanın önerisi: ' + tip])
    .join('\n');
  const subject = (opts.test ? '[Deneme] ' : '') + 'Web sitenizin haftalık özeti · ' + weekLabel +
    (cf ? ' · ' + fmt(cf.visits) + ' ziyaret' : '');
  return { html, text, subject };
}

/* ------------------------------------------------------------------ giriş */
module.exports = async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('X-Robots-Tag', 'noindex');
  const secret = process.env.CRON_SECRET;
  const auth = String(req.headers.authorization || '');
  const ok = secret && auth.length === ('Bearer ' + secret).length &&
    crypto.timingSafeEqual(Buffer.from(auth), Buffer.from('Bearer ' + secret));
  if (req.method !== 'GET' || !ok) {
    res.statusCode = 401;
    return res.end('yetkisiz');
  }
  // req.query Vercel'in eski url.parse() yolunu tetikliyor (DEP0169 uyarısı); WHATWG URL ile okunur.
  const q = new URL(req.url || '/', SITE).searchParams;
  const test = q.get('test') === '1';
  const useSample = test && q.get('ornek') === '1';
  const key = process.env.RESEND_API_KEY;
  const to = String((test ? process.env.REPORT_TEST_TO : process.env.REPORT_TO) || '').split(',').map((s) => s.trim()).filter(Boolean);
  if (!key || !to.length) {
    console.error('rapor: yapılandırma eksik');
    res.statusCode = 503;
    return res.end('yapilandirma eksik');
  }

  const range = weekRange(new Date());
  let data;
  if (useSample) data = sample(range);
  else {
    const [cf, gsc] = await Promise.all([cloudflare(range).catch(() => null), searchConsole().catch(() => null)]);
    data = { cf, gsc };
    // Gerçek gönderimde hiç veri yoksa boş özet gönderme.
    if (!test && !cf && !gsc) {
      console.error('rapor: veri kaynağı yok, gönderilmedi');
      res.statusCode = 200;
      return res.end('veri yok');
    }
  }
  const mail = render(data, range, { test, sample: useSample });
  const payload = { from: FROM, to, subject: mail.subject, html: mail.html, text: mail.text };
  if (process.env.REPORT_REPLY_TO) payload.reply_to = process.env.REPORT_REPLY_TO;
  // Cron'un aynı dakikadaki çift tetiklenmesi tek e-posta olur; panodan elle yeniden çalıştırma
  // (Vercel → Cron Jobs → Run) bir dakika sonra yeni e-posta gönderir.
  const idemKey = 'rapor-' + isoDay(range.start) + '-' + new Date().toISOString().slice(0, 16) + (test ? '-test-' + Date.now() : '');
  const r = await fetchJson('https://api.resend.com/emails', {
    method: 'POST',
    headers: { Authorization: 'Bearer ' + key, 'Content-Type': 'application/json', 'Idempotency-Key': idemKey },
    body: JSON.stringify(payload)
  }, 10000).catch(() => ({ ok: false, status: 0 }));
  if (!r.ok) {
    console.error('rapor: resend durum ' + r.status);
    res.statusCode = 502;
    // Yalnız şifreyle çağrılan deneme modunda Resend'in açıklaması döner (örn. alan adı doğrulanmadı).
    const why = test && r.body && r.body.message ? ' ' + String(r.body.message).slice(0, 200) : '';
    return res.end('gonderilemedi ' + r.status + why);
  }
  res.statusCode = 200;
  res.end('gonderildi');
};
