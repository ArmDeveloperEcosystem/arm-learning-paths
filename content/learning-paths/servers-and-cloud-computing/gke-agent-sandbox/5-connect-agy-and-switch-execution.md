---
title: Connect Antigravity CLI and run code in the sandbox
description: Install the Antigravity CLI, connect it to a GKE sandbox through an MCP bridge, and run agent-generated Python remotely.
weight: 7
layout: learningpathall
---

## What this page does

You install the Antigravity CLI, connect it to your GKE sandbox, and prompt it to write and run a Python program. The code runs inside the sandbox on the remote Arm node, not on your local machine. You verify this by checking that the output shows the remote Linux environment.

## Install the Antigravity CLI

Download the files needed for this page:

```bash
cd "$LP_WORKDIR"
BASE_URL=https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/servers-and-cloud-computing/gke-agent-sandbox/files/mcp-bridge
for FILE in \
  bridge.py \
  server.py \
  remote_tools.py \
  prepare_session.py \
  verify_connection.py \
  capture_hello.py \
  finish_session.py \
  requirements.txt; do
  mkdir -p mcp-bridge
  curl -fL "$BASE_URL/$FILE" -o "mcp-bridge/$FILE" || exit 1
done
```

If `agy` is not installed, run the official installer. It works on both macOS and Arm Linux and automatically detects your architecture:

```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash
```

Add `agy` to your `PATH` and verify the installation:

```bash
export PATH="$HOME/.local/bin:$PATH"
agy --version
```

Add the `export` line to your shell startup file (`~/.zshrc` on macOS, `~/.bashrc` on Linux) to make it permanent.

Before continuing, sign in to authenticate `agy` with your Google account:

```bash
agy
```

On your local machine this opens a browser for Google Sign-In. On a remote or SSH session it prints a URL. Copy it and open it in your local browser to complete the login. Once authenticated, type `/exit` to close `agy` and return to your terminal.

For an existing installation, run `agy update` to get the latest version. See the [Antigravity CLI install guide](/install-guides/antigravity/) for more details.

## Set up the MCP bridge

The MCP bridge is a Python script that runs on your local machine and forwards `agy`'s tool calls to the sandbox Pod using kubectl. Create a virtual environment for it and install its dependencies:

```bash
python3 -m venv mcp-bridge/.venv
source mcp-bridge/.venv/bin/activate
pip install -r mcp-bridge/requirements.txt
```

Create a sandbox claim and prepare the `agy` workspace:

```bash
export AGY_SESSION="$LP_WORKDIR/runs/agy"
export AGY_RECORD="$AGY_SESSION/run.json"
export AGY_CLIENT="$AGY_SESSION/client"
rm -rf "$AGY_SESSION"
python3 mcp-bridge/prepare_session.py \
  --context "$GKE_CONTEXT" --namespace "$NAMESPACE" --pool axion-python-pool \
  --output-dir "$AGY_SESSION"
```

`prepare_session.py` creates a sandbox claim, waits for the Pod to be ready, and writes the MCP configuration that tells `agy` which Pod to use.

Verify the connection:

```bash
python3 mcp-bridge/verify_connection.py --record "$AGY_RECORD"
```

The expected output confirms the MCP tools are available and identifies the remote Pod:

```output
MCP connected: environment, execute_command, list_files, read_file, write_file
GKE: aarch64 UID 1000; Pod <claim-bound-pod>
```

If the connection fails, check that `GKE_CONTEXT`, `NAMESPACE`, and the cluster credentials are still set correctly, then re-run `prepare_session.py` to create a new claim.

## Configure agy permissions and run code remotely

Start a new `agy` project in the prepared workspace:

```bash
cd "$AGY_CLIENT"
agy --new-project
```

Use `/mcp` to confirm that `gke-sandbox` is connected with the five tools listed above.

Open `/permissions`, select **Project**, and set these rules to allow the GKE tools and block built-in local execution:

| List | Rule |
| --- | --- |
| Allow | `mcp(gke-sandbox/*)` |
| Deny | `command(*)` |
| Deny | `read_file(*)` |
| Deny | `write_file(*)` |

Enter this prompt:

```text
Write hello.py using only Python's standard library. Print "Hello, World!",
the operating system, machine architecture, user ID, working directory,
Python version, and kernel release. Print available Linux distribution
information from /etc/os-release, or the macOS version when running on macOS.
Handle missing platform-specific files gracefully. Run the program and show
its actual output and exit code.
```

Watch that `agy` uses `gke-sandbox` `write_file` and `execute_command` tools rather than its built-in local tools. The output should show Linux, `aarch64`, UID `1000`, and a gVisor kernel, confirming the code ran in the remote sandbox:

```output
Hello, World!
Operating System: Linux
Machine Architecture: aarch64
User ID: 1000
Working Directory: /workspace/csv-<task-id>
Python Version: 3.12.15
Kernel Release: 4.19.0-gvisor
Linux Distribution Information (/etc/os-release):
NAME: Debian GNU/Linux
PRETTY_NAME: Debian GNU/Linux 12 (bookworm)
VERSION_ID: 12
...
```

Save the conversation using `agy`'s conversation controls, then enter `/exit`.

## Capture the result

Back in your terminal, capture the remote execution result:

```bash
cd "$LP_WORKDIR"
python3 mcp-bridge/capture_hello.py --record "$AGY_RECORD" --label remote-first
```

This runs `hello.py` in the recorded Pod one more time and saves the source, output, and a SHA-256 hash to `$AGY_SESSION/remote-first/` for your records.

## What you've accomplished and what's next

You've connected the Antigravity CLI to a GKE sandbox through an MCP bridge and verified that agent-generated Python ran remotely on Arm with gVisor isolation. Next, preserve your results and remove the cloud resources.
