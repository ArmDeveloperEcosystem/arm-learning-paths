"""Acceptance tests. Keep this file outside the agent's writable directory."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import release_tool


class ReleaseTests(unittest.TestCase):
    def run_cli(self, statuses):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "results.json"
            source.write_text(json.dumps({"tests": [{"status": s} for s in statuses]}))
            completed = subprocess.run(
                [sys.executable, release_tool.__file__, str(source)],
                capture_output=True, text=True, check=False,
            )
        return completed.returncode, json.loads(completed.stdout)

    def test_all_passed_can_release(self):
        code, result = self.run_cli(["passed", "passed"])
        self.assertTrue(result["ready"])
        self.assertEqual(code, 0)

    def test_failure_blocks_release(self):
        code, result = self.run_cli(["passed", "failed", "skipped"])
        self.assertEqual((result["passed"], result["failed"], result["skipped"]), (1, 1, 1))
        self.assertFalse(result["ready"])
        self.assertEqual(code, 1)

    def test_only_skipped_blocks_release(self):
        code, result = self.run_cli(["skipped"])
        self.assertFalse(result["ready"])
        self.assertEqual(code, 1)

    def test_no_tests_blocks_release(self):
        code, result = self.run_cli([])
        self.assertFalse(result["ready"])
        self.assertEqual(code, 1)


if __name__ == "__main__":
    unittest.main()
