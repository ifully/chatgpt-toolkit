# Design Production Kit — GitHub'a hazır eklenti

**Amaç:** Grafik tasarım, gerçek vektörel çıktı, düzenlenebilir sunum, responsive HTML e-posta bülteni ve kalite güvencesi için tek bir Codex plugin paketi.

Bu depo kullanıcıya ait **özel bir entegrasyon** örneğidir; OpenAI veya üçüncü taraf projelerin resmî dağıtımı değildir. Altı yüklenen arşiv incelendi ve uygun teknolojiler bağımlılık olarak tanımlandı. Kaynak depoların tamamı kopyalanmadı (özellikle `plugins-main` içindeki karma/proprietary lisanslı eklentiler).

## İçerik

```text
.agents/plugins/marketplace.json
plugins/design-production/
  .codex-plugin/plugin.json
  skills/
    vector-design-pro/SKILL.md
    presentation-design-pro/SKILL.md
    newsletter-design-pro/SKILL.md
    design-quality-audit/SKILL.md
  config/design-tokens.json
  templates/{vector-base.svg,newsletter.mjml,slides.md}
  tools/{create-vector.mjs,create-presentation.mjs,render-newsletter.mjs,qa.py}
  package.json
scripts/{validate_repository.py,install_into_repo.py}
docs/{SOURCE_INVENTORY.md,INTEGRATION.md,QA_CHECKLIST.md,THIRD_PARTY_LICENSES.md}
```

## 1) Yeni bir GitHub deposuna yükleme
ZIP'i açın. `design-production-kit` klasöründeki **gizli `.agents`, `.github` klasörleri de dahil** bütün dosyaları yeni deponun köküne ekleyin. Ardından:

```bash
git init
git add .
git commit -m "Add design production skills and QA toolkit"
git branch -M main
git remote add origin https://github.com/KULLANICI/DEPO.git
git push -u origin main
```

**Var olan depoya** doğrudan `git init` ya da `git remote add` uygulamayın; aşağıdaki güvenli ekleme yolunu kullanın.

## 2) Mevcut repoya güvenli entegre etme
```bash
python scripts/install_into_repo.py "C:/calismalarim/mevcut-repo" --dry-run
python scripts/install_into_repo.py "C:/calismalarim/mevcut-repo"
```

Betik mevcut `.agents/plugins/marketplace.json` girişlerini koruyarak `design-production` kaydını ekler. Var olan `plugins/design-production` dizinini izinsiz **üzerine yazmaz**; çakışmada durur. Ayrıntılar: [INTEGRATION.md](docs/INTEGRATION.md).

## 3) Çalıştırma

```bash
cd plugins/design-production
npm install
npm run demo
```

Örnek SVG / PPTX / newsletter HTML dosyaları `out/` altında üretilir. Kod taraması bağımsız çalışır:

```bash
python plugins/design-production/tools/validate_repository.py
python plugins/design-production/tools/qa.py
```

`npm install` için Node.js >=22.12 gereklidir; üretim altyapısının kendisi Python 3.9+ ile yapısal olarak doğrulanabilir.

## Önemli sınırlar
- **Gerçek vektör:** SVG içindeki `<image>` öğesi ya da gömülü JPG/PNG, tam vektörel tasarım değildir.
- **PPTX:** dosyanın oluşması, font ve taşma problemlerinin olmadığını ispatlamaz; slaytlar render edilip incelenmelidir.
- **Newsletter:** HTML'nin oluşması, Gmail/Outlook uyumluluğunu tek başına kanıtlamaz; gerçek istemci testleri gerekir.
- **Kaynak lisansları:** Üçüncü taraf ZIP dosyalarının tamamını bu depoya taşımayın; lisans ve boyut sorunlarından kaçının. [THIRD_PARTY_LICENSES.md](docs/THIRD_PARTY_LICENSES.md).
- **Tasarım:** Bir kalite kontrol betiği, estetik niteliği otomatik olarak garanti edemez.

Bu pakette telifli font dosyası veya kullanıcıya ait GitHub erişim anahtarı bulunmaz.
