---
title: Open a shell and inspect the sandbox
description: Open an interactive shell through kubectl, inspect the sandbox environment, and compare writable task paths with protected system paths.
weight: 6
layout: learningpathall
---

## Create a sandbox for interactive inspection

You don't need an SSH server or SSH keys inside the sandbox. `kubectl exec` uses your Kubernetes authentication to open a process in the selected container.

Download `inspect_filesystem.py` into your working directory:

```bash
cd "$LP_WORKDIR"
curl -fL https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/servers-and-cloud-computing/gke-agent-sandbox/files/inspect_filesystem.py \
  -o inspect_filesystem.py
```

Create a sandbox claim and wait for the Pod to be ready:

```bash
rm -rf "$LP_WORKDIR/runs/shell"
python3 claim.py create \
  --context "$GKE_CONTEXT" --namespace "$NAMESPACE" \
  --pool axion-python-pool --purpose shell --output-dir "$LP_WORKDIR/runs/shell"
```

Load the Pod name into your shell, verify the binding, then open a shell in the sandbox:

```bash
source "$LP_WORKDIR/runs/shell/binding.env"
python3 claim.py check --record "$LP_WORKDIR/runs/shell/run.json"
kubectl --context "$GKE_CONTEXT" -n "$NAMESPACE" exec -it "$POD_NAME" -c runtime -- /bin/sh
```

You now have a shell inside the sandbox. The next commands run inside the sandbox, not on your local machine.

## Inspect the user and Linux environment

Run these commands inside the sandbox shell:

```bash
id
uname -m
uname -sr
pwd
python3 --version
cat /etc/os-release
ls -la /workspace
```

Expected values include UID `1000`, architecture `aarch64`, working directory `/workspace`, Python `3.12.15`, and Debian GNU/Linux 12. The kernel release can include `gvisor`:

```output
uid=1000 gid=1000 groups=1000
aarch64
Linux 4.19.0-gvisor
/workspace
Python 3.12.15
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
...
total 4
drwxrwxrwt 2 root root   40 ...
drwxr-xr-x 2 root root 4096 ...
```

gVisor supplies an advertised kernel identity rather than reporting the node's real kernel version. The Debian release identifies the container's operating system environment.

Try CPU and memory information:

```bash
lscpu
head -n 12 /proc/meminfo
```

The CPU shows Neoverse-V2 with 2 cores, confirming this is a Google Axion node. Memory shows 512MB total, matching the `512Mi` limit set in the sandbox template.

Write a test file to the writable workspace, then leave the shell:

```bash
printf 'created in my sandbox shell\n' > /workspace/shell-marker.txt
cat /workspace/shell-marker.txt
exit
```

You return to your local machine terminal. Exiting the shell doesn't delete its Pod or claim.

## Compare filesystem writes

`inspect_filesystem.py` attempts to write a file to several paths in the sandbox and reports whether each write succeeded or was denied.

Review the script before running it:

```bash
cat inspect_filesystem.py
```

Run it from your local machine in the same Pod:

```bash
python3 claim.py check --record "$LP_WORKDIR/runs/shell/run.json"
kubectl --context "$GKE_CONTEXT" -n "$NAMESPACE" exec -i "$POD_NAME" -c runtime -- \
  python3 - < inspect_filesystem.py | tee "$LP_WORKDIR/output/filesystem-probes.txt"
```

The expected output is similar to this illustrative example; denied-write errno values and messages vary:

```output
/workspace: write/read/remove succeeded
/tmp: write/read/remove succeeded
/etc: denied (errno 13: Permission denied)
/usr/local: denied (errno 13: Permission denied)
```

The output shows which paths are writable and which are blocked. `/workspace` and `/tmp` succeed because they are writable volumes in the template. `/etc` and `/usr/local` are blocked because the root filesystem is read-only and the process runs as a non-root user.

## Verify sandbox configuration

Reconnect to confirm the test file is still there:

```bash
python3 claim.py check --record "$LP_WORKDIR/runs/shell/run.json"
kubectl --context "$GKE_CONTEXT" -n "$NAMESPACE" exec -it "$POD_NAME" -c runtime -- /bin/sh
```

Inside the sandbox, read and remove the test file. Check for the default service-account token:

```bash
cat /workspace/shell-marker.txt
rm /workspace/shell-marker.txt
if test -e /var/run/secrets/kubernetes.io/serviceaccount/token; then
  echo 'Unexpected: default service-account token exists'
else
  echo 'Default service-account token is absent'
fi
exit
```

The token should be absent. If it exists, stop and inspect the actual Pod configuration before continuing.

Save the Pod configuration and check the resource limits:

```bash
kubectl --context "$GKE_CONTEXT" -n "$NAMESPACE" get pod "$POD_NAME" -o yaml \
  > "$LP_WORKDIR/output/interactive-pod.yaml"
kubectl --context "$GKE_CONTEXT" -n "$NAMESPACE" get pod "$POD_NAME" \
  -o jsonpath='{.spec.runtimeClassName}{"\n"}{.spec.containers[0].resources.limits}{"\n"}'
```

Confirm RuntimeClass `gvisor` and limits `500m` CPU and `512Mi` memory.

## Release the inspection claim

Remove this claim when you're done:

```bash
python3 claim.py delete --record "$LP_WORKDIR/runs/shell/run.json"
```

Keep the cluster and warm pool running. The next page creates its own claim.

## What you've accomplished and what's next

You've inspected the environment interactively, verified permitted and denied writes, and confirmed the sandbox runs as a non-root user with the expected resource limits. Next, connect the Antigravity CLI to the sandbox and run agent-generated Python remotely.
