# Üçüncü taraf kaynaklar / lisans ve yeniden kullanım

Bu repo **yeni yazılmış beceri dosyaları** ve örnek araçlardan oluşur. Aşağıdaki üçüncü taraf kütüphaneler `package.json` üzerinden npm bağımlılığı olarak çağrılır; yüklenen upstream kaynak klasörleri bu pakete gömülmemiştir.

| Yüklenen arşiv | Upstream proje | Arşivdeki sürüm | Kaynak lisansı | Entegrasyon |
|---|---|---|---|---|
| `svg.js-master.zip` | https://github.com/svgdotjs/svg.js | 3.2.8 | MIT (`LICENSE.txt`) | `@svgdotjs/svg.js` bağımlılığı |
| `paper.js-develop.zip` | https://github.com/paperjs/paper.js | 0.16.0 | MIT (`LICENSE.txt`) | `paper` bağımlılığı |
| `PptxGenJS-master.zip` | https://github.com/gitbrent/PptxGenJS | 4.0.1 | MIT (`LICENSE`) | `pptxgenjs` bağımlılığı |
| `mjml-master.zip` | https://github.com/mjmlio/mjml | 5.4.1 (packages/mjml) | MIT (`LICENSE.md`) | `mjml` bağımlılığı |
| `slidev-main.zip` | https://github.com/slidevjs/slidev | 53.0.0 | MIT (`LICENSE`) | `@slidev/cli` bağımlılığı |
| `plugins-main.zip` | https://github.com/openai/plugins | n/a | **Karma lisanslar**: bazı eklentiler proprietary / özel şartlı; tek bir MIT lisanslı paket değil | Yalnızca `.codex-plugin` / marketplace mimari örneği olarak incelendi; içerik kopyalanmadı |

**Uyarı:** Buradaki sürümler kullanıcının yüklediği ZIP içeriğinden alınmıştır; npm registry'de yayınlanma durumu ve güncel sürüm uygunluğu çevrimiçi olarak ayrıca doğrulanmalıdır. Herhangi bir kütüphaneyi kaynak kodu olarak dağıtmaya karar verilirse ilgili lisans metnini ve hak bildirimlerini koruyun. Paket MIT lisansı yalnızca bizim yazdığımız entegrasyon kodu ve metinleri kapsar; upstream paketlerin lisansını değiştirmez.
