/*
 * Uslu Sürücü Kursu: canlı destek görünümlü teklif asistanı + erişilebilirlik çubuğu.
 *
 * Tawk.to yerine kendi asistanımız (maliaksoytesisat'taki akışın sürücü kursuna
 * uyarlanmışı): talep, eğitim ve kimin için olduğu liste kartından; ad soyad ve telefon
 * tek form kartından alınır. "Mesaj gönder" talebi /api/iletisim/ üzerinden Resend ile
 * kursun e-postasına iletir (site veriyi SAKLAMAZ); iletilemezse aynı talep WhatsApp'tan
 * gönderilebilir. Metinler KVKK aydınlatma metniyle (/kvkk/) uyumlu tutulur.
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
        launcher: 'Live chat',
        title: 'Uslu Driving School',
        online: 'Online',
        hours: 'Open 7 days',
        hoursLong: 'Monday-Thursday 09.00-19.30, Friday-Sunday 09.00-20.30',
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
        contactQ: 'So we can get back to you, could you share your name and phone number?',
        contactQOther: 'So we can get back to you, could you share your own name and phone number?',
        name: 'Full name',
        nameOther: 'Your full name',
        namePh: 'e.g. Ayşe Yılmaz',
        phone: 'Phone',
        phonePh: '0532 123 45 67',
        phoneHint: '11 digits starting with 0',
        formHint: 'Fill in the form above',
        pickHint: 'Choose an option above',
        nice: 'Nice to meet you, {n}.',
        timeQ: 'When is a good time to call you? You can choose more than one.',
        anyTime: 'Any time',
        noteQ: 'Is there anything you would like to add?',
        notePh: 'Write a note...',
        noNote: 'No, that is all',
        cont: 'Continue',
        sendAria: 'Send',
        nameErr: 'Please enter your first and last name together (e.g. Ayşe Yılmaz).',
        nameChars: 'Your name can only contain letters.',
        nameFake: 'Please enter your real first and last name.',
        phoneFake: 'Please enter a valid phone number.',
        textLink: 'Links cannot be added to the note.',
        textAbuse: 'Please use appropriate language.',
        editAck: 'Of course, let us fix that.',
        summaryAgain: 'Updated. Here is the latest version of your request.',
        edit: 'Edit',
        noNoteVal: 'None',
        phoneStart: 'The number must start with 0.',
        phoneLen: 'The number must have 11 digits (currently {n}).',
        summary: 'Thank you, {n}. Here is your request; you can check it before sending.',
        send: 'Send message',
        sending: 'Sending...',
        sentOk: 'Thank you, {n}. Your request has reached our team; we will get back to you during working hours ({h}).',
        sendFail: 'We could not deliver your request just now. You can send the same message on WhatsApp right away.',
        tooMany: 'Too many attempts. Please try again a little later or send it on WhatsApp.',
        waAlso: 'Also write on WhatsApp',
        waSend: 'Send on WhatsApp',
        again: 'New request',
        privacy: 'Your request is sent to our school by email so that we can reply.',
        privacyLink: 'Privacy notice (KVKK)',
        teaser: 'Hi! How can we help you?',
        teaserSub: 'Live chat · Online',
        teaserClose: 'Dismiss',
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
        times: [['sabah', 'Morning'], ['ogle', 'Afternoon'], ['aksam', 'Evening']]
      }
    : {
        launcher: 'Canlı destek',
        title: 'Uslu Sürücü Kursu',
        online: 'Çevrimiçi',
        hours: 'Haftanın 7 günü açığız',
        hoursLong: 'Pazartesi-Perşembe 09.00-19.30, Cuma-Pazar 09.00-20.30',
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
        contactQ: 'Size dönüş yapabilmemiz için adınızı ve telefon numaranızı paylaşır mısınız?',
        contactQOther: 'Size dönüş yapabilmemiz için kendi adınızı ve telefon numaranızı paylaşır mısınız?',
        name: 'Ad Soyad',
        nameOther: 'Sizin adınız soyadınız',
        namePh: 'Örn. Ayşe Yılmaz',
        phone: 'Telefon',
        phonePh: '0532 123 45 67',
        phoneHint: '0 ile başlayan 11 hane',
        formHint: 'Yukarıdaki formu doldurun',
        pickHint: 'Yukarıdan bir seçenek belirleyin',
        nice: 'Memnun oldum, {n}.',
        timeQ: 'Sizi hangi saatlerde aramamız uygun olur? Birden fazla seçebilirsiniz.',
        anyTime: 'Fark etmez',
        noteQ: 'Eklemek istediğiniz bir not var mı?',
        notePh: 'Notunuzu yazın...',
        noNote: 'Yok, bu kadar',
        cont: 'Devam et',
        sendAria: 'Gönder',
        nameErr: 'Adınızı ve soyadınızı birlikte yazın (örn. Ayşe Yılmaz).',
        nameChars: 'Ad soyad yalnız harf içermeli.',
        nameFake: 'Lütfen gerçek adınızı ve soyadınızı yazın.',
        phoneFake: 'Lütfen geçerli bir telefon numarası yazın.',
        textLink: 'Nota bağlantı eklenemez.',
        textAbuse: 'Lütfen uygun bir dil kullanın.',
        editAck: 'Tabii, hemen düzeltelim.',
        summaryAgain: 'Güncelledim. Talebinizin son hâline göz atabilirsiniz.',
        edit: 'Düzenle',
        noNoteVal: 'Yok',
        phoneStart: 'Numara 0 ile başlamalı.',
        phoneLen: 'Numara 11 haneli olmalı (şu an {n} hane).',
        summary: 'Teşekkürler {n}. Talebiniz hazır, göndermeden önce göz atabilirsiniz.',
        send: 'Mesaj gönder',
        sending: 'Gönderiliyor...',
        sentOk: 'Teşekkürler {n}, talebiniz ekibimize ulaştı. Mesai saatlerimizde ({h}) size dönüş yapacağız.',
        sendFail: 'Talebinizi şu an iletemedik. Aynı mesajı WhatsApp’tan hemen gönderebilirsiniz.',
        tooMany: 'Çok fazla deneme yapıldı. Biraz sonra yeniden deneyin ya da WhatsApp’tan gönderin.',
        waAlso: 'WhatsApp’tan da yazın',
        waSend: 'WhatsApp’tan gönder',
        again: 'Yeni talep',
        privacy: 'Talebiniz, size yanıt verebilmemiz için kursumuza e-postayla iletilir.',
        privacyLink: 'KVKK Aydınlatma Metni',
        teaser: 'Merhaba! Size nasıl yardımcı olabiliriz?',
        teaserSub: 'Canlı destek · Çevrimiçi',
        teaserClose: 'Kapat',
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
        times: [['sabah', 'Sabah'], ['ogle', 'Öğle'], ['aksam', 'Akşam']]
      };

  var A = EN
    ? {
        open: 'Accessibility options',
        title: 'Accessibility',
        hint: 'Saved in this browser',
        reset: 'Reset',
        move: 'Drag to move',
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
        move: 'Sürükleyerek taşıyabilirsiniz',
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
    /* açma düğmesi: sitenin kırmızısı, sohbet balonu, çevrimiçi noktası, okunmamış rozeti */
    '.uc-launch{position:fixed;right:20px;bottom:20px;z-index:9990;width:60px;height:60px;border-radius:50%;border:0;background:' + RED + ';color:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 26px rgb(203 22 67 / 32%);cursor:pointer;transition:transform .2s,background .2s}' +
    '.uc-launch:hover{transform:translateY(-2px);background:' + NAVY + '}.uc-launch:focus-visible{outline:3px solid ' + NAVY + ';outline-offset:3px}' +
    '.uc-launch svg{width:28px;height:28px}' +
    '.uc-launch::after{content:"";position:absolute;right:3px;bottom:5px;width:13px;height:13px;border-radius:50%;background:#22c55e;border:2px solid #fff}' +
    '.uc-launch[aria-expanded="true"]::after{display:none}' +
    '.uc-badge{position:absolute;top:-3px;right:-3px;min-width:21px;height:21px;padding:0 6px;border-radius:11px;background:#fff;color:' + RED + ';font-size:12px;font-weight:800;line-height:21px;text-align:center;box-shadow:0 2px 6px rgb(0 0 0 / 18%)}' +
    '.uc-launch.uc-bump{animation:uc-bump .9s ease-in-out 2}' +
    '@keyframes uc-bump{0%,100%{transform:none}25%{transform:translateY(-6px)}50%{transform:none}75%{transform:translateY(-3px)}}' +
    '.uc-teaser{position:fixed;right:92px;bottom:26px;z-index:9990;display:flex;align-items:flex-start;gap:6px;background:#fff;color:' + NAVY + ';border-radius:16px 16px 4px 16px;padding:11px 8px 11px 14px;box-shadow:0 8px 32px rgb(4 30 55 / 20%);max-width:250px;animation:uc-in .3s ease-out both}' +
    '.uc-teaser[hidden]{display:none}' +
    '.uc-tmsg{background:transparent;border:0;padding:0;text-align:left;cursor:pointer;color:inherit;font:inherit}' +
    '.uc-tmsg b{display:block;font-size:14px;font-weight:700;line-height:1.35}.uc-tmsg small{display:block;font-size:12px;color:#6b7280;margin-top:3px}' +
    '.uc-tx{flex:0 0 22px;width:22px;height:22px;border:0;border-radius:50%;background:transparent;color:#9aa4b2;cursor:pointer;font-size:16px;line-height:1}.uc-tx:hover{background:#f3f5f8;color:' + NAVY + '}' +
    '.uc-teaser button:focus-visible{outline:3px solid ' + RED + ';outline-offset:2px}' +
    '@media (max-width:480px){.uc-teaser{right:86px;max-width:calc(100vw - 110px)}}' +
    '.uc-panel{position:fixed;right:20px;bottom:90px;z-index:9991;width:370px;max-width:calc(100vw - 24px);height:min(620px,calc(100vh - 112px));display:flex;flex-direction:column;background:#fff;color:' + NAVY + ';border-radius:16px;box-shadow:0 12px 48px rgb(4 30 55 / 28%);overflow:hidden}' +
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
    '.uc-log{flex:1 1 auto;overflow-y:auto;padding:16px 14px 12px;background:#f3f5f8;display:flex;flex-direction:column;gap:4px;font-size:14.5px;line-height:1.45;scroll-behavior:smooth}' +
    '.uc-log>*{flex-shrink:0}' +
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
    /* seçenekler: mesajın altında tek parça liste kartı */
    '.uc-card{margin:6px 0 4px 34px;background:#fff;border:1px solid #e3e7ec;border-radius:14px;overflow:hidden;box-shadow:0 1px 3px rgb(4 30 55 / 6%);animation:uc-in .22s ease-out both}' +
    '.uc-panel .uc-choice{display:flex;align-items:center;gap:10px;width:100%;padding:11px 14px;background:#fff;border:0;border-top:1px solid #eef0f3;font-size:14px;font-weight:600;line-height:1.3;color:' + NAVY + ';text-align:left;cursor:pointer;transition:background .15s,color .15s}' +
    '.uc-choice:first-child{border-top:0}' +
    '.uc-choice span{flex:1 1 auto}' +
    '.uc-choice svg{width:8px;height:12px;flex:0 0 8px;color:' + RED + ';transition:transform .15s}' +
    '.uc-choice:hover{background:#f7f8fa;color:' + RED + '}.uc-choice:hover svg{transform:translateX(3px)}' +
    '.uc-choice .uc-box{width:18px;height:18px;flex:0 0 18px;border:1.5px solid #c9ced6;border-radius:5px;display:flex;align-items:center;justify-content:center;color:#fff;transition:all .15s}' +
    '.uc-choice .uc-box svg{width:11px;height:11px;color:#fff;opacity:0}' +
    '.uc-choice[aria-pressed="true"] .uc-box{background:' + RED + ';border-color:' + RED + '}.uc-choice[aria-pressed="true"] .uc-box svg{opacity:1}' +
    '.uc-choice.uc-go{justify-content:center;background:' + NAVY + ';color:#fff;border-top:0}.uc-choice.uc-go span{flex:0 0 auto}.uc-choice.uc-go:hover{background:' + RED + ';color:#fff}' +
    '.uc-choice.uc-go svg{color:#fff}' +
    /* iletişim formu kartı */
    '.uc-form{padding:12px 14px 14px}' +
    '.uc-form label{display:block;font-size:12.5px;font-weight:700;color:' + NAVY + ';margin:8px 0 5px}.uc-form label:first-of-type{margin-top:0}' +
    '.uc-form input{width:100%;border:1px solid #dfe3e8;border-radius:10px;padding:10px 12px;font-size:15px;color:' + NAVY + ';background:#fff}' +
    '.uc-form input:focus{border-color:' + NAVY + ';outline:0;box-shadow:0 0 0 3px rgb(4 30 55 / 8%)}.uc-form input[aria-invalid="true"]{border-color:' + RED + '}' +
    '.uc-fhint{font-size:12px;color:#6b7280;margin-top:5px}.uc-fhint.uc-good{color:#15803d;font-weight:600}.uc-fhint.uc-bad{color:' + RED + ';font-weight:600}' +
    '.uc-ferr{font-size:12px;color:' + RED + ';font-weight:600;margin-top:5px}.uc-ferr:empty{display:none}' +
    '.uc-fgo{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;margin-top:12px;border:0;border-radius:10px;padding:11px 14px;background:' + NAVY + ';color:#fff;font-size:14.5px;font-weight:700;cursor:pointer;transition:background .2s}' +
    '.uc-fgo:hover{background:' + RED + '}.uc-fgo svg{width:16px;height:16px}' +
    /* özet kartı: satır satır */
    '.uc-sum .uc-sr{display:flex;gap:10px;padding:8px 14px;border-top:1px solid #eef0f3;font-size:13px;line-height:1.4}.uc-sum .uc-sr:first-child{border-top:0}' +
    '.uc-sum .uc-sr{align-items:center}.uc-sum .uc-sr span{flex:0 0 104px;color:#6b7280}.uc-sum .uc-sr b{flex:1 1 auto;font-weight:600;color:' + NAVY + ';word-break:break-word}' +
    '.uc-edit{flex:0 0 30px;width:30px;height:30px;margin:-4px -6px -4px 0;border:0;border-radius:50%;background:transparent;color:#9aa4b2;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .15s}' +
    '.uc-edit:hover{color:' + RED + ';background:#fff1f3}.uc-edit svg{width:15px;height:15px}' +
    '.uc-dock{flex:0 0 auto;border-top:1px solid #e6e9ee;background:#fff;padding:10px 12px 12px}' +
    '.uc-hint{font-size:12px;color:#6b7280;margin:0 4px 6px;min-height:16px}.uc-hint.uc-bad{color:' + RED + ';font-weight:600}.uc-hint.uc-good{color:#15803d;font-weight:600}' +
    '.uc-comp{display:flex;align-items:center;gap:8px}' +
    '.uc-comp input{flex:1 1 auto;min-width:0;border:1px solid #dfe3e8;border-radius:22px;padding:10px 15px;font-size:15px;color:' + NAVY + ';background:#fff}' +
    '.uc-comp input:focus{border-color:' + NAVY + ';outline:0}.uc-comp input[aria-invalid="true"]{border-color:' + RED + '}' +
    '.uc-comp input:disabled{background:#f5f6f8;border-color:#eceef1}' +
    '.uc-sendb{width:42px;height:42px;flex:0 0 42px;border-radius:50%;border:0;background:' + RED + ';color:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:background .2s}' +
    '.uc-sendb:hover{background:' + NAVY + '}.uc-sendb:disabled{background:#d6dae0;cursor:default}.uc-sendb svg{width:18px;height:18px}' +
    '.uc-panel button:focus-visible,.uc-panel input:focus-visible,.uc-panel a:focus-visible{outline:3px solid ' + RED + ';outline-offset:2px}' +
    '.uc-main{display:flex;align-items:center;justify-content:space-between;width:100%;border:0;border-radius:28px;padding:7px 8px 7px 18px;background:' + RED + ';color:#fff;font-weight:600;font-size:15px;text-transform:uppercase;cursor:pointer;box-shadow:0 3px 24px rgb(0 0 0 / 10%);transition:background .4s;text-decoration:none}' +
    '.uc-main:hover{background:' + NAVY + ';color:#fff}.uc-main[disabled]{opacity:.75;cursor:wait}' +
    '.uc-main .uc-ic{display:flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:50%;background:#fff;color:' + RED + ';margin-left:12px;flex:0 0 36px}' +
    '.uc-main .uc-ic svg{width:18px;height:18px}' +
    '.uc-main.uc-wa{background:#25d366}.uc-main.uc-wa .uc-ic{color:#25d366}.uc-main.uc-wa:hover{background:#1da851}' +
    '.uc-alt{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;margin-top:8px;border:1.5px solid #25d366;border-radius:28px;padding:9px 14px;background:#fff;color:#128c4a;font-weight:700;font-size:14px;cursor:pointer;text-decoration:none}' +
    '.uc-alt:hover{background:#f0fdf4;color:#128c4a}.uc-alt svg{width:18px;height:18px}' +
    '.uc-link{display:block;margin:10px auto 0;background:transparent;border:0;color:#6b7280;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.03em;cursor:pointer}.uc-link:hover{color:' + RED + '}' +
    '.uc-note{font-size:11.5px;color:#6b7280;margin-top:8px;line-height:1.45;text-align:center}.uc-note a{color:' + NAVY + ';text-decoration:underline}' +
    '.uc-hp{position:absolute!important;left:-9999px!important;width:1px;height:1px;overflow:hidden}' +
    '@media (max-width:480px){.uc-panel{right:10px;left:10px;width:auto;bottom:84px;height:calc(100vh - 100px);height:calc(100dvh - 100px)}}' +
    '@media (prefers-reduced-motion:reduce){.uc-row,.uc-card{animation:none}.uc-dots i{animation:none}.uc-log{scroll-behavior:auto}}' +
    /* erişilebilirlik: aynı dil, küçük ve köşeli */
    '.ua-tab{position:fixed;left:0;top:50%;transform:translateY(-50%);z-index:9989;width:34px;height:42px;border:0;border-radius:0 4px 4px 0;background:' + NAVY + ';color:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer;box-shadow:0 3px 24px rgb(0 0 0 / 15%);opacity:.8;border-right:3px solid ' + RED + ';transition:opacity .2s,width .2s}' +
    '.ua-tab:hover,.ua-tab:focus-visible,.ua-tab[aria-expanded="true"]{opacity:1;width:38px}.ua-tab:focus-visible{outline:3px solid ' + RED + ';outline-offset:2px}' +
    '.ua-tab svg{width:20px;height:20px;pointer-events:none}.ua-tab{touch-action:none}.ua-tab.ua-drag{opacity:1;cursor:grabbing;transition:none}' +
    '.ua-tab.ua-right{left:auto;right:0;border-radius:4px 0 0 4px;border-right:0;border-left:3px solid ' + RED + '}.ua-panel.ua-right{left:auto;right:46px}' +
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
    '@media (prefers-reduced-motion:reduce){.uc-launch,.ua-tab{transition:none}.uc-launch.uc-bump,.uc-teaser{animation:none}}';

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

  var ICON_CHAT =
    '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3h11A2.5 2.5 0 0 1 20 5.5v8a2.5 2.5 0 0 1-2.5 2.5H10l-4.2 3.6c-.5.4-1.3.1-1.3-.6V16A2.5 2.5 0 0 1 4 13.5z" fill="currentColor"/><circle cx="8.5" cy="9.5" r="1.2" fill="' + RED + '"/><circle cx="12" cy="9.5" r="1.2" fill="' + RED + '"/><circle cx="15.5" cy="9.5" r="1.2" fill="' + RED + '"/></svg>';
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
  // müşteri hizmetleri gibi"): asistan baloncukla yazar, önce "yazıyor" görünür.
  // Seçenekler mesajın altında liste kartı; ad soyad ve telefon tek form kartında.
  // Akış: nasıl yardımcı olabiliriz → eğitim → kimin için → ad soyad + telefon →
  // arama zamanı → not → özet → "Mesaj gönder" (Resend ile kursun e-postasına, /api/iletisim/).
  // E-posta gidemezse aynı talep WhatsApp'tan gönderilebilir.
  function buildChat() {
    // Ad/telefon/metin kuralları sunucuyla ORTAK: assets/js/uslu-rules.js (önce yüklenir).
    var R = window.UsluRules;
    if (!R) return;
    var AVATAR = '/assets/img/course/logo-avatar.webp';
    var API = '/api/iletisim/';
    var REDUCED = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    // quiet: kendiliğinden açıldıysa ziyaretçi panele dokunana dek odak sayfada kalır.
    var state, gen = 0, lastSide = null, lastOpener = null, quiet = false;

    function reset() {
      state = { topic: null, course: null, who: null, name: '', phone: '', times: [], note: '', startedAt: Date.now() };
    }
    reset();

    var launch = el('button', { type: 'button', class: 'uc-launch', 'aria-label': T.launcher, 'aria-expanded': 'false', 'aria-controls': 'uc-panel', 'data-uslu-widget': '' });
    launch.innerHTML = ICON_CHAT;
    var badge = el('span', { class: 'uc-badge', 'aria-hidden': 'true' }, '1');
    badge.hidden = true;
    launch.appendChild(badge);

    var panel = el('div', { id: 'uc-panel', class: 'uc-panel', role: 'dialog', 'aria-label': T.title, 'data-uslu-widget': '' });
    panel.hidden = true;
    var head = el('div', { class: 'uc-head' });
    var ava = el('span', { class: 'uc-ava', 'aria-hidden': 'true' });
    ava.appendChild(el('img', { src: AVATAR, alt: '', width: '34', height: '34' }));
    var headText = el('div');
    headText.appendChild(el('b', null, T.title));
    headText.appendChild(el('small', null, T.online + ' · ' + T.hours));
    var againBtn = el('button', { type: 'button', class: 'uc-hbtn uc-hgap', 'aria-label': T.restart, title: T.restart });
    againBtn.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12a8 8 0 1 0 2.3-5.7M4 4v4h4" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    var x = el('button', { type: 'button', class: 'uc-hbtn', 'aria-label': T.close, title: T.close });
    x.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>';
    head.appendChild(ava);
    head.appendChild(headText);
    head.appendChild(againBtn);
    head.appendChild(x);
    var log = el('div', { class: 'uc-log', role: 'log', 'aria-live': 'polite' });
    var dock = el('div', { class: 'uc-dock' });
    panel.appendChild(head);
    panel.appendChild(log);
    panel.appendChild(dock);

    // Karşılama baloncuğu: mesaj + kapatma. Dokununca sohbet açılır.
    var teaser = el('div', { class: 'uc-teaser', role: 'status', 'data-uslu-widget': '' });
    var tmsg = el('button', { type: 'button', class: 'uc-tmsg' });
    tmsg.appendChild(el('b', null, T.teaser));
    tmsg.appendChild(el('small', null, T.teaserSub));
    var tx = el('button', { type: 'button', class: 'uc-tx', 'aria-label': T.teaserClose }, '×');
    teaser.appendChild(tmsg);
    teaser.appendChild(tx);
    teaser.hidden = true;

    var TICK = '<svg class="uc-tick" viewBox="0 0 16 10" aria-hidden="true" focusable="false"><path d="M1 5.5l3 3L10 2M6.5 8.5L13 2" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    var PLANE = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12l16-8-6 16-2.5-6.5z" stroke="currentColor" stroke-width="2" fill="none" stroke-linejoin="round"/></svg>';
    var CARET = '<svg viewBox="0 0 8 12" aria-hidden="true" focusable="false"><path d="M1.5 1l5 5-5 5" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    var CHECK = '<svg viewBox="0 0 12 12" aria-hidden="true" focusable="false"><path d="M2 6.5l2.5 2.5L10 3" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    var ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>';

    function label(list, key) {
      for (var i = 0; i < list.length; i++) if (list[i][0] === key) return list[i][1];
      return T.none;
    }
    function fill(s, map) {
      return s.replace(/\{(\w)\}/g, function (m, k) { return map[k] != null ? map[k] : m; });
    }
    function firstName() { return state.name.split(' ')[0]; }
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

    // Alt kutu: seçenek ve form adımlarında kapalı, yalnız not adımında açık.
    function idleDock(hint) {
      dock.textContent = '';
      var c = el('div', { class: 'uc-comp' });
      var inp = el('input', { type: 'text', placeholder: hint || T.pickHint, disabled: '', 'aria-label': hint || T.pickHint });
      var sb = el('button', { type: 'button', class: 'uc-sendb', disabled: '', 'aria-label': T.sendAria });
      sb.innerHTML = PLANE;
      c.appendChild(inp);
      c.appendChild(sb);
      dock.appendChild(c);
    }

    function card(extra) {
      var c = el('div', { class: 'uc-card' + (extra ? ' ' + extra : '') });
      log.appendChild(c);
      return c;
    }

    // Tek seçim: liste kartı, seçilen satır ziyaretçinin baloncuğu olur.
    function choices(list, onPick) {
      idleDock();
      var c = card();
      list.forEach(function (item) {
        var b = el('button', { type: 'button', class: 'uc-choice' });
        b.appendChild(el('span', null, item[1]));
        b.insertAdjacentHTML('beforeend', CARET);
        b.addEventListener('click', function () {
          c.remove();
          bubble('me', item[1]);
          onPick(item[0]);
        });
        c.appendChild(b);
      });
      scrollDown();
      focusIn(c.querySelector('button'));
    }

    // Çoklu seçim: işaret kutulu satırlar + altta "Fark etmez / Devam et".
    function multi(list, onDone, initial) {
      idleDock();
      var c = card();
      var picked = (initial || []).slice();
      var go;
      list.forEach(function (item) {
        var b = el('button', { type: 'button', class: 'uc-choice', 'aria-pressed': picked.indexOf(item[0]) >= 0 ? 'true' : 'false' });
        var box = el('span', { class: 'uc-box', 'aria-hidden': 'true' });
        box.innerHTML = CHECK;
        b.appendChild(box);
        b.appendChild(el('span', null, item[1]));
        b.addEventListener('click', function () {
          var i = picked.indexOf(item[0]);
          if (i >= 0) picked.splice(i, 1); else picked.push(item[0]);
          b.setAttribute('aria-pressed', i >= 0 ? 'false' : 'true');
          go.firstChild.textContent = picked.length ? T.cont : T.anyTime;
        });
        c.appendChild(b);
      });
      go = el('button', { type: 'button', class: 'uc-choice uc-go' });
      go.appendChild(el('span', null, picked.length ? T.cont : T.anyTime));
      go.insertAdjacentHTML('beforeend', CARET);
      go.addEventListener('click', function () {
        var chosen = list.filter(function (item) { return picked.indexOf(item[0]) >= 0; });
        c.remove();
        bubble('me', chosen.length ? chosen.map(function (x) { return x[1]; }).join(', ') : T.anyTime);
        onDone(chosen.map(function (x) { return x[0]; }));
      });
      c.appendChild(go);
      scrollDown();
      focusIn(c.querySelector('button'));
    }

    // Kural kodlarını ekrandaki metne çevir (kurallar: uslu-rules.js).
    var phoneDigits = R.phoneDigits, phoneFormat = R.phoneFormat;
    function titleCase(v) { return R.titleCase(v, EN); }
    function nameProblem(v) {
      var c = R.nameProblem(v);
      if (!c) return null;
      return c === 'name_chars' ? T.nameChars : c === 'name_format' ? T.nameErr : T.nameFake;
    }
    function phoneProblem(d) {
      var c = R.phoneProblem(d);
      if (!c) return null;
      return c === 'phone_start' ? T.phoneStart : c === 'phone_len' ? T.phoneLen.replace('{n}', String(d.length)) : T.phoneFake;
    }
    function textProblem(v) {
      var c = R.textProblem(v);
      return !c ? null : c === 'text_link' ? T.textLink : T.textAbuse;
    }

    // Ad soyad + telefon tek kartta (Ahmet: "iletişim ve ad soyad birlikte istensin").
    function contactForm(onOk) {
      idleDock(T.formHint);
      var c = card('uc-form-card');
      var f = el('form', { class: 'uc-form', novalidate: '' });
      var hp = el('input', { type: 'text', name: 'website', tabindex: '-1', autocomplete: 'off', 'aria-hidden': 'true', class: 'uc-hp' });
      f.appendChild(hp);
      f.appendChild(el('label', { for: 'uc-name' }, state.who && state.who !== 'kendim' ? T.nameOther : T.name));
      var nm = el('input', { id: 'uc-name', type: 'text', autocomplete: 'name', maxlength: '80', placeholder: T.namePh, 'aria-describedby': 'uc-name-err' });
      nm.value = state.name;
      f.appendChild(nm);
      var nErr = el('div', { class: 'uc-ferr', id: 'uc-name-err', role: 'alert' });
      f.appendChild(nErr);
      f.appendChild(el('label', { for: 'uc-phone' }, T.phone));
      var ph = el('input', { id: 'uc-phone', type: 'tel', inputmode: 'numeric', autocomplete: 'tel-national', maxlength: '14', placeholder: T.phonePh, 'aria-describedby': 'uc-phone-hint' });
      ph.value = state.phone;
      f.appendChild(ph);
      var hint = el('div', { class: 'uc-fhint', id: 'uc-phone-hint', role: 'status' });
      f.appendChild(hint);
      function paint() {
        var d = phoneDigits(ph.value);
        ph.value = phoneFormat(d);
        var bad = d.length > 0 && d.charAt(0) !== '0';
        hint.textContent = bad ? T.phoneStart : T.phoneHint + ' · ' + d.length + '/11';
        hint.className = 'uc-fhint' + (bad ? ' uc-bad' : d.length === 11 ? ' uc-good' : '');
        ph.removeAttribute('aria-invalid');
      }
      ph.addEventListener('input', paint);
      nm.addEventListener('input', function () { nErr.textContent = ''; nm.removeAttribute('aria-invalid'); });
      paint();
      var go = el('button', { type: 'submit', class: 'uc-fgo' });
      go.appendChild(el('span', null, T.cont));
      go.insertAdjacentHTML('beforeend', ARROW);
      f.appendChild(go);
      f.addEventListener('submit', function (ev) {
        ev.preventDefault();
        if (hp.value) return; // bot
        var name = nm.value.replace(/\s+/g, ' ').trim();
        var np = nameProblem(name);
        var d = phoneDigits(ph.value);
        var pp = phoneProblem(d);
        nErr.textContent = np || '';
        if (np) nm.setAttribute('aria-invalid', 'true');
        if (pp) {
          hint.textContent = pp;
          hint.className = 'uc-fhint uc-bad';
          ph.setAttribute('aria-invalid', 'true');
        }
        if (np) { nm.focus(); return; }
        if (pp) { ph.focus(); return; }
        state.name = titleCase(name);
        state.phone = phoneFormat(d);
        c.remove();
        bubble('me', state.name + '\n' + state.phone);
        onOk();
      });
      c.appendChild(f);
      scrollDown();
      focusIn(nm);
    }

    // Not: alttaki yazma kutusu açılır; "Yok, bu kadar" kartı atlar.
    function askNote(onOk, initial) {
      dock.textContent = '';
      var hint = el('div', { class: 'uc-hint', id: 'uc-note-hint', role: 'alert' });
      dock.appendChild(hint);
      var f = el('form', { class: 'uc-comp', novalidate: '' });
      var inp = el('input', { id: 'uc-note', type: 'text', placeholder: T.notePh, maxlength: '300', autocomplete: 'off', 'aria-label': T.notePh, 'aria-describedby': 'uc-note-hint' });
      inp.value = initial || '';
      inp.addEventListener('input', function () { hint.textContent = ''; hint.className = 'uc-hint'; inp.removeAttribute('aria-invalid'); });
      var sb = el('button', { type: 'submit', class: 'uc-sendb', 'aria-label': T.sendAria });
      sb.innerHTML = PLANE;
      f.appendChild(inp);
      f.appendChild(sb);
      dock.appendChild(f);
      var c = card();
      var skip = el('button', { type: 'button', class: 'uc-choice' });
      skip.appendChild(el('span', null, T.noNote));
      skip.insertAdjacentHTML('beforeend', CARET);
      c.appendChild(skip);
      function done(v) {
        c.remove();
        idleDock();
        bubble('me', v || T.noNote);
        onOk(v);
      }
      skip.addEventListener('click', function () { done(''); });
      f.addEventListener('submit', function (ev) {
        ev.preventDefault();
        var v = inp.value.replace(/\s+/g, ' ').trim().slice(0, 300);
        if (!v) return;
        var problem = textProblem(v);
        if (problem) {
          hint.textContent = problem;
          hint.className = 'uc-hint uc-bad';
          inp.setAttribute('aria-invalid', 'true');
          inp.focus();
          return;
        }
        done(v);
      });
      scrollDown();
      focusIn(inp);
    }

    // WhatsApp yedeği: satırlar "•" ile ayrılır ki WhatsApp'ın önizleme sayfası satır
    // sonlarını yutsa da okunaklı kalsın (Ahmet: "alt alta okunaklı olsun").
    function waText() {
      var lines = [
        T.intro,
        '',
        '• ' + T.request + ': ' + label(T.topics, state.topic),
        '• ' + T.course + ': ' + label(T.courses, state.course),
        '• ' + T.lWho + ': ' + label(T.who, state.who),
        '• ' + T.lName + ': ' + state.name,
        '• ' + T.lPhone + ': ' + state.phone
      ];
      if (state.times.length) lines.push('• ' + T.lTime + ': ' + state.times.map(function (k) { return label(T.times, k); }).join(', '));
      if (state.note) lines.push('• ' + T.lNote + ': ' + state.note);
      return lines.join('\n');
    }
    function waUrl() {
      return 'https://wa.me/' + PHONE + '?text=' + encodeURIComponent(waText());
    }
    function waButton(cls, text) {
      var a = el('a', { class: cls, href: waUrl(), target: '_blank', rel: 'noopener noreferrer' });
      if (cls.indexOf('uc-main') >= 0) {
        a.appendChild(el('span', null, text));
        var ic = el('span', { class: 'uc-ic', 'aria-hidden': 'true' });
        ic.innerHTML = ICON_WA;
        a.appendChild(ic);
      } else {
        a.innerHTML = ICON_WA;
        a.appendChild(el('span', null, text));
      }
      return a;
    }
    function restartLink() {
      var b = el('button', { type: 'button', class: 'uc-link' }, T.again);
      b.addEventListener('click', function () { restart(); });
      return b;
    }

    // Sabah 05.00-10.59, gün 11.00-17.59, akşam ve gece 18.00-04.59. Gece yarısından sonrası da
    // akşam selamıdır; 02.22'de "Günaydın" deniyordu (Ahmet 30.09).
    function greeting() {
      var h = new Date().getHours();
      return fill(T.welcome, { g: T.greet[h >= 5 && h < 11 ? 0 : h >= 11 && h < 18 ? 1 : 2] });
    }

    /* ---- akış ---- */
    function stepTopic() {
      say([greeting(), T.helpQ], function () {
        choices(T.topics, function (k) { state.topic = k; stepCourse(); });
      });
    }
    function stepCourse() {
      say([T.ack[state.topic], T.courseQ], function () {
        choices(T.courses, function (k) { state.course = k; stepWho(); });
      });
    }
    function stepWho(pre) {
      say((pre || []).concat(T.whoQ), function () {
        choices(T.who, function (k) { state.who = k; stepContact(); });
      });
    }
    function stepContact() {
      var self = state.who === 'kendim';
      say([self ? T.whoAckSelf : T.whoAckOther, self ? T.contactQ : T.contactQOther], function () {
        contactForm(stepTime);
      });
    }
    function stepTime() {
      say([fill(T.nice, { n: firstName() }), T.timeQ], function () {
        multi(T.times, function (keys) { state.times = keys; stepNote(); });
      });
    }
    function stepNote() {
      say([T.noteQ], function () {
        askNote(function (v) { state.note = v; stepSummary(); });
      });
    }
    // Özet: her satırın yanında "düzenle"; o adım yeniden sorulur, sonra özete dönülür
    // (Ahmet: "mesajda düzenleme imkanı yok").
    var PENCIL = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 20h4L19 9l-4-4L4 16v4zM14 6l4 4" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    function stepSummary(again) {
      say([again ? T.summaryAgain : fill(T.summary, { n: firstName() })], function () {
        var c = card('uc-sum');
        var rows = [
          ['topic', T.request, label(T.topics, state.topic)],
          ['course', T.course, label(T.courses, state.course)],
          ['who', T.lWho, label(T.who, state.who)],
          ['contact', T.lName, state.name],
          ['contact', T.lPhone, state.phone],
          ['times', T.lTime, state.times.length ? state.times.map(function (k) { return label(T.times, k); }).join(', ') : T.anyTime],
          ['note', T.lNote, state.note || T.noNoteVal]
        ];
        rows.forEach(function (r) {
          var d = el('div', { class: 'uc-sr' });
          d.appendChild(el('span', null, r[1]));
          d.appendChild(el('b', null, r[2]));
          var e = el('button', { type: 'button', class: 'uc-edit', 'aria-label': T.edit + ': ' + r[1], title: T.edit });
          e.innerHTML = PENCIL;
          e.addEventListener('click', function () { editField(r[0], c); });
          d.appendChild(e);
          c.appendChild(d);
        });
        scrollDown();
        dock.textContent = '';
        var send = el('button', { type: 'button', class: 'uc-main' });
        var st = el('span', null, T.send);
        var ic = el('span', { class: 'uc-ic', 'aria-hidden': 'true' });
        ic.innerHTML = PLANE;
        send.appendChild(st);
        send.appendChild(ic);
        send.addEventListener('click', function () { submit(send, st); });
        dock.appendChild(send);
        var note = el('div', { class: 'uc-note' });
        note.appendChild(document.createTextNode(T.privacy + ' '));
        note.appendChild(el('a', { href: '/kvkk/', target: '_blank', rel: 'noopener' }, T.privacyLink));
        dock.appendChild(note);
        scrollDown();
        focusIn(send);
      });
    }

    function editField(field, sumCard) {
      if (busy) return;
      if (sumCard) sumCard.remove();
      idleDock();
      var back = function () { stepSummary(true); };
      var ask = function (q, then) { say([T.editAck, q], then); };
      if (field === 'topic') ask(T.helpQ, function () { choices(T.topics, function (k) { state.topic = k; back(); }); });
      else if (field === 'course') ask(T.courseQ, function () { choices(T.courses, function (k) { state.course = k; back(); }); });
      else if (field === 'who') ask(T.whoQ, function () { choices(T.who, function (k) { state.who = k; back(); }); });
      else if (field === 'contact') ask(state.who === 'kendim' ? T.contactQ : T.contactQOther, function () { contactForm(back); });
      else if (field === 'times') ask(T.timeQ, function () { multi(T.times, function (keys) { state.times = keys; back(); }, state.times); });
      else ask(T.noteQ, function () { askNote(function (v) { state.note = v; back(); }, state.note); });
    }

    // Gönderim: sunucu doğrular, Resend ile kursun e-postasına iletir.
    var busy = false;
    function submit(btn, labelNode) {
      if (busy) return;
      busy = true;
      btn.disabled = true;
      labelNode.textContent = T.sending;
      var g = gen;
      var payload = {
        source: 'asistan',
        lang: EN ? 'en' : 'tr',
        website: '',
        t: Date.now() - state.startedAt,
        name: state.name,
        phone: phoneDigits(state.phone),
        topic: state.topic,
        course: state.course,
        who: state.who,
        times: state.times,
        note: state.note,
        kvkk: true
      };
      fetch(API, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
        credentials: 'same-origin'
      })
        .then(function (r) { return r.json().catch(function () { return { ok: false }; }); })
        .catch(function () { return { ok: false }; })
        .then(function (data) {
          busy = false;
          if (g !== gen) return;
          dock.textContent = '';
          if (data && data.ok) {
            // Gönderilen talep artık düzenlenmez (yeniden gönderimi önler); yeni talep baştan başlar.
            Array.prototype.forEach.call(log.querySelectorAll('.uc-edit'), function (b) { b.remove(); });
            say([fill(T.sentOk, { n: firstName(), h: T.hoursLong })], function () {
              dock.textContent = '';
              dock.appendChild(waButton('uc-alt', T.waAlso));
              dock.appendChild(restartLink());
              scrollDown();
            });
          } else if (data && (data.error === 'name' || data.error === 'phone' || data.error === 'note')) {
            editField(data.error === 'note' ? 'note' : 'contact', log.querySelector('.uc-sum'));
          } else {
            say([data && data.error === 'rate' ? T.tooMany : T.sendFail], function () {
              dock.textContent = '';
              dock.appendChild(waButton('uc-main uc-wa', T.waSend));
              dock.appendChild(restartLink());
              scrollDown();
              focusIn(dock.querySelector('a'));
            });
          }
        });
    }

    function restart(course) {
      gen++;
      busy = false;
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
      badge.hidden = true;
      store.set('uc-seen', '1', true);
      quiet = !!(opts && opts.auto);
      if (!quiet) lastOpener = document.activeElement;
      panel.hidden = false;
      launch.setAttribute('aria-expanded', 'true');
      if (opts && opts.course) { started = true; restart(opts.course); }
      else if (!started) { started = true; restart(); }
      else {
        var f = log.querySelector('.uc-card button, .uc-card input') || dock.querySelector('input:not([disabled]), button, a');
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
    againBtn.addEventListener('click', function () { restart(); });
    tmsg.addEventListener('click', function () { open(); });
    tx.addEventListener('click', function () {
      teaser.hidden = true;
      badge.hidden = true;
      store.set('uc-seen', '1', true); // kapatan ziyaretçiye bu oturumda panel kendiliğinden açılmaz
    });
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

    // Oturumda bir kez: 8. saniyede karşılama baloncuğu ve "1" rozeti; 30. saniyede
    // masaüstünde panel kendiliğinden açılır (Ahmet: "30 sn sonra otomatik açılsa").
    // Telefonda panel ekranı kaplayacağı için yalnız baloncuk kalır (Google da mobilde
    // içeriği örten açılır pencereyi sıralamada cezalandırıyor).
    if (!store.get('uc-seen', true)) {
      window.setTimeout(function () {
        if (store.get('uc-seen', true) || !panel.hidden) return;
        teaser.hidden = false;
        badge.hidden = false;
        launch.classList.add('uc-bump');
      }, 8000);
      window.setTimeout(function () {
        if (store.get('uc-seen', true) || !panel.hidden) return;
        if (window.matchMedia && window.matchMedia('(min-width: 768px)').matches) open({ auto: true });
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
    /* Taşınabilir düğme: kenar boyunca yukarı/aşağı, bırakıldığı yarıya göre sol ya da sağ
       kenara yapışır; konum bu tarayıcıda saklanır. Sürükleme bitince gelen tıklama yutulur.
       Klavye: odaktayken Alt + ok tuşları. */
    var POS = 'ua-pos';
    var pos = null;
    try { pos = JSON.parse(store.get(POS) || 'null'); } catch (e) { pos = null; }
    tab.title = A.move;
    function place() {
      var right = !!(pos && pos.side === 'right');
      tab.classList.toggle('ua-right', right);
      panel.classList.toggle('ua-right', right);
      if (!pos || typeof pos.y !== 'number') { tab.style.top = ''; tab.style.transform = ''; return; }
      var h = tab.offsetHeight || 42;
      var y = Math.min(Math.max(pos.y * window.innerHeight, 8), window.innerHeight - h - 8);
      tab.style.top = y + 'px';
      tab.style.transform = 'none';
    }
    function save() { store.set(POS, JSON.stringify(pos)); }
    var drag = null, swallow = false;
    tab.addEventListener('pointerdown', function (e) {
      if (e.button !== 0) return;
      var r = tab.getBoundingClientRect();
      drag = { x: e.clientX, y: e.clientY, top: r.top, moved: false, id: e.pointerId };
      e.preventDefault();
    });
    window.addEventListener('pointermove', function (e) {
      if (!drag || e.pointerId !== drag.id) return;
      var dy = e.clientY - drag.y, dx = e.clientX - drag.x;
      if (!drag.moved && Math.abs(dy) < 6 && Math.abs(dx) < 6) return;
      if (!drag.moved) { drag.moved = true; tab.classList.add('ua-drag'); }
      var h = tab.offsetHeight || 42;
      var y = Math.min(Math.max(drag.top + dy, 8), window.innerHeight - h - 8);
      tab.style.top = y + 'px';
      tab.style.transform = 'none';
      e.preventDefault();
    });
    function endDrag(e) {
      if (!drag) return;
      if (drag.moved) {
        pos = { side: e.clientX > window.innerWidth / 2 ? 'right' : 'left', y: parseFloat(tab.style.top) / window.innerHeight };
        save();
        place();
        swallow = true;
      }
      tab.classList.remove('ua-drag');
      drag = null;
    }
    window.addEventListener('pointerup', endDrag);
    window.addEventListener('pointercancel', endDrag);
    tab.addEventListener('keydown', function (e) {
      if (!e.altKey || ['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].indexOf(e.key) < 0) return;
      e.preventDefault();
      var r = tab.getBoundingClientRect();
      pos = pos || { side: 'left' };
      if (e.key === 'ArrowLeft') pos.side = 'left';
      if (e.key === 'ArrowRight') pos.side = 'right';
      var y = r.top + (e.key === 'ArrowUp' ? -40 : e.key === 'ArrowDown' ? 40 : 0);
      pos.y = Math.min(Math.max(y, 8), window.innerHeight - r.height - 8) / window.innerHeight;
      save();
      place();
    });
    window.addEventListener('resize', place);
    window.addEventListener('pointerdown', function () { swallow = false; }, true);
    document.addEventListener('click', function (e) {
      if (swallow) { e.preventDefault(); e.stopPropagation(); swallow = false; }
    }, true);
    tab.addEventListener('click', function (e) {
      panel.hidden ? open() : close();
    });
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
    place();
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
