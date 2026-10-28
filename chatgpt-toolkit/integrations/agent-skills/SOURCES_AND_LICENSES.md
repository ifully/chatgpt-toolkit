# Kaynak arşivleri, bütünlük ve lisans — v2 ve v3

Yeni sağlanan **15 arşivlik v3 paketi** için ayrıntılı SHA-256, kök lisans ve `SKILL.md` envanteri: [BATCH-V3-ARCHIVE-AUDIT.md](BATCH-V3-ARCHIVE-AUDIT.md). Aşağıdaki tablo, daha önce işlenen **ilk beş** ZIP'e aittir.

**Denetim:** 28 Ekim 2026. Aşağıdaki özet ilk beş ZIP dosyasına dayanır. Beş arşiv de `unzip -tq` bütünlük testini hatasız geçti. Testin başarısı içerikteki kodun güvenli olduğunu kanıtlamaz.

| Dosya | SHA-256 | ZIP içindeki lisans bulgusu |
|---|---|---|
| `agent-skills-main.zip` | `da67f2f7ded3cb7f746ea3fa70ad7f8aed37d1c5ab36972df7a3d72296194e9d` | Kök `LICENSE`/`LICENCE` bulunamadı; yeniden dağıtım için doğrulama gerekli |
| `claude-remotion-skill-main.zip` | `99a88e5d45ddeb12178ae97dc80e836e3a63167ac59dfb9166b90ce0cced356e` | Kök `LICENSE`: MIT |
| `skills-main.zip` | `1142f59c92084f7147fda173ffc915424e92ff990fd19f49f06519ae552c77d9` | Kök `LICENSE`: Creative Commons Attribution-ShareAlike 4.0 International |
| `ui-ux-pro-max-skill-main.zip` | `45ea8b8b8ebbdf01bb1fb12b31307dcc767aa16310ef750cd9f09443f58f2b9c` | Kök `LICENSE`: MIT |
| `scientific-agent-skills-main.zip` | `b8b7b4b44e0a7a536a5a969344cc229b8af9028bec2a64ead2c8e98e30fce1be` | Kök `LICENSE.md`: MIT; tekil becerilerde lisans alanları da bulunuyor |

## Lisans ve yeniden kullanım kararı

1. **UI/UX Pro Max:** Kaynak açıkça MIT lisansı taşımaktadır. Yeniden paketleme imkânı lisans koşullarına ve üçüncü taraf verilerin haklarına bağlıdır. Bu yükleme paketine yalnızca referans eklendi.
2. **Vercel Agent Skills:** Sağlanan arşivde kök lisans dosyası bulunamadı. Bu durum kullanımın yasak olduğunu tek başına göstermez; ancak yeniden dağıtım hakkını da doğrulamaz. **Kod kopyalanmadı.**
3. **Claude Remotion Skill:** Kaynak kök dizininde MIT lisansı bulunmaktadır. Örnek video, GIF, React kodu veya beceri betikleri bu pakete alınmadı.
4. **Trail of Bits Skills:** Creative Commons Attribution-ShareAlike 4.0 International koşulları nedeniyle kaynak içerik kopyalanmadan referans verildi. Gelecekte uyarlama yapılırsa atıf ve aynı lisans paylaşım koşulları ayrı incelenmeli.
5. **K-Dense Scientific Agent Skills:** Kök MIT lisansı ve incelenen akademik becerilerin kendi `license` alanları bulunuyor. Büyük araştırma arşivindeki betik, veri veya üçüncü taraf medya paketlenmedi. Özellikle `peer-review` becerisinin gizlilik/dergi politikası sınırları ve `literature-review` becerisinin dış kaynak/araç bağımlılıkları kaydedildi.

## Sınırlar

- Arşivler açılıp çalıştırılmadı; ZIP listeleme, metin okuma ve bütünlük denetimleri yapıldı.
- Yalnızca beş ana depo kataloglandı; `skills-main.zip` gibi genel adlar, README içeriği üzerinden kaynakla eşleştirildi.
- GitHub'da güncel bir sürüm, yüklenen ZIP ile farklı olabilir. Gerçek kuruluma geçmeden önce commit kimliği, lisans ve bağımlılıklar yeniden doğrulanmalı.
- Katalog hiçbir kimlik bilgisi, kişisel veri, gömülü upstream betik veya telifli medya içermez.
