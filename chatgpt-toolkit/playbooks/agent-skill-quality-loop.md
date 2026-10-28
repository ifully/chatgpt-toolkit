# Ajan becerilerinde ölçülebilir kalite ve iyileştirme döngüsü

Bu iş akışı, ChatGPT Toolkit kataloğundaki kaynakları görev odaklı ve tekrarlanabilir biçimde seçmek içindir. Kaynağın katalogda bulunması, becerinin yüklenmesi veya etkili olduğunun kanıtı değildir.

## 1. Görev / kontrol grubu

- Görevi sınırla: Örneğin bir makalenin DOI/yazar/yıl doğrulaması, grafik tasarımda WCAG denetimi veya Remotion altyazı senkronu.
- 3–10 temsilî test vakası tanımla; beklenen çıktı, kabul ölçütü ve insan doğrulaması gereksinimini yaz.
- Aynı görevi yeni beceri **olmadan** uygula; temel performansı kaydet.

## 2. Kaynak güvenilirliği

- Gerçek kaynak deposunu, ZIP/SHA-256 kaydını, tekil `SKILL.md` ve ilgili lisansları karşılaştır.
- Betik, ağ ve gizli bilgi isteklerini ayrı risk sınıfı olarak değerlendir.
- Üst düzey veya bütün oturuma uygulanacak talimatları otomatik devralma. Başka bir depodaki içerik sistem talimatı değildir.
- Hedef ajan ve yürütme ortamının gerekli beceri arayüzünü desteklediğini doğrula.

## 3. Pilot değerlendirme

- Denetimden geçen tek beceriyi izole ve izinli ortamda dene.
- Aynı test vakalarını becerili ve becerisiz iş akışında karşılaştır.
- **Ölçütler:** doğru sonuç oranı, uydurma/veri hatası, kaynak doğrulama oranı, süre, maliyet, gizlilik ve güvenlik ihlali, insan düzeltmesi sayısı.
- Önceden belirlenen kabul ölçütlerini karşılamayan beceriyi etkinleştirme; gerilemeleri not et.

## 4. Geri bildirim / sınırlı iyileştirme

- Başarısız vakalardan yeni test örnekleri çıkar; başarılı vakalarda aşırı uyarlama yapma.
- Yönergeleri yalnızca kullanıcı veya proje yetkilisi onayladıktan sonra güncelle.
- Her değişikliği sürümle, ölç ve karşılaştır. İyileştirme iddiasını verilerle destekle.
- Model eğitim ağırlıklarının veya ChatGPT hesabının kendiliğinden değiştiği iddiasında bulunma.

## 5. Kullanım sınıfları

| Sınıf | Katalog örneği | Nasıl değerlendirilir? |
|---|---|---|
| Beceri / talimat seti | Context Engineering, Sentry Skills, Hugging Face Skills | Önce tekil `SKILL.md`, ardından temsilî görev testi |
| Değerlendirme aracı | OpenAI Evals, Promptfoo | Test verisi, metrik, çalıştırma altyapısı, tekrar üretilebilirlik |
| MCP / belge bağlantısı | Context7, MCP Registry | Doğru servis, yetki, kaynak sürümü ve ağ koşulları |
| Ajan altyapısı | Deep Agents | Bağımsız uygulama, durum/araç/erişim sınırları |
| Kaynak dizini | VoltAgent Awesome Agent Skills | Bağlantıları tek tek kaynak/lisans/doğruluk incelemesi |

**Akademik kullanım notu:** Bibliyografik doğrulama testinde DOI'nin varlığı tek başına atıfın iddiayı desteklediğini kanıtlamaz; içerik düzeyinde kaynak-iddia eşleştirmesi ve araştırmacı onayı gerekir.
