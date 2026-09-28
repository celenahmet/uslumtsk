// İletişim formu → kursun e-posta kutusu (Resend). Vercel Node fonksiyonu, bağımlılık yok.
//
// Güvenlik:
//  - Yalnız POST; yalnız sitenin kendi kökeninden (Origin/Referer) gelen istek.
//  - Alanlar sunucuda yeniden doğrulanır (istemci doğrulaması yalnız kolaylık).
//  - Tuzak alan + gönderim süresi + örnek başına kaba hız sınırı; Resend günlük üst sınırı
//    (ücretsiz planda 100) kötüye kullanımın tavanıdır.
//  - Alıcı adresi ve API anahtarı KODDA DEĞİL, ortam değişkeninde (depo herkese açık):
//    RESEND_API_KEY (yalnız gönderim yetkili, alan adına kısıtlı), CONTACT_TO.
//  - Kişisel veri günlüğe yazılmaz; hata olursa yalnız durum kodu yazılır. Site veriyi
//    saklamaz, e-postayı iletir.
'use strict';

const crypto = require('node:crypto');

const FROM = 'Uslu Sürücü Kursu Web Sitesi <form@uslusurucukursu.com>';
const ORIGINS = ['https://uslusurucukursu.com', 'https://uslumtsk.vercel.app'];
const TOPICS = {
  teklif: 'Fiyat teklifi',
  kayit: 'Kayıt',
  program: 'Ders programı ve süre',
  diger: 'Diğer'
};
const NAME_OK = /^[\p{L}'’.\-]{2,}(?: [\p{L}'’.\-]{2,})+$/u;
const EMAIL_OK = /^[^\s@<>()",;:]+@[^\s@<>()",;:]+\.[^\s@<>()",;:]{2,}$/;

// Aynı sıcak örnekte IP başına 10 dakikada en çok 5 gönderim (kaba, en iyi çaba).
const WINDOW = 10 * 60 * 1000;
const LIMIT = 5;
const hits = new Map();
function limited(ip) {
  const now = Date.now();
  const list = (hits.get(ip) || []).filter((t) => now - t < WINDOW);
  list.push(now);
  hits.set(ip, list);
  if (hits.size > 5000) hits.clear();
  return list.length > LIMIT;
}

function clean(v, max) {
  return String(v == null ? '' : v).replace(/[\u0000-\u0008\u000b-\u001f\u007f]/g, '').replace(/[ \t]+/g, ' ').trim().slice(0, max);
}
function oneLine(v) {
  return v.replace(/[\r\n]+/g, ' ');
}
function esc(v) {
  return v.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}
function phoneDigits(v) {
  let d = String(v || '').replace(/\D/g, '');
  if (d.indexOf('90') === 0 && d.length > 11) d = '0' + d.slice(2);
  return d;
}

function allowedOrigin(req) {
  const o = req.headers.origin;
  if (o) return ORIGINS.includes(o);
  const r = req.headers.referer;
  if (!r) return false;
  try { return ORIGINS.includes(new URL(r).origin); } catch (e) { return false; }
}

async function readBody(req) {
  if (req.body && typeof req.body === 'object') return req.body;
  if (typeof req.body === 'string') {
    const type = String(req.headers['content-type'] || '');
    if (type.includes('application/json')) return JSON.parse(req.body);
    return Object.fromEntries(new URLSearchParams(req.body));
  }
  return {};
}

function reply(req, res, status, code, form) {
  // JavaScript kapalıysa form doğrudan gönderilir: sonucu sayfaya yönlendirerek bildir.
  if (form) {
    const lang = form.lang === 'en' ? '/en/contact/' : '/iletisim/';
    res.statusCode = 303;
    res.setHeader('Location', lang + '?form=' + (status === 200 ? 'ok' : code) + '#iletisim-formu');
    res.end();
    return;
  }
  res.statusCode = status;
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  res.end(JSON.stringify(status === 200 ? { ok: true } : { ok: false, error: code }));
}

module.exports = async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('X-Robots-Tag', 'noindex');
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return reply(req, res, 405, 'method');
  }
  const isForm = !String(req.headers['content-type'] || '').includes('application/json');
  if (!allowedOrigin(req)) return reply(req, res, 403, 'origin');

  const len = Number(req.headers['content-length'] || 0);
  if (len > 16 * 1024) return reply(req, res, 413, 'size');

  let body;
  try { body = await readBody(req); } catch (e) { return reply(req, res, 400, 'invalid'); }
  const form = isForm ? { lang: clean(body.lang, 2) } : null;

  // Tuzak alan doluysa bota başarılı görün, gönderme.
  if (clean(body.website, 200)) return reply(req, res, 200, 'ok', form);
  const elapsed = Number(body.t || 0);
  if (!isForm && !(elapsed >= 3000)) return reply(req, res, 400, 'fast');

  const ip = String(req.headers['x-forwarded-for'] || '').split(',')[0].trim() || 'yok';
  if (limited(ip)) return reply(req, res, 429, 'rate', form);

  const name = clean(body.name, 80);
  const digits = phoneDigits(body.phone);
  const email = clean(body.email, 120);
  const topicKey = clean(body.topic, 20);
  const message = String(body.message == null ? '' : body.message).replace(/[\u0000-\u0008\u000b-\u001f\u007f]/g, '').trim().slice(0, 2000);
  const ack = body.kvkk === true || body.kvkk === 'on' || body.kvkk === '1';

  if (!NAME_OK.test(name)) return reply(req, res, 400, 'name', form);
  if (!(digits.length === 11 && digits.charAt(0) === '0')) return reply(req, res, 400, 'phone', form);
  if (email && !EMAIL_OK.test(email)) return reply(req, res, 400, 'email', form);
  if (!TOPICS[topicKey]) return reply(req, res, 400, 'topic', form);
  if (message.length < 10) return reply(req, res, 400, 'message', form);
  if (!ack) return reply(req, res, 400, 'kvkk', form);

  const key = process.env.RESEND_API_KEY;
  const to = process.env.CONTACT_TO;
  if (!key || !to) {
    console.error('iletisim: yapılandırma eksik');
    return reply(req, res, 503, 'config', form);
  }

  const phone = [digits.slice(0, 4), digits.slice(4, 7), digits.slice(7, 9), digits.slice(9, 11)].join(' ');
  const topic = TOPICS[topicKey];
  const rows = [['Ad Soyad', name], ['Telefon', phone], ['E-posta', email || 'Belirtilmedi'], ['Konu', topic]];
  const text = rows.map((r) => r[0] + ': ' + r[1]).join('\n') + '\n\nMesaj:\n' + message +
    '\n\nBu mesaj uslusurucukursu.com iletişim formundan gönderildi.';
  const html =
    '<div style="font-family:Arial,sans-serif;font-size:15px;color:#041e37;max-width:560px">' +
    '<h2 style="font-size:18px;margin:0 0 12px;border-bottom:3px solid #cb1643;padding-bottom:8px">Web sitesinden yeni mesaj</h2>' +
    '<table cellpadding="6" style="border-collapse:collapse">' +
    rows.map((r) => '<tr><td style="color:#6b7280;white-space:nowrap">' + esc(r[0]) + '</td><td><b>' + esc(r[1]) + '</b></td></tr>').join('') +
    '</table>' +
    '<p style="margin:14px 0 4px;color:#6b7280">Mesaj</p>' +
    '<div style="white-space:pre-wrap;background:#f5f6f8;border-left:3px solid #cb1643;padding:10px 12px">' + esc(message) + '</div>' +
    '<p style="font-size:12px;color:#6b7280;margin-top:16px">Bu mesaj uslusurucukursu.com iletişim formundan gönderildi.' +
    (email ? ' Yanıtla dediğinizde doğrudan gönderene gider.' : '') + '</p></div>';

  const payload = {
    from: FROM,
    to: [to],
    subject: oneLine('Web sitesi: ' + topic + ' - ' + name),
    text,
    html
  };
  if (email) payload.reply_to = email;

  // Aynı içerik çift tıklamayla iki kez gitmesin (Resend 24 saat boyunca tekrarı yutar).
  const idem = crypto.createHash('sha256').update([name, digits, topicKey, message].join('|')).digest('hex').slice(0, 48);

  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), 8000);
  try {
    const r = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { Authorization: 'Bearer ' + key, 'Content-Type': 'application/json', 'Idempotency-Key': idem },
      body: JSON.stringify(payload),
      signal: ctrl.signal
    });
    if (!r.ok) {
      console.error('iletisim: resend durum ' + r.status);
      return reply(req, res, 502, 'send', form);
    }
  } catch (e) {
    console.error('iletisim: resend ulaşılamadı');
    return reply(req, res, 502, 'send', form);
  } finally {
    clearTimeout(timer);
  }
  return reply(req, res, 200, 'ok', form);
};
