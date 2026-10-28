# Görev → öneri alanı → doğrulama matrisi

| Görev örneği | Kural kimliği | Öncelikle değerlendirilen kaynaklar | Çıktı denetimi |
|---|---|---|---|
| “TÜBİTAK için bilimsel proje fikri ve hipotez” | `research-ideation` | AutoRA, OpenScholar | Özgünlük, yöntem ve kaynak doğruluğu |
| “Göstergebilim konusunda sistematik literatür taraması” | `literature-citations` | OpenScholar, scientific-agent-skills | DOI, tam metin, arama stratejisi |
| “Q1 makalemin yayın öncesi kontrolü” | `academic-writing` | scientific-agent-skills, Zotero | İddia/kanıt, hedef dergi kuralları |
| “Tipografik okunabilirlik deneyi” | `behavioral-experiment` + `graphic-design` | PsychoPy, fonttools | Uyaran ve etik; okunabilirlik ölçümü |
| “Afişlerde tematik ve göstergebilimsel analiz” | `qualitative-research` + `graphic-design` | scientific-agent-skills, OpenScholar | Kodlama gerekçesi, özgün belgeler |
| “Atıf ağı ve bibliyometrik harita” | `bibliometrics` | Gephi, Zotero | Veri tabanı kapsamı, ağ eşikleri |
| “Araştırmanın ön kaydı ve veri sürümleme” | `reproducibility` | DVC, Snakemake | Tekrarlanabilirlik ve izinler |
| “Eski afiş arşivinde OCR ve motif incelemesi” | `visual-archive` | PaddleOCR, VTracer | Görsel doğrulama, provenans |
| “Logo ve tipografik kimlik sistemi” | `graphic-design` | ui-ux-pro-max-skill, fonttools | Lisans, kontrast, hiyerarşi |
| “Remotion ile kinetik tipografi” | `motion-design` | remotion-dev/skills, claude-remotion-skill | Render ayarları ve telif |
| “3B obje tarama ve GLB dosyası” | `three-d` | COLMAP, Blender | Ölçek, geometri, glTF doğrulama |
| “Web sitemde WCAG testi” | `web-accessibility` | Playwright, Lighthouse, axe-core | Erişilebilirlik ve elle doğrulama |
| “Yetkili firmware tersine mühendislik analizi” | `reverse-engineering` | Ghidra, angr, Rizin | Yetki, izolasyon, kanıt kaydı |
| “Veri setinde regresyon ve görselleştirme” | `data-analysis` | pandas, polars, DuckDB | Varsayım, etki büyüklüğü |
| “Kodda gizli anahtar ve güvenlik açığı” | `security-quality` | Semgrep, Gitleaks, Trivy | Yanlış pozitif, yetki, gizlilik |
| “Ajan becerisini değerlendir ve iyileştir” | `agent-evaluation` | Context Engineering, OpenAI evals | Öncesi/sonrası ölçüt ve test |
| “MCP ile tekrarlanan iş akışı” | `automation-mcp` | n8n, Activepieces, MCP Registry | Kimlik bilgisi, hata yönetimi |

Buradaki kaynak sırası **uygunluk adayı** anlamına gelir. Kurulu olma, ücretsiz kullanım, güncel sürüm veya hizmete bağlılık garantisi yoktur. Doğal dil yönlendirmesi anahtar sözcük temellidir; birden fazla alan eşleşebilir.
