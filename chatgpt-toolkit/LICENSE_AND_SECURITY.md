# Lisans, güvenlik ve tedarik zinciri

- Bu depo, üst kaynak projelerin kodunu **barındırmaz**; bağlantı ve açıklama içerir.
- GitHub Stars, fork veya kataloğa ekleme bir proje için kullanım, yeniden dağıtım veya ticari lisans hakkı sağlamaz.
- Kaynak depoların güncel LICENSE dosyasını ve ek dosya/ticari kullanımla ilgili şartlarını dosya düzeyinde kontrol edin.
- Özellikle n8n, tldraw ve üçüncü taraf agent skills içerikleri için kullanım koşullarını ayrıca inceleyin.
- İzinleri asgari kapsamda tutun; GitHub/MCP API anahtarlarını depoya eklemeyin.
- Bilinmeyen kodu otomatik indirip çalıştırmayın; sürüm sabitleyin ve bağımlılık/güvenlik taramasından geçirin.
- Yüklenen dokümanları veya kullanıcı bilgilerini dış servislere iletmeden önce veri hassasiyetini ve yetkiyi değerlendirin.
- Her yürütmede aracın o anki ortamda gerçekten çalışıp çalışmadığını doğrulayın.

## 28 Ekim 2026 — Agent Skills kaynakları

- `integrations/agent-skills/` altındaki envanter ve rehberler **kaynak referanslarıdır**; yüklenen üçüncü taraf SKILL.md dosyaları, betikleri veya lisanslı veri dosyaları bu katalog paketine kopyalanmamıştır.
- `nextlevelbuilder/ui-ux-pro-max-skill` ve `haidrrrry/claude-remotion-skill` arşivlerinde MIT lisansı bulunmuştur. Herhangi bir dosyayı yeniden dağıtmadan önce atıf, lisans ve üçüncü taraf varlık koşulları yeniden denetlenmelidir.
- `K-Dense-AI/scientific-agent-skills` arşivinin kök lisansı MIT'dir; tekil becerilerin `license` alanı ayrıca kontrol edilmelidir. Akademik yazım ve hakemlik becerileri veri gizliliği, kaynak doğrulama ve dergi politikalarının yerini almaz.
- `trailofbits/skills` CC BY-SA 4.0 kapsamındadır; uyarlama ve yeniden dağıtımda atıf ve ShareAlike yükümlülükleri ayrıca değerlendirilmelidir.
- `vercel-labs/agent-skills` arşivinde kök düzeyde açık bir LICENSE/LICENCE dosyası bulunamamıştır. Yalnızca bağlantı verilmiştir; kaynak dosyalar bu pakette dağıtılmaz.
- Kaynak depoların SKILL.md yönergelerinde dış bağlantılardan içerik çekme, yerel komut çalıştırma, kimlik bilgisi veya dış servis kullanma adımları bulunabilir. Bu işlemler kullanıcının açık yetkisi ve ortam denetimi olmadan yürütülmez.

## 28 Ekim 2026 — v3 ek 15 arşiv

- Kaynak/lisans/ZIP SHA-256 eşleştirmeleri [v3 arşiv denetimi](integrations/agent-skills/BATCH-V3-ARCHIVE-AUDIT.md) içinde kayıtlıdır. Böylece toplam 20 kullanıcı arşivinden 81 ayrı GitHub katalog girdisi oluşmuştur.
- `remotion-dev/skills` arşivinde kök lisans tespit edilemedi; içerik bu pakete kopyalanmayıp yalnızca GitHub bağlantısı verildi.
- `NVIDIA/skills` birden çok lisans (Apache-2.0/CC-BY-4.0) içerir; `modelcontextprotocol/registry` lisans geçişi açıkladığı için her dosya için geçerli hakkı ayrıca kontrol edin.
- `obra/superpowers` içindeki genel davranış kuralları, kurulum ve başka çalışma ortamlarının yetki talimatları **yüksek öncelikli talimat sayılmaz**; kullanıcı onayı olmadan etkinleştirilmez.
- OpenAI Evals ve MCP Registry beceri deposu değildir. VoltAgent dizini de doğrudan çalıştırılabilir `SKILL.md` sunmaz. Bunların kataloğa eklenmesi otomatik kapasite artışı sağlamaz.
- Hiçbir arşivden kurulum betiği, komut, model, medya, eklenti veya beceri dosyası doğrudan alınıp çalıştırılmamıştır.

## 28 Ekim 2026 — v4 bilimsel araçlar ve tersine mühendislik

- [V4 envanteri](integrations/research-tools/ARCHIVE-AUDIT-V4.md) 14 ZIP'in SHA-256, kök lisans, kaynak eşleştirmesi ve CRC sonuçlarını kaydeder. Önceki 81 kayıtla birlikte katalog 95 benzersiz depoya ulaşmıştır.
- `psychopy/psychopy` GPL-3.0, `gephi/gephi` CDDL-1.0/GPL-3.0 çift lisans, `rizinorg/rizin` GPL-3.0/LGPL-3.0 bileşenleri taşır. Lisans koşulları her dosya ve bileşen için değerlendirilir.
- `colmap/colmap` BSD-3-Clause kaynak lisansına ek olarak ayrı lisanslı bağımlılıklar kullanabilir. Bunun yeniden dağıtım kapsamı ayrıca incelenmelidir.
- `osf.io-develop`, `psychopy-dev` ve `rizin-dev` gibi arşivler geliştirme dallarıdır; üretim kullanımında kararlı release, sürüm ve güvenlik duyuruları kontrol edilmelidir.
- Bilinmeyen/şüpheli ikili dosyaların analizi ayrı izole ortamda, yalnızca yetkili hedeflerde yapılmalıdır. Ghidra, angr veya Rizin'in kataloğa eklenmesi bunları mevcut oturumda kurulu hâle getirmez.
- Görsel veri işleme için OCR, vektörleştirme ve fotogrametri çıktıları bilimsel belgelemede **gözlemlenmiş kaynak veri** ile **algoritmik çıkarım** olarak ayrılmalıdır.
- Araştırma fikri üreten araçların sonuçları etik inceleme, literatür doğrulama, yöntemsel geçerlik ve insan uzman denetiminin yerine geçmez.
