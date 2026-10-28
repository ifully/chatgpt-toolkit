# Üçüncü taraf Agent Skill değerlendirme protokolü

Bu protokol, bir `SKILL.md` becerisini **kullanmadan veya kaynak kodunu taşımadan önce** uygulanır.

## 1. Kaynak ve kimlik doğrulaması

- [ ] Kaynak repo ve resmi README bağlantısı doğrulandı.
- [ ] Doğrudan `SKILL.md` yolu ve varsa `references/`, `scripts/`, `assets/` belirlendi.
- [ ] Son commit veya release sabitlendi; kaynak revizyonu kaydedildi.
- [ ] Mevcut katalogda yinelenen işlevler kontrol edildi.

## 2. Lisans ve haklar

- [ ] Kök lisansın yanı sıra tekil beceri ve bağlı veri lisansı incelendi.
- [ ] Kod, doküman, örnek varlık ve üçüncü taraf font/görsel lisansları ayrıştırıldı.
- [ ] Gerekli atıf ve ShareAlike hükümleri kaydedildi.
- [ ] Belirsizlik varsa yalnızca bağlantı verildi; dosya kopyalanmadı.

## 3. Güvenlik ve gizlilik

- [ ] `SKILL.md` içindeki `curl | sh`, uzak kurulum, silme ve yetki yükseltme yönergeleri işaretlendi.
- [ ] Ağ bağlantıları, dış API'ler ve veri çıkış hedefleri kaydedildi.
- [ ] Erişim anahtarı, kimlik bilgisi, özel proje verisi ve telifli içerik akışı değerlendirildi.
- [ ] Betikler izole deneme ortamında ve asgari yetkiyle test edilmeden çalıştırılmadı.
- [ ] Haricî talimatların (web sayfası, depodaki metin) ajan yetki ve güvenlik kurallarını geçersiz kılamayacağı teyit edildi.

## 4. Uyum ve kalite

- [ ] Hedef çalışma ortamının beceri yükleme mekanizması resmen destekleniyor.
- [ ] Gerekli CLI, Python, Node.js, tarayıcı veya masaüstü uygulaması gerçekten kullanılabiliyor.
- [ ] 2–3 temsilî görevde çıktı doğruluğu, hata durumları ve tekrar üretilebilirlik test edildi.
- [ ] Sonuçlar `kuruldu`, `yalnızca referans`, `lisans belirsiz`, `test edilmedi` olarak açıkça ayrıldı.

**Geçiş kuralı:** Bütünlük kontrolü, README varlığı veya GitHub yıldız sayısı tek başına kabul için yeterli değildir. Bir beceri ancak lisans/bağımlılık/güvenlik incelemesi ve hedef ortam testinden sonra "kurulabilir" veya "çalışıyor" olarak raporlanabilir.

## 5. Ölçülebilir iyileştirme kapısı

- [ ] Temsilî görevler, başarı ölçütleri ve mevcut becerisiz/önceki sürüm sonucu kaydedildi.
- [ ] Test girdileri ile gerçek kullanıcı/veri gizliliği ayrıştırıldı.
- [ ] Yeni becerinin çıktısı, aynı koşullarda önceki sürümle karşılaştırıldı.
- [ ] Hata ve güvenlik gerilemeleri kaydedildi; başarısız değişiklik etkinleştirilmedi.
- [ ] İnsan onayı sonrası uygun ajan ortamında kontrollü kurulum kararı verildi.

Örnek değerlendirme metodolojisi: [agent-skill-quality-loop.md](agent-skill-quality-loop.md). Büyük bir beceri koleksiyonundaki `SKILL.md` dosyası sayısı, kalite veya o dosyaların bağımsız çalışabilirliği anlamına gelmez.
