"""Run: python -m unittest discover -s integrations/3d-space/tests -v (from repo root)."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
import trimesh

BASE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('openplan_to_glb',BASE/'scripts/openplan_to_glb.py')
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class ConverterTests(unittest.TestCase):
    def test_example_gallery_exports_glb_and_audit(self):
        with TemporaryDirectory() as d:
            out=Path(d)/'gallery.glb'
            audit=mod.convert(BASE/'examples/example-gallery.openplan.json',out)
            self.assertTrue(out.is_file())
            self.assertGreater(out.stat().st_size,1000)
            self.assertEqual(audit['summary']['walls'],5)
            self.assertEqual(audit['summary']['windows'],1)
            self.assertEqual(audit['summary']['doors'],2)
            self.assertTrue(out.with_suffix('.audit.json').exists())
            glb=trimesh.load(out,force='scene')
            self.assertEqual(len(glb.geometry),audit['geometries'])
            self.assertAlmostEqual(glb.bounds[1][0],10.1,places=3)
    def test_reject_bad_opening(self):
        with TemporaryDirectory() as d:
            data=json.loads((BASE/'examples/example-gallery.openplan.json').read_text(encoding='utf8'))
            data['floors'][0]['doors'][0]['width']=100000
            inp=Path(d)/'bad.json';inp.write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError,'opening extends beyond wall'):
                mod.convert(inp,Path(d)/'bad.glb')
    def test_reject_curved_walls_rather_than_silently_flatten(self):
        with TemporaryDirectory() as d:
            data=json.loads((BASE/'examples/example-gallery.openplan.json').read_text(encoding='utf8'))
            data['floors'][0]['walls'][0]['curvePoint']={'x':500,'y':200}
            inp=Path(d)/'bad.json';inp.write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError,'curved walls unsupported'):
                mod.convert(inp,Path(d)/'bad.glb')
if __name__=='__main__': unittest.main()
