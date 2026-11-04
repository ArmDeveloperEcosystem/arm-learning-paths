---
title: OpenSandbox

description: Install OpenSandbox on Arm Linux and run a Python command in a Docker-backed sandbox.

minutes_to_complete: 20
official_docs: https://open-sandbox.ai/getting-started/

author: Anupras Mohapatra

test_maintenance: false

additional_search_terms:
- opensandbox
- osb
- sandbox
- docker
- containers
- arm64

weight: 1
tool_install: true
multi_install: false
multitool_install_part: false
layout: installtoolsall
---

OpenSandbox provides a server and a command-line interface (CLI) for creating and managing isolated environments. Its Docker runtime runs sandboxes as containers that share the host Linux kernel. 

You'll install OpenSandbox on an `aarch64` host with Ubuntu 24.04 LTS or later. Then, you'll start a local server and create a sandbox. Finally, you'll run a Python command inside it to verify the installation. 

## Before you begin

You need an Arm Linux system running Ubuntu 24.04 LTS with `sudo` access. The system also needs to have internet access to the Ubuntu package repositories, Python package index, and Docker Hub. Allow free disk space for Docker images and container data. You don't need kernel-based virtual machine (KVM) for the Docker runtime.

Check the host architecture and operating system:

```bash
uname -m
cat /etc/os-release
```

Confirm that the architecture is `aarch64` and that the operating system is Ubuntu 24.04 LTS or later.

You also need Docker Engine version 20.10 or later installed on your system. For installation steps, see the [Docker Engine install guide](/install-guides/docker/docker-engine/).

Confirm that Docker works without `sudo`:

```bash
docker version
docker info --format '{{.Architecture}}'
```

The server version should be at least `20.10`, and the architecture should be `aarch64`. If Docker reports a socket permission error, log out and log back in before continuing.

### Install `uv`

Install `uv` using the [official installer](https://docs.astral.sh/uv/getting-started/installation/):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Make the installed command available in your current shell, then check its version:

```bash
export PATH="$HOME/.local/bin:$PATH"
uv --version
```

Add the same `export PATH` line to `~/.bashrc` if `~/.local/bin` isn't already on your `PATH` in new shells.

## Install and configure OpenSandbox

Install the OpenSandbox server and CLI as user-level tools:

```bash
uv tool install opensandbox-server
uv tool install opensandbox-cli
```

Confirm that both commands are available:

```bash
opensandbox-server --help
osb --version
```

Generate a server configuration for the Docker runtime:

```bash
opensandbox-server init-config ~/.sandbox.toml --example docker
```

`host` under `[server]` is set to `127.0.0.1` by default. Confirm that this is the case in `~/.sandbox.toml`:

```toml
[server]
host = "127.0.0.1"
```

Binding the server to localhost keeps its API reachable from the same host without exposing port `8080`.

The example configuration has no API key. Use this configuration only for testing the installation. If the server asks you to acknowledge the unauthenticated configuration, enter `YES`.

Start the server in this terminal and leave it running:

```bash
opensandbox-server
```

In a second terminal on the same host, check the server health endpoint:

```bash
curl http://127.0.0.1:8080/health
```

The expected output is:

```output
{"status":"healthy"}
```

Configure the CLI to use the local server and proxy sandbox requests through it:

```bash
osb config init
osb config set connection.domain localhost:8080
osb config set connection.protocol http
osb config set connection.use_server_proxy true
```

## Verify the installation

Create a sandbox from the Python image with a 30-minute timeout:

```bash
osb sandbox create --image python:3.12 --timeout 30m -o json
```

The first run downloads the Python image and the OpenSandbox execution helper image. The command returns JSON containing the new sandbox ID. 

The output is similar to:

```json
{
  "id": "5e4b52ca-9947-4f3a-a1a7-6254239cd431",
  "status": "created",
  "timeout": "0:30:00",
  "image": "python:3.12"
}
```

Copy the `id` into a shell variable in the second terminal:

```bash
sandbox_id="<sandbox-id>"
```

Replace `<sandbox-id>` with the `id` that was returned by your `create` command. 

Check that the sandbox is healthy:

```bash
osb sandbox health "$sandbox_id" -o json
```

The output is similar to:

```json
{
  "sandbox_id": "5e4b52ca-9947-4f3a-a1a7-6254239cd431",
  "healthy": true
}
```

Run the architecture check inside the sandbox:

```bash
osb command run "$sandbox_id" -o raw -- sh -c 'uname -m'
```

The expected output is:

```output
aarch64
```

The `aarch64` result confirms that the sandbox container runs on Arm.

Run a Python command inside the sandbox:

```bash
osb command run "$sandbox_id" -o raw -- sh -c 'python -c "print(6 * 7)"'
```

The expected output is:

```output
42
```

The Python result confirms that you can run a command in the sandbox through the OpenSandbox CLI.

## Clean up test resources 

Delete the test sandbox:

```bash
osb sandbox kill "$sandbox_id" -o json
```

The output is similar to:

```json
[
  {
    "sandbox_id": "5e4b52ca-9947-4f3a-a1a7-6254239cd431",
    "status": "deletion_requested"
  }
]
```

List sandboxes to confirm deletion:

```bash
osb sandbox list -o json
```

The output is similar to:

```json
{
  "items": [],
  "pagination": {
    "page": 1,
    "page_size": 20,
    "total_items": 0,
    "total_pages": 0,
    "has_next_page": false
  }
}
```

The `kill` command can return `deletion_requested` while removal completes. Repeat the `osb sandbox list` command if the sandbox is still present. The server configuration, CLI settings, and downloaded images remain available for future use.

Return to the terminal with the running server and shut the server by pressing **Ctrl + C**. 

## Next steps

You can now use OpenSandbox to create and manage Docker-backed sandboxes on Arm Linux. 

For additional commands, see the [OpenSandbox CLI documentation](https://open-sandbox.ai/cli/). For server authentication and deployment settings, see the [OpenSandbox configuration documentation](https://open-sandbox.ai/getting-started/configuration).
