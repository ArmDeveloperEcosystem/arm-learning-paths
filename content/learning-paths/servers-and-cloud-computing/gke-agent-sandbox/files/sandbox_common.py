#!/usr/bin/env python3
"""Shared sandbox lifecycle helpers used by claim.py and csv-app/run_demo.py."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import uuid

CLAIMS = "sandboxclaims.extensions.agents.x-k8s.io"
POOLS = "sandboxwarmpools.extensions.agents.x-k8s.io"
SANDBOXES = "sandboxes.agents.x-k8s.io"
LABEL = "csv-demo-run"


class Demo:
    def __init__(self, args):
        self.args = args
        self.run_id = uuid.uuid4().hex[:12]
        self.claim_name = "csv-analysis-" + self.run_id  # may be overridden before allocate()
        self.workspace = "/workspace/csv-" + self.run_id
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        self.output = args.output_dir or Path(".") / "runs" / (stamp + "-" + self.run_id)
        self.output.mkdir(parents=True, exist_ok=False)
        self.claim = None
        self.sandbox = None
        self.pod = None
        self.creation_attempted = False
        self.record = {"started_utc": stamp, "context": args.context,
                       "namespace": args.namespace, "pool": args.pool,
                       "workspace": self.workspace,
                       "mode": "saved revisions; no live LLM", "steps": {}, "status": "running"}
        # claim_name written in allocate() so caller overrides take effect first

    def save(self):
        (self.output / "run.json").write_text(
            json.dumps(self.record, indent=2) + "\n", encoding="utf-8")

    def kubectl(self, *arguments, payload=None, timeout=60):
        command = ["kubectl", "--context", self.args.context, "--namespace", self.args.namespace,
                   f"--request-timeout={timeout - 5}s", *arguments]
        result = subprocess.run(command, input=payload, capture_output=True, text=True, timeout=timeout)
        if result.returncode:
            raise RuntimeError(f"kubectl {' '.join(arguments[:3])} failed:\n{result.stderr.strip()}")
        return result.stdout

    def get(self, kind, name):
        output = self.kubectl("get", kind, name, "--ignore-not-found", "-o", "json")
        return json.loads(output) if output.strip() else None

    def require(self, kind, name):
        result = self.get(kind, name)
        if not result:
            raise RuntimeError(f"Missing {kind}/{name}")
        return result

    @staticmethod
    def owned_by(child, parent):
        return any(owner["uid"] == parent["metadata"]["uid"]
                   for owner in child["metadata"].get("ownerReferences", []))

    def wait(self, condition, resource):
        self.kubectl("wait", f"--for={condition}", resource,
                     f"--timeout={self.args.wait_timeout}s",
                     timeout=self.args.wait_timeout + 30)

    def remote(self, action, files=None, remote_worker_src=None):
        if remote_worker_src is None:
            raise ValueError("remote_worker_src must be provided")
        output = self.kubectl(
            "exec", "-i", self.pod["metadata"]["name"], "-c", "runtime", "--",
            "python3", "-c", remote_worker_src, self.workspace, action,
            payload=json.dumps(files) if files is not None else "", timeout=60)
        return json.loads(output)

    def allocate(self, remote_worker_src=None):
        """Allocate and verify a claim without uploading or running an application."""
        self.record["claim_name"] = self.claim_name  # capture after any caller override
        print(f"Context: {self.args.context}\nNamespace: {self.args.namespace}\n"
              f"Pool: {self.args.pool}", flush=True)
        self.require(POOLS, self.args.pool)
        self.record["kubectl_client"] = json.loads(
            self.kubectl("version", "--client", "-o", "json"))["clientVersion"]
        self.record["client_python"] = sys.version.split()[0]
        manifest = {
            "apiVersion": "extensions.agents.x-k8s.io/v1beta1", "kind": "SandboxClaim",
            "metadata": {"name": self.claim_name, "namespace": self.args.namespace,
                         "labels": {LABEL: self.run_id}},
            "spec": {"warmPoolRef": {"name": self.args.pool}},
        }
        started = time.monotonic()
        self.creation_attempted = True
        self.claim = json.loads(
            self.kubectl("create", "-f", "-", "-o", "json", payload=json.dumps(manifest)))
        print(f"Created claim: {self.claim_name}; waiting for Ready…", flush=True)
        self.wait("condition=Ready", f"{CLAIMS}/{self.claim_name}")
        self.claim = self.require(CLAIMS, self.claim_name)
        name = self.claim.get("status", {}).get("sandbox", {}).get("name")
        if not name:
            raise RuntimeError("Ready claim has no status.sandbox.name")
        self.sandbox = self.require(SANDBOXES, name)
        if not self.owned_by(self.sandbox, self.claim):
            raise RuntimeError("Sandbox owner UID does not match this claim")
        selector = self.sandbox.get("status", {}).get("selector")
        if not selector:
            raise RuntimeError("Sandbox has no status.selector")
        pods = json.loads(
            self.kubectl("get", "pods", "-l", selector, "-o", "json"))["items"]
        if len(pods) != 1 or not self.owned_by(pods[0], self.sandbox):
            raise RuntimeError("Expected exactly one Pod owned by the claimed Sandbox")
        self.pod = pods[0]
        self.wait("condition=Ready", "pod/" + self.pod["metadata"]["name"])
        ready_pod = self.require("pod", self.pod["metadata"]["name"])
        if (ready_pod["metadata"]["uid"] != self.pod["metadata"]["uid"]
                or not self.owned_by(ready_pod, self.sandbox)):
            raise RuntimeError("Pod binding changed while waiting for readiness")
        self.pod = ready_pod
        if self.pod["spec"].get("runtimeClassName") != "gvisor":
            raise RuntimeError("Claimed Pod does not use RuntimeClass gvisor")
        self.record["claim_to_pod_ready_seconds"] = round(time.monotonic() - started, 3)
        self.record["binding"] = {
            "claim_uid": self.claim["metadata"]["uid"], "sandbox": name,
            "sandbox_uid": self.sandbox["metadata"]["uid"],
            "pod": self.pod["metadata"]["name"],
            "pod_uid": self.pod["metadata"]["uid"],
            "node": self.pod["spec"].get("nodeName"),
            "runtime_class": self.pod["spec"]["runtimeClassName"],
            "container_statuses": [
                {key: entry.get(key) for key in ("name", "image", "imageID", "restartCount")}
                for entry in self.pod["status"].get("containerStatuses", [])],
        }
        if remote_worker_src:
            info = self.remote("info", remote_worker_src=remote_worker_src)["environment"]
            self.record["environment"] = info
            if info["architecture"] not in {"aarch64", "arm64"} or info["uid"] == 0:
                raise RuntimeError(f"Expected Arm and non-root execution, got {info}")
            print(f"Bound Pod: {self.pod['metadata']['name']} "
                  f"({info['architecture']}, UID {info['uid']})", flush=True)
        else:
            print(f"Bound Pod: {self.pod['metadata']['name']}", flush=True)

    def cleanup(self):
        if not self.creation_attempted:
            self.record["cleanup"] = "no claim created"
            return
        claim = self.get(CLAIMS, self.claim_name)
        if claim:
            if claim["metadata"].get("labels", {}).get(LABEL) != self.run_id:
                raise RuntimeError(
                    "Refusing to delete a claim without this run's identifying label")
            if self.claim and claim["metadata"]["uid"] != self.claim["metadata"]["uid"]:
                raise RuntimeError(
                    "Refusing to delete a replacement claim with a different UID")
            if getattr(self.args, "keep_claim", False):
                self.record["cleanup"] = "claim retained"
                print(f"Retained claim: {self.claim_name}", flush=True)
                return
            self.kubectl("delete", CLAIMS, self.claim_name, "--wait=false")
            self.wait("delete", f"{CLAIMS}/{self.claim_name}")
        for kind, resource in ((SANDBOXES, self.sandbox), ("pod", self.pod)):
            if resource:
                self.wait("delete", f"{kind}/{resource['metadata']['name']}")
        self.record["cleanup"] = (
            "claim removed; deletion confirmed for discovered Sandbox and Pod")
        print("Cleanup: claim removed" +
              ("; bound Sandbox and Pod deleted." if self.pod else "."), flush=True)


FILES = ("analyze_sales.py", "sales.csv", "test_sales.py",
         "reports/summary.json", "reports/report.html")
DOWNLOAD = '''
import json, sys
from pathlib import Path
w = Path(sys.argv[1])
if w.parent != Path("/workspace") or not w.name.startswith("csv-"):
    raise ValueError("Expected a CSV task directory under /workspace")
result = {}
for name in json.loads(sys.argv[2]):
    file = (w / name).resolve()
    if not file.is_relative_to(w.resolve()):
        raise ValueError("Artifact path escapes the task workspace")
    if file.stat().st_size > 262144:
        raise ValueError("Artifact exceeds the 256 KiB collection limit")
    result[name] = file.read_text(encoding="utf-8")
print(json.dumps(result))
'''


class Collector:
    def __init__(self, record):
        self.record = record
        self.pod_name = record["binding"]["pod"]

    def kubectl(self, *arguments):
        command = ["kubectl", "--context", self.record["context"],
                   "--namespace", self.record["namespace"],
                   "--request-timeout=55s", *arguments]
        process = subprocess.run(command, capture_output=True, text=True, timeout=60)
        if process.returncode:
            raise RuntimeError(process.stderr.strip() or "kubectl failed")
        return process.stdout

    def get(self, kind, name):
        return json.loads(self.kubectl("get", kind, name, "-o", "json"))

    def check_binding(self):
        binding = self.record["binding"]
        claim = self.get(CLAIMS, self.record["claim_name"])
        sandbox = self.get(SANDBOXES, binding["sandbox"])
        pod = self.get("pod", self.pod_name)
        if (claim["metadata"]["uid"] != binding["claim_uid"]
                or sandbox["metadata"]["uid"] != binding["sandbox_uid"]
                or pod["metadata"]["uid"] != binding["pod_uid"]
                or claim.get("status", {}).get("sandbox", {}).get("name") != binding["sandbox"]
                or not Demo.owned_by(sandbox, claim)
                or not Demo.owned_by(pod, sandbox)
                or pod["spec"].get("runtimeClassName") != "gvisor"):
            raise RuntimeError(
                "Live claim/Sandbox/Pod binding does not match the retained setup record")
        return pod
