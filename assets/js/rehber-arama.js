// Ehliyet Rehberi araması (/rehber/): yazdıkça sorular süzülür. Ana sayfadaki arama kutusu
// buraya ?q= ile gelir. Başlık, kısa açıklama ve yazının SSS sorularında (data-ara) arar; Türkçe
// harfsiz yazım da eşleşir ("sinav" → "Sınav"). Aranan metin sayfaya HTML olarak yazılmaz,
// yalnız textContent ile kullanılır.
(function () {
  'use strict';
  var form = document.getElementById('guide-search');
  var hub = document.querySelector('.guide-hub');
  var info = document.getElementById('guide-search-info');
  if (!form || !hub || !info) return;
  var input = form.querySelector('input');
  var MAP = { 'ı': 'i', 'ş': 's', 'ğ': 'g', 'ü': 'u', 'ö': 'o', 'ç': 'c', 'â': 'a', 'î': 'i', 'û': 'u' };
  var norm = function (t) {
    return String(t).toLocaleLowerCase('tr').replace(/[ışğüöçâîû]/g, function (c) { return MAP[c]; })
      .replace(/[^a-z0-9]+/g, ' ').trim();
  };
  var groups = [].slice.call(hub.querySelectorAll('.guide-hub-group')).map(function (g) {
    var name = g.querySelector('h2').textContent;
    return {
      el: g,
      items: [].slice.call(g.querySelectorAll('.guide-hub-list li')).map(function (li) {
        return { el: li, text: norm(name + ' ' + li.textContent + ' ' + (li.getAttribute('data-ara') || '')) };
      })
    };
  });

  function apply(value) {
    var words = norm(value).split(' ').filter(Boolean);
    var found = 0;
    hub.classList.toggle('is-searching', words.length > 0);
    groups.forEach(function (g) {
      var shown = 0;
      g.items.forEach(function (it) {
        var ok = words.every(function (w) { return it.text.indexOf(w) !== -1; });
        it.el.hidden = !ok;
        if (ok) shown++;
      });
      g.el.hidden = shown === 0;
      found += shown;
    });
    if (!words.length) {
      info.hidden = true;
      return;
    }
    info.hidden = false;
    if (found) {
      info.textContent = found + ' yazı bulundu.';
    } else {
      info.innerHTML = 'Bu aramayla eşleşen yazı bulunamadı. Sorunuzu bize iletin: ' +
        '<a href="tel:+905320685647">0532 068 56 47</a> ya da <a href="/iletisim/">iletişim formu</a>.';
    }
  }

  input.addEventListener('input', function () { apply(input.value); });
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    apply(input.value);
    info.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
  var q = new URLSearchParams(location.search).get('q');
  if (q) {
    input.value = q.slice(0, 100);
    apply(input.value);
  }
})();
