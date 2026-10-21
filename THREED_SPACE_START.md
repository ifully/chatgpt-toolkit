# 3D Space Creation — ChatGPT Web çalışma modülü

Bu paket, **kullanıcının sağladığı** openPlan3D, Building Tools, IfcOpenShell 0.9.0 ve Archimesh 1.2.5 kaynakları temel alınarak hazırlanmış **özgün** bir çalışma kılavuzu ve kısmi 3B dönüştürücü içerir. **Blender eklentilerinin kurulumu veya çalıştırılması değildir.**

- [Başlangıç ve hızlı kullanım](integrations/3d-space/README.md)
- [Ajan çalışma ve doğrulama kuralları](integrations/3d-space/AGENT_GUIDE.md)
- [Dört aracın karşılaştırması](integrations/3d-space/INTEGRATION_MATRIX.md)
- [Kaynak ve lisans ilkeleri](integrations/3d-space/UPSTREAM_AND_LICENSES.md)
- [openPlan3D veri şeması](integrations/3d-space/PLAN_FORMAT_RULES.md)
- [Kalite kontrol ve sınırlılıklar](integrations/3d-space/QUALITY_CHECKS.md)
- [Örnek 2B plan (openPlan3D JSON)](integrations/3d-space/examples/example-gallery.openplan.json)
- [Örnek GLB](integrations/3d-space/examples/example-gallery.glb)
- [GLB üretme betiği](integrations/3d-space/scripts/openplan_to_glb.py)
- [Tarayıcıda GLB inceleyici](integrations/3d-space/viewer/viewer.html)

## Bana nasıl görev verilir?

> GitHub'daki `ifully/chatgpt-toolkit` deposunun `THREED_SPACE_START.md` ve `integrations/3d-space/AGENT_GUIDE.md` dosyalarını oku. Ölçülerini verdiğim sergi alanı için önce ölçülü openPlan3D JSON planı hazırla, sonra destekleniyorsa `openplan_to_glb.py` ile GLB üret ve geometri denetim raporunu sun. Eksik duvar, kapı veya pencere ölçülerini varsayım olarak açıkça listele; kaynak planı değiştirme.

**Not:** GitHub üzerindeki modül kendi başına ChatGPT'ye kalıcı Python kütüphanesi, Blender veya eklenti kurmaz. Her çalışmada ortam desteği kontrol edilir.
