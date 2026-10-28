# Agent Skills — beceri kaynakları

Bu sayfa, `SKILL.md` biçiminde görev iş akışları sunan depoların **referans kataloğudur**. Bir kaynağın bu listeye eklenmesi onun ChatGPT Web'e, Codex'e veya bilgisayara yüklendiği anlamına gelmez.

**28 Ekim 2026 tarihinde sağlanan 20 ZIP arşivi** iki aşamada incelendi. İlk beş kaynak ve daha sonra gelen on beş kaynak ayrı değerlendirilmiştir. ZIP kökeni, dosya yolları ve lisans notları için [entegrasyon kaydı](../integrations/agent-skills/README.md) ile [v3 doğrulama tablosuna](../integrations/agent-skills/BATCH-V3-ARCHIVE-AUDIT.md) bakın.

### Önceki beş kaynak (v2)

| Öncelik | Kaynak | Örnek beceriler | Kategori | Dağıtım kararı |
|---|---|---|---|---|
| 1 | [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | `ui-ux-pro-max`, `design-system`, `brand` | Tasarım | MIT; katalog bağlantısı |
| 1 | [K-Dense Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) | `literature-review`, `peer-review`, `citation-management`, `scientific-writing` | Akademik araştırma | Kök MIT; beceri bazında lisans kontrolü |
| 2 | [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills) | `web-design-guidelines`, `react-best-practices` | Web tasarımı | Kök lisans belirsiz; yalnızca bağlantı |
| 2 | [Claude Remotion Skill](https://github.com/haidrrrry/claude-remotion-skill) | `remotion-motion-graphics` | Hareketli grafik | MIT; katalog bağlantısı |
| 2 | [Trail of Bits Skills](https://github.com/trailofbits/skills) | `differential-review`, `agentic-actions-auditor` | Güvenlik | CC BY-SA 4.0; yalnızca bağlantı |

### Yeni on beş kaynak (v3)

| Öncelik | Kaynak | Seçilen örnek beceri veya ana işlev | Tür | Lisans/uygulama kararı |
|---|---|---|---|---|
| 1 | [Context Engineering Skills](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | `context-compression`, `evaluation`, `memory-systems` | Beceri | MIT; bağlantı |
| 1 | [Sentry Skills](https://github.com/getsentry/skills) | `skill-writer`, `skill-scanner`, `brand-guidelines` | Beceri | Apache-2.0; bağlantı |
| 1 | [Hugging Face Skills](https://github.com/huggingface/skills) | `hf-cli`, `huggingface-datasets`, `huggingface-community-evals` | Beceri | Apache-2.0; bağlantı |
| 1 | [Awesome Copilot](https://github.com/github/awesome-copilot) | `adobe-illustrator-scripting`, `penpot-uiux-design` | Topluluk beceri koleksiyonu | MIT; seçici inceleme |
| 1 | [Remotion Skills](https://github.com/remotion-dev/skills) | `remotion-render`, `remotion-captions` | Beceri | Kök lisans belirsiz; bağlantı |
| 1 | [OpenAI Evals](https://github.com/openai/evals) | Model/ajan test senaryoları | Değerlendirme aracı | MIT; ayrı kurulum |
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | LLM değerlendirme ve red-team | Değerlendirme aracı + örnek beceriler | MIT; ayrı CLI |
| 1 | [Context7](https://github.com/upstash/context7) | `context7-mcp`, `find-docs` | MCP ve beceri | MIT; bağlantı/kurulum ayrımı |
| 2 | [Superpowers](https://github.com/obra/superpowers) | `systematic-debugging`, `verification-before-completion` | Beceri | MIT; genel kuralları aktarma |
| 2 | [wshobson Agents](https://github.com/wshobson/agents) | `llm-evaluation`, `screen-reader-testing` | Beceri/ajan koleksiyonu | MIT; seçici inceleme |
| 2 | [seb1n Agent Skills](https://github.com/seb1n/awesome-ai-agent-skills) | `agent-evaluation`, `skill-supply-chain-audit` | Topluluk beceri koleksiyonu | MIT; seçici inceleme |
| 2 | [MCP Registry](https://github.com/modelcontextprotocol/registry) | Sunucu kayıt ve keşfi | MCP altyapısı | Karma/geçiş lisansı |
| 2 | [Deep Agents](https://github.com/langchain-ai/deepagents) | Dosya/bellek/uzun görev altyapısı | Ajan çatısı + örnek beceriler | MIT; ayrı uygulama |
| 3 | [NVIDIA Skills](https://github.com/NVIDIA/skills) | `nvidia-skill-finder`, `data-designer` | Beceri | Apache-2.0 + CC-BY-4.0 |
| 3 | [VoltAgent Awesome Agent Skills](https://github.com/VoltAgent/awesome-agent-skills) | Üçüncü taraf beceri bağlantıları | Yalnızca dizin | MIT; SKILL.md bulunmadı |

## Seçim rehberi

- **Akademik makale, sistematik tarama, araştırma etiği ve hakemlik:** K-Dense seçkisini PyAlex/Zotero iş akışlarıyla karşılaştırarak kullanın; DOI doğrulaması iddianın kaynakla desteklendiğini tek başına kanıtlamaz. Gizli hakemlik metinlerini dış servise göndermeden önce yetki ve dergi politikalarını denetleyin.
- **Görsel sistem, tipografi, renk, UI/UX:** Önce UI/UX Pro Max; içerikteki örnekleri tasarım bağlamına göre eleştirel değerlendirin.
- **Web arayüzünün kod, erişilebilirlik ve performans incelemesi:** Vercel Agent Skills. `web-design-guidelines` güncel yönergeleri internetten çekebilir; alınan içeriği ve kaynağı doğrulayın.
- **Kinetik tipografi, logo animasyonu, hareketli afiş:** Claude Remotion Skill. Remotion/React, uygun video render ortamı ve gerektiğinde FFmpeg gerekir; salt `SKILL.md` bu bağımlılıkları kurmaz.
- **Kod güvenliği ve CI iş akışı:** Trail of Bits Skills. İlgili becerinin sistem bağımlılıklarını ve riskli komutlarını denetleyin; bazıları başka Claude Code eklentilerini gerektirir.
- **Bağlam ve beceri geliştirme:** Context Engineering + Sentry Skills + OpenAI Evals/Promptfoo. Becerili/becerisiz testlerde ölçülen katkıyı karşılaştırın.
- **Adobe Illustrator / hareketli grafik:** Awesome Copilot'daki Illustrator örneğini ve Remotion Skills'i ayrı değerlendirin; uygulama, render ve lisans koşullarını doğrulayın.
- **Güncel API belgeleri:** Context7 uygun MCP/CLI bağlantısı olmadan çalışmaz; MCP Registry yalnızca keşif altyapısıdır.

## Uygulama ilkeleri

1. Önce [beceri değerlendirme iş akışını](../playbooks/skill-evaluation.md) uygulayın.
2. Tekil `SKILL.md` ve destekleyici dosyaların yolunu, lisansını ve bağımlılıklarını doğrulayın.
3. Kaynağı görevle ilişkilendirin; kopyalama/kurulum kararını ayrıca verin.
4. İşlem gerektiren becerileri, sadece izin verilmiş ve doğrulanmış çalışma ortamında çalıştırın.
5. Bu depo otomatik kurulum manifesti değildir.

> `openai/skills` ve `anthropics/skills` daha önce katalogda bulunduğundan yeniden eklenmemiştir. İlk beş kaynak 61 → 66, sonraki on beş kaynak 66 → 81 kayıt oluşturmuştur. **Hiçbir üçüncü taraf beceri veya ajan bu işlem sırasında otomatik kurulmamıştır.**
