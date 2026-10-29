# SEO uygulaması · 30 Ekim 2026

## Tamamlanan site içi işler
- Ana sayfa: dört somut sürüş ihtiyacından ilgili eğitim sayfasına geçiş ve yerel adres/iletişim bölümü; doğrulanmamış hızlı başarı vaadi kaldırıldı.
- 8 Türkçe eğitim sayfası: her hizmete özgü giriş, üç konu bölümü, kayıt hazırlığı, görünür soru/cevaplar, ilgili eğitim ve rehber bağlantıları. Başlık, açıklama, H1 ve WebPage/Service verisi aynı içeriği anlatıyor.
- 8 İngilizce karşılık: mevcut hizmet kapsamına uygun açıklamalar ve konu bölümleri. Türkçe rehber bağlantıları dil etiketiyle gösteriliyor.
- 50 rehber yazısı: makalenin içinde konuya uygun eğitim sayfasına veya eğitim karşılaştırmasına bağlantı.
- Önceki fotoğraflı rehber kartları ve kapaklar korundu. Gerçek kurs fotoğrafları için arama niyetine uygun, görselle ilişkili alt açıklamalar taşındı.
- Sabit “+12 saat ortalama”, ücretsiz sağlık raporu ve doğrulanmamış çevrim içi kurs/garanti iddiaları eğitim metinlerinden kaldırıldı. SSS’de sağlık raporu yanıtı da görünür metin ve FAQPage içinde düzeltildi.
- Mobil eğitim sayfalarında asıl eğitim içeriği uzun yan menüden önce geliyor.
- İçerik kaynağı `content/course-seo.json` ve `content/course-seo-en.json`; `scripts/strengthen-seo.py` derlemede tekrar üretir. Rehberlerin hukuki bilgi kontrol tarihleri bu işlemle değiştirilmedi.

## Ölçüm
- Cloudflare Web Analytics mevcut yapılandırması korunuyor.
- `api/olcum.js` yalnız sabit izin listelerindeki telefon tıklaması, WhatsApp tıklaması ve otomatik WhatsApp açılışını kabul eder.
- İstemci yalnız sabit sayfa yolu, genel geliş kanalı ve bağlantının sayfadaki konumunu gönderir. Arama sorgusu, ham yönlendiren URL, telefon numarası, WhatsApp mesajı, form alanı, ziyaretçi kimliği veya çerez gönderilmez.
- Kaynak kanalı yalnız sabit bir kategori olarak sessionStorage içinde sekme boyunca korunur; site içi gezinmede organik kaynağın kaybolmasını önler. Kişi kimliği değildir. Sağlayıcıca kabul edilen talep olayında bu kategori ayrıca kayıt altına alınır.
- DNT veya Global Privacy Control etkinse tıklama ölçümü devreye girmez. Aynı sayfa yüklemesinde aynı olay/konum tekrarı tekilleştirilir. Bu kullanıcı veya oturum bazlı bir tekil kişi sayımı değildir.
- Başarıyla iletilen form/asistan talepleri `api/iletisim.js` içinde e-posta sağlayıcısı başarı yanıtından sonra `uslu_lead_delivery` olayıyla kaydedilir. Bot tuzağı ve başarısız gönderim başarı metriğine girmez.
- Yeni olaylar Vercel Runtime Logs içinde `uslu_engagement` ve `uslu_lead_delivery` etiketleriyle izlenebilir. Kalıcı analitik veri tabanı veya geçmişe dönük ölçüm oluşturulmadı. Log saklama süresi Vercel planına bağlıdır; haftalık rapora otomatik dahil oldukları iddia edilmez.
- Tıklama bir telefon görüşmesi, gönderilmiş WhatsApp mesajı veya kesin kurs kaydı değildir. E-posta sağlayıcısının kabulü de tamamlanmış kayıt değildir.
- Aydınlatma metnine gerçek ölçüm alanlarını açıklayan bölüm eklendi. Bu değişiklik bir hukuki uygunluk denetimi değildir.

## Hesap erişimi veya işletme doğrulaması bekleyenler
- Vercel üretim ortamında GSC ve Cloudflare rapor değişkenlerinin yapılandırıldığı, gizli değerleri açılmadan doğrulandı.
- GSC sorgu/sayfa verisi okunamadı: Vercel Secret değerlerini `env run` ile yerel komuta aktarmıyor. Son 90 gün performansı, gerçek indeks durumu ve Google’ın seçtiği canonical bu çalışma kapsamında doğrulanmış değildir. Haftalık rapor veya yetkili Search Console erişimiyle devam edilmeli; sıralama/tıklama artışı iddia edilmez.
- Google’ın herkese açık işletme paneli kontrol edildi: web sitesi, Atatürk Cd. No:2/17 adresi ve 0532 068 56 47 ana telefon eşleşiyor.
- Aynı Google panelinde her gün 08.30–20.30; sitede Pazartesi–Perşembe 09.00–19.30 ve Cuma–Pazar 09.00–20.30 görünüyor. İşletme sahibi sitedeki saatlerin doğru olduğunu doğruladı. Site saatleri korundu; Google profil saatlerinin yetkili profil hesabından siteyle eşitlenmesi gerekiyor.
- Google profil açıklamasında ana telefondan farklı bir numara bulunuyor; profil sahibi üzerinden doğrulanmalı. Bu çalışma profil düzenlemesi veya yorum yayını yapmadı.
- Araç modeli, donanım, özel ders koşulları, belirli ders saatleri veya başarı oranları işletme onayı olmadan eklenmedi.

## Doğrulama
`npm run build`: güvenlik kuralları, statik çıktı ve yerel bağlantılar.
`npm run check`: 84 sayfanın metadata/başlık/JSON-LD kontrolleri; 8 farklı Türkçe eğitim içeriği, 50 bağlamsal rehber bölümü, ölçüm izin listeleri, veri sızıntısı engeli, olay tekilleştirme, DNT/GPC ve sahte e-posta sağlayıcısıyla sunucu başarı metriği.
Gerçek e-posta, telefon veya WhatsApp mesajı gönderilerek test yapılmadı.

Resmî bilgi kaynağı: https://www.nvi.gov.tr/sss-surucu-belgeleri-hizmetleri
Otomatik araç kodu: https://www.nvi.gov.tr/kurumlar/nvi.gov.tr/Projeler/kodtablosu.pdf
SEO yaklaşımı: https://developers.google.com/search/docs/fundamentals/creating-helpful-content

## Profil sahibine hazır düzeltme metni
Çalışma saatleri: Pazartesi–Perşembe 09.00–19.30, Cuma–Pazar 09.00–20.30.
Ana iletişim: 0532 068 56 47. Web sitesi: https://uslusurucukursu.com/
Açıklama önerisi: “Uslu Sürücü Kursu, Ankara Sincan’da B sınıfı manuel ve otomatik ehliyet, A1–A2 motosiklet eğitimleri ve özel direksiyon dersi hakkında program ve kayıt bilgisi sunar. Eğitim seçiminizi, mevcut belgenizi ve ders hedeflerinizi birlikte değerlendirmek için Atatürk Caddesi’ndeki ofisimizle iletişime geçebilirsiniz. Ofisimiz 2. Noterin üst katındadır.”
Bu metin profile gönderilmedi; profil sahibinin yetkili hesabında kullanılmak üzere hazırlandı.
