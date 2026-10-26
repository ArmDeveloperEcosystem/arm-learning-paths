"""Trusted helper transmitted to the Pod; generated commands run only there."""

import hashlib
import json
import os
from pathlib import Path
import platform
import signal
import subprocess
import sys
import tempfile

FILE_LIMIT = 262144
OUTPUT_LIMIT = 65536


def task_path(root, name):
    root = root.resolve()
    relative = Path(name)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("Use a relative path inside the task workspace")
    destination = (root / relative).resolve()
    if not destination.is_relative_to(root):
        raise ValueError("Path or symlink escapes the task workspace")
    return destination


def execute(root, command, cwd, timeout):
    if not isinstance(command, str) or not command.strip() or len(command.encode()) > FILE_LIMIT:
        raise ValueError("Expected a nonempty command of at most 256 KiB")
    if type(timeout) is not int or not 1 <= timeout <= 30:
        raise ValueError("Execution timeout must be between 1 and 30 seconds")
    directory = task_path(root, cwd)
    timed_out = False
    with tempfile.TemporaryFile() as stdout, tempfile.TemporaryFile() as stderr:
        process = subprocess.Popen(["/bin/sh", "-c", command], cwd=directory,
                                   stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr,
                                   start_new_session=True)
        try:
            process.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
        finally:
            # Also remove children left behind by a command whose shell exited.
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            process.wait()
        result = {"returncode": process.returncode, "timed_out": timed_out}
        for name, stream in (("stdout", stdout), ("stderr", stderr)):
            stream.seek(0)
            data = stream.read(OUTPUT_LIMIT + 1)
            result[name] = data[:OUTPUT_LIMIT].decode("utf-8", errors="replace")
            result[name + "_truncated"] = len(data) > OUTPUT_LIMIT
        return result


def dispatch(root, request):
    action = request["action"]
    if action == "execute_command":
        return execute(root, request["command"], request.get("cwd", "."), request.get("timeout", 30))
    if action == "environment":
        return {"architecture": platform.machine(), "uid": os.getuid(),
                "python": platform.python_version(), "workspace": str(root)}
    destination = task_path(root, request.get("path", "."))
    if action == "write_file":
        data = request["content"].encode("utf-8")
        if len(data) > FILE_LIMIT:
            raise ValueError("File exceeds the 256 KiB limit")
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
        return {"path": request["path"], "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
    if action == "read_file":
        with destination.open("rb") as stream:
            data = stream.read(FILE_LIMIT + 1)
        if len(data) > FILE_LIMIT:
            raise ValueError("File exceeds the 256 KiB limit")
        return {"path": request["path"], "content": data.decode("utf-8"),
                "sha256": hashlib.sha256(data).hexdigest()}
    if action == "list_files":
        entries = []
        with os.scandir(destination) as iterator:
            for entry in iterator:
                if len(entries) == 200:
                    return {"entries": entries, "truncated": True}
                entries.append({"name": entry.name, "directory": entry.is_dir(follow_symlinks=False),
                                "symlink": entry.is_symlink()})
        return {"entries": sorted(entries, key=lambda item: item["name"]), "truncated": False}
    raise ValueError("Unknown remote action")


def main():
    root = Path(sys.argv[1])
    if root.parent != Path("/workspace") or not root.name.startswith("csv-") or root.is_symlink():
        raise ValueError("Expected a real CSV task directory under /workspace")
    root = root.resolve(strict=True)
    print(json.dumps(dispatch(root, json.load(sys.stdin))))


if __name__ == "__main__":
    main()
