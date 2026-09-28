/*
 * Uslu Sürücü Kursu: WhatsApp teklif asistanı + erişilebilirlik çubuğu.
 *
 * Tawk.to yerine kendi asistanımız (maliaksoytesisat'taki akışın sürücü kursuna
 * uyarlanmışı), canlı destek görünümünde: talep, eğitim ve kimin için olduğu hızlı
 * cevapla; ad, telefon ve not yazma kutusundan alınır, hazır mesajla kursun WhatsApp
 * hattına geçilir. Bilgiler SİTEDE SAKLANMAZ; mesajı ziyaretçi kendi WhatsApp'ından
 * gönderir.
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
        launcher: 'Chat with us',
        title: 'Uslu Driving School',
        online: 'Online',
        hours: 'Daily 09.00-19.30',
        close: 'Close',
        restart: 'Start over',
        typing: 'typing',
        greet: ['Good morning', 'Good afternoon', 'Good evening'],
        welcome: '{g}, welcome to Uslu Driving School.',
        helpQ: 'How can we help you today?',
        ack: {
          teklif: 'Happy to help. Let us prepare a quote just for you.',
          kayit: 'Great, let us help you with your enrolment.',
          program: 'Of course, let us clarify the schedule and duration for you.',
          soru: 'Of course, we are here to help.'
        },
        courseQ: 'Which licence course are you interested in?',
        whoQ: 'Who is the course for?',
        whoAckSelf: 'Got it.',
        whoAckOther: 'Got it, let us prepare the details for them together.',
        nameQ: 'So we can get back to you, could you type your first and last name?',
        nameQOther: 'Could you type your own first and last name? We will get back to you.',
        namePh: 'e.g. Ayşe Yılmaz',
        phoneQ: 'Nice to meet you, {n}. Which number can we reach you on?',
        phonePh: '0532 123 45 67',
        phoneHint: '11 digits starting with 0',
        timeQ: 'When is a good time to call you? You can choose more than one.',
        anyTime: 'Any time',
        noteQ: 'Is there anything you would like to add?',
        notePh: 'Write a note...',
        noNote: 'No, that is all',
        pickHint: 'Choose an option above',
        cont: 'Continue',
        sendAria: 'Send',
        nameErr: 'Please enter your first and last name together (e.g. Ayşe Yılmaz).',
        nameChars: 'Your name can only contain letters.',
        phoneStart: 'The number must start with 0.',
        phoneLen: 'The number must have 11 digits (currently {n}).',
        spamErr: 'That was very fast. Please wait a moment and try again.',
        summary: 'Thank you, {n}. Your message is ready; you can check it before sending.',
        send: 'Send message',
        sent: 'Opened, please send it there',
        after: 'Once you send the message, our team will get back to you during working hours (daily 09.00-19.30).',
        privacy: 'Your details are not stored on this website; you send the message from your own WhatsApp.',
        teaser: 'Would you like a quote?',
        course: 'Course',
        request: 'Request',
        lWho: 'Course is for',
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
          ['soru', 'Something else']
        ],
        who: [
          ['kendim', 'For myself'],
          ['cocugum', 'For my child'],
          ['kardesim', 'For my sibling'],
          ['esim', 'For my spouse'],
          ['yakinim', 'For a relative or friend']
        ],
        times: ['Morning', 'Afternoon', 'Evening']
      }
    : {
        launcher: 'Bize yazın',
        title: 'Uslu Sürücü Kursu',
        online: 'Çevrimiçi',
        hours: 'Her gün 09.00-19.30',
        close: 'Kapat',
        restart: 'Baştan başla',
        typing: 'yazıyor',
        greet: ['Günaydın', 'İyi günler', 'İyi akşamlar'],
        welcome: '{g}, Uslu Sürücü Kursu’na hoş geldiniz.',
        helpQ: 'Size nasıl yardımcı olabiliriz?',
        ack: {
          teklif: 'Memnuniyetle. Size özel bir teklif hazırlayalım.',
          kayit: 'Harika, kaydınız için size yardımcı olalım.',
          program: 'Tabii, ders programını ve süreyi sizin için netleştirelim.',
          soru: 'Elbette, size yardımcı olalım.'
        },
        courseQ: 'Hangi ehliyet eğitimiyle ilgileniyorsunuz?',
        whoQ: 'Eğitimi kimin için düşünüyorsunuz?',
        whoAckSelf: 'Anladım.',
        whoAckOther: 'Anladım, bilgileri onun için birlikte hazırlayalım.',
        nameQ: 'Size dönüş yapabilmemiz için adınızı ve soyadınızı yazar mısınız?',
        nameQOther: 'Size dönüş yapabilmemiz için kendi adınızı ve soyadınızı yazar mısınız?',
        namePh: 'Örn. Ayşe Yılmaz',
        phoneQ: 'Memnun oldum, {n}. Size hangi numaradan ulaşalım?',
        phonePh: '0532 123 45 67',
        phoneHint: '0 ile başlayan 11 hane',
        timeQ: 'Sizi hangi saatlerde aramamız uygun olur? Birden fazla seçebilirsiniz.',
        anyTime: 'Fark etmez',
        noteQ: 'Eklemek istediğiniz bir not var mı?',
        notePh: 'Notunuzu yazın...',
        noNote: 'Yok, bu kadar',
        pickHint: 'Yukarıdan bir seçenek belirleyin',
        cont: 'Devam et',
        sendAria: 'Gönder',
        nameErr: 'Adınızı ve soyadınızı birlikte yazın (örn. Ayşe Yılmaz).',
        nameChars: 'Ad soyad yalnız harf içermeli.',
        phoneStart: 'Numara 0 ile başlamalı.',
        phoneLen: 'Numara 11 haneli olmalı (şu an {n} hane).',
        spamErr: 'Çok hızlı ilerlediniz. Birkaç saniye bekleyip yeniden deneyin.',
        summary: 'Teşekkürler {n}. Mesajınız hazır, göndermeden önce göz atabilirsiniz.',
        send: 'Mesaj gönder',
        sent: 'Açıldı, oradan gönderin',
        after: 'Mesajınızı gönderdiğinizde ekibimiz mesai saatlerinde (her gün 09.00-19.30) size dönüş yapar.',
        privacy: 'Bilgileriniz bu sitede saklanmaz; mesajı kendi WhatsApp’ınızdan siz gönderirsiniz.',
        teaser: 'Teklif almak ister misiniz?',
        course: 'İlgilendiğim eğitim',
        request: 'Talebim',
        lWho: 'Eğitim kimin için',
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
          ['soru', 'Başka bir konu']
        ],
        who: [
          ['kendim', 'Kendim için'],
          ['cocugum', 'Çocuğum için'],
          ['kardesim', 'Kardeşim için'],
          ['esim', 'Eşim için'],
          ['yakinim', 'Bir yakınım veya arkadaşım için']
        ],
        times: ['Sabah', 'Öğle', 'Akşam']
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
  var NAVY = '#041e37', RED = '#cb1643';
  var CSS =
    '[data-uslu-widget]{font-family:inherit;box-sizing:border-box}' +
    '[data-uslu-widget] *{box-sizing:border-box}' +
    '[data-uslu-widget] button,[data-uslu-widget] input,[data-uslu-widget] select,[data-uslu-widget] textarea{font-family:inherit}' +
    '#scroll-top{bottom:92px!important;right:24px!important}' +
    /* sohbet: canlı destek görünümü; sitenin lacivert/kırmızı dili, baloncuklar yuvarlak */
    '.uc-launch{position:fixed;right:20px;bottom:20px;z-index:9990;width:58px;height:58px;border-radius:50%;border:0;background:#25d366;color:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 24px rgb(0 0 0 / 20%);cursor:pointer;transition:transform .2s}' +
    '.uc-launch:hover{transform:translateY(-2px)}.uc-launch:focus-visible{outline:3px solid ' + RED + ';outline-offset:3px}' +
    '.uc-launch svg{width:30px;height:30px}' +
    '.uc-teaser{position:fixed;right:88px;bottom:30px;z-index:9990;background:#fff;color:' + NAVY + ';border:0;border-radius:16px 16px 4px 16px;padding:10px 14px;font-size:14px;font-weight:600;box-shadow:0 6px 30px rgb(4 30 55 / 18%);cursor:pointer;max-width:220px;text-align:left}' +
    '.uc-panel{position:fixed;right:20px;bottom:90px;z-index:9991;width:370px;max-width:calc(100vw - 24px);height:min(600px,calc(100vh - 112px));display:flex;flex-direction:column;background:#fff;color:' + NAVY + ';border-radius:16px;box-shadow:0 12px 48px rgb(4 30 55 / 28%);overflow:hidden}' +
    '.uc-panel[hidden]{display:none}' +
    '.uc-head{display:flex;align-items:center;gap:12px;padding:14px 14px 14px 16px;background:' + NAVY + ';color:#fff;border-top:3px solid ' + RED + ';flex:0 0 auto}' +
    '.uc-ava{position:relative;width:42px;height:42px;flex:0 0 42px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center}' +
    '.uc-ava img{width:34px;height:34px;border-radius:50%;object-fit:contain}' +
    '.uc-ava::after{content:"";position:absolute;right:0;bottom:1px;width:11px;height:11px;border-radius:50%;background:#22c55e;border:2px solid ' + NAVY + '}' +
    '.uc-head b{display:block;font-size:16px;font-weight:700;line-height:1.2}' +
    '.uc-head small{display:block;font-size:12px;opacity:.82;margin-top:3px}' +
    '.uc-hbtn{background:transparent;border:0;color:#fff;width:34px;height:34px;border-radius:50%;cursor:pointer;display:flex;align-items:center;justify-content:center;opacity:.85;flex:0 0 34px}' +
    '.uc-hbtn:hover{opacity:1;background:rgb(255 255 255 / 10%)}.uc-hbtn svg{width:18px;height:18px}' +
    '.uc-hgap{margin-left:auto}' +
    '.uc-log{flex:1 1 auto;overflow-y:auto;padding:16px 14px 10px;background:#f3f5f8;display:flex;flex-direction:column;gap:4px;font-size:14.5px;line-height:1.45;scroll-behavior:smooth}' +
    '.uc-row{display:flex;align-items:flex-end;gap:8px;animation:uc-in .22s ease-out both}' +
    '.uc-row.uc-me{justify-content:flex-end}' +
    '.uc-row.uc-gap{margin-top:8px}' +
    '.uc-av{width:26px;height:26px;flex:0 0 26px;border-radius:50%;background:#fff;border:1px solid #e3e7ec;display:flex;align-items:center;justify-content:center;overflow:hidden}' +
    '.uc-av img{width:20px;height:20px;object-fit:contain}.uc-av.uc-blank{visibility:hidden}' +
    '.uc-bub{max-width:80%;padding:9px 13px;border-radius:18px;white-space:pre-wrap;word-wrap:break-word}' +
    '.uc-bot .uc-bub{background:#fff;color:' + NAVY + ';border-bottom-left-radius:5px;box-shadow:0 1px 2px rgb(4 30 55 / 8%)}' +
    '.uc-me .uc-bub{background:' + NAVY + ';color:#fff;border-bottom-right-radius:5px}' +
    '.uc-tick{display:inline-block;width:15px;height:10px;margin-left:6px;vertical-align:-1px;color:#7dd3fc}' +
    '.uc-dots{display:inline-flex;gap:4px;padding:3px 0}.uc-dots i{width:7px;height:7px;border-radius:50%;background:#9aa4b2;animation:uc-dot 1.1s infinite ease-in-out}' +
    '.uc-dots i:nth-child(2){animation-delay:.15s}.uc-dots i:nth-child(3){animation-delay:.3s}' +
    '@keyframes uc-dot{0%,60%,100%{transform:translateY(0);opacity:.5}30%{transform:translateY(-4px);opacity:1}}' +
    '@keyframes uc-in{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}' +
    '.uc-replies{display:flex;flex-wrap:wrap;justify-content:flex-end;gap:6px;margin:8px 0 2px 34px;animation:uc-in .22s ease-out both}' +
    '.uc-reply{border:1.5px solid ' + RED + ';background:#fff;color:' + RED + ';border-radius:18px;padding:7px 13px;font-size:13.5px;font-weight:600;line-height:1.3;cursor:pointer;text-align:left;transition:background .15s,color .15s}' +
    '.uc-reply:hover,.uc-reply[aria-pressed="true"]{background:' + RED + ';color:#fff}' +
    '.uc-reply.uc-go{background:' + NAVY + ';border-color:' + NAVY + ';color:#fff}.uc-reply.uc-go:hover{background:' + RED + ';border-color:' + RED + '}' +
    '.uc-card{margin:4px 0 0 34px;background:#fff;border-left:3px solid ' + RED + ';border-radius:4px 12px 12px 4px;padding:10px 12px;font-size:13px;line-height:1.55;white-space:pre-wrap;color:' + NAVY + ';box-shadow:0 1px 2px rgb(4 30 55 / 8%);animation:uc-in .22s ease-out both}' +
    '.uc-dock{flex:0 0 auto;border-top:1px solid #e6e9ee;background:#fff;padding:10px 12px 12px}' +
    '.uc-hint{font-size:12px;color:#6b7280;margin:0 4px 6px;min-height:16px}.uc-hint.uc-bad{color:' + RED + ';font-weight:600}.uc-hint.uc-good{color:#15803d;font-weight:600}' +
    '.uc-comp{display:flex;align-items:center;gap:8px}' +
    '.uc-comp input{flex:1 1 auto;min-width:0;border:1px solid #dfe3e8;border-radius:22px;padding:10px 15px;font-size:15px;color:' + NAVY + ';background:#fff}' +
    '.uc-comp input:focus{border-color:' + NAVY + ';outline:0}.uc-comp input[aria-invalid="true"]{border-color:' + RED + '}' +
    '.uc-comp input:disabled{background:#f5f6f8;border-color:#eceef1}' +
    '.uc-sendb{width:42px;height:42px;flex:0 0 42px;border-radius:50%;border:0;background:' + RED + ';color:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:background .2s}' +
    '.uc-sendb:hover{background:' + NAVY + '}.uc-sendb:disabled{background:#d6dae0;cursor:default}.uc-sendb svg{width:18px;height:18px}' +
    '.uc-panel button:focus-visible,.uc-panel input:focus-visible{outline:3px solid ' + RED + ';outline-offset:2px}' +
    '.uc-main{display:flex;align-items:center;justify-content:space-between;width:100%;border:0;border-radius:28px;padding:7px 8px 7px 18px;background:' + RED + ';color:#fff;font-weight:600;font-size:15px;text-transform:uppercase;cursor:pointer;box-shadow:0 3px 24px rgb(0 0 0 / 10%);transition:background .4s}' +
    '.uc-main:hover{background:' + NAVY + '}' +
    '.uc-main .uc-ic{display:flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:50%;background:#fff;color:' + RED + ';margin-left:12px;flex:0 0 36px}' +
    '.uc-main .uc-ic svg{width:18px;height:18px}' +
    '.uc-note{font-size:11.5px;color:#6b7280;margin-top:8px;line-height:1.45;text-align:center}' +
    '.uc-hp{position:absolute!important;left:-9999px!important;width:1px;height:1px;overflow:hidden}' +
    '@media (max-width:480px){.uc-panel{right:10px;left:10px;width:auto;bottom:84px;height:calc(100vh - 100px);height:calc(100dvh - 100px)}}' +
    '@media (prefers-reduced-motion:reduce){.uc-row,.uc-replies,.uc-card{animation:none}.uc-dots i{animation:none}.uc-log{scroll-behavior:auto}}' +
    /* erişilebilirlik: aynı dil, küçük ve köşeli */
    '.ua-tab{position:fixed;left:0;top:50%;transform:translateY(-50%);z-index:9989;width:34px;height:42px;border:0;border-radius:0 4px 4px 0;background:' + NAVY + ';color:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer;box-shadow:0 3px 24px rgb(0 0 0 / 15%);opacity:.8;border-right:3px solid ' + RED + ';transition:opacity .2s,width .2s}' +
    '.ua-tab:hover,.ua-tab:focus-visible,.ua-tab[aria-expanded="true"]{opacity:1;width:38px}.ua-tab:focus-visible{outline:3px solid ' + RED + ';outline-offset:2px}' +
    '.ua-tab svg{width:20px;height:20px}' +
    '.ua-panel{position:fixed;left:46px;top:50%;transform:translateY(-50%);z-index:9989;width:268px;max-width:calc(100vw - 58px);max-height:calc(100vh - 24px);overflow-y:auto;background:#fff;color:' + NAVY + ';box-shadow:0 0 50px 0 rgb(32 32 32 / 22%)}' +
    '.ua-panel[hidden]{display:none}' +
    '.ua-top{display:flex;align-items:flex-start;gap:8px;padding:14px 14px 16px;background:' + NAVY + ';color:#fff;border-top:4px solid ' + RED + '}' +
    '.ua-top b{font-size:15px;font-weight:700;display:block;padding-bottom:9px;position:relative}' +
    '.ua-top b::before,.ua-top b::after{content:"";position:absolute;bottom:0;height:3px;background:' + RED + '}.ua-top b::before{left:0;width:15px}.ua-top b::after{left:20px;width:35px}' +
    '.ua-top small{display:block;font-size:11px;opacity:.8;margin-top:7px}' +
    '.ua-close{margin-left:auto;background:transparent;border:0;width:28px;height:28px;cursor:pointer;font-size:20px;color:#fff;opacity:.85}' +
    '.ua-grid{display:grid;grid-template-columns:1fr 1fr;gap:6px;padding:12px 12px 4px}' +
    '.ua-btn{display:flex;align-items:center;gap:7px;border:1px solid #e6e9ed;background:#fff;border-radius:0;padding:8px;font-size:12px;font-weight:600;line-height:1.25;color:' + NAVY + ';cursor:pointer;text-align:left;min-height:40px;transition:border-color .2s}' +
    '.ua-btn:hover{border-color:' + RED + '}' +
    '.ua-btn svg{width:16px;height:16px;flex:0 0 16px;color:' + RED + '}' +
    '.ua-btn[aria-pressed="true"]{background:' + RED + ';border-color:' + RED + ';color:#fff}.ua-btn[aria-pressed="true"] svg{color:#fff}' +
    '.ua-btn:focus-visible,.ua-close:focus-visible,.ua-reset:focus-visible{outline:3px solid ' + RED + ';outline-offset:2px}' +
    '.ua-reset{margin:4px 12px 12px;background:transparent;border:0;color:#6b7280;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.03em;cursor:pointer;padding:6px 0}.ua-reset:hover{color:' + RED + '}' +
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
  // Canlı destek havası (Ahmet, 28.09.2026: "chat ediliyormuş havası vermeli, premium
  // müşteri hizmetleri gibi"): asistan baloncukla yazar, önce "yazıyor" görünür;
  // seçenekler hızlı cevap düğmesi, serbest bilgi alttaki yazma kutusundan alınır.
  // Akış: nasıl yardımcı olabiliriz → eğitim → kimin için → ad soyad → telefon →
  // arama zamanı → not → özet ve "Mesaj gönder".
  function buildChat() {
    var AVATAR = '/assets/img/course/logo-avatar.webp';
    var REDUCED = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    // quiet: kendiliğinden açıldıysa ziyaretçi panele dokunana dek odak sayfada kalır.
    var state, gen = 0, lastSide = null, lastOpener = null, quiet = false;

    function reset() {
      state = { topic: null, course: null, who: null, name: '', phone: '', times: [], note: '', openedAt: 0 };
    }
    reset();

    var launch = el('button', { type: 'button', class: 'uc-launch', 'aria-label': T.launcher, 'aria-expanded': 'false', 'aria-controls': 'uc-panel', 'data-uslu-widget': '' });
    launch.innerHTML = ICON_WA;

    var panel = el('div', { id: 'uc-panel', class: 'uc-panel', role: 'dialog', 'aria-label': T.title, 'data-uslu-widget': '' });
    panel.hidden = true;
    var head = el('div', { class: 'uc-head' });
    var ava = el('span', { class: 'uc-ava', 'aria-hidden': 'true' });
    ava.appendChild(el('img', { src: AVATAR, alt: '', width: '34', height: '34' }));
    var headText = el('div');
    headText.appendChild(el('b', null, T.title));
    headText.appendChild(el('small', null, T.online + ' · ' + T.hours));
    var again = el('button', { type: 'button', class: 'uc-hbtn uc-hgap', 'aria-label': T.restart, title: T.restart });
    again.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12a8 8 0 1 0 2.3-5.7M4 4v4h4" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    var x = el('button', { type: 'button', class: 'uc-hbtn', 'aria-label': T.close, title: T.close });
    x.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>';
    head.appendChild(ava);
    head.appendChild(headText);
    head.appendChild(again);
    head.appendChild(x);
    var log = el('div', { class: 'uc-log', role: 'log', 'aria-live': 'polite' });
    var dock = el('div', { class: 'uc-dock' });
    panel.appendChild(head);
    panel.appendChild(log);
    panel.appendChild(dock);

    var teaser = el('button', { type: 'button', class: 'uc-teaser', 'data-uslu-widget': '' }, T.teaser);
    teaser.hidden = true;

    var TICK = '<svg class="uc-tick" viewBox="0 0 16 10" aria-hidden="true" focusable="false"><path d="M1 5.5l3 3L10 2M6.5 8.5L13 2" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    var PLANE = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12l16-8-6 16-2.5-6.5z" stroke="currentColor" stroke-width="2" fill="none" stroke-linejoin="round"/></svg>';

    function label(list, key) {
      for (var i = 0; i < list.length; i++) if (list[i][0] === key) return list[i][1];
      return T.none;
    }
    function fill(s, map) {
      return s.replace(/\{(\w)\}/g, function (m, k) { return map[k] != null ? map[k] : m; });
    }
    function scrollDown() { log.scrollTop = log.scrollHeight; }
    function focusIn(node) { if (!quiet && !panel.hidden && node && node.focus) node.focus(); }

    // Baloncuk. Asistanın ardışık mesajlarında logo yalnız ilkinde görünür.
    function row(side) {
      var r = el('div', { class: 'uc-row uc-' + side + (lastSide && lastSide !== side ? ' uc-gap' : '') });
      if (side === 'bot') {
        var av = el('span', { class: 'uc-av' + (lastSide === 'bot' ? ' uc-blank' : ''), 'aria-hidden': 'true' });
        av.appendChild(el('img', { src: AVATAR, alt: '', width: '20', height: '20' }));
        r.appendChild(av);
      }
      lastSide = side;
      return r;
    }
    function bubble(side, text) {
      var r = row(side);
      var b = el('div', { class: 'uc-bub' }, text);
      if (side === 'me') b.insertAdjacentHTML('beforeend', TICK);
      r.appendChild(b);
      log.appendChild(r);
      scrollDown();
      return r;
    }

    // Asistan yazar: önce "yazıyor", sonra mesaj. Yeniden başlatılırsa eski sıra durur.
    function say(lines, done) {
      var g = gen, i = 0;
      (function next() {
        if (g !== gen) return;
        if (i >= lines.length) { if (done) done(); return; }
        var text = lines[i++];
        if (REDUCED) { bubble('bot', text); next(); return; }
        var r = row('bot');
        var b = el('div', { class: 'uc-bub', 'aria-label': T.typing });
        b.innerHTML = '<span class="uc-dots" aria-hidden="true"><i></i><i></i><i></i></span>';
        r.appendChild(b);
        log.appendChild(r);
        scrollDown();
        window.setTimeout(function () {
          if (g !== gen) return;
          b.removeAttribute('aria-label');
          b.textContent = text;
          scrollDown();
          next();
        }, Math.min(1200, 450 + text.length * 11));
      })();
    }

    // Alt kutu: seçenek adımlarında kapalı, serbest yanıt adımlarında açık.
    function idleDock() {
      dock.textContent = '';
      dock.appendChild(el('div', { class: 'uc-hint' }));
      var c = el('div', { class: 'uc-comp' });
      var inp = el('input', { type: 'text', placeholder: T.pickHint, disabled: '', 'aria-label': T.pickHint });
      var sb = el('button', { type: 'button', class: 'uc-sendb', disabled: '', 'aria-label': T.sendAria });
      sb.innerHTML = PLANE;
      c.appendChild(inp);
      c.appendChild(sb);
      dock.appendChild(c);
    }

    function replies(list, onPick) {
      idleDock();
      var wrap = el('div', { class: 'uc-replies' });
      list.forEach(function (item) {
        var b = el('button', { type: 'button', class: 'uc-reply' }, item[1]);
        b.addEventListener('click', function () {
          wrap.remove();
          bubble('me', item[1]);
          onPick(item[0]);
        });
        wrap.appendChild(b);
      });
      log.appendChild(wrap);
      scrollDown();
      focusIn(wrap.querySelector('button'));
    }

    function multi(list, onDone) {
      idleDock();
      var wrap = el('div', { class: 'uc-replies' });
      var picked = [];
      list.forEach(function (t) {
        var b = el('button', { type: 'button', class: 'uc-reply', 'aria-pressed': 'false' }, t);
        b.addEventListener('click', function () {
          var i = picked.indexOf(t);
          if (i >= 0) picked.splice(i, 1); else picked.push(t);
          b.setAttribute('aria-pressed', i >= 0 ? 'false' : 'true');
          go.textContent = picked.length ? T.cont + ' →' : T.anyTime;
        });
        wrap.appendChild(b);
      });
      var go = el('button', { type: 'button', class: 'uc-reply uc-go' }, T.anyTime);
      go.addEventListener('click', function () {
        var chosen = list.filter(function (t) { return picked.indexOf(t) >= 0; });
        wrap.remove();
        bubble('me', chosen.length ? chosen.join(', ') : T.anyTime);
        onDone(chosen);
      });
      wrap.appendChild(go);
      log.appendChild(wrap);
      scrollDown();
      focusIn(wrap.querySelector('button'));
    }

    // Serbest yanıt: cfg = { ph, type, mode, hint(v)->[metin, sınıf], format(v), check(v)->hata|null, skip }
    function ask(cfg, onOk) {
      var skipWrap = null;
      dock.textContent = '';
      var hint = el('div', { class: 'uc-hint', id: 'uc-hint' });
      var f = el('form', { class: 'uc-comp', novalidate: '' });
      var hp = el('input', { type: 'text', name: 'website', tabindex: '-1', autocomplete: 'off', 'aria-hidden': 'true', class: 'uc-hp' });
      var inp = el('input', { id: cfg.id, type: cfg.type || 'text', placeholder: cfg.ph, maxlength: String(cfg.max || 80), autocomplete: cfg.ac || 'off', 'aria-label': cfg.ph, 'aria-describedby': 'uc-hint' });
      if (cfg.mode) inp.setAttribute('inputmode', cfg.mode);
      var sb = el('button', { type: 'submit', class: 'uc-sendb', 'aria-label': T.sendAria });
      sb.innerHTML = PLANE;
      f.appendChild(hp);
      f.appendChild(inp);
      f.appendChild(sb);
      function paint() {
        if (cfg.format) inp.value = cfg.format(inp.value);
        var h = cfg.hint ? cfg.hint(inp.value) : ['', ''];
        hint.textContent = h[0];
        hint.className = 'uc-hint' + (h[1] ? ' ' + h[1] : '');
        inp.removeAttribute('aria-invalid');
      }
      inp.addEventListener('input', paint);
      paint();
      f.addEventListener('submit', function (ev) {
        ev.preventDefault();
        if (hp.value) return; // bot
        var v = inp.value.replace(/\s+/g, ' ').trim();
        var problem = cfg.check ? cfg.check(v) : null;
        if (problem) {
          hint.textContent = problem;
          hint.className = 'uc-hint uc-bad';
          inp.setAttribute('aria-invalid', 'true');
          inp.focus();
          return;
        }
        if (!v && cfg.skip) return;
        if (skipWrap) skipWrap.remove();
        idleDock();
        bubble('me', cfg.show ? cfg.show(v) : v);
        onOk(v);
      });
      dock.appendChild(hint);
      dock.appendChild(f);
      if (cfg.skip) {
        var wrap = skipWrap = el('div', { class: 'uc-replies' });
        var s = el('button', { type: 'button', class: 'uc-reply' }, cfg.skip);
        s.addEventListener('click', function () {
          wrap.remove();
          idleDock();
          bubble('me', cfg.skip);
          onOk('');
        });
        wrap.appendChild(s);
        log.appendChild(wrap);
        scrollDown();
      }
      scrollDown();
      focusIn(inp);
    }

    // Telefon: 0 ile başlayan 11 hane (Ahmet, 28.09.2026). +90 ile yazılırsa 0'a çevrilir;
    // yazarken "0532 123 45 67" biçimine girer.
    function phoneDigits(v) {
      var d = String(v || '').replace(/\D/g, '');
      if (d.indexOf('90') === 0 && d.length > 11) d = '0' + d.slice(2);
      return d.slice(0, 11);
    }
    function phoneFormat(d) {
      return [d.slice(0, 4), d.slice(4, 7), d.slice(7, 9), d.slice(9, 11)].filter(Boolean).join(' ');
    }
    function phoneProblem(d) {
      if (!d) return T.phoneLen.replace('{n}', '0');
      if (d.charAt(0) !== '0') return T.phoneStart;
      if (d.length !== 11) return T.phoneLen.replace('{n}', String(d.length));
      return null;
    }
    // Ad soyad: en az iki kelime, yalnız harf (Türkçe dahil). Baş harfler büyütülür.
    var NAME_OK = /^[\p{L}'’.\-]{2,}(?: [\p{L}'’.\-]{2,})+$/u;
    function nameProblem(v) {
      if (/[\d_@#$%^&*()+=<>?!/\\|{}\[\]]/.test(v)) return T.nameChars;
      return NAME_OK.test(v) ? null : T.nameErr;
    }
    function titleCase(v) {
      var loc = EN ? 'en' : 'tr';
      return v.split(' ').map(function (w) {
        return w.charAt(0).toLocaleUpperCase(loc) + w.slice(1).toLocaleLowerCase(loc);
      }).join(' ');
    }

    function message() {
      var lines = [
        T.intro,
        T.request + ': ' + label(T.topics, state.topic),
        T.course + ': ' + label(T.courses, state.course),
        T.lWho + ': ' + label(T.who, state.who),
        T.lName + ': ' + state.name,
        T.lPhone + ': ' + state.phone
      ];
      if (state.times.length) lines.push(T.lTime + ': ' + state.times.join(', '));
      if (state.note) lines.push(T.lNote + ': ' + state.note);
      return lines.join('\n');
    }

    function greeting() {
      var h = new Date().getHours();
      return fill(T.welcome, { g: T.greet[h < 11 ? 0 : h < 18 ? 1 : 2] });
    }

    /* ---- akış ---- */
    function stepTopic() {
      say([greeting(), T.helpQ], function () {
        replies(T.topics, function (k) { state.topic = k; stepCourse(true); });
      });
    }
    function stepCourse(withAck) {
      say((withAck ? [T.ack[state.topic]] : []).concat(T.courseQ), function () {
        replies(T.courses, function (k) { state.course = k; stepWho(); });
      });
    }
    function stepWho(pre) {
      say((pre || []).concat(T.whoQ), function () {
        replies(T.who, function (k) {
          state.who = k;
          state.openedAt = Date.now();
          stepName();
        });
      });
    }
    function stepName() {
      var self = state.who === 'kendim';
      say([self ? T.whoAckSelf : T.whoAckOther, self ? T.nameQ : T.nameQOther], function () {
        ask({ id: 'uc-name', ph: T.namePh, ac: 'name', max: 80, check: nameProblem, show: titleCase }, function (v) {
          state.name = titleCase(v);
          stepPhone();
        });
      });
    }
    function stepPhone() {
      say([fill(T.phoneQ, { n: state.name.split(' ')[0] })], function () {
        ask({
          id: 'uc-phone', ph: T.phonePh, type: 'tel', mode: 'numeric', ac: 'tel-national', max: 14,
          format: function (v) { return phoneFormat(phoneDigits(v)); },
          hint: function (v) {
            var d = phoneDigits(v);
            if (d.length && d.charAt(0) !== '0') return [T.phoneStart, 'uc-bad'];
            return [T.phoneHint + ' · ' + d.length + '/11', d.length === 11 ? 'uc-good' : ''];
          },
          check: function (v) {
            var p = phoneProblem(phoneDigits(v));
            if (!p && Date.now() - state.openedAt < 1500) return T.spamErr;
            return p;
          },
          show: function (v) { return phoneFormat(phoneDigits(v)); }
        }, function (v) {
          state.phone = phoneFormat(phoneDigits(v));
          stepTime();
        });
      });
    }
    function stepTime() {
      say([T.timeQ], function () {
        multi(T.times, function (chosen) { state.times = chosen; stepNote(); });
      });
    }
    function stepNote() {
      say([T.noteQ], function () {
        ask({ id: 'uc-note', ph: T.notePh, max: 300, skip: T.noNote }, function (v) {
          state.note = v.slice(0, 300);
          stepSummary();
        });
      });
    }
    function stepSummary() {
      var text = message();
      say([fill(T.summary, { n: state.name.split(' ')[0] })], function () {
        log.appendChild(el('div', { class: 'uc-card' }, text));
        scrollDown();
        dock.textContent = '';
        var b = el('button', { type: 'button', class: 'uc-main' });
        var bt = el('span', null, T.send);
        var ic = el('span', { class: 'uc-ic', 'aria-hidden': 'true' });
        ic.innerHTML = PLANE;
        b.appendChild(bt);
        b.appendChild(ic);
        var told = false;
        b.addEventListener('click', function () {
          window.open('https://wa.me/' + PHONE + '?text=' + encodeURIComponent(text), '_blank', 'noopener');
          bt.textContent = T.sent;
          if (!told) { told = true; say([T.after]); }
        });
        dock.appendChild(b);
        dock.appendChild(el('div', { class: 'uc-note' }, T.privacy));
        scrollDown();
        focusIn(b);
      });
    }

    function restart(course) {
      gen++;
      reset();
      log.textContent = '';
      lastSide = null;
      idleDock();
      if (course) {
        // Kurs kartındaki "Teklif al": talep ve kurs belli, "kimin için" sorusundan devam.
        state.topic = 'teklif';
        state.course = course;
        say([greeting()], function () {
          bubble('me', label(T.topics, 'teklif'));
          bubble('me', label(T.courses, course));
          stepWho([T.ack.teklif]);
        });
      } else {
        stepTopic();
      }
    }

    var started = false;
    function open(opts) {
      teaser.hidden = true;
      store.set('uc-seen', '1', true);
      quiet = !!(opts && opts.auto);
      if (!quiet) lastOpener = document.activeElement;
      panel.hidden = false;
      launch.setAttribute('aria-expanded', 'true');
      if (opts && opts.course) { started = true; restart(opts.course); }
      else if (!started) { started = true; restart(); }
      else {
        var f = dock.querySelector('input:not([disabled]), button') || log.querySelector('.uc-replies button');
        focusIn(f);
      }
    }

    function close() {
      panel.hidden = true;
      launch.setAttribute('aria-expanded', 'false');
      if (lastOpener && lastOpener.focus) lastOpener.focus();
    }

    launch.addEventListener('click', function () { panel.hidden ? open() : close(); });
    x.addEventListener('click', close);
    again.addEventListener('click', function () { restart(); });
    teaser.addEventListener('click', function () { open(); });
    panel.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
    panel.addEventListener('pointerdown', function () { quiet = false; });

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
        if (window.matchMedia && window.matchMedia('(min-width: 768px)').matches) open({ auto: true });
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
