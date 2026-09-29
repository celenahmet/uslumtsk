# Ehliyet Rehberi içerikleri. Yalnız resmî kaynaklarda doğrulanan bilgiler.
# Kural: uzun tire yok, kurs fiyatı yok, doğrulanmamış tutar yok.

SRC = {
    'mtsk': ('MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği (mevzuat.gov.tr)',
             'https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=18408&MevzuatTur=7&MevzuatTertip=5'),
    'esinav': ('MEB Motorlu Taşıt Sürücü Kursiyerleri e-Sınav Başvuru ve Uygulama Kılavuzu 2026 (PDF)',
               'https://www.meb.gov.tr/meb_iys_dosyalar/2026_07/6a6b50c06daf3993652350_MTSK_e-Sinav_Kilavuzu_2026.pdf'),
    'kty': ('Karayolları Trafik Yönetmeliği (mevzuat.gov.tr)',
            'https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=8182&MevzuatTur=7&MevzuatTertip=5'),
    'saglik': ('Sürücü Adayları ve Sürücülerde Aranacak Sağlık Şartları ile Muayenelerine Dair Yönetmelik (mevzuat.gov.tr)',
               'https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=10664&MevzuatTur=7&MevzuatTertip=5'),
    'nvi_sss': ('Nüfus ve Vatandaşlık İşleri Genel Müdürlüğü: Sürücü Belgeleri Hizmetleri Sıkça Sorulan Sorular',
                'https://www.nvi.gov.tr/sss-surucu-belgeleri-hizmetleri'),
    'nvi_ucret': ('NVİ Randevu Sistemi: 2026 yılı sürücü belgesi ücretleri',
                  'https://randevu.nvi.gov.tr/pages/applicationprices'),
    'adli': ('e-Devlet: Adli Sicil Kaydı Sorgulama', 'https://www.turkiye.gov.tr/adli-sicil-kaydi'),
    'esinav_site': ('MEB e-Sınav Bilgi Sistemi', 'https://esinav.meb.gov.tr/'),
    'ktk': ('2918 sayılı Karayolları Trafik Kanunu (mevzuat.gov.tr, PDF)',
            'https://www.mevzuat.gov.tr/MevzuatMetin/1.5.2918.pdf'),    'kabahat': ('5326 sayılı Kabahatler Kanunu (mevzuat.gov.tr, PDF)',
                'https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5326.pdf'),
}

def ext(label, url):
    return '<a href="%s" rel="noopener noreferrer" target="_blank">%s</a>' % (url, label)

R = {  # rehber içi bağlantılar
    'nasil': '/rehber/ehliyet-nasil-alinir/',
    'siniflar': '/rehber/ehliyet-siniflari/',
    'belgeler': '/rehber/ehliyet-icin-gerekli-belgeler/',
    'sinav': '/rehber/ehliyet-sinavi/',
    'masraf': '/rehber/ehliyet-masraflari/',
    'otomatik': '/rehber/otomatik-vites-ehliyet/',
    'kalirsam': '/rehber/sinavda-kalirsam/',
    'motor': '/rehber/b-ehliyetle-motosiklet/',
    'korku': '/rehber/ehliyetim-var-araba-kullanamiyorum/',
    'sincan': '/rehber/sincanda-ehliyet-almak/',
    'yenileme': '/rehber/ehliyet-yenileme/',
    'kayip': '/rehber/kayip-ehliyet/',
    'yurtdisi': '/rehber/yurt-disi-ehliyet/',
    'aday': '/rehber/aday-surucu-belgesi/',
    'ceza': '/rehber/ehliyet-ceza-puani/',
    'rapor': '/rehber/surucu-olur-raporu/',
    'motosiklet': '/rehber/motosiklet-ehliyeti/',
    'ekleme': '/rehber/ehliyete-sinif-ekleme/',
    'ozel': '/rehber/ozel-gereksinimli-surucu-adaylari/',
    'randevu': '/rehber/ehliyet-randevusu/',
    'ankara': '/rehber/ankarada-ehliyet-almak/',
    'kayitdonemi': '/rehber/surucu-kursu-kayit-donemleri/',
    'devamsizlik': '/rehber/surucu-kursu-devamsizlik/',
    'nakil': '/rehber/surucu-kursu-degistirme/',
    'direksiyon': '/rehber/direksiyon-dersi/',
    'kbelgesi': '/rehber/k-sinifi-surucu-aday-belgesi/',
    'sertifika': '/rehber/surucu-sertifikasi/',
    'esinavkural': '/rehber/e-sinav-kurallari/',
    'esinavitiraz': '/rehber/e-sinav-sonucu-itiraz/',
    'geripark': '/rehber/direksiyon-sinavi-geri-park/',
    'motorsinav': '/rehber/motosiklet-direksiyon-sinavi/',
    'mazeret': '/rehber/ehliyet-sinavi-mazeret/',
    'yas16': '/rehber/16-yasinda-ehliyet/',
    'romork': '/rehber/b-ehliyetle-romork/',
    'kamyon': '/rehber/kamyon-ehliyeti/',
    'otobus': '/rehber/otobus-ehliyeti/',
    'traktor': '/rehber/traktor-ehliyeti/',
    'ismakinesi': '/rehber/is-makinesi-ehliyeti/',
    'sabika': '/rehber/sabika-kaydi-ehliyet/',
    'diploma': '/rehber/diplomasiz-ehliyet/',
    'yabanci': '/rehber/yabancilar-icin-ehliyet/',
    'fotograf': '/rehber/ehliyet-fotografi/',
    'psikoteknik': '/rehber/psikoteknik-degerlendirme/',
    'alkol': '/rehber/alkollu-arac-kullanma-cezasi/',
    'hiz': '/rehber/hiz-siniri-cezasi/',
    'kirmizi': '/rehber/kirmizi-isik-cezasi/',
    'telefon': '/rehber/arac-kullanirken-telefon-cezasi/',
    'ehliyetsiz': '/rehber/ehliyetsiz-arac-kullanma-cezasi/',
    'kaza': '/rehber/trafik-kazasinda-ne-yapilmali/',
    'itiraz': '/rehber/trafik-cezasina-itiraz/',
}

def a(key, text):
    return '<a href="%s">%s</a>' % (R[key], text)

PAGES = []

# 1 ─────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='nasil',
    title='Ehliyet Nasıl Alınır? 2026 Adım Adım Süreç | Uslu Sürücü Kursu',
    desc='Ankara’da ehliyet nasıl alınır? Sürücü olur raporundan nüfus müdürlüğü başvurusuna kadar adımlar: kurs kaydı, teorik dersler, e-Sınav, direksiyon eğitimi ve sınavı.',
    h1='Ehliyet Nasıl Alınır? Adım Adım 2026',
    crumb='Ehliyet Nasıl Alınır',
    card='Rapordan nüfus müdürlüğüne kadar sekiz adımda tüm süreç.',
    lead='Türkiye’de ehliyet (sürücü belgesi) almak için Millî Eğitim Bakanlığına bağlı bir özel sürücü kursunda eğitim alıp teorik ve direksiyon sınavlarını geçmek, ardından nüfus müdürlüğüne başvurmak gerekir. Aşağıda süreci en çok alınan B sınıfı (otomobil) ehliyeti üzerinden adım adım anlattık; diğer sınıflarda adımlar aynıdır, yaş şartı ve ders saatleri değişir.',
    summary=[
        'Sürücü olur raporunu alıp belgelerinizle bir sürücü kursuna kayıt olursunuz.',
        '34 saatlik teorik dersin ardından 50 soruluk e-Sınav’a girersiniz; geçme puanı 70’tir.',
        'B sınıfında akan trafikte en az 14 saat direksiyon dersi alırsınız, bunun en az 2 saati gecedir.',
        'Direksiyon sınavını geçince sertifikanız e-Devlet’te görünür; ehliyet için nüfus müdürlüğüne randevuyla başvurursunuz.',
    ],
    body='''
<h2>1. Sınıfınızı ve yaş şartını kontrol edin</h2>
<p>Otomobil ve kamyonet için B sınıfı ehliyet gerekir ve 18 yaşını bitirmiş olmak şarttır. Motosiklette A1 için 16, A2 için 18 yaş aranır. Bunun yanında en az ilkokul düzeyinde öğrenim, sağlık şartlarını taşımak ve belirli suçlardan adli sicil kaydı bulunmamak gerekir (Karayolları Trafik Yönetmeliği m.76). Tüm sınıflar için ''' + a('siniflar', 'ehliyet sınıfları ve yaş sınırları') + ''' yazımıza bakabilirsiniz.</p>

<h2>2. Sürücü olur raporunu alın</h2>
<p>Sürücü adaylarının muayenesini; Sağlık Bakanlığına ve üniversitelere bağlı sağlık tesisleri, aile sağlığı merkezleri ve muayenehaneler dışındaki özel sağlık kuruluşlarında görevli hekimler yapar ve raporu düzenler (Sürücü Sağlık Yönetmeliği m.4). Nüfus ve Vatandaşlık İşleri Genel Müdürlüğü, sürücü sağlık raporlarının 2 yıl geçerli olduğunu belirtir.</p>

<h2>3. Sürücü kursuna kayıt olun</h2>
<p>Kayıtta kimlik kartı, öğrenim belgesi, biyometrik fotoğraf, sürücü olur raporu ve adli sicil kaydı belgesi istenir; 18 yaşını doldurmamış adaylardan ayrıca veli izni alınır. Tam liste için ''' + a('belgeler', 'ehliyet için gerekli belgeler') + ''' yazımıza bakın.</p>

<h2>4. Teorik dersleri tamamlayın</h2>
<p>Bütün sınıflarda aynı teorik dersler verilir: trafik ve çevre 16 saat, ilk yardım 8 saat, araç tekniği 6 saat, trafik adabı 4 saat. Toplam 34 saattir. Teorik ders saatlerinin beşte birinden fazlasına katılmayan kursiyerin kaydı silinir (MTSK Yönetmeliği m.7 ve m.14).</p>

<h2>5. e-Sınav’a girin</h2>
<p>Teorik eğitimi biten aday, sınav ücretini yatırdıktan sonra kursu aracılığıyla e-Sınav başvurusu yapar. Sınav 50 soru ve 45 dakikadır, 70 ve üzeri puan başarılı sayılır. 2026 yılında her sınav oturumu için ücret KDV dahil 1.250 TL’dir. Adaylar, kayıtlı oldukları kursun bulunduğu ildeki e-Sınav merkezlerinde sınava girer. Ayrıntılar ''' + a('sinav', 'ehliyet sınavı') + ''' yazımızda.</p>

<h2>6. Direksiyon eğitimini alın</h2>
<p>Direksiyon eğitimi önce eğitim alanında veya simülatörde en az 2 saat verilir; usta öğretici adayın akan trafiğe hazır olduğuna karar verince trafikte devam edilir. B sınıfında akan trafikte en az 14 saat ders alınır ve bunun en az 2 saati gece sürüşüdür. Eğitim ve sınavda kullanılmak üzere, akan trafikte ders başladığı tarihten itibaren 6 ay geçerli K sınıfı sürücü aday belgesi düzenlenir (MTSK Yönetmeliği m.6 ve m.7).</p>

<h2>7. Direksiyon sınavını geçin</h2>
<p>Direksiyon sınavı, il veya ilçe millî eğitim müdürlüğünün belirlediği tarihlerde, izin alınmış güzergâhta ve akan trafikte yapılır. Sınavlar hafta sonları 07.00 ile 21.00 arasında düzenlenir ve her aday için en az 40 dakika sürer (MTSK Yönetmeliği m.28). Sınavda neler istendiğini ''' + a('sinav', 'ehliyet sınavı') + ''' yazımızda anlattık.</p>

<h2>8. Sertifikanızı alıp ehliyet başvurusu yapın</h2>
<p>Sınavları geçen adayın sertifikasına e-Devlet üzerinden erişilir; sertifika bilgileri, imza, fotoğraf ve sağlık raporu elektronik olarak Nüfus ve Vatandaşlık İşleri Genel Müdürlüğüne iletilir (MTSK Yönetmeliği m.38). Ehliyet için randevu.nvi.gov.tr, e-Devlet, NVİ Mobil veya Alo 199 üzerinden randevu alınır. Başvuru, sertifikanın alındığı yerden bağımsız olarak yetkili nüfus müdürlüklerinden birine yapılabilir; hazırlanan belge PTT ile ücretsiz olarak adresinize gönderilir. 09.07.2022 ve sonrasında alınan sertifikalarda başvuru için süre sınırı yoktur. Ödenecek harçlar için ''' + a('masraf', 'ehliyet masrafları') + ''' yazımıza bakın.</p>

<h2>Ehliyet almak ne kadar sürer?</h2>
<p>Süre; kursun grup başlama tarihine, sınav randevularına ve direksiyon ders planına göre değişir. Yönetmelik, grup başlama tarihinden itibaren son teorik sınav hakkı için randevu alma süresinin 90 günü, teorik sınavın geçildiği tarihten itibaren direksiyon derslerinin tamamlanma süresinin de 90 günü geçmeyecek şekilde planlanmasını öngörür (MTSK Yönetmeliği m.15).</p>
''',
    faq=[
        ('Ehliyet almak için kaç yaşında olmak gerekir?',
         'B sınıfı otomobil ehliyeti için 18 yaşını bitirmiş olmak gerekir. M, A1 ve B1 sınıfları için 16, A2 için 18, A sınıfı için 20 yaş aranır (Karayolları Trafik Yönetmeliği m.76).'),
        ('Sürücü kursuna gitmeden ehliyet alınabilir mi?',
         'Hayır. Sürücü belgesi alabilmek için sürücü sınavlarını başararak motorlu taşıt sürücüsü sertifikası almış olmak gerekir. Eğitim ve sınavlar MEB’e bağlı sürücü kursları üzerinden yürütülür.'),
        ('Ehliyet başvurusu hangi nüfus müdürlüğüne yapılır?',
         'NVİ’ye göre başvuru, sertifikanın alındığı yerden bağımsız olarak yetkilendirilen ilçe nüfus müdürlüklerinden birine, dış temsilciliklere veya nüfusmatik aracılığıyla yapılabilir. Randevu randevu.nvi.gov.tr, e-Devlet, NVİ Mobil veya Alo 199 üzerinden alınır.'),
        ('Sürücü sertifikasının geçerlilik süresi var mı?',
         'NVİ’ye göre 09.07.2022 ve sonrasında alınan sürücü sertifikalarında süre sınırlaması yoktur.'),
    ],
    sources=['mtsk', 'esinav', 'kty', 'saglik', 'nvi_sss'],
))

# 2 ─────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='siniflar',
    title='Ehliyet Sınıfları ve Yaş Sınırları (2026) | Uslu Sürücü Kursu',
    desc='M, A1, A2, A, B1, B, BE, C1, C, D1, D, F ve G ehliyet sınıfları hangi araçları kapsar, kaç yaşında alınır, kaç saat direksiyon dersi gerekir? Güncel tablo.',
    h1='Ehliyet Sınıfları ve Yaş Sınırları',
    crumb='Ehliyet Sınıfları',
    card='Hangi sınıf hangi aracı kapsar, kaç yaşında alınır, kaç saat ders gerekir.',
    lead='Ehliyet sınıfları, kullanacağınız aracın türüne göre belirlenir. Aşağıdaki tablolar Karayolları Trafik Yönetmeliği’nin 75, 76 ve 85. maddeleri ile MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’nin 7. maddesine dayanır.',
    summary=[
        'Otomobil için B sınıfı gerekir ve 18 yaşını bitirmiş olmak şarttır.',
        'Motosiklette A1 16, A2 18, A 20 yaşında alınır; A için iki yıllık A2 gerekir (24 yaşını dolduranlarda aranmaz).',
        'Kamyon (C) ve minibüs (D1) için 21, otobüs (D) için 24 yaş ve B sınıfı ehliyet gerekir.',
        'B sınıfı ehliyetle M (moped), B1 ve F (traktör) sınıfı araçlar da kullanılabilir.',
    ],
    body='''
<h2>Sınıflar, araçlar ve yaş şartları</h2>
<div class="guide-table"><table>
<thead><tr><th>Sınıf</th><th>Araç</th><th>En küçük yaş</th><th>Önce gereken ehliyet</th></tr></thead>
<tbody>
<tr><td>M</td><td>Moped</td><td>16</td><td>Yok</td></tr>
<tr><td>A1</td><td>Hafif motosiklet</td><td>16</td><td>Yok</td></tr>
<tr><td>A2</td><td>Orta güçte motosiklet</td><td>18</td><td>Yok</td></tr>
<tr><td>A</td><td>Tüm motosikletler</td><td>20</td><td>2 yıllık A2</td></tr>
<tr><td>B1</td><td>Dört tekerlekli motosiklet</td><td>16</td><td>Yok</td></tr>
<tr><td>B</td><td>Otomobil, kamyonet</td><td>18</td><td>Yok</td></tr>
<tr><td>BE</td><td>B + römork</td><td>18</td><td>B</td></tr>
<tr><td>C1</td><td>Kamyon (3.500-7.500 kg)</td><td>18</td><td>B</td></tr>
<tr><td>C1E</td><td>C1 + römork</td><td>18</td><td>C1</td></tr>
<tr><td>C</td><td>Kamyon, çekici</td><td>21</td><td>B</td></tr>
<tr><td>CE</td><td>C + römork</td><td>21</td><td>C</td></tr>
<tr><td>D1</td><td>Minibüs</td><td>21</td><td>B</td></tr>
<tr><td>D1E</td><td>D1 + römork</td><td>21</td><td>D1</td></tr>
<tr><td>D</td><td>Minibüs, otobüs</td><td>24</td><td>B</td></tr>
<tr><td>DE</td><td>D + römork</td><td>24</td><td>D</td></tr>
<tr><td>F</td><td>Lastik tekerlekli traktör</td><td>18</td><td>Yok</td></tr>
<tr><td>G</td><td>İş makinesi</td><td>18</td><td>Yok</td></tr>
</tbody></table></div>
<p>Tablodaki araç tanımlarının ayrıntısı:</p>
<ul>
<li><strong>M:</strong> iki, üç ve dört tekerlekli motorlu bisikletler (moped).</li>
<li><strong>A1:</strong> silindir hacmi 125 cm³’ü, gücü 11 kW’ı geçmeyen iki tekerlekli motosikletler ve gücü 15 kW’ı geçmeyen üç tekerlekli motosikletler.</li>
<li><strong>A2:</strong> gücü 35 kW’ı geçmeyen iki tekerlekli motosikletler ve gücü 15 kW’ı geçmeyen üç tekerlekli motosikletler.</li>
<li><strong>A:</strong> tüm iki tekerlekli motosikletler ve gücü 15 kW’ı geçen üç tekerlekli motosikletler. Bu üç tekerlekliler için yaş şartı 21’dir. 24 yaşını dolduran adaylarda iki yıllık A2 şartı aranmaz.</li>
<li><strong>B1:</strong> net motor gücü 15 kW’ı ve net ağırlığı 400 kg’ı (yük taşımada 550 kg’ı) geçmeyen dört tekerlekli motosikletler.</li>
<li><strong>B:</strong> otomobil ve kamyonet. Yönetmelikte belirtilen eğitimi tamamlayan ya da sınavı geçen B sahipleri, azami yüklü ağırlığı 4.250 kg’a kadar olan birleşik araçları da kullanabilir.</li>
<li><strong>BE:</strong> B sınıfı araca takılan, azami yüklü ağırlığı 3.500 kg’ı geçmeyen römork veya yarı römorklu birleşik araçlar.</li>
<li><strong>C1E, CE, D1E, DE:</strong> ilgili sınıfın aracına takılan ve azami yüklü ağırlığı 750 kg’ı geçen römorklu birleşik araçlar. C1E’de katar ağırlığı 12.000 kg’ı geçemez.</li>
</ul>

<h2>Bir ehliyetle hangi araçlar da kullanılabilir?</h2>
<p>Karayolları Trafik Yönetmeliği’nin 85. maddesine göre bazı sınıflar, başka sınıfların araçlarını da kapsar:</p>
<ul>
<li>B sınıfı ile M, B1 ve F sınıfı araçlar.</li>
<li>A2 ile M ve A1; A ile M, A1 ve A2 sınıfı araçlar.</li>
<li>C ile M, B, B1, C1 ve F; D ile M, B, B1, D1 ve F sınıfı araçlar.</li>
<li>B, C, C1, D ve D1 sahipleri, azami yüklü ağırlığı 750 kg’a kadar hafif römork takabilir (m.86).</li>
</ul>
<p>B sınıfı ehliyeti en az iki yıllık olanlar, ek eğitim ve sınavla A1 sınıfı motosiklet de kullanabilir. Şartlarını ''' + a('motor', 'B ehliyetle motosiklet') + ''' yazımızda anlattık.</p>

<h2>Sınıfa göre en az direksiyon dersi</h2>
<p>Eğitim alanında veya simülatörde en az 2 saatlik dersten sonra akan trafikte verilecek en az ders saatleri şöyledir (MTSK Yönetmeliği m.7):</p>
<div class="guide-table"><table>
<thead><tr><th>Sınıf</th><th>Akan trafikte en az</th></tr></thead>
<tbody>
<tr><td>M, A1, A2, B1</td><td>12 saat</td></tr>
<tr><td>A (A2 deneyimiyle)</td><td>6 saat</td></tr>
<tr><td>A (24 yaş, deneyimsiz)</td><td>12 saat</td></tr>
<tr><td>B</td><td>14 saat</td></tr>
<tr><td>C1</td><td>10 saat</td></tr>
<tr><td>C</td><td>20 saat</td></tr>
<tr><td>D1</td><td>7 saat</td></tr>
<tr><td>D</td><td>14 saat</td></tr>
<tr><td>BE, C1E, CE, D1E, DE</td><td>6 saat</td></tr>
<tr><td>F</td><td>12 saat</td></tr>
</tbody></table></div>
<p>G dışındaki bu sınıflarda en az 2 saat gece sürüşü zorunludur; sağlık raporunda gece araç kullanamayacağı yazan adaylara gece eğitimi verilmez.</p>

<h2>Sağlık muayenesinde iki grup</h2>
<p>Sağlık muayenesinde sınıflar iki gruba ayrılır. Birinci grup M, A1, A2, A, B1, B, BE ve F; ikinci grup C1, C1E, C, CE, D1, D1E, D, DE ve G sınıflarıdır. İkinci grupta görme şartları daha sıkıdır (Sürücü Sağlık Yönetmeliği m.4 ve m.5).</p>

<h2>Ehliyet kaç yıl geçerlidir?</h2>
<p>M, A1, A2, A, B1, B, BE, F ve G sınıfı ehliyetler 10 yıl; C1, C1E, C, CE, D1, D1E, D ve DE sınıfı ehliyetler 5 yıl geçerlidir (Karayolları Trafik Yönetmeliği m.87).</p>

<h2>Uslu Sürücü Kursu’nda hangi sınıflar var?</h2>
<p>Kursumuzda <a href="/egitim/manuel-b/">B sınıfı manuel</a>, <a href="/egitim/otomatik-b/">B sınıfı otomatik</a>, <a href="/egitim/motor-a1/">A1</a> ve <a href="/egitim/motor-a2/">A2 motosiklet</a> eğitimleri ile <a href="/egitim/diger/">büyük araç ehliyetleri</a> için seçenekler bulunur. Büyük araç seçenekleri hedeflediğiniz sınıfa ve mevcut ehliyetinize göre değişir.</p>
''',
    faq=[
        ('B sınıfı ehliyetle hangi araçlar kullanılır?',
         'B sınıfı ehliyetle otomobil ve kamyonet kullanılır. Karayolları Trafik Yönetmeliği m.85’e göre B sahipleri M (moped), B1 (dört tekerlekli motosiklet) ve F (traktör) sınıfı araçları da kullanabilir.'),
        ('Kamyon ehliyeti için kaç yaşında olmak gerekir?',
         'C1 sınıfı (3.500-7.500 kg kamyon) için 18, C sınıfı için 21 yaşını bitirmiş olmak ve en az B sınıfı ehliyete sahip olmak gerekir.'),
        ('Minibüs ve otobüs ehliyeti kaç yaşında alınır?',
         'Minibüs için D1 sınıfında 21, otobüs için D sınıfında 24 yaş şartı vardır; her ikisi için de en az B sınıfı ehliyet gerekir.'),
        ('A sınıfı motosiklet ehliyeti için A2 şart mı?',
         'A sınıfı için en az iki yıllık A2 ehliyeti gerekir. 24 yaşını doldurmuş adaylarda bu deneyim şartı aranmaz.'),
    ],
    sources=['kty', 'mtsk', 'saglik'],
))

# 3 ─────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='belgeler',
    title='Ehliyet İçin Gerekli Belgeler 2026: Kurs ve Nüfus | Uslu',
    desc='Ankara’da sürücü kursu kaydı için gereken belgeler, sürücü olur raporunun nereden alındığı ve nüfus müdürlüğünde ehliyet başvurusunda istenenler.',
    h1='Ehliyet İçin Gerekli Belgeler',
    crumb='Gerekli Belgeler',
    card='Kurs kaydı, sürücü olur raporu ve nüfus müdürlüğü başvurusu için liste.',
    lead='Ehliyet sürecinde belgeler iki yerde istenir: sürücü kursuna kayıt olurken ve sınavları geçtikten sonra nüfus müdürlüğüne başvururken. Aşağıdaki listeler MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’nin 11. maddesine ve Nüfus ve Vatandaşlık İşleri Genel Müdürlüğünün açıklamalarına dayanır.',
    summary=[
        'Kurs kaydı: kimlik kartı, öğrenim belgesi, biyometrik fotoğraf, sürücü olur raporu ve adli sicil kaydı belgesi.',
        '18 yaşını doldurmamış adaylardan ayrıca veli veya vasi izni istenir.',
        'Sürücü olur raporu aile sağlığı merkezlerinden, devlet ve üniversite hastanelerinden ve muayenehane dışındaki özel sağlık kuruluşlarından alınır.',
        'Nüfus müdürlüğü başvurusunda ayrıca harç, değerli kâğıt bedeli ve vakıf payı ödenir.',
    ],
    body='''
<h2>Sürücü kursuna kayıt için gerekli belgeler</h2>
<p>T.C. vatandaşı adaylardan istenenler:</p>
<ul>
<li>Fotoğraflı T.C. kimlik kartı (kayıtta görülüp geri verilir).</li>
<li>Diploma, diploma yerine geçen belge ya da bir kamu kurumundan alınan öğrenim durumu belgesi. Aslı görülerek kurs tarafından onaylı örneği alınır. En az ilkokul düzeyinde öğrenim gerekir.</li>
<li>Son altı ayda çekilmiş biyometrik fotoğraf. Kursumuzda kayıt için 1 adet yeterlidir.</li>
<li>Sürücü olur raporu.</li>
<li>Ehliyet almaya engel bir sabıka kaydı olmadığını gösteren barkodlu belge. Bu belgeyi e-Devlet’teki adli sicil kaydı hizmetinden alabilirsiniz; Bakanlık ayrıca yetkili adli mercilerden teyit eder.</li>
<li>Başka sınıf ehliyetiniz varsa mevcut ehliyetinizin fotokopisi.</li>
<li>18 yaşını doldurmamış adaylar için veli veya vasi muvafakatnamesi.</li>
</ul>
<p>Gerçeğe aykırı beyanda bulunduğu tespit edilen kursiyerler sınava alınmaz; sınava girmiş olsalar bile sınavları geçersiz sayılır.</p>

<h2>Yabancı uyruklu adaylar için</h2>
<ul>
<li>Pasaportun noter tasdikli Türkçe tercümesi veya geçici koruma kimlik belgesi.</li>
<li>Kayıt tarihinden itibaren Türkiye’de en az altı ay kalacağını gösteren ikamet izni, öğrenim vizesi veya çalışma izni.</li>
<li>Öğrenim belgesinin noter tasdikli Türkçe tercümesi.</li>
<li>Sürücü olur raporu ve son altı ayda çekilmiş biyometrik fotoğraf.</li>
<li>Cumhuriyet başsavcılığı veya kaymakamlıktan alınan adli sicil belgesi.</li>
<li>18 yaşını doldurmamış adaylar için veli veya vasi muvafakatnamesi.</li>
</ul>

<h2>Sürücü olur raporu nereden alınır?</h2>
<p>Muayeneyi; Sağlık Bakanlığına ve üniversitelere bağlı sağlık tesisleri, aile sağlığı merkezleri ve Sağlık Bakanlığınca ruhsatlandırılan muayenehaneler dışındaki özel sağlık kuruluşlarında görevli hekimler yapar (Sürücü Sağlık Yönetmeliği m.4). Hekim gerek görürse sizi ilgili uzmanlık muayenesine yönlendirir.</p>
<ul>
<li><strong>Görme:</strong> birinci grup sınıflarda (M, A1, A2, A, B1, B, BE, F) gözlükle veya gözlüksüz olarak, bir gözün görmesi 0,1’den az olmamak şartıyla iki gözün toplam görme derecesi 1,0 olmalıdır (m.5).</li>
<li><strong>Kısıtlar:</strong> sağlık durumu nedeniyle araç kullanımı bir şarta bağlanırsa, bu şart kod numarasıyla rapora yazılır.</li>
<li><strong>Geçerlilik:</strong> NVİ’ye göre sürücü sağlık raporları 2 yıl geçerlidir.</li>
</ul>

<h2>Nüfus müdürlüğünde ehliyet başvurusu için istenenler</h2>
<p>Sınavları geçtikten sonra ehliyet başvurusunda NVİ şunları ister:</p>
<ul>
<li>Kimlik belgesi.</li>
<li>Sürücü sertifikası.</li>
<li>Öğrenim belgesi.</li>
<li>Sürücü sağlık raporu.</li>
<li>Harç, değerli kâğıt bedeli ve vakıf payının ödendiğini gösteren bilgi.</li>
<li>Son altı ay içinde çekilmiş, ICAO standartlarına uygun biyometrik fotoğraf.</li>
<li>Kan grubunu gösteren belge veya beyan.</li>
<li>Adli sicil kaydı belgesi.</li>
</ul>
<p>2026 tutarları için ''' + a('masraf', 'ehliyet masrafları') + ''' yazımıza bakın. Sürecin tamamını ''' + a('nasil', 'ehliyet nasıl alınır') + ''' yazımızda adım adım anlattık.</p>
''',
    faq=[
        ('Ehliyet kursuna kayıt için hangi belgeler gerekir?',
         'T.C. kimlik kartı, diploma veya öğrenim belgesi, son altı ayda çekilmiş biyometrik fotoğraf, sürücü olur raporu ve ehliyete engel sabıka kaydı olmadığını gösteren barkodlu adli sicil belgesi gerekir. 18 yaşını doldurmamış adaylardan veli veya vasi izni de istenir.'),
        ('Sürücü olur raporunu kimler verir?',
         'Aile sağlığı merkezleri, Sağlık Bakanlığına ve üniversitelere bağlı sağlık tesisleri ile muayenehaneler dışındaki özel sağlık kuruluşlarındaki hekimler sürücü olur raporu düzenleyebilir.'),
        ('Diplomamı kaybettim, kursa kayıt olabilir miyim?',
         'Evet. Yönetmelik diploma yerine geçen belgeyi ya da bir kamu kurumundan alınan öğrenim durumu belgesini de kabul eder.'),
        ('Adli sicil kaydı belgesi nereden alınır?',
         'T.C. vatandaşları barkodlu adli sicil kaydı belgesini e-Devlet’teki Adli Sicil Kaydı Sorgulama hizmetinden alabilir.'),
    ],
    sources=['mtsk', 'saglik', 'nvi_sss', 'adli'],
))

