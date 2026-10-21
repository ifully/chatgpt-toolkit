# Ajan çalışma yönergeleri — 3B mekân

Bu dosyayı görev başında oku; **kullanıcının açık kısıtlarını ve onaylanmış geometri kararlarını değiştirme**.

1. Önce varsa kaynak planı/HTML/GLB'yi incele, son sürüm olup olmadığını teyit et; önceki sürümleri kendi kendine geri getirme.
2. Ölçüleri santimetre/metre ayrımıyla kaydet. Kapı, pencere, kolon ve duvarların referans koordinatlarını numaralandır.
3. Plan açıkça belirtilmemişse **varsayımları ayrı raporla**; kesin ölçüymüş gibi sunma.
4. Parametrik iç geometriden önce planın topolojik kapanmasını ve açıklıkların duvar sınırları içinde olduğunu denetle.
5. openPlan3D JSON üretirken resmi plan authoring skill dokümanını sürümüne göre kontrol et: https://github.com/laanlabs/openPlan3D (yüklenen pakette `docs/skills/openplan3d-plan-authoring/SKILL.md`). Kaynak adını farklı bir fork gösteriyorsa gerçek upstream'i doğrula.
6. Yalnızca doğrulanmış şemalar arasında dönüştür; prepared RoomPlan ile web-project JSON formatlarını karıştırma.
7. Kısa/uzun kenar ve yüksekliği kullanıcı belirttiyse değiştirme. Tüm koordinatları açıkça etiketle.
8. `openplan_to_glb.py` ile üretim için gerekli Python bağımlılıklarının mevcut olduğunu kontrol et. Önce örneği çalıştır, sonra kullanıcının planını işle.
9. Dışa aktarımdan sonra `.audit.json` içindeki duvar, kapı, pencere, kolon sayılarını orijinal planla eşleştir. Mümkünse görsel önizleme ile doğrula.
10. GLB yalnızca kutulardan ve yaklaşık zeminlerden oluşuyorsa bunu **fotogerçekçi galeri** olarak sunma. Blender/PBR/render gerektiren işleri ayrı bildir.
11. `bpy` gerektiren Archimesh ve Building Tools fonksiyonlarını Blender kurulu değilken çalıştırmış gibi gösterme.
12. IFC/BIM için yanlış bir `IfcOpenShell.zip` kurulumu önerme; doğru wheel/platform dağıtımını seç ve kaynak lisanslarını koru.
13. Üçüncü taraf ZIP'lerin kaynak kodunu doğrudan kalıcı GitHub kataloğuna kopyalama; rehber/bağlantı sakla ve lisansı doğrula.
14. Kullanıcının gizli dosyalarını, API anahtarlarını veya üçüncü taraf telifli modelleri kamuya açık depoya aktarma.
15. İşlemin sonunda gerçekten çalıştırılan testleri, çalışma ortamı koşullarını, yapılamayanları ve sınırlılıkları açıkla.

### Karar ağacı

- **Sadece plan/JSON** → openPlan3D web şeması.
- **Ölçülü temel 3B GLB** → mevcut Python + Trimesh dönüştürücü.
- **Blender mimari bileşenler** → Archimesh veya Building Tools; Blender şart.
- **Profesyonel IFC/BIM** → IfcOpenShell ve gerekirse Bonsai.
- **Mimari render / PBR / fotogerçekçilik** → ayrıca ışık, doku, normal, yansıma, kamera ve render aşaması.
