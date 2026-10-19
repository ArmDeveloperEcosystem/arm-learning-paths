#!/usr/bin/env python3
"""Prepare a fresh GKE claim and isolated client workspace for an agy MCP experiment."""

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import uuid

from bridge import HERE
sys.path.insert(0, str(HERE.parent))
from sandbox_common import Demo  # noqa: E402

CSV = HERE.parent / "csv-app"

RULES = """# GKE task workspace

All task files and commands belong to the GKE workspace exposed by the
gke-sandbox MCP server. Use its environment, list_files, read_file, write_file,
and execute_command tools for generating, inspecting, running, and testing code.
Paths passed to these tools are relative to the remote workspace. The local
directory contains only client configuration; do not run or save task code here.
If remote tools are unavailable or fail, report the error and stop the task.
Check exit codes, timeout flags, and truncation flags; do not infer success.
Follow the user's requested task. For example, when asked to write and run a
hello-world Python program, write hello.py through MCP and run python3 hello.py
through MCP. Return its actual output and exit code. Do not require the user to
mention GKE, kubectl, or Pod names in each prompt.

The remote workspace initially contains optional sample files sales.csv and
test_sales.py. Use them only when the user requests the CSV analysis task.
For that task, read them through MCP before implementing analyze_sales.py.
Keep both sample files unchanged.
Implement analyze(rows) -> dict (rows is an iterable of CSV row dictionaries)
and render_report(summary) -> str so the existing
tests can import them. Provide CLI:
python3 analyze_sales.py sales.csv --output-dir reports
Write reports/summary.json and reports/report.html. Use Python's standard library
and Decimal for money. Handle invalid rows, refunds, duplicate orders, and HTML
escaping as specified by the tests. Run python3 -m unittest -v test_sales, then
generate and read both reports. For the CSV task, limit repair attempts to five
and finish with the test outcome, net revenue, accepted/rejected row counts,
and remote artifact paths. Other tasks do not need to implement or test the CSV app.
"""


def write_client(demo, mcp_python):
    client = demo.output.resolve() / "client"
    (client / ".agents").mkdir(parents=True)
    config = {"mcpServers": {"gke-sandbox": {
        # Keep the venv executable path: resolving its symlink bypasses the venv.
        "command": str(mcp_python.absolute()),
        "args": [str(HERE / "server.py"), "--record", str(demo.output.resolve() / "run.json")],
        "env": {key: os.environ[key] for key in
                ("PATH", "KUBECONFIG", "CLOUDSDK_CONFIG", "USE_GKE_GCLOUD_AUTH_PLUGIN") if key in os.environ},
    }}}
    (client / ".agents" / "mcp_config.json").write_text(json.dumps(config, indent=2) + "\n")
    (client / "AGENTS.md").write_text(RULES, encoding="utf-8")
    return client


def prepare(demo, mcp_python):
    remote_worker_src = (CSV / "remote_worker.py").read_text(encoding="utf-8")
    demo.record.update(mode="agy MCP; fresh code generation", run_id=demo.run_id)
    demo.allocate(remote_worker_src=remote_worker_src)
    seed_files = {name: (CSV / name).read_text(encoding="utf-8")
                  for name in ("sales.csv", "test_sales.py")}
    demo.remote("write", seed_files, remote_worker_src=remote_worker_src)
    import hashlib
    demo.record["source_sha256"] = {name: hashlib.sha256(content.encode("utf-8")).hexdigest()
                                    for name, content in seed_files.items()}
    demo.record["seeded_files"] = list(seed_files)
    client = write_client(demo, mcp_python)
    demo.record.update(status="prepared", client_workspace=str(client),
                       cleanup="claim retained for interactive MCP session")
    demo.save()
    return client


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--context", required=True)
    parser.add_argument("--namespace", default=os.environ.get("NAMESPACE", "axion-sandbox-prototype"))
    parser.add_argument("--pool", default="axion-python-pool")
    parser.add_argument("--wait-timeout", type=int, default=180)
    parser.add_argument("--output-dir", type=Path, help="New session directory")
    parser.add_argument("--mcp-python", type=Path, default=HERE / ".venv" / "bin" / "python")
    args = parser.parse_args()
    if not args.context.strip() or args.wait_timeout < 1:
        parser.error("Context must be nonempty and wait timeout must be positive")
    if not shutil.which("kubectl"):
        parser.error("kubectl is required on PATH")
    # Fail before allocating a claim if the MCP interpreter cannot import the pinned SDK.
    if not args.mcp_python.is_file():
        parser.error("Create mcp-bridge/.venv and install requirements.txt first")
    check = subprocess.run([str(args.mcp_python), "-c",
                            "from mcp.server.fastmcp import FastMCP; import importlib.metadata; "
                            "assert importlib.metadata.version('mcp') == '1.26.0'"],
                           capture_output=True, text=True, timeout=15)
    if check.returncode:
        parser.error("Install mcp==1.26.0 in the MCP interpreter before creating a session")
    args.keep_claim = True
    if args.output_dir is None:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        args.output_dir = HERE / "sessions" / (stamp + "-" + uuid.uuid4().hex[:8])
    demo = Demo(args)
    try:
        client = prepare(demo, args.mcp_python)
    except (Exception, KeyboardInterrupt) as error:
        demo.record.update(status="failed", error=str(error) or "Interrupted")
        args.keep_claim = False
        try:
            demo.cleanup()
        except Exception as cleanup_error:
            demo.record["cleanup_error"] = str(cleanup_error)
        demo.save()
        print(f"ERROR: {demo.record['error']}\nRecord: {demo.output.resolve() / 'run.json'}", file=sys.stderr)
        if "cleanup_error" in demo.record:
            print(f"CLEANUP ERROR: {demo.record['cleanup_error']}", file=sys.stderr)
        return 1
    record = demo.output.resolve() / "run.json"
    print(f"Session record: {record}\nClient workspace: {client}")
    print("From this authenticated terminal, verify MCP first:")
    print(shlex.join([str(args.mcp_python.absolute()), str(HERE / "verify_connection.py"), "--record", str(record)]))
    print("Then start a new agy project; configure Project permissions before the task:")
    print("cd " + shlex.quote(str(client)))
    print("agy --new-project")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
