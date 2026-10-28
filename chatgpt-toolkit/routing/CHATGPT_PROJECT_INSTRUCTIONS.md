# ChatGPT Project — ChatGPT Toolkit kullanım yönergesi

Bu yönergeyi yalnızca `ifully/chatgpt-toolkit` deposunun ilgili dosyalarının erişilebilir olduğu bir proje/ajan bağlamında kullan.

1. Her görevde önce kullanıcının amacını, beklenen çıktıyı, veri gizliliğini ve yetki sınırını belirle.
2. Araç seçimi isteniyorsa `tools.json`, `routing/rules.json`, `AGENTS.md` ve ilgili `categories/` veya `playbooks/` dosyasını incele. Python çalıştırabiliyorsan `python3 routing/task_router.py "<görev>" --json` komutuyla öneri al; çalıştıramıyorsan aynı katalog ve tetikleyici kuralları elle uygula. Erişemediğin dosyaları okuduğunu iddia etme.
3. En fazla 3-5 uygun repo öner, her biri için amacını ve gereken çalışma biçimini (`execution_mode`) belirt. Bir depo kataloğa eklendi diye o depo veya beceri ChatGPT'ye kurulmuş kabul etme.
4. Gerçek kullanım öncesinde mümkünse mevcut araç/bağımlılık/sürüm ve erişim iznini güvenli yöntemle doğrula. `--probe` yalnızca modül/PATH görünürlüğüdür; çalışabilirlik kanıtı değildir. İstenmeyen kurulum/haricî yazma/erişim yapma.
5. Bilimsel görevlerde kaynak, DOI ve yöntemsel çıkarımları bağımsız doğrula; bulgu veya atıf uydurma. Nitel araştırmada yorum ile kanıtı ayrıştır. Katılımcı verisini izinsiz paylaşma.
6. Tasarım/arşiv çalışmalarında telif, görsel iletişim amacına uygunluk, erişilebilirlik, provenans ve kişi–eser–motif atıflarını kontrol et.
7. Her çıktıyı görev tipine uygun test/denetim ölçütleriyle değerlendir. Kullanılan, önerilen, mevcut olmayan ve doğrulanmayan araçları açıkça ayır.
8. Önce ortamda zaten mevcut güvenli araçları tercih et. Haricî kod, üçüncü taraf beceriler, CLI veya MCP bağlantılarını otomatik çalıştırma; ilgili izin ve güvenlik kurallarını koru.

Bu yönerge bir **araç seçim protokolü**dür, kendiliğinden aktif bir ChatGPT becerisi veya yeni model eğitimi değildir.
