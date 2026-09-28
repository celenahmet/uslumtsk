/*
 * Uslu Sürücü Kursu: WhatsApp teklif asistanı + erişilebilirlik çubuğu.
 *
 * Tawk.to yerine kendi asistanımız (maliaksoytesisat'taki akışın sürücü kursuna
 * uyarlanmışı): kurs ve talep seçilir, iletişim bilgisi alınır, hazır mesajla
 * kursun WhatsApp hattına geçilir. Bilgiler SİTEDE SAKLANMAZ; mesajı ziyaretçi
 * kendi WhatsApp'ından gönderir.
 *
 * Erişilebilirlik çubuğu: solda, dikeyde ortalı, küçük; 10 işlev, tercihler bu
 * tarayıcıda saklanır.
 *
 * Kurallar: kullanıcı girdisi DOM'a yalnız textContent/value ile yazılır (innerHTML
 * yalnız sabit ikonlar için). Stil bu dosyanın içinde; ayrı CSS isteği yok.
 */
(function () {
  'use strict';
  if (window.__usluWidgets) return;
  window.__usluWidgets = true;

  var PHONE = '905320685647';
  var SITE = 'uslusurucukursu.com';
  var EN = (document.documentElement.lang || '').toLowerCase().indexOf('en') === 0;

  var T = EN
    ? {
        launcher: 'Get a quote on WhatsApp',
        title: 'Uslu Driving School Assistant',
        online: 'online',
        close: 'Close',
        back: 'Back',
        hello: 'Hello! Which licence course are you interested in?',
        topic: 'What would you like to know?',
        contact: 'Where can we reach you?',
        name: 'Full name',
        namePh: 'Your full name',
        phone: 'Phone',
        phonePh: '05xx xxx xx xx',
        time: 'Best time to call (optional)',
        note: 'Note (optional)',
        notePh: 'Anything you would like to add...',
        cont: 'Continue',
        nameErr: 'Please enter your full name.',
        phoneErr: 'Please enter a valid phone number.',
        spamErr: 'That was very fast. Please wait a moment and try again.',
        summary: 'Your message is ready. It will open in WhatsApp and you send it yourself.',
        send: 'Send on WhatsApp',
        sent: 'WhatsApp opened. We will get back to you soon.',
        again: 'New request',
        privacy: 'Your details are not stored on this website; you send the message from your own WhatsApp.',
        teaser: 'Would you like a quote?',
        course: 'Course',
        request: 'Request',
        none: 'Not specified',
        intro: 'Hello, I found your driving school on your website ' + SITE + '.',
        lName: 'Name',
        lPhone: 'Phone',
        lTime: 'Best time to call',
        lNote: 'Note',
        courses: [
          ['manuel-b', 'Manual B class licence'],
          ['otomatik-b', 'Automatic B class licence'],
          ['motor-a1', 'A1 motorcycle licence'],
          ['motor-a2', 'A2 motorcycle licence'],
          ['ozel-ab', 'Special needs A-B class'],
          ['diger', 'Large vehicle licences'],
          ['ozel', 'Private driving lessons'],
          ['bilmiyorum', 'Other / not sure']
        ],
        topics: [
          ['teklif', 'I would like a price quote'],
          ['kayit', 'I would like to enrol'],
          ['program', 'Schedule and duration'],
          ['soru', 'Another question']
        ],
        times: ['Any time', 'Morning', 'Afternoon', 'Evening']
      }
    : {
        launcher: 'WhatsApp’tan teklif alın',
        title: 'Uslu Sürücü Kursu Asistanı',
        online: 'çevrimiçi',
        close: 'Kapat',
        back: 'Geri',
        hello: 'Merhaba! Hangi ehliyet eğitimiyle ilgileniyorsunuz?',
        topic: 'Ne öğrenmek istersiniz?',
        contact: 'Size nasıl ulaşalım?',
        name: 'Ad Soyad',
        namePh: 'Adınız ve soyadınız',
        phone: 'Telefon',
        phonePh: '05xx xxx xx xx',
        time: 'Uygun arama zamanı (isteğe bağlı)',
        note: 'Not (isteğe bağlı)',
        notePh: 'Eklemek istediğiniz bir şey varsa...',
        cont: 'Devam et',
        nameErr: 'Lütfen adınızı ve soyadınızı yazın.',
        phoneErr: 'Lütfen geçerli bir telefon numarası yazın.',
        spamErr: 'Çok hızlı ilerlediniz. Birkaç saniye bekleyip yeniden deneyin.',
        summary: 'Mesajınız hazır. WhatsApp’ta açılacak ve siz göndereceksiniz.',
        send: 'WhatsApp’a gönder',
        sent: 'WhatsApp açıldı. En kısa sürede dönüş yapacağız.',
        again: 'Yeni talep',
        privacy: 'Bilgileriniz bu sitede saklanmaz; mesajı kendi WhatsApp’ınızdan siz gönderirsiniz.',
        teaser: 'Teklif almak ister misiniz?',
        course: 'İlgilendiğim eğitim',
        request: 'Talebim',
        none: 'Belirtilmedi',
        intro: 'Merhabalar, ' + SITE + ' web sitenizden sürücü kursunuzu gördüm.',
        lName: 'Ad Soyad',
        lPhone: 'Telefon',
        lTime: 'Uygun arama zamanı',
        lNote: 'Not',
        courses: [
          ['manuel-b', 'B sınıfı manuel ehliyet'],
          ['otomatik-b', 'B sınıfı otomatik ehliyet'],
          ['motor-a1', 'A1 motosiklet ehliyeti'],
          ['motor-a2', 'A2 motosiklet ehliyeti'],
          ['ozel-ab', 'Özel gereksinimli A-B sınıfı'],
          ['diger', 'Büyük araç ehliyetleri'],
          ['ozel', 'Özel direksiyon dersi'],
          ['bilmiyorum', 'Diğer / emin değilim']
        ],
        topics: [
          ['teklif', 'Fiyat teklifi almak istiyorum'],
          ['kayit', 'Kayıt olmak istiyorum'],
          ['program', 'Ders programı ve süre'],
          ['soru', 'Başka bir sorum var']
        ],
        times: ['Fark etmez', 'Sabah', 'Öğle', 'Akşam']
      };

  var A = EN
    ? {
        open: 'Accessibility options',
        title: 'Accessibility',
        hint: 'Saved in this browser',
        reset: 'Reset',
        close: 'Close',
        items: {
          text: 'Larger text',
          contrast: 'High contrast',
          mono: 'Monochrome',
          links: 'Highlight links',
          font: 'Readable font',
          spacing: 'Line spacing',
          guide: 'Reading guide',
          images: 'Hide images',
          motion: 'Stop motion',
          cursor: 'Large cursor'
        }
      }
    : {
        open: 'Erişilebilirlik seçenekleri',
        title: 'Erişilebilirlik',
        hint: 'Tercihler bu tarayıcıda saklanır',
        reset: 'Sıfırla',
        close: 'Kapat',
        items: {
          text: 'Yazıyı büyüt',
          contrast: 'Yüksek kontrast',
          mono: 'Monokrom',
          links: 'Bağlantıları vurgula',
          font: 'Okunabilir yazı',
          spacing: 'Satır aralığı',
          guide: 'Okuma kılavuzu',
          images: 'Görselleri gizle',
          motion: 'Hareketi durdur',
          cursor: 'Büyük imleç'
        }
      };

  /* ------------------------------------------------------------------ stil */
  var CSS =
    '[data-uslu-widget]{font-family:inherit;box-sizing:border-box}' +
    '[data-uslu-widget] *{box-sizing:border-box}' +
    '#scroll-top{bottom:92px!important;right:24px!important}' +
    /* sohbet */
    '.uc-launch{position:fixed;right:20px;bottom:20px;z-index:9990;width:56px;height:56px;border-radius:50%;border:0;background:#25d366;color:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 20px rgba(0,0,0,.22);cursor:pointer;transition:transform .15s}' +
    '.uc-launch:hover{transform:translateY(-2px)}.uc-launch:focus-visible{outline:3px solid #cb1643;outline-offset:3px}' +
    '.uc-launch svg{width:30px;height:30px}' +
    '.uc-teaser{position:fixed;right:84px;bottom:30px;z-index:9990;background:#fff;color:#1f2937;border-radius:14px;padding:8px 12px;font-size:14px;box-shadow:0 6px 20px rgba(0,0,0,.16);cursor:pointer;border:0;max-width:200px;text-align:left}' +
    '.uc-panel{position:fixed;right:20px;bottom:88px;z-index:9991;width:340px;max-width:calc(100vw - 24px);max-height:min(560px,calc(100vh - 110px));display:flex;flex-direction:column;background:#fff;color:#1f2937;border-radius:16px;box-shadow:0 12px 40px rgba(0,0,0,.25);overflow:hidden}' +
    '.uc-panel[hidden]{display:none}' +
    '.uc-head{display:flex;align-items:center;gap:10px;padding:12px 14px;background:#cb1643;color:#fff}' +
    '.uc-head b{display:block;font-size:15px;line-height:1.2}.uc-head small{font-size:12px;opacity:.9}' +
    '.uc-dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:#34d399;margin-right:5px;vertical-align:middle}' +
    '.uc-x{margin-left:auto;background:transparent;border:0;color:#fff;width:32px;height:32px;border-radius:8px;cursor:pointer;font-size:20px;line-height:1}' +
    '.uc-x:focus-visible,.uc-body button:focus-visible,.uc-body input:focus-visible,.uc-body select:focus-visible,.uc-body textarea:focus-visible{outline:3px solid #cb1643;outline-offset:2px}' +
    '.uc-body{padding:14px;overflow-y:auto;font-size:14px;line-height:1.5}' +
    '.uc-msg{background:#f3f4f6;border-radius:12px 12px 12px 4px;padding:9px 12px;margin-bottom:10px}' +
    '.uc-opts{display:flex;flex-direction:column;gap:6px}' +
    '.uc-opt{text-align:left;background:#fff;border:1px solid #e5e7eb;border-radius:10px;padding:9px 12px;cursor:pointer;font-size:14px;color:#1f2937}' +
    '.uc-opt:hover{border-color:#cb1643;color:#cb1643}' +
    '.uc-body label{display:block;font-size:13px;font-weight:600;margin:8px 0 4px}' +
    '.uc-body input,.uc-body select,.uc-body textarea{width:100%;border:1px solid #d1d5db;border-radius:8px;padding:8px 10px;font-size:14px;color:#111827;background:#fff}' +
    '.uc-body textarea{min-height:64px;resize:vertical}' +
    '.uc-err{color:#b91c1c;font-size:13px;margin-top:6px;min-height:0}' +
    '.uc-main{width:100%;margin-top:12px;border:0;border-radius:10px;padding:10px 12px;background:#cb1643;color:#fff;font-weight:600;cursor:pointer;font-size:15px}' +
    '.uc-main.uc-wa{background:#25d366}' +
    '.uc-link{background:transparent;border:0;color:#6b7280;font-size:13px;padding:6px 0;cursor:pointer;text-decoration:underline}' +
    '.uc-pre{white-space:pre-wrap;background:#f9fafb;border:1px solid #e5e7eb;border-radius:10px;padding:10px;font-size:13px;margin:8px 0}' +
    '.uc-note{font-size:12px;color:#6b7280;margin-top:8px}' +
    '.uc-hp{position:absolute!important;left:-9999px!important;width:1px;height:1px;overflow:hidden}' +
    '@media (max-width:480px){.uc-panel{right:12px;left:12px;width:auto;bottom:84px}}' +
    /* erişilebilirlik */
    '.ua-tab{position:fixed;left:0;top:50%;transform:translateY(-50%);z-index:9989;width:34px;height:40px;border:0;border-radius:0 10px 10px 0;background:rgba(31,41,55,.82);color:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer;box-shadow:0 2px 10px rgba(0,0,0,.18);opacity:.75;transition:opacity .15s,width .15s}' +
    '.ua-tab:hover,.ua-tab:focus-visible,.ua-tab[aria-expanded="true"]{opacity:1;width:38px}.ua-tab:focus-visible{outline:3px solid #cb1643;outline-offset:2px}' +
    '.ua-tab svg{width:20px;height:20px}' +
    '.ua-panel{position:fixed;left:44px;top:50%;transform:translateY(-50%);z-index:9989;width:252px;max-width:calc(100vw - 56px);max-height:calc(100vh - 24px);overflow-y:auto;background:#fff;color:#1f2937;border-radius:14px;box-shadow:0 10px 32px rgba(0,0,0,.22);padding:12px}' +
    '.ua-panel[hidden]{display:none}' +
    '.ua-top{display:flex;align-items:flex-start;gap:8px;margin-bottom:8px}.ua-top b{font-size:14px;display:block}.ua-top small{font-size:11px;color:#6b7280}' +
    '.ua-close{margin-left:auto;background:transparent;border:0;width:28px;height:28px;border-radius:8px;cursor:pointer;font-size:18px;color:#374151}' +
    '.ua-grid{display:grid;grid-template-columns:1fr 1fr;gap:6px}' +
    '.ua-btn{display:flex;align-items:center;gap:6px;border:1px solid #e5e7eb;background:#fff;border-radius:9px;padding:7px 8px;font-size:12px;line-height:1.25;color:#1f2937;cursor:pointer;text-align:left;min-height:38px}' +
    '.ua-btn svg{width:16px;height:16px;flex:0 0 16px;color:#cb1643}' +
    '.ua-btn[aria-pressed="true"]{background:#cb1643;border-color:#cb1643;color:#fff}.ua-btn[aria-pressed="true"] svg{color:#fff}' +
    '.ua-btn:focus-visible,.ua-close:focus-visible,.ua-reset:focus-visible{outline:3px solid #cb1643;outline-offset:2px}' +
    '.ua-reset{margin-top:8px;background:transparent;border:0;color:#6b7280;font-size:12px;cursor:pointer;text-decoration:underline;padding:4px 0}' +
    '.ua-guide{position:fixed;left:0;right:0;height:14px;z-index:9988;pointer-events:none;background:rgba(203,22,67,.18);border-top:2px solid rgba(203,22,67,.6);border-bottom:2px solid rgba(203,22,67,.6);display:none}' +
    'html.ua-guide-on .ua-guide{display:block}' +
    'html.ua-text-1 body>:not([data-uslu-widget]){zoom:1.12}html.ua-text-2 body>:not([data-uslu-widget]){zoom:1.25}' +
    'html.ua-links a{text-decoration:underline!important;outline:2px solid #f59e0b!important;outline-offset:2px}' +
    'html.ua-font body *:not(i):not([class*="fa-"]):not(svg):not(path){font-family:Verdana,Tahoma,"Segoe UI",sans-serif!important;letter-spacing:.02em!important;word-spacing:.06em!important}' +
    'html.ua-spacing body p,html.ua-spacing body li,html.ua-spacing body dd{line-height:1.95!important}' +
    'html.ua-images body>:not([data-uslu-widget]) img,html.ua-images body>:not([data-uslu-widget]) video{visibility:hidden!important}html.ua-images body>:not([data-uslu-widget]) *{background-image:none!important}' +
    'html.ua-motion *,html.ua-motion *::before,html.ua-motion *::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}' +
    'html.ua-cursor,html.ua-cursor *{cursor:url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 width=%2740%27 height=%2740%27 viewBox=%270 0 24 24%27%3E%3Cpath d=%27M4 2l16 9-7 2-3 7z%27 fill=%27%23000%27 stroke=%27%23fff%27 stroke-width=%271.5%27/%3E%3C/svg%3E") 4 2,auto!important}' +
    '@media (prefers-reduced-motion:reduce){.uc-launch,.ua-tab{transition:none}}';

  function injectStyle() {
    var s = document.createElement('style');
    s.setAttribute('data-uslu-style', '');
    s.textContent = CSS;
    document.head.appendChild(s);
  }

  function el(tag, attrs, text) {
    var n = document.createElement(tag);
    if (attrs) for (var k in attrs) if (Object.prototype.hasOwnProperty.call(attrs, k)) n.setAttribute(k, attrs[k]);
    if (text != null) n.textContent = text;
    return n;
  }

  var store = {
    get: function (k, s) {
      try { return (s ? window.sessionStorage : window.localStorage).getItem(k); } catch (e) { return null; }
    },
    set: function (k, v, s) {
      try { (s ? window.sessionStorage : window.localStorage).setItem(k, v); } catch (e) { /* gizli pencere */ }
    }
  };

  var ICON_WA =
    '<svg viewBox="0 0 32 32" aria-hidden="true" focusable="false"><path fill="currentColor" d="M16 3C8.8 3 3 8.7 3 15.8c0 2.5.7 4.9 2 7L3 29l6.4-2c2 1.1 4.3 1.7 6.6 1.7 7.2 0 13-5.7 13-12.8S23.2 3 16 3zm0 23.3c-2.1 0-4.1-.6-5.9-1.7l-.4-.3-3.8 1.2 1.2-3.7-.3-.4c-1.2-1.8-1.9-3.9-1.9-6.1C4.9 9.8 9.9 5 16 5s11.1 4.8 11.1 10.8S22.1 26.3 16 26.3zm6.1-8c-.3-.2-2-1-2.3-1.1-.3-.1-.5-.2-.8.2-.2.3-.9 1.1-1.1 1.3-.2.2-.4.3-.7.1-.3-.2-1.4-.5-2.7-1.7-1-.9-1.7-2-1.9-2.3-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.3.3-.6.1-.2 0-.4 0-.6-.1-.2-.8-1.8-1-2.5-.3-.7-.5-.6-.8-.6h-.7c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.8s1.2 3.3 1.4 3.5c.2.2 2.4 3.6 5.8 5 .8.3 1.4.5 1.9.7.8.3 1.5.2 2.1.1.6-.1 2-.8 2.2-1.6.3-.8.3-1.4.2-1.6-.1-.1-.3-.2-.6-.3z"/></svg>';
  var ICON_A11Y =
    '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="4" r="2" fill="currentColor"/><path fill="currentColor" d="M20 8.5c-2.6.7-5.3 1-8 1s-5.4-.3-8-1l-.4 1.6c2 .6 4.2.9 6.4 1.1V14l-2.2 7.3 1.6.5L11.4 16h1.2l1.9 5.8 1.6-.5L14 14v-2.8c2.2-.2 4.4-.5 6.4-1.1L20 8.5z"/></svg>';
  var ICONS = {
    text: '<path d="M4 18L9 6l5 12M6 14h6M16 10h6M19 7v6" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    contrast: '<circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="2" fill="none"/><path d="M12 3a9 9 0 0 1 0 18z" fill="currentColor"/>',
    mono: '<circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="2" fill="none"/><path d="M12 3v18" stroke="currentColor" stroke-width="2"/>',
    links: '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>',
    font: '<path d="M5 19L11 5l6 14M7.5 14h7" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    spacing: '<path d="M4 6h16M4 12h16M4 18h16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    guide: '<path d="M3 12h18" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M3 6h12M3 18h12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" opacity=".5"/>',
    images: '<rect x="3" y="5" width="18" height="14" rx="2" stroke="currentColor" stroke-width="2" fill="none"/><path d="M4 20L20 4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    motion: '<circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="2" fill="none"/><path d="M10 9v6M14 9v6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    cursor: '<path d="M5 3l14 8-6 2-3 6z" stroke="currentColor" stroke-width="2" fill="none" stroke-linejoin="round"/>'
  };

  /* ================================================================ SOHBET */
  function buildChat() {
    var state = { step: 0, course: null, topic: null, openedAt: 0, lastOpener: null };

    var launch = el('button', { type: 'button', class: 'uc-launch', 'aria-label': T.launcher, 'aria-expanded': 'false', 'aria-controls': 'uc-panel', 'data-uslu-widget': '' });
    launch.innerHTML = ICON_WA;

    var panel = el('div', { id: 'uc-panel', class: 'uc-panel', role: 'dialog', 'aria-label': T.title, 'data-uslu-widget': '' });
    panel.hidden = true;
    var head = el('div', { class: 'uc-head' });
    var headText = el('div');
    headText.appendChild(el('b', null, T.title));
    var small = el('small');
    small.appendChild(el('span', { class: 'uc-dot', 'aria-hidden': 'true' }));
    small.appendChild(document.createTextNode(T.online));
    headText.appendChild(small);
    var x = el('button', { type: 'button', class: 'uc-x', 'aria-label': T.close }, '×');
    head.appendChild(headText);
    head.appendChild(x);
    var body = el('div', { class: 'uc-body', 'aria-live': 'polite' });
    panel.appendChild(head);
    panel.appendChild(body);

    var teaser = el('button', { type: 'button', class: 'uc-teaser', 'data-uslu-widget': '' }, T.teaser);
    teaser.hidden = true;

    function label(list, key) {
      for (var i = 0; i < list.length; i++) if (list[i][0] === key) return list[i][1];
      return T.none;
    }

    function focusFirst() {
      var f = body.querySelector('button, input, select, textarea');
      if (f) f.focus();
    }

    function options(list, onPick) {
      var wrap = el('div', { class: 'uc-opts' });
      list.forEach(function (item) {
        var b = el('button', { type: 'button', class: 'uc-opt' }, item[1]);
        b.addEventListener('click', function () { onPick(item[0]); });
        wrap.appendChild(b);
      });
      return wrap;
    }

    function backLink(to) {
      var b = el('button', { type: 'button', class: 'uc-link' }, '← ' + T.back);
      b.addEventListener('click', function () { render(to); });
      return b;
    }

    function message(data) {
      var lines = [T.intro, T.course + ': ' + label(T.courses, state.course), T.request + ': ' + label(T.topics, state.topic), T.lName + ': ' + data.name, T.lPhone + ': ' + data.phone];
      if (data.time) lines.push(T.lTime + ': ' + data.time);
      if (data.note) lines.push(T.lNote + ': ' + data.note);
      return lines.join('\n');
    }

    var form = { name: '', phone: '', time: '', note: '' };

    function render(step) {
      state.step = step;
      body.textContent = '';
      if (step === 0) {
        body.appendChild(el('div', { class: 'uc-msg' }, T.hello));
        body.appendChild(options(T.courses, function (k) { state.course = k; render(1); }));
      } else if (step === 1) {
        body.appendChild(el('div', { class: 'uc-msg' }, T.topic));
        body.appendChild(options(T.topics, function (k) { state.topic = k; state.openedAt = Date.now(); render(2); }));
        body.appendChild(backLink(0));
      } else if (step === 2) {
        body.appendChild(el('div', { class: 'uc-msg' }, T.contact));
        var f = el('form', { novalidate: '' });
        var hp = el('input', { type: 'text', name: 'website', tabindex: '-1', autocomplete: 'off', 'aria-hidden': 'true', class: 'uc-hp' });
        f.appendChild(hp);
        f.appendChild(el('label', { for: 'uc-name' }, T.name));
        var nm = el('input', { id: 'uc-name', type: 'text', autocomplete: 'name', maxlength: '80', placeholder: T.namePh, required: '' });
        nm.value = form.name;
        f.appendChild(nm);
        f.appendChild(el('label', { for: 'uc-phone' }, T.phone));
        var ph = el('input', { id: 'uc-phone', type: 'tel', autocomplete: 'tel', inputmode: 'tel', maxlength: '20', placeholder: T.phonePh, required: '' });
        ph.value = form.phone;
        f.appendChild(ph);
        f.appendChild(el('label', { for: 'uc-time' }, T.time));
        var tm = el('select', { id: 'uc-time' });
        T.times.forEach(function (t, i) {
          var o = el('option', { value: i === 0 ? '' : t }, t);
          if ((i === 0 && !form.time) || form.time === t) o.selected = true;
          tm.appendChild(o);
        });
        f.appendChild(tm);
        f.appendChild(el('label', { for: 'uc-note' }, T.note));
        var nt = el('textarea', { id: 'uc-note', maxlength: '300', placeholder: T.notePh });
        nt.value = form.note;
        f.appendChild(nt);
        var err = el('div', { class: 'uc-err', role: 'alert' });
        f.appendChild(err);
        f.appendChild(el('button', { type: 'submit', class: 'uc-main' }, T.cont));
        f.addEventListener('submit', function (ev) {
          ev.preventDefault();
          if (hp.value) return; // bot
          var name = nm.value.replace(/\s+/g, ' ').trim();
          var digits = ph.value.replace(/[^\d+]/g, '');
          if (name.length < 3 || name.indexOf(' ') < 0) { err.textContent = T.nameErr; nm.focus(); return; }
          if (!/^\+?\d{10,15}$/.test(digits)) { err.textContent = T.phoneErr; ph.focus(); return; }
          if (Date.now() - state.openedAt < 1500) { err.textContent = T.spamErr; return; }
          form.name = name;
          form.phone = ph.value.trim();
          form.time = tm.value;
          form.note = nt.value.replace(/\s+/g, ' ').trim().slice(0, 300);
          render(3);
        });
        body.appendChild(f);
        body.appendChild(backLink(1));
      } else if (step === 3) {
        var text = message(form);
        body.appendChild(el('div', { class: 'uc-msg' }, T.summary));
        body.appendChild(el('div', { class: 'uc-pre' }, text));
        var send = el('button', { type: 'button', class: 'uc-main uc-wa' }, T.send);
        send.addEventListener('click', function () {
          window.open('https://wa.me/' + PHONE + '?text=' + encodeURIComponent(text), '_blank', 'noopener');
          send.textContent = T.sent;
        });
        body.appendChild(send);
        var again = el('button', { type: 'button', class: 'uc-link' }, T.again);
        again.addEventListener('click', function () {
          state.course = null; state.topic = null;
          form.name = form.phone = form.time = form.note = '';
          render(0);
        });
        body.appendChild(backLink(2));
        body.appendChild(el('br'));
        body.appendChild(again);
        body.appendChild(el('div', { class: 'uc-note' }, T.privacy));
      }
      if (!panel.hidden) focusFirst();
    }

    function open(opts) {
      teaser.hidden = true;
      store.set('uc-seen', '1', true);
      if (opts && opts.course) {
        state.course = opts.course;
        state.topic = 'teklif';
        state.openedAt = Date.now();
        render(2);
      } else if (panel.hidden) {
        render(state.step || 0);
      }
      state.lastOpener = document.activeElement;
      panel.hidden = false;
      launch.setAttribute('aria-expanded', 'true');
      focusFirst();
    }

    function close() {
      panel.hidden = true;
      launch.setAttribute('aria-expanded', 'false');
      if (state.lastOpener && state.lastOpener.focus) state.lastOpener.focus();
    }

    launch.addEventListener('click', function () { panel.hidden ? open() : close(); });
    x.addEventListener('click', close);
    teaser.addEventListener('click', function () { open(); });
    panel.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });

    // "Teklif al" düğmeleri: data-uslu-quote="<kurs anahtarı>"
    document.addEventListener('click', function (e) {
      var t = e.target && e.target.closest ? e.target.closest('[data-uslu-quote]') : null;
      if (!t) return;
      e.preventDefault();
      open({ course: t.getAttribute('data-uslu-quote') || 'bilmiyorum' });
    });

    document.body.appendChild(teaser);
    document.body.appendChild(panel);
    document.body.appendChild(launch);

    // maliaksoy'daki gibi 30 sn sonra kendiliğinden açılır; oturumda bir kez. Dar
    // ekranda içeriği kapatmasın diye yalnız küçük bir baloncuk gösterilir.
    if (!store.get('uc-seen', true)) {
      window.setTimeout(function () {
        if (store.get('uc-seen', true) || !panel.hidden) return;
        store.set('uc-seen', '1', true);
        if (window.matchMedia && window.matchMedia('(min-width: 768px)').matches) open();
        else teaser.hidden = false;
      }, 30000);
    }
  }

  /* ======================================================= ERİŞİLEBİLİRLİK */
  function buildA11y() {
    var KEY = 'ua-prefs';
    var keys = ['text', 'contrast', 'mono', 'links', 'font', 'spacing', 'guide', 'images', 'motion', 'cursor'];
    var prefs = {};
    try { prefs = JSON.parse(store.get(KEY) || '{}') || {}; } catch (e) { prefs = {}; }

    var root = document.documentElement;
    var guide = el('div', { class: 'ua-guide', 'aria-hidden': 'true', 'data-uslu-widget': '' });

    function apply() {
      root.classList.remove('ua-text-1', 'ua-text-2');
      if (prefs.text === 1) root.classList.add('ua-text-1');
      if (prefs.text === 2) root.classList.add('ua-text-2');
      root.classList.toggle('ua-links', !!prefs.links);
      root.classList.toggle('ua-font', !!prefs.font);
      root.classList.toggle('ua-spacing', !!prefs.spacing);
      root.classList.toggle('ua-images', !!prefs.images);
      root.classList.toggle('ua-motion', !!prefs.motion);
      root.classList.toggle('ua-cursor', !!prefs.cursor);
      root.classList.toggle('ua-guide-on', !!prefs.guide);
      var f = [];
      if (prefs.mono) f.push('grayscale(1)');
      if (prefs.contrast) f.push('contrast(1.4)');
      root.style.filter = f.join(' ');
      buttons.forEach(function (b) {
        var k = b.getAttribute('data-k');
        var on = k === 'text' ? prefs.text > 0 : !!prefs[k];
        b.setAttribute('aria-pressed', on ? 'true' : 'false');
        if (k === 'text') b.querySelector('span').textContent = A.items.text + (prefs.text ? ' (' + (prefs.text === 1 ? '+' : '++') + ')' : '');
      });
      store.set(KEY, JSON.stringify(prefs));
    }

    var tab = el('button', { type: 'button', class: 'ua-tab', 'aria-label': A.open, 'aria-expanded': 'false', 'aria-controls': 'ua-panel', 'data-uslu-widget': '' });
    tab.innerHTML = ICON_A11Y;
    var panel = el('div', { id: 'ua-panel', class: 'ua-panel', role: 'dialog', 'aria-label': A.title, 'data-uslu-widget': '' });
    panel.hidden = true;
    var top = el('div', { class: 'ua-top' });
    var tt = el('div');
    tt.appendChild(el('b', null, A.title));
    tt.appendChild(el('small', null, A.hint));
    var cl = el('button', { type: 'button', class: 'ua-close', 'aria-label': A.close }, '×');
    top.appendChild(tt);
    top.appendChild(cl);
    panel.appendChild(top);
    var grid = el('div', { class: 'ua-grid' });
    var buttons = [];
    keys.forEach(function (k) {
      var b = el('button', { type: 'button', class: 'ua-btn', 'data-k': k, 'aria-pressed': 'false' });
      b.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">' + ICONS[k] + '</svg>';
      b.appendChild(el('span', null, A.items[k]));
      b.addEventListener('click', function () {
        if (k === 'text') prefs.text = ((prefs.text || 0) + 1) % 3;
        else prefs[k] = !prefs[k];
        apply();
      });
      buttons.push(b);
      grid.appendChild(b);
    });
    panel.appendChild(grid);
    var reset = el('button', { type: 'button', class: 'ua-reset' }, A.reset);
    reset.addEventListener('click', function () { prefs = {}; apply(); });
    panel.appendChild(reset);

    function open() {
      panel.hidden = false;
      tab.setAttribute('aria-expanded', 'true');
      buttons[0].focus();
    }
    function close() {
      panel.hidden = true;
      tab.setAttribute('aria-expanded', 'false');
      tab.focus();
    }
    tab.addEventListener('click', function () { panel.hidden ? open() : close(); });
    cl.addEventListener('click', close);
    panel.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
    document.addEventListener('click', function (e) {
      if (!panel.hidden && !panel.contains(e.target) && !tab.contains(e.target)) {
        panel.hidden = true;
        tab.setAttribute('aria-expanded', 'false');
      }
    });
    document.addEventListener('mousemove', function (e) {
      if (prefs.guide) guide.style.top = e.clientY - 7 + 'px';
    }, { passive: true });

    document.body.appendChild(guide);
    document.body.appendChild(panel);
    document.body.appendChild(tab);
    apply();
  }

  function init() {
    injectStyle();
    buildChat();
    buildA11y();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
