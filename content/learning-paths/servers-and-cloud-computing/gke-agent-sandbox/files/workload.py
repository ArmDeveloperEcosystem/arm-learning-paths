"""Run via kubectl exec stdin in the claimed Pod; writes one result artifact."""

import errno
import json
import os
import platform
from pathlib import Path

architecture = platform.machine()
assert architecture in {"aarch64", "arm64"}, architecture
assert os.getuid() != 0, "The workload must run as a non-root user"
assert not Path("/var/run/secrets/kubernetes.io/serviceaccount/token").exists()

# This is a controlled write to our own new filename, not an escape test.
try:
    Path("/etc/axion-prototype-denied.txt").write_text("probe\n")
except OSError as error:
    if error.errno not in {errno.EACCES, errno.EPERM, errno.EROFS}:
        raise
    denied_write = {"errno": error.errno, "reason": error.strerror}
else:
    raise AssertionError("The write outside the workspace unexpectedly succeeded")

result = {
    "architecture": architecture,
    "uid": os.getuid(),
    "sum_of_squares": sum(number * number for number in range(10)),
    "service_account_token_present": False,
    "denied_write": denied_write,
}
assert result["sum_of_squares"] == 285
Path("/workspace/result.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
