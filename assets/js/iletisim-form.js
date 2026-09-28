/*
 * İletişim formu: alanları anında denetler, /api/iletisim'e JSON gönderir.
 * JavaScript kapalıysa form yine çalışır (sunucu sonucu ?form=... ile geri döner).
 * Kurallar sunucudakiyle aynı; asıl denetim sunucuda (api/iletisim.js).
 */
(function () {
  'use strict';
  var form = document.getElementById('iletisim-formu');
  if (!form) return;
  var EN = (document.documentElement.lang || '').toLowerCase().indexOf('en') === 0;
  var M = EN
    ? {
        name: 'Please enter your first and last name (e.g. Ayşe Yılmaz).',
        nameChars: 'Your name can only contain letters.',
        phoneStart: 'The number must start with 0.',
        phoneLen: 'The number must have 11 digits (currently {n}).',
        phoneHint: '11 digits starting with 0',
        email: 'Please check your email address.',
        topic: 'Please choose a subject.',
        message: 'Please write your message (at least 10 characters).',
        kvkk: 'Please confirm that you have read the privacy notice.',
        sending: 'Sending...',
        ok: 'Thank you, your message has reached us. We will get back to you as soon as possible.',
        fast: 'That was very fast. Please wait a few seconds and try again.',
        rate: 'Too many attempts. Please try again a little later or call us.',
        fail: 'Your message could not be sent. Please try again or call us on +90 532 068 56 47.'
      }
    : {
        name: 'Adınızı ve soyadınızı birlikte yazın (örn. Ayşe Yılmaz).',
        nameChars: 'Ad soyad yalnız harf içermeli.',
        phoneStart: 'Numara 0 ile başlamalı.',
        phoneLen: 'Numara 11 haneli olmalı (şu an {n} hane).',
        phoneHint: '0 ile başlayan 11 hane',
        email: 'E-posta adresinizi kontrol edin.',
        topic: 'Bir konu seçin.',
        message: 'Mesajınızı yazın (en az 10 karakter).',
        kvkk: 'Aydınlatma metnini okuduğunuzu onaylayın.',
        sending: 'Gönderiliyor...',
        ok: 'Teşekkürler, mesajınız bize ulaştı. En kısa sürede size dönüş yapacağız.',
        fast: 'Çok hızlı gönderildi. Birkaç saniye bekleyip yeniden deneyin.',
        rate: 'Çok fazla deneme yapıldı. Biraz sonra yeniden deneyin ya da bizi arayın.',
        fail: 'Mesajınız gönderilemedi. Yeniden deneyin ya da 0532 068 56 47 numarasından bizi arayın.'
      };

  var started = Date.now();
  var $ = function (id) { return document.getElementById(id); };
  var name = $('cf-name'), phone = $('cf-phone'), email = $('cf-email'), topic = $('cf-topic'),
      message = $('cf-message'), kvkk = $('cf-kvkk'), hp = $('cf-website'), hint = $('cf-phone-hint'),
      status = $('cf-status'), button = form.querySelector('.cf-send');

  var NAME_OK = /^[\p{L}'’.\-]{2,}(?: [\p{L}'’.\-]{2,})+$/u;
  var EMAIL_OK = /^[^\s@<>()",;:]+@[^\s@<>()",;:]+\.[^\s@<>()",;:]{2,}$/;

  function digits(v) {
    var d = String(v || '').replace(/\D/g, '');
    if (d.indexOf('90') === 0 && d.length > 11) d = '0' + d.slice(2);
    return d.slice(0, 11);
  }
  function fmt(d) {
    return [d.slice(0, 4), d.slice(4, 7), d.slice(7, 9), d.slice(9, 11)].filter(Boolean).join(' ');
  }
  function squash(v) { return v.replace(/\s+/g, ' ').trim(); }

  var checks = {
    name: function () {
      var v = squash(name.value);
      if (/[\d_@#$%^&*()+=<>?!/\\|{}\[\]]/.test(v)) return M.nameChars;
      return NAME_OK.test(v) ? '' : M.name;
    },
    phone: function () {
      var d = digits(phone.value);
      if (d.charAt(0) && d.charAt(0) !== '0') return M.phoneStart;
      return d.length === 11 ? '' : M.phoneLen.replace('{n}', String(d.length));
    },
    email: function () {
      var v = email.value.trim();
      return !v || EMAIL_OK.test(v) ? '' : M.email;
    },
    topic: function () { return topic.value ? '' : M.topic; },
    message: function () { return message.value.trim().length >= 10 ? '' : M.message; },
    kvkk: function () { return kvkk.checked ? '' : M.kvkk; }
  };
  var fields = { name: name, phone: phone, email: email, topic: topic, message: message, kvkk: kvkk };

  function show(key, text) {
    var err = $('cf-' + key + '-err');
    if (err) err.textContent = text;
    if (text) fields[key].setAttribute('aria-invalid', 'true');
    else fields[key].removeAttribute('aria-invalid');
  }

  phone.addEventListener('input', function () {
    var d = digits(phone.value);
    phone.value = fmt(d);
    var bad = d.length > 0 && d.charAt(0) !== '0';
    hint.textContent = bad ? M.phoneStart : M.phoneHint + ' · ' + d.length + '/11';
    hint.className = 'cf-hint' + (d.length === 11 && !bad ? ' cf-good' : '');
    if (fields.phone.getAttribute('aria-invalid')) show('phone', checks.phone());
  });
  // Hata ilk gönderimden sonra ya da alandan çıkınca gösterilir, yazarken değil.
  Object.keys(fields).forEach(function (k) {
    var ev = k === 'kvkk' || k === 'topic' ? 'change' : 'blur';
    fields[k].addEventListener(ev, function () {
      if (k === 'phone' && !phone.value) return;
      if ((k === 'name' || k === 'message') && !fields[k].value) return;
      show(k, checks[k]());
    });
  });

  function setStatus(kind, text) {
    status.className = 'cf-status' + (kind ? ' cf-' + kind : '');
    status.textContent = text;
  }

  // JavaScript kapalıyken gönderilen formun sonucu (?form=ok|...).
  var q = /[?&]form=([a-z]+)/.exec(location.search);
  if (q) setStatus(q[1] === 'ok' ? 'ok' : 'fail', q[1] === 'ok' ? M.ok : M[q[1]] || M.fail);

  var busy = false;
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (busy) return;
    var first = null;
    Object.keys(checks).forEach(function (k) {
      var problem = checks[k]();
      show(k, problem);
      if (problem && !first) first = fields[k];
    });
    if (first) { first.focus(); setStatus('', ''); return; }

    busy = true;
    button.disabled = true;
    setStatus('', M.sending);
    var payload = {
      lang: EN ? 'en' : 'tr',
      website: hp.value,
      t: Date.now() - started,
      name: squash(name.value),
      phone: digits(phone.value),
      email: email.value.trim(),
      topic: topic.value,
      message: message.value.trim(),
      kvkk: kvkk.checked
    };
    fetch(form.getAttribute('action'), {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
      credentials: 'same-origin'
    })
      .then(function (r) { return r.json().catch(function () { return { ok: false }; }); })
      .then(function (data) {
        if (data && data.ok) {
          setStatus('ok', M.ok);
          form.reset();
          hint.textContent = M.phoneHint;
          hint.className = 'cf-hint';
          started = Date.now();
          return;
        }
        var code = data && data.error;
        if (code && checks[code] && fields[code]) { show(code, checks[code]() || M[code] || M.fail); setStatus('', ''); fields[code].focus(); }
        else setStatus('fail', M[code] || M.fail);
      })
      .catch(function () { setStatus('fail', M.fail); })
      .then(function () { busy = false; button.disabled = false; });
  });
})();
