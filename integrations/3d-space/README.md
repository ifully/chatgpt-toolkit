# 3B mekân üretimi — Kurulum ve çalışma

## Temel yaklaşım

1. **Mekân şeması**: Kullanıcıdan veya mevcut dosyadan en, boy, kat yüksekliği, duvar kalınlığı, duvar uç noktaları, kapı/pencere yerleri, malzemeler ve isteğe bağlı mobilya/eser yerleşimi elde et.
2. **Düzenlenebilir plan**: openPlan3D'nin *web project JSON* şemasında (santimetre, 2B x/y) bir plan üret; uygulamadaki `Import JSON` ile açılabilir.
3. **Temel 3B model**: Bu modüldeki özgün Python dönüştürücü ile doğrudan bir `.glb` ve `.audit.json` oluştur. Çıktı metre birimlidir. Kapı/pencere alanları *gerçek açıklık* şeklindedir.
4. **İsteğe bağlı zenginleştirme**: Blender ortamı varsa Building Tools/Archimesh ile mimari detayları artır. IFC/BIM projesi gerektiğinde uygun IfcOpenShell/Bonsai dağıtımını kur.
5. **Denetleme**: Dışa aktarımdan sonra modelin ölçülerini, geometri sayısını, duvar yönelimlerini ve eksik kalan özellikleri karşılaştır.

## ChatGPT veya Python ortamında kullanma

Bağımlılıklar: Python 3.10+, `numpy`, `trimesh`, `shapely`.

```bash
python -m pip install numpy trimesh shapely
python integrations/3d-space/scripts/openplan_to_glb.py \
  integrations/3d-space/examples/example-gallery.openplan.json \
  example-gallery.glb
```

Deneme modunda üretilen örnek GLB ayrıca `examples/` içindedir. `example-gallery.glb` dosyasını `viewer/viewer.html` sayfasında açabilir veya 3B görüntüleyiciye aktarabilirsiniz.

Desteklenen parametreler:
- `--furniture-proxies`: gerçek mobilya modeli yerine basit boyutsal kutular ekler.
- `--no-floor`: kapalı duvar çevrimlerinden yaklaşık zemin yüzeyi çıkarılmasını kapatır.

Örneğin `python -m unittest discover -s integrations/3d-space/tests -v` komutuyla testleri çalıştırabilirsiniz.

## openPlan3D'ye aktarma

`examples/example-gallery.openplan.json` dosyasını https://app.openplan3d.com üzerindeki **Import JSON** özelliğiyle içe aktarın. Buradaki veri **santimetre**; GLB verisi **metre** cinsindendir. Bu modül yalnızca web-project `floors[]` JSON'u işler; prepared RoomPlan JSON'u desteklemez.

## Blender eklentileri neden ayrı?

- Archimesh v1.2.5: `bpy` kullandığı için Blender 4.2+ gerektiren eklenti dağıtımı (manifest'e göre).
- Building Tools v1.0.13: `bpy` tabanlı Blender eklentisi; kaynak ZIP'i yerine ilgili sürümün paketlenmiş Blender eklentisinin kurulması tercih edilir.
- IfcOpenShell 0.9.0: Tam GitHub **kaynak ağacı** bir Python wheel veya Blender eklenti paketi değildir. Resmî Python paketlerini veya Bonsai sürümünü platform ve Python/Blender sürümüne uygun seçmek gerekir.
- openPlan3D: SvelteKit + Three.js web uygulaması; tarayıcıda host edilmiş sürümü kullanılabilir, kendi sunucunuza kurmak için Node ve bağımlılıkların kurulması gerekir.

## Doğruluk / sınırlılıklar

Bu GLB dönüştürücü CAD/BIM veya fotogerçekçi render motoru **değildir**. Düz duvarlar, basit dikdörtgen kapı/pencere boşlukları, sütunlar ve kapalı duvar çevrimlerinden yaklaşık zemin oluşturur. Eğrisel/eğimli duvar, karmaşık merdiven, kapı kanadı, pencere doğraması, PBR malzeme, detaylı 3B eser geometrisi ve IFC semantiğini temsil etmez. Bu özellikler başka üretim aşamaları gerektirir.
