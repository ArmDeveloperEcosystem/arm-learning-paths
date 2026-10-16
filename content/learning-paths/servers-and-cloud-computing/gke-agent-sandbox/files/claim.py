#!/usr/bin/env python3
"""Create, verify, or delete one sandbox claim on an existing warm pool."""

import argparse
import json
from pathlib import Path
import shlex
import sys

from sandbox_common import Demo, CLAIMS


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="action", required=True)
    create = commands.add_parser("create")
    create.add_argument("--context", required=True)
    create.add_argument("--namespace", required=True)
    create.add_argument("--pool", default="axion-python-pool")
    create.add_argument("--purpose", choices=("smoke", "shell"), required=True)
    create.add_argument("--output-dir", required=True, type=Path)
    create.add_argument("--wait-timeout", type=int, default=180)
    for action in ("check", "delete"):
        command = commands.add_parser(action)
        command.add_argument("--record", required=True, type=Path)
    args = parser.parse_args()

    if args.action == "create":
        args.keep_claim = True
        args.pool = getattr(args, "pool", "axion-python-pool")
        demo = Demo(args)
        demo.claim_name = args.purpose + "-" + demo.run_id
        try:
            demo.allocate()
            demo.record["mode"] = "interactive inspection"
            demo.record["status"] = "prepared"
            binding = demo.record["binding"]
            values = {
                "CLAIM_NAME": demo.claim_name,
                "SANDBOX_NAME": binding["sandbox"],
                "POD_NAME": binding["pod"],
                "POD_UID": binding["pod_uid"],
            }
            (demo.output / "binding.env").write_text(
                "".join(f"export {k}={shlex.quote(v)}\n" for k, v in values.items()))
        except (Exception, KeyboardInterrupt):
            args.keep_claim = False
            demo.cleanup()
            raise
        finally:
            demo.save()
        print(f"Record: {demo.output.resolve() / 'run.json'}")
        return

    record = json.loads(args.record.read_text())
    if record.get("mode") != "interactive inspection":
        raise ValueError("Use an inspection record created by this helper")

    # Verify the binding is still intact.
    import subprocess
    def kubectl(*arguments):
        cmd = ["kubectl", "--context", record["context"], "--namespace", record["namespace"],
               "--request-timeout=55s", *arguments]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode:
            raise RuntimeError(result.stderr.strip() or "kubectl failed")
        return result.stdout

    def get(kind, name):
        return json.loads(kubectl("get", kind, name, "-o", "json"))

    def check_binding():
        b = record["binding"]
        claim = get(CLAIMS, record["claim_name"])
        pod = get("pod", b["pod"])
        if (claim["metadata"]["uid"] != b["claim_uid"]
                or pod["metadata"]["uid"] != b["pod_uid"]):
            raise RuntimeError("Live claim/Pod binding does not match the record")

    check_binding()

    if args.action == "check":
        b = record["binding"]
        print(f"Verified binding: {b['pod']} UID {b['pod_uid']}")
        return

    # delete action
    import argparse as _ap
    demo = Demo.__new__(Demo)
    demo.args = _ap.Namespace(
        context=record["context"], namespace=record["namespace"],
        wait_timeout=180, keep_claim=False)
    demo.record, demo.output = record, args.record.resolve().parent
    demo.claim_name = record["claim_name"]
    demo.workspace = record["workspace"]
    demo.run_id = demo.claim_name.rsplit("-", 1)[1]
    demo.creation_attempted = True
    demo.claim = get(CLAIMS, demo.claim_name)
    demo.sandbox = {"metadata": {"name": record["binding"]["sandbox"],
                                 "uid": record["binding"]["sandbox_uid"]}}
    demo.pod = {"metadata": {"name": record["binding"]["pod"],
                              "uid": record["binding"]["pod_uid"]}}
    try:
        demo.cleanup()
        demo.record["status"] = "closed"
    finally:
        demo.save()


if __name__ == "__main__":
    main()
