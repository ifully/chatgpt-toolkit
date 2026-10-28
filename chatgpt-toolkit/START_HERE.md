# ChatGPT Toolkit — Başlangıç ve kullanım rehberi

> **Bu depodaki GitHub projeleri otomatik olarak ChatGPT'ye kurulmaz.** Depo, araç seçimini, uygunluk denetimini ve güvenli kullanım biçimini standartlaştırmak amacıyla hazırlanmış bir kataloğudur.

**Güncelleme:** 28 Ekim 2026  
**Kapsam:** Yapay zekâ, akademik araştırma, programlama, belge üretimi, tasarım, veri analizi, otomasyon ve güvenlik.

## Başlangıç

1. Araçları `tools.yaml` veya `tools.json` üzerinden inceleyin.
2. Konuya göre `categories/` klasöründeki rehberi okuyun.
3. İş türüne göre `playbooks/` klasöründeki kontrol listesini uygulayın.
4. Kod ajanları için `AGENTS.md` güvenlik ve seçim yönergesini kullanın.
5. İlgili kaynağın güncel README, lisans, sürüm ve bağımlılıklarını ayrıca doğrulayın.
6. Ajan becerileri için `integrations/agent-skills/catalog.yaml` kaydındaki ZIP kökenini ve seçilmiş `SKILL.md` yollarını kontrol edin; beceriler otomatik kurulmaz.

## ChatGPT Web'de gerçek kullanım modeli

| Durum | Anlamı | Ne gerekir? |
|---|---|---|
| Kaynak okuma | Public GitHub repo içeriğini incelemek | URL ve erişim |
| Python paketi | Mevcut yürütme ortamında kod çalıştırmak | Kurulu paket, gerekli izinler ve bağımlılıklar |
| Komut satırı | CLI üzerinden araç çalıştırmak | Çalışır komut ve uygun işletim ortamı |
| Web uygulaması | Site üzerinden hizmete erişmek | Web/servis hesabı; işlem için uygun tarayıcı veya entegrasyon |
| MCP sunucusu | ChatGPT/ajanı haricî araca bağlamak | Uyumlu istemci, uzak/yerel sunucu ve hesap izni |
| Dış ajan | Ajan sistemini ayrı başlatmak | İşletim ortamı, API anahtarları ve işlem yetkisi |

**Önemli:** Repo kataloğuna ekleme veya Star/Fork işlemi, ChatGPT'nin kabiliyetlerini kendiliğinden genişletmez. Kurulumlar oturum ve dağıtım ortamına bağlıdır. Özellikle gizli verileri public GitHub'a koymayın.

## Benimle kullanmak için örnek istek

> `https://github.com/ifully/chatgpt-toolkit deposundaki tools.yaml ve AGENTS.md dosyalarını incele. Şu görev için en uygun üç aracı belirle: [görev]. Mevcut oturumda gerçekten kullanılabilir olanları test et, kullanılamayanlar için hangi kurulum veya entegrasyonun eksik olduğunu belirt. Gereksiz kurulum yapma.`

## Kategori rehberleri
- [Yapay zekâ ajanları ve bilgi erişimi](categories/ai-agents.md)
- [Akademik araştırma ve belge üretimi](categories/academic-research.md)
- [Kod geliştirme ve test](categories/coding-development.md)
- [Tasarım, tipografi ve yaratıcı kodlama](categories/design-creative.md)
- [Veri analizi ve istatistik](categories/data-analysis.md)
- [Otomasyon ve MCP](categories/automation-mcp.md)
- [Güvenlik, erişilebilirlik ve kalite](categories/security-testing.md)
- [Agent Skills beceri depoları](categories/agent-skills.md)

## Görev akışları
- [Akademik literatür incelemesi](playbooks/academic-research.md)
- [Belge üretimi ve kalite kontrol](playbooks/document-production.md)
- [Yazılım deposu analizi](playbooks/repository-audit.md)
- [Web uygulaması testleri](playbooks/web-app-audit.md)
- [Veri analizi](playbooks/data-analysis.md)
- [Tasarım ve tipografi denetimi](playbooks/design-quality.md)
- [Üçüncü taraf beceri değerlendirmesi](playbooks/skill-evaluation.md)
- [Beceri performansını ölçme ve iyileştirme döngüsü](playbooks/agent-skill-quality-loop.md)

## Lisans ve güvenlik
- [Lisans/tedarik zinciri kuralları](LICENSE_AND_SECURITY.md)

Bu katalog bir bağlantı ve iş akışı dizinidir; kaynak kodlarının dağıtımı değildir. Repo lisansları, servis fiyatları ve sürümler zamanla değişebilir. Kopyalama, dağıtma veya üretime alma öncesinde kaynak depoları yeniden denetlenmelidir.

**28 Ekim 2026 v3 eklentisi:** Kullanıcı arşivlerinden doğrulanan 15 yeni depo, önceki 66 katalog kaydı üzerine eklenerek toplam 81 kayıt oluşturuldu. Bazı kaynaklar Agent Skills koleksiyonu, bazıları değerlendirme, MCP veya keşif altyapısıdır. [15 arşivlik ayrıntılı inceleme](integrations/agent-skills/BATCH-V3-ARCHIVE-AUDIT.md).
