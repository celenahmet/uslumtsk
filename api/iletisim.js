// İletişim formu ve web asistanı → kursun e-posta kutusu (Resend). Vercel Node fonksiyonu,
// bağımlılık yok. İki kaynak aynı kapıdan geçer: source = 'form' (iletişim sayfası) ya da
// 'asistan' (sağ alttaki canlı destek).
//
// Güvenlik:
//  - Yalnız POST; yalnız sitenin kendi kökeninden (Origin/Referer) gelen istek.
//  - Alanlar sunucuda yeniden doğrulanır (istemci doğrulaması yalnız kolaylık); seçmeli
//    alanlar yalnız bilinen anahtarları kabul eder, e-postaya serbest metin olarak yalnız
//    ad, not ve mesaj girer (HTML'e kaçışlanarak).
//  - Tuzak alan + gönderim süresi + örnek başına kaba hız sınırı; Resend günlük üst sınırı
//    (ücretsiz planda 100) kötüye kullanımın tavanıdır.
//  - Alıcı adresi ve API anahtarı KODDA DEĞİL, ortam değişkeninde (depo herkese açık):
//    RESEND_API_KEY (yalnız gönderim yetkili, alan adına kısıtlı), CONTACT_TO.
//  - Kişisel veri günlüğe yazılmaz; hata olursa yalnız durum kodu yazılır. Site veriyi
//    saklamaz, e-postayı iletir.
'use strict';

const crypto = require('node:crypto');
// Ad/telefon/metin kuralları tarayıcıyla ORTAK (tek kaynak): assets/js/uslu-rules.js
const R = require('../assets/js/uslu-rules.js');

const FROM = 'Uslu Sürücü Kursu Web Sitesi <form@uslusurucukursu.com>';
const ORIGINS = ['https://uslusurucukursu.com', 'https://uslumtsk.vercel.app'];
const FORM_TOPICS = {
  teklif: 'Fiyat teklifi',
  kayit: 'Kayıt',
  program: 'Ders programı ve süre',
  diger: 'Diğer'
};
// Asistandaki seçeneklerin anahtarları (assets/js/uslu-widgets.js ile aynı liste).
const CHAT_TOPICS = {
  teklif: 'Fiyat teklifi almak istiyor',
  kayit: 'Kayıt olmak istiyor',
  program: 'Ders programı ve süre',
  soru: 'Başka bir konu'
};
const COURSES = {
  'manuel-b': 'B sınıfı manuel ehliyet',
  'otomatik-b': 'B sınıfı otomatik ehliyet',
  'motor-a1': 'A1 motosiklet ehliyeti',
  'motor-a2': 'A2 motosiklet ehliyeti',
  'ozel-ab': 'Özel gereksinimli A-B sınıfı',
  diger: 'Büyük araç ehliyetleri',
  ozel: 'Özel direksiyon dersi',
  bilmiyorum: 'Diğer / emin değil'
};
const WHO = {
  kendim: 'Kendisi',
  cocugum: 'Çocuğu',
  kardesim: 'Kardeşi',
  esim: 'Eşi',
  yakinim: 'Bir yakını veya arkadaşı'
};
const TIMES = { sabah: 'Sabah', ogle: 'Öğle', aksam: 'Akşam' };