# 4 ─────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='sinav',
    title='Ehliyet Sınavı 2026: e-Sınav ve Direksiyon Sınavı | Uslu',
    desc='Ehliyet e-Sınavı kaç soru, kaç dakika, kaç puanla geçilir? Ankara’da e-Sınav ve direksiyon sınavı nerede, nasıl yapılır? MEB 2026 e-Sınav Kılavuzuna göre.',
    h1='Ehliyet Sınavı Nasıl Yapılır?',
    crumb='Ehliyet Sınavı',
    card='e-Sınav soru sayısı, süre, puan ve direksiyon sınavının aşamaları.',
    lead='Ehliyet için iki sınav vardır: teorik derslerin ölçüldüğü e-Sınav ve akan trafikte yapılan direksiyon sınavı. Bu yazı MEB’in 2026 e-Sınav Kılavuzu ile MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’ne dayanır.',
    summary=[
        'e-Sınav 50 soru ve 45 dakikadır; 70 ve üzeri puan başarılıdır, yanlış cevaplar doğruları götürmez.',
        '2026’da her e-Sınav oturumunun ücreti KDV dahil 1.250 TL’dir.',
        'Direksiyon sınavı hafta sonları 07.00 ile 21.00 arasında, akan trafikte yapılır ve aday başına en az 40 dakika sürer.',
        'B sınıfı direksiyon sınavında geri park, geri gitme, dar alanda dönüş ve ani fren gibi aşamalar vardır.',
    ],
    body='''
<h2>e-Sınav nasıl yapılır?</h2>
<p>e-Sınav, M, A1, A2, A, B1, B, F ve G sınıflarında teorik eğitimini tamamlayan adaylar için yapılır. Sınavda tüm sınıflarda aynı dağılım kullanılır:</p>
<div class="guide-table"><table>
<thead><tr><th>Ders</th><th>Soru</th></tr></thead>
<tbody>
<tr><td>Trafik ve çevre</td><td>23</td></tr>
<tr><td>İlk yardım</td><td>12</td></tr>
<tr><td>Araç tekniği</td><td>9</td></tr>
<tr><td>Trafik adabı</td><td>6</td></tr>
<tr><td><strong>Toplam</strong></td><td><strong>50</strong></td></tr>
</tbody></table></div>
<p>Sınav süresi 45 dakikadır; işitme engelli adaylara 15 dakika ek süre tanınır. Puan, doğru sayısının soru sayısına bölünüp 100 ile çarpılmasıyla hesaplanır; 70 ve üzeri puan alan başarılı sayılır. Tüm soruların puanı eşittir ve yanlış cevaplar doğru cevapları etkilemez. e-Sınav’ı geçen aday direksiyon eğitimine başlama hakkı kazanır.</p>

<h3>Başvuru ve ücret</h3>
<p>Aday, her sınav oturumu için KDV dahil 1.250 TL e-Sınav ücretini MEB Döner Sermaye İşletmesi hesabına Ziraat Bankası, Vakıfbank veya Halkbank üzerinden ya da odeme.meb.gov.tr adresinden tüm banka kartlarıyla öder ve dekontu kursuna teslim eder. Başvuru kurs aracılığıyla yapılır, sınav tarihi ve saati randevu sisteminde belirlenir. Randevu alıp sınava girmeyen aday ücret iadesi isteyemez ve bir sınav hakkını kullanmış sayılır. Belgelenmiş bir mazeret varsa randevu, sınavdan en az 24 saat önce il veya ilçe millî eğitim müdürlüğüne başvurularak değiştirilebilir.</p>

<h3>Sınav günü</h3>
<ul>
<li>Adaylar, kayıtlı oldukları kursun bulunduğu ildeki e-Sınav merkezinde sınava girer. Merkez, bina ve salon bilgisi e-Sınav giriş belgesinde yazar.</li>
<li>Sınav saatinden en geç 30 dakika önce salonda olmanız gerekir.</li>
<li>Yanınızda e-Sınav giriş belgesi ve süresi dolmamış kimlik kartı ya da pasaport bulunmalıdır. Bu belgeler olmadan sınava alınmazsınız.</li>
<li>Cep telefonu, saat, çanta, cüzdan ve elektronik cihazlar sınav binasına alınmaz.</li>
<li>Sonucu sınav merkezindeki sonuç ekranından ya da oturum bittikten sonra esinav.meb.gov.tr adresinden öğrenebilirsiniz.</li>
</ul>

<h2>Direksiyon sınavı nasıl yapılır?</h2>
<p>Direksiyon eğitimini tamamlayan ve kursun sınava girmesini uygun gördüğü aday, sınavdan en az dört iş günü önce sisteme onaylanır. Sınav tarihlerini il veya ilçe millî eğitim müdürlükleri belirler. Sınav, izin alınmış güzergâhta ve akan trafikte yapılır; hafta sonları 07.00 ile 21.00 arasında düzenlenir ve her aday için en az 40 dakika sürer. Değerlendirme, MEB Direksiyon Uygulama Sınav Sistemi’ndeki (MEBDUS) formlara göre yapılır (MTSK Yönetmeliği m.28).</p>

<h3>B sınıfı direksiyon sınavının aşamaları</h3>
<ul>
<li>Araç bilgisini ölçen sorular.</li>
<li>Aracı çalıştırıp hareket ettirme.</li>
<li>Koniler arasına geri park: tek hamlede girilir, giremeyene bir hak daha verilir; araç en fazla iki hamlede, konilere ve kaldırıma değmeden kaldırıma paralel park edilir.</li>
<li>En fazla 3,5 metre genişliğindeki şeritte 25 metre geri gitme.</li>
<li>Geri giderken sağa (L) dönüş ve dar alanda en fazla üç hamlede geri dönüş.</li>
<li>Güzergâhta yol için belirlenen azami hıza ulaşma ve 30 km/s hızla giderken komutla ani fren.</li>
<li>Akan trafikte sürüş becerileri ve trafik algısı.</li>
</ul>

<h3>Motosiklet (A1, A2, A) sınavının aşamaları</h3>
<ul>
<li>Araç bilgisi soruları, ardından sınav alanında dokuz koni arasında slalom.</li>
<li>Yedi metre çapındaki iki çember içinde sekiz çizme ve 20 metrelik denge çizgisi üzerinden geçiş.</li>
<li>Dar alanda (U) dönüş, 30 metrede hızlanıp yavaşlayarak durma, engelden kaçınma ve ani fren.</li>
<li>Alanda başarılı olan adayın sınavı güzergâhta devam eder (MTSK Yönetmeliği m.35).</li>
</ul>
<p>Sınavı geçen aday sertifikasına e-Devlet üzerinden erişir. Kalan adaylar için haklar ''' + a('kalirsam', 'sınavda kalırsam') + ''' yazımızda.</p>
''',
    faq=[
        ('Ehliyet e-Sınavı kaç soru ve kaç dakika?',
         'e-Sınav 50 sorudur ve 45 dakika sürer: 23 trafik ve çevre, 12 ilk yardım, 9 araç tekniği ve 6 trafik adabı sorusu sorulur.'),
        ('Ehliyet sınavı kaç puanla geçilir?',
         'e-Sınavda 100 puan üzerinden 70 ve üzeri puan alan aday başarılı sayılır.'),
        ('e-Sınavda yanlış cevaplar doğruları götürür mü?',
         'Hayır. Puan yalnız doğru cevaplarla hesaplanır: doğru sayısı soru sayısına bölünüp 100 ile çarpılır.'),
        ('Direksiyon sınavı hangi günlerde yapılır?',
         'Yönetmeliğe göre direksiyon sınavları hafta sonları 07.00 ile 21.00 arasında yapılır ve her aday için en az 40 dakika sürer.'),
        ('e-Sınav sonucu nereden öğrenilir?',
         'Sonuç, sınav merkezindeki sonuç ekranından ya da oturum bittikten sonra esinav.meb.gov.tr adresinden öğrenilir.'),
    ],
    sources=['esinav', 'mtsk', 'esinav_site'],
))

# 5 ─────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='masraf',
    title='Ehliyet Masrafları 2026: Harç ve Sınav Ücretleri | Uslu',
    desc='Ankara’da ehliyet masrafları 2026: B sınıfı harç 6.754,60 TL, değerli kâğıt 1.690 TL, vakıf payı 425 TL, e-Sınav 1.250 TL. Kurs ücreti ayrıca öğrenilir.',
    h1='Ehliyet Masrafları 2026',
    crumb='Ehliyet Masrafları',
    card='2026 harç, kart bedeli ve e-Sınav ücreti; kalem kalem hesap.',
    lead='Ehliyet masrafı; devlete ödenen resmî kalemler ile kurs ve sınav süreciyle ilgili kalemlerden oluşur. Bu yazıda yalnız resmî olarak yayımlanan 2026 tutarlarını verdik. Kurs ücreti kurstan kursa ve seçilen eğitime göre değiştiği için ayrıca öğrenilmelidir.',
    summary=[
        'B sınıfı ilk ehliyet için nüfus müdürlüğüne ödenen toplam 8.869,60 TL’dir (harç, değerli kâğıt ve vakıf payı).',
        'e-Sınav ücreti her oturum için KDV dahil 1.250 TL’dir.',
        'Kurs ücreti, direksiyon sınavı ücreti, sağlık raporu ve fotoğraf bu tutarlara dahil değildir.',
        'Yeni tip ehliyet yenilemede ödenen tutar 2.115 TL’dir.',
    ],
    body='''
<h2>Nüfus müdürlüğüne ödenen tutarlar (2026)</h2>
<p>İlk defa ehliyet alırken ve sınıf eklerken, alınan sınıfın harcı ile birlikte değerli kâğıt bedeli (1.690 TL) ve vakıf hizmet bedeli (425 TL) ödenir:</p>
<div class="guide-table"><table>
<thead><tr><th>Sınıf</th><th>Harç</th><th>Toplam</th></tr></thead>
<tbody>
<tr><td>A1, A2, A, F</td><td>2.239,90 TL</td><td>4.354,90 TL</td></tr>
<tr><td>B</td><td>6.754,60 TL</td><td>8.869,60 TL</td></tr>
<tr><td>M, B1, BE, C1, C1E, C, CE, D1, D1E, D, DE, G</td><td>11.271,20 TL</td><td>13.386,20 TL</td></tr>
</tbody></table></div>
<p>Toplam sütunu harca 1.690 TL değerli kâğıt bedeli ile 425 TL vakıf payının eklenmesiyle bulunur. Tutarlar ve ödeme yapılabilecek hesaplar NVİ’nin ücret sayfasında yayımlanır; yıl içinde değişebileceği için ödeme öncesinde kontrol edin.</p>

<h2>Sınav ücretleri</h2>
<ul>
<li><strong>e-Sınav:</strong> her oturum için KDV dahil 1.250 TL. Randevu alıp sınava girmeyen aday ücret iadesi isteyemez; başvurusu onaylanmayan ya da yanlış yatırılan ücretler iade edilir.</li>
<li><strong>Direksiyon sınavı:</strong> sınav ücretlerini her yıl MEB belirler. Güncel tutarı kayıt sırasında kursunuzdan öğrenebilirsiniz.</li>
</ul>

<h2>Diğer kalemler</h2>
<ul>
<li><strong>Kurs ücreti:</strong> teorik ve direksiyon eğitimini kapsar; kursa ve seçtiğiniz eğitime göre değişir.</li>
<li><strong>Ek direksiyon dersi:</strong> kendini yeterli görmeyen kursiyer isterse ek ders alır ve o yıl ilan edilen ders ücreti üzerinden öder. Direksiyon sınavında kalan aday da her sınavdan sonra ilan edilen ders ücretini ödeyip en az 2 saat ders alır (MTSK Yönetmeliği m.7 ve m.15).</li>
<li><strong>Sağlık raporu ve biyometrik fotoğraf:</strong> alındığı yere göre değişir.</li>
</ul>

<h2>Örnek hesap: B sınıfı, sınavlar ilk denemede geçilirse</h2>
<div class="guide-table"><table>
<thead><tr><th>Kalem</th><th>Tutar</th></tr></thead>
<tbody>
<tr><td>B sınıfı harç</td><td>6.754,60 TL</td></tr>
<tr><td>Değerli kâğıt bedeli</td><td>1.690,00 TL</td></tr>
<tr><td>Vakıf hizmet bedeli</td><td>425,00 TL</td></tr>
<tr><td>e-Sınav (1 oturum)</td><td>1.250,00 TL</td></tr>
<tr><td><strong>Resmî kalemler toplamı</strong></td><td><strong>10.119,60 TL</strong></td></tr>
</tbody></table></div>
<p>Bu toplama kurs ücreti, direksiyon sınavı ücreti, sağlık raporu ve fotoğraf dahil değildir. Her tekrar e-Sınav oturumu 1.250 TL ekler.</p>

<h2>Ehliyet yenileme ücreti</h2>
<p>2016 sonrası verilen yeni tip ehliyetlerin yenilenmesinde 1.690 TL değerli kâğıt bedeli ve 425 TL vakıf payı olmak üzere toplam 2.115 TL ödenir.</p>

<h2>Uslu Sürücü Kursu ücreti</h2>
<p>Kurs ücretimiz seçtiğiniz eğitime göre değişir; sabit bir liste yayımlamıyoruz. Güncel ücret ve ödeme seçenekleri için <a href="tel:+905320685647">0532 068 56 47</a> numarasını arayabilir ya da <a href="/iletisim/">iletişim sayfamızdan</a> teklif isteyebilirsiniz.</p>
''',
    faq=[
        ('2026’da B sınıfı ehliyet harcı ne kadar?',
         'NVİ’nin 2026 tarifesine göre B sınıfı harcı 6.754,60 TL’dir. Buna 1.690 TL değerli kâğıt bedeli ve 425 TL vakıf payı eklenince toplam 8.869,60 TL olur.'),
        ('Motosiklet ehliyeti harcı ne kadar?',
         'A1, A2 ve A sınıfları için 2026 harcı 2.239,90 TL’dir; değerli kâğıt bedeli ve vakıf payıyla toplam 4.354,90 TL ödenir.'),
        ('e-Sınav ücreti ne kadar?',
         '2026 MEB e-Sınav Kılavuzuna göre her sınav oturumu için KDV dahil 1.250 TL’dir.'),
        ('Ehliyet yenileme ücreti ne kadar?',
         'Yeni tip ehliyetlerin yenilenmesinde 2026 yılında toplam 2.115 TL (1.690 TL değerli kâğıt bedeli ve 425 TL vakıf payı) ödenir.'),
    ],
    sources=['nvi_ucret', 'esinav', 'mtsk'],
))

# 6 ─────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='otomatik',
    title='Otomatik Vites Ehliyet: Kısıtlama ve Manuele Geçiş | Uslu',
    desc='Otomatik vitesli araçla ehliyet alanlar yalnız otomatik araç kullanabilir. Manuele geçiş için gereken ders ve sınav, sınav sırasında vites değişikliği. Yönetmelikle.',
    h1='Otomatik Vites Ehliyet Nedir?',
    crumb='Otomatik Vites Ehliyet',
    card='Otomatik ehliyetin kısıtı ve sonradan manuele geçişin şartları.',
    lead='Otomatik vitesli araçla eğitim alıp sınavı geçmek mümkündür. Ancak bu yolun, ehliyetinizle hangi araçları kullanabileceğinizi belirleyen bir sonucu vardır. Aşağıdaki bilgiler MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’nin 6, 15 ve 39. maddelerine dayanır.',
    summary=[
        'Otomatik vitesli araçla eğitim alıp sınavı geçenlerin sertifikasında yalnız otomatik araç kullanabilecekleri belirtilir.',
        'Sonradan manuel araç kullanmak için sınıfınızın direksiyon eğitiminin yarısına devam edip direksiyon sınavını geçmeniz gerekir.',
        'İlk dört sınav hakkını kullanan aday, ikinci dört hakta vites türünü değiştirebilir.',
        'Manuel vitesli araçla alınan ehliyette böyle bir kısıt yoktur.',
    ],
    body='''
<h2>Otomatik ehliyetin kısıtı</h2>
<p>Yönetmeliğe göre bir sertifika sınıfına ait aracın otomatik şanzımanlı olanıyla eğitim alıp sınavda başarılı olanların sertifikasında, yalnız otomatik araç kullanabilecekleri belirtilir (m.6/2). Sertifika bilgileri ehliyetinize esas olduğu için bu kısıt ehliyetinize de yansır. Manuel vitesli araçla alınan ehliyette böyle bir kısıt bulunmaz.</p>

<h2>Eğitim ve sınav farkı</h2>
<p>Teorik dersler ve e-Sınav her iki yolda aynıdır. Yönetmelik en az direksiyon ders saatlerini sınıfa göre belirler; B sınıfında akan trafikte en az 14 saattir ve manuel ile otomatik için ayrı süre öngörmez. Direksiyon sınavının aşamaları da aynıdır; fark, eğitimin ve sınavın otomatik şanzımanlı araçla yapılmasıdır.</p>

<h2>Sonradan manuele geçiş</h2>
<p>Ehliyetinde veya sertifikasında yalnız otomatik araç kullanabileceği yazanlar, kendi sınıflarının manuel vitesli aracını kullanmak üzere sertifika alabilmek için direksiyon eğitimi dersinin yarısına devam eder (m.39/2). Kursun sınava girmesini uygun görmesiyle direksiyon sınavına alınır; başarılı olanlara ilgili sertifika verilir (m.39/3). NVİ’ye göre aynı sınıfın manuel sertifikasını getirenlerden ehliyet değişiminde harç alınmaz; yalnız değerli kâğıt bedeli ve vakıf payı ödenir.</p>
<p>Yönetmelikte bu konuda bir ayrıntı daha vardır: C1, C, D1 veya D sertifikasını manuel vitesli araçla alanlar, M, A1, A2 ve A dışındaki diğer manuel şanzımanlı araçları da kullanabilir.</p>

<h2>Sınav sürecinde vites türünü değiştirmek</h2>
<p>İlk dört direksiyon sınavı hakkının bir kısmını veya tamamını manuel araçta kullanan aday, isterse kalan haklarından vazgeçerek ikinci dört sınav hakkında aynı sınıfın otomatik şanzımanlı sertifikası için otomatik araç kullanabilir. Tersi de mümkündür: otomatikte başlayan aday ikinci dört hakta manuele geçebilir (m.15/6). Sınav hakları için ''' + a('kalirsam', 'sınavda kalırsam') + ''' yazımıza bakın.</p>

<h2>Hangisini seçmeli?</h2>
<p>Karar, kullanacağınız araca bağlıdır. Yalnız otomatik vitesli araç kullanacaksanız otomatik eğitim işinizi görür; manuel araç kullanma ihtimaliniz varsa manuel eğitim, sonradan ek ders ve sınav gerektirmez. Kursumuzda <a href="/egitim/otomatik-b/">B sınıfı otomatik ehliyet</a> ve <a href="/egitim/manuel-b/">B sınıfı manuel ehliyet</a> eğitimleri verilir.</p>
''',
    faq=[
        ('Otomatik ehliyetle manuel araç kullanılır mı?',
         'Hayır. Otomatik vitesli araçla eğitim alıp sınavı geçenlerin sertifikasında yalnız otomatik araç kullanabilecekleri belirtilir.'),
        ('Otomatik ehliyeti manuele çevirmek için ne gerekir?',
         'Yönetmeliğe göre kendi sınıfınızın direksiyon eğitimi dersinin yarısına devam etmeniz ve direksiyon sınavında başarılı olmanız gerekir.'),
        ('Otomatik ehliyet için ders saati daha mı az?',
         'Hayır. Yönetmelik en az direksiyon ders saatini sınıfa göre belirler; B sınıfında akan trafikte en az 14 saattir ve manuel ile otomatik için ayrı süre yoktur.'),
        ('Manuel ehliyetle otomatik araç kullanılır mı?',
         'Evet. Yalnız otomatik araç kısıtı, otomatik şanzımanlı araçla eğitim alıp sınavı geçenlerin sertifikasına yazılır; manuel araçla alınan ehliyette bu kısıt yoktur.'),
    ],
    sources=['mtsk', 'nvi_sss'],
))

# 7 ─────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='kalirsam',
    title='Ehliyet Sınavında Kalırsam Ne Olur? Sınav Hakları | Uslu',
    desc='e-Sınavda kalan aday kursa yeniden devam etmeden 3 kez daha sınava girebilir. Direksiyon sınavında kalanlar için ek ders, 4+4 sınav hakkı ve mazeret kuralları.',
    h1='Ehliyet Sınavında Kalınca Ne Olur?',
    crumb='Sınavda Kalırsam',
    card='e-Sınav ve direksiyon sınavında kaç hak var, sonra ne yapılır.',
    lead='Ehliyet sınavında kalmak süreci bitirmez; yönetmelik hem e-Sınav hem direksiyon sınavı için tekrar hakları tanır. Aşağıdaki bilgiler MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’nin 15. maddesine ve 2026 e-Sınav Kılavuzuna dayanır.',
    summary=[
        'e-Sınavda kalan aday, kursa yeniden devam etmeden ve kurs ücreti ödemeden, yalnız sınav ücretiyle aralıksız üç kez daha sınava girebilir.',
        'Direksiyon sınavında kalan aday, her sınavdan sonra ilan edilen ders ücretini ödeyip en az 2 saat ders alarak üç sınav dönemi daha girer.',
        'Dört direksiyon sınavında da kalan aday, 60 gün içinde başvurup sınıfının ders saatini yeniden alarak dört hak daha kazanır.',
        'Teorik sınavı geçmiş aday, üç yıl içinde yeniden kayıt yaptırırsa teorik eğitim ve sınavdan muaf sayılır.',
    ],
    body='''
<h2>e-Sınavda kalırsanız</h2>
<p>Teorik sınavda başarısız olan aday, teorik derslere yeniden devam etmeden ve kurs ücreti ödemeden, yalnız sınav ücretini ödeyerek aralıksız üç kez daha e-Sınav’a girebilir. Böylece toplam dört hak olur. Her oturumun ücreti 2026 yılında KDV dahil 1.250 TL’dir.</p>
<ul>
<li>Son sınav hakkı için randevu alma süresi, kursa kayıt olunan dönemin grup başlama tarihinden itibaren 90 günü geçmeyecek şekilde planlanır.</li>
<li>Randevu alınan sınava gelmeyen aday bir sınav hakkını kullanmış sayılır.</li>
<li>Belirlenen sürede sınavlara mazeretsiz katılmayan ya da haklarını başarısız tamamlayan aday kursa yeniden kayıt yaptırabilir.</li>
</ul>

<h2>Direksiyon sınavında kalırsanız</h2>
<p>Direksiyon sınavında başarısız olan aday, her başarısız sınavdan sonra kayıtlı olduğu kursun ilan ettiği ders ücretini ödeyip en az 2 saat direksiyon dersi alarak aralıksız üç sınav dönemi daha sınava girer. Böylece ilk dört hak kullanılmış olur.</p>
<h3>Dört sınavda da kalırsanız</h3>
<p>Teorik sınavı geçip dört direksiyon sınavında da başarısız olan aday, isterse son sınav sonucunun açıklandığı tarihten itibaren en geç 60 gün içinde, aynı kursta ya da nakil olacağı kursta, ilan edilen direksiyon ders ücretini ödeyip sınıfı için belirlenen direksiyon ders saatini yeniden alarak dört sınav hakkı daha kazanır.</p>
<h3>İkinci dört hak da biterse</h3>
<p>İkinci dört hakkın sonunda da başarısız olan aday, kayıt işlemlerini tamamlayıp ücretini ödeyerek kursa yeniden kayıt yaptırabilir. Teorik sınavı geçmiş olan aday, son girdiği sınav tarihinden itibaren üç yıl içinde yeniden kayıt yaptırırsa teorik eğitim ve sınavdan muaf sayılır.</p>
<h3>Vites türünü değiştirmek</h3>
<p>İlk dört hakta manuel araç kullanan aday ikinci dört hakta otomatik araca, otomatikte başlayan aday da manuele geçebilir. Ayrıntılar ''' + a('otomatik', 'otomatik vites ehliyet') + ''' yazımızda.</p>

<h2>Mazeretiniz varsa</h2>
<ul>
<li><strong>Hastalık:</strong> sınav günü sınava girecek durumda olmadığını sağlık kuruluşundan alacağı raporla belgeleyen aday, raporu en geç 2 iş günü içinde kursa teslim etmelidir.</li>
<li><strong>Afet, yakınların ağır hastalığı veya ölümü, ülkeyi temsil:</strong> resmî belge 10 gün içinde kursa teslim edilir.</li>
<li>Bu iki durumda mazereti kabul edilen aday, dört dönem sınav hakkını tamamlayıp başarılı olamazsa bir defaya mahsus mazeret sınavına girebilir.</li>
<li><strong>Askerlik, hamilelik ve doğum, uzun süren tedavi:</strong> belgeyle yazılı başvuruda kayıt dondurulur, kalan sınav hakları sonra ilçede yapılan ilk sınavdan itibaren kullandırılır.</li>
<li>Randevusu onaylanan e-Sınav, belgelenmiş mazeretle sınavdan en az 24 saat önce il veya ilçe millî eğitim müdürlüğüne başvurularak değiştirilebilir.</li>
</ul>
<p>Sınavların nasıl yapıldığını ''' + a('sinav', 'ehliyet sınavı') + ''' yazımızda anlattık.</p>
''',
    faq=[
        ('Ehliyet e-Sınavında kaç hak var?',
         'İlk sınavla birlikte dört hak vardır. e-Sınavda kalan aday, kursa yeniden devam etmeden ve yalnız sınav ücretini ödeyerek aralıksız üç kez daha sınava girebilir.'),
        ('Direksiyon sınavında kalınca ne yapılır?',
         'Aday, kayıtlı olduğu kursun ilan ettiği ders ücretini ödeyip en az 2 saat direksiyon dersi alır ve sonraki sınav dönemine girer. İlk dört hak böyle kullanılır.'),
        ('Direksiyon sınavında dört kez kalırsam ne olur?',
         'Son sınav sonucunun açıklanmasından itibaren en geç 60 gün içinde başvurup ilan edilen ders ücretini ödeyerek ve sınıfınızın direksiyon ders saatini yeniden alarak dört sınav hakkı daha kazanırsınız.'),
        ('Sınav haklarım biterse teorik derslere yeniden girer miyim?',
         'Teorik sınavı geçmişseniz, son girdiğiniz sınav tarihinden itibaren üç yıl içinde kursa yeniden kayıt yaptırdığınızda teorik eğitim ve sınavdan muaf sayılırsınız.'),
    ],
    sources=['mtsk', 'esinav'],
))

# 8 ─────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='motor',
    title='B Ehliyetle 125 cc Motosiklet (A1) Kullanmak: Şartlar | Uslu',
    desc='En az iki yıllık B ehliyeti olanlar ek direksiyon eğitimi ve uygulama sınavıyla A1 sınıfı motosiklet kullanabilir. Şartlar, eğitim süresi ve sınırlar.',
    h1='B Ehliyetle Motosiklet Kullanılır mı?',
    crumb='B Ehliyetle Motosiklet',
    card='İki yıllık B ehliyetiyle A1 motosiklet kullanmanın şartları ve sınırları.',
    lead='2024’te Karayolları Trafik Yönetmeliği’ne eklenen bir fıkrayla, en az iki yıllık B sınıfı ehliyeti olan sürücülerin ek eğitim ve sınavla A1 sınıfı motosiklet kullanmasının yolu açıldı. Aşağıdaki bilgiler bu düzenlemeye (m.85/2) ve MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’nin 39. maddesine dayanır.',
    summary=[
        'En az iki yıllık B ehliyeti, iki tekerlekli araç için aranan sağlık şartları ve son beş yılda ehliyetin geri alınmamış olması gerekir.',
        'A1 sınıfı için öngörülen direksiyon eğitiminin yarısı alınır ve uygulama sınavı geçilir.',
        'Ticari faaliyette kullanılan motosikletler bu yetkinin dışındadır; yetki yalnız Türkiye sınırları içinde geçerlidir.',
        'Yetki sistem kaydına işlenir, ehliyetin üzerine ayrıca kod yazılmaz.',
    ],
    body='''
<h2>Kimler başvurabilir?</h2>
<p>B sınıfı ehliyeti olan sürücü, şu şartların hepsini taşıyorsa bu yoldan yararlanabilir (Karayolları Trafik Yönetmeliği m.85/2):</p>
<ul>
<li>En az iki yıllık geçerli B sınıfı ehliyete sahip olmak.</li>
<li>Sürücü Sağlık Yönetmeliği’nde iki tekerlekli araç kullanacaklar için aranan sağlık şartlarını taşımak.</li>
<li>Başvuru tarihinden geriye doğru beş yıl içinde ehliyeti geçici ya da sürekli olarak geri alınmamış olmak.</li>
</ul>

<h2>Eğitim ve sınav</h2>
<p>Bu şartları taşıyan adaya, A1 sınıfı için yönetmelikte öngörülen direksiyon eğitim saatinin yarısı kadar eğitim verilir. A1 için akan trafikte en az 12 saat öngörüldüğünden bu yolda eğitim bunun yarısı kadardır. Uygulama sınavında başarılı olan adaya A1 sınıfı sertifika verilir (MTSK Yönetmeliği m.39/5). Motosiklet sınavının aşamalarını ''' + a('sinav', 'ehliyet sınavı') + ''' yazımızda anlattık.</p>

<h2>Yetkinin sınırları</h2>
<ul>
<li>Her türlü ticari faaliyette kullanılan motosikletler bu yetkinin dışındadır.</li>
<li>Yetki yalnız Türkiye sınırları içinde geçerlidir.</li>
<li>MEB’in düzenlediği A1 sertifikası ehliyet sistem kayıtlarına işlenir; ehliyetin üzerine ayrıca kod yazılmaz. Sürücü isterse iki yıl içinde sertifikasını ehliyetine işletebilir.</li>
<li>Şartlardan biri kaybedilirse ya da ehliyet geçici veya sürekli olarak geri alınırsa bu yetki başka bir işleme gerek kalmadan iptal edilir.</li>
</ul>

<h2>Tam A1 ehliyeti ile farkı</h2>
<p>A1 sınıfı ehliyeti ayrıca almak isteyenler için ticari kullanım ve yurt dışı sınırları söz konusu değildir; bu durumda A1 sınıfının normal eğitim ve sınav süreci izlenir. Sınıfların kapsamı için ''' + a('siniflar', 'ehliyet sınıfları') + ''' yazımıza bakın. Kursumuzda <a href="/egitim/motor-a1/">A1 motosiklet</a> ve <a href="/egitim/motor-a2/">A2 motosiklet</a> eğitimleri verilir.</p>
''',
    faq=[
        ('B ehliyetle 125 cc motosiklet kullanılır mı?',
         'Doğrudan kullanılamaz. En az iki yıllık B ehliyeti olan, sağlık şartlarını taşıyan ve son beş yılda ehliyeti geri alınmamış sürücüler, A1 sınıfı için öngörülen direksiyon eğitiminin yarısını alıp uygulama sınavını geçerse A1 sınıfı motosiklet kullanabilir.'),
        ('Bu yetkiyle motokurye olarak çalışabilir miyim?',
         'Hayır. Her türlü ticari faaliyette kullanılan motosikletler bu yetkinin dışındadır.'),
        ('Bu yetki yurt dışında geçerli mi?',
         'Hayır. Yönetmelik bu yetkiyi yalnız Türkiye sınırları içinde tanır.'),
        ('Ehliyetimin üzerine bir şey yazılır mı?',
         'Yetki ehliyet sistem kayıtlarına işlenir, ehliyetin üzerine ayrıca kod yazılmaz. İsterseniz iki yıl içinde sertifikanızı ehliyetinize işletebilirsiniz.'),
    ],
    sources=['kty', 'mtsk', 'saglik'],
))

