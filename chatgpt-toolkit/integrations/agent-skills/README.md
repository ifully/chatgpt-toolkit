# Üçüncü taraf Agent Skills — dört arşivin entegrasyonu

**İnceleme tarihi:** 28 Ekim 2026  
**Kapsam:** Kullanıcı tarafından sağlanan dört ZIP arşivi  
**Yöntem:** ZIP bütünlük testi; README, lisans ve örnek `SKILL.md` incelemesi; katalog alanlarının eşleştirilmesi. Arşivlerdeki betikler **çalıştırılmadı**.

Bu entegrasyon, `chatgpt-toolkit` deposunun mevcut **bağlantı ve çalışma akışı kataloğu** yaklaşımını korur. Hiçbir üçüncü taraf beceri kodu, medya dosyası, komut çalıştırıcısı veya geniş kaynak ağacı yeniden paketlenmemiştir.

| Sağlanan ZIP | Doğrulanan kaynak | Belirgin beceri yolu | Depodaki durum |
|---|---|---|---|
| `ui-ux-pro-max-skill-main.zip` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | `.claude/skills/ui-ux-pro-max/SKILL.md` | Kataloga eklendi |
| `agent-skills-main.zip` | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | `skills/web-design-guidelines/SKILL.md` | Kataloga eklendi; lisans kontrolü gerekli |
| `claude-remotion-skill-main.zip` | [haidrrrry/claude-remotion-skill](https://github.com/haidrrrry/claude-remotion-skill) | `remotion-motion-graphics/SKILL.md` | Kataloga eklendi |
| `skills-main.zip` | [trailofbits/skills](https://github.com/trailofbits/skills) | `plugins/differential-review/skills/differential-review/SKILL.md` | Kataloga eklendi; CC BY-SA 4.0 |

## Dosyaların rolü

- [`catalog.yaml`](catalog.yaml): Dört kaynağın makinece okunabilir seçki ve bağımlılık kayıtları.
- [`SOURCES_AND_LICENSES.md`](SOURCES_AND_LICENSES.md): Orijinal ZIP doğrulama özetleri, SHA-256 ve lisans sınırları.
- [`../../categories/agent-skills.md`](../../categories/agent-skills.md): Okuyucu için kullanım karşılaştırması.
- [`../../playbooks/skill-evaluation.md`](../../playbooks/skill-evaluation.md): Kurulumdan veya kod taşımadan önce uygulanacak denetim protokolü.

## İleride gerçek beceri kurulumu istenirse

1. Kullanılacak tekil beceriyi ve hedef ajanı (`ChatGPT`, `Codex`, `Claude Code` vb.) belirleyin.
2. Kurulum yolunun ve `SKILL.md` biçiminin o ortamda desteklendiğini resmi belgelerden doğrulayın.
3. Lisans, betik, dış ağ çağrısı ve veri gizliliği denetimini tamamlayın.
4. Kaynak revizyonunu sabitleyip, ayrı bir uygulama/proje ortamında kontrollü kurulum yapın.
5. Davranışı örnek görevlerde test edin; katalogda "kurulu" olarak yalnızca gerçekten kuruluysa işaretleyin.

**Not:** Bu işlem bir ChatGPT becerisi yüklemesi veya GitHub deposuna otomatik gönderim değildir. Kataloğun referans listesi dört kaynakla genişletilmiştir.
