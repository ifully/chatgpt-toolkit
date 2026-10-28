# Yapay zekâ ajanları ve bilgi erişimi

Bu sayfadaki depolar birer öneri ve kaynak bağlantısıdır; ChatGPT Web içinde otomatik yüklenmiş sayılmazlar.

| Öncelik | Kaynak | Kullanım | Çalıştırma biçimi |
|---|---|---|---|
| 1 | [codex](https://github.com/openai/codex) | Terminal tabanlı kodlama ajanı; ayrı çalışma ortamı gerekir. | `external-agent` |
| 1 | [openai-agents-python](https://github.com/openai/openai-agents-python) | Araç kullanan, görev devreden ajan uygulamaları geliştirme. | `python-package` |
| 1 | [servers](https://github.com/modelcontextprotocol/servers) | MCP sunucu uygulamaları; uygun istemci ve bağlantı gerekir. | `mcp-server` |
| 1 | [skills](https://github.com/openai/skills) | Codex görev becerileri; uyumlu istemci ve yürütme ortamı gerekir. | `reference` |
| 1 | [skills](https://github.com/anthropics/skills) | Agent Skills örnekleri ve yönergeleri; dosya bazlı lisansı doğrula. | `reference` |
| 2 | [browser-use](https://github.com/browser-use/browser-use) | Tarayıcı ile etkileşen ajanlar; tarayıcı ve servis yapılandırması gerekir. | `browser-runtime` |
| 2 | [gpt-researcher](https://github.com/assafelovic/gpt-researcher) | Web kaynakları üzerinden otomatik araştırma iş akışları. | `external-agent` |
| 2 | [langgraph](https://github.com/langchain-ai/langgraph) | Durum tutan, çok aşamalı ajan iş akışları. | `python-package` |
| 2 | [llama_index](https://github.com/run-llama/llama_index) | Belge erişimi ve RAG veri akışları. | `python-package` |
| 2 | [ollama](https://github.com/ollama/ollama) | Modelleri lokal veya uzak makinede çalıştırma. | `external-service` |
| 2 | [OpenHands](https://github.com/OpenHands/OpenHands) | Kod geliştirme ajanı; servis veya çalışma ortamı gerektirir. | `external-agent` |
| 2 | [qdrant](https://github.com/qdrant/qdrant) | Vektör arama veritabanı; servis gerekir. | `external-service` |
| 2 | [storm](https://github.com/stanford-oval/storm) | Kaynaklara dayalı taslak araştırma sistemi; doğrulama gerekir. | `external-agent` |
| 2 | [transformers](https://github.com/huggingface/transformers) | Dil, görüntü ve çok kipli model uygulamaları. | `python-package` |
| 1 | [context-engineering-agent-skills](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | Bağlam, bellek ve ölçülebilir iyileştirme becerileri. | `reference` |
| 1 | [awesome-copilot](https://github.com/github/awesome-copilot) | Farklı alanlara yönelik ajan beceri koleksiyonu; seçici değerlendirme gerekir. | `reference` |
| 1 | [openai-evals](https://github.com/openai/evals) | Yapay zekâ/ajan çıktılarının test edilmesi. | `python-package` |
| 2 | [wshobson-agents](https://github.com/wshobson/agents) | Çok sayıda uzman ajan ve beceri; tek tek denetleme. | `reference` |
| 2 | [seb1n-agent-skills](https://github.com/seb1n/awesome-ai-agent-skills) | Ajan güvenliği, değerlendirme ve UI tasarım becerileri. | `reference` |
| 2 | [deepagents](https://github.com/langchain-ai/deepagents) | Uzun görevlerde durum, bellek ve alt-ajan iş akışları. | `python-package` |
| 2 | [rd-agent](https://github.com/microsoft/RD-Agent) | Veri odaklı araştırmada fikir ve model deneme döngüleri; ayrı ajan. | `external-agent` |
| 3 | [nvidia-skills](https://github.com/NVIDIA/skills) | NVIDIA ürünlerine ilişkin özel beceriler; karma lisans. | `reference` |
| 3 | [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | Bağımsız beceri depolarını keşfetme dizini. | `reference` |

## Uygulama ölçütü

Araç seçerken güncel lisans, sürüm, bağımlılık, platform uyumu ve erişim yetkisini teyit edin. `tools.yaml` dosyasındaki yürütme sınıfları, kurulumun gerçekleştiğini göstermez.

## Görev istemi

> `Yapay zekâ ajanları ve bilgi erişimi alanındaki bir görev için bu kategorideki adayları karşılaştır; mevcut çalışma ortamında kullanılabilenleri doğrula; kaynak ve sınırlılıkları bildir.`
