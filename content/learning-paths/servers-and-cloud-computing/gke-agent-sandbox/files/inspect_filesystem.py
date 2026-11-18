"""Run inside the Pod to compare controlled writes to new probe files."""

import errno
from pathlib import Path
import uuid

name = "lp-probe-" + uuid.uuid4().hex + ".txt"
for directory, expected in (("/workspace", True), ("/tmp", True), ("/etc", False), ("/usr/local", False)):
    path = Path(directory) / name
    try:
        with path.open("x") as stream:
            stream.write("sandbox probe\n")
        assert path.read_text() == "sandbox probe\n"
    except OSError as error:
        if expected or error.errno not in (errno.EACCES, errno.EPERM, errno.EROFS):
            raise
        print(f"{directory}: denied (errno {error.errno}: {error.strerror})")
    else:
        path.unlink()
        if not expected:
            raise AssertionError(f"Unexpected writable system path: {directory}")
        print(f"{directory}: write/read/remove succeeded")
