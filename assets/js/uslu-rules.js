/*
 * Ad soyad, telefon ve serbest metin kuralları: TEK KAYNAK.
 * Tarayıcıda window.UsluRules (asistan ve iletişim formu), sunucuda
 * require('../assets/js/uslu-rules.js') (api/iletisim.js). Kural bir yerde değişirse
 * öbüründe de değişmiş olur; scripts/check-rules.mjs ikisini aynı örneklerle sınar.
 *
 * Amaç kötüye kullanımı zorlaştırmak: uydurma ad ("asdf qwer", "aaa bbb"), küfür,
 * sahte numara (0500 000 00 00, 0532 123 45 67), nota bağlantı. Kusursuz değildir;
 * son sözü kurs verir (e-postadaki numarayı arayarak).
 *
 * Dönüş değerleri: sorun yoksa null, varsa kısa bir kod (ekrandaki metni çağıran seçer).
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.UsluRules = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  function lower(v) {
    return String(v || '').toLocaleLowerCase('tr');
  }
  // Küfür denetimi için sadeleştir: Türkçe harfleri Latin karşılığına indir, tekrarı kısalt.
  // ı BİLEREK korunur: "sık" (sıklık) ile "sik" ayrı kalsın, yanlış alarm olmasın.
  function plain(v) {
    return lower(v)
      .replace(/[ç]/g, 'c').replace(/[ğ]/g, 'g').replace(/[ö]/g, 'o')
      .replace(/[ş]/g, 's').replace(/[ü]/g, 'u').replace(/[âà]/g, 'a').replace(/[îì]/g, 'i').replace(/[ûù]/g, 'u')
      .replace(/(.)\1{2,}/g, '$1$1');
  }

  // Tek başına kelime olarak geçerse reddedilenler (kısa olanlar ada gömülü geçebilir: "Kemal").
  // ("got", "pic", "dick" gibi İngilizcede olağan sözcükler BİLEREK yok: yanlış alarm.)
  var ABUSE_WORDS = ['amk', 'aq', 'amq', 'amına', 'oc', 'ibne', 'sik', 'sikik', 'sikis', 'yarak', 'gotveren',
    'kahpe', 'gavat', 'pust', 'surtuk', 'kaltak', 'serefsiz', 'yavsak', 'amcik', 'amcık', 'fuck', 'shit', 'bitch'];
  // Kelimenin içinde geçerse reddedilenler (uzun, ada gömülü geçmeyen kökler). "amina" YOK:
  // Amina bir kadın adı; küfür "amına" (ı ile) yazılışıyla yakalanır.
  var ABUSE_PARTS = ['orospu', 'siktir', 'yarrak', 'pezeven', 'amınak', 'aminak', 'ananı', 'dalyarak', 'amcık', 'amcik',
    'yavsak', 'serefsiz', 'kaltak', 'gotver', 'fucker', 'asshole'];
  // Ad soyad yerine yazılan dolgu ve deneme sözcükleri.
  var FAKE_WORDS = ['test', 'deneme', 'asd', 'asdf', 'asdasd', 'sdf', 'qwe', 'qwer', 'qwerty', 'zxc', 'zxcv', 'abc', 'abcd',
    'xxx', 'xx', 'yok', 'bilmiyorum', 'isim', 'soyisim', 'ad', 'soyad', 'adsoyad', 'admin', 'null', 'undefined', 'none',
    'name', 'surname', 'firstname', 'lastname', 'user', 'kullanici', 'ornek', 'example'];
  var VOWEL = /[aeıioöuüâîûy]/i;

  function hasAbuse(v) {
    var words = plain(v).split(/[^a-zı]+/).filter(Boolean);
    for (var i = 0; i < words.length; i++) {
      if (ABUSE_WORDS.indexOf(words[i]) >= 0) return true;
      for (var j = 0; j < ABUSE_PARTS.length; j++) if (words[i].indexOf(ABUSE_PARTS[j]) >= 0) return true;
    }
    return false;
  }
  function hasLink(v) {
    var s = String(v || '');
    if (/https?:\/\/|www\./i.test(s)) return true;
    // Çıplak alan adı (e-posta adresi hariç): "site.com", "ornek.xyz/..."
    return /(^|[^@\w.])[a-z0-9-]{2,}\.(com|net|org|ru|xyz|top|info|biz|site|online|shop|link|click|io|me|co|tr)\b/i.test(s);
  }

  var NAME_OK = /^[\p{L}'’.\-]{2,}(?: [\p{L}'’.\-]{2,})+$/u;

  function nameProblem(v) {
    var s = String(v || '').replace(/\s+/g, ' ').trim();
    if (!s) return 'name_format';
    if (/[\d_@#$%^&*()+=<>?!/\\|{}\[\]:;"~`]/.test(s)) return 'name_chars';
    if (!NAME_OK.test(s)) return 'name_format';
    var words = s.split(' ');
    if (words.length > 5 || s.length > 60) return 'name_fake';
    if (hasAbuse(s)) return 'name_abuse';
    for (var i = 0; i < words.length; i++) {
      var w = words[i].replace(/['’.\-]/g, '');
      var lw = lower(w);
      if (w.length > 20) return 'name_fake';
      if (!VOWEL.test(lw)) return 'name_fake';                 // "xzqw"
      if (/(.)\1\1/.test(lw)) return 'name_fake';              // "aaa"
      if (FAKE_WORDS.indexOf(plain(w)) >= 0) return 'name_fake';
    }
    // Aynı kelimenin tekrarı ("Ali Ali", "Test Test")
    var seen = {};
    for (var k = 0; k < words.length; k++) {
      var key = lower(words[k]);
      if (seen[key]) return 'name_fake';
      seen[key] = true;
    }
    return null;
  }

  // Telefon: 0 ile başlayan 11 hane (Ahmet, 28.09.2026). "+90 ..." yazılırsa 0'a çevrilir.
  function phoneDigits(v) {
    var d = String(v || '').replace(/\D/g, '');
    if (d.indexOf('90') === 0 && d.length > 11) d = '0' + d.slice(2);
    return d.slice(0, 11);
  }
  function phoneFormat(d) {
    return [d.slice(0, 4), d.slice(4, 7), d.slice(7, 9), d.slice(9, 11)].filter(Boolean).join(' ');
  }
  function phoneProblem(d) {
    d = String(d || '');
    if (!d) return 'phone_len';
    if (d.charAt(0) !== '0') return 'phone_start';
    if (d.length !== 11) return 'phone_len';
    // Türkiye: sabit hat 02-04, cep 05. Abone kısmı tek rakam ya da düz sıra olamaz.
    if (!/^0[2-5]/.test(d)) return 'phone_fake';
    var sub = d.slice(4);
    if (/^(\d)\1{6}$/.test(sub)) return 'phone_fake';
    if (sub === '1234567' || sub === '7654321' || sub === '0123456') return 'phone_fake';
    if (/^0(\d)\1{9}$/.test(d)) return 'phone_fake';
    return null;
  }

  // Serbest metin (asistan notu, form mesajı): bağlantı ve küfür yok.
  function textProblem(v) {
    var s = String(v || '');
    if (hasLink(s)) return 'text_link';
    if (hasAbuse(s)) return 'text_abuse';
    return null;
  }

  function titleCase(v, en) {
    var loc = en ? 'en' : 'tr';
    return String(v || '').replace(/\s+/g, ' ').trim().split(' ').map(function (w) {
      return w.charAt(0).toLocaleUpperCase(loc) + w.slice(1).toLocaleLowerCase(loc);
    }).join(' ');
  }

  return {
    nameProblem: nameProblem,
    phoneDigits: phoneDigits,
    phoneFormat: phoneFormat,
    phoneProblem: phoneProblem,
    textProblem: textProblem,
    titleCase: titleCase
  };
});
