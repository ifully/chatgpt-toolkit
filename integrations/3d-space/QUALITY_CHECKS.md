# 3B mekân kalite denetim listesi

1. **Birim ve ölçek:** Kaynak JSON santimetredir; çıktı metre. Örnek mekân 1000×700×320 cm, GLB'de duvar dış kalınlığı hesaba katılmadan 10×7×3.2 m'dir.
2. **Geometri:** Duvardan duvara bağlantılar ve kapalı döngüler; sıfır uzunluklu duvar bulunmamalı.
3. **Kapı/pencere:** Her açıklık var olan duvara bağlı; genişlik duvar uzunluğuna sığmalı; z alt ve üst sınırları duvar içinde olmalı; bindirmeler engellenmeli.
4. **Zemin:** Yaklaşık duvar merkez çizgisi çokgeni zeminle eşleşir. Gerçek döşeme detayı/bitişi üretim için ilave mimari model gerekir.
5. **Mekânsal doğruluk:** Sol/sağ veya +Y/−Y dönüşümü kontrol edilmeli (OpenPlan3D'de 2B y ekranda aşağı, GLB'de dünyasal y yukarı).
6. **Malzemeler:** Mevcut dönüştürücü yalnızca basit vertex colour üretir; pürüzlülük, metaliklik, normal map ve fiziksel ışık çözümü iddiası yoktur.
7. **Uyumluluk:** GLB dosyası 3B görüntüleyicide açılmalı; geometri ölçüleri audit ile karşılaştırılmalı.
8. **Dosya boyutu:** Önce gerçek asset dağılımını hesaplayın; optimum boyut kalite, doku atlasları ve hedef cihaza göre belirlensin.
9. **Güvenlik:** Yetkisiz dış model indirmeyin; telifli eserleri kullanıcı izni olmadan sahneye katmayın.
10. **Teslim:** Düzenlenebilir JSON, GLB, audit raporu ve varsa gösterim HTML'ini ayrı sağlayın.

Test komutu: `python -m unittest discover -s integrations/3d-space/tests -v`.
