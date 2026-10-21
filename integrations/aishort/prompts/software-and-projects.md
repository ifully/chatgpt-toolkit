# Yazılım ve analiz projeleri

Aşağıdaki istemler `prompts.json` içindeki aynı kimliklerin okunabilir sürümüdür.

## SW-01 — Yazılım özellik spesifikasyonu

**Gerekli bilgiler:** Mevcut proje ve mimari, İstenen özellik, Korunacak işlevler, Dağıtım koşulları

**İstem:**

> Mevcut kod tabanındaki mimariyi ve kullanıcının korunmasını istediği kararları tespit etmeden yeni mimari varsayma. İstenen özelliği kullanıcı öykülerine, işlevsel ve işlevsel olmayan gereksinimlere, kabul ölçütlerine ve geri alma stratejisine ayır. Her kabul ölçütü için test tanımla. Değişiklikleri küçük ve bağımsız tut, geriye dönük uyumluluk ve veri taşıma risklerini ayrı raporla. Kod incelemeden uygulanmış veya test edilmiş gibi sunma.

**Kontrol:** Mevcut davranış korunuyor; Kabul ölçütleri test edilebilir; Rollback tanımlı

## SW-02 — Kod ve güvenlik incelemesi

**Gerekli bilgiler:** Depo URL veya ZIP, Çalıştırılabilir test ortamı (varsa), Kullanıcı hedefi

**İstem:**

> Sağlanan kaynak kodunu güvenlik, bakım maliyeti, veri doğrulama, kimlik doğrulama/yetkilendirme, üçüncü taraf bağımlılıklar, erişilebilirlik ve performans açısından incele. Bulguları dosya yolu ve mümkünse satır referansı ile sınıflandır. Doğrulanmamış açıkları kesin açık gibi sunma. Statik analiz ile dinamik test sonuçlarını ayır. En küçük güvenli düzeltme, olası yan etkiler ve tekrar testi öner. Sırları ve kişisel veriyi rapora kopyalama.

**Kontrol:** Her bulgu kaynağa bağlı; Test edilen/edilmeyen ayrılmış; Hassas veriler korunmuş

## SW-03 — Araştırma veri analizi planı

**Gerekli bilgiler:** Veri sözlüğü, Araştırma sorusu, Örneklem ve toplama süreci, Eksik veriler

**İstem:**

> Verinin gözlemsel/deneysel yapısı, değişken düzeyleri, dağılım varsayımları, eksik veri mekanizması, olası karıştırıcılar ve örneklem kısıtları üzerinden analiz planı hazırla. Temizleme adımlarını ham veriden ayrıştır; tekrar üretilebilir kod, sürüm notu ve çıktı kontrolü öner. p değeri ile etki büyüklüğünü birbirine indirgeme. Veri verilmemişse istatistik, tablo veya grafik icat etme.

**Kontrol:** Yöntem varsayımları raporlu; Analiz tekrarlanabilir; Uydurma istatistik yok
