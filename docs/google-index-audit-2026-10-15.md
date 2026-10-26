# Google dizin denetimi — 15 Ekim 2026

Kaynak: Downloads/edakapusuz içindeki iki Coverage-Drilldown Excel raporu. Raporların son zaman serisi verisi 9 Ekim 2026. Canlı HTTP denetimi 15 Ekim 2026 (Türkiye saati).

40 keşfedilmiş URL: tamamı HTTP 200, kendine işaret eden canonical, index/follow, X-Robots-Tag engeli yok. Tamamı yerel sitemap içinde ve iç bağlantı alıyor. Canlı robots.txt taramaya izin veriyor. Bu kontrol Googlebot erişimini veya Google tarafından seçilen canonical değerini doğrulamaz; bunlar Search Console URL Denetimi ve tarama istatistiklerinden kontrol edilmeli.

7 eski URL: iki galeri URLsi mevcut doğru sayfaya kalıcı yönleniyor. Diğer beşi eski WordPress yolları; canlıda ana sayfaya yönleniyor. Vercel yapılandırmasında genel blog alt yolu yönlendirmesi kaldırıldı: karşılığı olmayan kaynaklar gerçek 404 vermeli. Blog ana adresi ilgili /rehber/ sayfasına kalıcı yönlendiriliyor. Değişiklik henüz yayınlanmadı.

## Search Console adımları

1. /sitemap.xml kaydının son okuma tarihini ve başarı durumunu kontrol et; gerekiyorsa yeniden gönder.
2. /rehber/ ve öncelikli kurs rehberlerinde URL Denetimi → Canlı URLyi test et → Dizine eklenmesini iste.
3. Tarama istatistiklerinde sunucu erişimi/5xx/429 problemlerini ve URL Denetiminde Google tarafından seçilen canonical adresini kontrol et.
4. Galeri 404 doğrulaması zaten başlatılmış; yeni tarama sonucunu bekle. Silinmiş WordPress kaynaklarının dizine girmesi istenmez, 404 normaldir.
5. Keşfedilen sayfalar için raporu yeni tarama verisiyle tekrar karşılaştır. Dizine eklenme garanti edilemez.

## URL bazında canlı sonuçlar

