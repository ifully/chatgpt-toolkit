# Bilimsel proje, araştırma fikri ve yöntem geliştirme

Bu sayfa bilimsel araştırma sürecinin **fikir/hipotez → literatür → yöntem → veri → analiz → raporlama** aşamalarında yararlı olabilecek kaynakları sınıflandırır. Depoların listelenmesi onların otomatik kurulduğunu veya bilimsel özgünlüğü garanti ettiğini göstermez.

| Aşama | Araç | Kullanım sınırı |
|---|---|---|
| Fikir ve hipotez geliştirme | [AutoRA](https://github.com/AutoResearch/autora) | Deneysel araştırma otomasyonu; alanın kuramsal çerçevesi ve etik izin ayrıca gerekir. |
| Veri odaklı fikir/deney iyileştirme | [R&D-Agent](https://github.com/microsoft/RD-Agent) | Genellikle makine öğrenmesi ve veri odaklı Ar-Ge; sosyal bilimlere doğrudan taşınamaz. |
| Literatür sentezi | [OpenScholar](https://github.com/AkariAsai/OpenScholar) | Kaynak doğruluğu, metin-iddia ilişkisi ve kapsam denetlenmeli. |
| Görsel algı/deney | [PsychoPy](https://github.com/psychopy/psychopy) | Uyaran sunumu, tepki ölçümü ve çalışma sürümü kayıt altına alınmalı. |
| Belge/görsel arşiv analizi | [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | OCR hataları, dil ve yazı sistemi farklılıkları insan denetimi gerektirir. |
| Bibliyometrik/kültürel ağlar | [Gephi](https://github.com/gephi/gephi) | Ağ grafiği, yorumlama çerçevesi olmadan bilimsel açıklama değildir. |
| Araştırma kaydı | [OSF](https://github.com/CenterForOpenScience/osf.io) | Depo platform kaynak kodudur; gerçek kullanım için OSF hizmeti/kurulumu gerekir. |
| Veri ve deney sürümleme | [DVC](https://github.com/treeverse/dvc) | Veri erişimi, saklama, gizlilik ve Git altyapısı gerekir. |
| Tekrarlanabilir analiz | [Snakemake](https://github.com/snakemake/snakemake) | Ortam/bağımlılık sürümleriyle birlikte tanımlanmalı. |

## Grafik tasarım ve görsel iletişimde olası araştırma senaryoları

1. **Tipografik okunabilirlik:** İki veya daha fazla tipografik koşul için algı/tepki deneyini PsychoPy ile tanımlayın; rastgeleleme, örneklem büyüklüğü ve körleme/uyaran sırası etkilerini önceden değerlendirin.
2. **Grafik tasarım eğilimleri:** Bibliyometrik verileri mevcut katalogdaki Zotero ve bilimsel araçlarla derleyip Gephi'de ilişki ağı oluşturun. Veri tabanı kapsamını ve ağ metriklerini açıkça raporlayın.
3. **Arşivdeki görsel metinler:** PaddleOCR ile transkripsiyon adayı üretin; altın standart örneklem üzerinden karakter/kelime hatalarını ölçün. OCR'ı özgün kaynak yerine koymayın.
4. **Geleneksel üretim / tasarım bilgisi:** Birincil kaynak, görüşme ve nesne verileri için veri sözlüğü oluşturun; gözlemlenmiş kanıt ile yorum/çıkarımı ayırın.
5. **Açık bilim:** Araştırma soruları, hipotez, veri işleme kuralları ve önceden belirlenen ölçütler için OSF ön kayıt yaklaşımını değerlendirin; analiz kodunu DVC/Snakemake ile sürümleyin.

## Gerekli akademik denetimler

- Araştırma boşluğu, yalnızca bibliyometrik ağdaki düşük yoğunlukla veya ajan önerisiyle kanıtlanmaz; sistematik alan/literatür karşılaştırması gerektirir.
- Hipotezler yanlışlanabilir, araştırma soruları ölçülebilir, bağımlı ve bağımsız değişkenler operasyonel biçimde tanımlı olmalıdır.
- İnsan katılımcılarla deney/görüşme için etik kurul, aydınlatılmış onam ve veri koruma koşulları dikkate alınmalıdır.
- Kaynak kontrolünde DOI bulunması yeterli değildir; iddia ile tam metin arasındaki anlam ilişkisi doğrulanmalıdır.

Kontrollü uygulama için [araştırma projesi iş akışı](../playbooks/research-project-methodology.md) ve [v4 kaynak/lisans denetimi](../integrations/research-tools/ARCHIVE-AUDIT-V4.md).
