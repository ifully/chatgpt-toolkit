# Tam Spec Kit kurulumu: ChatGPT Web'den farklıdır

Bu yöntem **desteklenen kod ajanı ve terminali olan bir çalışma ortamı** içindir. ChatGPT Web'in normal sohbetinde "/speckit" komutlarını görünür hâle getirmez.

## Gereksinimler
- Python >= 3.11
- `uv` paket yöneticisi
- Desteklenen bir kod ajanı (ör. Codex CLI)

## Resmî kurulum örneği

```sh
uv tool install specify-cli
specify init ornek-proje --integration codex
cd ornek-proje
```

Mevcut projede kurulum daha fazla dikkat ister; resmî [existing projects](https://github.com/github/spec-kit/blob/main/docs/guides/existing-projects.md) rehberini okuyun. `--here --force` kullanımı mevcut yönetilen dosyaların üzerine yazabilir; önce yedek, sürüm kontrolü ve diff incelemesi yapın.

## ChatGPT Web'e özel sonuç

Bu depo içindeki `workflows` ve `templates` belgelerini okumam için yerel kurulum **gerekmez**. Ancak Specify CLI'nin komutlarını gerçekten yürütmek isterseniz, uygun terminal ortamı ve ajan entegrasyonu zorunludur.

Resmî belgeler: https://github.github.io/spec-kit/ ve https://github.com/github/spec-kit
