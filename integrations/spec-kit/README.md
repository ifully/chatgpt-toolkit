# Spec Kit yöntemi — ChatGPT Web köprüsü

**Amacı:** Kaynak dosyaları / proje gereksinimlerini dayanak alarak kapsam, teknik plan, test ve teslimat belgelerini üretmek; mevcut projelerde geri alınabilir değişiklikler yapmak.

## Kullanım biçimleri

| Biçim | Gereksinim | Yapabilecekleri | Yapamayacakları |
|---|---|---|---|
| ChatGPT Web, belge temelli | Bu depoya erişim ve proje dosyaları | Constitution, spec, clarify, plan, tasks, analyze, implement (uygun araç varsa), validate belgeleri | Resmî slash komutlarını veya CLI'ı otomatik etkinleştiremez |
| Kod çalıştırmalı oturum | Kod/dosya çalışma ortamı + bağımlılıklar | Uygun kodu değiştirme ve mevcut testleri çalıştırma | Gizli bağımlılıkları veya erişilemeyen servisleri otomatik sağlayamaz |
| Spec Kit CLI + Codex / uyumlu ajan | Python 3.11+, uv, specify-cli ve desteklenen ajan | Resmî Spec Kit komut/skill akışı | ChatGPT Web sohbetine kendiliğinden entegre olmaz |

## Resmî kaynaklar

- Kaynak: https://github.com/github/spec-kit
- Başlangıç: https://github.com/github/spec-kit/blob/main/docs/quickstart.md
- Mevcut projeler: https://github.com/github/spec-kit/blob/main/docs/guides/existing-projects.md
- Codex: https://github.com/github/spec-kit/blob/main/docs/integrations/codex.md
- Lisans: https://github.com/github/spec-kit/blob/main/LICENSE — MIT, Copyright GitHub, Inc.

## Önemli

Bu dizindeki metinler **bizim ChatGPT Web uyarlamamızdır**; GitHub'ın resmî Spec Kit şablonlarının birebir kopyası veya kurulu Specify CLI çıktısı değildir. Akademik araştırma akışı ayrıca uyarlanmıştır ve **orijinal Spec Kit'in yerleşik akademik özelliği değildir.**

İlgili dosyaları bu GitHub deposundan her yeni sohbet için okuyabilen bir asistan bunları uygulayabilir. Depo bağlantısı hatırlanabilir olsa da oturumlar arası otomatik okuma veya sürekli kurulu bir eklenti garantisi yoktur.