const EMAIL_OK = /^[^\s@<>()",;:]+@[^\s@<>()",;:]+\.[^\s@<>()",;:]{2,}$/;

// Kötüye kullanım sınırları (aynı sıcak örnekte, en iyi çaba; kalıcı depo yok):
//  - IP başına 10 dakikada 5 gönderim
//  - aynı telefon numarası için saatte 3 gönderim
//  - örnek başına günde 80 e-posta (Resend ücretsiz planı günde 100; tükenmesin)
// Sınır aşılırsa istemci WhatsApp yedeğini gösterir.
const buckets = { ip: new Map(), phone: new Map() };
function over(kind, key, windowMs, limit) {
  const map = buckets[kind];
  const now = Date.now();
  const list = (map.get(key) || []).filter((t) => now - t < windowMs);
  list.push(now);
  map.set(key, list);
  if (map.size > 5000) map.clear();
  return list.length > limit;
}
let day = '';
let sentToday = 0;
function dailyCapReached() {
  const today = new Date().toISOString().slice(0, 10);
  if (today !== day) { day = today; sentToday = 0; }
  return sentToday >= 80;
}

function clean(v, max) {
  return String(v == null ? '' : v).replace(/[\u0000-\u0008\u000b-\u001f\u007f]/g, '').replace(/[ \t]+/g, ' ').trim().slice(0, max);
}
function text(v, max) {
  return String(v == null ? '' : v).replace(/[\u0000-\u0008\u000b-\u001f\u007f]/g, '').trim().slice(0, max);
}
function oneLine(v) {
  return v.replace(/[\r\n]+/g, ' ');
}
function esc(v) {
  return v.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}
function pick(map, key) {
  return Object.prototype.hasOwnProperty.call(map, key) ? map[key] : null;
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

// Kaynağa göre doğrula ve e-posta içeriğini kur. Hata varsa { error } döner.
function build(body) {
  const source = body.source === 'asistan' ? 'asistan' : 'form';
  const rawName = clean(body.name, 80);
  if (R.nameProblem(rawName)) return { error: 'name' };
  const name = R.titleCase(rawName);
  // phoneDigits 11 haneden fazlasını keser; ham girdi fazlaysa bu da hata sayılır.
  const rawDigits = String(body.phone == null ? '' : body.phone).replace(/\D/g, '');
  const digits = R.phoneDigits(body.phone);
  if (rawDigits.length > 12 || R.phoneProblem(digits)) return { error: 'phone' };
  const phone = R.phoneFormat(digits);
  const ack = body.kvkk === true || body.kvkk === 'on' || body.kvkk === '1';

  if (source === 'asistan') {
    const topic = pick(CHAT_TOPICS, clean(body.topic, 20));
    const course = pick(COURSES, clean(body.course, 20));
    const who = pick(WHO, clean(body.who, 20));
    if (!topic) return { error: 'topic' };
    if (!course) return { error: 'course' };
    if (!who) return { error: 'who' };
    const list = Array.isArray(body.times) ? body.times.slice(0, 3) : [];
    const times = [];
    for (const k of list) {
      const t = pick(TIMES, clean(k, 10));
      if (!t) return { error: 'times' };
      if (!times.includes(t)) times.push(t);
    }
    const note = text(body.note, 300);
    if (R.textProblem(note)) return { error: 'note' };
    if (!ack) return { error: 'kvkk' };
    return {
      source,
      name,
      digits,
      subject: 'Web asistanı: ' + topic + ' - ' + course + ' - ' + name,
      heading: 'Web sitesi asistanından yeni talep',
      rows: [
        ['Talep', topic],
        ['Eğitim', course],
        ['Eğitim kimin için', who],
        ['Ad Soyad', name],
        ['Telefon', phone],
        ['Uygun arama zamanı', times.length ? times.join(', ') : 'Fark etmez']
      ],
      message: note,
      messageLabel: 'Not',
      email: '',
      idem: [source, name, digits, topic, course, who, times.join(','), note].join('|')
    };
  }

  const email = clean(body.email, 120);
  const topic = pick(FORM_TOPICS, clean(body.topic, 20));
  const message = text(body.message, 2000);
  if (email && !EMAIL_OK.test(email)) return { error: 'email' };
  if (!topic) return { error: 'topic' };
  if (message.length < 10 || R.textProblem(message)) return { error: 'message' };
  if (!ack) return { error: 'kvkk' };
  return {
    source,
    name,
    digits,
    subject: 'Web sitesi: ' + topic + ' - ' + name,
    heading: 'Web sitesi iletişim formundan yeni mesaj',
    rows: [['Ad Soyad', name], ['Telefon', phone], ['E-posta', email || 'Belirtilmedi'], ['Konu', topic]],
    message,
    messageLabel: 'Mesaj',
    email,
    idem: [source, name, digits, topic, message].join('|')
  };
}

function render(m) {
  // Kurs personeli için tek dokunuşla arama ve WhatsApp bağlantısı (numara doğrulanmış 11 hane).
  const intl = '90' + m.digits.slice(1);
  const call = 'tel:+' + intl;
  const wa = 'https://wa.me/' + intl;
  const origin = m.source === 'asistan' ? 'web sitesi asistanından' : 'web sitesi iletişim formundan';
  const text =
    m.rows.map((r) => r[0] + ': ' + r[1]).join('\n') +
    (m.message ? '\n\n' + m.messageLabel + ':\n' + m.message : '') +
    '\n\nAra: +' + intl + '\nWhatsApp: ' + wa +
    '\n\nBu mesaj uslusurucukursu.com ' + origin + ' gönderildi.';
  const html =
    '<div style="font-family:Arial,sans-serif;font-size:15px;color:#041e37;max-width:560px">' +
    '<h2 style="font-size:18px;margin:0 0 12px;border-bottom:3px solid #cb1643;padding-bottom:8px">' + esc(m.heading) + '</h2>' +
    '<table cellpadding="6" style="border-collapse:collapse">' +
    m.rows.map((r) => '<tr><td style="color:#6b7280;white-space:nowrap;vertical-align:top">' + esc(r[0]) + '</td><td><b>' + esc(r[1]) + '</b></td></tr>').join('') +
    '</table>' +
    (m.message
      ? '<p style="margin:14px 0 4px;color:#6b7280">' + esc(m.messageLabel) + '</p>' +
        '<div style="white-space:pre-wrap;background:#f5f6f8;border-left:3px solid #cb1643;padding:10px 12px">' + esc(m.message) + '</div>'
      : '') +
    '<p style="margin:18px 0 0">' +
    '<a href="' + call + '" style="display:inline-block;background:#cb1643;color:#fff;text-decoration:none;font-weight:bold;padding:10px 16px;margin:0 8px 8px 0">Ara</a>' +
    '<a href="' + wa + '" style="display:inline-block;background:#25d366;color:#fff;text-decoration:none;font-weight:bold;padding:10px 16px;margin:0 8px 8px 0">WhatsApp’tan yaz</a>' +
    '</p>' +
    '<p style="font-size:12px;color:#6b7280;margin-top:12px">Bu mesaj uslusurucukursu.com ' + origin + ' gönderildi.' +
    (m.email ? ' Yanıtla dediğinizde doğrudan gönderene gider.' : '') + '</p></div>';
  return { text, html };
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
  if (!body || typeof body !== 'object' || Array.isArray(body)) return reply(req, res, 400, 'invalid');
  const form = isForm ? { lang: clean(body.lang, 2) } : null;

  // Tuzak alan doluysa bota başarılı görün, gönderme.
  if (clean(body.website, 200)) return reply(req, res, 200, 'ok', form);
  const elapsed = Number(body.t || 0);
  if (!isForm && !(elapsed >= 3000)) return reply(req, res, 400, 'fast');

  const ip = String(req.headers['x-forwarded-for'] || '').split(',')[0].trim() || 'yok';
  if (over('ip', ip, 10 * 60 * 1000, 5)) return reply(req, res, 429, 'rate', form);

  const m = build(body);
  if (m.error) return reply(req, res, 400, m.error, form);
  if (over('phone', m.digits, 60 * 60 * 1000, 3)) return reply(req, res, 429, 'rate', form);
  if (dailyCapReached()) {
    console.error('iletisim: gunluk sinir doldu');
    return reply(req, res, 429, 'rate', form);
  }

  const key = process.env.RESEND_API_KEY;
  const to = process.env.CONTACT_TO;
  if (!key || !to) {
    console.error('iletisim: yapılandırma eksik');
    return reply(req, res, 503, 'config', form);
  }

  const { text: plain, html } = render(m);
  const payload = { from: FROM, to: [to], subject: oneLine(m.subject), text: plain, html };
  if (m.email) payload.reply_to = m.email;

  // Aynı içerik çift tıklamayla iki kez gitmesin (Resend 24 saat boyunca tekrarı yutar).
  const idem = crypto.createHash('sha256').update(m.idem).digest('hex').slice(0, 48);

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
    sentToday++;
  } catch (e) {
    console.error('iletisim: resend ulaşılamadı');
    return reply(req, res, 502, 'send', form);
  } finally {
    clearTimeout(timer);
  }
  return reply(req, res, 200, 'ok', form);
};