# 9 ─────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='korku',
    title='Ehliyetim Var Ama Araba Kullanamıyorum: Ne Yapmalı? | Uslu',
    desc='Ehliyeti olup trafiğe çıkmaya çekinenler sürücü kursunda ihtiyaç kadar direksiyon dersi alabilir. Yönetmelikteki hak, derslerin işleyişi ve pratik öneriler.',
    h1='Ehliyeti Olanlara Direksiyon Dersi',
    crumb='Ehliyetim Var',
    card='Ehliyeti olup trafiğe çıkmaya çekinenler için direksiyon eğitimi.',
    lead='Ehliyeti olduğu hâlde uzun süre araç kullanmamış ya da trafiğe çıkmaya çekinen çok sayıda sürücü var. Yönetmelik bu durumdakiler için sürücü kursunda eğitim almanın yolunu açık bırakır.',
    summary=[
        'Ehliyeti olup kendini her koşulda yeterli görmeyen sürücü, ehliyetiyle sürücü kursuna kayıt olabilir.',
        'Bu kursiyerlere trafik adabı dersi ve ihtiyaç duyduğu kadar direksiyon dersi verilir.',
        'Dersler kursun kayıtlı direksiyon eğitim ve sınav araçlarıyla yapılır.',
    ],
    body='''
<h2>Yönetmelik ne diyor?</h2>
<p>MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’ne göre ehliyeti olup her koşulda araç kullanma konusunda kendini yeterli görmeyen ve kursa başvuran kişilerin kaydı ehliyetleriyle yapılır. Bu kursiyerlere trafik adabı dersi ile ihtiyaç duydukları kadar direksiyon dersi verilir. Eğitimler kursun kayıtlı direksiyon eğitim ve sınav araçlarıyla verilir ve sisteme işlenir (m.6/4).</p>

<h2>Derslerde nelere çalışılabilir?</h2>
<p>Ders planı, eksik hissettiğiniz konuya göre kurulur. Sık çalışılan başlıklar:</p>
<ul>
<li>Kalkış, duruş ve yokuşta kalkış gibi temel araç kontrolü.</li>
<li>Paralel park, geri manevra ve dar alanda dönüş.</li>
<li>Kavşaklar, şerit değiştirme ve yoğun şehir trafiği.</li>
<li>Şehirlerarası yol ve yüksek hızda güvenli takip mesafesi.</li>
<li>Gece sürüşü ve kötü hava koşulları.</li>
</ul>

<h2>Birkaç pratik öneri</h2>
<ul>
<li>İlk derslerde trafiğin sakin olduğu saatleri seçmek, özgüveni hızlı toplar.</li>
<li>Her dersten sonra zorlandığınız durumu not edin; bir sonraki ders buna ayrılabilir.</li>
<li>Kullanacağınız araç otomatikse dersleri de otomatik araçla almak geçişi kolaylaştırır. Vites türüyle ilgili kurallar için ''' + a('otomatik', 'otomatik vites ehliyet') + ''' yazımıza bakın.</li>
</ul>

<h2>Uslu Sürücü Kursu’nda</h2>
<p>Trafiğe yeniden çıkış, park ve araç kontrolünü pekiştirmek isteyenler için <a href="/egitim/ozel/">özel direksiyon dersi</a> veriyoruz. Ders planını mevcut deneyiminizi ve hedeflerinizi konuşarak birlikte oluşturabiliriz.</p>
''',
    faq=[
        ('Ehliyeti olan biri sürücü kursuna kayıt olabilir mi?',
         'Evet. Yönetmeliğe göre ehliyeti olup kendini her koşulda yeterli görmeyen kişiler ehliyetleriyle kursa kayıt olabilir ve ihtiyaç duydukları kadar direksiyon dersi alabilir.'),
        ('Kaç saat direksiyon dersi almam gerekir?',
         'Sabit bir süre yoktur. Yönetmelik, bu durumdaki kursiyerlere ihtiyaç duydukları kadar direksiyon dersi verilmesini öngörür.'),
        ('Dersler kendi aracımla yapılabilir mi?',
         'Yönetmeliğe göre bu eğitimler kursun kayıtlı direksiyon eğitim ve sınav araçlarıyla verilir.'),
    ],
    sources=['mtsk'],
))

# 10 ────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='sincan',
    title='Sincan’da Ehliyet Almak: Kayıt, Ders ve Sınav | Uslu',
    desc='Ehliyet almak için gerekli adımlar: sağlık raporu, kurs kaydı, teorik ders, e-Sınav, direksiyon dersi ve sınavı, başvuru. Sincan’da her adım nerede yapılır.',
    h1='Ehliyet Almak İçin Gerekli Adımlar',
    crumb='Gerekli Adımlar',
    card='Kayıttan ehliyete kadar her adım ve Sincan’da nerede yapıldığı.',
    lead='Sincan’da oturuyor ya da çalışıyorsanız ehliyet sürecinin adımlarını büyük ölçüde ilçe içinde tamamlayabilirsiniz. Aşağıda her adımın nerede yapıldığını ve Uslu Sürücü Kursu’nda nasıl işlediğini özetledik.',
    summary=[
        'Kayıt ve teorik dersler: Atatürk Mah. Atatürk Cd. No:2/17 (2. Noterin üst katı), Sincan.',
        'e-Sınav: Ankara’daki e-Sınav merkezlerinde; merkez bilgisi giriş belgesinde yazar.',
        'Direksiyon dersleri: OSB Törekent parkurunda.',
        'Ehliyet başvurusu: randevuyla yetkili nüfus müdürlüklerinden birine; belge PTT ile adrese gelir.',
    ],
    body='''
<h2>1. Rapor ve belgeler</h2>
<p>Sürücü olur raporunu aile sağlığı merkezinizden ya da hastanelerden alabilirsiniz. Adli sicil kaydı belgesini e-Devlet’ten alırsınız. Kayıtta istenen tüm belgeler ''' + a('belgeler', 'ehliyet için gerekli belgeler') + ''' yazımızda.</p>

<h2>2. Kayıt ve teorik dersler</h2>
<p>Kursumuz Atatürk Mah. Atatürk Cd. No:2/17 (2. Noterin üst katı), 06936 Sincan/Ankara adresindedir. Teorik dersler kurs sınıflarımızda yapılır; sınıflarımızı <a href="/galeri/siniflar/">galeride</a> görebilirsiniz. Pazartesi-Perşembe 09.00-19.30, Cuma-Pazar 09.00-20.30 arasında açığız.</p>

<h2>3. e-Sınav</h2>
<p>MEB’in 2026 kılavuzuna göre adaylar, kayıtlı oldukları kursun bulunduğu ildeki e-Sınav merkezlerinde sınava girer. Sincan’daki bir kursa kayıtlı adaylar için bu, Ankara’daki e-Sınav merkezleri demektir. Hangi merkezde, binada ve salonda sınava gireceğiniz e-Sınav giriş belgenizde yazar. Sınavın ayrıntıları ''' + a('sinav', 'ehliyet sınavı') + ''' yazımızda.</p>

<h2>4. Direksiyon dersleri</h2>
<p>Kursumuzun direksiyon dersleri OSB Törekent parkurunda yapılır. Eğitim alanındaki derslerin ardından akan trafikte devam edilir; B sınıfında akan trafikte en az 14 saat ders alınır ve bunun en az 2 saati gece sürüşüdür. Eğitim araçlarımızı <a href="/galeri/araclar/">galeride</a> görebilirsiniz.</p>

<h2>5. Direksiyon sınavı</h2>
<p>Sınav tarihlerini il veya ilçe millî eğitim müdürlükleri belirler. Sınav, izin alınmış güzergâhta ve akan trafikte, hafta sonları 07.00 ile 21.00 arasında yapılır.</p>

<h2>6. Ehliyet başvurusu</h2>
<p>Sınavları geçince sertifikanız e-Devlet’te görünür. Ehliyet için randevu.nvi.gov.tr, e-Devlet, NVİ Mobil veya Alo 199 üzerinden randevu alıp yetkili nüfus müdürlüklerinden birine başvurursunuz; belge PTT ile ücretsiz olarak adresinize gönderilir. Ödenecek tutarlar ''' + a('masraf', 'ehliyet masrafları') + ''' yazımızda.</p>

<h2>İletişim</h2>
<ul>
<li>Adres: Atatürk Mah. Atatürk Cd. No:2/17 (2. Noterin üst katı), 06936 Sincan/Ankara. <a href="https://g.co/kgs/MfyA3BT" rel="noopener noreferrer" target="_blank">Haritada yol tarifi</a></li>
<li>Telefon ve WhatsApp: <a href="tel:+905320685647">0532 068 56 47</a></li>
<li>Çalışma saatleri: Pazartesi-Perşembe 09.00-19.30, Cuma-Pazar 09.00-20.30</li>
</ul>
''',
    faq=[
        ('Sincan’da e-Sınav nerede yapılır?',
         'MEB kılavuzuna göre adaylar, kayıtlı oldukları kursun bulunduğu ildeki e-Sınav merkezlerinde sınava girer. Sincan’daki kursa kayıtlı adaylar Ankara’daki e-Sınav merkezlerinde sınava girer; merkez, bina ve salon bilgisi e-Sınav giriş belgesinde yazar.'),
        ('Uslu Sürücü Kursu’nda direksiyon dersleri nerede yapılır?',
         'Direksiyon derslerimiz OSB Törekent parkurunda yapılır; eğitim alanındaki derslerin ardından akan trafikte devam edilir.'),
        ('Uslu Sürücü Kursu nerede?',
         'Atatürk Mah. Atatürk Cd. No:2/17 (2. Noterin üst katı), 06936 Sincan/Ankara adresindeyiz.'),
        ('Kurs hangi saatlerde açık?',
         'Pazartesi-Perşembe 09.00-19.30, Cuma-Pazar 09.00-20.30 arasında açığız.'),
    ],
    sources=['esinav', 'mtsk', 'nvi_sss'],
))

# 11 ────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='yenileme',
    title='Ehliyet Yenileme 2026: Ücret, Belgeler ve Süre | Uslu',
    desc='Ankara’da ehliyet yenileme: kaç yılda yenilenir, 2026 ücreti ne kadar, hangi belgeler gerekir? Süresi dolan ehliyetin cezası ve eski tip belgeler.',
    h1='Ehliyet Nasıl Yenilenir? 2026 Ücreti',
    crumb='Ehliyet Yenileme',
    card='Süresi dolan ehliyet, 2026 yenileme ücreti ve gereken belgeler.',
    lead='Yeni tip ehliyetler süreli verilir ve süre dolunca nüfus müdürlüğünden yenilenir. 2016’da verilen ilk yeni tip B sınıfı ehliyetlerin süresi 2026 başında dolduğu için bu konu bu yıl sık soruluyor. Bilgiler NVİ açıklamalarına ve Karayolları Trafik Kanunu’na dayanır.',
    summary=[
        'M, A1, A2, A, B1, B, BE, F ve G sınıfı ehliyetler 10 yıl; C1, C1E, C, CE, D1, D1E, D ve DE sınıfı ehliyetler 5 yıl geçerlidir.',
        '2026’da yenileme bedeli 2.115 TL’dir (1.690 TL değerli kâğıt bedeli ve 425 TL vakıf payı); yenilemede harç alınmaz.',
        'Süresi dolan ehliyetle araç kullanana 2026’da 4.712 TL idari para cezası uygulanır ve ehliyet geri alınır.',
    ],
    body='''
<h2>Ehliyet ne zaman yenilenir?</h2>
<p>NVİ’ye göre ehliyet, geçerlilik süresinin bitimini izleyen tarihten itibaren geçersiz sayılır. Süre, yenileme başvurusuyla uzatılır. 01.01.2016’da düzenlenen B sınıfı yeni tip ehliyetler 01.01.2026 itibarıyla geçerliliğini kaybetmiştir. Ehliyetinizin ne zaman sona erdiği kartın üzerinde yazar.</p>

<h2>Yenileme için gerekli belgeler</h2>
<ul>
<li>Kimlik belgesi.</li>
<li>Kayıp veya çalıntı değilse mevcut ehliyet.</li>
<li>Sürücü sağlık raporu.</li>
<li>Son altı ay içinde çekilmiş 1 adet biyometrik fotoğraf.</li>
<li>Kan grubunu gösteren belge veya beyan.</li>
<li>Adli sicil kaydı ile değerli kâğıt bedeli ve vakıf payı ödemesi (bunlar sistemden kontrol edilir).</li>
</ul>
<p>Sağlık raporunun nereden alındığını ''' + a('rapor', 'sürücü olur raporu') + ''' yazımızda anlattık.</p>

<h2>Yenileme ücreti</h2>
<p>2026 yılında yenileme bedeli 1.690 TL değerli kâğıt bedeli ve 425 TL vakıf payı olmak üzere toplam 2.115 TL’dir. Karayolları Trafik Kanunu’nun 39. maddesine göre süresi dolduğu için yenilenen ehliyetlerden harç alınmaz.</p>

<h2>Süresi dolan ehliyetle araç kullanmak</h2>
<p>Geçerlilik süresi biten ehliyetle araç kullanana Karayolları Trafik Kanunu’nun 39/3 maddesi uyarınca işlem yapılır. NVİ’ye göre 2026 yılında bu ceza 4.712 TL’dir ve ehliyet geri alınır.</p>

<h2>Eski tip (2016 öncesi) ehliyetler</h2>
<p>NVİ’ye göre eski tip ehliyetler Kasım 2025 itibarıyla geçerliliğini kaybetmiştir ve bu belgelerle araç kullananların ehliyeti geri alınır. Eski tip ehliyetler; sınıfa ait o yılın harcı, indirimsiz değerli kâğıt bedeli ve vakıf payı ödenerek herhangi bir il veya ilçe nüfus müdürlüğünde ya da yurt dışında dış temsilciliklerde yenilenir.</p>
<p>Başvuru randevuyla yapılır; ayrıntılar ''' + a('randevu', 'ehliyet randevusu') + ''' yazımızda.</p>
''',
    faq=[
        ('2026’da ehliyet yenileme ücreti ne kadar?',
         'NVİ’ye göre 2026 yılında yeni tip ehliyet yenileme bedeli 1.690 TL değerli kâğıt bedeli ve 425 TL vakıf payı olmak üzere toplam 2.115 TL’dir.'),
        ('Ehliyet yenilemek için sağlık raporu gerekir mi?',
         'Evet. NVİ, yenileme başvurusunda istenen belgeler arasında sürücü sağlık raporunu sayar.'),
        ('Süresi dolan ehliyetle araç kullanılırsa ne olur?',
         'Karayolları Trafik Kanunu’nun 39/3 maddesi uyarınca işlem yapılır; NVİ’ye göre 2026 yılında 4.712 TL idari para cezası uygulanır ve ehliyet geri alınır.'),
    ],
    sources=['nvi_sss', 'nvi_ucret', 'ktk', 'kty'],
))

# 12 ────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='kayip',
    title='Kayıp veya Çalıntı Ehliyet: Yenileme ve Ücret | Uslu',
    desc='Kayıp veya çalıntı ehliyet nasıl yenilenir, ücret ödenir mi, hangi belgeler gerekir? Ad soyad değişikliği ve dağıtımda kaybolan belgeler için NVİ bilgileri.',
    h1='Ehliyet Kaybolursa Ne Yapılır?',
    crumb='Kayıp Ehliyet',
    card='Kaybolan, çalınan ya da bilgisi değişen ehliyet nasıl yenilenir.',
    lead='Ehliyetiniz kaybolduysa, çalındıysa ya da üzerindeki bilgiler değiştiyse süresi dolmadan da yenilenir. Başvuru, diğer ehliyet işlemleri gibi nüfus müdürlüğüne randevuyla yapılır. Bilgiler NVİ açıklamalarına dayanır.',
    summary=[
        'Kayıp veya çalıntı ehliyet, randevuyla yetkili nüfus müdürlüklerinden birinde yenilenir.',
        'Kayıp ya da çalıntı olsa da değerli kâğıt bedeli ve vakıf payı ödenir; 2026’da bu iki kalemin toplamı 2.115 TL’dir.',
        'Ad veya soyadı değişen sürücünün ehliyeti de bu bedellerle yenilenir.',
    ],
    body='''
<h2>Ehliyet süresi dolmadan hangi durumlarda değiştirilir?</h2>
<p>NVİ’ye göre ehliyet; kayıp veya çalıntı durumunda, üzerindeki kimlik bilgilerinden biri değiştiğinde, kartta tahrifat veya kırılma olduğunda, sertifika bilgilerinde ekleme veya çıkarma yapıldığında ya da kullanılmasını engelleyen bir kusur tespit edildiğinde süresi dolmadan değiştirilebilir.</p>

<h2>Gerekli belgeler</h2>
<ul>
<li>Kimlik belgesi.</li>
<li>Sürücü sağlık raporu.</li>
<li>Son altı ay içinde çekilmiş 1 adet biyometrik fotoğraf.</li>
<li>Kan grubunu gösteren belge veya beyan.</li>
<li>Adli sicil kaydı ile değerli kâğıt bedeli ve vakıf payı ödemesi (bunlar sistemden kontrol edilir).</li>
</ul>
<p>Kayıp veya çalıntı değilse mevcut ehliyetinizi de götürmeniz gerekir.</p>

<h2>Özel durumlar</h2>
<ul>
<li><strong>Dağıtımda kaybolursa:</strong> posta görevlisinin bildirimi üzerine kayıtlarınız esas alınarak ehliyet yeniden düzenlenir; tekrar başvurmanız gerekmez.</li>
<li><strong>Evde bulunamadıysanız:</strong> belge nüfus müdürlüğüne geri döner; başvurduğunuz ya da başvuruda belirttiğiniz müdürlükten alabilirsiniz.</li>
<li><strong>Hatalı basım:</strong> hata sistemden kaynaklanıyorsa ehliyet bedelsiz değiştirilir; başvuru sahibinin beyanından kaynaklanıyorsa bedeller yeniden alınır.</li>
<li><strong>Vekalet:</strong> ehliyet başvurusu ve teslimi vekaletle yapılamaz, başvuru bizzat yapılır.</li>
</ul>
<p>Randevu ve teslim süreci için ''' + a('randevu', 'ehliyet randevusu') + ''' yazımıza bakın.</p>
''',
    faq=[
        ('Kayıp ehliyet için ücret ödenir mi?',
         'Evet. NVİ’ye göre ehliyet kayıp veya çalıntı nedeniyle yenilense bile değerli kâğıt bedeli ve vakıf payı ödenir. 2026’da bu iki kalemin toplamı 2.115 TL’dir.'),
        ('Kayıp ehliyet için sağlık raporu gerekir mi?',
         'Evet. NVİ, kayıp veya çalıntı nedeniyle yenilemede istenen belgeler arasında sürücü sağlık raporunu sayar.'),
        ('Ehliyetim kargoda kayboldu, yeniden başvurmalı mıyım?',
         'Hayır. Dağıtım sırasında kaybolduğu posta görevlisince bildirilen ehliyet, kayıtlarınız esas alınarak yeniden düzenlenir; tekrar başvurmanız gerekmez.'),
    ],
    sources=['nvi_sss', 'nvi_ucret'],
))

# 13 ────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='yurtdisi',
    title='Yurt Dışı Ehliyeti Türkiye’de Geçerli mi? Değişim | Uslu',
    desc='Yurt dışından alınan ehliyetle Türkiye’de ne kadar araç kullanılır, Türk ehliyetine nasıl çevrilir? Türk ehliyetinin yurt dışında geçerliliği ve uluslararası belge.',
    h1='Yurt Dışı Ehliyeti Türkiye’de Geçerli mi?',
    crumb='Yurt Dışı Ehliyeti',
    card='Yabancı ehliyetle Türkiye’de araç kullanma süresi ve değişim işlemi.',
    lead='Yurt dışından alınan ehliyetle Türkiye’de belirli bir süre araç kullanılabilir; bu sürenin sonunda ehliyetin Türk ehliyetiyle değiştirilmesi gerekir. Bilgiler NVİ açıklamalarına dayanır.',
    summary=[
        '01.01.2016’dan itibaren yurt dışından alınan ehliyetle Türk vatandaşları 2 yıl, yabancılar 6 ay Türkiye’de araç kullanabilir.',
        'Bu sürenin sonunda araç kullanmaya devam etmek için Türk ehliyeti almak ya da yabancı ehliyeti değiştirmek gerekir.',
        'Yeni tip Türk ehliyetiyle Karayolu Trafiği Konvansiyonuna üye 93 ülkede araç kullanılabilir.',
    ],
    body='''
<h2>Yabancı ehliyetle Türkiye’de araç kullanmak</h2>
<p>NVİ’ye göre 01.01.2016’dan itibaren yurt dışından alınan ehliyetle Türk vatandaşları 2 yıl, yabancılar 6 ay süreyle Türkiye’de araç kullanabilir. Bu süre dolduktan sonra Türkiye’de araç kullanmak için Türk ehliyeti gerekir.</p>

<h2>Yabancı ehliyeti Türk ehliyetiyle değiştirme</h2>
<p>Değişim başvurusunda NVİ şunları ister:</p>
<ul>
<li>Yabancı ehliyetin aslı ve renkli fotokopisi.</li>
<li>Noter veya konsolosluk onaylı Türkçe tercümesi.</li>
<li>Kimlik belgesi ve sürücü sağlık raporu.</li>
<li>Son altı ay içinde çekilmiş 1 adet biyometrik fotoğraf.</li>
<li>Kan grubunu gösteren belge veya beyan.</li>
<li>Öğrenim belgesi; yurt dışından alınanlar için noter tasdikli tercümesi.</li>
<li>Değerli kâğıt bedeli, harç ve vakıf payı ile adli sicil kaydı (bunlar sistemden kontrol edilir).</li>
</ul>
<p>Değiştirilen yabancı ehliyet, Karayolları Trafik Yönetmeliği uygulama talimatına göre ilgili ülkeye gönderilir. Yurt dışında yaşayan vatandaşların ehliyet başvuruları 15.02.2021’den beri dış temsilciliklerde de alınmaktadır. Mavi Kart sahipleri, ehliyetlerini Türk ehliyetine dönüştürürlerse ticari araç kullanabilir.</p>

<h2>Yurt dışı ehliyetiyle başka sınıf almak</h2>
<p>MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’ne göre yurt dışından alınmış ehliyet önce Türk ehliyetiyle değiştirilir; farklı bir sınıf için sürücü kursuna ondan sonra başvurulabilir (m.39/4). Ayrıntılar ''' + a('ekleme', 'ehliyete sınıf ekleme') + ''' yazımızda.</p>

<h2>Türk ehliyeti yurt dışında geçerli mi?</h2>
<p>NVİ’ye göre 01.01.2016’dan itibaren verilen yeni tip Türk ehliyetiyle Karayolu Trafiği Konvansiyonuna üye 93 ülkede araç kullanılabilir. Bu ülkelerde ne kadar süre araç kullanılabileceği o ülkenin mevzuatına göre değişir. Konvansiyona üye olmayan ülkelerde araç kullanmak için Türkiye Turing ve Otomobil Kurumunun verdiği Uluslararası Sürücü Belgesi gerekir.</p>
''',
    faq=[
        ('Yurt dışı ehliyetiyle Türkiye’de ne kadar araç kullanılır?',
         'NVİ’ye göre 01.01.2016’dan itibaren yurt dışından alınan ehliyetle Türk vatandaşları 2 yıl, yabancılar 6 ay süreyle Türkiye’de araç kullanabilir.'),
        ('Yabancı ehliyeti Türk ehliyetine çevirmek için ne gerekir?',
         'Yabancı ehliyetin aslı ve renkli fotokopisi, noter veya konsolosluk onaylı Türkçe tercümesi, kimlik, sağlık raporu, biyometrik fotoğraf, kan grubu belgesi, öğrenim belgesi ile harç, değerli kâğıt bedeli ve vakıf payı gerekir.'),
        ('Türk ehliyetiyle yurt dışında araç kullanılır mı?',
         'Yeni tip Türk ehliyetiyle Karayolu Trafiği Konvansiyonuna üye 93 ülkede araç kullanılabilir. Üye olmayan ülkelerde Türkiye Turing ve Otomobil Kurumundan Uluslararası Sürücü Belgesi alınması gerekir.'),
    ],
    sources=['nvi_sss', 'mtsk'],
))

# 14 ────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='aday',
    title='Aday Sürücü Belgesi Nedir? 2 Yıl Kuralı ve İptal | Uslu',
    desc='İlk ehliyetini alanlar iki yıl aday sürücüdür. 75 ceza puanı, 0.20 promil üzeri alkol ve bazı kuralların üç kez ihlali aday belgenin iptaline yol açar.',
    h1='Aday Sürücü Belgesi Nedir?',
    crumb='Aday Sürücü',
    card='İlk iki yılın kuralları ve belgenin iptal edildiği durumlar.',
    lead='İlk kez ehliyet alan sürücüler, belgenin alındığı tarihten itibaren iki yıl aday sürücü sayılır ve bu dönemde daha sıkı kurallara tabidir. Bilgiler Karayolları Trafik Kanunu’nun 24.07.2026’da değişen Ek 17. maddesine ve NVİ açıklamalarına dayanır.',
    summary=[
        'İlk kez ehliyet alanlar ile ehliyeti iptal edilip yeniden alanlar, belgenin alındığı tarihten itibaren iki yıl aday sürücüdür.',
        'Bu sürede 75 ceza puanını aşmak ya da 0.20 promilin üzerinde alkollü araç kullanmak aday belgenin iptaline yol açar.',
        'Belgesi iptal edilen aday, yeniden ehliyet için sürücü kursuna devam edip sınavları tekrar geçmelidir.',
    ],
    body='''
<h2>Kimler aday sürücüdür?</h2>
<p>İlk defa ehliyet alanlar ile ehliyeti herhangi bir nedenle iptal edilip yeniden almaya hak kazananlar, belgenin alındığı tarihten itibaren iki yıl aday sürücü sayılır (Karayolları Trafik Kanunu Ek 17). NVİ’ye göre ehliyetin üzerinde aday sürücü olduğunu gösteren bir ibare bulunmaz, bu bilgi sistemde görülür; iki yıllık süre sonunda ehliyet yenilenmez.</p>

<h2>Aday belge hangi durumlarda iptal edilir?</h2>
<ul>
<li>Kanuna göre ehliyetin geçici olarak geri alınmasını gerektiren bir ihlal.</li>
<li>75 ceza puanının aşılması.</li>
<li>Araç cinsine bakılmaksızın 0.20 promilin üzerinde alkollü araç kullanılması.</li>
<li>Şu kurallardan herhangi birinin üç kez ihlal edilmesi: dönüşlerde yayalara, bisiklet ve elektrikli skuter kullananlara ve sola dönüşte sağdan ve karşıdan gelen trafiğe ilk geçiş hakkını vermek (m.53/2); yaya ve okul geçitlerinde yayalara ilk geçiş hakkını vermek (m.74); emniyet kemeri, koruma başlığı ve çocuk bağlama sistemi gibi koruyucu sistemleri kullanmak (m.78).</li>
</ul>

<h2>İptalden sonra yeniden ehliyet</h2>
<p>Aday belgesi iptal edilen kişi, yeniden ehliyet alabilmek için sürücü kursuna devam edip sınavlarda başarılı olarak yeni bir sertifika almalıdır. Kursa başlayabilmesi için psikoteknik değerlendirme ve psikiyatri uzmanı muayenesi sonucunda sürücülüğe engel hâli olmadığını gösteren belgeyi kursa vermesi, kanun kapsamındaki idari para cezalarının tamamını ödemiş olması ve varsa bekleme ya da geri alma süresinin geçmiş olması gerekir.</p>
<p>Ceza puanı kuralları için ''' + a('ceza', 'ehliyet ceza puanı') + ''' yazımıza bakın.</p>
''',
    faq=[
        ('Aday sürücülük kaç yıl sürer?',
         'Ehliyetin alındığı tarihten itibaren iki yıl sürer. İlk kez ehliyet alanlar ile ehliyeti iptal edilip yeniden alanlar aday sürücü sayılır.'),
        ('Aday sürücü ehliyetinde bir ibare olur mu?',
         'Hayır. NVİ’ye göre ehliyetin üzerinde aday sürücü olduğunu gösteren bir ibare bulunmaz; bu bilgi sistemde görülür.'),
        ('Aday sürücü kaç ceza puanında ehliyetini kaybeder?',
         'Aday sürücülük süresinde 75 ceza puanının aşılması aday belgenin iptaline yol açar.'),
    ],
    sources=['ktk', 'nvi_sss'],
))

# 15 ────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='ceza',
    title='Ehliyet Ceza Puanı ve 100 Puan Kuralı | Uslu Sürücü Kursu',
    desc='Bir yılda 100 ceza puanını dolduran sürücünün ehliyeti 2 ay geri alınır; ikincisinde 4 ay, üçüncüsünde süresiz iptal. Emniyet kemeri kuralı ve aday sürücüler.',
    h1='Ehliyet Ceza Puanı Nasıl İşler?',
    crumb='Ceza Puanı',
    card='100 puan kuralı, geri alma süreleri ve emniyet kemeri kuralı.',
    lead='Trafik kurallarını ihlal eden sürücülere, aldıkları her ceza için ceza puanı verilir. Puanlar belirli bir sınırı aşınca ehliyet geri alınır. Bilgiler Karayolları Trafik Kanunu’nun 78, 118 ve Ek 17. maddelerine dayanır.',
    summary=[
        'Suçun işlendiği tarihten geriye doğru bir yıl içinde 100 ceza puanını dolduran sürücünün ehliyeti 2 ay geri alınır ve sürücü eğitime alınır.',
        'Aynı yıl ikinci kez 100 puan dolarsa ehliyet 4 ay geri alınır; üçüncüsünde ehliyet süresiz iptal edilir.',
        'Aday sürücülerde sınır 75 puandır; aşılırsa aday belge iptal edilir.',
    ],
    body='''
<h2>100 ceza puanı kuralı</h2>
<p>Karayolları Trafik Kanunu’nun 118. maddesine göre:</p>
<ul>
<li>Trafik suçunun işlendiği tarihten geriye doğru bir yıl içinde toplam 100 ceza puanını dolduran sürücünün ehliyeti 2 ay süreyle geri alınır ve sürücü eğitime alınır.</li>
<li>Aynı yıl içinde ikinci kez 100 puanı dolduran sürücünün ehliyeti 4 ay süreyle geri alınır; sürücü psikoteknik değerlendirmeye ve psikiyatri uzmanı muayenesine tabi tutulur. Engel hâli yoksa ehliyet süre sonunda iade edilir.</li>
<li>Bir yıl içinde üç kez 100 puanı dolduran sürücünün ehliyeti süresiz olarak iptal edilir.</li>
<li>Ölümle sonuçlanan bir trafik kazasına asli kusurlu olarak sebep olan sürücünün ehliyeti 1 yıl süreyle geri alınır.</li>
</ul>
<p>Hangi ihlale kaç puan verileceği yönetmelikte belirlenir. Ehliyeti geri alınmışken araç kullanan sürücü ayrıca cezalandırılır.</p>

<h2>Emniyet kemeri kuralı</h2>
<p>Kanunun 12.02.2026’da değişen 78. maddesine göre, son ihlalin gerçekleştiği tarihten geriye doğru bir yıl içinde emniyet kemeri kuralını dört veya daha fazla kez ihlal eden sürücünün ehliyeti her seferinde 30 gün süreyle geri alınır. Geri alınan ehliyetin iadesi için kanun kapsamındaki idari para cezalarının tamamının ödenmiş olması gerekir.</p>

<h2>Aday sürücüler için</h2>
<p>İlk iki yılındaki sürücülerde sınır 75 ceza puanıdır; bu puanın aşılması aday belgenin iptaline yol açar. Ayrıntılar ''' + a('aday', 'aday sürücü belgesi') + ''' yazımızda.</p>
''',
    faq=[
        ('Kaç ceza puanında ehliyet alınır?',
         'Suçun işlendiği tarihten geriye doğru bir yıl içinde 100 ceza puanını dolduran sürücünün ehliyeti 2 ay süreyle geri alınır ve sürücü eğitime alınır.'),
        ('İkinci kez 100 ceza puanı dolarsa ne olur?',
         'Aynı yıl içinde ikinci kez 100 puanı dolduran sürücünün ehliyeti 4 ay geri alınır; psikoteknik değerlendirme ve psikiyatri uzmanı muayenesi gerekir. Üçüncüsünde ehliyet süresiz iptal edilir.'),
        ('Emniyet kemeri takmamak ehliyeti etkiler mi?',
         'Evet. Bir yıl içinde emniyet kemeri kuralını dört veya daha fazla kez ihlal eden sürücünün ehliyeti her seferinde 30 gün geri alınır.'),
    ],
    sources=['ktk'],
))

