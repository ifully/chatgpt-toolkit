# ChatGPT Toolkit v4 — GitHub yükleme rehberi

**Tarih:** 28 Ekim 2026  
**Hedef GitHub deposu:** https://github.com/ifully/chatgpt-toolkit  
**Temel depo commit'i:** `0ce7de55e8e717dfc364a2faa597e0e987085143`

## Ne hazırladık?

Bu ZIP'in `chatgpt-toolkit/` dizini, **var olan GitHub deponuzun kökünde** güncellenecek veya yeni eklenecek dosyaları içerir. ZIP kaynak kodu derlemesi veya otomatik beceri yükleyicisi değildir.

| Aşama | Katalog |
|---|---:|
| İlk orijinal depo | 61 kaynak |
| v2 — ilk beş beceri ZIP'i | 66 kaynak |
| v3 — sonraki on beş beceri/ajan ZIP'i | 81 kaynak |
| **v4 — bu turdaki on dört bilimsel/teknik ZIP** | **95 benzersiz kaynak** |

**v4 paketi önceki v2 ve v3 içeriklerini kapsar.** Daha önceki ZIP paketlerini ayrıca yüklemek gerekmez.

### Önemli içerik

- `tools.yaml` / `tools.json`: 95 benzersiz GitHub deposunu aynı veri ve sırayla tanımlar.
- `categories/scientific-projects.md`: Bilimsel fikir, hipotez, yöntem, görsel algı, bilimsel arşiv ve tekrar üretilebilirlik.
- `categories/reverse-engineering.md`: Yetkili yazılım analizi ve görsel yeniden yapılandırma kaynakları.
- `integrations/research-tools/catalog.yaml`: 14 yeni kaynağın kimliği, arşiv adı, SHA-256, lisans ve kullanım sınıfı.
- `integrations/research-tools/ARCHIVE-AUDIT-V4.md`: 14 ZIP'in bütünlük, lisans ve kaynak eşleştirmesi.
- `playbooks/research-project-methodology.md`: Yöntem, etik, veri, kanıt ve yayın doğrulaması kontrol listesi.
- `integrations/agent-skills/`: Önceki 20 beceri arşivinin bütün katalog/denetim kayıtları korunmuştur.

## Yükleme adımları

1. **ZIP'i bilgisayarınızda açın.** GitHub'a ZIP'in kendisini yüklemek içindeki dosyaları açmaz.
2. GitHub'da [ifully/chatgpt-toolkit](https://github.com/ifully/chatgpt-toolkit) deposunu açın ve tercihen `toolkit-v4` adlı bir dal/PR oluşturun.
3. ZIP içindeki `chatgpt-toolkit/` klasörünün **içindekileri** deponuzun köküyle birleştirin. `chatgpt-toolkit/chatgpt-toolkit/` şeklinde ikinci bir depo klasörü oluşturmayın.
4. Yeni `integrations/research-tools/`, `categories/scientific-projects.md`, `categories/reverse-engineering.md` ve `playbooks/research-project-methodology.md` yollarını ekleyin.
5. Var olan `README.md`, `START_HERE.md`, `tools.yaml`, `tools.json`, kategori belgeleri ve güvenlik notlarının farklarını kontrol edin. Güncelde kişisel değişiklikler varsa dosyaları **elle birleştirin**.
6. `tools.yaml` ve `tools.json` içinde **95** benzersiz `repo` bulunduğunu ve herhangi bir dosya silinmediğini doğruladıktan sonra commit/PR tamamlayın.

**Çakışma uyarısı:** ZIP'in temel aldığı commit 28 Ekim 2026 tarihinde denetlenmiştir. GitHub deponuz bu commit'ten sonra değiştiyse dosyaları körlemesine üzerine yazmayın; birleştirme gerekir.

## Bilinçli sınırlar

- 14 kaynağın büyük ZIP arşivleri veya uygulama kaynak kodları buraya alınmadı.
- Hiçbir üçüncü taraf kurulum betiği, bilimsel model, medya dosyası, GPU bağımlılığı, veri kümesi veya API anahtarı içermiyor.
- Ghidra, angr ve Rizin otomatik kurulmadı/çalıştırılmadı; yazılım analizi yalnızca izinli kapsamda yapılabilir.
- Akademik yazılımın veya görüntü dönüşümünün bilimsel geçerliği kendiliğinden kanıtlanmaz.
- GitHub hesabınızda commit, push veya PR işlemi yapılmadı.

## Test özeti

| Denetim | Sonuç |
|---|---|
| Yeni ZIP bütünlük testi | 14/14 geçti |
| Toplam makinece okunabilir araç | 95 |
| Benzersiz GitHub depo kimliği | 95 |
| YAML–JSON içerik eşitliği | Geçti |
| Önceki beceri envanteri | 20 kaynak, korundu |
| Yeni araştırma/tersine mühendislik envanteri | 14 kaynak |
| Kaynak kodu yeniden dağıtımı | Yok |

Detaylı dosyalar ve lisans kayıtları `chatgpt-toolkit/integrations/` altındadır.
