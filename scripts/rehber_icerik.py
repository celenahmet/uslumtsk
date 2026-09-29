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
            'https://www.mevzuat.gov.tr/MevzuatMetin/1.5.2918.pdf'),
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
}

def a(key, text):
    return '<a href="%s">%s</a>' % (R[key], text)

PAGES = []

# 1 ─────────────────────────────────────────────────────────────
PAGES.append(dict(
    key='nasil',
    title='Ehliyet Nasıl Alınır? 2026 Adım Adım Süreç | Uslu Sürücü Kursu',
    desc='Ankara’da ehliyet nasıl alınır? Sürücü olur raporundan nüfus müdürlüğü başvurusuna kadar adımlar: kurs kaydı, teorik dersler, e-Sınav, direksiyon eğitimi ve sınavı.',
    h1='Ehliyet Nasıl Alınır?',
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
        ('Otobüs ehliyeti kaç yaşında alınır?',
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
<li>Son altı ayda çekilmiş biyometrik fotoğraf. Yönetmelik iki adet sayar.</li>
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
<li>Sürücü olur raporu ve son altı ayda çekilmiş iki biyometrik fotoğraf.</li>
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
        ('Sürücü olur raporu nereden alınır?',
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
    h1='Ehliyet Sınavı: e-Sınav ve Direksiyon',
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
    h1='Otomatik Vites Ehliyet',
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
    h1='Ehliyet Sınavında Kalırsam Ne Olur?',
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
    h1='B Ehliyetle Motosiklet Kullanmak',
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
    h1='Ehliyetim Var Ama Araba Kullanamıyorum',
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
    desc='Sincan’da ehliyet almak isteyenler için adım adım yol: kursa kayıt, teorik dersler, Ankara’daki e-Sınav, OSB Törekent parkurunda direksiyon dersi ve başvuru.',
    h1='Sincan’da Ehliyet Almak',
    crumb='Sincan’da Ehliyet',
    card='Sincan’da kayıttan ehliyet başvurusuna kadar hangi adım nerede yapılır.',
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
    h1='Ehliyet Yenileme',
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
    h1='Kayıp veya Çalıntı Ehliyet',
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
    h1='Yurt Dışı Ehliyeti ve Değişimi',
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
    h1='Aday Sürücü Belgesi',
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
    h1='Ehliyet Ceza Puanı',
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
    h1='Sürücü Olur Raporu',
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
    h1='Motosiklet Ehliyeti: A1, A2, A',
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
    h1='Ehliyete Sınıf Ekleme',
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
    desc='Özel tertibatlı araç gereken sürücü adaylarında sağlık raporu komisyonu, özel tertibat kodu, eğitim ve sınav aracı. Sürücü Sağlık Yönetmeliği ve MEB yönetmeliğine göre.',
    h1='Özel Gereksinimli Sürücü Adayları',
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
    h1='Ehliyet Randevusu ve Başvurusu',
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
    h1='Ankara’da Ehliyet Almak',
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
<p>Kursumuz Ankara’nın Sincan ilçesinde, Atatürk Mah. Atatürk Cd. No:2/17 (2. Noterin üst katı) adresindedir. <a href="/egitim/manuel-b/">B sınıfı manuel</a> ve <a href="/egitim/otomatik-b/">otomatik</a> ehliyet, <a href="/egitim/motor-a1/">A1</a> ve <a href="/egitim/motor-a2/">A2 motosiklet</a> eğitimleri ile <a href="/egitim/ozel/">özel direksiyon dersi</a> veriyoruz. Direksiyon derslerimiz OSB Törekent parkurunda yapılır. Sincan’daki adımlar için ''' + a('sincan', 'Sincan’da ehliyet almak') + ''' yazımıza bakın.</p>
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

# Gruplar: merkez sayfadaki bölümler ve "diğer yazılar" bağlantıları buna göre.
GROUPS = [
    ('Ehliyet almak', ['nasil', 'ankara', 'siniflar', 'belgeler', 'rapor', 'masraf', 'randevu', 'sincan']),
    ('Eğitim ve sınavlar', ['sinav', 'kalirsam', 'otomatik', 'motosiklet', 'motor', 'ekleme', 'ozel', 'korku']),
    ('Ehliyet aldıktan sonra', ['yenileme', 'kayip', 'aday', 'ceza', 'yurtdisi']),
]
# Footer'daki "Rehber" bölümünde görünen yazılar (tümü için merkez sayfa bağlantısı ayrıca var).
FOOTER = ['ankara', 'nasil', 'belgeler', 'sinav', 'masraf', 'siniflar', 'rapor', 'yenileme', 'motosiklet', 'kalirsam', 'sincan']


HUB = dict(
    title='Ehliyet Rehberi: Belgeler, Sınavlar ve Masraflar | Uslu',
    desc='Ehliyet nasıl alınır, hangi belgeler gerekir, e-Sınav ve direksiyon sınavı nasıl yapılır, 2026 harçları ne kadar? Sincan’daki Uslu Sürücü Kursu’ndan resmî kaynaklı rehber.',
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
