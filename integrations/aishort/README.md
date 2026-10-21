# AiShort yaklaşımına dayalı uzmanlaşmış istem kütüphanesi

## Bu modül nedir?

ChatGPT Web'den erişilebilen, akademik metin üretimi, kaynak doğrulama, araştırma tasarımı, akademik proje hazırlığı ve yazılım geliştirme için **tamamı bu projeye özgü hazırlanmış** 14 Türkçe istem. AiShort'un orijinal uygulamasını veya tüm hazır istemlerini içermez.

## Kullanım

1. `prompts.json` dosyasından ihtiyaca uygun `id` seçin.
2. `required_inputs` alanlarını kullanıcı dosyaları veya doğrulanmış bilgiyle doldurun.
3. `prompt` alanını görev bağlamıyla uyarlayın. Protokol kullanıcı talimatının yerine geçmez.
4. `quality_checks` maddeleriyle metni, veriyi ve kaynakları denetleyin.
5. İşlemde gerçekten kullanılan araçları ve kalan sınırlılıkları raporlayın.

**Not:** Bu modül kaynak kodunu, istem kütüphanesini veya platformun kendisini ChatGPT'ye kurmaz. Ekstra API anahtarı da gerektirmez; istem belgelerinin okunabilmesi yeterlidir. Haricî literatür veri tabanı, bilimsel yayın tam metni veya yazılım testleri gerektiğinde uygun erişim koşulları ayrıca gerekir.

## Doğrudan kullanım komutları

- `AW-01`: akademik makale planlama
- `LR-02`: kaynak/DOI doğrulama
- `RP-02`: araştırma projesi tasarımı
- `RP-03`: görsel iletişim/göstergebilim araştırması
- `SW-01`: yazılım gereksinimleri

Bkz. [tam dizin](PROMPT_INDEX.md) ve [kalite geçidi](QUALITY_GATE.md).
