# Yapısal doğrulama

Aşağıdaki işlemler ağ erişimi gerektirmez; yalnızca betiğin sözdizimini ve seçicinin çalışmasını denetler:

```bash
python -m py_compile integrations/aishort/find_prompt.py
python integrations/aishort/find_prompt.py literatür
python integrations/aishort/find_prompt.py --id RP-02
```

Bu testler, istemlerin bilimsel çıktısının doğruluğunu veya AiShort uygulamasının kurulduğunu **kanıtlamaz**. İş bazında `QUALITY_GATE.md` kontrolleri uygulanmalıdır.