# 16 ────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='rapor',
    title='Sürücü Olur Raporu Nereden Alınır? Şartlar 2026 | Uslu',
    desc='Ankara’da sürücü olur raporu nereden alınır, muayenede nelere bakılır, görme şartı nedir, rapor kaç yıl geçerlidir? Sürücü Sağlık Yönetmeliğine göre.',
    h1='Sürücü Olur Raporu Nereden Alınır?',
    crumb='Sürücü Olur Raporu',
    card='Raporu kim verir, muayenede nelere bakılır, kaç yıl geçerli.',
    lead='Sürücü olur raporu, hem sürücü kursuna kayıtta hem de nüfus müdürlüğündeki ehliyet başvurusunda istenir. Bilgiler Sürücü Adayları ve Sürücülerde Aranacak Sağlık Şartları ile Muayenelerine Dair Yönetmeliğe ve NVİ açıklamalarına dayanır.',
    summary=[
        'Rapor; Sağlık Bakanlığına ve üniversitelere bağlı sağlık tesisleri, aile sağlığı merkezleri ve muayenehaneler dışındaki özel sağlık kuruluşlarındaki hekimlerce düzenlenir.',
        'Birinci grup sınıflarda (M, A1, A2, A, B1, B, BE, F) iki gözün toplam görmesi 1,0 olmalıdır; gözlük ve kontakt lens kabul edilir.',
        'NVİ’ye göre hekim aksine bir tarih yazmadıysa sağlık raporu 2 yıl geçerlidir.',
    ],
    body='''
<h2>Rapor nereden alınır?</h2>
<p>Sürücü adaylarının ve sürücülerin muayenesini; Sağlık Bakanlığına ve üniversitelere bağlı sağlık tesisleri, aile sağlığı merkezleri ve Sağlık Bakanlığınca ruhsatlandırılan muayenehaneler dışındaki özel sağlık kuruluşlarında görevli hekimler yapar ve raporu düzenler (m.4/1).</p>

<h2>Muayenede nelere bakılır?</h2>
<p>Yönetmelik; göz, iç hastalıkları, kulak burun boğaz, ortopedi, ruh ve sinir hastalıkları muayenelerine ilişkin esasları belirler. Hakkında karar verilemeyen durumlarda aday ilgili uzman hekime yönlendirilir. Muayenede sınıflar iki gruba ayrılır: birinci grup M, A1, A2, A, B1, B, BE ve F; ikinci grup C1, C1E, C, CE, D1, D1E, D, DE ve G sınıflarıdır.</p>

<h2>Görme şartı</h2>
<ul>
<li><strong>Birinci grup:</strong> gözlüklü ya da gözlüksüz, bir gözün görmesi 0,1’in altında olmamak şartıyla iki gözün toplam görme derecesi 1,0 olmalıdır.</li>
<li><strong>İkinci grup:</strong> az gören gözün görmesi 0,6’nın, iyi gören gözün görmesi 0,8’in altında olmamalı ya da her iki göz 0,7 olmalıdır.</li>
<li>Gözlük ve kontakt lensle düzeltme kabul edilir; bu durumda araç kullanırken gözlük veya lens takmak zorunludur.</li>
<li>Görme alanı için de yönetmelikte ayrıca şartlar vardır; muayeneyi yapan hekim bunları değerlendirir.</li>
</ul>

<h2>Kısıtlar ve itiraz</h2>
<p>Sağlık durumu nedeniyle araç kullanımı bir şarta bağlanırsa bu şart kod numarasıyla rapora yazılır (m.4/7). Özel tertibatlı araç gerekiyorsa süreç komisyonda yürür; bunu ''' + a('ozel', 'özel gereksinimli sürücü adayları') + ''' yazımızda anlattık. Kişinin, adına düzenlenen rapora itiraz hakkı vardır; itiraz usullerini Sağlık Bakanlığı belirler (m.4/5).</p>

<h2>Rapor kaç yıl geçerli?</h2>
<p>NVİ, Sağlık Raporları Usul ve Esasları Hakkında Yönerge’ye dayanarak, hekimlerce veya ilgili mevzuatta aksine bir tarih belirtilmediği durumlarda raporların 2 yıl geçerli olduğunu belirtir.</p>

<h2>Ehliyet aldıktan sonra sağlık durumu değişirse</h2>
<p>Karayolları Trafik Kanunu’nun 45. maddesine göre sürücüde sağlığı bakımından sürücülüğe engel açık bir değişiklik görülürse ehliyet geri alınır ve muayene istenir. Engel hâlinin olmadığı ya da ortadan kalktığı raporla tespit edilirse ehliyet iade edilir.</p>
''',
    faq=[
        ('Sürücü olur raporu nereden alınır?',
         'Aile sağlığı merkezlerinden, Sağlık Bakanlığına ve üniversitelere bağlı sağlık tesislerinden ve muayenehaneler dışındaki özel sağlık kuruluşlarından alınır.'),
        ('Gözlük takıyorum, ehliyet alabilir miyim?',
         'Evet. Gözlük ve kontakt lensle düzeltme kabul edilir; görme şartını gözlükle sağlıyorsanız araç kullanırken gözlük takmanız zorunludur.'),
        ('Sürücü sağlık raporu kaç yıl geçerlidir?',
         'NVİ’ye göre hekim veya ilgili mevzuat aksine bir tarih belirtmediyse sağlık raporu 2 yıl geçerlidir.'),
    ],
    sources=['saglik', 'nvi_sss', 'ktk'],
))

# 17 ────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='motosiklet',
    title='Motosiklet Ehliyeti: A1, A2 ve A Sınıfı Rehberi | Uslu',
    desc='A1, A2 ve A motosiklet ehliyeti kaç yaşında alınır, hangi motosikletleri kapsar, kaç saat ders gerekir, sınavda neler istenir? 2026 harç tutarlarıyla.',
    h1='Motosiklet Ehliyeti Nasıl Alınır?',
    crumb='Motosiklet Ehliyeti',
    card='Yaş, motor gücü sınırı, ders saati, sınav ve 2026 harcı.',
    lead='Motosiklet ehliyeti üç sınıftan oluşur: A1, A2 ve A. Sınıf; motosikletin gücüne, sizin yaşınıza ve deneyiminize göre belirlenir. Bilgiler Karayolları Trafik Yönetmeliği ile MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’ne dayanır.',
    summary=[
        'A1 16, A2 18, A 20 yaşında alınır; A için iki yıllık A2 gerekir, 24 yaşını dolduranlarda bu şart aranmaz.',
        'A1 125 cm³ ve 11 kW’a, A2 35 kW’a kadar motosikletleri kapsar; A tüm iki tekerlekli motosikletleri kapsar.',
        '2026’da A1, A2 ve A için ilk ehliyette nüfus müdürlüğüne toplam 4.354,90 TL ödenir.',
    ],
    body='''
<h2>Sınıflar</h2>
<div class="guide-table"><table>
<thead><tr><th>Sınıf</th><th>Motosiklet</th><th>Yaş</th><th>Akan trafikte en az ders</th></tr></thead>
<tbody>
<tr><td>A1</td><td>125 cm³, 11 kW’a kadar</td><td>16</td><td>12 saat</td></tr>
<tr><td>A2</td><td>35 kW’a kadar</td><td>18</td><td>12 saat</td></tr>
<tr><td>A</td><td>Tüm motosikletler</td><td>20</td><td>6 saat (A2 ile), 12 saat (24 yaş)</td></tr>
</tbody></table></div>
<p>A sınıfı için en az iki yıllık A2 ehliyeti gerekir; 24 yaşını dolduran adaylarda bu şart aranmaz. Gücü 15 kW’ı aşan üç tekerlekli motosikletler için A sınıfında yaş şartı 21’dir. A2 ehliyetiyle A1, A ehliyetiyle A1 ve A2 motosikletleri de kullanılabilir (Karayolları Trafik Yönetmeliği m.85).</p>

<h2>Eğitim ve sınav</h2>
<p>Teorik dersler tüm sınıflarda aynıdır (34 saat) ve e-Sınav’la ölçülür. Direksiyon sınavı önce sınav alanında yapılır: araç bilgisi soruları, dokuz koni arasında slalom, iki çember içinde sekiz çizme, 20 metrelik denge çizgisi, dar alanda dönüş, hızlanıp durma, engelden kaçınma ve ani fren. Alanda başarılı olan adayın sınavı güzergâhta, trafikte devam eder (MTSK Yönetmeliği m.35). Ayrıntılar ''' + a('sinav', 'ehliyet sınavı') + ''' yazımızda.</p>

<h2>B ehliyetiniz varsa</h2>
<p>B ehliyeti olan biri motosiklet sınıfı için kursa kayıt olduğunda, yönetmelikteki tabloya göre A1, A2 veya A için akan trafikte 12 saat direksiyon dersi alır. Ehliyeti en az iki yıllık olanlar için ayrıca A1 motosikletleri kullanmanın daha kısa bir yolu vardır; şartlarını ''' + a('motor', 'B ehliyetle motosiklet') + ''' yazımızda anlattık.</p>

<h2>Uslu Sürücü Kursu’nda</h2>
<p>Kursumuzda <a href="/egitim/motor-a1/">A1 motosiklet</a> ve <a href="/egitim/motor-a2/">A2 motosiklet</a> eğitimleri verilir. Masraf kalemleri için ''' + a('masraf', 'ehliyet masrafları') + ''' yazımıza bakın.</p>
''',
    faq=[
        ('Motosiklet ehliyeti kaç yaşında alınır?',
         'A1 sınıfı 16, A2 sınıfı 18, A sınıfı 20 yaşında alınır. A için ayrıca iki yıllık A2 ehliyeti gerekir; 24 yaşını dolduranlarda bu şart aranmaz.'),
        ('A2 ehliyetle 125 cc motosiklet kullanılır mı?',
         'Evet. Karayolları Trafik Yönetmeliği’nin 85. maddesine göre A2 ehliyetiyle M ve A1 sınıfı araçlar da kullanılabilir.'),
        ('Motor ehliyeti harcı ne kadar?',
         '2026’da A1, A2 ve A sınıfları için harç 2.239,90 TL’dir; değerli kâğıt bedeli ve vakıf payıyla toplam 4.354,90 TL ödenir.'),
    ],
    sources=['kty', 'mtsk', 'nvi_ucret'],
))

# 18 ────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='ekleme',
    title='Ehliyete Sınıf Ekleme: Ders Saatleri ve Belgeler | Uslu',
    desc='B ehliyetine A2, BE, C veya D eklemek için kaç saat direksiyon dersi gerekir, hangi belgeler istenir, ne ödenir? MEB yönetmeliğindeki tabloya göre.',
    h1='Ehliyete Sınıf Nasıl Eklenir?',
    crumb='Sınıf Ekleme',
    card='Mevcut ehliyete yeni sınıf eklerken ders saati ve belgeler.',
    lead='Ehliyeti olan biri başka bir sınıf için de sürücü kursuna kayıt olabilir. Bu durumda alınacak direksiyon dersi, sahip olunan ehliyete göre yönetmelikteki tabloda belirlenir. Bilgiler MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’nin 39. maddesine ve NVİ açıklamalarına dayanır.',
    summary=[
        'Farklı sınıf isteyen ehliyet sahibi, o sınıfın yaş ve deneyim şartlarını taşıyorsa tablodaki saat kadar akan trafikte direksiyon dersi alır ve direksiyon sınavına girer.',
        'B sahibi için akan trafikteki ders saatleri: BE 6, C1 10, C 20, D1 7, D 14; A1, A2 ve A için 12 saat.',
        'Sınavı geçtikten sonra nüfus müdürlüğünde yeni sınıfın harcı, değerli kâğıt bedeli ve vakıf payı ödenir.',
    ],
    body='''
<h2>Nasıl işler?</h2>
<p>Ehliyet sahibi, istediği sınıfın şartlarını taşımak kaydıyla yönetmelikteki tabloda belirtilen saat kadar direksiyon dersi alır. Eğitim sonunda kursun uygun görmesiyle direksiyon sınavına girer; başarılı olana yeni sınıfın sertifikası verilir (m.39/1 ve 39/3). Farklı sınıf alacakların eğitim alanında veya simülatörde alması gereken dersler akan trafikte de yapılabilir (m.7/1). Yaş ve deneyim şartları için ''' + a('siniflar', 'ehliyet sınıfları') + ''' yazımıza bakın.</p>

<h2>B ehliyeti olanlar için ders saatleri</h2>
<div class="guide-table"><table>
<thead><tr><th>Eklenecek sınıf</th><th>Akan trafikte ders</th><th>Şart</th></tr></thead>
<tbody>
<tr><td>A1, A2</td><td>12 saat</td><td>Yaş şartı</td></tr>
<tr><td>A</td><td>12 saat</td><td>20 yaş, 2 yıllık A2 veya 24 yaş</td></tr>
<tr><td>BE</td><td>6 saat</td><td>B</td></tr>
<tr><td>C1</td><td>10 saat</td><td>18 yaş, B</td></tr>
<tr><td>C</td><td>20 saat</td><td>21 yaş, B</td></tr>
<tr><td>D1</td><td>7 saat</td><td>21 yaş, B</td></tr>
<tr><td>D</td><td>14 saat</td><td>24 yaş, B</td></tr>
</tbody></table></div>
<p>Motosiklet ehliyeti olanlar için tablodaki bazı değerler: A1 sahibinin A2 eklemesi 6 saat, A2 sahibinin A eklemesi 6 saat, A1 veya A2 sahibinin B eklemesi 14 saattir. 2016 öncesi eski sınıf ehliyeti olanlar için yönetmelikte ayrı bir tablo uygulanır.</p>

<h2>Nüfus müdürlüğünde</h2>
<p>Sınıf eklemede NVİ şunları ister: kimlik belgesi, sürücü sertifikası, öğrenim belgesi, kayıp veya çalıntı değilse mevcut ehliyet, sürücü sağlık raporu, 1 adet biyometrik fotoğraf, kan grubu belgesi veya beyanı ile harç, değerli kâğıt bedeli ve vakıf payı. Adli sicil kaydı sistemden kontrol edilir. Yeni sınıfın 2026 harcı için ''' + a('masraf', 'ehliyet masrafları') + ''' yazımıza bakın.</p>
<p>Otomatik ehliyetini aynı sınıfın manuel ehliyetine çevirenlerden harç alınmaz; bu durum ''' + a('otomatik', 'otomatik vites ehliyet') + ''' yazımızda.</p>
''',
    faq=[
        ('B ehliyetine motosiklet sınıfı eklemek için kaç saat ders gerekir?',
         'MEB yönetmeliğindeki tabloya göre B ehliyeti olan biri A1, A2 veya A sınıfı için akan trafikte 12 saat direksiyon dersi alır.'),
        ('B ehliyetine C sınıfı eklemek için ne gerekir?',
         'C sınıfı için 21 yaşını bitirmiş olmak ve B ehliyetine sahip olmak gerekir; tabloya göre akan trafikte 20 saat direksiyon dersi alınır ve direksiyon sınavı geçilir.'),
        ('Sınıf eklemede ne ödenir?',
         'Nüfus müdürlüğünde yeni sınıfın harcı ile değerli kâğıt bedeli ve vakıf payı ödenir. Kurs ve sınav ücretleri ayrıca ödenir.'),
    ],
    sources=['mtsk', 'nvi_sss', 'nvi_ucret', 'kty'],
))

# 19 ────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='ozel',
    title='Engelli Sürücü Adayları: Rapor, Araç ve Sınav | Uslu',
    desc='Özel tertibatlı araç gereken sürücü adaylarında sağlık raporu komisyonu, özel tertibat kodu, eğitim ve sınav aracı. Yönetmeliklere göre adım adım.',
    h1='Engelli Bireyler Nasıl Ehliyet Alır?',
    crumb='Özel Gereksinimli Adaylar',
    card='Özel tertibat raporu, komisyon süreci, eğitim ve sınav aracı.',
    lead='Özel tertibatlı araç kullanması gereken sürücü adayları için sağlık raporu, eğitim ve sınav süreci ayrıca düzenlenmiştir. Bilgiler Sürücü Sağlık Yönetmeliği ile MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’ne dayanır.',
    summary=[
        'Özel tertibatlı araç gerektiren durumlarda sağlık raporu il sağlık müdürlüğü bünyesindeki komisyona sevk edilir.',
        'Komisyon, uygun özel tertibat kodlarını ve hangi sınıf ehliyet alınabileceğini raporda belirtir.',
        'Direksiyon eğitimi ve sınavı, raporda belirtilen şartları taşıyan araçla yapılır.',
    ],
    body='''
<h2>Sağlık raporu ve komisyon</h2>
<p>Özel tertibatlı araç kullanılması gereken durumlarda hekim, raporda tanıyı ve adayın ehliyet alabileceğini ve özel tertibatlı araç kullanabileceğini belirtir; kod ve sınıf yazmadan raporu il sağlık müdürlüğü bünyesindeki komisyona sevk eder (m.4/8). Komisyonda ilgili branş uzmanları, ortopedi ve travmatoloji, fiziksel tıp ve rehabilitasyon ve nöroloji uzmanları ile bir makine mühendisi bulunur. Komisyon, uygun özel tertibat kodlarını, hangi sınıf ehliyet alınabileceğini ya da sürücü olunup olunamayacağını raporda belirtir. Başvuru olması hâlinde en az ayda bir toplanır.</p>

<h2>Kodlar ehliyete yazılır</h2>
<p>Sağlık durumuna bağlı şartlar kod numarasıyla rapora yazılır (m.4/7). Sürücünün sağlık şartları ve araçta bulunması gereken özel tertibatlara ilişkin kodlar, ehliyetin ve araç tescil belgesinin ilgili bölümüne yazılır (m.4/10).</p>

<h2>Eğitim ve sınav aracı</h2>
<p>MEB yönetmeliğine göre engelli kursiyerlerin direksiyon sınavları, ilgili mevzuata göre düzenlenen raporda belirtilen şartları taşıyan direksiyon eğitim ve sınav aracıyla yapılır (m.7/5). Teorik ders saatleri bütün adaylar için aynıdır; e-Sınav’da işitme engelli adaylara 15 dakika ek süre tanınır.</p>

<h2>Eski H sınıfı ehliyetler</h2>
<p>Karayolları Trafik Yönetmeliği’ne göre eski H sınıfı ehliyetler, engellinin kullanmaya yetkili olduğu araç cinsine göre A veya B sınıfı ehliyetle değiştirilir; değişim sırasında sağlık raporu istenir.</p>

<h2>Uslu Sürücü Kursu’nda</h2>
<p>Kursumuzda <a href="/egitim/ozel-ab/">özel gereksinimli A-B sınıfı</a> eğitimi verilir; eğitim ve araç uygunluğu adaya göre bireysel değerlendirilir. Raporun genel esasları için ''' + a('rapor', 'sürücü olur raporu') + ''' yazımıza bakın.</p>
''',
    faq=[
        ('Özel tertibatlı araç gereken adayın raporunu kim verir?',
         'Hekim raporu tanı ve özel tertibatlı araç kullanabileceği bilgisiyle il sağlık müdürlüğü bünyesindeki komisyona sevk eder; özel tertibat kodlarını ve ehliyet sınıfını komisyon belirler.'),
        ('Özel tertibat kodu nereye yazılır?',
         'Sürücünün sağlık şartları ve araçta bulunması gereken özel tertibatlara ilişkin kodlar ehliyetin ve araç tescil belgesinin ilgili bölümüne yazılır.'),
        ('Direksiyon sınavı hangi araçla yapılır?',
         'Engelli kursiyerlerin direksiyon sınavları, raporda belirtilen şartları taşıyan direksiyon eğitim ve sınav aracıyla yapılır.'),
    ],
    sources=['saglik', 'mtsk', 'kty', 'esinav'],
))

# 20 ────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='randevu',
    title='Ehliyet Randevusu ve Başvurusu: Nüfus Müdürlüğü | Uslu',
    desc='Ankara’da ehliyet randevusu nereden alınır, randevuya ne zaman gidilir, vekaletle başvuru olur mu, belge nasıl teslim edilir? NVİ bilgileriyle.',
    h1='Ehliyet Randevusu Nasıl Alınır?',
    crumb='Ehliyet Randevusu',
    card='Randevu kanalları, başvuru günü, teslim ve takip.',
    lead='Sınavları geçtikten sonra ehliyet için nüfus müdürlüğüne randevuyla başvurulur. Aynı yol yenileme, kayıp ve sınıf ekleme işlemlerinde de izlenir. Bilgiler NVİ açıklamalarına dayanır.',
    summary=[
        'Randevu randevu.nvi.gov.tr, e-Devlet, NVİ Mobil, Nüfusmatik veya Alo 199 üzerinden alınır.',
        'Randevu saatinden 30 dakika önce ile 60 dakika sonrası arasında sıra alınabilir; 60 dakikayı geçirenin başvurusu alınmaz.',
        'Başvuru bizzat yapılır, vekaletle işlem yapılmaz; ehliyet PTT ile ücretsiz olarak adrese gönderilir.',
    ],
    body='''
<h2>Randevu nereden alınır?</h2>
<p>Ehliyet randevusu randevu.nvi.gov.tr, e-Devlet, NVİ Mobil, Nüfusmatik veya Alo 199 üzerinden alınır. Başvuru, sertifikanın alındığı yerden bağımsız olarak yetkilendirilen ilçe nüfus müdürlüklerinden birine, dış temsilciliklere ya da nüfusmatik aracılığıyla yapılabilir. Başvuru yapılabilen müdürlükler randevu.nvi.gov.tr’de görülür.</p>

<h2>Başvuru günü</h2>
<ul>
<li>Randevu saatinizden 30 dakika önce ile 60 dakika sonrası arasında sıramatik veya dijital sıramatikten sıra alabilirsiniz; 60 dakikayı geçirenlerin başvurusu alınmaz.</li>
<li>Kimliğinizi kanıtlayan ve doğruluğu sorgulanabilen bir kimlik belgesi zorunludur.</li>
<li>Getirdiğiniz biyometrik fotoğraf taranıp sisteme kaydedildikten sonra size iade edilir; fotokopi veya biyometrik olmayan fotoğraf kabul edilmez.</li>
<li>Ehliyet başvurularında bir defaya mahsus parmak izi alınır.</li>
<li>Başvuru bizzat yapılır; vekaletle işlem yapılmaz.</li>
</ul>
<p>İstenen belgelerin tam listesi ''' + a('belgeler', 'ehliyet için gerekli belgeler') + ''' yazımızda.</p>

<h2>Teslim ve takip</h2>
<ul>
<li>Sorun yoksa ehliyet üretilir ve başvuruda belirttiğiniz adrese PTT güvenli taşıma hizmetiyle gönderilir; gönderim ücretsizdir.</li>
<li>Evde bulunamazsanız belge nüfus müdürlüğüne döner; oradan alabilirsiniz.</li>
<li>Teslim aldığınızda kimlik bilgilerini ve sınıfları kontrol edin; hata varsa belgeyi iade etmeniz gerekir.</li>
<li>Başvurunun hangi aşamada olduğunu randevu.nvi.gov.tr, e-Devlet, NVİ Mobil veya Alo 199’dan takip edebilirsiniz.</li>
</ul>
''',
    faq=[
        ('Ehliyet randevusu nereden alınır?',
         'Randevu randevu.nvi.gov.tr, e-Devlet, NVİ Mobil, Nüfusmatik veya Alo 199 üzerinden alınır.'),
        ('Sürücü sertifikasıyla araç kullanabilir miyim?',
         'Hayır. NVİ’ye göre sürücü sertifikası ehliyetle değiştirilmedikçe karayolunda araç kullanma yetkisi vermez.'),
        ('Ehliyet başvurusu vekaletle yapılabilir mi?',
         'Hayır. Ehliyet başvurusu ve teslimi vekaletle yapılamaz; başvuru bizzat yapılır.'),
    ],
    sources=['nvi_sss'],
))

# 21 ────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='ankara',
    title='Ankara’da Ehliyet Almak',
    desc='Ankara’da ehliyet almak isteyenler için adım adım yol: kurs kaydı, Ankara’daki e-Sınav merkezleri, direksiyon sınavı, sağlık raporu ve nüfus müdürlüğü başvurusu.',
    h1='Ankara’da Ehliyet Nasıl Alınır?',
    crumb='Ankara’da Ehliyet',
    card='Ankara’da kurs kaydından ehliyet başvurusuna kadar süreç.',
    lead='Ankara’da ehliyet süreci, Türkiye’nin her yerinde olduğu gibi MEB ve NVİ kurallarıyla yürür; bazı adımlar ise il düzeyinde, Ankara’daki kurumlarda yapılır. Aşağıda hangi adımın nerede yapıldığını ve Ankara’da yaşayanların nelere dikkat etmesi gerektiğini özetledik.',
    summary=[
        'Ankara’da bir sürücü kursuna kayıt olan aday, e-Sınav’a Ankara’daki e-Sınav merkezlerinde girer; merkez bilgisi e-Sınav giriş belgesinde yazar.',
        'Direksiyon sınavı tarihlerini il ve ilçe millî eğitim müdürlükleri belirler; sınav hafta sonları, izin alınmış güzergâhta yapılır.',
        'Ehliyet başvurusu randevuyla, sertifikanın alındığı yerden bağımsız olarak yetkili nüfus müdürlüklerinden birine yapılır.',
    ],
    body='''
<h2>1. Sağlık raporu ve belgeler</h2>
<p>Sürücü olur raporunu Ankara’daki aile sağlığı merkezlerinden, Sağlık Bakanlığına ve üniversitelere bağlı hastanelerden ya da muayenehane dışındaki özel sağlık kuruluşlarından alabilirsiniz. Özel tertibatlı araç gerekiyorsa rapor, Ankara İl Sağlık Müdürlüğü bünyesindeki komisyona sevk edilir. Ayrıntılar ''' + a('rapor', 'sürücü olur raporu') + ''' ve ''' + a('belgeler', 'gerekli belgeler') + ''' yazılarımızda.</p>

<h2>2. Kurs kaydı ve dersler</h2>
<p>Kayıt, MEB’e bağlı bir özel sürücü kursunda yapılır. Teorik dersler bütün sınıflarda 34 saattir; direksiyon dersleri sınıfa göre değişir, B sınıfında akan trafikte en az 14 saattir. Kurs seçerken ders saatlerinin programınıza uyması, direksiyon derslerinin yapıldığı yere ulaşım, öğrenmek istediğiniz vites türü (manuel veya otomatik) ve ödeme koşulları işinizi kolaylaştırır.</p>

<h2>3. e-Sınav</h2>
<p>MEB’in 2026 kılavuzuna göre adaylar, kayıtlı oldukları kursun bulunduğu ildeki e-Sınav merkezlerinde sınava girer. Ankara’daki bir kursa kayıtlı adaylar Ankara’daki merkezlerde sınava girer. Sınav 50 soru ve 45 dakikadır, 70 puan başarılı sayılır. Ayrıntılar ''' + a('sinav', 'ehliyet sınavı') + ''' yazımızda.</p>

<h2>4. Direksiyon sınavı</h2>
<p>Sınav tarihlerini il veya ilçe millî eğitim müdürlükleri belirler. Sınav, izin alınmış güzergâhta ve akan trafikte, hafta sonları 07.00 ile 21.00 arasında yapılır ve aday başına en az 40 dakika sürer.</p>

<h2>5. Ehliyet başvurusu</h2>
<p>Sınavları geçince sertifikanız e-Devlet’te görünür. Ehliyet için randevu.nvi.gov.tr, e-Devlet, NVİ Mobil, Nüfusmatik veya Alo 199 üzerinden randevu alırsınız. Başvuru, sertifikanın alındığı yerden bağımsız olarak yetkilendirilen nüfus müdürlüklerinden birine yapılabilir; randevu ekranında Ankara’daki müdürlükleri seçebilirsiniz. Belge PTT ile ücretsiz olarak adresinize gönderilir. Ayrıntılar ''' + a('randevu', 'ehliyet randevusu') + ''' yazımızda.</p>

<h2>Ankara Sincan’da Uslu Sürücü Kursu</h2>
<p>Kursumuz Ankara’nın Sincan ilçesinde, Atatürk Mah. Atatürk Cd. No:2/17 (2. Noterin üst katı) adresindedir. <a href="/egitim/manuel-b/">B sınıfı manuel</a> ve <a href="/egitim/otomatik-b/">otomatik</a> ehliyet, <a href="/egitim/motor-a1/">A1</a> ve <a href="/egitim/motor-a2/">A2 motosiklet</a> eğitimleri ile <a href="/egitim/ozel/">özel direksiyon dersi</a> veriyoruz. Direksiyon derslerimiz OSB Törekent parkurunda yapılır. Sincan’daki adımlar için ''' + a('sincan', 'ehliyet almak için gerekli adımlar') + ''' yazımıza bakın.</p>
''',
    faq=[
        ('Ankara’da e-Sınav nerede yapılır?',
         'MEB kılavuzuna göre adaylar kayıtlı oldukları kursun bulunduğu ildeki e-Sınav merkezlerinde sınava girer. Ankara’daki bir kursa kayıtlı adaylar Ankara’daki merkezlerde sınava girer; merkez, bina ve salon bilgisi e-Sınav giriş belgesinde yazar.'),
        ('Ankara’da ehliyet başvurusu nereye yapılır?',
         'Randevu alınarak yetkilendirilen nüfus müdürlüklerinden birine yapılır. Başvuru, sertifikanın alındığı yerden bağımsızdır; randevu ekranında Ankara’daki müdürlükler seçilebilir.'),
        ('Ankara’da ehliyet kursu ücretleri ne kadar?',
         'Kurs ücretleri kursa ve seçilen eğitime göre değişir. Resmî kalemler ise her yerde aynıdır: 2026’da B sınıfı için nüfus müdürlüğüne toplam 8.869,60 TL, her e-Sınav oturumu için 1.250 TL ödenir.'),
        ('Uslu Sürücü Kursu Ankara’nın neresinde?',
         'Ankara Sincan’da, Atatürk Mah. Atatürk Cd. No:2/17 (2. Noterin üst katı), 06936 Sincan/Ankara adresindedir.'),
    ],
    sources=['esinav', 'mtsk', 'saglik', 'nvi_sss', 'nvi_ucret'],
))

# ── Parti 3a: kurs, dersler, sınavlar ─────────────────────────────
PAGES.append(dict(
    key='kayitdonemi',
    title='', desc='Sürücü kursu dönemleri ne zaman başlar, kayıt ne zamana kadar yapılır, teorik dersler günde kaç saat? Ankara’da kursa kayıt için MEB yönetmeliğindeki kurallar.',
    h1='Sürücü Kursuna Ne Zaman Kayıt Olunur?', crumb='Kayıt Dönemleri',
    card='Eğitim dönemleri, grup açılışı ve kayıt tarihleri.',
    lead='Sürücü kurslarında eğitim aylık dönemler hâlinde yürür. Ne zaman kayıt olmanız gerektiği bu dönemlere bağlıdır. Bilgiler MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’nin 12 ve 16. maddelerine dayanır.',
    summary=[
        'Eğitim dönemleri her ayın ilk on günü içinde, kursun belirlediği tarihlerde başlar.',
        'Bir dönemde en fazla üç farklı tarihte grup açılabilir; kayıt, grubun başlama tarihinden önce yapılır.',
        'Teorik dersler günde en az 2, en çok 6 saat yapılır.',
    ],
    body='''
<h2>Dönemler ve gruplar</h2>
<p>Eğitim dönemleri her ayın ilk on günü içinde kurslarca belirlenen tarihlerde başlatılır. Bir dönemde, kurs kontenjanını aşmamak şartıyla üç farklı tarihte grup açılabilir. Ayın onuncu günü hafta sonuna ya da resmî tatile denk gelirse, izleyen ilk iş günü bitimine kadar yeni grup açılmaz ancak açılmış gruplara kayıt yapılabilir (m.16/7). Kursiyerin kaydı, eğitim dönemine ait grup başlama tarihlerinden önce yapılır (m.12/2).</p>

<h2>Ders düzeni</h2>
<ul>
<li>Teorik dersler günde en az 2, en çok 6 saat yapılır.</li>
<li>Direksiyon dersleri her kursiyer için ayrı ayrı ve günde en fazla 2 saat yapılır (m.16/4).</li>
<li>Bir dönemde bir direksiyon eğitim ve sınav aracı için en fazla 12 kursiyer kaydedilir (m.16/8).</li>
<li>Kursun teorik ders çalışma planı, dönem başlamadan önce sisteme girilir (m.12/4).</li>
</ul>

<h2>Derslerden muaf olabilir misiniz?</h2>
<p>Üniversite, yüksekokul, lise ve dengi okullarda zorunlu trafik ve çevre, ilk yardım ve araç tekniği derslerinden başarılı olduğunu belgeleyenler, belgeledikleri derslerden; geçerli ilk yardımcı sertifikası olanlar ilk yardım dersinden, isterlerse eğitime alınmaz ve yalnız sınava girerler (m.16/2).</p>

<h2>Kayıtta dikkat</h2>
<p>Kayıtta çekilen fotoğraf ve girilen bilgiler size onaylatılır; fotoğrafı veya bilgileri hatalı girilen kursiyerde o dönem düzeltme yapılmaz (m.12/1). Gerekli belgeler için ''' + a('belgeler', 'ehliyet için gerekli belgeler') + ''' yazımıza bakın. Ankara Sincan’daki kursumuzda dönem ve grup tarihlerini öğrenmek için <a href="/iletisim/">bize ulaşabilirsiniz</a>.</p>
''',
    faq=[
        ('Sürücü kursu dönemleri ne zaman başlar?',
         'MEB yönetmeliğine göre eğitim dönemleri her ayın ilk on günü içinde, kursların belirlediği tarihlerde başlar; bir dönemde en fazla üç farklı tarihte grup açılabilir.'),
        ('Ayın ortasında sürücü kursuna kayıt olunur mu?',
         'Kayıt, grubun başlama tarihinden önce yapılır. Ayın onuncu gününden sonra yeni grup açılmadığı için kayıt genellikle bir sonraki dönemin grubuna yapılır.'),
        ('İlk yardım sertifikam varsa ilk yardım dersine girmem gerekir mi?',
         'Geçerli ilk yardımcı sertifikası olanlar isterlerse ilk yardım dersinden eğitime alınmaz, yalnız sınava girerler.'),
    ],
    sources=['mtsk'],
))

