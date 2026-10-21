# ChatGPT / ajan kullanım protokolü

## Kapsam ve öncelik

1. Kullanıcının son isteği, proje dosyaları ve varsa onaylanmış mimari/terminoloji temel alınır. Kapsamı izinsiz genişletme.
2. Önce bu dosyayı ve ilgili `workflows/*.md` belgesini oku.
3. Mevcut sistem üzerinde değişiklik istendiyse önce kod tabanını, testleri, bağımlılıkları ve çalışan işlevleri değerlendir. Kritik dosyalar okunmadan değişiklik önerisini kesinleştirme.
4. İstenmeyen yeniden yazım, veri silme, şema değişimi ve toplu refaktörden kaçın; değişiklikleri dar ve geri alınabilir tut.
5. **Aşama kayıtları**: constitution → spec → clarify → plan → checklist → tasks → analyze → implement → verify. Her aşamanın çıktı dosyasını ve onay durumunu belirt.
6. `spec.md` **ne/neden**, `plan.md` **nasıl**, `tasks.md` **uygulama adımları** için kullanılır. Bu ayrımı koru.
7. Uygulama izni veya kod erişimi yoksa yalnızca taslak/plan üretildiğini açıkça söyle. Test edilmemiş işlemleri tamamlanmış olarak işaretleme.
8. Güvenlik / erişilebilirlik / gizlilik / sürüm uyumluluğu / veri bütünlüğü gereksinimlerini gereksiz yere atlama; bağlama göre ele al.
9. Harici kod ve araç çalıştırmadan önce lisans, erişim, bağımlılık ve güvenlik koşullarını doğrula.
10. Akademik araştırmada doğrulanmamış kaynak, DOI, veri, analiz veya nedensellik iddiası üretme. Literatür kayıtlarının varlığı ile içerik desteğini ayır.

## Aşama geçiş kapıları

- **Specification gate:** Sorunun kapsamı, kapsam dışı hususlar, aktörler, kabul ölçütleri ve mevcut sisteme uyum açık mı?
- **Planning gate:** Teknik yaklaşım kanıta ve gerçek teknoloji yığınına dayanıyor mu? Riskler ve geri alma yöntemi yazılmış mı?
- **Implementation gate:** Dosyalar, test yaklaşımı ve izinler mevcut mu? Geri döndürülemez etkiler için kullanıcı onayı alındı mı?
- **Release gate:** Kabul ölçütleri karşılandı mı? Otomatik testler, manuel kontroller ve sınırlılıklar raporlandı mı?

## ChatGPT Web kullanım komutu

`Bu depo içindeki integrations/spec-kit/AGENT_GUIDE.md ve uygun workflow'u oku; bana yönelik mevcut istekte yöntemini uygula. Resmî /speckit komutlarını çalıştırdığını iddia etme. Önce kanıt/gereksinim, sonra plan, sonra izinli uygulama, ardından test.`
