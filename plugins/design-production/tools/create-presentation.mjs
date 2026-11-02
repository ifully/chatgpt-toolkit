import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import pptxgen from 'pptxgenjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const out = path.join(root, 'out');
fs.mkdirSync(out, {recursive: true});

const pptx = new pptxgen();
pptx.layout = 'LAYOUT_WIDE';
pptx.author = 'Design Production Kit — example';
pptx.subject = 'Editable presentation demonstration';
pptx.title = 'Tasarım Sistemi — Örnek';
pptx.lang = 'tr-TR';
pptx.theme = {
  headFontFace: 'Aptos Display', bodyFontFace: 'Aptos', lang: 'tr-TR'
};

const C = {ink:'15191D', paper:'F6F4EF', accent:'0B7058', muted:'65706D'};
function baseSlide() {
  const slide = pptx.addSlide();
  slide.background = { color:C.paper };
  slide.addShape(pptx.ShapeType.line, { x:0.9, y:0.85, w:11.5, h:0, line:{color:C.accent,width:2}});
  return slide;
}
let slide = baseSlide();
slide.addText('Tasarım Sistemi', {x:0.9,y:1.5,w:11.4,h:0.95,fontFace:'Aptos Display',fontSize:44,bold:true,color:C.ink,breakLine:false,margin:0});
slide.addText('Tipografi · Grid · Görsel hiyerarşi', {x:0.93,y:2.75,w:10.9,h:0.55,fontSize:22,color:C.muted,margin:0});
slide.addShape(pptx.ShapeType.rect, {x:0.9,y:4.1,w:2.2,h:0.20,line:{color:C.accent,transparency:100},fill:{color:C.accent}});
slide.addText('01 / Örnek sunum', {x:0.92,y:6.58,w:4.5,h:0.35,fontSize:12,color:C.muted,margin:0});

slide = baseSlide();
slide.addText('Düzenlenebilir içerik', {x:0.9,y:1.2,w:11.2,h:0.65,fontFace:'Aptos Display',fontSize:34,bold:true,color:C.ink,margin:0});
slide.addText('Yerel metin kutuları\nGerçek vektör şekiller\nTutarlı görsel hiyerarşi', {x:1.12,y:2.3,w:10.9,h:2.1,breakLine:false,fontSize:23,color:C.ink,margin:0.03});
slide.addText('02 / Örnek sunum', {x:0.92,y:6.58,w:4.5,h:0.35,fontSize:12,color:C.muted,margin:0});

await pptx.writeFile({fileName:path.join(out,'sample-presentation.pptx')});
console.log(`PPTX written: ${path.join(out,'sample-presentation.pptx')}`);
