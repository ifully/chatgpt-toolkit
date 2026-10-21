# ChatGPT ajan yönergesi: PyAlex akademik tarama

1. İlk olarak araştırma problemini, disiplin(ler)i, kapsamı, tarih aralığını ve TR/EN arama dilini belirle; kullanıcıca kararlaştırılmış kapsamı değiştirme.
2. Sorgu dizgilerini ve eşanlamlı kavramları izlenebilir biçimde belgele; keşif sorgusunu sistematik tarama olarak sunma.
3. Canlı veri gerekiyorsa çalışma ortamında `pyalex`, dış ağ bağlantısı ve yetkili OpenAlex erişimi olup olmadığını kontrol et. **Yoksa sorgunun çalıştırıldığını söyleme.**
4. Mevcut erişimi kullanarak bibliyografik metadata getir; her kayda OpenAlex ID, DOI, arama zamanı ve sorgu kökeni ekle.
5. DOI, yazar adı, başlık, yıl, dergi/kitap kaynağı gibi alanları çapraz doğrula (yayıncı ve/veya Crossref). OpenAlex kaydı tek başına atıf doğrulaması değildir.
6. Scopus/WoS indeksleme, Q1 quartile, güncel etki faktörü veya hakemli statüsü **OpenAlex kaydından çıkarılamaz**; yetkili kaynakta ayrıca doğrula.
7. Başlık/özet elemesini önceden tanımlanan ölçütlere göre yap; tam metin gerekliyse telif ve erişim koşullarını koru. Uydurma alıntı/sayfa numarası üretme.
8. Bulguları düz kayıtlar ve yorumlarla ayrı tut; akademik yazımda yöntem, bulgu ve yorum ayrımını koru. APA 7 yazımını ve tüm atıfların kaynakça eşleşmesini denetle.
9. Sonuç raporunda veri erişim sınırı, arama tarih(ler)i, sorgular, veritabanı kapsamı, dahil/dışla kararları, eksik DOI/özet ve belirsizlikleri belirt.
10. Kullanıcı izni ve uygun yürütme altyapısı olmadan dış sisteme veri yükleme veya uzak kod kurulumuna girişme.