PAGES.append(dict(
    key='devamsizlik',
    title='', desc='Sürücü kursunda devamsızlık hakkı var mı? Teorik derslerin beşte birinden fazlasına girmeyenin kaydı silinir; direksiyon dersinde telafi. MEB yönetmeliğine göre.',
    h1='Sürücü Kursunda Devamsızlık Hakkı Var mı?', crumb='Devamsızlık',
    card='Teorik ve direksiyon derslerinde devam zorunluluğu ve telafi.',
    lead='Sürücü kursunda derslere devam esastır. Yönetmelik teorik ve direksiyon dersleri için ayrı devam kuralları koyar. Bilgiler MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’nin 14. maddesine dayanır.',
    summary=[
        'Teorik derslerin toplam saatinin beşte birinden fazlasına katılmayan kursiyerin kaydı silinir.',
        'Direksiyon derslerinin beşte biri veya daha azına katılamayana bir defaya mahsus telafi programı uygulanır.',
        'Direksiyon telafi derslerinin ücreti kursiyerden alınır.',
    ],
    body='''
<h2>Teorik dersler</h2>
<p>Teorik derslerin toplam saati 34’tür (trafik ve çevre 16, ilk yardım 8, araç tekniği 6, trafik adabı 4). Bu sürenin beşte birinden fazlasına devam etmeyen kursiyerin kaydı silinir. Eğitim personelinin izinli veya raporlu olması ve millî eğitim müdürlüğünün mazereti uygun görmesi hâlinde o günkü ders için telafi eğitimi yapılır (m.14/2).</p>

<h2>Direksiyon dersleri</h2>
<p>Direksiyon eğitimi ders saatinin beşte birine veya daha azına devam etmeyenler için, bir defaya mahsus ve kursiyerin durumu da gözetilerek, o dönemde kurs müdürünün uygun göreceği bir zamanda devam etmediği süre kadar telafi programı uygulanır. Telafi derslerinin ücreti kursiyerden alınır (m.14/2). Direksiyon telafi programına da devam etmeyen kursiyer için yönetmelikte ayrıca hükümler vardır; bu durumda kursunuza danışın.</p>

<h2>Pratik öneri</h2>
<p>Dönem başlamadan ders programını isteyin ve devam edemeyeceğiniz günleri önceden planlayın. Ders saatleri için ''' + a('kayitdonemi', 'sürücü kursu kayıt dönemleri') + ''' yazımıza bakın.</p>
''',
    faq=[
        ('Sürücü kursunda kaç saat devamsızlık hakkı var?',
         'Teorik derslerin toplam saatinin beşte birinden fazlasına devam etmeyen kursiyerin kaydı silinir. 34 saatlik teorik eğitimde bu sınır 6,8 saattir.'),
        ('Direksiyon dersini kaçırırsam ne olur?',
         'Direksiyon ders saatinin beşte biri veya daha azına devam edemeyenlere bir defaya mahsus telafi programı uygulanır; telafi derslerinin ücreti kursiyerden alınır.'),
        ('Öğretmen gelmezse ders telafi edilir mi?',
         'Eğitim personelinin izinli veya raporlu olması ve millî eğitim müdürlüğünün mazereti uygun görmesi hâlinde o günkü ders için telafi eğitimi yapılır.'),
    ],
    sources=['mtsk'],
))

PAGES.append(dict(
    key='nakil',
    title='', desc='Sürücü kursu değiştirilebilir mi? Kurs kapanırsa il içinde nakil, direksiyon sınavında kalanlar için ikinci dört hakta başka kursa geçiş. MEB yönetmeliğine göre.',
    h1='Sürücü Kursu Değiştirilebilir mi?', crumb='Kurs Değiştirme',
    card='Başka kursa nakil hangi durumlarda yapılır.',
    lead='Sürücü kursuna kayıt olduktan sonra başka kursa geçiş (nakil) her durumda serbest değildir; yönetmelik nakli belirli durumlara bağlar. Bilgiler MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’nin 13 ve 15. maddelerine dayanır.',
    summary=[
        'Kurs kapanırsa ya da kapatılırsa kayıtlı kursiyerler il sınırları içinde başka kurslara nakledilir.',
        'Teorik sınavı geçip direksiyon sınavının ilk dört hakkından birinde veya birkaçında başarısız olan kursiyer, isterse ikinci dört hak için başka kursa nakil olabilir.',
        'Nakil işlemlerini nakil yapılacak il millî eğitim müdürlüğü yürütür.',
    ],
    body='''
<h2>Kurs kapanırsa</h2>
<p>Kurucusunun başvurusu ya da inceleme sonucunda kapatılacak veya kapatılan kurslarda kayıtlı kursiyerler, il sınırları içinde başka kurslara nakledilir (m.13/1).</p>

<h2>Direksiyon sınavında başarısız olanlar</h2>
<p>Teorik sınavı geçip direksiyon sınavının ilk dört hakkından biri, birkaçı ya da tamamı sonunda başarısız olan kursiyer, isterse kalan haklarından vazgeçer. Sertifika sınıfı için belirlenen direksiyon ders saati kadar eğitim almak ve ikinci dört sınav hakkını kullanmak üzere, uygun direksiyon ve sınav aracı bulunan başka bir kursa nakil olabilir. Bu kursiyerler, kayıtlı oldukları dönemden sonraki döneme, naklini istedikleri kursun kontenjanına dahil edilerek kaydedilir. İşlemleri nakil yapılacak il millî eğitim müdürlüğü yürütür (m.13/2).</p>
<p>Vites türünü değiştiren kursiyerler de istemeleri hâlinde bu kurala göre başka kursa nakil isteyebilir (m.15/6). Sınav hakları için ''' + a('kalirsam', 'ehliyet sınavında kalınca ne olur') + ''' yazımıza bakın.</p>

<h2>Diğer durumlarda</h2>
<p>Yönetmelik nakli bu iki durumda düzenler. Kursunuzu değiştirmeyi düşünüyorsanız, kayıtlı olduğunuz kursa ve il ya da ilçe millî eğitim müdürlüğüne durumunuzu danışın.</p>
''',
    faq=[
        ('Kayıt olduğum sürücü kursunu değiştirebilir miyim?',
         'Yönetmelik nakli iki durumda düzenler: kursun kapanması ve direksiyon sınavının ilk dört hakkında başarısız olan kursiyerin ikinci dört hak için başka kursa geçmesi.'),
        ('Direksiyon sınavında kaldım, başka kursa geçebilir miyim?',
         'Evet. Teorik sınavı geçip direksiyon sınavının ilk dört hakkından birinde veya birkaçında başarısız olan kursiyer, kalan haklarından vazgeçerek ikinci dört hak için başka kursa nakil olabilir.'),
        ('Nakil işlemini kim yapar?',
         'Nakil işlemlerini nakil yapılacak il millî eğitim müdürlüğü yürütür.'),
    ],
    sources=['mtsk'],
))

PAGES.append(dict(
    key='direksiyon',
    title='', desc='Direksiyon dersi kaç saat, günde kaç saat ders alınır, gece dersi zorunlu mu? B sınıfında en az 14 saat. Ankara’da direksiyon eğitimi kuralları.',
    h1='Direksiyon Dersi Kaç Saat, Nasıl İşler?', crumb='Direksiyon Dersi',
    card='Ders saatleri, gece sürüşü, ek ders ve emniyet kemeri eğitimi.',
    lead='Direksiyon eğitimi, e-Sınav’ı geçtikten sonra başlar ve sınıfa göre belirlenen en az ders saatiyle yürür. Bilgiler MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’nin 6, 7, 12, 14, 16 ve 16/A maddelerine dayanır.',
    summary=[
        'Direksiyon dersleri teorik sınavı geçen kursiyerlerle başlar; önce eğitim alanında veya simülatörde en az 2 saat ders verilir.',
        'B sınıfında akan trafikte en az 14 saat ders alınır, bunun en az 2 saati gece sürüşüdür.',
        'Direksiyon dersi günde en fazla 2 saat yapılır; kendini yeterli görmeyen kursiyer ek ders alabilir.',
    ],
    body='''
<h2>Ders akışı</h2>
<ul>
<li>Direksiyon eğitimine başlamadan önce bütün adaylara emniyet kemeri simülasyon eğitimi verilir (m.16/A).</li>
<li>Önce eğitim alanında veya simülatörde en az 2 saat ders verilir; usta öğretici adayın trafiğe hazır olduğuna karar verince akan trafikte devam edilir (m.7/1).</li>
<li>Akan trafikteki en az ders saati sınıfa göre değişir: B 14, A1 ve A2 12, C 20, D 14 saattir. Tüm sınıflar için ''' + a('siniflar', 'ehliyet sınıfları') + ''' yazımıza bakın.</li>
<li>Çoğu sınıfta en az 2 saat gece sürüşü zorunludur; sağlık raporunda gece kısıtı olanlara gece dersi verilmez (m.7/3).</li>
<li>Dersler her kursiyer için ayrı ayrı ve günde en fazla 2 saat yapılır (m.16/4).</li>
</ul>

<h2>K sınıfı sürücü aday belgesi</h2>
<p>Akan trafikte ders başladığı tarihten itibaren 6 ay geçerli K sınıfı sürücü aday belgesi düzenlenir; bu belge eğitim ve sınavda kullanılır (m.6/3). Ayrıntılar ''' + a('kbelgesi', 'K sınıfı sürücü aday belgesi') + ''' yazımızda.</p>

<h2>Ek ders ve vites seçimi</h2>
<p>Direksiyon dersleri sonunda kendini yeterli görmeyen kursiyer isterse akan trafikte ek ders alır ve o yıl ilan edilen ders ücretini öder (m.7/4). e-Sınav’ı geçen kursiyer, direksiyon ders planlaması yapılmadan önce yazılı başvuruyla aynı sınıfın manuel ya da otomatik seçeneğine geçebilir (m.12/5).</p>

<h2>Ankara Sincan’da</h2>
<p>Kursumuzun direksiyon dersleri OSB Törekent parkurunda yapılır; ardından akan trafikte devam edilir.</p>
''',
    faq=[
        ('B sınıfı ehliyet için kaç saat direksiyon dersi alınır?',
         'Eğitim alanında veya simülatörde en az 2 saatin ardından akan trafikte en az 14 saat direksiyon dersi alınır; bunun en az 2 saati gece sürüşüdür.'),
        ('Günde kaç saat direksiyon dersi alınabilir?',
         'MEB yönetmeliğine göre direksiyon dersleri her kursiyer için günde en fazla 2 saat yapılır.'),
        ('Direksiyon dersi yetmezse ek ders alınır mı?',
         'Evet. Kendini yeterli görmeyen kursiyer isterse akan trafikte ek ders alır ve o yıl ilan edilen ders ücretini öder.'),
    ],
    sources=['mtsk'],
))

PAGES.append(dict(
    key='kbelgesi',
    title='', desc='K sınıfı sürücü aday belgesi nedir, ne zaman verilir, kaç ay geçerlidir, bu belgeyle tek başına araç kullanılır mı? Yönetmeliklere göre.',
    h1='K Sınıfı Sürücü Aday Belgesi Nedir?', crumb='K Belgesi',
    card='Eğitim ve sınavda kullanılan aday belgesi ve geçerlilik süresi.',
    lead='Sürücü kursunda direksiyon eğitimi alan adaylar için K sınıfı sürücü aday belgesi düzenlenir. Bu belge bir ehliyet değildir; yalnız eğitim ve sınav içindir.',
    summary=[
        'K sınıfı sürücü aday belgesi, araç sürmeyi öğrenen adaylara eğitim ve sınavda kullanmak üzere verilir.',
        'Belgeyi kurs müdürlüğü düzenler; akan trafikte direksiyon dersinin başladığı tarihten itibaren 6 ay geçerlidir.',
        'Karayolunda tek başına araç kullanmak için ehliyet (sürücü belgesi) gerekir.',
    ],
    body='''
<h2>Belge ne işe yarar?</h2>
<p>Karayolları Trafik Yönetmeliği’ne göre K sınıfı sürücü aday belgesi, yönetmelikteki şartlara göre araç sürmeyi öğrenen adaylara eğitim ve sınavda kullanmak üzere verilir (m.75). MEB yönetmeliğine göre bu belgeyi kurs müdürlüğü düzenler ve belge, akan trafikte direksiyon eğitiminin başladığı tarihten itibaren 6 ay geçerlidir (m.6/3).</p>

<h2>Belgeyle tek başına araç kullanılır mı?</h2>
<p>Hayır. Belge yalnız eğitim ve sınav için verilir. Karayolunda araç kullanmak için ehliyet gerekir; sınavları geçtikten sonra alınan sertifika da tek başına araç kullanma yetkisi vermez. Ehliyet için nüfus müdürlüğüne başvurulur. Ayrıntılar ''' + a('sertifika', 'sürücü sertifikası') + ''' ve ''' + a('randevu', 'ehliyet randevusu') + ''' yazılarımızda.</p>

<h2>6 ay dolarsa</h2>
<p>Direksiyon derslerinin teorik sınavı geçtiğiniz tarihten itibaren 90 gün içinde tamamlanacak şekilde planlanması öngörülür (m.15). Süreyle ilgili sorunuz olursa kursunuza danışın; ders planı için ''' + a('direksiyon', 'direksiyon dersi') + ''' yazımıza bakın.</p>
''',
    faq=[
        ('K sınıfı sürücü aday belgesi kaç ay geçerlidir?',
         'MEB yönetmeliğine göre akan trafikte direksiyon eğitiminin başladığı tarihten itibaren 6 ay geçerlidir.'),
        ('K belgesiyle tek başına araç kullanılır mı?',
         'Hayır. K sınıfı sürücü aday belgesi yalnız eğitim ve sınavda kullanılmak üzere verilir.'),
        ('K belgesini kim verir?',
         'Belgeyi kursiyerin kayıtlı olduğu kursun müdürlüğü düzenler.'),
    ],
    sources=['kty', 'mtsk', 'nvi_sss'],
))

PAGES.append(dict(
    key='sertifika',
    title='', desc='Sürücü sertifikası nedir, nereden alınır, süresi var mı, sertifikayla araç kullanılır mı? e-Devlet ve NVİ bilgileriyle sertifikadan ehliyete.',
    h1='Sürücü Sertifikası Nedir, Ne İşe Yarar?', crumb='Sürücü Sertifikası',
    card='Sınav sonrası sertifika, e-Devlet ve ehliyete dönüşüm.',
    lead='Sürücü kursundaki sınavları geçen aday önce motorlu taşıt sürücüsü sertifikası alır; ehliyet (sürücü belgesi) bu sertifikaya dayanarak nüfus müdürlüğünde düzenlenir. Bilgiler MEB yönetmeliğinin 37 ve 38. maddelerine ve NVİ açıklamalarına dayanır.',
    summary=[
        'Sertifika elektronik olarak düzenlenir ve e-Devlet üzerinden görülür.',
        '09.07.2022 ve sonrasında alınan sertifikalarda süre sınırı yoktur.',
        'Sertifika, ehliyetle değiştirilmedikçe karayolunda araç kullanma yetkisi vermez.',
    ],
    body='''
<h2>Sertifika nasıl düzenlenir?</h2>
<p>Sertifika, sertifika almaya hak kazanılan son sınav tarihi yazılarak elektronik ortamda düzenlenir ve e-Devlet üzerinden erişilir (m.37). Sertifika bilgileri, imza, fotoğraf ve sağlık raporu, ehliyetin düzenlenmesine esas olmak üzere elektronik olarak Nüfus ve Vatandaşlık İşleri Genel Müdürlüğüne iletilir. Sertifikanın iptali kursun bağlı olduğu il millî eğitim müdürlüğünce yapılır (m.38).</p>

<h2>Süresi var mı?</h2>
<p>NVİ’ye göre 09.07.2022 ve sonrasında alınan sürücü sertifikalarında süre sınırlaması yoktur.</p>

<h2>Sertifikayla araç kullanılır mı?</h2>
<p>Hayır. NVİ’ye göre sürücü sertifikası ehliyetle değiştirilmedikçe karayolunda araç kullanma yetkisi vermez. Ehliyet için randevu alıp nüfus müdürlüğüne başvurmanız, harç, değerli kâğıt bedeli ve vakıf payını ödemeniz gerekir. Ayrıntılar ''' + a('randevu', 'ehliyet randevusu') + ''' ve ''' + a('masraf', 'ehliyet masrafları') + ''' yazılarımızda.</p>

<h2>B ehliyetle A1 yetkisi</h2>
<p>B ehliyeti en az iki yıllık olanların aldığı A1 sertifikası, ehliyete ayrıca işlenmeden sistem kayıtlarına eklenir. Ayrıntılar ''' + a('motor', 'B ehliyetle motosiklet') + ''' yazımızda.</p>
''',
    faq=[
        ('Sürücü sertifikası nereden alınır?',
         'Sınavları geçen adayın sertifikası elektronik olarak düzenlenir ve e-Devlet üzerinden görülür.'),
        ('Sürücü sertifikasının süresi var mı?',
         'NVİ’ye göre 09.07.2022 ve sonrasında alınan sertifikalarda süre sınırlaması yoktur.'),
        ('Sertifikayla araç kullanabilir miyim?',
         'Hayır. Sertifika, nüfus müdürlüğünde ehliyetle değiştirilmedikçe karayolunda araç kullanma yetkisi vermez.'),
    ],
    sources=['mtsk', 'nvi_sss'],
))

PAGES.append(dict(
    key='esinavkural',
    title='', desc='e-Sınava girerken yanınızda ne olmalı, binaya neler alınmaz, geç kalırsanız ne olur, kopyanın yaptırımı nedir? MEB 2026 e-Sınav Kılavuzuna göre.',
    h1='e-Sınava Girerken Nelere Dikkat Edilmeli?', crumb='e-Sınav Kuralları',
    card='Sınav günü belgeler, yasak eşyalar, geç kalma ve kopya kuralları.',
    lead='e-Sınav’da kurallara uyulmadığında sınav iptal edilebilir. Aşağıdaki bilgiler MEB’in 2026 Motorlu Taşıt Sürücü Kursiyerleri e-Sınav Kılavuzuna dayanır.',
    summary=[
        'Sınav saatinden en geç 30 dakika önce salonda olun; e-Sınav giriş belgesi ve geçerli kimlik belgesi olmadan sınava alınmazsınız.',
        'Sınav başladıktan sonra 15 dakika içinde gelen aday sınava alınır ama ek süre verilmez; 15 dakikadan sonra gelen alınmaz.',
        'Kopya çeken ya da yerine başkasını sokan adayın sınavı iptal edilir ve 2 yıl MEB sınavlarına giremez.',
    ],
    body='''
<h2>Yanınızda olması gerekenler</h2>
<ul>
<li>e-Sınav giriş belgesi. T.C. kimlik kartıyla gelen adayların giriş belgesinde imza ve mühür aranmaz.</li>
<li>Geçerli kimlik belgesi: süresi dolmamış T.C. kimlik kartı ya da pasaport; yabancılar için kılavuzda sayılan belgeler.</li>
</ul>

<h2>Sınav binasına alınmayanlar</h2>
<p>Cep telefonu, her türlü saat, çanta, cüzdan, anahtarlık, elektronik anahtar, kulaklık, takılar, kitap ve not, yiyecek ve içecek sınav binasına alınmaz. Doktor raporuyla belirlenen cihaz ve ilaçlar, anahtarlıksız basit anahtar, ulaşım kartı, kâğıt para, alyans, şeffaf şişede su ve şeffaf numaralı gözlük istisnadır.</p>

<h2>Sınav sırasında</h2>
<ul>
<li>Kimlik kontrolüyle salona alınan aday sınav başlayana kadar dışarı çıkamaz; kendi isteğiyle çıkan tekrar alınmaz ve sınavı iptal edilir.</li>
<li>Sınav başladıktan sonra ilk 15 dakika içinde gelen aday alınır ama ek süre verilmez; 15 dakikadan sonra gelen alınmaz. Sınavın ilk 15 dakikasında salondan çıkılamaz.</li>
<li>Kopya çekmek, kopyaya teşebbüs etmek ya da yerine başkasını sokmak sınavın iptaline yol açar ve aday, sınav tarihinden itibaren 2 yıl boyunca MEB Ölçme, Değerlendirme ve Sınav Hizmetleri Genel Müdürlüğünün hiçbir sınavına başvuramaz.</li>
</ul>
<p>Sınavın yapısı ve puanlama için ''' + a('sinav', 'ehliyet sınavı') + ''' yazımıza bakın.</p>
''',
    faq=[
        ('e-Sınava giderken yanımda ne olmalı?',
         'e-Sınav giriş belgesi ve süresi dolmamış T.C. kimlik kartı ya da pasaport gibi geçerli bir kimlik belgesi olmalıdır.'),
        ('e-Sınava geç kalırsam ne olur?',
         'Sınav başladıktan sonra ilk 15 dakika içinde gelen aday sınava alınır ama ek süre verilmez; 15 dakikadan sonra gelen aday salona alınmaz.'),
        ('e-Sınava telefonla girilir mi?',
         'Hayır. Cep telefonu, saat, çanta ve elektronik cihazlar sınav binasına alınmaz.'),
    ],
    sources=['esinav'],
))

PAGES.append(dict(
    key='esinavitiraz',
    title='', desc='e-Sınav sonucu nereden öğrenilir, sorulara ve sonuca itiraz nasıl yapılır, itiraz ücreti ve süresi nedir? MEB 2026 e-Sınav Kılavuzuna göre.',
    h1='e-Sınav Sonucuna İtiraz Edilir mi?', crumb='e-Sınav İtirazı',
    card='Sonuç öğrenme, 5 günlük itiraz süresi ve itiraz ücreti.',
    lead='e-Sınav’ın sonucu sınav biter bitmez açıklanır. Sonuca ya da sorulara itiraz etmek mümkündür ama süre kısadır. Bilgiler MEB’in 2026 e-Sınav Kılavuzuna dayanır.',
    summary=[
        'Sonuç, sınav merkezindeki sonuç ekranından ya da oturum bittikten sonra esinav.meb.gov.tr adresinden öğrenilir; ayrıca tebligat yapılmaz.',
        'Sorulara ve sonuca itiraz, sonucun yayımlanmasından itibaren 5 takvim günü içinde, 75 TL itiraz ücreti ödenerek e-İtiraz Modülünden yapılır.',
        'İtiraz, 10 günlük dava açma süresini durdurmaz.',
    ],
    body='''
<h2>Sonuç nasıl öğrenilir?</h2>
<p>Sonuç, sınav merkezindeki sonuç açıklama cihazından ya da oturum bittikten sonra esinav.meb.gov.tr adresinden öğrenilir; adaylara ayrıca tebligat yapılmaz. Sınav soruları ve cevapları yayımlanmaz. 70 ve üzeri puan başarılıdır.</p>

<h2>İtiraz nasıl yapılır?</h2>
<ul>
<li>Sınav sonucuna ve sorulara itiraz, sonucun yayımlanmasından itibaren 5 takvim günü içinde yapılır.</li>
<li>Kendi T.C. kimlik numaranızla Ziraat Bankası, Vakıfbank veya Halkbank üzerinden KDV dahil 75 TL itiraz ücreti yatırılır ve başvuru e-İtiraz Modülünden (eitiraz.meb.gov.tr) yapılır.</li>
<li>Sınavın uygulanışına ilişkin itirazlar dilekçeyle il veya ilçe millî eğitim müdürlüğüne şahsen yapılır.</li>
<li>Süre dışında itiraz yapılamaz.</li>
</ul>
<p>İtiraz, sonucun yayımlanmasıyla başlayan 10 günlük dava açma süresini durdurmaz. İptal edilen sorular değerlendirme dışı bırakılır ve puan geçerli sorular üzerinden yeniden hesaplanır.</p>

<h2>Kaldıysanız</h2>
<p>e-Sınav’da kalan aday, kursa yeniden devam etmeden ve yalnız sınav ücretini ödeyerek üç kez daha sınava girebilir. Ayrıntılar ''' + a('kalirsam', 'ehliyet sınavında kalınca ne olur') + ''' yazımızda.</p>
''',
    faq=[
        ('e-Sınav sonucu ne zaman açıklanır?',
         'Sonuç sınav bitince açıklanır; sınav merkezindeki sonuç ekranından ya da oturum bittikten sonra esinav.meb.gov.tr adresinden öğrenilir.'),
        ('e-Sınav sonucuna itiraz ücreti ne kadar?',
         '2026 kılavuzuna göre itiraz ücreti KDV dahil 75 TL’dir; itiraz, sonucun yayımlanmasından itibaren 5 takvim günü içinde e-İtiraz Modülünden yapılır.'),
        ('İtiraz dava açma süresini durdurur mu?',
         'Hayır. Kılavuza göre itiraz, sonucun yayımlanmasıyla başlayan 10 günlük dava açma süresini durdurmaz.'),
    ],
    sources=['esinav', 'esinav_site'],
))

PAGES.append(dict(
    key='geripark',
    title='', desc='Direksiyon sınavında geri park nasıl yapılır, kaç hamle hakkı var, park alanı ne kadar? B sınıfı sınavında park, geri gitme ve dönüş aşamaları.',
    h1='Direksiyon Sınavında Geri Park Nasıl Yapılır?', crumb='Geri Park',
    card='Park alanı ölçüleri, hamle hakları ve diğer manevralar.',
    lead='B sınıfı direksiyon sınavının en çok merak edilen aşaması koniler arasına geri parktır. Yönetmelik bu aşamayı ölçüleriyle tarif eder. Bilgiler MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’nin 34. maddesine dayanır.',
    summary=[
        'Araç, en az 100 cm yüksekliğindeki konilerin arasına geri geri ve tek hamlede girilerek park edilir; giremeyene bir hak daha verilir.',
        'Koniler arasına giren araç en fazla iki hamlede, konilere ve kaldırıma değmeden, ön tekerler düz ve kaldırıma paralel park edilir.',
        'Park bitince “Park işlemini tamamladım.” denir; değerlendirme bundan sonra yapılır.',
    ],
    body='''
<h2>Park alanı</h2>
<p>Park alanının boyu, park edecek aracın bir buçuk katı; eni ise aracın genişliğinden 50 cm fazladır. Alan kaldırımdan 50 cm açıkta yatay çizgiyle belirlenir; konilerin yerleri dikey çizgilerle işaretlenir. Hatchback ve sedan gibi farklı uzunluktaki araçlar için ayrı park alanları düzenlenir.</p>

<h2>Geri park adımları</h2>
<ol>
<li>Aracı geriye doğru, tek hamlede koniler arasına sokun. Giremezseniz bu hamleyi yeniden yapmak için bir hak daha verilir.</li>
<li>Koniler arasına giren aracı en fazla iki hamlede, kaldırıma ve konilere değmeden, ön tekerleri düz konuma getirerek kaldırıma paralel park edin.</li>
<li>Park bitince “Park işlemini tamamladım.” deyin; komisyon değerlendirmeyi bundan sonra yapar.</li>
</ol>

<h2>Parktan sonraki manevralar</h2>
<ul>
<li>İçten içe en fazla 3,5 metre genişliğindeki şeritte, lastikleri çizgiye veya kaldırıma değdirmeden 25 metre geri gitme.</li>
<li>Geri giderken sağa (L) dönüş; tek hamlede ve çizgi, kaldırım veya konilere değmeden. Bitince “Dönüş işlemini tamamladım.” denir.</li>
<li>Dar alanda en fazla üç hamlede geri dönüş.</li>
<li>Güzergâhta yol için belirlenen azami hıza ulaşma ve 30 km/s hızla giderken komutla ani fren.</li>
</ul>
<p>Sınavın tamamı için ''' + a('sinav', 'ehliyet sınavı') + ''' yazımıza bakın. Ankara Sincan’daki kursumuzda direksiyon dersleri OSB Törekent parkurunda yapılır.</p>
''',
    faq=[
        ('Direksiyon sınavında geri parkta kaç hak var?',
         'Koniler arasına tek hamlede girilmesi istenir; giremeyen adaya bu hamleyi yeniden yapması için bir hak daha verilir. Girdikten sonra araç en fazla iki hamlede park edilir.'),
        ('Park alanı ne kadar büyük?',
         'Park alanının boyu aracın bir buçuk katı, eni ise aracın genişliğinden 50 cm fazladır.'),
        ('Park bitince ne söylenir?',
         'Aday “Park işlemini tamamladım.” der; komisyon değerlendirmeyi bundan sonra yapar.'),
    ],
    sources=['mtsk'],
))

PAGES.append(dict(
    key='motorsinav',
    title='', desc='Motosiklet direksiyon sınavında neler istenir? Slalom, sekiz çizme, denge çizgisi, U dönüşü, hız ve ani fren. MEB yönetmeliğine göre A1, A2 ve A sınavı.',
    h1='Motosiklet Direksiyon Sınavı Nasıl Yapılır?', crumb='Motosiklet Sınavı',
    card='Slalom, sekiz, denge çizgisi, U dönüşü ve ani fren.',
    lead='M, A1, A2, A ve B1 sınıflarının direksiyon sınavı önce kapalı bir sınav alanında, sonra trafikte yapılır. Bilgiler MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’nin 35. maddesine dayanır.',
    summary=[
        'Sınav alanında araç bilgisi soruları, dokuz koni arasında slalom, sekiz çizme, denge çizgisi ve dar alanda U dönüşü istenir.',
        'A1, A2 ve A sınıflarında 30 metrede 40 km/s hıza ulaşıp sonraki 30 metrede durmak gerekir; M sınıfında bu hız 25 km/s’tir.',
        'Alanda başarılı olan adayın sınavı güzergâhta, trafikte devam eder.',
    ],
    body='''
<h2>Sınav alanındaki aşamalar</h2>
<ol>
<li>Araç bilgisini ölçen sorular.</li>
<li>Motoru çalıştırıp hareket etme.</li>
<li>Sağdan başlayarak dokuz koni arasında slalom.</li>
<li>Yedi metre çapındaki iki çember içinde sekiz çizme (B1 hariç).</li>
<li>20 metre uzunluğunda, 20 cm genişliğindeki denge çizgisi üzerinden geçiş (B1 hariç).</li>
<li>6 metre genişliğinde, 8 metre uzunluğundaki alanda, tekerlekler dışarı çıkmadan ve konilere değmeden U dönüşü (B1 hariç).</li>
<li>30 metrede M sınıfı için 25 km/s, A1, A2, A ve B1 için 40 km/s hıza ulaşıp sonraki 30 metrede yavaşlayarak durma.</li>
<li>20 km/s hızdayken 1 metre genişliğindeki engele en fazla 3 metre kala şeritten ayrılıp engelin yanındaki 100 cm’lik bölümden geçme ve şeride dönme (B1 hariç).</li>
<li>20 km/s hızdayken ani fren.</li>
</ol>
<p>Sınav alanındaki değerlendirmeler tek seferde tamamlanır. Alanda başarılı olan adayın sınavı güzergâhta, akan trafikte devam eder ve değerlendirme formundaki trafikte sürüş becerilerine göre değerlendirilir.</p>

<h2>Hazırlık</h2>
<p>Motosiklet sınıflarının yaş ve ders saatleri için ''' + a('motosiklet', 'motosiklet ehliyeti') + ''' yazımıza bakın. Kursumuzda <a href="/egitim/motor-a1/">A1</a> ve <a href="/egitim/motor-a2/">A2 motosiklet</a> eğitimleri verilir.</p>
''',
    faq=[
        ('Motor ehliyeti sınavında neler yapılır?',
         'Sınav alanında slalom, sekiz çizme, denge çizgisi, dar alanda U dönüşü, hızlanıp durma, engelden kaçınma ve ani fren istenir; ardından trafikte sürüş değerlendirilir.'),
        ('Motosiklet sınavında sekiz çizme var mı?',
         'Evet. Yedi metre çapındaki iki çember içinde sekiz çizilir; B1 sınıfında bu aşama yoktur.'),
        ('Motosiklet sınavında hangi hıza çıkılır?',
         'A1, A2 ve A sınıflarında 30 metrede 40 km/s hıza ulaşılıp sonraki 30 metrede durulur; M sınıfında bu hız 25 km/s’tir.'),
    ],
    sources=['mtsk'],
))

