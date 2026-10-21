# Akademik yazım, literatür ve araştırma tasarımı modülü

**Kaynak projesi:** https://github.com/ahmetbersoz/chatgpt-prompts-for-academic-writing  
**İncelenen yükleme:** `chatgpt-prompts-for-academic-writing-main.zip` (README.md + cover.jpg)  
**Modül üretim tarihi:** 21 Ekim 2026

## Neler var?

23 özgün Türkçe istem; akademik makale, kaynak doğrulama, sistematik tarama, araştırma yöntemi, görsel iletişim/göstergebilim, akademik çeviri, hakem değerlendirmesi ve proje önerisi.

1. [PROMPT_INDEX.md](PROMPT_INDEX.md) üzerinden bir ID belirleyin.
2. [prompts.json](prompts.json) içindeki `required_inputs` alanlarını sağlayın.
3. `prompt_tr` alanını kullanırken kullanıcı tarafından kararlaştırılmış başlığı, amaçları ve yöntemi koruyun.
4. [QUALITY_GATE.md](QUALITY_GATE.md) denetimlerini uygulayın.
5. Gerçekten doğrulanan kaynakları, veri olmayan kısımları ve yöntemin sınırlarını raporlayın.

## Kullanım örnekleri

- `AWL-03`: ekli makalelerden kanıt matrisi üret.
- `AWR-02`: sorularımla yöntem ve veri toplama araçlarımın uyumunu kontrol et.
- `AWR-04`: grafik tasarım çalışmam için görsel iletişim/göstergebilim kodlama şeması öner.
- `AWW-09`: kaynakça ile metin içi atıfları APA 7 bakımından karşılaştır.
- `AWQ-01`: Q1 düzeyinde eleştirel değerlendirme yap; gerçek editoryal karar verme iddiasında bulunma.
- `AWP-01`: resmî proje çağrısı üzerinden amaç, yöntem, iş paketi ve riskleri eşleştir.

## Çalışma modelleri

| Biçim | Yapabilecekleri | Koşullar |
|---|---|---|
| ChatGPT Web, metin temelli | İstem/protokol okuma, kullanıcı belgelerini analiz etme, yapılandırılmış yazım | GitHub erişimi ve gerekli girdiler |
| ChatGPT Web, güncel literatür | İlgili kaynakları keşfetme, mümkün olan bibliyografik doğrulama | Yetkili web/veri tabanı erişimi; iddia bazlı kontrol |
| Yerel/uzak ajan | `prompts.json` üzerinden programatik istem seçimi | Uygun çalışma ortamı ve izinler |

**Yapamayacakları:** DOI uydurmak, Scopus/WoS indeks üyeliğini kaynak olmadan garanti etmek, veri olmadan bulgu üretmek veya GitHub yüklemesiyle yeni bir modeli otomatik kurmak.

## Modül sınırları
Bu içerik kaynak depodaki hazır istemlerin tam kopyası değildir. Kaynak depoda incelenen anlık görüntü açık bir lisans dosyası sunmadığından bu pakette orijinal metin ya da görsel bulunmaz. Verilen bağlantı bir atıf/keşif yoludur.
