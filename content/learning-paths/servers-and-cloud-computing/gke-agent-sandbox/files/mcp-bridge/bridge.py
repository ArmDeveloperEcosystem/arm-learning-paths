"""Claim-bound kubectl transport. There is no local command execution backend."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import threading
import uuid

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from sandbox_common import Collector  # noqa: E402


class Bridge(Collector):
    def __init__(self, record_path):
        super().__init__(json.loads(Path(record_path).read_text(encoding="utf-8")))
        self.audit = Path(record_path).resolve().parent / "tool-calls.jsonl"
        self.lock = threading.Lock()

    def invoke(self, action, **arguments):
        with self.lock:
            request = {"action": action, **arguments}
            logged = dict(request)
            if "content" in logged:
                data = logged.pop("content").encode("utf-8")
                logged.update(content_sha256=hashlib.sha256(data).hexdigest(), content_bytes=len(data))
            event = {"call_id": uuid.uuid4().hex, "utc": datetime.now(timezone.utc).isoformat(), "request": logged,
                     "binding": self.record["binding"], "status": "started"}
            self.append(event)
            try:
                self.check_binding()
                command = ["kubectl", "--context", self.record["context"], "--namespace", self.record["namespace"],
                           "--request-timeout=45s", "exec", "-i", self.pod_name, "-c", "runtime", "--",
                           "python3", "-c", (HERE / "remote_tools.py").read_text(encoding="utf-8"),
                           self.record["workspace"]]
                process = subprocess.run(command, input=json.dumps(request), capture_output=True,
                                         text=True, timeout=50)
                if process.returncode:
                    raise RuntimeError(process.stderr.strip() or "Remote transport failed")
                result = json.loads(process.stdout)
                self.check_binding()
                result["binding"] = self.record["binding"]
                event.update(status="completed", result=result)
                self.append(event)
                return result
            except Exception as error:
                event.update(status="failed", error=str(error))
                self.append(event)
                raise RuntimeError(f"GKE operation failed; no local fallback: {error}") from error

    def append(self, event):
        with self.audit.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(event) + "\n")
