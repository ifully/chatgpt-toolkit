# Yazılım deposu teknik incelemesi

**Önkoşul:** araçların kurulu olması veya erişim yetkisi varsayılmaz.

1. İş hedefini ve depo erişim/yazma yetkilerini doğrula.
2. Depoyu güncel kaynak ve bağımlılık dosyalarından incele; lisans ve sürüm uyumunu belirle.
3. Testleri ve statik denetimleri ancak mevcut çalışma ortamı izin veriyorsa çalıştır.
4. Güvenlik, veri sızıntısı, geriye dönük uyum, performans ve erişilebilirlik risklerini ayır.
5. Kod değişikliği gerekiyorsa en küçük geri alınabilir farkı oluştur; test et.
6. Değişmeyen dosyaları ve doğrulanamayan varsayımları açıkça belirt.

**Çıktı standardı:** doğrulanan işlemler, üretilen artefaktlar, kaynaklar, kullanılan sürümler (biliniyorsa), test sonuçları, açık sınırlılıklar.
