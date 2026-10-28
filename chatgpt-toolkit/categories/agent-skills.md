# Agent Skills — beceri kaynakları

Bu sayfa, `SKILL.md` biçiminde görev iş akışları sunan depoların **referans kataloğudur**. Bir kaynağın bu listeye eklenmesi onun ChatGPT Web'e, Codex'e veya bilgisayara yüklendiği anlamına gelmez.

**28 Ekim 2026 tarihinde yüklenen beş ZIP arşivi** incelenerek aşağıdaki seçki hazırlandı. Arşiv kökeni, dosya yolları ve lisans notları için [entegrasyon kaydı](../integrations/agent-skills/README.md) ile [kaynak/lisans tablosuna](../integrations/agent-skills/SOURCES_AND_LICENSES.md) bakın.

| Öncelik | Kaynak | Örnek beceriler | Kategori | Dağıtım kararı |
|---|---|---|---|---|
| 1 | [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | `ui-ux-pro-max`, `design-system`, `brand` | Tasarım | MIT; katalog bağlantısı |
| 1 | [K-Dense Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) | `literature-review`, `peer-review`, `citation-management`, `scientific-writing` | Akademik araştırma | Kök MIT; beceri bazında lisans kontrolü |
| 2 | [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills) | `web-design-guidelines`, `react-best-practices` | Web tasarımı | Kök lisans belirsiz; yalnızca bağlantı |
| 2 | [Claude Remotion Skill](https://github.com/haidrrrry/claude-remotion-skill) | `remotion-motion-graphics` | Hareketli grafik | MIT; katalog bağlantısı |
| 2 | [Trail of Bits Skills](https://github.com/trailofbits/skills) | `differential-review`, `agentic-actions-auditor` | Güvenlik | CC BY-SA 4.0; yalnızca bağlantı |

## Seçim rehberi

- **Akademik makale, sistematik tarama, araştırma etiği ve hakemlik:** K-Dense seçkisini PyAlex/Zotero iş akışlarıyla karşılaştırarak kullanın; DOI doğrulaması iddianın kaynakla desteklendiğini tek başına kanıtlamaz. Gizli hakemlik metinlerini dış servise göndermeden önce yetki ve dergi politikalarını denetleyin.
- **Görsel sistem, tipografi, renk, UI/UX:** Önce UI/UX Pro Max; içerikteki örnekleri tasarım bağlamına göre eleştirel değerlendirin.
- **Web arayüzünün kod, erişilebilirlik ve performans incelemesi:** Vercel Agent Skills. `web-design-guidelines` güncel yönergeleri internetten çekebilir; alınan içeriği ve kaynağı doğrulayın.
- **Kinetik tipografi, logo animasyonu, hareketli afiş:** Claude Remotion Skill. Remotion/React, uygun video render ortamı ve gerektiğinde FFmpeg gerekir; salt `SKILL.md` bu bağımlılıkları kurmaz.
- **Kod güvenliği ve CI iş akışı:** Trail of Bits Skills. İlgili becerinin sistem bağımlılıklarını ve riskli komutlarını denetleyin; bazıları başka Claude Code eklentilerini gerektirir.

## Uygulama ilkeleri

1. Önce [beceri değerlendirme iş akışını](../playbooks/skill-evaluation.md) uygulayın.
2. Tekil `SKILL.md` ve destekleyici dosyaların yolunu, lisansını ve bağımlılıklarını doğrulayın.
3. Kaynağı görevle ilişkilendirin; kopyalama/kurulum kararını ayrıca verin.
4. İşlem gerektiren becerileri, sadece izin verilmiş ve doğrulanmış çalışma ortamında çalıştırın.
5. Bu depo otomatik kurulum manifesti değildir.

> Katalogda halihazırda bulunan `openai/skills` ve `anthropics/skills` yeniden eklenmemiştir. Buradaki beş kaynak, mevcut 61 kayıt üzerine eklenmiştir.
