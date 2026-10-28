# Türkçe görev yönlendiricisi (v5)

Bu klasör, `tools.json` içindeki **95 referans depodan** göreve uygun olanları seçen, yalnızca Python standart kütüphanesi kullanan küçük ve denetlenebilir bir katmandır. 17 görev alanı tanımlanmıştır. **Depo kurmaz, modele yeni yetenek yüklemez, ağ çağrısı yapmaz ve seçtiği kaynakları çalıştırmaz.**

## Nasıl çalıştırılır?

Depo kökünde Python 3 ile:

```bash
python3 routing/task_router.py "TÜBİTAK projem için görsel algı araştırması tasarlamak istiyorum"
python3 routing/task_router.py "Bir yazılımın yetkili tersine mühendislik incelemesini planla" --json
python3 routing/task_router.py "Tipografik okunabilirlik deneyi" --limit 5 --max-rules 3
```

Salt-okuma ortam görünürlük kontrolü için ayrıca:

```bash
python3 routing/task_router.py "Veri analizi ve istatistik" --probe
```

`--probe` yalnızca tanımlı Python modüllerinin bulunup bulunmadığını veya komutun `PATH` üzerinde görünüp görünmediğini kontrol eder. Bu **kurulu sürümü, bağlantıyı, yürütme yetkisini ya da aracın kullanılabilirliğini doğrulamaz**. Birçok masaüstü uygulama, beceri, web servisi ve MCP sunucusu için sonuç `unknown` olur.

Makine tarafından işlenecek çıktı için `--json` kullanılır. Her öneride `repo`, `url`, `execution_mode`, `recommended_by` ve açıkça `runtime_status: not-verified` alanları vardır.

## Karar mekanizması

1. Görev ifadesindeki Türkçe karakterler eşleştirilir; kelime başlangıcı ve çok sözcüklü tetikleyiciler aranır.
2. Eşleşen en fazla üç görev alanı puanlanır; her alandan sırayla seçilerek altı öneriye kadar listelenir.
3. `rules.json` içindeki görev bazlı doğrulama kontrolleri ve risk notları gösterilir.
4. Gerçek kullanımdan önce kaynak deponun durumu/lisansı, mevcut çalışma ortamı, yetki ve verinin niteliği **ayrıca** kontrol edilir.

Kurallar, `routing/rules.json` içindeki açık eşleştirmelerdir; istatistiksel bir sınıflandırıcı veya güncel öneri motoru değildir. Özellikle alan dışı, belirsiz ve eş anlamlı ifadelerde eşleşme kaçırabilir. Yanlış pozitifler de mümkündür; nihai karar insan denetimine dayanmalıdır.

## Test

```bash
python3 -m unittest discover -s routing/tests -v
```

Testler internet bağlantısı veya üçüncü taraf paket gerektirmez. Katalog kimlikleri, 95 benzersiz kayıt, Türkçe normalizasyon, iki alanın ortak eşleşmesi, JSON çıkışı ve `--probe` durum işaretlerinin dürüstlüğü kontrol edilir.

## ChatGPT içinde nasıl kullanılır?

GitHub'a yüklenen dosyalar **ChatGPT Web tarafından tüm konuşmalarda otomatik okunmaz**. `routing/CHATGPT_PROJECT_INSTRUCTIONS.md` metnini ilgili ChatGPT Project yönergelerine elle ekleyebilir ve `tools.json`, `rules.json`, `AGENTS.md` dosyalarını proje bağlamında erişilebilir kılabilirsiniz. Python çalıştırma olanağı olan yetkili bir ajan ortamında bu komut kullanılabilir; yalnızca ChatGPT Web bağlamında dosyalara bakılarak aynı öneri mantığı izlenebilir. İkinci durumda CLI testinin yapılmış olması, araçların o oturumda kullanılabilir olduğunu kanıtlamaz.

## Özellikle doğrulanması gerekenler

- Akademik alanlarda literatür kapsamı, DOI/künye, etik uygunluk, yöntem/ölçüm geçerliliği, yeniden üretilebilirlik.
- Görsel ve kültürel miras alanlarında telif/provenans, kişiye motif atfı, OCR hata oranı.
- Yazılımda yetkilendirme, bağımlılık, lisans, güvenlik, test ve veri gizliliği.

Tetikleyici örnekleri ve örnek görevlerin rota eşleşmeleri için [tetikleyici matrisi](TRIGGER_MATRIX.md) dosyasına bakın.