PAGES.append(dict(
    key='mazeret',
    title='', desc='Ehliyet sınavı günü hastalanırsanız, askere giderseniz ya da hamileyseniz ne olur? e-Sınav randevusu değiştirme ve mazeret belgeleri.',
    h1='Ehliyet Sınavına Giremezsem Ne Olur?', crumb='Sınav Mazereti',
    card='Hastalık, askerlik, hamilelik ve randevu değişikliği.',
    lead='Ehliyet sınavına girememek her zaman hak kaybı demek değildir; yönetmelik mazeret durumlarını ayrıca düzenler. Bilgiler MEB yönetmeliğinin 15. maddesine ve 2026 e-Sınav Kılavuzuna dayanır.',
    summary=[
        'Randevu alınan e-Sınav’a gelinmezse bir sınav hakkı kullanılmış sayılır.',
        'Belgeli mazereti olan aday, sınavdan en az 24 saat önce il veya ilçe millî eğitim müdürlüğüne başvurarak randevusunu değiştirebilir.',
        'Hastalık raporu 2 iş günü, afet veya yakın kaybı gibi durumların belgesi 10 gün içinde kursa verilmelidir.',
    ],
    body='''
<h2>e-Sınav randevusu</h2>
<p>Randevusu onaylanan aday belirlenen gün ve saatte sınava girmek zorundadır; girmezse bir sınav hakkını kullanmış sayılır ve ücret iadesi isteyemez. Mazeretini belgeleyen aday, sınav saatinden en az 24 saat önce il veya ilçe millî eğitim müdürlüğüne başvurarak randevusunu değiştirebilir.</p>

<h2>Mazeret türleri</h2>
<ul>
<li><strong>Hastalık:</strong> sınav günü sınava girecek durumda olmadığını sağlık kuruluşundan alacağı raporla belgeleyen aday, raporu en geç 2 iş günü içinde kursa teslim eder.</li>
<li><strong>Afet, yakınların ağır hastalığı veya ölümü, ülkeyi temsil:</strong> resmî makamdan alınan belge 10 gün içinde kursa teslim edilir.</li>
<li>Bu iki durumda mazereti kabul edilen aday, dört dönem sınav hakkını tamamlayıp başarılı olamazsa bir defaya mahsus mazeret sınavına girebilir.</li>
<li><strong>Askerlik:</strong> belgeleriyle kursa yazılı bildirim yapılır; terhisten itibaren 10 gün içinde başvurulursa kalan haklar ilçedeki ilk sınavdan itibaren kullandırılır.</li>
<li><strong>Hamilelik veya doğum:</strong> doktor raporuyla 10 gün içinde yazılı bildirim yapılır; kalan haklar rapor süresi bitince kullandırılır.</li>
<li><strong>Uzun süren tedavi:</strong> sağlık kurulu raporuyla belgelenir; tedavi bitince 10 gün içinde başvurulursa kalan haklar kullandırılır.</li>
</ul>
<p>Askerlik, hamilelik ve uzun tedavi durumlarında kayıt millî eğitim müdürlüğünce dondurulur (m.15/3). Sınav hakları için ''' + a('kalirsam', 'ehliyet sınavında kalınca ne olur') + ''' yazımıza bakın.</p>
''',
    faq=[
        ('e-Sınav randevusunu değiştirebilir miyim?',
         'Belgelenmiş mazeretiniz varsa sınav saatinden en az 24 saat önce il veya ilçe millî eğitim müdürlüğüne başvurarak değiştirebilirsiniz.'),
        ('Sınav günü hastalanırsam hakkım yanar mı?',
         'Sağlık kuruluşundan aldığınız raporu en geç 2 iş günü içinde kursa teslim ederseniz mazeretiniz değerlendirilir; kabul edilirse haklarınızı tamamladıktan sonra bir defaya mahsus mazeret sınavına girebilirsiniz.'),
        ('Askere gidersem kursum ne olur?',
         'Belgeleriyle kursa yazılı bildirim yaparsanız kaydınız dondurulur; terhisten itibaren 10 gün içinde başvurursanız kalan sınav haklarınız kullandırılır.'),
    ],
    sources=['mtsk', 'esinav'],
))

# ── Parti 3b: sınıflar, şartlar, psikoteknik ───────────────────────
PAGES.append(dict(
    key='yas16',
    title='', desc='16 yaşında hangi ehliyet alınır? M (moped), A1 motosiklet ve B1 sınıfı; veli izni, ders saatleri ve 18 yaş şartı olan sınıflar.',
    h1='16 Yaşında Hangi Ehliyet Alınır?', crumb='16 Yaşında Ehliyet',
    card='M, A1 ve B1 sınıfları, veli izni ve ders saatleri.',
    lead='Otomobil ehliyeti için 18 yaş beklemek gerekir, ama bazı sınıflar 16 yaşında alınabilir. Bilgiler Karayolları Trafik Yönetmeliği’nin 75 ve 76. maddeleri ile MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’ne dayanır.',
    summary=[
        '16 yaşını bitirenler M, A1 ve B1 sınıfı ehliyet alabilir.',
        '18 yaşını doldurmamış adaylardan kurs kaydında veli veya vasi muvafakatnamesi istenir.',
        'Otomobil (B) ve A2 motosiklet için 18 yaş gerekir.',
    ],
    body='''
<h2>16 yaşında alınabilen sınıflar</h2>
<ul>
<li><strong>M:</strong> iki, üç ve dört tekerlekli motorlu bisikletler (moped).</li>
<li><strong>A1:</strong> silindir hacmi 125 cm³’ü, gücü 11 kW’ı geçmeyen motosikletler ve gücü 15 kW’ı geçmeyen üç tekerlekli motosikletler.</li>
<li><strong>B1:</strong> net motor gücü 15 kW’ı, net ağırlığı 400 kg’ı (yük taşımada 550 kg’ı) geçmeyen dört tekerlekli motosikletler.</li>
</ul>
<p>Bu üç sınıfta akan trafikte en az 12 saat direksiyon dersi alınır. A1 ehliyetiyle M sınıfı araçlar da kullanılabilir (Karayolları Trafik Yönetmeliği m.85).</p>

<h2>Kayıt için</h2>
<p>Belgeler diğer adaylarla aynıdır; 18 yaşını doldurmamış kursiyerler için ayrıca veli veya vasi muvafakatnamesi istenir (MTSK Yönetmeliği m.11). Teorik dersler ve e-Sınav tüm sınıflarda aynıdır. Liste için ''' + a('belgeler', 'ehliyet için gerekli belgeler') + ''' yazımıza bakın.</p>

<h2>18 yaşında</h2>
<p>A2 motosiklet ve B sınıfı otomobil ehliyeti 18 yaşını bitirince alınır. Yaş tablosunun tamamı ''' + a('siniflar', 'ehliyet sınıfları') + ''' yazımızda. Kursumuzda <a href="/egitim/motor-a1/">A1 motosiklet</a> eğitimi verilir.</p>
''',
    faq=[
        ('16 yaşında ehliyet alınır mı?',
         'Evet. 16 yaşını bitirenler M (moped), A1 (hafif motosiklet) ve B1 (dört tekerlekli motosiklet) sınıfı ehliyet alabilir.'),
        ('16 yaşında hangi motor kullanılır?',
         'A1 ehliyetiyle silindir hacmi 125 cm³’ü ve gücü 11 kW’ı geçmeyen motosikletler kullanılır.'),
        ('18 yaşından küçükler için veli izni gerekir mi?',
         'Evet. 18 yaşını doldurmamış kursiyerlerden kurs kaydında veli veya vasi muvafakatnamesi istenir.'),
    ],
    sources=['kty', 'mtsk'],
))

PAGES.append(dict(
    key='romork',
    title='', desc='B ehliyetle römork çekilir mi? 750 kg’a kadar hafif römork, 4.250 kg birleşik araç kuralı ve BE sınıfı ehliyet. Karayolları Trafik Yönetmeliğine göre.',
    h1='B Ehliyetle Römork Çekilir mi?', crumb='Römork ve BE',
    card='Hafif römork sınırı, 4.250 kg kuralı ve BE sınıfı.',
    lead='Karavan, tekne ya da yük römorku çekmek isteyenlerin en çok sorduğu soru, B ehliyetin yetip yetmeyeceğidir. Cevap römorkun ağırlığına bağlıdır. Bilgiler Karayolları Trafik Yönetmeliği’nin 75, 76 ve 86. maddelerine dayanır.',
    summary=[
        'B sınıfı ehliyetle azami yüklü ağırlığı 750 kg’a kadar (750 kg dahil) hafif römork takılabilir.',
        'Yönetmelikteki eğitimi tamamlayan ya da sınavı geçen B sahibi, azami yüklü ağırlığı 4.250 kg’a kadar birleşik araçları da kullanabilir.',
        'Daha ağır römorklar için BE sınıfı gerekir: B ehliyeti şarttır, akan trafikte 6 saat ders alınır.',
    ],
    body='''
<h2>Hafif römork</h2>
<p>B, C, C1, D ve D1 sınıfı ehliyet sahipleri araçlarına azami yüklü ağırlığı 750 kg’a kadar (750 kg dahil) hafif römork takarak kullanabilir (m.86).</p>

<h2>4.250 kg kuralı</h2>
<p>B sınıfı ehliyet sahibi; tip onayı mevzuatına aykırı olmamak ve MEB yönetmeliğinde belirtilen eğitimi tamamlamak ya da yetenek ve davranış sınavını geçmiş olmak kaydıyla, azami yüklü ağırlığı 4.250 kg’a kadar olan birleşik araçları da kullanabilir (m.75).</p>

<h2>BE sınıfı</h2>
<p>BE sınıfı; B ehliyetiyle kullanılan araca takılan ve azami yüklü ağırlığı 3.500 kg’ı geçmeyen römork veya yarı römorklu birleşik araçlar için verilir. BE için 18 yaş ve B ehliyeti gerekir (m.76). B sahibinin BE eklemesi için akan trafikte 6 saat direksiyon dersi alınır ve sınav römork takılı araçla yapılır. 2026’da BE harcı 11.271,20 TL’dir. Sınıf ekleme için ''' + a('ekleme', 'ehliyete sınıf ekleme') + ''' yazımıza bakın.</p>
''',
    faq=[
        ('B ehliyetle karavan çekilir mi?',
         'Azami yüklü ağırlığı 750 kg’a kadar olan hafif römork B ehliyetle çekilebilir. Daha ağır römorklar için 4.250 kg kuralının şartları ya da BE sınıfı gerekir.'),
        ('BE ehliyeti için kaç saat ders gerekir?',
         'B ehliyeti olan biri BE için akan trafikte 6 saat direksiyon dersi alır; sınav römork takılı araçla yapılır.'),
        ('BE ehliyet kaç yaşında alınır?',
         'BE için 18 yaşını bitirmiş olmak ve B sınıfı ehliyete sahip olmak gerekir.'),
    ],
    sources=['kty', 'mtsk', 'nvi_ucret'],
))

PAGES.append(dict(
    key='kamyon',
    title='', desc='Kamyon ehliyeti (C ve C1) nasıl alınır? Yaş şartı, B ehliyeti şartı, direksiyon ders saati, sağlık şartı, 5 yıllık geçerlilik ve 2026 harcı.',
    h1='Kamyon Ehliyeti (C Sınıfı) Nasıl Alınır?', crumb='Kamyon Ehliyeti',
    card='C ve C1 sınıfı: yaş, ön şart, ders saati ve geçerlilik.',
    lead='Kamyon ehliyeti iki sınıftan oluşur: orta ağırlıktaki kamyonlar için C1, bütün kamyon ve çekiciler için C. Bilgiler Karayolları Trafik Yönetmeliği ile MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’ne dayanır.',
    summary=[
        'C1: azami yüklü ağırlığı 3.500-7.500 kg arası kamyon ve çekiciler; 18 yaş ve B ehliyeti gerekir.',
        'C: tüm kamyon ve çekiciler; 21 yaş ve B ehliyeti gerekir.',
        'C1 ve C ehliyetleri 5 yıl geçerlidir; sağlık muayenesinde ikinci grup şartları uygulanır.',
    ],
    body='''
<h2>Şartlar ve ders saatleri</h2>
<div class="guide-table"><table>
<thead><tr><th>Sınıf</th><th>Yaş</th><th>Ön şart</th><th>Akan trafikte ders</th></tr></thead>
<tbody>
<tr><td>C1</td><td>18</td><td>B</td><td>10 saat</td></tr>
<tr><td>C</td><td>21</td><td>B</td><td>20 saat</td></tr>
<tr><td>CE (römorklu)</td><td>21</td><td>C</td><td>6 saat</td></tr>
</tbody></table></div>
<p>Ders saatleri B ehliyeti olanlar için yönetmelikteki tabloya göredir. C ehliyetiyle M, B, B1, C1 ve F sınıfı araçlar da kullanılabilir (Karayolları Trafik Yönetmeliği m.85).</p>

<h2>Sağlık ve geçerlilik</h2>
<p>C1, C1E, C ve CE sınıfları sağlık muayenesinde ikinci gruptadır; görme şartı daha sıkıdır (Sürücü Sağlık Yönetmeliği m.4-5). Bu sınıflardaki ehliyetler 5 yıl geçerlidir (Karayolları Trafik Yönetmeliği m.87).</p>

<h2>Masraf</h2>
<p>2026’da C1, C ve CE sınıflarının harcı 11.271,20 TL’dir; değerli kâğıt bedeli ve vakıf payıyla toplam 13.386,20 TL ödenir. Diğer kalemler için ''' + a('masraf', 'ehliyet masrafları') + ''' yazımıza bakın. Kursumuzdaki seçenekler için <a href="/egitim/diger/">büyük araç ehliyetleri</a> sayfamıza bakabilirsiniz.</p>
''',
    faq=[
        ('Kamyon ehliyeti kaç yaşında alınır?',
         'C1 sınıfı için 18, C sınıfı için 21 yaşını bitirmiş olmak ve en az B sınıfı ehliyete sahip olmak gerekir.'),
        ('C ehliyeti için kaç saat ders gerekir?',
         'B ehliyeti olan biri C sınıfı için akan trafikte 20 saat, C1 için 10 saat direksiyon dersi alır.'),
        ('C ehliyeti kaç yıl geçerlidir?',
         'C1, C1E, C ve CE sınıfı ehliyetler 5 yıl geçerlidir.'),
    ],
    sources=['kty', 'mtsk', 'saglik', 'nvi_ucret'],
))

PAGES.append(dict(
    key='otobus',
    title='', desc='Otobüs ve minibüs ehliyeti (D ve D1) nasıl alınır? Yaş şartı, B ehliyeti şartı, direksiyon ders saati, sağlık şartı ve 5 yıllık geçerlilik.',
    h1='Otobüs Ehliyeti (D Sınıfı) Nasıl Alınır?', crumb='Otobüs Ehliyeti',
    card='D ve D1 sınıfı: yaş, ön şart, ders saati ve geçerlilik.',
    lead='Yolcu taşıyan büyük araçlar için iki sınıf vardır: minibüs için D1, minibüs ve otobüs için D. Bilgiler Karayolları Trafik Yönetmeliği ile MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’ne dayanır.',
    summary=[
        'D1 minibüs için verilir; 21 yaş ve B ehliyeti gerekir.',
        'D minibüs ve otobüs için verilir; 24 yaş ve B ehliyeti gerekir.',
        'D1 ve D ehliyetleri 5 yıl geçerlidir; sağlık muayenesinde ikinci grup şartları uygulanır.',
    ],
    body='''
<h2>Şartlar ve ders saatleri</h2>
<div class="guide-table"><table>
<thead><tr><th>Sınıf</th><th>Yaş</th><th>Ön şart</th><th>Akan trafikte ders</th></tr></thead>
<tbody>
<tr><td>D1</td><td>21</td><td>B</td><td>7 saat</td></tr>
<tr><td>D</td><td>24</td><td>B</td><td>14 saat</td></tr>
<tr><td>DE (römorklu)</td><td>24</td><td>D</td><td>6 saat</td></tr>
</tbody></table></div>
<p>Ders saatleri B ehliyeti olanlar için yönetmelikteki tabloya göredir. D ehliyetiyle M, B, B1, D1 ve F sınıfı araçlar da kullanılabilir (Karayolları Trafik Yönetmeliği m.85).</p>

<h2>Sağlık ve geçerlilik</h2>
<p>D1, D1E, D ve DE sınıfları sağlık muayenesinde ikinci gruptadır (Sürücü Sağlık Yönetmeliği m.4-5) ve bu sınıflardaki ehliyetler 5 yıl geçerlidir (Karayolları Trafik Yönetmeliği m.87).</p>

<h2>Masraf</h2>
<p>2026’da D1, D ve DE sınıflarının harcı 11.271,20 TL’dir; değerli kâğıt bedeli ve vakıf payıyla toplam 13.386,20 TL ödenir. Kursumuzdaki seçenekler için <a href="/egitim/diger/">büyük araç ehliyetleri</a> sayfamıza bakabilirsiniz.</p>
''',
    faq=[
        ('Otobüs ehliyeti kaç yaşında alınır?',
         'D sınıfı otobüs ehliyeti için 24, D1 sınıfı minibüs ehliyeti için 21 yaşını bitirmiş olmak ve B ehliyetine sahip olmak gerekir.'),
        ('D ehliyeti için kaç saat ders gerekir?',
         'B ehliyeti olan biri D sınıfı için akan trafikte 14 saat, D1 için 7 saat direksiyon dersi alır.'),
        ('D ehliyeti kaç yıl geçerlidir?',
         'D1, D1E, D ve DE sınıfı ehliyetler 5 yıl geçerlidir.'),
    ],
    sources=['kty', 'mtsk', 'saglik', 'nvi_ucret'],
))

PAGES.append(dict(
    key='traktor',
    title='', desc='Traktör ehliyeti (F sınıfı) nasıl alınır? 18 yaş şartı, ders saati, römorklu sınav, B ehliyetin traktörü kapsaması ve 2026 harcı.',
    h1='Traktör Ehliyeti (F Sınıfı) Nasıl Alınır?', crumb='Traktör Ehliyeti',
    card='F sınıfı: yaş, ders saati, römorklu sınav ve B ehliyet.',
    lead='Lastik tekerlekli traktör kullanmak için F sınıfı ehliyet gerekir; ancak B ehliyeti olanlar traktörü de kullanabilir. Bilgiler Karayolları Trafik Yönetmeliği ile MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği’ne dayanır.',
    summary=[
        'F sınıfı lastik tekerlekli traktör kullanacaklara verilir; 18 yaş gerekir.',
        'B sınıfı ehliyet sahipleri F sınıfı araçları da kullanabilir.',
        'F sınıfında akan trafikte en az 12 saat ders alınır; sınav traktörün katar ağırlığına uygun römorkla yapılır.',
    ],
    body='''
<h2>Şartlar</h2>
<p>F sınıfı ehliyet lastik tekerlekli traktör kullanacaklara verilir ve 18 yaşını bitirmiş olmak gerekir (Karayolları Trafik Yönetmeliği m.75-76). F ehliyetiyle M sınıfı araçlar da kullanılabilir; B, C ve D sınıfı ehliyet sahipleri ise F sınıfı araçları da kullanabilir (m.85).</p>

<h2>Eğitim ve sınav</h2>
<p>F sınıfında akan trafikte en az 12 saat direksiyon dersi alınır ve en az 2 saati gece sürüşüdür (MTSK Yönetmeliği m.7). Direksiyon sınavı, sınavın yapılacağı traktörün katar ağırlığına uygun römorkla yapılır (m.36). Yönetmelikteki genel hız sınırı traktörler için yerleşim yeri içinde 20, şehirlerarası çift yönlü yolda 30, bölünmüş yolda 40 km/s’tir; otoyola giremez.</p>

<h2>Masraf</h2>
<p>2026’da F sınıfı harcı 2.239,90 TL’dir; değerli kâğıt bedeli ve vakıf payıyla toplam 4.354,90 TL ödenir. Diğer kalemler için ''' + a('masraf', 'ehliyet masrafları') + ''' yazımıza bakın.</p>
''',
    faq=[
        ('B ehliyetle traktör kullanılır mı?',
         'Evet. Karayolları Trafik Yönetmeliği’nin 85. maddesine göre B sınıfı ehliyetle F sınıfı araçlar, yani lastik tekerlekli traktörler de kullanılabilir.'),
        ('Traktör ehliyeti kaç yaşında alınır?',
         'F sınıfı traktör ehliyeti için 18 yaşını bitirmiş olmak gerekir.'),
        ('Traktör ehliyeti harcı ne kadar?',
         '2026’da F sınıfı harcı 2.239,90 TL’dir; değerli kâğıt bedeli ve vakıf payıyla toplam 4.354,90 TL ödenir.'),
    ],
    sources=['kty', 'mtsk', 'nvi_ucret'],
))

PAGES.append(dict(
    key='ismakinesi',
    title='', desc='İş makinesi ehliyeti (G sınıfı) nasıl alınır? Operatörlük belgesi şartı, 18 yaş, e-Sınav ve sağlık şartı. MEB yönetmeliği ve Karayolları Trafik Yönetmeliğine göre.',
    h1='İş Makinesi Ehliyeti (G Sınıfı) Nasıl Alınır?', crumb='İş Makinesi Ehliyeti',
    card='G sınıfı: operatörlük belgesi şartı, yaş ve sınav.',
    lead='İş makinesi türündeki motorlu araçlarla karayoluna çıkmak için G sınıfı ehliyet gerekir. Bu sınıfın kursa kayıt şartı diğerlerinden farklıdır. Bilgiler MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği ve Karayolları Trafik Yönetmeliği’ne dayanır.',
    summary=[
        'G sınıfı sertifika için kursa kayıt olabilmek için İş Makinesi Kullanma Yetki Belgesi (operatörlük belgesi) gerekir.',
        'Operatörlük belgesi olup ehliyeti olmayanlar, teorik eğitimi alıp e-Sınav’ı geçince lastik tekerlekli iş makinesi için G sertifikası alır.',
        'G sınıfı için 18 yaş gerekir; sağlık muayenesinde ikinci grup şartları uygulanır.',
    ],
    body='''
<h2>Kayıt şartı</h2>
<p>G sınıfı sürücü sertifikası almak üzere kursa kayıt olabilmek için İş Makinesi Kullanma Yetki Belgesi (operatörlük belgesi) gerekir (MTSK Yönetmeliği m.12/3).</p>

<h2>Eğitim ve sınav</h2>
<p>Operatörlük belgesine sahip olup ehliyeti bulunmayan ve G sınıfı için kursa kayıt olan kursiyerlere, teorik dersleri alıp e-Sınav’da başarılı olmaları hâlinde lastik tekerlekli iş makinesi kullanmak için G sınıfı sertifika verilir (m.6/2). e-Sınav 50 soru ve 45 dakikadır, 70 puan başarılı sayılır.</p>

<h2>Diğer şartlar</h2>
<p>G sınıfı ehliyet iş makinesi türündeki motorlu araçları kullanacaklara verilir ve 18 yaşını bitirmiş olmak gerekir (Karayolları Trafik Yönetmeliği m.75-76). G ehliyetiyle M sınıfı araçlar da kullanılabilir (m.85). G sınıfı sağlık muayenesinde ikinci gruptadır (Sürücü Sağlık Yönetmeliği m.4). Ehliyet 10 yıl geçerlidir (Karayolları Trafik Yönetmeliği m.87). 2026’da G sınıfı harcı 11.271,20 TL’dir.</p>
''',
    faq=[
        ('İş makinesi ehliyeti için operatörlük belgesi şart mı?',
         'Evet. MEB yönetmeliğine göre G sınıfı sertifika için kursa kayıt olabilmek için İş Makinesi Kullanma Yetki Belgesi (operatörlük belgesi) gerekir.'),
        ('G sınıfı için direksiyon sınavı var mı?',
         'Operatörlük belgesi olup ehliyeti olmayanlara, teorik dersleri alıp e-Sınav’ı geçmeleri hâlinde lastik tekerlekli iş makinesi için G sertifikası verilir.'),
        ('G sınıfı ehliyet kaç yaşında alınır?',
         'G sınıfı ehliyet için 18 yaşını bitirmiş olmak gerekir.'),
    ],
    sources=['mtsk', 'kty', 'saglik', 'nvi_ucret'],
))

PAGES.append(dict(
    key='sabika',
    title='', desc='Sabıka kaydı ehliyet almaya engel mi? Karayolları Trafik Yönetmeliğinde sayılan suçlar, kurs kaydındaki adli sicil belgesi ve gerçeğe aykırı beyanın sonucu.',
    h1='Sabıka Kaydı Ehliyet Almaya Engel mi?', crumb='Sabıka Kaydı',
    card='Hangi suç kayıtları engel, adli sicil belgesi nasıl kontrol edilir.',
    lead='Ehliyet almak için adli sicil şartı vardır, ancak bu şart her suç kaydını kapsamaz; yönetmelik belirli suçları sayar. Bilgiler Karayolları Trafik Yönetmeliği’nin 76. maddesine, MEB yönetmeliğinin 11. maddesine ve NVİ açıklamalarına dayanır.',
    summary=[
        'Engel sayılan kayıtlar, yönetmelikte madde numaralarıyla sayılan suçlardan hüküm giymiş olmaktır.',
        'Kurs kaydında adli sicil kaydını gösteren barkodlu belge istenir; Bakanlık ayrıca yetkili adli mercilerden teyit eder.',
        'Gerçeğe aykırı beyanda bulunan kursiyer sınava alınmaz; sınava girmişse sınavı geçersiz sayılır ve kaydı silinir.',
    ],
    body='''
<h2>Hangi suçlar engel?</h2>
<p>Karayolları Trafik Yönetmeliği’ne göre ehliyet alacakların adli sicilinde şu suçlardan hüküm giydiğine dair kayıt bulunmamalıdır (m.76/1-e):</p>
<ul>
<li>Türk Ceza Kanunu’nun 188, 190 ve 191. maddeleri (uyuşturucu veya uyarıcı madde suçları).</li>
<li>Kaçakçılıkla Mücadele Kanunu’nun 4. maddesinin yedinci fıkrası.</li>
<li>6136 sayılı Ateşli Silahlar ve Bıçaklar ile Diğer Aletler Hakkında Kanun’un 12. maddesinin ikinci ve sonraki fıkraları.</li>
</ul>
<p>Yönetmelikteki adli sicil şartı bu suçlarla sınırlıdır. NVİ de aynı listeyi ehliyet şartı olarak açıklar.</p>

<h2>Kurs kaydında</h2>
<p>Kayıtta, ehliyet almaya engel sabıka kaydı olmadığını gösteren barkodlu belge istenir; bu belgeyi e-Devlet’teki Adli Sicil Kaydı Sorgulama hizmetinden alabilirsiniz. Bakanlık ayrıca yetkili adli mercilerden teyit eder. Gerçeğe aykırı beyanda bulunduğu tespit edilen kursiyer sınava alınmaz; sınava girmişse sınavı geçersiz sayılır ve kaydı silinir (MTSK Yönetmeliği m.11).</p>

<h2>Ehliyet başvurusunda</h2>
<p>Nüfus müdürlüğündeki ehliyet başvurusunda adli sicil kaydı sistemden kontrol edilir. Diğer belgeler için ''' + a('belgeler', 'ehliyet için gerekli belgeler') + ''' yazımıza bakın.</p>
''',
    faq=[
        ('Her sabıka kaydı ehliyet almaya engel mi?',
         'Hayır. Karayolları Trafik Yönetmeliği belirli suçları sayar: TCK 188, 190 ve 191. maddeler, Kaçakçılıkla Mücadele Kanunu 4/7 ve 6136 sayılı Kanun’un 12. maddesinin ikinci ve sonraki fıkraları.'),
        ('Sürücü kursu adli sicil belgesi ister mi?',
         'Evet. Kayıtta ehliyet almaya engel sabıka kaydı olmadığını gösteren barkodlu belge istenir; Bakanlık ayrıca adli mercilerden teyit eder.'),
        ('Adli sicil belgesi nereden alınır?',
         'Barkodlu adli sicil kaydı belgesi e-Devlet’teki Adli Sicil Kaydı Sorgulama hizmetinden alınabilir.'),
    ],
    sources=['kty', 'mtsk', 'nvi_sss', 'adli'],
))

PAGES.append(dict(
    key='diploma',
    title='', desc='Diploma olmadan ehliyet alınır mı? En az ilkokul şartı, diploma yerine geçen belgeler, kaybolan diploma ve yurt dışında alınan öğrenim belgesi.',
    h1='Diploma Olmadan Ehliyet Alınır mı?', crumb='Öğrenim Şartı',
    card='İlkokul şartı, diploma yerine geçen belgeler ve yurt dışı diploma.',
    lead='Ehliyet için öğrenim şartı vardır ama diplomanın kendisi tek seçenek değildir. Bilgiler Karayolları Trafik Yönetmeliği’nin 76. maddesine, MEB yönetmeliğinin 11. maddesine ve NVİ açıklamalarına dayanır.',
    summary=[
        'Ehliyet için en az ilkokul düzeyinde öğrenim görmüş olmak gerekir.',
        'Kursa kayıtta diploma, diploma yerine geçen belge ya da bir kamu kurumundan alınan öğrenim durumu belgesi kabul edilir.',
        'Yurt dışında alınan öğrenim belgelerinin noter tasdikli Türkçe tercümesi istenir.',
    ],
    body='''
<h2>Öğrenim şartı</h2>
<p>Karayolları Trafik Yönetmeliği’ne göre ehliyet alacakların en az ilkokul düzeyinde eğitim almış olması gerekir (m.76/1-c).</p>

<h2>Kabul edilen belgeler</h2>
<ul>
<li>Diploma.</li>
<li>Diploma yerine geçen belge.</li>
<li>Kamu kurum veya kuruluşlarından alınan, öğrenim durumunu bildiren belge.</li>
</ul>
<p>Kurs bu belgelerin aslını görerek onaylı örneğini alır (MTSK Yönetmeliği m.11). Diplomanızı kaybettiyseniz okulunuzdan ya da ilgili kamu kurumundan alacağınız öğrenim durumu belgesiyle kayıt olabilirsiniz.</p>

<h2>Yurt dışında okuyanlar</h2>
<p>Yurt dışından alınan öğrenim belgelerinin noter tasdikli Türkçe tercümesi istenir. NVİ, ehliyet başvurusunda öğrenim belgesini sistemden kontrol eder. Türkçe bilmeyen adaylar için tercüman ve yabancı dilde e-Sınav imkânı ''' + a('yabanci', 'yabancılar için ehliyet') + ''' yazımızda.</p>
''',
    faq=[
        ('Ehliyet için hangi okul mezuniyeti gerekir?',
         'Karayolları Trafik Yönetmeliği’ne göre en az ilkokul düzeyinde eğitim almış olmak gerekir.'),
        ('Diplomamı kaybettim, ehliyet kursuna kayıt olabilir miyim?',
         'Evet. Diploma yerine geçen belge ya da bir kamu kurumundan alınan öğrenim durumu belgesi de kabul edilir.'),
        ('Yurt dışında aldığım diploma geçerli mi?',
         'Yurt dışından alınan öğrenim belgelerinin noter tasdikli Türkçe tercümesi istenir.'),
    ],
    sources=['kty', 'mtsk', 'nvi_sss'],
))

