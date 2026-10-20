---
title: Connect Antigravity CLI and run code in the sandbox
description: Install the Antigravity CLI, connect it to a GKE sandbox through an MCP bridge, and run agent-generated Python remotely.
weight: 7
layout: learningpathall
---

## Install the Antigravity CLI

You'll now install the Antigravity CLI, connect it to your Google Kubernetes Engine (GKE) sandbox, and prompt it to write and run a Python program. The code runs inside the sandbox on the remote Arm node, not on your local machine. You'll verify this by checking that the output shows the remote Linux environment.

Start by downloading the code that you'll run:

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

If `agy` isn't installed, follow the instructions in the [Antigravity CLI install guide](/install-guides/antigravity/) to install the Antigravity CLI and add it to your `PATH` in `~/.zshrc` or  `~/.bashrc`. 

For an existing installation, run `agy update` to get the latest version. 

Sign in to authenticate `agy` with your Google account:

```bash
agy
```

On your local machine, this opens a browser for Google Sign-In. 

On a remote or SSH session, it prints a URL. Copy the URL and open it in your local browser to complete the login. 

After authenticating, type `/exit` to close `agy` and return to your terminal.

## Set up the MCP bridge

The Model Context Protocol (MCP) bridge is a Python script that runs on your local machine and forwards the `agy` tool calls to the sandbox Pod using `kubectl`.

Create a virtual environment for the bridge and install its dependencies:

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

The expected output is:

```output
MCP connected: environment, execute_command, list_files, read_file, write_file
GKE: aarch64 UID 1000; Pod <claim-bound-pod>
```

The output identifies the remote Pod and confirms that the MCP tools are available.

If the connection fails, check that `GKE_CONTEXT`, `NAMESPACE`, and the cluster credentials are still set correctly, then re-run `prepare_session.py` to create a new claim.

## Configure agy permissions and run code remotely

Start a new `agy` project in the prepared workspace:

```bash
cd "$AGY_CLIENT"
agy --new-project
```

Use `/mcp` to confirm that `gke-sandbox` is connected with the five tools listed earlier.

Open `/permissions`, select **Project**, and set the following rules to allow the GKE tools and block built-in local execution:

| List | Rule |
| --- | --- |
| Allow | `mcp(gke-sandbox/*)` |
| Deny | `command(*)` |
| Deny | `read_file(*)` |
| Deny | `write_file(*)` |

Enter the following prompt:

```text
Write hello.py using only Python's standard library. Print "Hello, World!",
the operating system, machine architecture, user ID, working directory,
Python version, and kernel release. Print available Linux distribution
information from /etc/os-release, or the macOS version when running on macOS.
Handle missing platform-specific files gracefully. Run the program and show
its actual output and exit code.
```

Watch that `agy` uses `gke-sandbox` `write_file` and `execute_command` tools rather than its built-in local tools.

The expected output is:

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

The output including Linux, `aarch64`, UID `1000`, and a gVisor kernel confirms that the code ran in the remote sandbox.

Save the conversation using `agy` conversation controls, then enter `/exit`.

## Capture the result

Back in your terminal, capture the results of the remote run:

```bash
cd "$LP_WORKDIR"
python3 mcp-bridge/capture_hello.py --record "$AGY_RECORD" --label remote-first
```

The command runs `hello.py` in the recorded Pod one more time and saves the source, output, and a SHA-256 hash to `$AGY_SESSION/remote-first/` for your records.

## What you've accomplished and what's next

You've connected the Antigravity CLI to a GKE sandbox through an MCP bridge. You've verified that agent-generated Python ran remotely on Arm with gVisor isolation. 

Next, you'll preserve your results and remove the cloud resources.
