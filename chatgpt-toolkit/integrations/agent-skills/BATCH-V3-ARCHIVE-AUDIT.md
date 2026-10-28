# V3 — 15 beceri ve ajan deposunun arşiv denetimi

**İnceleme:** 28 Ekim 2026  
**Kaynak:** Kullanıcının sağladığı 15 ZIP arşivi  
**Kapsam:** Mevcut 66 katalog kaydı üzerine eklenen 15 farklı GitHub deposu; toplam 81 kayıt  
**Yöntem:** ZIP merkezi dizini, README/manifest ve kök lisans kontrolü, örnek `SKILL.md` yolu doğrulaması, SHA-256 ve her arşivde CRC/bütünlük testi. Arşiv içindeki hiçbir üçüncü taraf betik veya kurulum talimatı çalıştırılmadı.

## Arşiv / GitHub kaynağı / lisans eşleştirmesi

Arşivlerdeki `SKILL.md` sayıları **örnekler ve test verileri dahil ham dosya adetleridir**; benzersiz veya doğrudan kurulabilir beceri sayısı değildir.

| ZIP dosyası | Doğrulanan kaynak | Kök lisans bulgusu | `SKILL.md` | Bütünlük |
|---|---|---|---:|---|
| `Agent-Skills-for-Context-Engineering-main.zip` | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | MIT | 24 | Geçti |
| `skills-main(1).zip` | [getsentry/skills](https://github.com/getsentry/skills) | Apache-2.0 | 30 | Geçti |
| `superpowers-main.zip` | [obra/superpowers](https://github.com/obra/superpowers) | MIT | 15 | Geçti |
| `agents-main.zip` | [wshobson/agents](https://github.com/wshobson/agents) | MIT | 185 | Geçti |
| `skills-main (1).zip` | [huggingface/skills](https://github.com/huggingface/skills) | Apache-2.0 | 26 | Geçti |
| `awesome-copilot-main.zip` | [github/awesome-copilot](https://github.com/github/awesome-copilot) | MIT | 465 | Geçti |
| `skills-main (2).zip` | [remotion-dev/skills](https://github.com/remotion-dev/skills) | Kök lisans saptanamadı | 12 | Geçti |
| `skills-main (3).zip` | [NVIDIA/skills](https://github.com/NVIDIA/skills) | Apache-2.0 **ve** CC-BY-4.0 | 421 | Geçti |
| `awesome-ai-agent-skills-main.zip` | [seb1n/awesome-ai-agent-skills](https://github.com/seb1n/awesome-ai-agent-skills) | MIT | 103 | Geçti |
| `evals-main.zip` | [openai/evals](https://github.com/openai/evals) | MIT | 0 | Geçti |
| `promptfoo-main.zip` | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | MIT | 17 | Geçti |
| `context7-master.zip` | [upstash/context7](https://github.com/upstash/context7) | MIT | 10 | Geçti |
| `registry-main.zip` | [modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry) | MIT/Apache-2.0 geçişi; belgeler CC-BY-4.0 | 0 | Geçti |
| `deepagents-main.zip` | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | MIT | 26 | Geçti |
| `awesome-agent-skills-main.zip` | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | MIT | 0 | Geçti |

`skills-main(1).zip`, `skills-main (1).zip`, `skills-main (2).zip` ve `skills-main (3).zip` **farklı** kaynaklardır; aynı `skills-main/` iç klasör adına sahip olmalarına karşın README, manifest ve içeriklerden ayırt edilmişlerdir. ZIP dosyaları tek bir dizine açılmamış veya birbirinin üzerine yazılmamıştır.

## SHA-256 bütünlük kayıtları

| ZIP dosyası | SHA-256 |
|---|---|
| `Agent-Skills-for-Context-Engineering-main.zip` | `ad6496527143f85a682542aac67f6565785680d3146d967ac0e298f2c0cc7abe` |
| `skills-main(1).zip` | `194a4f72ccdad62ff050e62cf91085b2f21c71834c1deba3e4da935d9fed6fe7` |
| `superpowers-main.zip` | `d06a326ee189068b1aa0956452c259d39a66f5ff76ae9f0f7ece31710cbfe995` |
| `agents-main.zip` | `b5a307c07c5d08a43cf995339c47a4196aef4f09cf0e52d70d3073e91fdbc77a` |
| `skills-main (1).zip` | `2f16662b2e17157af0a5fe7090b100126ab715dab5294132dd3205e89397a049` |
| `awesome-copilot-main.zip` | `1aafab0e00dddd9d0dd50a4da0147c398087f6a4720d91f8d2430fd04ea39399` |
| `skills-main (2).zip` | `9fdbee0d8ef8a1de8e8edad409b243650d14ab991e2e8e7d724e164081ebc235` |
| `skills-main (3).zip` | `5e4826adeb46dda815430e4d2a3e4f4c26a85fb78487885ba80ec3cb117c1b08` |
| `awesome-ai-agent-skills-main.zip` | `fa5fc80fb854cb7e8ddfb2337a2da8a956e2433cf327001d20bc0401509b1510` |
| `evals-main.zip` | `5f1391939e3c257441da15a6c7ec175d0b2050e849152dafdb7632e9db93453c` |
| `promptfoo-main.zip` | `b0e257450341a9102df54cb8eea533cf524746145fe22df116dc717c3999960b` |
| `context7-master.zip` | `7cd9d2058f8c958be1891e67f4e0b7d7883287083303eee75445a0f0090746a1` |
| `registry-main.zip` | `656552511328546e6c2d2fdfc797de04939e535a59649e0616a45a438690096b` |
| `deepagents-main.zip` | `f904473dec81cfa3adf558ba1ce69fc2d896ee135bcee4f7282faf194b955b5d` |
| `awesome-agent-skills-main.zip` | `94ff4e8260ab71b60673126c699646d5035a275af593cab2f100d5c953460f33` |

## İşlevsel sınıflandırma ve risk notları

- **Doğrudan beceri kaynakları:** Context Engineering, Sentry, Superpowers, wshobson, Hugging Face, Awesome Copilot, Remotion, NVIDIA, seb1n ve Context7. İlgili becerilerin seçilmiş gerçek dosya yolları [catalog.yaml](catalog.yaml) içindedir.
- **Beceri içeren daha geniş altyapılar:** Promptfoo ve Deep Agents, ilgili örnek `SKILL.md` dosyalarını içerir; temel işlevleri ayrı ürün/ajan altyapısıdır.
- **Beceri olmayan araç ve dizinler:** OpenAI Evals değerlendirme yazılımıdır; MCP Registry keşif/kayıt altyapısıdır; VoltAgent Awesome Agent Skills dış depolara bağlantı dizinidir. Bu üçünde `SKILL.md` bulunmadı.
- **Lisans belirsizliği:** Remotion Skills arşivinde kök lisans saptanamadı. Bu ZIP'in içeriği bu pakete kopyalanmadı ve herhangi bir yeniden dağıtım hakkı varsayılmadı.
- **Karma lisanslar:** NVIDIA lisans dosyaları kod ve içerik için farklı koşullar içerir. MCP Registry lisans metni MIT katkıları, Apache-2.0 ve belge lisansı arasında geçiş açıklaması yapar.
- **Yönerge güvenliği:** Superpowers `using-superpowers` becerisi konuşmadaki tüm eylemlere uygulanacak katı üst kurallar önerir. Bu metin değerlendirme verisi olarak incelenmiş, çalışma kurallarına eklenmemiştir.
- **Çakışma:** Remotion Skills, önceki `haidrrrry/claude-remotion-skill` ile konu olarak örtüşür. Her iki kaynak ayrı katalog girdisidir; otomatik birleşim yapılmadı.

## Sınırlar

1. Bütünlük testi dosya bozulmalarını belirler; kötü amaçlı veya hatalı kodu dışlamaz.
2. Kaynak ZIP'lerinde Git commit kimliği sabitlenmiş bir manifest yoktur. Buradaki SHA-256 **ZIP arşivine** aittir; kaynak commit kimliği değildir.
3. Üçüncü taraf kod, medya, örnek komut ve kurulum betikleri yeniden paketlenmemiştir.
4. Kataloglama ChatGPT'ye otomatik beceri yüklemez; model ağırlıklarını değiştirmez.
5. Gerçek kurulum istenirse [beceri değerlendirme protokolü](../../playbooks/skill-evaluation.md) ve [kalite döngüsü](../../playbooks/agent-skill-quality-loop.md) uygulanmalıdır.
