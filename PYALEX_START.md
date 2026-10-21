# PyAlex × ChatGPT Web — Başlangıç

Bu modül, [PyAlex](https://github.com/J535D165/pyalex) ve [OpenAlex](https://openalex.org/) verilerini akademik literatür arama ve bibliyografik ön inceleme için güvenli, tekrarlanabilir bir iş akışına dönüştürür. **PyAlex'in kaynak kodu burada kopyalanmaz.**

- [Kullanım seçenekleri](integrations/pyalex/README.md)
- [ChatGPT görev yönergesi](integrations/pyalex/AGENT_GUIDE.md)
- [Literatür arama protokolü](integrations/pyalex/LITERATURE_PROTOCOL.md)
- [Bibliyografik doğrulama ve sınırlar](integrations/pyalex/VERIFICATION.md)
- [Örnek Python arama komutu](integrations/pyalex/scripts/search_openalex.py)
- [Arama günlüğü şablonu](integrations/pyalex/templates/search_log.csv)
- [Literatür eleme formu](integrations/pyalex/templates/screening.csv)

**ChatGPT Web'de kullanım:** Bana `https://github.com/ifully/chatgpt-toolkit/blob/main/PYALEX_START.md dosyasındaki protokolü kullanarak [konu] için literatür tarama planı ve kaynak doğrulama tablosu oluştur.` diyebilirsiniz.

**Sınırlama:** Bu depo, ChatGPT Web'e PyAlex yüklemez, OpenAlex API anahtarı oluşturmaz ve dış ağa erişim yetkisi kazandırmaz. Canlı PyAlex sorgusu için ağ erişimi bulunan bir Python çalışma ortamı ve OpenAlex API yapılandırması gerekir.
