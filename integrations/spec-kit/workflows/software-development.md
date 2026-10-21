# Yazılım iş akışı — Spec Kit ilkelerine uyarlama

Bu belge, [GitHub Spec Kit](https://github.com/github/spec-kit/blob/main/docs/quickstart.md) SDD aşamalarını **ChatGPT Web'e manuel olarak** uyarlar. Otomatik `/speckit-*` komutları çalışmaz.

## Sıra ve çıktılar

| Aşama | Amaç | Kayıt |
|---|---|---|
| Constitution | Kısıtları, değişmezleri ve proje ilkelerini tanımla | `constitution.md` |
| Specify | Kullanıcı ihtiyacını ve doğrulanabilir kabul ölçütlerini belirle | `spec.md` |
| Clarify | Belirsizleri hedefli sorularla gider | `clarifications.md` |
| Plan | Mimari, veri modeli, risk, güvenlik ve test yaklaşımını açıkla | `plan.md` |
| Checklist | Gereksinimleri kalite kontrolünden geçir | `requirements-checklist.md` |
| Tasks | Bağımlılıklara göre küçük uygulama işleri oluştur | `tasks.md` |
| Analyze | Anlaşmazlık ve eksiklikleri çapraz incele | `analysis.md` |
| Implement | Yetkili ortamda kodu kontrollü değiştir | Kod/diff + test çıktısı |
| Verify / Converge | Kabul ve regresyon testlerini doğrula, açık işleri kaydet | `validation.md` |

## Gereksinim kalitesi

- Gereksinimler kullanıcı açısından gözlenebilir olmalıdır.
- Ölçülebilir **kabul koşulları** her ana özellik için tanımlanmalıdır.
- Mevcut projede korunacak davranışlar ve veri yapıları ayrı kaydedilmelidir.
- Teknoloji tercihi (`plan.md`) kullanım ihtiyacını (`spec.md`) geriye dönük yeniden tanımlamamalıdır.
- Kapsam dışı talepler açıkça işaretlenmelidir.

## Mevcut proje özel ilkeleri

1. Ekteki kaynakları incelemeden mevcut mimari hakkında kesin hüküm verme.
2. Yeni geliştirmeyi küçük bir değişiklik olarak ayır; çalışan özellikleri koru.
3. Dosya/dizin etkisi, geriye uyumluluk, erişim ve veri kaybı risklerini değerlendir.
4. Mevcut testleri çalıştır; yoksa uygun regresyon testleri tasarla.
5. Uygulama sonunda hangi testlerin gerçekten çalıştırıldığı ve hangi kontrollerin yalnızca önerildiği açıklansın.

## Kullanım

Şablonlar: `../templates/constitution.md`, `spec.md`, `plan.md`, `tasks.md`, `validation.md`.
