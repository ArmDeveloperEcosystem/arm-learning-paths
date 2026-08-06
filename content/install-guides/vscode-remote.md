---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: VS Code Server

draft: true

description: Install VS Code Server on a remote Arm Linux machine and access the full VS Code experience from a browser without tunnels or third-party services.

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- ide
- vscode
- vs code
- visual studio
- vs code server
- serve-web
- browser
- remote development

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

author: Jason Andrews

### Link to official documentation
official_docs: https://code.visualstudio.com/docs/remote/vscode-server

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

VS Code Server is a built-in feature of VS Code that runs a web-based instance on a remote machine, accessible from any browser. You start it with the `code serve-web` command. Unlike [VS Code Tunnels](/install-guides/vscode-tunnels/), VS Code Server doesn't need a GitHub account or a connection to Microsoft's tunnel service. All traffic stays between your local machine and the remote server.

Use cases for VS Code Server include:
- Remote Arm Linux servers, including cloud instances, with no Linux desktop installed
- Developer virtual machines such as Multipass
- Arm single board computers running Linux
- Air-gapped or restricted environments where external tunnel services aren't available

You'll learn how to install VS Code on a remote Arm Linux machine and use VS Code Server to access it from a browser.

## Before you begin

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

You also need SSH access to the remote machine.

## How do I download VS Code?

The VS Code CLI is a small standalone binary that includes `serve-web` support. It's the best choice for running VS Code Server on a headless remote machine.

Download the CLI for Arm (aarch64):

```bash
wget -O vscode-cli.tgz 'https://code.visualstudio.com/sha/download?build=stable&os=cli-alpine-arm64'
```

## How do I install VS Code?

Extract the CLI archive:

```bash
tar xvf vscode-cli.tgz
```

The archive file contains a single executable named `code`. 

The `code` binary is placed in your current directory.

Verify the installation:

```bash
./code --version
```

The output prints the VS Code version:

```output
code 1.132.0 (commit df53daabb18cd157bdb08c7f01c34df936cf12f4)
```

## How do I start VS Code Server?

Start VS Code Server on the remote machine:

```bash
./code serve-web --host 0.0.0.0 --port 8000 --without-connection-token
```

The server starts and prints output similar to:

```output
*
* Visual Studio Code Server
*
* By using the software, you agree to
* the Visual Studio Code Server License Terms (https://aka.ms/vscode-server-license) and
* the Microsoft Privacy Statement (https://privacy.microsoft.com/en-US/privacystatement).
*
Web UI available at http://0.0.0.0:8000
```

{{% notice Note %}}
The `--without-connection-token` flag disables the authentication token. This is convenient for local and private networks. If your remote machine is on a public network, omit this flag and use the token-based URL for security, or use SSH port forwarding as described in the next section.
{{% /notice %}}

## How do I connect to VS Code Server from a browser?

If the remote machine isn't directly accessible in a browser (for example, a cloud instance or headless server), there are two ways to connect.

### Connect using SSH port forwarding

For more information about SSH, see [SSH](/install-guides/ssh/).

Use SSH port forwarding to securely access VS Code Server. Bind to `localhost` instead of `0.0.0.0` when using this approach:

Start the server on the remote machine:

```bash
./code serve-web --host 127.0.0.1 --port 8000 --without-connection-token
```

On your local machine, forward the port with SSH:

```bash
ssh -L 8000:localhost:8000 user@ip-address
```

Open your local browser and navigate to:

```output
http://localhost:8000
```

VS Code appears in the browser, connected to the remote machine.

### Connect by opening a port on the remote machine

You can also open port `8000` on the remote machine for direct access. On a cloud instance, this involves modifying the security group to allow inbound TCP traffic on port 8000.

{{% notice Warning %}}
For best security, open the port only for your IP address. Don't open the port to all IP addresses unless you also use token-based authentication.
{{% /notice %}}

Each cloud provider has instructions on how to configure security groups. For an example, see the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html#adding-security-group-rule).

With the port open, start the server. Use `hostname -I` to pass the machine's IP address directly so the generated link is ready to use:

```bash
./code serve-web --host $(hostname -I | awk '{print $1}') --port 8000 --without-connection-token
```

Without the `--without-connection-token` flag, the server generates a token URL. The output includes a clickable URL with the IP address:

```output
Web UI available at http://10.7.43.188:8000
```

Open this URL in your browser to access VS Code.

## What are the common configuration options?

The `code serve-web` command accepts several options. View all options with:

```bash
./code serve-web --help
```

Common options include:

| Option | Description |
|--------|-------------|
| `--host` | The host interface to bind to. Defaults to `localhost`. Use `0.0.0.0` for all interfaces. |
| `--port` | The port to listen on. Defaults to `8000`. If `0` is passed, a random free port is picked. |
| `--without-connection-token` | Disable token authentication. Only use this if the connection is secured by other means. |
| `--connection-token` | Specify a fixed secret that must be included with all requests. |
| `--default-folder` | The workspace folder to open when no input is specified in the browser URL. |
| `--disable-telemetry` | Disable telemetry reporting. |

## How do I keep VS Code Server running?

If you start VS Code Server in an SSH session and the session disconnects or times out, the server process stops. You would then need to SSH back in and start the server again.

To avoid this, use `nohup` or a terminal multiplexer such as `tmux` or `screen` to keep the server running independently of your SSH session:

```bash
nohup ./code serve-web --host 127.0.0.1 --port 8000 --without-connection-token > vscode-serve.log 2>&1 &
```

Check the log to verify it started:

```bash
cat vscode-serve.log
```

To stop the server:

```bash
kill $(pgrep -f "code serve-web")
```

## What are the key differences between VS Code Server and tunnels?

| Feature | VS Code Server | VS Code Tunnels |
|---------|----------------|-----------------|
| GitHub account required | No | Yes |
| External service dependency | None | Microsoft tunnel service |
| Authentication | Token or none | GitHub |
| Network requirements | Direct access or SSH | Outbound internet |

You're now ready to use VS Code in the browser on your remote Arm machine. You can install extensions, select a color theme, and develop with the full VS Code experience.
