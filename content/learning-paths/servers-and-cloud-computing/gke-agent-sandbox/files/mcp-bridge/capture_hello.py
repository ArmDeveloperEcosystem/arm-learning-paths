#!/usr/bin/env python3
"""Preserve remote Hello World source/output and optionally copy source to the local project."""

import argparse
import hashlib
import json
from pathlib import Path

from bridge import Bridge


def capture(record_path, label, copy_local):
    record_path = record_path.resolve()
    bridge = Bridge(record_path)
    output = record_path.parent / label
    if output.exists():
        raise FileExistsError(f"Preserve or rename the existing capture first: {output}")
    destination = Path(bridge.record["client_workspace"]) / "hello.py"
    if copy_local and (label != "remote-first" or destination.exists()):
        raise ValueError("Copy only the first pass into a new local hello.py")
    before = bridge.invoke("read_file", path="hello.py")
    data = before["content"].encode("utf-8")
    digest = hashlib.sha256(data).hexdigest()
    if label == "remote-return":
        original = (record_path.parent / "remote-first" / "hello.py").read_bytes()
        if data != original:
            raise ValueError("Remote source changed since the first capture")
    result = bridge.invoke("execute_command", command="python3 hello.py", cwd=".", timeout=30)
    after = bridge.invoke("read_file", path="hello.py")
    if before["sha256"] != after["sha256"]:
        raise ValueError("Source changed during execution")
    if result["returncode"] != 0 or result["timed_out"] or any(
            result[key] for key in ("stdout_truncated", "stderr_truncated")):
        raise RuntimeError(f"Remote run did not complete successfully: {result}")
    output.mkdir()
    (output / "hello.py").write_bytes(data)
    (output / "source.sha256").write_text(digest + "\n")
    (output / "stdout.txt").write_text(result["stdout"])
    (output / "execution.json").write_text(json.dumps(result, indent=2) + "\n")
    if copy_local:
        with destination.open("xb") as stream:
            stream.write(data)
        print(f"Copied source for the intentional local pass: {destination}")
    print(result["stdout"], end="")
    print(f"Source SHA-256: {digest}\nEvidence: {output}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", required=True, type=Path)
    parser.add_argument("--label", required=True, choices=("remote-first", "remote-return"))
    parser.add_argument("--copy-local", action="store_true")
    args = parser.parse_args()
    capture(args.record, args.label, args.copy_local)


if __name__ == "__main__":
    main()
