# PyAlex — Kullanım modelleri

**Kaynak:** https://github.com/J535D165/pyalex  
**Kaynak taraması:** Kullanıcı tarafından yüklenen `pyalex-main.zip` paketindeki README, `pyproject.toml` ve API kodu incelenmiştir (21.10.2026).  
**Lisans:** PyAlex MIT; veri lisansları ve tam metin hakları ayrı değerlendirilir.

PyAlex, OpenAlex API'si için Python istemcisidir. OpenAlex'ten yayın (`Works`), yazar, kaynak, kurum, konu ve ilişkili bibliyografik metadata elde etmeyi sağlar.

| Senaryo | Mümkün olan | Koşul |
|---|---|---|
| ChatGPT Web / doküman rehberi | Sorgu stratejisi, dahil etme/dışlama ölçütleri, kaynak denetimi, CSV yorumlama | Bu depodaki dosyalara erişim |
| ChatGPT kod çalışma ortamında PyAlex | Python betiğinin çalıştırılması | `pyalex` paketi, OpenAlex API anahtarı ve internet erişimi olmalı |
| Yerel/bulut Python | Gerçek OpenAlex sorgusu; CSV ve arama günlüğü üretimi | Ağ erişimi, kurulum, API anahtarı |
| Salt GitHub | Protokol, kod ve belgeleri okumak | Araç otomatik çalışmaz |

## API anahtarı

PyAlex README'si, 13 Şubat 2026'dan beri düzenli OpenAlex kullanımı için API anahtarına ihtiyaç bulunduğunu bildiriyor. Güncel kota/ücret kurallarını [OpenAlex belgelerinden](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication) yeniden kontrol edin.

1. OpenAlex üzerinde hesap ve API anahtarı edinin: https://openalex.org/settings/api
2. API anahtarını **GitHub'a eklemeyin** ve sohbet mesajında paylaşmayın.
3. Sadece çalıştırma ortamında `OPENALEX_API_KEY` ortam değişkeni olarak kullanın.
4. Güvenilir ayrı bir Python ortamında `python -m pip install pyalex` ile kurulum yapılabilir.

Örnek komut:

```bash
python integrations/pyalex/scripts/search_openalex.py --query "visual communication design" --from-year 2020 --to-year 2026 --max-records 50 --output results.csv
```

Önce, erişim olmadan parametre doğrulama:

```bash
python integrations/pyalex/scripts/search_openalex.py --query "visual communication design" --dry-run
```

**Not:** Bu kod canlı sorgu için sunulmuştur; mevcut ChatGPT ortamında API erişimi/doğrulama yapılmış olduğu iddia edilmez. Sonuçların bilimsel uygunluğu insan denetimi gerektirir.
