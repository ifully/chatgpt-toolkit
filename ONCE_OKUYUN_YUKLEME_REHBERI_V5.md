# iFully / chatgpt-toolkit — v5 GitHub yükleme rehberi

**Hazırlanma:** 28 Ekim 2026  
**Hedef repo:** https://github.com/ifully/chatgpt-toolkit  
**Kapsam:** Önceki v2, v3 ve v4 eklemelerini içeren **kümülatif güncelleme paketi** + v5 görev yönlendiricisi.  
**Doğrulanan başlangıç commit'i:** `0ce7de55e8e717dfc364a2faa597e0e987085143`.

## Bu ZIP'in içinde ne var?

`chatgpt-toolkit/` içindeki dosyalar hedef GitHub deposunun köküne karşılık gelir. Bu paket, depoda **eklenecek ve güncellenecek dosyaları** içerir; deponun tamamının bir klonu değildir. Mevcut diğer dosyalar korunmalıdır.

- Önceki katalog, kategoriler, araştırma ve beceri arşiv denetimlerine ait **95 benzersiz GitHub kaydı**.
- Yeni `routing/rules.json`: bilimsel proje, literatür, makale, deney, nitel araştırma, bibliyometri, tekrarlanabilirlik, kültürel miras, grafik tasarım, animasyon, 3B, web, tersine mühendislik, veri analizi, güvenlik, ajan değerlendirme ve otomasyon için **17 sınıf**.
- Yeni `routing/task_router.py`: Türkçe/İngilizce kısa görev tanımını öneri, doğrulama ölçütü ve risk notlarına yönlendirir. Sadece Python standart kütüphanesi kullanır.
- Yeni `routing/tests/`: çevrimdışı otomatik testler.
- Yeni `routing/CHATGPT_PROJECT_INSTRUCTIONS.md`: yalnızca desteklenen ChatGPT Project/ajan bağlamına **elle** taşınabilecek kullanım kuralları.
- Güncellenen `README.md`, `START_HERE.md`, `AGENTS.md` ve görev matrisi.

## GitHub'a yüklemek

1. ZIP'i bilgisayarınıza indirin ve arşivi çıkarın.
2. Çıkan `chatgpt-toolkit` klasörünün **içeriğini** kendi `ifully/chatgpt-toolkit` çalışma kopyanızın kök klasörüyle birleştirin. Mevcut dosyalar varsa yalnızca aynı yoldaki güncellenenleri üzerine yazın; depoyu bütünüyle değiştirmeyin.
3. Önce değişiklikleri gözden geçirin. Git kullanıyorsanız `git status` ve `git diff` ile kontrol edip commit/push yapabilirsiniz. GitHub web arayüzünde yalnızca ZIP dosyasını yüklemek, içeriğin klasörlere otomatik açılmasını sağlamaz.
4. Özellikle `routing/rules.json`, `routing/task_router.py`, `routing/README.md`, `routing/tests/test_task_router.py` dosyalarının doğru konumda olduğuna bakın.
5. Çalıştırma ortamında Python 3 bulunuyorsa repo kökünde şu iki komutu kullanın:

   ```bash
   python3 -m unittest discover -s routing/tests -v
   python3 routing/task_router.py "Bilimsel proje fikri ve literatür taraması"
   ```

## Görevlere göre kullanım

Örnekler:

```bash
python3 routing/task_router.py "TÜBİTAK için araştırma fikri"
python3 routing/task_router.py "Tipografik okunabilirlik deneyi ve bilimsel yayın"
python3 routing/task_router.py "Yetkili tersine mühendislik incelemesi" --json
python3 routing/task_router.py "Veri analizi" --probe
```

## Açık sınırlar

- Bu v5, 95 kaydı **gerçekten kurmaz veya ChatGPT'ye 95 yeni yerleşik beceri yüklemez**. Haricî depo/kod dağıtımı içermez.
- `--probe` yalnızca Python modülü veya komut yolu görünürlüğünü kontrol eder. Gerçek kurulum, sürüm, entegrasyon, güvenlik ve yetki hâlâ ayrı denetim gerektirir.
- ChatGPT Web, GitHub deposunu her oturumda otomatik kullanmaz. Yönergelerin bağlı Project'e yüklenmesi veya uygun ajan ortamının depo dosyalarına açık erişimi gerekir.
- GitHub’daki tüm kaynakların lisansı, sürümü ve güncelliği, fiilen kullanılacakları tarihte ilgili ana projeden yeniden doğrulanmalıdır.
- Akademik iddialar, DOI ve kaynaklar bağımsız doğrulama gerektirir; etik onam ve veri gizliliği korumaları kullanıcı/araştırmacı sorumluluğundadır.

**Test kaydı:** 28 Ekim 2026; standart kütüphaneli yönlendirici için 9 test başarıyla tamamlandı. ZIP bütünlüğü dağıtım öncesi ayrıca kontrol edilir.
