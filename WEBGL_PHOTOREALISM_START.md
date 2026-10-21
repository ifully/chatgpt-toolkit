
# WebGL Photorealism — ChatGPT Toolkit

## Amaç
Mevcut Three.js mimarisini değiştirmeden, WebGL tabanlı
3B iç mekânların görsel gerçekçiliğini artırmak.

## Kaynak depolar
- mrdoob/three.js
- pmndrs/postprocessing
- 0beqz/realism-effects
- playcanvas/skills
- playcanvas/engine
- donmccurdy/glTF-Transform
- KhronosGroup/KTX-Software

## Korunacak özellikler
- Mimari geometri ve fiziksel ölçüler
- Kapı, pencere ve duvar koordinatları
- Sanat eserlerinin konum, ölçek ve dönüşleri
- Kamera kontrol mekanizmaları
- Mevcut editör ve veri kayıt yapısı

## Geliştirme sırası

### 1. Mevcut durumu denetle
Three.js sürümünü, render ayarlarını,
malzemeleri, ışıkları ve performansı incele.
Sabit kamera açılarından referans görüntüler kaydet.

### 2. PBR malzemeleri iyileştir
Yüzey türüne göre roughness, metalness,
normal map ve environment map ayarlarını düzenle.
Mevcut eser materyallerini izinsiz değiştirme.

### 3. Aydınlatma ve gölgeler
Ortam aydınlatması, yönlü ışık, spot ışıkları
ve temas gölgelerini düzenle.
Statik mimari için lightmap seçeneğini değerlendir.

### 4. Renk yönetimi
Linear-sRGB iş akışını doğrula.
sRGB çıktı, pozlama ve ton eşlemeyi kontrol et.
Çift renk dönüşümü ve çift ton eşlemeden kaçın.

### 5. Postprocessing
Uyumlu sürüm üzerinden kenar yumuşatma ve
gerekli görüntü efektlerini aşamalı uygula.
Efektleri ayrı ayrı açılıp kapatılabilir tasarla.

### 6. Deneysel gerçekçilik
SSGI ve SSR yalnızca ayrı test ortamında denenir.
Sürüm uyumu ve performans doğrulanmadan
üretim sistemine eklenmez.

### 7. GLB ve doku optimizasyonu
glTF-Transform ve KTX araçlarını değerlendir.
Geometri, UV, materyal ve görünüm bütünlüğünü koru.
Sıkıştırma öncesi ve sonrası karşılaştırma yap.

## Kabul kriterleri
- Mimari geometri değişmeyecek.
- Eser konumları ve ölçüleri korunacak.
- Önce/sonra görselleri aynı kamera açılarıyla alınacak.
- Masaüstü ve mobil performansı ölçülecek.
- Konsol hataları ve görsel bozulmalar kontrol edilecek.
- Değişiklikler geri alınabilir olacak.
- Yapılmayan testler başarıyla tamamlandı denmeyecek.

## ChatGPT görev protokolü
Bu dosyayı ve ilgili upstream depoları incele.
Önce mevcut uygulamanın kaynak kodunu denetle.
Kullanılabilecek kütüphanelerin sürümlerini doğrula.
Mimari veya editör davranışını değiştirmeden
fotogerçekçilik için aşamalı bir çözüm uygula.
Görsel karşılaştırma ve regresyon testlerini raporla.

## Sınırlar
Bu dosya bağımlılıkları otomatik kurmaz.
PlayCanvas Engine, Three.js eklentisi değildir.
Gerçek uygulama entegrasyonu için projenin
kaynak kodu ve çalıştırılabilir test ortamı gerekir.
