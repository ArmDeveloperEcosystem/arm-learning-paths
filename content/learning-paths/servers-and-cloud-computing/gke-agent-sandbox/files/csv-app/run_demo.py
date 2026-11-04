#!/usr/bin/env python3
"""Run saved CSV-app revisions in a new claim on an existing GKE warm pool."""

import argparse
import json
import os
from pathlib import Path
import shutil
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from sandbox_common import Demo, CLAIMS, POOLS, SANDBOXES, LABEL  # noqa: E402


class CsvDemo(Demo):
    """Extends Demo with CSV-specific run, upload, and collect steps."""

    def run(self):
        remote_worker = (HERE / "remote_worker.py").read_text()
        self.allocate(remote_worker_src=remote_worker)
        self.record["source_sha256"] = {
            name: __import__("hashlib").sha256((HERE / name).read_bytes()).hexdigest()
            for name in ("sales.csv", "analyze_sales_initial.py",
                         "analyze_sales.py", "test_sales.py", "remote_worker.py")
        }
        self.remote("write", {
            "sales.csv": (HERE / "sales.csv").read_text(),
            "test_sales.py": (HERE / "test_sales.py").read_text(),
            "analyze_sales.py": (HERE / "analyze_sales_initial.py").read_text(),
        }, remote_worker_src=remote_worker)
        initial = self.remote("initial", remote_worker_src=remote_worker)
        self.record["steps"]["initial"] = initial
        self.save()
        if initial["timed_out"] or initial["returncode"] == 0 or "ValueError" not in initial["stderr"]:
            raise RuntimeError("Initial revision did not produce the expected ValueError")
        print("Initial revision failed as expected:", flush=True)
        print(initial["stderr"].rstrip(), flush=True)
        self.remote("write", {
            "analyze_sales.py": (HERE / "analyze_sales.py").read_text(),
        }, remote_worker_src=remote_worker)
        for action in ("corrected", "checks"):
            result = self.remote(action, remote_worker_src=remote_worker)
            self.record["steps"][action] = result
            self.save()
            if result["timed_out"] or result["returncode"] != 0:
                raise RuntimeError(f"{action} failed:\n{result['stderr']}")
            if result["input_sha256"] != initial["input_sha256"]:
                raise RuntimeError("CSV changed between revisions")
        print(self.record["steps"]["checks"]["stderr"].rstrip(), flush=True)
        artifacts = self.remote("collect", remote_worker_src=remote_worker)
        for filename in ("summary.json", "report.html"):
            (self.output / filename).write_text(artifacts[filename], encoding="utf-8")
        summary = json.loads(artifacts["summary.json"])
        if (summary["net_revenue"], summary["accepted_rows"], summary["rejected_rows"]) != ("328.41", 9, 3):
            raise RuntimeError("Downloaded report does not match the expected result")
        self.record["status"] = "passed"
        print(f"Report: net revenue ${summary['net_revenue']}; "
              f"{summary['accepted_rows']} accepted, {summary['rejected_rows']} rejected", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--context", required=True)
    parser.add_argument("--namespace", default=os.environ.get("NAMESPACE", "axion-sandbox-prototype"))
    parser.add_argument("--pool", default="axion-python-pool")
    parser.add_argument("--wait-timeout", type=int, default=180)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--keep-claim", action="store_true")
    args = parser.parse_args()
    if not args.context.strip() or args.wait_timeout <= 0:
        parser.error("Context must be nonempty and wait timeout must be positive")
    if not shutil.which("kubectl"):
        parser.error("kubectl is required on PATH")
    demo = CsvDemo(args)
    status = 0
    try:
        demo.run()
    except (Exception, KeyboardInterrupt) as error:
        status = 1
        demo.record["status"] = "failed"
        demo.record["error"] = str(error) or "Interrupted"
        print(f"ERROR: {demo.record['error']}", file=sys.stderr, flush=True)
    finally:
        try:
            demo.cleanup()
        except (Exception, KeyboardInterrupt) as error:
            status = 1
            demo.record["status"] = ("cleanup_failed" if demo.record["status"] == "passed"
                                     else "failed")
            demo.record["cleanup_error"] = str(error) or "Interrupted"
            print(f"CLEANUP ERROR: {demo.record['cleanup_error']}\n"
                  f"Inspect claim {demo.claim_name} in namespace {args.namespace}.",
                  file=sys.stderr, flush=True)
        demo.save()
        print(f"Artifacts and execution record: {demo.output.resolve()}", flush=True)
    return status


if __name__ == "__main__":
    raise SystemExit(main())
