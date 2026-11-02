import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

// A deterministic, dependency-free SVG baseline. For interactive geometry,
// use @svgdotjs/svg.js or Paper.js in browser / compatible DOM environments.
const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '..');
const out = path.join(root, 'out');
fs.mkdirSync(out, { recursive: true });
const xml = fs.readFileSync(path.join(root, 'templates', 'vector-base.svg'), 'utf8');
fs.writeFileSync(path.join(out, 'sample-vector.svg'), xml, 'utf8');
console.log(`SVG written: ${path.join(out, 'sample-vector.svg')}`);