PAGES.append(dict(
    key='yabanci',
    title='', desc='Yabancılar Türkiye’de nasıl ehliyet alır? Kayıt belgeleri, 6 aylık ikamet şartı, tercümanla eğitim ve yabancı dilde e-Sınav.',
    h1='Yabancılar Türkiye’de Nasıl Ehliyet Alır?', crumb='Yabancılar İçin Ehliyet',
    card='Belgeler, ikamet şartı, tercüman ve yabancı dilde e-Sınav.',
    lead='Türkiye’de yaşayan yabancılar da sürücü kursuna kayıt olarak ehliyet alabilir. Türkçe bilmeyenler için tercüman ve yabancı dilde sınav imkânı vardır. Bilgiler MEB yönetmeliğinin 11 ve 16. maddelerine, 2026 e-Sınav Kılavuzuna ve NVİ açıklamalarına dayanır.',
    summary=[
        'Kayıt tarihinden itibaren Türkiye’de en az altı ay kalacağını gösteren ikamet izni, öğrenim vizesi veya çalışma izni gerekir.',
        'Türkçe bilmeyen kursiyerler için valilik izniyle tercüman görevlendirilir; tercüman teorik ve direksiyon derslerine girer.',
        'Teorik eğitimi tercümanla tamamlayan aday, e-Sınav’a MEB’in belirlediği yabancı dillerde girebilir; dil seçimi sınavdan en az 48 saat önce sisteme işlenmelidir.',
    ],
    body='''
<h2>Kayıt belgeleri</h2>
<ul>
<li>Pasaportun noter tasdikli Türkçe tercümesi veya geçici koruma kimlik belgesi.</li>
<li>Kayıt tarihinden itibaren Türkiye’de en az altı ay kalacağını gösteren ikamet izni, öğrenim vizesi veya çalışma izni.</li>
<li>Öğrenim belgesinin noter tasdikli Türkçe tercümesi.</li>
<li>Sürücü olur raporu ve son altı ayda çekilmiş biyometrik fotoğraf.</li>
<li>Cumhuriyet başsavcılığı veya kaymakamlıktan alınan adli sicil belgesi.</li>
<li>18 yaşını doldurmamış adaylar için veli veya vasi muvafakatnamesi.</li>
</ul>

<h2>Tercüman ve yabancı dilde sınav</h2>
<p>Türkçe bilmeyen yabancı uyruklu kursiyerlere eğitim verecek kurslarda, valilik izniyle yeminli bir tercüman ya da yabancı dil bilgisi yeterli bulunan bir kişi görevlendirilir; tercüman teorik ve direksiyon derslerine girer. Kursiyer isterse direksiyon sınavında da tercüman görevlendirilir (m.16/6). Teorik eğitimini tercümanla tamamlayan aday, e-Sınav’a MEB’in belirlediği yabancı dillerde girebilir. Bunun için dil seçiminin sınav randevusundan en az 48 saat önce sisteme işlenmesi gerekir; işlenmezse sorular Türkçe gelir. Geçici koruma kimlik belgesi olan adaylar e-Sınav’a yalnız belgede yazan ikamet ilinde girebilir.</p>

<h2>Yabancı ehliyeti olanlar</h2>
<p>NVİ’ye göre yurt dışından alınan ehliyetle yabancılar Türkiye’de 6 ay araç kullanabilir. Ayrıntılar ''' + a('yurtdisi', 'yurt dışı ehliyeti') + ''' yazımızda.</p>
''',
    faq=[
        ('Yabancılar Türkiye’de ehliyet alabilir mi?',
         'Evet. Kayıt tarihinden itibaren en az altı ay Türkiye’de kalacağını gösteren ikamet izni, öğrenim vizesi veya çalışma izni olan yabancılar sürücü kursuna kayıt olabilir.'),
        ('e-Sınav yabancı dilde yapılır mı?',
         'Teorik eğitimini tercümanla tamamlayan yabancı uyruklu aday, e-Sınav’a MEB’in belirlediği yabancı dillerde girebilir; dil seçimi sınavdan en az 48 saat önce sisteme işlenmelidir.'),
        ('Türkçe bilmeyen kursiyere tercüman verilir mi?',
         'Kurslarda valilik izniyle tercüman görevlendirilir; tercüman teorik ve direksiyon derslerine girer, kursiyer isterse direksiyon sınavında da bulunur.'),
    ],
    sources=['mtsk', 'esinav', 'nvi_sss'],
))

PAGES.append(dict(
    key='fotograf',
    title='', desc='Ehliyet fotoğrafı nasıl olmalı? Biyometrik ve son altı ayda çekilmiş olma şartı, kurs kaydında ve nüfus müdürlüğünde fotoğraf. NVİ ve MEB yönetmeliğine göre.',
    h1='Ehliyet Fotoğrafı Nasıl Olmalı?', crumb='Ehliyet Fotoğrafı',
    card='Biyometrik fotoğraf şartı, kurs kaydı ve nüfus başvurusu.',
    lead='Ehliyet sürecinde fotoğraf iki yerde istenir: sürücü kursuna kayıtta ve nüfus müdürlüğündeki ehliyet başvurusunda. Bilgiler NVİ açıklamalarına ve MEB yönetmeliğinin 11 ve 12. maddelerine dayanır.',
    summary=[
        'Fotoğraf son altı ay içinde çekilmiş ve ICAO standartlarına uygun biyometrik olmalıdır.',
        'Fotokopi, bilgisayarda çoğaltılmış ya da biyometrik olmayan fotoğraf kabul edilmez.',
        'Kursumuzda kayıt için 1 adet biyometrik fotoğraf yeterlidir.',
    ],
    body='''
<h2>Fotoğraf şartları</h2>
<p>NVİ’ye göre ehliyette kullanılacak fotoğraf, kişinin son hâlini göstermesi için son altı ay içinde çekilmiş ve Uluslararası Sivil Havacılık Teşkilatı (ICAO) standartlarına uygun biyometrik olmalıdır. Fotokopi, bilgisayarda çoğaltılmış ya da biyometrik olmayan fotoğraflar kabul edilmez.</p>

<h2>Kurs kaydında</h2>
<p>Kurs, kayıt sırasında yüzünüzün net görüldüğü bir fotoğrafınızı da çeker; biyometrik fotoğrafınız ve belgeleriniz taranarak sisteme aktarılır. Kayıt bilgileri size onaylatılır; fotoğrafı veya bilgileri hatalı girilen kursiyerde o dönem düzeltme yapılmaz (MTSK Yönetmeliği m.12). Kursumuzda kayıt için 1 adet biyometrik fotoğraf yeterlidir.</p>

<h2>Nüfus müdürlüğünde</h2>
<p>Ehliyet başvurusunda 1 adet biyometrik fotoğraf istenir; fotoğraf taranarak sisteme kaydedildikten sonra size iade edilir. Başvuru günü için ''' + a('randevu', 'ehliyet randevusu') + ''' yazımıza bakın.</p>
''',
    faq=[
        ('Ehliyet için nasıl fotoğraf gerekir?',
         'Son altı ay içinde çekilmiş, ICAO standartlarına uygun biyometrik fotoğraf gerekir; fotokopi veya biyometrik olmayan fotoğraf kabul edilmez.'),
        ('Ehliyet başvurusunda kaç fotoğraf istenir?',
         'NVİ, ehliyet başvurusunda 1 adet biyometrik fotoğraf ister; fotoğraf taranıp sisteme kaydedildikten sonra iade edilir.'),
        ('Sürücü kursu kaydı için kaç fotoğraf gerekir?',
         'Kursumuzda kayıt için 1 adet biyometrik fotoğraf yeterlidir; kurs ayrıca kayıt sırasında sizin bir fotoğrafınızı çeker.'),
    ],
    sources=['nvi_sss', 'mtsk'],
))

PAGES.append(dict(
    key='psikoteknik',
    title='', desc='Psikoteknik değerlendirme ne zaman istenir? Aday belgesinin iptali, ikinci 100 ceza puanı, tekrarlanan alkol, kırmızı ışık ve hız ihlalleri.',
    h1='Psikoteknik Değerlendirme Ne Zaman İstenir?', crumb='Psikoteknik',
    card='Hangi ihlallerden sonra psikoteknik ve psikiyatri muayenesi gerekir.',
    lead='Psikoteknik değerlendirme, bazı ihlallerden sonra ehliyetin iadesi ya da yeniden alınması için aranır ve çoğunlukla psikiyatri uzmanı muayenesiyle birlikte istenir. Bilgiler Karayolları Trafik Kanunu’nun 2026’da değişen maddelerine ve MEB yönetmeliğinin 11. maddesine dayanır.',
    summary=[
        'Aday sürücü belgesi iptal edilenler ve ehliyeti iptal edilip yeniden kursa kayıt olanlar için psikoteknik değerlendirme ve psikiyatri muayenesi istenir.',
        'Aynı yıl ikinci kez 100 ceza puanını dolduranlar ile beş yıl içinde üçüncü kez alkollü araç kullananlar değerlendirmeye alınır.',
        'Kırmızı ışık ve hız ihlallerinde belirli sayıya ulaşınca ehliyet, psikoteknik değerlendirme sonucuna göre iade edilir.',
    ],
    body='''
<h2>Hangi durumlarda istenir?</h2>
<ul>
<li><strong>Aday sürücü belgesinin iptali:</strong> yeniden kursa başlamak için psikoteknik değerlendirme ve psikiyatri uzmanı muayenesinde engel hâli olmadığını gösteren belge kursa verilir (Ek 17).</li>
<li><strong>İkinci 100 ceza puanı:</strong> aynı yıl ikinci kez 100 puanı dolduranın ehliyeti 4 ay geri alınır; psikoteknik değerlendirme ve psikiyatri muayenesi yapılır (m.118).</li>
<li><strong>Alkol:</strong> beş yıl içinde üç veya daha fazla kez alkol nedeniyle ehliyeti geri alınanlar psikoteknik değerlendirmeye ve psikiyatri muayenesine alınır; ikincisinde sürücü davranışlarını geliştirme eğitimi uygulanır (m.48).</li>
<li><strong>Uyuşturucu:</strong> ehliyeti iptal edilen kişinin yeniden kursa başlaması için en az beş yıl geçmesi, psikoteknik değerlendirmeden geçmesi ve resmî sağlık kurulu raporu gerekir (m.48).</li>
<li><strong>Kırmızı ışık:</strong> bir yıl içinde üç, dört veya beş ihlalde geri alınan ehliyet, süre sonunda psikoteknik değerlendirmede engel çıkmazsa iade edilir; altıncıda ehliyet iptal edilir (m.47).</li>
<li><strong>Hız:</strong> bir yıl içinde beşinci kez geri alınan ehliyet, psikoteknik değerlendirme ve psikiyatri muayenesinde engel çıkmazsa iade edilir (m.51).</li>
</ul>

<h2>Sonuçlar farklı çıkarsa</h2>
<p>MEB yönetmeliğine göre psikoteknik değerlendirme merkezi ile psikiyatri uzmanının rapor sonuçları farklıysa psikiyatri uzmanının kararı geçerlidir. Geri alma süreleri dolmadan kursa müracaat kabul edilmez (MTSK Yönetmeliği m.11).</p>
<p>İlgili kurallar ''' + a('aday', 'aday sürücü belgesi') + ''', ''' + a('ceza', 'ehliyet ceza puanı') + ''' ve ''' + a('alkol', 'alkollü araç kullanma cezası') + ''' yazılarımızda.</p>
''',
    faq=[
        ('Psikoteknik değerlendirme ne zaman istenir?',
         'Aday belgesinin iptali, aynı yıl ikinci kez 100 ceza puanı, beş yıl içinde üçüncü alkol ihlali, uyuşturucu nedeniyle iptal ve tekrarlanan kırmızı ışık ya da hız ihlallerinde istenir.'),
        ('Psikoteknik ile psikiyatri raporu farklı çıkarsa hangisi geçerli?',
         'MEB yönetmeliğine göre psikiyatri uzmanının kararı geçerlidir.'),
        ('Aday belgesi iptal olan kursa ne zaman başvurabilir?',
         'Varsa iptal nedenlerindeki geri alma süreleri dolmadan kursa müracaat kabul edilmez; ayrıca psikoteknik ve psikiyatri belgeleri gerekir.'),
    ],
    sources=['ktk', 'mtsk'],
))

# ── Parti 3c: trafik kuralları ve cezalar ───────────────────────────
TUTAR_NOTU = ('<p class="guide-note">Tutarlar Karayolları Trafik Kanunu’nun 12.02.2026 tarihli 7574 sayılı Kanunla değişen metnindeki tutarlardır. '
              'Kabahatler Kanunu’na göre idari para cezaları her takvim yılı başında yeniden değerleme oranında artırılır.</p>')

PAGES.append(dict(
    key='alkol',
    title='', desc='Alkollü araç kullanmanın cezası 2026’da ne kadar? 0.50 promil sınırı, ehliyetin 6 ay, 2 yıl ve 5 yıl geri alınması, ölçüm yaptırmama ve uyuşturucu.',
    h1='Alkollü Araç Kullanmanın Cezası Nedir?', crumb='Alkol Cezası',
    card='Promil sınırları, 2026 cezaları ve ehliyetin geri alınması.',
    lead='Alkollü araç kullanmak hem para cezası hem ehliyetin geri alınmasıyla sonuçlanır ve tekrarlandıkça ağırlaşır. Bilgiler Karayolları Trafik Kanunu’nun 12.02.2026’da değişen 48. maddesine dayanır.',
    summary=[
        'Hususi otomobil sürücülerinde sınır 0.50 promil, diğer araçlarda 0.20 promildir.',
        'İlk ihlalde 25.000 TL idari para cezası verilir ve ehliyet 6 ay geri alınır.',
        'Beş yıl içinde ikincisinde 50.000 TL ve 2 yıl, üçüncüsünde 150.000 TL ve her seferinde 5 yıl geri alma uygulanır.',
    ],
    body='''
<h2>Promil sınırları</h2>
<p>Hususi otomobil sürücüleri için 0.50 promilin, hususi otomobil dışındaki araçları kullananlar için 0.20 promilin üzeri alkollü araç kullanma sayılır. Aday sürücülerde, araç cinsine bakılmaksızın 0.20 promilin üzeri aday belgenin iptaline yol açar (Ek 17). Ayrıntılar ''' + a('aday', 'aday sürücü belgesi') + ''' yazımızda.</p>

<h2>Cezalar ve geri alma süreleri</h2>
<div class="guide-table"><table>
<thead><tr><th>Beş yıl içinde</th><th>Para cezası</th><th>Ehliyet</th></tr></thead>
<tbody>
<tr><td>İlk kez</td><td>25.000 TL</td><td>6 ay geri alınır</td></tr>
<tr><td>İkinci kez</td><td>50.000 TL</td><td>2 yıl geri alınır</td></tr>
<tr><td>Üç ve daha fazla</td><td>150.000 TL</td><td>Her seferinde 5 yıl</td></tr>
</tbody></table></div>
<p>İkinci kez ehliyeti geri alınanlar sürücü davranışlarını geliştirme eğitimine, üç ve daha fazlasında psikoteknik değerlendirme ve psikiyatri muayenesine alınır. 1.00 promilin üzerinde alkollü olanlar hakkında ayrıca Türk Ceza Kanunu’nun 179/3 maddesi uygulanır; alkollüyken kazaya sebep olanlar hakkında da ceza kanunu hükümleri uygulanır. Geri alınan ehliyetin iadesi için idari para cezalarının tamamının ödenmiş olması gerekir.</p>

<h2>Ölçüm yaptırmamak ve uyuşturucu</h2>
<ul>
<li>Kolluğun alkol veya uyuşturucu ölçümünü yaptırmayan sürücüye 150.000 TL idari para cezası verilir ve ehliyeti 5 yıl geri alınır.</li>
<li>Uyuşturucu veya uyarıcı madde aldığı tespit edilen sürücüye 150.000 TL idari para cezası verilir ve ehliyeti iptal edilir; yeniden ehliyet için en az beş yıl beklemek, kursa devam edip sınavları geçmek gerekir.</li>
</ul>
''' + TUTAR_NOTU,
    faq=[
        ('Alkollü araç kullanma cezası 2026’da ne kadar?',
         'Kanunun 2026 metnine göre ilk ihlalde 25.000 TL idari para cezası verilir ve ehliyet 6 ay geri alınır; beş yıl içinde ikincisinde 50.000 TL ve 2 yıl, üçüncüsünde 150.000 TL ve 5 yıl uygulanır.'),
        ('Alkol sınırı kaç promil?',
         'Hususi otomobil sürücüleri için 0.50 promil, diğer araç sürücüleri için 0.20 promildir. Aday sürücülerde her araç için 0.20 promilin üzeri aday belgenin iptaline yol açar.'),
        ('Alkol ölçümünü reddedersem ne olur?',
         'Ölçüm yaptırmayan sürücüye 150.000 TL idari para cezası verilir ve ehliyeti 5 yıl geri alınır.'),
    ],
    sources=['ktk', 'kabahat'],
))

PAGES.append(dict(
    key='hiz',
    title='', desc='Hız sınırları nedir, aşınca ceza ne kadar, ehliyet ne zaman geri alınır? Şehir içi 50, otoyol 120 km/s; 2026 hız cezaları tablosu.',
    h1='Hız Sınırları Nedir, Aşınca Ne Olur?', crumb='Hız Sınırı Cezası',
    card='Araç cinsine göre hız sınırları ve 2026 hız cezaları.',
    lead='Hız sınırları araç cinsine ve yol türüne göre değişir. 2026’da yapılan değişiklikle hız cezaları kademeli hâle geldi ve büyük aşımlarda ehliyet geri alınıyor. Bilgiler Karayolları Trafik Yönetmeliği’nin 100. maddesine ve Karayolları Trafik Kanunu’nun 51. maddesine dayanır.',
    summary=[
        'Otomobilde genel sınırlar: yerleşim yeri içinde 50, şehirlerarası çift yönlü yolda 90, bölünmüş yolda 110, otoyolda 120 km/s.',
        'Yerleşim yeri içinde 6-10 km/s aşım 2.000 TL’den başlar, 66 km/s ve üzeri aşım 30.000 TL’ye çıkar.',
        'Büyük aşımlarda ehliyet her seferinde 30, 60 veya 90 gün geri alınır.',
    ],
    body='''
<h2>Genel hız sınırları (km/s)</h2>
<div class="guide-table"><table>
<thead><tr><th>Araç</th><th>Yerleşim içi</th><th>Çift yönlü yol</th><th>Bölünmüş yol</th><th>Otoyol</th></tr></thead>
<tbody>
<tr><td>Otomobil</td><td>50</td><td>90</td><td>110</td><td>120</td></tr>
<tr><td>Minibüs, otobüs</td><td>50</td><td>80</td><td>90</td><td>100</td></tr>
<tr><td>Kamyonet</td><td>50</td><td>80</td><td>85</td><td>95</td></tr>
<tr><td>Kamyon, çekici</td><td>50</td><td>80</td><td>85</td><td>90</td></tr>
<tr><td>Motosiklet (L3)</td><td>50</td><td>80</td><td>90</td><td>100</td></tr>
</tbody></table></div>
<p>Bunlar yönetmelikteki genel sınırlardır; levhayla farklı bir sınır belirlenen yerde levhaya uyulur.</p>

<h2>Hız cezaları (2026)</h2>
<div class="guide-table"><table>
<thead><tr><th>Aşım</th><th>Yerleşim içi</th><th>Yerleşim dışı</th></tr></thead>
<tbody>
<tr><td>Küçük aşım</td><td>6-10 km/s: 2.000 TL</td><td>11-15 km/s: 2.000 TL</td></tr>
<tr><td>Orta aşım</td><td>26-35 km/s: 12.000 TL</td><td>31-40 km/s: 12.000 TL</td></tr>
<tr><td>30 gün geri alma</td><td>46-55 km/s: 20.000 TL</td><td>51-60 km/s: 20.000 TL</td></tr>
<tr><td>60 gün geri alma</td><td>56-65 km/s: 25.000 TL</td><td>61-70 km/s: 25.000 TL</td></tr>
<tr><td>90 gün geri alma</td><td>66 ve üzeri: 30.000 TL</td><td>71 ve üzeri: 30.000 TL</td></tr>
</tbody></table></div>
<p>Aradaki kademeler de kanunda ayrı ayrı belirlenmiştir. Geri alınan ehliyetin iadesi için idari para cezalarının tamamının ödenmiş olması gerekir. Bir yıl içinde beşinci kez geri alınan ehliyet, psikoteknik değerlendirme ve psikiyatri muayenesinden sonra iade edilir. Radar yerini tespit eden ya da sürücüyü uyaran cihazları araçta bulundurmak yasaktır.</p>
''' + TUTAR_NOTU,
    faq=[
        ('Şehir içi hız sınırı kaç?',
         'Yönetmelikteki genel sınıra göre yerleşim yeri içinde otomobil, otobüs, kamyon ve motosiklet için hız sınırı 50 km/s’tir; levhayla farklı sınır belirlenebilir.'),
        ('Otoyolda hız sınırı kaç?',
         'Otomobil için otoyolda genel hız sınırı 120 km/s, bölünmüş yolda 110 km/s’tir.'),
        ('Hız cezasında ehliyet ne zaman alınır?',
         'Yerleşim yeri içinde 46 km/s, dışında 51 km/s ve üzeri aşımlarda ehliyet aşım miktarına göre her seferinde 30, 60 veya 90 gün geri alınır.'),
    ],
    sources=['ktk', 'kty', 'kabahat'],
))

PAGES.append(dict(
    key='kirmizi',
    title='', desc='Kırmızı ışıkta geçmenin cezası 2026’da ne kadar? Tekrarlanan ihlallerde artan cezalar, ehliyetin geri alınması ve iptali.',
    h1='Kırmızı Işıkta Geçmenin Cezası Nedir?', crumb='Kırmızı Işık Cezası',
    card='2026 cezaları, tekrar eden ihlaller ve ehliyetin geri alınması.',
    lead='Kırmızı ışık ihlali 2026 değişikliğiyle ağırlaştı: bir yıl içinde tekrarlanan ihlallerde ceza artıyor, ehliyet geri alınıyor ve altıncı ihlalde iptal ediliyor. Bilgiler Karayolları Trafik Kanunu’nun 47. maddesine dayanır.',
    summary=[
        'Trafik ışıklarına uymayan sürücüye 5.000 TL idari para cezası verilir.',
        'Bir yıl içinde tekrarlandıkça ceza artar: ikincide 10.000 TL, altıncıda 80.000 TL.',
        'Üçüncü ihlalde ehliyet 30 gün, dördüncüde 60 gün, beşincide 90 gün geri alınır; altıncıda iptal edilir.',
    ],
    body='''
<h2>Cezalar (son ihlalden geriye doğru bir yıl içinde)</h2>
<div class="guide-table"><table>
<thead><tr><th>İhlal</th><th>Para cezası</th><th>Ehliyet</th></tr></thead>
<tbody>
<tr><td>İlk</td><td>5.000 TL</td><td>-</td></tr>
<tr><td>İkinci</td><td>10.000 TL</td><td>-</td></tr>
<tr><td>Üçüncü</td><td>15.000 TL</td><td>30 gün geri alınır</td></tr>
<tr><td>Dördüncü</td><td>20.000 TL</td><td>60 gün geri alınır</td></tr>
<tr><td>Beşinci</td><td>30.000 TL</td><td>90 gün geri alınır</td></tr>
<tr><td>Altıncı</td><td>80.000 TL</td><td>İptal edilir</td></tr>
</tbody></table></div>
<p>Geri alınan ehliyet, süre sonunda psikoteknik değerlendirmede engel çıkmazsa iade edilir. Altıncı ihlalde iptal edilen ehliyeti yeniden almak için cezaların tamamı ödenmiş olmalı, iptalden itibaren en az bir yıl geçmeli ve kurs ile sınavlar yeniden tamamlanmalıdır.</p>

<h2>Diğer durumlar</h2>
<ul>
<li>Kırmızı ışık ihlaliyle kazaya sebep olan sürücünün ehliyeti 60 gün geri alınır.</li>
<li>Trafik polisinin uyarı ve işaretlerine uymayana 3.000 TL, levha ve yer işaretlerine uymayana 1.000 TL idari para cezası verilir.</li>
<li>Dur ihtarına uymayıp kaçan sürücüye 200.000 TL idari para cezası verilir; ehliyeti 60 gün geri alınır ve araç 60 gün trafikten men edilir.</li>
</ul>
''' + TUTAR_NOTU,
    faq=[
        ('Kırmızı ışık cezası 2026’da ne kadar?',
         'Kanunun 2026 metnine göre trafik ışığına uymayan sürücüye 5.000 TL idari para cezası verilir; bir yıl içinde tekrarlandıkça ceza 10.000 TL’den 80.000 TL’ye kadar artar.'),
        ('Kırmızı ışıkta kaç kez geçince ehliyet alınır?',
         'Bir yıl içinde üçüncü ihlalde ehliyet 30 gün, dördüncüde 60 gün, beşincide 90 gün geri alınır; altıncı ihlalde ehliyet iptal edilir.'),
        ('Kırmızı ışıkta geçip kazaya sebep olursam ne olur?',
         'Kırmızı ışık ihlaliyle kazaya sebep olan sürücünün ehliyeti 60 gün geri alınır.'),
    ],
    sources=['ktk', 'kabahat'],
))

PAGES.append(dict(
    key='telefon',
    title='', desc='Araç kullanırken telefon cezası 2026’da ne kadar? İlk ihlal 5.000 TL, tekrarında 10.000 ve 20.000 TL; üçüncüde ehliyet 30 gün geri alınır.',
    h1='Araç Kullanırken Telefon Cezası Nedir?', crumb='Telefon Cezası',
    card='Seyir hâlinde telefon kullanmanın 2026 cezaları.',
    lead='Seyir hâlinde cep veya araç telefonu ile benzer haberleşme cihazlarını kullanmak yasaktır. 2026 değişikliğiyle tekrarlanan ihlallerde ehliyet de geri alınıyor. Bilgiler Karayolları Trafik Kanunu’nun 73. maddesine dayanır.',
    summary=[
        'Seyir hâlinde telefon kullanan sürücüye 5.000 TL idari para cezası verilir.',
        'Bir yıl içinde ikinci ihlalde 10.000 TL, üç ve daha fazlasında her seferinde 20.000 TL uygulanır.',
        'Üç ve daha fazla ihlalde ehliyet her seferinde 30 gün geri alınır.',
    ],
    body='''
<h2>Kural</h2>
<p>Karayolunda seyir hâlindeki sürücülerin cep ve araç telefonu ile benzer haberleşme cihazlarını kullanması yasaktır. Aynı madde, aracın kamunun rahat ve huzurunu bozacak ya da kişilere zarar verecek şekilde saygısızca sürülmesini ve araçtan bir şey atılmasını da yasaklar (m.73).</p>

<h2>Cezalar (son ihlalden geriye doğru bir yıl içinde)</h2>
<div class="guide-table"><table>
<thead><tr><th>İhlal</th><th>Para cezası</th><th>Ehliyet</th></tr></thead>
<tbody>
<tr><td>İlk</td><td>5.000 TL</td><td>-</td></tr>
<tr><td>İkinci</td><td>10.000 TL</td><td>-</td></tr>
<tr><td>Üç ve daha fazla</td><td>Her seferinde 20.000 TL</td><td>Her seferinde 30 gün geri alınır</td></tr>
</tbody></table></div>
<p>Maddenin diğer hükümlerine uymayanlara 1.000 TL idari para cezası uygulanır. Geri alınan ehliyetin iadesi için idari para cezalarının tamamının ödenmiş olması gerekir.</p>

<h2>Güvenli kullanım</h2>
<p>Sürüş sırasında dikkati dağıtan her şey kaza riskini artırır. Telefonla ilgili işinizi aracı güvenli bir yerde durdurduktan sonra yapın. Aday sürücüler için ek kurallar ''' + a('aday', 'aday sürücü belgesi') + ''' yazımızda.</p>
''' + TUTAR_NOTU,
    faq=[
        ('Araç kullanırken telefonla konuşmanın cezası ne kadar?',
         'Kanunun 2026 metnine göre ilk ihlalde 5.000 TL, bir yıl içinde ikincisinde 10.000 TL, üç ve daha fazlasında her seferinde 20.000 TL idari para cezası uygulanır.'),
        ('Telefon cezasında ehliyet alınır mı?',
         'Evet. Bir yıl içinde üç ve daha fazla ihlalde ehliyet her seferinde 30 gün geri alınır.'),
        ('Geri alınan ehliyet ne zaman iade edilir?',
         'Geri alma süresi dolduğunda ve kanun kapsamındaki idari para cezalarının tamamı ödenmişse iade edilir.'),
    ],
    sources=['ktk', 'kabahat'],
))

PAGES.append(dict(
    key='ehliyetsiz',
    title='', desc='Ehliyetsiz araç kullanmanın cezası 2026’da 40.000 TL; ehliyeti geri alınmış veya iptal edilmişken araç kullanana 200.000 TL.',
    h1='Ehliyetsiz Araç Kullanmanın Cezası Nedir?', crumb='Ehliyetsiz Araç',
    card='Ehliyetsiz, geri alınmış ya da iptal edilmiş ehliyetle araç kullanmak.',
    lead='Motorlu aracı ehliyeti olmayan birinin kullanması da, kullanmasına izin verilmesi de yasaktır. 2026 değişikliğiyle bu cezalar önemli ölçüde arttı. Bilgiler Karayolları Trafik Kanunu’nun 36. maddesine dayanır.',
    summary=[
        'Ehliyeti olmadan motorlu araç kullanana 40.000 TL idari para cezası verilir.',
        'Ehliyeti geri alınmışken ya da iptal edilmişken araç kullanana 200.000 TL idari para cezası verilir.',
        'Aracının ehliyetsiz kişilerce kullanılmasına izin veren işletene de 40.000 TL ceza verilir.',
    ],
    body='''
<h2>Kural</h2>
<p>Motorlu araçlar; yönetmelikte sınıfları belirtilen ehliyete sahip sürücüler ile çok taraflı anlaşmalara göre ehliyeti olan ya da geçerli uluslararası sürücü belgesi bulunan kişilerce sürülebilir. Ehliyeti olmayanların araç kullanması ve kullanmasına izin verilmesi yasaktır (m.36).</p>

<h2>Cezalar (2026)</h2>
<ul>
<li>Ehliyeti olmadan motorlu araç kullanana 40.000 TL.</li>
<li>Mahkeme, savcılık ya da yetkililerce ehliyeti geçici veya tedbiren geri alınmışken araç kullanana 200.000 TL.</li>
<li>Ehliyeti iptal edilmişken araç kullanana 200.000 TL.</li>
<li>Bu kişilerin aracını kullanmasına izin veren işletene, tescil plakası üzerinden 40.000 TL.</li>
</ul>
<p>Ehliyet sahibinin, ehliyetinin sınıfı dışındaki bir aracı kullanması da yasaktır; bu durumda sürücüye ve araç sahibine ayrıca idari para cezası verilir (m.39).</p>

<h2>Sertifika ve K belgesi ehliyet değildir</h2>
<p>Sınavları geçince alınan sertifika ile kursta verilen K sınıfı sürücü aday belgesi, karayolunda tek başına araç kullanma yetkisi vermez. Ayrıntılar ''' + a('sertifika', 'sürücü sertifikası') + ''' ve ''' + a('kbelgesi', 'K sınıfı sürücü aday belgesi') + ''' yazılarımızda.</p>
''' + TUTAR_NOTU,
    faq=[
        ('Ehliyetsiz araç kullanmanın cezası ne kadar?',
         'Kanunun 2026 metnine göre ehliyeti olmadan motorlu araç kullanana 40.000 TL idari para cezası verilir.'),
        ('Ehliyeti geri alınmışken araç kullanılırsa ne olur?',
         'Ehliyeti geçici olarak geri alınmışken ya da iptal edilmişken araç kullanana 200.000 TL idari para cezası verilir.'),
        ('Ehliyetsiz birine aracımı verirsem ceza alır mıyım?',
         'Evet. Aracın ehliyetsiz kişilerce kullanılmasına izin veren işletene tescil plakası üzerinden 40.000 TL idari para cezası verilir.'),
    ],
    sources=['ktk', 'kabahat'],
))

