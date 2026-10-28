# ChatGPT Toolkit v3 — GitHub yükleme rehberi

**Tarih:** 28 Ekim 2026  
**Hedef:** https://github.com/ifully/chatgpt-toolkit  
**Dayanak alınan depo commit'i:** `0ce7de55e8e717dfc364a2faa597e0e987085143`

## Paket içeriği

Bu ZIP, `chatgpt-toolkit/` dizininde **GitHub depo köküne yerleştirilecek değiştirilmiş ve yeni katalog dosyalarını** içerir; tüm projelerin kopyası değildir. Üçüncü taraf beceri kodu veya çalıştırma betiği bulunmaz.

- İlk arşiv paketinin 5 kaydı ve bu turda sağlanan 15 yeni arşiv: 20 kullanıcı ZIP'i.
- Mevcut katalog 61 → 66 → **81 benzersiz GitHub depo kaydı**. **Önceki v2 dosyasını ayrıca yüklemek gerekmez**; bu sürüm önceki v2 katalog güncellemesini de kapsar.
- `tools.yaml` ve `tools.json`: 81 kayıt; alanları ve sıraları eşleşir.
- `categories/agent-skills.md`: Kaynakların doğrudan beceri, araç, altyapı veya keşif dizini olarak ayrımı.
- `integrations/agent-skills/catalog.yaml`: 20 ZIP'in kayıtları ve seçilen `SKILL.md` yolları.
- `integrations/agent-skills/BATCH-V3-ARCHIVE-AUDIT.md`: Son 15 ZIP'in gerçek kaynak eşleştirmesi, lisans/CRC ve SHA-256 bilgileri.
- `playbooks/agent-skill-quality-loop.md`: Ölçme, güvenlik denetimi, gerileme testi ve insan onayı çerçevesi.

## GitHub'a yükleme

1. **ZIP'i bilgisayarında aç.** GitHub web arayüzüne ZIP dosyasını tek parça olarak yüklemek içindeki dosyaları otomatik çıkarmaz.
2. [ChatGPT Toolkit](https://github.com/ifully/chatgpt-toolkit) deposuna git. Mümkünse `toolkit-v3` adında yeni bir dal aç veya PR üzerinde incele.
3. ZIP içindeki `chatgpt-toolkit/` klasörünün **içeriğini**, deponun kök diziniyle aynı dosya yollarına yerleştir. `chatgpt-toolkit/chatgpt-toolkit/` gibi iç içe ekleme yapma.
4. Aynı isimli dosyaları güncelle; yeni `integrations/agent-skills/BATCH-V3-ARCHIVE-AUDIT.md` ve `playbooks/agent-skill-quality-loop.md` dosyalarını ekle.
5. GitHub değişiklik önizlemesinde beklenmedik silme/çakışma olmadığını, `tools.yaml` ve `tools.json` toplamının **81** olduğunu doğrula.
6. Onayladıktan sonra commit/PR tamamla.

**Önemli çakışma uyarısı:** Paket, yukarıda belirtilen commit ve aynı tarihteki v2 katalog dosyaları üzerinde hazırlanmıştır. GitHub'daki mevcut dosyalar bu tarihten sonra değiştiyse yeni sürümleri körlemesine üstlerine yazmayın; içerik birleştirmesi yapın. Özellikle `README.md`, `tools.yaml`, `tools.json`, `START_HERE.md` ve aynı isimli kategori rehberleri kontrol edilmelidir.

## Bilinçli olarak paketlenmeyenler

- Kullanıcının 15 orijinal ZIP'i (toplam yüzlerce MB)
- Üçüncü taraf `SKILL.md` içeriği, çalıştırılabilir kod, örnek medya ve install komutları
- Kimlik bilgileri, API anahtarları, model ağırlıkları ve ek kurulum bağımlılıkları
- GitHub hesabı üzerinde otomatik commit, push, beceri etkinleştirme veya ChatGPT'ye kurulum

Katalogdaki kaynaklar birer **referanstır**. `remotion-dev/skills` kök lisansı bu arşivde bulunamamış, NVIDIA ve MCP Registry karma lisansları ayrı not edilmiş, Superpowers küresel talimatları uygulanmamıştır. Bütün arşivler CRC/bütünlük testini geçmiştir; bu kod güvenliği garantisi değildir.

## Kontrol özeti

| Kontrol | Sonuç |
|---|---|
| Yeni ZIP arşivleri | 15 / 15 bütünlük doğrulaması başarılı |
| Toplam katalog kaydı | 81; benzersiz depo kimliği |
| JSON/YAML eşleşmesi | Doğrulandı |
| Arşiv kökeni kayıtları | 20 |
| Seçilen `SKILL.md` dosya yolları | 62; tamamı sağlanan ilgili ZIP'lerde mevcut |
| Üçüncü taraf kaynak kodu yeniden dağıtımı | Yok |

**Sonuç:** ZIP, var olan GitHub deposuna kontrollü olarak eklenebilecek katalog dosyalarını içerir. Otomatik beceri kurulumu veya ajan davranışı değişikliği yapmaz.
