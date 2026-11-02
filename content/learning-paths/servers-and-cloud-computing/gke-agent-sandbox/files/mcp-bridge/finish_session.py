#!/usr/bin/env python3
"""Preserve bridge logs and release this MCP session's claim."""

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import shutil
import subprocess
import sys
import uuid

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from sandbox_common import CLAIMS, LABEL, Demo  # noqa: E402


def owned_session(record_path, keep_claim):
    record = json.loads(record_path.read_text())
    if record.get("mode") != "agy MCP; fresh code generation" or not record.get("run_id"):
        raise ValueError("Use a run.json created by prepare_session.py")
    # Verify the claim still exists and belongs to this session.
    cmd = ["kubectl", "--context", record["context"], "--namespace", record["namespace"],
           "--request-timeout=55s", "get", CLAIMS, record["claim_name"], "-o", "json"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode:
        raise RuntimeError(f"Could not retrieve claim: {result.stderr.strip()}")
    claim = json.loads(result.stdout)
    if (claim["metadata"]["uid"] != record["binding"]["claim_uid"]
            or claim["metadata"].get("labels", {}).get(LABEL) != record["run_id"]):
        raise RuntimeError("Refusing to operate on a replacement or unowned claim")
    demo = Demo.__new__(Demo)
    demo.args = argparse.Namespace(context=record["context"], namespace=record["namespace"],
                                   wait_timeout=180, keep_claim=keep_claim)
    demo.record, demo.output, demo.run_id = record, record_path.parent, record["run_id"]
    demo.claim_name, demo.workspace = record["claim_name"], record["workspace"]
    demo.creation_attempted, demo.claim = True, claim
    demo.sandbox = {"metadata": {"name": record["binding"]["sandbox"],
                                 "uid": record["binding"]["sandbox_uid"]}}
    demo.pod = {"metadata": {"name": record["binding"]["pod"],
                              "uid": record["binding"]["pod_uid"]}}
    return demo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", required=True, type=Path)
    parser.add_argument("--keep-claim", action="store_true",
                        help="Preserve the claim without releasing it")
    args = parser.parse_args()
    record_path = args.record.resolve()
    demo = owned_session(record_path, args.keep_claim)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output = record_path.parent / ("finish-" + stamp)
    output.mkdir(parents=True)
    demo.record["status"] = "finished"
    for name in ("tool-calls.jsonl", "mcp-connection.json"):
        source = record_path.parent / name
        if source.is_file():
            shutil.copyfile(source, output / name)
    try:
        demo.cleanup()
    except Exception as error:
        demo.record.update(status="cleanup_failed", cleanup_error=str(error))
        raise
    finally:
        demo.record["finish_directory"] = str(output)
        demo.save()
        shutil.copyfile(record_path, output / "session-final.json")
    print(f"Session finished. Records preserved in: {output}")


if __name__ == "__main__":
    main()
