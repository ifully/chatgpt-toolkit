# Mevcut repoya entegrasyon

## Tercih edilen yol: korumalı kopyalama

Önce ZIP'i açın; ardından paket kökünden:

```powershell
python scripts/install_into_repo.py "C:\Users\YOU\Projects\MY_REPO" --dry-run
python scripts/install_into_repo.py "C:\Users\YOU\Projects\MY_REPO"
```

- `--dry-run` mevcut dosyaları değiştirmeden yapılan işleri listeler.
- `plugins/design-production` varsa betik durur; mevcut projeyi silmez, üzerine yazmaz.
- `.agents/plugins/marketplace.json` varsa mevcut kayıtları koruyup bir tane yeni kayıt ekler.
- Var olan `AGENTS.md` üzerine yazılmaz. Bu durumda plugin becerilerinin kullanımı için mevcut AGENTS.md'ye kuralları manuel ekleyin.
- Mevcut `.github/workflows` dosyalarına dokunulmaz; repo QA workflow'u ayrıca isteğe bağlı kopyalanabilir.
- Betik, hedef depoda `git add/commit/push` yapmaz. Git işlemleri kullanıcıya aittir.

> Yalnızca yeni ve boş depolarda tüm paket içeriğini köke kopyalamak en kolay yoldur.

## Kod ve ajan çalıştırma

```powershell
cd C:\Users\YOU\Projects\MY_REPO\plugins\design-production
npm install
npm run demo
npm run qa
```

**Üretim:** `out` Git'e alınmaz, ancak sizin teslimatlarınızı ayrıca saklamanız gerekir. Asıl şablonlar ve beceri dosyaları sürüm kontrolüyle izlenir.

## Kullanım örnekleri
- “vector-design-pro becerisiyle, gerçek SVG olarak düzenlenebilir bir amblem oluştur; QA'dan geçir.”
- “presentation-design-pro ile kaynaklı bir akademik sunum hazırla; her slaytın görsel kontrolünü yap.”
- “newsletter-design-pro ile erişilebilir MJML bülten hazırla; gönderilmeden önce linkleri raporla.”
- “design-quality-audit ile tüm çıktıları teknik ve görsel eksikler açısından kontrol et.”

## Zamanında güncelleme
Depoda üçüncü tarafların **tam kaynak kodlarını** saklamaz. `npm install` paket kurulumundan sonra ekip için `package-lock.json` üreterek commit edin; sürdürülebilir kurulumlarda `npm ci` kullanın. Değişiklikleri ayrı PR'da inceleyin. Upstream sürümleri ve lisanslarını takip edin.
