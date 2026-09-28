// Ad/telefon/metin kurallarının örnek sınaması (assets/js/uslu-rules.js).
// Hem kabul edilmesi gereken gerçek girdiler (yanlış alarm olmasın) hem reddedilmesi
// gereken kötüye kullanım örnekleri. Sunucu (api/iletisim.js) aynı modülü kullanır.
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const R = require('../assets/js/uslu-rules.js');

const ok = {
  name: ['Ayşe Yılmaz', 'Mehmet Ali Kaya', 'Şuayip Saygılı', 'Çağlar Öztürk', 'İbrahim Halil Güneş', 'Amina Yılmaz',
    'Kemal Sıkı', 'Mert Güzel', 'Gökçe Nur Er', 'Ali Veli', "John O'Connor", 'Jean-Luc Picard', 'Hülya Koç',
    'Ümmü Gülsüm Ak', 'Nurşah Aksoy', 'Semih Kırmızıgül', 'ayşe yılmaz', 'Oğuz Kağan Işık', 'Aysu Nur Yıldırım'],
  phone: ['05321234568', '0532 595 85 83', '+90 312 270 56 47', '05551112233', '0 (532) 068 56 47', '904242223344'],
  text: ['Hafta sonu da olabilir', 'sık sık arayın lütfen', 'Mailim ayse@gmail.com', 'I got my licence last year',
    "Saat 10.30'dan sonra", 'Sıkı bir program istiyorum', 'Kemal Bey ile görüşmek istiyorum', '']
};
const bad = {
  name: ['Ayşe', 'asdf qwer', 'aaa bbb', 'Test Test', 'Ali Ali', 'xzqw plmk', 'Ayşe 123', 'orospu çocuğu', 'Amk Veli',
    'Ad Soyad', 'Deneme Kullanici', 'Siktir Git', 'Ahmet siktirgit', 'a b', 'Ayşe <b>Yılmaz</b>', 'Ayşe@ Yılmaz', ''],
  phone: ['5321234567', '0532123456', '05321234567', '05000000000', '05555555555', '0850 123 45 67', '0532 111 11 11',
    '0632 123 45 68', ''],
  text: ['www.site.com', 'https://x.y', 'ucuzilac.xyz sitesine bakın', 'amk', 'orospu', 'bu ne biçim iş yavşak']
};

let fail = 0;
const check = (kind, v, expectOk) => {
  const p = kind === 'name' ? R.nameProblem(v) : kind === 'phone' ? R.phoneProblem(R.phoneDigits(v)) : R.textProblem(v);
  const good = expectOk ? p === null : p !== null;
  if (!good) { fail++; console.log('FAIL', kind, JSON.stringify(v), '->', p, expectOk ? '(kabul edilmeliydi)' : '(reddedilmeliydi)'); }
};
for (const k of Object.keys(ok)) for (const v of ok[k]) check(k, v, true);
for (const k of Object.keys(bad)) for (const v of bad[k]) check(k, v, false);
const total = Object.values(ok).flat().length + Object.values(bad).flat().length;
if (fail) { console.log(`${fail}/${total} örnek hatalı`); process.exit(1); }
console.log(`PASS: ${total} kural örneği (kabul ve ret)`);
