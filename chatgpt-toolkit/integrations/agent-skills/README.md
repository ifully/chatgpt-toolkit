# Üçüncü taraf Agent Skills — 20 arşivin katalog entegrasyonu

**İnceleme tarihi:** 28 Ekim 2026  
**Kapsam:** Kullanıcı tarafından iki aşamada sağlanan 20 ZIP arşivi  
**Yöntem:** ZIP bütünlük testi; README, lisans ve örnek `SKILL.md` incelemesi; katalog alanlarının eşleştirilmesi. Arşivlerdeki betikler **çalıştırılmadı**.

Bu entegrasyon, `chatgpt-toolkit` deposunun mevcut **bağlantı ve çalışma akışı kataloğu** yaklaşımını korur. Hiçbir üçüncü taraf beceri kodu, medya dosyası, komut çalıştırıcısı veya geniş kaynak ağacı yeniden paketlenmemiştir.

### İlk beş ZIP (v2)

| Sağlanan ZIP | Doğrulanan kaynak | Belirgin beceri yolu | Depodaki durum |
|---|---|---|---|
| `ui-ux-pro-max-skill-main.zip` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | `.claude/skills/ui-ux-pro-max/SKILL.md` | Kataloga eklendi |
| `agent-skills-main.zip` | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | `skills/web-design-guidelines/SKILL.md` | Kataloga eklendi; lisans kontrolü gerekli |
| `claude-remotion-skill-main.zip` | [haidrrrry/claude-remotion-skill](https://github.com/haidrrrry/claude-remotion-skill) | `remotion-motion-graphics/SKILL.md` | Kataloga eklendi |
| `skills-main.zip` | [trailofbits/skills](https://github.com/trailofbits/skills) | `plugins/differential-review/skills/differential-review/SKILL.md` | Kataloga eklendi; CC BY-SA 4.0 |
| `scientific-agent-skills-main.zip` | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | `skills/literature-review/SKILL.md` | Kataloga eklendi; tekil beceri lisansı denetlenmeli |

### Sonraki on beş ZIP (v3)

Kaynak, arşiv ismi, `SKILL.md` adedi, kök lisans bulgusu, SHA-256 ve istisnalar [V3 — 15 arşiv denetimi](BATCH-V3-ARCHIVE-AUDIT.md) dosyasında ayrı ayrı yer alır. Bu on beş kaynak, katalogdaki 66 kayda eklenerek toplam **81** kayıt oluşturmuştur. Bunların üçü doğrudan `SKILL.md` içermez (OpenAI Evals, MCP Registry, VoltAgent dizini); diğer bazıları ana ürünün içinde yalnızca örnek beceriler sunar.

## Dosyaların rolü

- [`catalog.yaml`](catalog.yaml): Yirmi kaynağın makinece okunabilir seçki ve bağımlılık kayıtları.
- [`SOURCES_AND_LICENSES.md`](SOURCES_AND_LICENSES.md): Orijinal ZIP doğrulama özetleri, SHA-256 ve lisans sınırları.
- [`BATCH-V3-ARCHIVE-AUDIT.md`](BATCH-V3-ARCHIVE-AUDIT.md): Sonradan sağlanan 15 ZIP'in SHA-256, kaynak eşleştirmesi ve bulguları.
- [`../../categories/agent-skills.md`](../../categories/agent-skills.md): Okuyucu için kullanım karşılaştırması.
- [`../../playbooks/skill-evaluation.md`](../../playbooks/skill-evaluation.md): Kurulumdan veya kod taşımadan önce uygulanacak denetim protokolü.
- [`../../playbooks/agent-skill-quality-loop.md`](../../playbooks/agent-skill-quality-loop.md): Beceri değerlendirme ve kontrollü iyileştirme döngüsü.

## İleride gerçek beceri kurulumu istenirse

1. Kullanılacak tekil beceriyi ve hedef ajanı (`ChatGPT`, `Codex`, `Claude Code` vb.) belirleyin.
2. Kurulum yolunun ve `SKILL.md` biçiminin o ortamda desteklendiğini resmi belgelerden doğrulayın.
3. Lisans, betik, dış ağ çağrısı ve veri gizliliği denetimini tamamlayın.
4. Kaynak revizyonunu sabitleyip, ayrı bir uygulama/proje ortamında kontrollü kurulum yapın.
5. Davranışı örnek görevlerde test edin; katalogda "kurulu" olarak yalnızca gerçekten kuruluysa işaretleyin.

**Not:** Bu işlem bir ChatGPT becerisi yüklemesi veya GitHub deposuna otomatik gönderim değildir. Kataloğun referans listesi toplam yirmi kullanıcı arşiviyle genişletilmiştir. Kaynak ZIP'ler dağıtıma alınmamıştır.
