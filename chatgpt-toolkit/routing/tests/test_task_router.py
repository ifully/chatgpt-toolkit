"""Çevrimdışı, bağımlılıksız yönlendirme katmanı testleri."""

import json
from pathlib import Path
import subprocess
import sys
import unittest


ROUTING_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROUTING_DIR))
import task_router  # noqa: E402


class RouterTests(unittest.TestCase):
    def test_catalog_exact_95_unique(self):
        catalog, rules = task_router.load_data()
        self.assertEqual(len(catalog["tools"]), 95)
        self.assertGreaterEqual(len(rules), 15)
        self.assertEqual(len({x["repo"] for x in catalog["tools"]}), 95)

    def test_normalize_turkish(self):
        self.assertEqual(task_router.normalize("GÖRSEL İLETİŞİM TASARIMI"),
                         "gorsel iletisim tasarimi")
        self.assertEqual(task_router.normalize("TÜBİTAK / şûra"), "tubitak sura")

    def test_research_project(self):
        result = task_router.route("TÜBİTAK için bilimsel proje fikri ve hipotez üretelim")
        self.assertIn("research-ideation", [x["id"] for x in result["matched_rules"]])
        self.assertIn("AutoResearch/autora", [x["repo"] for x in result["recommendations"]])
        self.assertTrue(result["validation"])

    def test_reverse_engineering(self):
        result = task_router.route("İzinli tersine mühendislik ve firmware analizi")
        self.assertEqual(result["matched_rules"][0]["id"], "reverse-engineering")
        self.assertIn("NationalSecurityAgency/ghidra", [x["repo"] for x in result["recommendations"]])

    def test_graphic_design(self):
        result = task_router.route("Afiş tipografisi ve okunabilirlik deneyi planla")
        repos = [x["repo"] for x in result["recommendations"]]
        self.assertIn("fonttools/fonttools", repos)
        self.assertIn("psychopy/psychopy", repos)

    def test_unmatched_query_returns_no_installation_claims(self):
        result = task_router.route("xyzzy plugh flurp")
        self.assertEqual(result["recommendations"], [])
        self.assertFalse(result["matched_rules"])

    def test_probe_is_passive_and_not_verification(self):
        result = task_router.route("veri analizi", probe=True)
        self.assertTrue(result["recommendations"])
        for tool in result["recommendations"]:
            self.assertEqual(tool["runtime_status"], "not-verified")
            self.assertIn("environment_probe", tool)

    def test_round_robin_does_not_starve_second_intent(self):
        result = task_router.route("TÜBİTAK bilimsel proje fikri ve literatür tarama", limit=3)
        self.assertGreaterEqual(len(result["matched_rules"]), 2)
        recommendations = result["recommendations"]
        self.assertTrue(any(x["recommended_by"] == "literature-citations" for x in recommendations))

    def test_json_cli(self):
        proc = subprocess.run(
            [sys.executable, str(ROUTING_DIR / "task_router.py"),
             "Görsel algı deneyi", "--json", "--limit", "2"],
            capture_output=True, text=True, check=True,
        )
        data = json.loads(proc.stdout)
        self.assertEqual(len(data["recommendations"]), 2)
        self.assertTrue(all(t["runtime_status"] == "not-verified"
                            for t in data["recommendations"]))


if __name__ == "__main__":
    unittest.main()
