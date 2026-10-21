# AGENTS.md — Çalışma ve güvenlik yönergesi

Bu depo **referans kataloğu ve iş akışı rehberidir**. ChatGPT Web'e yeni yazılım kurmaz, hesabın yetkilerini değiştirmez ve ajanlar tarafından otomatik okunacağını garanti etmez.

1. Önce `START_HERE.md`, `tools.yaml` ve ilgili `categories/*.md` dosyasını oku.
2. Araç seçimini gerekli çıktı, veri gizliliği, izinler, lisans, bağımlılıklar ve o anki çalışma ortamına göre yap.
3. GitHub bağlantısının erişilebilir olması, kaynak kodunun çalıştırılabileceği veya bir MCP sunucusunun bağlandığı anlamına gelmez.
4. Önce mevcut yerleşik araçları kullan; yalnızca gerçekten gerekliyse yeni bağımlılık veya dış servis öner.
5. `curl | sh`, doğrulanmamış kurulum komutları, uzak kod çalıştırma ve belirsiz dış bağımlılıklardan kaçın.
6. Public depoya kişisel verileri, erişim anahtarlarını, kurum içi belgeleri, özel repo kodunu veya telifli içeriği gönderme.
7. Dış sistemlerde yazma/silme/yayımlama işlemlerinden önce kapsamı ve yetkiyi doğrula; kullanıcının onayını koru.
8. Akademik araştırmada atıfları bağımsız doğrula; geçerliliği kontrol edilmeyen DOI, yazar, yıl veya sonuç üretme.
9. Deponun varlığını 'kurulu' olarak yorumlama; kurulu paketi ve sürümü her oturumda ayrı kontrol et.
10. Yapılan ve yapılamayan işlemleri ayrıştır; test etmeden başarı iddia etme.
11. Haricî projelerin lisansını proje/dosya/sürüm düzeyinde kontrol et, lisans verilmemiş kodu kopyalama.
12. Mevcut yazılım projelerinde küçük, geri alınabilir değişiklikler yap ve test kaydı tut.

## Standart seçim sırası
Görev tanımı → risk/veri sınıflandırması → araç taraması → çalışma ortamı denetimi → lisans ve kaynak inceleme → yetkili icra → çıktı doğrulama → kaynak/limit raporu.

**Not:** Bu dosyanın GitHub'da bulunması ChatGPT Web'in her görüşmede otomatik olarak bunları izleyeceği anlamına gelmez. Kullanıcı bu deponun ilgili dosyalarını açıkça referans gösterebilir veya desteklenen ajan ortamına bağlayabilir.
