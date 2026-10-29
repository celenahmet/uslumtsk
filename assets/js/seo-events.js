(function(){
 'use strict';
 // Navigation must work even if measurement is disabled, blocked or unavailable.
 if(location.hostname!=='uslusurucukursu.com'||navigator.doNotTrack==='1'||navigator.globalPrivacyControl)return;
 /* pages start */
var pages=["/", "/en/", "/hakkimizda/", "/en/about-us/", "/iletisim/", "/en/contact/", "/sss/", "/en/faq/", "/yorumlar/", "/en/comments/", "/egitim/", "/en/train/", "/egitim/manuel-b/", "/en/train/manuel-b/", "/egitim/otomatik-b/", "/en/train/automatic-b/", "/egitim/motor-a1/", "/en/train/motorcycle-a1/", "/egitim/motor-a2/", "/en/train/motorcycle-a2/", "/egitim/ozel/", "/en/train/special/", "/egitim/ozel-ab/", "/en/train/special-ab/", "/egitim/diger/", "/en/train/other/", "/galeri/genel/", "/en/gallery/general/", "/galeri/araclar/", "/en/gallery/cars/", "/galeri/siniflar/", "/en/gallery/class/", "/kvkk/", "/rehber/", "/rehber/ehliyet-nasil-alinir/", "/rehber/ankarada-ehliyet-almak/", "/rehber/sincanda-ehliyet-almak/", "/rehber/ehliyet-icin-gerekli-belgeler/", "/rehber/surucu-olur-raporu/", "/rehber/sabika-kaydi-ehliyet/", "/rehber/diplomasiz-ehliyet/", "/rehber/yabancilar-icin-ehliyet/", "/rehber/ehliyet-fotografi/", "/rehber/ehliyet-masraflari/", "/rehber/ehliyet-randevusu/", "/rehber/surucu-kursu-kayit-donemleri/", "/rehber/surucu-kursu-devamsizlik/", "/rehber/surucu-kursu-degistirme/", "/rehber/direksiyon-dersi/", "/rehber/k-sinifi-surucu-aday-belgesi/", "/rehber/surucu-sertifikasi/", "/rehber/otomatik-vites-ehliyet/", "/rehber/ehliyetim-var-araba-kullanamiyorum/", "/rehber/ehliyet-sinavi/", "/rehber/e-sinav-kurallari/", "/rehber/e-sinav-sonucu-itiraz/", "/rehber/direksiyon-sinavi-geri-park/", "/rehber/motosiklet-direksiyon-sinavi/", "/rehber/sinavda-kalirsam/", "/rehber/ehliyet-sinavi-mazeret/", "/rehber/ehliyet-siniflari/", "/rehber/16-yasinda-ehliyet/", "/rehber/motosiklet-ehliyeti/", "/rehber/b-ehliyetle-motosiklet/", "/rehber/b-ehliyetle-romork/", "/rehber/kamyon-ehliyeti/", "/rehber/otobus-ehliyeti/", "/rehber/traktor-ehliyeti/", "/rehber/is-makinesi-ehliyeti/", "/rehber/ehliyete-sinif-ekleme/", "/rehber/ozel-gereksinimli-surucu-adaylari/", "/rehber/ehliyet-yenileme/", "/rehber/kayip-ehliyet/", "/rehber/aday-surucu-belgesi/", "/rehber/yurt-disi-ehliyet/", "/rehber/psikoteknik-degerlendirme/", "/rehber/ehliyet-ceza-puani/", "/rehber/alkollu-arac-kullanma-cezasi/", "/rehber/hiz-siniri-cezasi/", "/rehber/kirmizi-isik-cezasi/", "/rehber/arac-kullanirken-telefon-cezasi/", "/rehber/ehliyetsiz-arac-kullanma-cezasi/", "/rehber/trafik-kazasinda-ne-yapilmali/", "/rehber/trafik-cezasina-itiraz/"];
/* pages end */
 var page=location.pathname;if(pages.indexOf(page)<0)return;
 var channel='direct';
 try{if(document.referrer){var host=new URL(document.referrer).hostname;if(host===location.hostname)channel='internal';else if(/(^|\.)google\.[a-z.]+$|(^|\.)(bing|yandex|duckduckgo)\.com$/.test(host))channel='search';else if(/(^|\.)(instagram|facebook|tiktok|youtube)\.com$|(^|\.)t\.co$/.test(host))channel='social';else channel='referral';}}catch(_){}
 // Keep only a coarse acquisition category for this tab, never a visitor ID.
 try{var stored=sessionStorage.getItem('uslu-acquisition');if(channel==='internal'&&['search','social','referral','direct'].indexOf(stored)>=0)channel=stored;else if(channel!=='internal')sessionStorage.setItem('uslu-acquisition',channel);}catch(_){}
 window.usluSourceChannel=function(){return channel;};
 var seen=Object.create(null);
 function send(event,placement){
  var key=event+':'+placement;if(seen[key])return;seen[key]=true;
  var body=JSON.stringify({event:event,page:page,channel:channel,placement:placement});
  try{if(navigator.sendBeacon&&navigator.sendBeacon('/api/olcum/',new Blob([body],{type:'application/json'})))return;fetch('/api/olcum/',{method:'POST',headers:{'Content-Type':'application/json'},body:body,keepalive:true,credentials:'omit'}).catch(function(){});}catch(_){}
 }
 document.addEventListener('click',function(e){
  var a=e.target.closest&&e.target.closest('a[href]');if(!a)return;
  var placement=a.closest('.uc-panel')?'assistant':a.closest('footer')?'footer':a.closest('.header-top,header,.main-navigation')?'header':'content';
  var href=a.getAttribute('href')||'';
  if(href.indexOf('tel:')===0){send('phone_click',placement);return;}
  try{var u=new URL(href,location.href);if(u.hostname==='wa.me'||u.hostname==='api.whatsapp.com'||(u.origin===location.origin&&u.pathname==='/whatsapp/'))send('whatsapp_click',placement);}catch(_){}
 },{capture:true});
 window.usluWhatsAppOpened=function(){send('whatsapp_auto_open','assistant');};
})();