| URL | Son HTTP | Son hedef | Yerel iç bağlantı veren sayfa |
|---|---|---|---|
| https://uslusurucukursu.com/en/gallery/general/ | 200 | https://uslusurucukursu.com/en/gallery/general/ | 17 |
| https://uslusurucukursu.com/rehber/16-yasinda-ehliyet/ | 200 | https://uslusurucukursu.com/rehber/16-yasinda-ehliyet/ | 12 |
| https://uslusurucukursu.com/rehber/aday-surucu-belgesi/ | 200 | https://uslusurucukursu.com/rehber/aday-surucu-belgesi/ | 9 |
| https://uslusurucukursu.com/rehber/alkollu-arac-kullanma-cezasi/ | 200 | https://uslusurucukursu.com/rehber/alkollu-arac-kullanma-cezasi/ | 10 |
| https://uslusurucukursu.com/rehber/ankarada-ehliyet-almak/ | 200 | https://uslusurucukursu.com/rehber/ankarada-ehliyet-almak/ | 69 |
| https://uslusurucukursu.com/rehber/arac-kullanirken-telefon-cezasi/ | 200 | https://uslusurucukursu.com/rehber/arac-kullanirken-telefon-cezasi/ | 8 |
| https://uslusurucukursu.com/rehber/b-ehliyetle-motosiklet/ | 200 | https://uslusurucukursu.com/rehber/b-ehliyetle-motosiklet/ | 13 |
| https://uslusurucukursu.com/rehber/b-ehliyetle-romork/ | 200 | https://uslusurucukursu.com/rehber/b-ehliyetle-romork/ | 11 |
| https://uslusurucukursu.com/rehber/diplomasiz-ehliyet/ | 200 | https://uslusurucukursu.com/rehber/diplomasiz-ehliyet/ | 11 |
| https://uslusurucukursu.com/rehber/direksiyon-dersi/ | 200 | https://uslusurucukursu.com/rehber/direksiyon-dersi/ | 56 |
| https://uslusurucukursu.com/rehber/direksiyon-sinavi-geri-park/ | 200 | https://uslusurucukursu.com/rehber/direksiyon-sinavi-geri-park/ | 9 |
| https://uslusurucukursu.com/rehber/e-sinav-kurallari/ | 200 | https://uslusurucukursu.com/rehber/e-sinav-kurallari/ | 7 |
| https://uslusurucukursu.com/rehber/e-sinav-sonucu-itiraz/ | 200 | https://uslusurucukursu.com/rehber/e-sinav-sonucu-itiraz/ | 7 |
| https://uslusurucukursu.com/rehber/ehliyet-ceza-puani/ | 200 | https://uslusurucukursu.com/rehber/ehliyet-ceza-puani/ | 10 |
| https://uslusurucukursu.com/rehber/ehliyet-fotografi/ | 200 | https://uslusurucukursu.com/rehber/ehliyet-fotografi/ | 11 |
| https://uslusurucukursu.com/rehber/ehliyet-sinavi-mazeret/ | 200 | https://uslusurucukursu.com/rehber/ehliyet-sinavi-mazeret/ | 7 |
| https://uslusurucukursu.com/rehber/ehliyet-sinavi/ | 200 | https://uslusurucukursu.com/rehber/ehliyet-sinavi/ | 69 |
| https://uslusurucukursu.com/rehber/ehliyet-siniflari/ | 200 | https://uslusurucukursu.com/rehber/ehliyet-siniflari/ | 69 |
| https://uslusurucukursu.com/rehber/ehliyet-yenileme/ | 200 | https://uslusurucukursu.com/rehber/ehliyet-yenileme/ | 69 |
| https://uslusurucukursu.com/rehber/ehliyete-sinif-ekleme/ | 200 | https://uslusurucukursu.com/rehber/ehliyete-sinif-ekleme/ | 14 |
| https://uslusurucukursu.com/rehber/ehliyetsiz-arac-kullanma-cezasi/ | 200 | https://uslusurucukursu.com/rehber/ehliyetsiz-arac-kullanma-cezasi/ | 8 |
| https://uslusurucukursu.com/rehber/hiz-siniri-cezasi/ | 200 | https://uslusurucukursu.com/rehber/hiz-siniri-cezasi/ | 9 |
| https://uslusurucukursu.com/rehber/is-makinesi-ehliyeti/ | 200 | https://uslusurucukursu.com/rehber/is-makinesi-ehliyeti/ | 11 |
| https://uslusurucukursu.com/rehber/k-sinifi-surucu-aday-belgesi/ | 200 | https://uslusurucukursu.com/rehber/k-sinifi-surucu-aday-belgesi/ | 9 |
| https://uslusurucukursu.com/rehber/kayip-ehliyet/ | 200 | https://uslusurucukursu.com/rehber/kayip-ehliyet/ | 5 |
| https://uslusurucukursu.com/rehber/kirmizi-isik-cezasi/ | 200 | https://uslusurucukursu.com/rehber/kirmizi-isik-cezasi/ | 8 |
| https://uslusurucukursu.com/rehber/motosiklet-ehliyeti/ | 200 | https://uslusurucukursu.com/rehber/motosiklet-ehliyeti/ | 69 |
| https://uslusurucukursu.com/rehber/otobus-ehliyeti/ | 200 | https://uslusurucukursu.com/rehber/otobus-ehliyeti/ | 12 |
| https://uslusurucukursu.com/rehber/ozel-gereksinimli-surucu-adaylari/ | 200 | https://uslusurucukursu.com/rehber/ozel-gereksinimli-surucu-adaylari/ | 13 |
| https://uslusurucukursu.com/rehber/psikoteknik-degerlendirme/ | 200 | https://uslusurucukursu.com/rehber/psikoteknik-degerlendirme/ | 5 |
| https://uslusurucukursu.com/rehber/sabika-kaydi-ehliyet/ | 200 | https://uslusurucukursu.com/rehber/sabika-kaydi-ehliyet/ | 11 |
| https://uslusurucukursu.com/rehber/sinavda-kalirsam/ | 200 | https://uslusurucukursu.com/rehber/sinavda-kalirsam/ | 69 |
| https://uslusurucukursu.com/rehber/sincanda-ehliyet-almak/ | 200 | https://uslusurucukursu.com/rehber/sincanda-ehliyet-almak/ | 69 |
| https://uslusurucukursu.com/rehber/surucu-kursu-degistirme/ | 200 | https://uslusurucukursu.com/rehber/surucu-kursu-degistirme/ | 8 |
| https://uslusurucukursu.com/rehber/surucu-kursu-devamsizlik/ | 200 | https://uslusurucukursu.com/rehber/surucu-kursu-devamsizlik/ | 8 |
| https://uslusurucukursu.com/rehber/surucu-kursu-kayit-donemleri/ | 200 | https://uslusurucukursu.com/rehber/surucu-kursu-kayit-donemleri/ | 52 |
| https://uslusurucukursu.com/rehber/surucu-sertifikasi/ | 200 | https://uslusurucukursu.com/rehber/surucu-sertifikasi/ | 9 |
| https://uslusurucukursu.com/rehber/trafik-cezasina-itiraz/ | 200 | https://uslusurucukursu.com/rehber/trafik-cezasina-itiraz/ | 8 |
| https://uslusurucukursu.com/rehber/trafik-kazasinda-ne-yapilmali/ | 200 | https://uslusurucukursu.com/rehber/trafik-kazasinda-ne-yapilmali/ | 9 |
| https://uslusurucukursu.com/rehber/traktor-ehliyeti/ | 200 | https://uslusurucukursu.com/rehber/traktor-ehliyeti/ | 11 |
| https://uslusurucukursu.com/en/gallery/gcars | 200 | https://uslusurucukursu.com/en/gallery/cars/ | 0 |
| https://uslusurucukursu.com/blog/wp-content/themes/mistify/* | 200 | https://uslusurucukursu.com/ | 0 |
| https://uslusurucukursu.com/blog/wp-content/uploads/* | 200 | https://uslusurucukursu.com/ | 0 |
| https://uslusurucukursu.com/blog/wp-admin/* | 200 | https://uslusurucukursu.com/ | 0 |
| https://uslusurucukursu.com/blog/* | 200 | https://uslusurucukursu.com/ | 0 |
| https://uslusurucukursu.com/blog/wp-content/plugins/* | 200 | https://uslusurucukursu.com/ | 0 |
| https://uslusurucukursu.com/en/gallery/gclass | 200 | https://uslusurucukursu.com/en/gallery/class/ | 0 |
