# Kaynak arşiv envanteri

Kullanıcının yüklediği 6 ZIP arşivi teknik olarak incelendi. Sürüm, lisans ve SHA-256 bilgileri [source-manifest.json](source-manifest.json) dosyasına kaydedildi.

- SVG.js / Paper.js: gerçek vektör üretimi için gerekli kütüphaneler.
- PptxGenJS: düzenlenebilir PowerPoint sunumu üretimi.
- MJML: responsive HTML newsletter derlemesi.
- Slidev: Markdown tabanlı web sunumları.
- OpenAI `plugins-main`: Codex plugin manifest/skill mimarisi referansı; karma lisanslı upstream bileşenler bu pakete kopyalanmadı.

**Neden upstream ZIP'ler burada yok?** Birleştirilmiş monorepo halinde tekrar dağıtmak, çok sayıda gereksiz bağımlılık, binlerce test dosyası, büyük binary dosyaları ve karma lisans yükü oluşturur. Burada bağımlılık manifesti ve özelleştirilmiş çalıştırma/QA becerileri verildi.
