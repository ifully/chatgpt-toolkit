# openPlan3D web-project formatı — görev için gerekli asgari kurallar

Bu özet, kullanıcının yüklediği openPlan3D paketindeki `docs/skills/openplan3d-plan-authoring/SKILL.md` ve ilgili doğrulayıcının incelenmesiyle hazırlanmıştır. Hatalı kullanım şüphesinde **kaynak sürümdeki doğrulayıcı** esas alınır.

## Temel şema

- Proje `id` (boş olmayan string), `name`, `floors[]`, `activeFloorId` alanlarını içerir.
- Kat `id`, `name`, `level`, `elevation` ve **zorunlu `walls[]`** taşır; diğer diziler (`doors`, `windows`, `furniture`, `rooms`, `stairs`, `columns` vb.) boş olabilir.
- Tüm plan koordinatları ve kalınlıklar **santimetredir**. x sağa, y aşağı gider. Duvar geometrisi merkez çizgileriyle yazılır.
- Her kat içinde duvar/kapı/pencere/mobilya vb. nesne kimlikleri çakışmamalıdır.
- Duvar: `id`, `start:{x,y}`, `end:{x,y}`, `thickness` (> 0), `height` (genellikle 280 cm).
- Kapı: `id`, `wallId`, `position` (0–1 merkez), `width`, `height`, isteğe bağlı `type` (single/double/sliding/french/pocket/bifold/opening/garage).
- Pencere: `id`, `wallId`, `position` (0–1 merkez), `width`, `height`, `sillHeight` (zeminden, ≥ 0).
- Kolon: `id`, `position:{x,y}`, `diameter`, `height`, `shape` (`square`/`round`).
- Oda: `id`, `name`, `walls` (duvar id listesi), `floorTexture`, `area`; odalar kapanan çevrimlerden otomatik tespit edilir. Duvar dizilimi açık kalırsa oda görünmeyebilir.

## Bu modüldeki GLB dönüştürücünün ilave koşulları

- Yalnızca düz, sabit yükseklikte duvarlar; `curvePoint`, `startHeight`, `endHeight` yok.
- Kapı ve pencereler duvar uçlarının dışına taşmaz; örtüşen açıklıklar reddedilir.
- Basit kutu duvar mesh'leri oluşturulur; kapı/pencere açıklıklarında mesh boşluğu bırakılır.
- GLB koordinatı x sağa, **y yukarı yönünde uzamsal yatay**, z düşey olarak tanımlıdır; ekran y ekseni ters çevrilir.
- Gerçek kapı kanadı ve pencere camı üretilmez; duvar içinde doğru delik/boşluk bulunması garanti edilir.
- Zemin, duvar merkez çizgilerinin oluşturduğu kapalı poligonlardan yaklaşık üretilir; statik/teknik döşeme modeli değildir.

## Kaynak

Kaynak beceri yönergeleri yüklenen `openPlan3D-main.zip` içinde:
`openPlan3D-main/docs/skills/openplan3d-plan-authoring/SKILL.md`

Hata ve sürüm farklılığında GitHub'daki güncel `projectValidation.ts` ve plan authoring skill kontrol edilir.
