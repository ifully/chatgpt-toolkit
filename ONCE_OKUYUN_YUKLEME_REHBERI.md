# ChatGPT Toolkit — beş Agent Skills kaynağı için yükleme rehberi

**Hazırlanma tarihi:** 28 Ekim 2026  
**Hedef depo:** https://github.com/ifully/chatgpt-toolkit  
**Temel alınan depo commit'i:** `0ce7de55e8e717dfc364a2faa597e0e987085143`

## Bu paket ne yapar?

`chatgpt-toolkit/` klasörü, mevcut GitHub deponuza **eklendiğinde/değiştirildiğinde** kullanılacak dosyaları içerir. Bu, sıfırdan ayrı bir repo değildir; **yalnızca değişen ve yeni dosyaların üstüne ekleme paketidir**.

- `tools.yaml` ve `tools.json`: 61 kayıt 66 kayda çıkarıldı.
- `README.md`, `START_HERE.md`, `LICENSE_AND_SECURITY.md`: Yeni kaynaklar ve lisans sınırları işlendi.
- `categories/design-creative.md`, `categories/security-testing.md`, `categories/academic-research.md`: Beş kaynak kendi kategorilerine eklendi.
- `categories/agent-skills.md`: Beceri seçimi için yeni kategori.
- `integrations/agent-skills/`: Beş ZIP için kaynak, lisans, SHA-256 ve beceri dosyası envanteri.
- `playbooks/skill-evaluation.md`: Lisans, güvenlik ve uyumluluk değerlendirme kontrol listesi.

## GitHub'a nasıl yüklersiniz?

1. ZIP'i bilgisayarınızda **açın**. GitHub'a ZIP dosyasını doğrudan yüklemek klasör içeriğini otomatik açmaz.
2. [GitHub deponuzu](https://github.com/ifully/chatgpt-toolkit) açın. Mümkünse yeni bir dal oluşturup değişiklikleri önce o dalda inceleyin.
3. `chatgpt-toolkit/` klasörünün **içindeki** dosya ve klasörleri aynı göreli yollar korunacak şekilde depo köküne ekleyin. Üstteki `ONCE_OKUYUN_YUKLEME_REHBERI.md` dosyasını depoya eklemek zorunda değilsiniz.
4. Aynı isimli mevcut dosyaların (`README.md`, `START_HERE.md`, `tools.yaml`, `tools.json`, `LICENSE_AND_SECURITY.md`, üç kategori rehberi ve `playbooks/academic-research.md`) yeni sürümlerini birleştirin/değiştirin. Bu paket yalnızca belirtilen temel commit üzerinden hazırlandı; depo daha sonra değiştiyse çakışmaları elle gözden geçirin.
5. GitHub değişiklik önizlemesinde aşağıdaki yolları ve 66 kayıt sonucunu kontrol edin, sonra commit/PR oluşturun.

**Kritik:** Klasörün kendisini repo köküne `chatgpt-toolkit/chatgpt-toolkit/` olarak koymayın. Dosyalar mevcut `README.md` ve `tools.yaml` ile aynı kök seviyesinde bulunmalı.

## İsteğe bağlı yerel Git yöntemi

Mevcut Git deposunun yerel kopyası içindeyken ZIP'ten çıkarılan `chatgpt-toolkit/` içeriğini depo köküyle birleştirin. Sonra `git diff`, `git status`, `git add`, `git commit` ve `git push` sırasını izleyin. Mevcut dosyalarınız daha yeniyse körlemesine üzerine yazmayın.

## Neler özellikle DAHİL EDİLMEDİ?

- Beş kaynak deponun bütün kaynak kodları veya orijinal ZIP dosyaları
- Kurulum betikleri, uzaktan kod çalıştıran komutlar ve örnek medya
- Otomatik ChatGPT/Claude/Codex beceri kurulumu
- GitHub hesabınızda commit veya push işlemi

Deponuzun mevcut [AGENTS.md](https://github.com/ifully/chatgpt-toolkit/blob/main/AGENTS.md) ve güvenlik politikası, üçüncü taraf kaynakların otomatik yüklenmediğini ve kodlarının katalogda barındırılmadığını açıkça belirtiyor. Bu paket o ilkeye uyuyor.

## Doğrulama özeti

- Beş ZIP arşivi bütünlük testini geçti.
- Arşivlerin gerçek kaynakları ve örnek `SKILL.md` yolları incelendi.
- `tools.yaml` ↔ `tools.json` alan ve kayıt eşitliği kontrol edilmelidir; hazırlanırken JSON YAML'dan üretildi.
- Beş kaynak referans olarak eklendi; hiçbiri kurulu/çalışıyor olarak işaretlenmedi.

Envanter ve lisans ayrıntıları: `chatgpt-toolkit/integrations/agent-skills/SOURCES_AND_LICENSES.md`.
