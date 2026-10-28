# Tersine mühendislik: yazılım ve görsel yeniden yapılandırma

**İki ayrı alan karıştırılmamalıdır:** Yazılım tersine mühendisliği derlenmiş kodun/çalışma davranışının analizidir. Görsel yeniden yapılandırma ise raster, belge veya fotoğraf gibi gözlemlenebilir girdilerden hesaplamalı temsiller oluşturur; özgün üretim yöntemini her zaman geri kazandırmaz.

## Yazılım ve ikili dosya analizi

| Araç | İşlevi | Çalışma koşulu |
|---|---|---|
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | Ayrıştırma, dekompilasyon, kod grafikleri, fonksiyon ve referans analizi | Masaüstü/JDK ve izinli hedef |
| [angr](https://github.com/angr/angr) | Sembolik yürütme, program akışı ve veri bağımlılığı incelemesi | Python bağımlılıkları ve uzman incelemesi |
| [Rizin](https://github.com/rizinorg/rizin) | Scriptlenebilir tersine mühendislik ve ikili analiz | CLI ve izinli hedef |

## Görsel tasarım ve kültürel miras

| Araç | İşlevi | Çıkarım sınırı |
|---|---|---|
| [VTracer](https://github.com/visioncortex/vtracer) | JPG/PNG gibi raster görselden SVG vektör elde etme | Çizgilerin/nesnelerin özgün vektör geometrisi doğrulanamaz. |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Afiş, belge ve fotoğraftan metin/yerleşim bilgisi çıkarma | OCR hata payı ve yazı tipi özellikleri ayrı ölçülmeli. |
| [COLMAP](https://github.com/colmap/colmap) | Çoklu görüntüden 3B geometrik yapı kestirimi | Kamera/veri kalitesi, örtüşme ve ölçek/geometri sınırlamaları bulunur. |

## Kullanım ilkeleri

- Yalnızca sahibinin izin verdiği veya hukuken/meşru araştırma kapsamında erişilebilen yazılım ve verilerle çalışın.
- Tanınmayan ikili dosyalar ana bilgisayar veya kullanıcı hesabında doğrudan yürütülmemeli; izole analiz ortamı kullanılmalıdır.
- Görsel rekonstrüksiyon sırasında **gözlem**, **algoritmik dönüşüm** ve **tarihsel/kuramsal yorum** ayrı raporlanmalıdır.
- Kaynak kimliği, sürüm, dosya hash'i, analiz parametreleri, belirsizlik ve doğrulama örneklemi kaydedilmelidir.
- Eski afiş, tipografik numune veya sanat nesnesinden türetilen vektör/3B model, telif ve kültürel hakların ortadan kalktığı anlamına gelmez.

Kaynak ve lisans ayrıntısı: [14 arşivin v4 denetimi](../integrations/research-tools/ARCHIVE-AUDIT-V4.md).
