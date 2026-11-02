"""Trusted transport helper, sent by the client to Python inside the claimed Pod."""

import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys


def main():
    workspace = Path(sys.argv[1])
    action = sys.argv[2]
    if workspace.parent != Path("/workspace") or not workspace.name.startswith("csv-"):
        raise ValueError("Expected a task directory directly under /workspace")
    result = {}
    if action == "write":
        files = json.load(sys.stdin)
        if not files or not set(files) <= {"sales.csv", "analyze_sales.py", "test_sales.py"}:
            raise ValueError("Unexpected upload filename")
        workspace.mkdir(exist_ok=True)
        for name, contents in files.items():
            (workspace / name).write_text(contents, encoding="utf-8")
    elif action in {"initial", "corrected", "checks"}:
        arguments = {
            "initial": ["analyze_sales.py", "sales.csv"],
            "corrected": ["analyze_sales.py", "sales.csv", "--output-dir", "reports"],
            "checks": ["-m", "unittest", "-v", "test_sales"],
        }[action]
        try:
            process = subprocess.run([sys.executable, *arguments], cwd=workspace,
                                     capture_output=True, text=True, timeout=30)
            result = {"returncode": process.returncode, "stdout": process.stdout,
                      "stderr": process.stderr, "timed_out": False}
        except subprocess.TimeoutExpired as error:
            def decode(value):
                return value.decode(errors="replace") if isinstance(value, bytes) else value or ""
            result = {"returncode": None, "stdout": decode(error.stdout),
                      "stderr": decode(error.stderr), "timed_out": True}
    elif action == "collect":
        result = {name: (workspace / "reports" / name).read_text(encoding="utf-8")
                  for name in ("summary.json", "report.html")}
    elif action != "info":
        raise ValueError("Unknown worker action")
    result["environment"] = {"architecture": platform.machine(), "uid": os.getuid(),
                             "python": platform.python_version(), "workspace": str(workspace)}
    result["input_sha256"] = (hashlib.sha256((workspace / "sales.csv").read_bytes()).hexdigest()
                               if (workspace / "sales.csv").exists() else None)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
