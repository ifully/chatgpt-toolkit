# Doğrulanmış araç ve ortam matrisi (21.10.2026)

| Kaynak ZIP | Doğrulanan teknik bilgi | Uygun kullanım | ChatGPT Web için gerçek durum |
|---|---|---|---|
| `openPlan3D-main.zip` | `package.json`: SvelteKit 2, Three.js 0.182, web application 0.9.0, MIT; plan-authoring `SKILL.md` | Web plan editörü ve JSON planı | Kaynak/JSON şeması okunabilir; web editörü bağlantısı üzerinden çalışır. Node uygulaması bu katalogla otomatik kurulmaz |
| `building_tools-master.zip` | `pyproject.toml`: 1.0.13; `__init__.py` `bpy` kullanır, MIT | Blender'da hızlı yapı geometrisi | Yalnızca kaynak kodu incelenebilir; Blender yoksa eklenti çalışmaz |
| `IfcOpenShell-0.9.0.zip` | IfcOpenShell kaynak ağacı (Python/C++/Bonsai), Bonsai manifest Blender ≥ 4.2, GPL-3.0-or-later | IFC/BIM ve Bonsai | Kaynak ZIP, çalışan wheel değildir; bu ortamda `ifcopenshell` paketi yoksa aktif API kullanılamaz |
| `add-on-archimesh-v1.2.5.zip` | `blender_manifest.toml`: Archimesh 1.2.5, Blender ≥ 4.2, GPL-2.0-or-later | Odalar, pencere, kapı, dekorasyon | Bu ZIP gerçek Blender eklentisi; yalnızca Blender içinde çalışır |
| `openplan_to_glb.py` (bu paket) | Özgün Python kodu, NumPy/Trimesh/Shapely ile test edildi | Web plan JSON → temel GLB + audit | Bu bağımlılıklar sağlandığı sürece ChatGPT'nin Python ortamında çalışır |

**Lisans uyarısı:** IfcOpenShell kaynak ağacının alt bileşenleri farklı lisanslara tabidir. Bonsai GPL; çekirdek IfcOpenShell LGPL koşullarını taşıyabilir. Tek etiketle tüm paketi yeniden lisanslamayın.

**Tercih:** Teknik sergi prototipleri için önce web plan JSON + GLB dönüştürücü; BIM şart değilse 135 MB kaynak ağacını depoya taşımayın.
