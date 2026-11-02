import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import mjml2html from 'mjml';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const source = path.join(root,'templates','newsletter.mjml');
const out = path.join(root,'out');
fs.mkdirSync(out,{recursive:true});
const result = mjml2html(fs.readFileSync(source,'utf8'),{
  validationLevel:'strict', keepComments:false
});
if (result.errors?.length) {
  for (const e of result.errors) console.error(`${e.line ?? '?'}: ${e.formattedMessage ?? e.message}`);
  process.exit(1);
}
fs.writeFileSync(path.join(out,'newsletter.html'),result.html,'utf8');
console.log(`HTML written: ${path.join(out,'newsletter.html')}`);
console.warn('WARNING: Demo URLs and contact information must be replaced before any sending.');