PAGES.append(dict(
    key='kaza',
    title='', desc='Trafik kazasında ne yapılmalı? Durmak, güvenlik önlemi, ilk yardım, bilgi paylaşımı, maddi hasarlı kazada tutanak ve olay yerinden ayrılmanın cezası.',
    h1='Trafik Kazasında Ne Yapılmalı?', crumb='Trafik Kazası',
    card='Kaza anında yükümlülükler, tutanak ve olay yerinden ayrılma.',
    lead='Trafik kazasına karışan sürücünün kanundan doğan yükümlülükleri vardır; bunlara uymamak ayrıca ceza gerektirir. Bilgiler Karayolları Trafik Kanunu’nun 81 ve 82. maddelerine dayanır.',
    summary=[
        'Kazaya karışan sürücü hemen durmalı, güvenlik önlemi almalı ve kaza yerindeki durumu değiştirmemelidir.',
        'Yalnız maddi hasarlı kazada taraflar yetkili çağırmadan durumu aralarında yazılı olarak tespit edip ayrılabilir.',
        'Ölümlü veya yaralanmalı kazada izin almadan olay yerinden ayrılan sürücüye 1-3 yıl hapis cezası verilir.',
    ],
    body='''
<h2>Kazaya karışan sürücünün yükümlülükleri</h2>
<ol>
<li>Trafik için ek tehlike yaratmadan hemen durmak ve kaza yerinde güvenlik önlemlerini almak.</li>
<li>Ölen, yaralanan veya maddi hasar varsa, trafiği ve can güvenliğini etkilemiyorsa kanıt ve izler dahil kaza yerindeki durumu değiştirmemek.</li>
<li>İstenirse kimliğini, adresini, ehliyet ve ruhsat bilgilerini, sigorta poliçesinin tarih ve numarasını bildirmek.</li>
<li>Kazayı yetkililere bildirmek, gelene kadar ya da izinleri olmadan kaza yerinden ayrılmamak.</li>
<li>Sahibi yokken bir araca veya eşyaya zarar verdiyse sahibini bulmak; bulamazsa zarar verdiği şeyin üzerine yazılı bilgi bırakmak ve en kısa zamanda zabıtaya haber vermek.</li>
</ol>
<p>Kaza yerinden geçen ya da kazaya karışan sürücüler ilk yardım önlemlerini almak, en yakın zabıtaya veya sağlık kuruluşuna haber vermek ve yetkililer isterse yaralıları sağlık kuruluşuna götürmekle yükümlüdür (m.82). İlk yardım dersi bu yüzden sürücü kursunun zorunlu derslerindendir.</p>

<h2>Maddi hasarlı kazada tutanak</h2>
<p>Yalnız maddi hasar olan kazalarda, kazaya karışanların tümü yetkili çağırmaya gerek görmezse durumu aralarında yazılı olarak tespit ederek kaza yerinden ayrılabilir (m.81).</p>

<h2>Olay yerinden ayrılmanın cezası</h2>
<p>Anlaşma hâli dışında zabıtanın iznini almadan, zaruret dışında olay yerinden ayrılan ya da kaza yerindeki durumu değiştiren sürücüye 46.000 TL idari para cezası verilir. Ölümlü veya yaralanmalı kazada izin almadan olay yerinden ayrılan sürücüye bir yıldan üç yıla kadar hapis cezası verilir.</p>
''' + TUTAR_NOTU,
    faq=[
        ('Trafik kazasında ilk ne yapılır?',
         'Trafik için ek tehlike yaratmadan hemen durulur, kaza yerinde güvenlik önlemleri alınır, yaralı varsa ilk yardım önlemleri alınıp en yakın zabıtaya veya sağlık kuruluşuna haber verilir.'),
        ('Maddi hasarlı kazada polis çağırmak zorunlu mu?',
         'Yalnız maddi hasar varsa ve kazaya karışanların tümü gerek görmezse, durumu aralarında yazılı olarak tespit ederek kaza yerinden ayrılabilirler.'),
        ('Kaza yerinden ayrılmanın cezası nedir?',
         'Anlaşma dışında izin almadan ayrılana 46.000 TL idari para cezası verilir; ölümlü veya yaralanmalı kazada ayrılana 1-3 yıl hapis cezası verilir.'),
    ],
    sources=['ktk', 'kabahat'],
))

PAGES.append(dict(
    key='itiraz',
    title='', desc='Trafik cezasına nasıl itiraz edilir? 15 gün içinde sulh ceza hâkimliği, bir ay içinde ödemede yüzde 25 indirim, gecikme faizi ve taksit.',
    h1='Trafik Cezasına Nasıl İtiraz Edilir?', crumb='Trafik Cezası İtirazı',
    card='İtiraz süresi, yüzde 25 indirim, ödeme ve gecikme faizi.',
    lead='Trafik idari para cezasına itiraz etmek de, cezayı indirimli ödemek de belirli sürelere bağlıdır. Bilgiler Kabahatler Kanunu’nun 17 ve 27. maddelerine ve Karayolları Trafik Kanunu’nun 115 ve 116. maddelerine dayanır.',
    summary=[
        'İtiraz, cezanın tebliğinden itibaren en geç 15 gün içinde sulh ceza hâkimliğine dilekçeyle yapılır.',
        'Ceza, tebliğden itibaren bir ay içinde ödenirse yüzde 25 indirim yapılır; ödemek itiraz hakkını ortadan kaldırmaz.',
        'Bir ay içinde ödenmeyen cezaya her ay yüzde 5 gecikme faizi eklenir; toplam, cezanın iki katını geçemez.',
    ],
    body='''
<h2>İtiraz</h2>
<ul>
<li>İdari para cezasına karşı, kararın tebliğ veya tefhim tarihinden itibaren en geç 15 gün içinde sulh ceza hâkimliğine başvurulabilir. Süresinde başvurulmazsa karar kesinleşir.</li>
<li>Başvuru, kişinin kendisi, kanuni temsilcisi veya avukatı tarafından iki nüsha dilekçeyle yapılır. Dilekçede karara ilişkin bilgiler ve deliller açıkça gösterilir.</li>
<li>Mücbir sebeple süre kaçırıldıysa, sebebin ortadan kalktığı tarihten itibaren en geç 7 gün içinde başvurulabilir (Kabahatler Kanunu m.27).</li>
</ul>

<h2>Ödeme ve indirim</h2>
<ul>
<li>Trafik cezası, tutanağın tebliğinden itibaren bir ay içinde ödenmelidir (KTK m.115).</li>
<li>Ödeme süresi içinde ödenen cezadan yüzde 25 indirim yapılır; ödeme yapmak itiraz hakkını etkilemez (Kabahatler Kanunu m.17/6).</li>
<li>Bir ay içinde ödenmeyen cezaya her ay yüzde 5 faiz uygulanır; bulunan tutar cezanın iki katını geçemez.</li>
<li>Cezalar vergi dairelerine, muhasebe birimlerine, yetkili bankalara ve PTT’ye ödenebilir.</li>
<li>Kişinin ekonomik durumu müsait değilse, ilk taksit peşin ödenmek koşuluyla bir yıl içinde dört eşit taksitte ödenmesine karar verilebilir (Kabahatler Kanunu m.17/3).</li>
</ul>

<h2>Plakaya yazılan cezalar</h2>
<p>Sürücüsü tespit edilemeyen araçlara plakaya göre tutanak düzenlenir ve tebligat trafik kaydında araç sahibi görünen kişiye posta yoluyla yapılır (KTK m.116).</p>
''' + TUTAR_NOTU,
    faq=[
        ('Trafik cezasına itiraz süresi kaç gün?',
         'Kabahatler Kanunu’na göre cezanın tebliğinden itibaren en geç 15 gün içinde sulh ceza hâkimliğine başvurulabilir.'),
        ('Trafik cezasında yüzde 25 indirim var mı?',
         'Evet. Ceza tebliğden itibaren bir aylık ödeme süresi içinde ödenirse yüzde 25 indirim yapılır; ödeme, itiraz hakkını etkilemez.'),
        ('Trafik cezası geç ödenirse ne olur?',
         'Bir ay içinde ödenmeyen cezaya her ay yüzde 5 faiz uygulanır; toplam tutar cezanın iki katını geçemez.'),
    ],
    sources=['kabahat', 'ktk'],
))

# Ek SSS: her yazı en az 5 soru (Ahmet 29.09: "en az 4-5 tane olsun").
# Cevaplar yalnız yazının gövdesinde kaynağıyla verilen bilgilerden türetilir.
EXTRA_FAQ = {
'nasil': [('Ehliyet almak için hangi sınavlar geçilir?', 'Önce teorik dersleri ölçen 50 soruluk e-Sınav, ardından akan trafikte yapılan direksiyon sınavı geçilir.')],
'siniflar': [('Ehliyet kaç yıl geçerlidir?', 'M, A1, A2, A, B1, B, BE, F ve G sınıfı ehliyetler 10 yıl; C1, C1E, C, CE, D1, D1E, D ve DE sınıfı ehliyetler 5 yıl geçerlidir.')],
'belgeler': [('Ehliyet başvurusunda nüfus müdürlüğü neler ister?', 'Kimlik belgesi, sürücü sertifikası, öğrenim belgesi, sürücü sağlık raporu, harç ve vakıf payı, biyometrik fotoğraf, kan grubu belgesi veya beyanı ile adli sicil kaydı istenir.')],
'masraf': [('Uslu Sürücü Kursu’nun ücreti ne kadar?', 'Kurs ücreti seçilen eğitime göre değişir ve sabit liste yayımlanmaz; güncel ücret için 0532 068 56 47 numarasından ya da iletişim sayfasından teklif alınır.')],
'otomatik': [('e-Sınav’dan sonra vites türünü değiştirebilir miyim?', 'Evet. e-Sınav’ı geçen kursiyer, direksiyon ders planlaması yapılmadan önce yazılı başvuruyla aynı sınıfın manuel ya da otomatik seçeneğine geçebilir.')],
'kalirsam': [('Sınav hakkım biterse ne olur?', 'Haklarını başarısız tamamlayan aday kursa yeniden kayıt yaptırabilir; teorik sınavı geçmişse üç yıl içinde kayıtta teorik eğitim ve sınavdan muaf olur.')],
'motor': [('B ehliyetle A1 için kaç saat ders alınır?', 'A1 sınıfı için öngörülen direksiyon eğitim saatinin yarısı kadar ders alınır; A1 için akan trafikte en az 12 saat öngörüldüğünden bu yolda eğitim yarısı kadardır.')],
'korku': [('Ehliyeti olanlar için teorik ders var mı?', 'Yönetmeliğe göre bu kursiyerlere trafik adabı dersi ile ihtiyaç duydukları kadar direksiyon dersi verilir.'),
          ('Uslu Sürücü Kursu’nda ehliyeti olanlara ders veriliyor mu?', 'Evet. Trafiğe yeniden çıkış, park ve araç kontrolünü pekiştirmek isteyenler için özel direksiyon dersi veriyoruz; ders planı mevcut deneyime göre birlikte oluşturulur.')],
'sincan': [('Sincan’da ehliyet başvurusu nereye yapılır?', 'Randevuyla, sertifikanın alındığı yerden bağımsız olarak yetkili nüfus müdürlüklerinden birine yapılır; belge PTT ile ücretsiz olarak adrese gönderilir.')],
'ankara': [('Ankara’da sürücü olur raporu nereden alınır?', 'Ankara’daki aile sağlığı merkezlerinden, Sağlık Bakanlığına ve üniversitelere bağlı hastanelerden ya da muayenehane dışındaki özel sağlık kuruluşlarından alınabilir.')],
'yenileme': [('Ehliyet yenilemek için nereye başvurulur?', 'Randevu alınarak yetkili nüfus müdürlüklerinden birine başvurulur; randevu randevu.nvi.gov.tr, e-Devlet, NVİ Mobil veya Alo 199 üzerinden alınır.'),
             ('Eski tip ehliyetler hâlâ geçerli mi?', 'NVİ’ye göre eski tip ehliyetler Kasım 2025 itibarıyla geçerliliğini kaybetmiştir; bu belgelerle araç kullananların ehliyeti geri alınır.')],
'kayip': [('Kayıp ehliyet için nereye başvurulur?', 'Randevu alınarak yetkili nüfus müdürlüklerinden birine başvurulur; başvuru bizzat yapılır, vekaletle işlem yapılmaz.'),
          ('Ad soyadım değişti, ehliyeti değiştirmem gerekir mi?', 'Evet. NVİ’ye göre ad ve soyadı gibi kişisel bilgiler değiştiğinde değerli kâğıt bedeli ve vakıf payı ödenerek ehliyet yenilenmelidir.')],
'yurtdisi': [('Yabancılar yurt dışı ehliyetiyle Türkiye’de ne kadar araç kullanabilir?', 'NVİ’ye göre yabancılar yurt dışından alınan ehliyetle Türkiye’de 6 ay araç kullanabilir.'),
             ('Yurt dışı ehliyetim varsa başka sınıf için kursa yazılabilir miyim?', 'Önce yurt dışı ehliyeti Türk ehliyetiyle değiştirmeniz gerekir; farklı bir sınıf için kursa ondan sonra kayıt olunur.')],
'aday': [('Aday sürücü alkol sınırı kaç promil?', 'Aday sürücülerde araç cinsine bakılmaksızın 0.20 promilin üzerinde alkollü araç kullanmak aday belgenin iptaline yol açar.'),
         ('Aday belgesi iptal edilen yeniden nasıl ehliyet alır?', 'Sürücü kursuna devam edip sınavları yeniden geçmesi gerekir; kursa başlamak için psikoteknik değerlendirme ve psikiyatri belgesi, cezaların ödenmiş olması ve bekleme sürelerinin geçmiş olması aranır.')],
'ceza': [('Ceza puanıyla geri alınan ehliyet için eğitim var mı?', 'Evet. 100 ceza puanı nedeniyle ehliyeti 2 ay geri alınan sürücü eğitime alınır ve bu sürede sürücü kursunda teorik derslerin tamamına devam eder.'),
         ('Ölümlü kazada ehliyet ne kadar geri alınır?', 'Ölümle sonuçlanan trafik kazasına asli kusurlu olarak sebep olan sürücünün ehliyeti 1 yıl süreyle geri alınır.')],
'rapor': [('Sürücü raporunda hangi muayeneler yapılır?', 'Yönetmelik göz, iç hastalıkları, kulak burun boğaz, ortopedi, ruh ve sinir hastalıkları muayenelerine ilişkin esasları belirler; gerekirse uzman hekime yönlendirme yapılır.'),
          ('Sürücü raporuna itiraz edilebilir mi?', 'Evet. Kişinin adına düzenlenen rapora itiraz hakkı vardır; itiraz usullerini Sağlık Bakanlığı belirler.')],
'motosiklet': [('Motor ehliyeti için kaç saat ders gerekir?', 'A1 ve A2 için akan trafikte en az 12 saat, A2 deneyimiyle A için 6 saat, 24 yaşını dolduranların A sınıfı için 12 saat direksiyon dersi alınır.'),
               ('Uslu Sürücü Kursu’nda motor ehliyeti var mı?', 'Evet. Ankara Sincan’daki kursumuzda A1 ve A2 motosiklet ehliyeti eğitimleri verilir.')],
'ekleme': [('Sınıf eklemede direksiyon sınavı var mı?', 'Evet. Tablodaki saat kadar ders alındıktan sonra kursun uygun görmesiyle direksiyon sınavına girilir; başarılı olana yeni sınıfın sertifikası verilir.'),
           ('A2 ehliyetime A eklemek için kaç saat ders gerekir?', 'Yönetmelikteki tabloya göre A2 sahibinin A eklemesi için akan trafikte 6 saat direksiyon dersi alınır.')],
'ozel': [('Özel tertibat komisyonunda kimler bulunur?', 'İlgili branş uzmanları, ortopedi ve travmatoloji, fiziksel tıp ve rehabilitasyon ve nöroloji uzmanları ile bir makine mühendisi bulunur.'),
         ('Uslu Sürücü Kursu’nda özel gereksinimli eğitim var mı?', 'Evet. Kursumuzda özel gereksinimli A-B sınıfı eğitimi verilir; eğitim ve araç uygunluğu adaya göre bireysel değerlendirilir.')],
'randevu': [('Randevuya geç kalırsam ne olur?', 'Randevu saatinden 30 dakika önce ile 60 dakika sonrası arasında sıra alınabilir; 60 dakikayı geçirenlerin başvurusu alınmaz.'),
            ('Ehliyet kargo ücreti var mı?', 'Hayır. Ehliyet başvuruda belirtilen adrese PTT güvenli taşıma hizmetiyle gönderilir ve gönderim ücretsizdir.')],
'kayitdonemi': [('Sürücü kursunda teorik dersler günde kaç saat?', 'Kurslarda günde en az 2, en çok 6 saat teorik ders yapılır.'),
                ('Bir araç için kaç kursiyer kaydedilir?', 'Bir dönemde bir direksiyon eğitim ve sınav aracı için en fazla 12 kursiyer kaydedilir.')],
'devamsizlik': [('Direksiyon telafi dersleri ücretli mi?', 'Evet. Yönetmeliğe göre direksiyon telafi programlarında kursiyerden devam ettiği derslerin ücreti alınır.'),
                ('Teorik derslerin toplam süresi kaç saat?', 'Bütün sınıflarda teorik dersler 34 saattir: trafik ve çevre 16, ilk yardım 8, araç tekniği 6, trafik adabı 4 saat.')],
'nakil': [('Nakil olursam sınav hakkım ne olur?', 'Direksiyon sınavının ilk dört hakkında başarısız olup nakil olan kursiyere, yeni kursta sınıfın ders saati kadar eğitimden sonra ikinci dört sınav hakkı kullandırılır.'),
          ('Nakil olunca hangi döneme kaydolunur?', 'Nakil olan kursiyer, kayıtlı olduğu dönemden sonraki döneme, naklini istediği kursun kontenjanına dahil edilerek kaydedilir.')],
'direksiyon': [('Gece direksiyon dersi zorunlu mu?', 'Evet. Çoğu sınıfta akan trafikte en az 2 saat gece sürüşü zorunludur; sağlık raporunda gece kısıtı olanlara gece dersi verilmez.'),
               ('Uslu Sürücü Kursu’nda direksiyon eğitimi nerede verilir?', 'Ankara Sincan’daki kursumuzun direksiyon dersleri OSB Törekent parkurunda yapılır, ardından akan trafikte devam edilir.')],
'kbelgesi': [('K belgesi ehliyet yerine geçer mi?', 'Hayır. K sınıfı sürücü aday belgesi ehliyet değildir; yalnız kurstaki eğitim ve sınav için kullanılır.'),
             ('K belgesi ne zaman verilir?', 'Akan trafikte direksiyon eğitimi başladığında kurs müdürlüğünce düzenlenir.')],
'sertifika': [('Sertifika e-Devlet’te ne zaman görünür?', 'Sınavları geçen adayın sertifikası elektronik olarak düzenlenir ve e-Devlet üzerinden erişilir; bilgileri ayrıca NVİ’ye iletilir.'),
              ('Sertifikayı ehliyete çevirmek için ne ödenir?', 'Nüfus müdürlüğünde sınıfın harcı, değerli kâğıt bedeli ve vakıf payı ödenir; 2026’da B sınıfı için toplam 8.869,60 TL’dir.')],
'esinavkural': [('e-Sınava saat takılabilir mi?', 'Hayır. Kılavuza göre her türlü saat sınav binasına alınmaz.'),
                ('e-Sınava kaç dakika önce gidilmeli?', 'Adaylar sınav saatinden en geç 30 dakika önce e-Sınav salonunda hazır bulunmalıdır.')],
'esinavitiraz': [('e-Sınav itirazı nereden yapılır?', 'İtiraz ücreti yatırıldıktan sonra MEB e-İtiraz Modülü (eitiraz.meb.gov.tr) üzerinden yapılır.'),
                 ('e-Sınav soruları yayımlanır mı?', 'Hayır. Kılavuza göre sınav soruları ve cevapları yayımlanmaz.')],
'geripark': [('Direksiyon sınavında geri parktan sonra ne yapılır?', 'Şerit içinde 25 metre geri gitme, geri giderken sağa dönüş, dar alanda en fazla üç hamlede geri dönüş, azami hıza ulaşma ve 30 km/s hızda ani fren yapılır.'),
             ('Geri parkta konilere değersem ne olur?', 'Yönetmelik aracın kaldırıma ve konilere değmeden park edilmesini ister; değerlendirmeyi sınav komisyonu formdaki ölçütlere göre yapar.')],
'motorsinav': [('Motor sınavında denge çizgisi ne kadar?', 'Denge çizgisi 20 metre uzunluğunda ve 20 cm genişliğindedir; B1 sınıfında bu aşama yoktur.'),
               ('Motor sınavı trafikte de yapılır mı?', 'Evet. Sınav alanında başarılı olan adayın sınavı güzergâhta, akan trafikte devam eder.')],
'mazeret': [('e-Sınava girmezsem ücret iade edilir mi?', 'Hayır. Randevu alıp sınava girmeyen aday ücret iadesi isteyemez ve bir sınav hakkını kullanmış sayılır.'),
            ('Hamilelik nedeniyle sınava giremezsem ne olur?', 'Doktor raporuyla 10 gün içinde kursa yazılı bildirim yapılırsa kayıt dondurulur ve kalan haklar rapor süresi bitince kullandırılır.')],
'yas16': [('16 yaşında otomobil ehliyeti alınır mı?', 'Hayır. B sınıfı otomobil ehliyeti için 18 yaşını bitirmiş olmak gerekir.'),
          ('A1 ehliyetle moped kullanılır mı?', 'Evet. Karayolları Trafik Yönetmeliği’ne göre A1 ehliyetiyle M sınıfı araçlar, yani mopedler de kullanılabilir.')],
'romork': [('BE ehliyeti harcı ne kadar?', '2026’da BE sınıfı harcı 11.271,20 TL’dir; değerli kâğıt bedeli ve vakıf payıyla toplam 13.386,20 TL ödenir.'),
           ('C ve D ehliyetle hafif römork takılır mı?', 'Evet. B, C, C1, D ve D1 sınıfı ehliyet sahipleri azami yüklü ağırlığı 750 kg’a kadar hafif römork takabilir.')],
'kamyon': [('C ehliyetle otomobil kullanılır mı?', 'Evet. C sınıfı ehliyetle M, B, B1, C1 ve F sınıfı araçlar da kullanılabilir.'),
           ('Kamyon ehliyeti harcı ne kadar?', '2026’da C1 ve C sınıfı harcı 11.271,20 TL’dir; değerli kâğıt bedeli ve vakıf payıyla toplam 13.386,20 TL ödenir.')],
'otobus': [('Minibüs ehliyeti hangi sınıf?', 'Minibüs için D1 sınıfı ehliyet gerekir; 21 yaş ve B ehliyeti şarttır. D sınıfı ise minibüs ve otobüsü kapsar.'),
           ('D ehliyetle otomobil kullanılır mı?', 'Evet. D sınıfı ehliyetle M, B, B1, D1 ve F sınıfı araçlar da kullanılabilir.')],
'traktor': [('Traktör ehliyeti için kaç saat ders gerekir?', 'F sınıfında akan trafikte en az 12 saat direksiyon dersi alınır; en az 2 saati gece sürüşüdür.'),
            ('Traktör otoyola girebilir mi?', 'Hayır. Yönetmelikteki hız tablosunda lastik tekerlekli traktörlerin otoyola giremeyeceği belirtilir.')],
'ismakinesi': [('İş makinesi ehliyeti kaç yıl geçerlidir?', 'G sınıfı ehliyet 10 yıl geçerlidir.'),
               ('G ehliyeti harcı ne kadar?', '2026’da G sınıfı harcı 11.271,20 TL’dir; değerli kâğıt bedeli ve vakıf payıyla toplam 13.386,20 TL ödenir.')],
'sabika': [('Yalan beyanda bulunursam ne olur?', 'Gerçeğe aykırı beyanda bulunduğu tespit edilen kursiyer sınava alınmaz; sınava girmişse sınavı geçersiz sayılır ve kaydı silinir.'),
           ('Nüfus müdürlüğü adli sicili kontrol eder mi?', 'Evet. Ehliyet başvurusunda adli sicil kaydı sistemden kontrol edilir.')],
'diploma': [('Diploma aslı gerekli mi?', 'Kurs, diploma veya öğrenim belgesinin aslını görerek onaylı örneğini alır.'),
            ('Nüfus müdürlüğü öğrenim belgesi ister mi?', 'Evet. Ehliyet başvurusunda öğrenim belgesi istenir ve sistemden kontrol edilir.')],
'yabanci': [('Yabancılar için kurs kaydında hangi belgeler istenir?', 'Pasaportun noter tasdikli Türkçe tercümesi veya geçici koruma kimlik belgesi, en az altı aylık ikamet izni ya da vize, öğrenim belgesinin tercümesi, sürücü olur raporu, biyometrik fotoğraf ve adli sicil belgesi istenir.'),
            ('Geçici koruma altındakiler e-Sınava nerede girer?', 'Geçici koruma kimlik belgesi olan adaylar e-Sınav’a yalnız belgede yazan ikamet ilinde girebilir.')],
'fotograf': [('Ehliyet fotoğrafı kaç aylık olmalı?', 'Fotoğraf son altı ay içinde çekilmiş olmalıdır.'),
             ('Kayıtta fotoğrafım yanlış girilirse düzeltilir mi?', 'Kayıt bilgileri kursiyere onaylatılır; fotoğrafı veya bilgileri hatalı girilen kursiyerde o eğitim döneminde düzeltme yapılmaz.')],
'psikoteknik': [('Hız ihlalinde psikoteknik ne zaman istenir?', 'Bir yıl içinde beşinci kez hız nedeniyle geri alınan ehliyet, psikoteknik değerlendirme ve psikiyatri muayenesinden sonra iade edilir.'),
                ('Kırmızı ışık ihlalinde psikoteknik istenir mi?', 'Evet. Bir yıl içinde üç, dört veya beş ihlalde geri alınan ehliyet süre sonunda psikoteknik değerlendirmede engel çıkmazsa iade edilir.')],
'alkol': [('Alkollü araç kullanan sürücü hapis cezası alır mı?', '1.00 promilin üzerinde alkollü olanlar hakkında ayrıca Türk Ceza Kanunu’nun 179/3 maddesi uygulanır; kazaya sebep olanlar hakkında da ceza kanunu hükümleri uygulanır.'),
          ('Alkol nedeniyle geri alınan ehliyet ne zaman iade edilir?', 'Geri alma süresi dolduğunda ve kanun kapsamındaki idari para cezalarının tamamı ödenmişse iade edilir.')],
'hiz': [('Şehir içinde 10 km/s hız aşmanın cezası ne kadar?', 'Kanunun 2026 metnine göre yerleşim yeri içinde 6-10 km/s aşan sürücüye 2.000 TL idari para cezası verilir.'),
        ('Radar dedektörü kullanmak yasak mı?', 'Evet. Hız ölçen cihazların yerini tespit eden veya sürücüyü uyaran cihazları araçta bulundurmak yasaktır.')],
'kirmizi': [('Kırmızı ışıkta 6 kez geçen ne zaman yeniden ehliyet alır?', 'Cezaların tamamı ödenmiş olmalı, iptalden itibaren en az bir yıl geçmeli ve psikoteknik değerlendirmeden sonra kurs ile sınavlar yeniden tamamlanmalıdır.'),
            ('Dur ihtarına uymamanın cezası nedir?', 'Dur ihtarına uymayıp kaçan sürücüye 200.000 TL idari para cezası verilir; ehliyeti 60 gün geri alınır ve araç 60 gün trafikten men edilir.')],
'telefon': [('Araçta telefonla konuşmak her durumda yasak mı?', 'Kanun, seyir hâlinde cep ve araç telefonu ile benzer haberleşme cihazlarının kullanılmasını yasaklar.'),
            ('Araçtan çöp atmanın cezası var mı?', 'Evet. Araçlardan bir şey atılması da aynı maddeyle yasaktır; bu hükme uymayanlara 1.000 TL idari para cezası uygulanır.')],
'ehliyetsiz': [('Ehliyet sınıfım dışında araç kullanırsam ne olur?', 'Ehliyetin sınıfı dışındaki aracı kullanmak yasaktır; sürücüye ve aracı kullandıran araç sahibine idari para cezası verilir.'),
               ('Sertifikayla araç kullanmak ehliyetsiz sayılır mı?', 'Sertifika, ehliyetle değiştirilmedikçe karayolunda araç kullanma yetkisi vermez.')],
'kaza': [('Kazada sigorta bilgisi vermek zorunlu mu?', 'Evet. İstenirse kimlik, adres, ehliyet ve ruhsat bilgileri ile sigorta poliçesinin tarih ve numarası bildirilir.'),
         ('Park hâlindeki araca çarparsam ne yapmalıyım?', 'Aracın sahibini bulmalı; bulamazsanız durumu tespit edip araç üzerine yazılı bilgi bırakmalı ve en kısa zamanda zabıtaya haber vermelisiniz.')],
'itiraz': [('Trafik cezasına itiraz nereye yapılır?', 'İtiraz, cezanın tebliğinden itibaren en geç 15 gün içinde sulh ceza hâkimliğine dilekçeyle yapılır.'),
           ('Trafik cezası taksitle ödenir mi?', 'Kişinin ekonomik durumu müsait değilse, ilk taksit peşin ödenmek koşuluyla bir yıl içinde dört eşit taksitte ödenmesine karar verilebilir.')],
}
for _p in PAGES:
    _p['faq'] = _p['faq'] + EXTRA_FAQ.get(_p['key'], [])

# Gruplar: merkez sayfadaki bölümler ve "diğer yazılar" bağlantıları buna göre.
GROUPS = [
    ('Ehliyet almak', ['nasil', 'ankara', 'sincan', 'belgeler', 'rapor', 'sabika', 'diploma', 'yabanci', 'fotograf', 'masraf', 'randevu']),
    ('Kurs ve dersler', ['kayitdonemi', 'devamsizlik', 'nakil', 'direksiyon', 'kbelgesi', 'sertifika', 'otomatik', 'korku']),
    ('Sınavlar', ['sinav', 'esinavkural', 'esinavitiraz', 'geripark', 'motorsinav', 'kalirsam', 'mazeret']),
    ('Ehliyet sınıfları', ['siniflar', 'yas16', 'motosiklet', 'motor', 'romork', 'kamyon', 'otobus', 'traktor', 'ismakinesi', 'ekleme', 'ozel']),
    ('Ehliyet aldıktan sonra', ['yenileme', 'kayip', 'aday', 'yurtdisi', 'psikoteknik']),
    ('Trafik kuralları ve cezalar', ['ceza', 'alkol', 'hiz', 'kirmizi', 'telefon', 'ehliyetsiz', 'kaza', 'itiraz']),
]
# Footer'daki "Rehber" bölümünde görünen yazılar (tümü için merkez sayfa bağlantısı ayrıca var).
FOOTER = ['ankara', 'nasil', 'belgeler', 'sinav', 'masraf', 'siniflar', 'rapor', 'yenileme', 'motosiklet', 'kalirsam', 'sincan']


HUB = dict(
    title='Ehliyet Rehberi: Belgeler, Sınavlar ve Masraflar | Uslu',
    desc='Ankara ve Sincan için resmî kaynaklı ehliyet rehberi: 50 yazıda belgeler, sınavlar, 2026 masrafları, ehliyet sınıfları ve trafik cezaları.',
    h1='Ehliyet Rehberi',
    lead='Ehliyet sürecinde en çok sorulan soruları resmî kaynaklara dayanarak yanıtladık: MEB Özel Motorlu Taşıt Sürücüleri Kursu Yönetmeliği, MEB 2026 e-Sınav Kılavuzu, Karayolları Trafik Yönetmeliği, Sürücü Sağlık Yönetmeliği ve Nüfus ve Vatandaşlık İşleri Genel Müdürlüğü. Her yazının sonunda kaynaklarını bulabilirsiniz.',
    quick=[
        ('Otomobil ehliyeti kaç yaşında alınır?', '18 yaşını bitirmiş olmak gerekir.', 'siniflar'),
        ('e-Sınav kaç soru, kaç puanla geçilir?', '50 soru, 45 dakika; 70 ve üzeri puan başarılıdır.', 'sinav'),
        ('B sınıfında kaç saat direksiyon dersi var?', 'Akan trafikte en az 14 saat, bunun en az 2 saati gece.', 'siniflar'),
        ('2026’da B sınıfı ehliyet harcı ne kadar?', 'Harç 6.754,60 TL; kart bedeli ve vakıf payıyla toplam 8.869,60 TL.', 'masraf'),
        ('e-Sınavda kalırsam kaç hakkım var?', 'Yalnız sınav ücretiyle üç kez daha, toplam dört hak.', 'kalirsam'),
        ('Otomatik ehliyetle manuel araç kullanılır mı?', 'Hayır; manuele geçmek için ek ders ve sınav gerekir.', 'otomatik'),
    ],
    sources=['mtsk', 'esinav', 'kty', 'saglik', 'nvi_sss', 'nvi_ucret'],
)

# Ana sayfadaki "Rehber" bölümü: en çok aranan konular (görselli kartlar).
# Ana sayfa: ilki büyük görselli öne çıkan yazı, kalan altısı numaralı soru listesi.
HOME_FEATURED = ['nasil', 'masraf', 'sinav', 'ankara', 'yenileme', 'alkol', 'hiz']
