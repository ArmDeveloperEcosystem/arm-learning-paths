---
title: VS Code Tunnels
description: Install the VS Code CLI on Arm systems and configure Remote Tunnels for browser-based access to non-desktop Arm development environments.

additional_search_terms:
- ide
- vscode

minutes_to_complete: 10

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

Visual Studio Code fully supports the Arm architecture. The [Download page](https://code.visualstudio.com/download) has binaries for all popular Arm architectures and operating systems. Desktop installation is straightforward and there are plenty of tutorials.

VS Code Remote Tunnels is a useful feature for non-desktop Arm development.

Tunnel use cases include:
- Remote Linux servers, including Arm cloud instances, with no Linux desktop installed
- Developer virtual machines such as Multipass
- Arm single-board computers running Linux

A command-line instance of VS Code is run on the remote machine (server) which registers a tunnel. A browser or a VS Code desktop instance (client) is used to connect to the tunnel and access the remote machine. The tunnel removes the need for open ports or SSH port forwarding. VS Code tunnels also work well for connecting to Arm boards on your local network when you are away because no changes to the network are needed.

Creating VS Code tunnels requires a [GitHub](https://github.com/) or [Microsoft](https://account.microsoft.com/) account. This guide uses GitHub. Create an account if you don't already have one.

## Before you begin

Install either the CLI version or the desktop version of VS Code on an Arm Linux machine. This is the remote machine you want to use for development.

The use cases for VS Code tunnels assume SSH or command-line access to the remote Linux machine is available, but no Linux desktop or browser access is required. This means VS Code must be installed from the command line. 

Confirm you are using an Arm machine by running:

```bash 
uname -m
```

Depending on the version of the Arm architecture, the output is one of the following. Both Armv8-A and Armv7-A are supported.

For the Armv8-A architecture, the output is:

```output
aarch64
```

For the Armv7-A architecture, the output is:

```output
armv7l
```

## Download VS Code

Download either the CLI version or the desktop version of VS Code. The desktop version is the best choice if the machine has a Linux desktop and you want to use both a remote tunnel and do desktop development. The CLI version is best for tunneling only.

### Download the CLI version

Select the download for your Arm architecture. Armv8-A is 64-bit and Armv7-A is 32-bit.

### Download for Armv8-A

```console
wget -O vscode.tgz 'https://code.visualstudio.com/sha/download?build=stable&os=cli-alpine-arm64'
```

### Download for Armv7-A

```console
wget -O vscode.tgz 'https://code.visualstudio.com/sha/download?build=stable&os=cli-linux-armhf'
```

### Download the desktop version

VS Code desktop also works for the remote machine. 

Download the Debian package for VS Code desktop using the command line. This is for Ubuntu or Debian Linux machines. An RPM version is also available for Red Hat and Fedora.

```bash
wget -O vscode.deb 'https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-arm64'
```

{{% notice Warning %}}
The `snap` install is for a non-Arm architecture and does not work.
{{% /notice %}}

## Install VS Code

For CLI, extract the file. The result is a single executable named `code`. It is placed in the current directory.

```console
tar xvf vscode.tgz
```

Then copy the binary to `/usr/local/bin/` so it is available on `PATH`:

```console
sudo cp code /usr/local/bin/
```

For the desktop, install the Debian package.

```console
sudo apt install ./vscode.deb
```

## Verify the installation

Confirm the installed binary works:

```console
code --version
```

For the CLI version, the output looks like:

```output
code 1.146.0 (commit 69047191fc427f2f92828279aae1d90d8eeda7ab)
```

For the desktop version, the output looks like:
```output
1.146.0
69047191fc427f2f92828279aae1d90d8eeda7ab
arm64
```

The exact version numbers will differ, but a successful response confirms the binary is working. The `arm64` line in the desktop output also confirms the correct architecture was installed.

## Start a VS Code tunnel

On the remote machine, start a VS Code tunnel.

```console
code tunnel --name my-tunnel-1 --accept-server-license-terms
```

If `--name` is not used, an arbitrary name is assigned to the tunnel.

{{% notice Note %}}
This command runs the tunnel in the foreground, attached to your terminal session. The tunnel stays online only while the command is running. If you close the terminal, disconnect your SSH session, or press `Ctrl+C`, the tunnel stops and disappears from your tunnel list. To keep a tunnel running permanently, install it as a service instead. See [Run a tunnel as a service](#service).
{{% /notice %}}

The VS Code tunnel server prints a URL to authenticate and link the machine to your GitHub account.
```output
*
* Visual Studio Code Server
*
* By using the software, you agree to
* the Visual Studio Code Server License Terms (https://aka.ms/vscode-server-license) and
* the Microsoft Privacy Statement (https://privacy.microsoft.com/en-US/privacystatement).
*
To grant access to the server, please log into https://github.com/login/device and use code XXXX-YYYY
```
Open [https://github.com/login/device](https://github.com/login/device) in a browser and enter the code shown.

After the code is entered, the tunnel comes online and prints the connection URL:
```output
[2026-01-01 00:00:00] info Creating tunnel with the name: my-tunnel-1

  Visual Studio Code Tunnel v1.146.0

  ➜  Tunnel:   my-tunnel-1
  ➜  Open:  https://vscode.dev/tunnel/my-tunnel-1
```

![Device Connect #center](/install-guides/_images/vsc-device-connect.png)

## Run a tunnel as a service {#service}

The foreground `code tunnel` command stops when the terminal closes. For a tunnel that stays online across logouts and reboots, install it as a background service. On Linux, this registers a `systemd` user service that starts the tunnel automatically.

```console
code tunnel service install --name my-tunnel-1 --accept-server-license-terms
```

The first time you install the service, you are prompted to authenticate with GitHub using the same device-code flow as the foreground tunnel command. After you enter the code, the service registers and starts:
```output
[2026-01-01 00:00:00] info Successfully registered service...
[2026-01-01 00:00:00] info Successfully enabled unit files...
[2026-01-01 00:00:00] info Tunnel service successfully started
[2026-01-01 00:00:00] info Tip: run `sudo loginctl enable-linger $USER` to ensure the service stays running after you disconnect.
Service successfully installed! You can use `code tunnel service log` to monitor it, and `code tunnel service uninstall` to remove it.
```

Run the `loginctl` command shown in the tip to keep the service alive across SSH logouts and reboots:
```console
sudo loginctl enable-linger $USER
```

Manage the service with these commands:

| Command | Action |
|---------|--------|
| `code tunnel service log`       | Follow the live service log (press `Ctrl+C` to exit) |
| `code tunnel service uninstall` | Stop and remove the service |

Running `code tunnel service uninstall` prints:
```output
[2026-01-01 00:00:00] info Successfully stopped service...
[2026-01-01 00:00:00] info Tunnel service uninstalled
```

## Find and manage tunnels

If you started a tunnel but cannot find it, the most common reason is that it was run in the foreground and stopped when the terminal closed. Use the commands below to check the current state on the remote machine.

Check whether a tunnel is running and whether a service is installed:
```console
code tunnel status
```
The output reports the tunnel name, whether it is `Connected`, and whether a service is installed:
```output
{"tunnel":{"name":"my-tunnel-1","tunnel":"Connected", ... },"service_installed":true}
```
If the output shows `"tunnel":null` and `"service_installed":false`, no tunnel is currently running. Start one again, or install it as a service so it persists.

Check which GitHub account the tunnel is registered to:
```console
code tunnel user show
```
```output
logged in with provider GitHub Account
```

Other useful management commands:

| Command | Action |
|---------|--------|
| `code tunnel kill`       | Stop any tunnel currently running on this machine |
| `code tunnel restart`    | Restart the running tunnel |
| `code tunnel rename <name>` | Change the machine's tunnel name |
| `code tunnel prune`      | Delete registered tunnels that are not currently running |
| `code tunnel unregister` | Remove this machine's association with the tunnel service |

You can also see every tunnel registered to your account, and whether each one is online, by opening [https://vscode.dev](https://vscode.dev) and selecting **Connect to Tunnel**, or from the **Remote Explorer** in VS Code Desktop.

## Connect to the remote machine

The remote machine is now ready to accept client connections. These can be from a browser or VS Code desktop.

### Connect using a browser

The quickest way to connect to the remote machine is using a browser. Even a tablet or phone can be used. 

Connect using a browser by visiting the link which is printed by the server.

The link will contain the tunnel name specified with `--name` or a created name if no name was provided.

If you used `--name my-tunnel-1`, the tunnel link is:
```url
https://vscode.dev/tunnel/my-tunnel-1
```
If you do not remember or cannot see the tunnel name, open:
```url
https://vscode.dev
```
When VS Code opens, click on the lower-left corner and select **Connect to Tunnel**. 

![Remote #center](/install-guides/_images/vsc-remote.png)

A list of tunnels attached to your account opens. If you are not signed in to GitHub, it will require authentication before showing the list of tunnels. The tunnel list also shows if the tunnel is online and ready for a connection.

Select the tunnel to open. VS Code connects to the remote machine and you're ready to develop software.

### Connect using VS Code Desktop

Connecting to a tunnel from VS Code Desktop requires the [Remote - Tunnels Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.remote-server).

Search for `remote tunnels` in the **Extensions** view and install the extension.

Just as with the browser connection, click on the lower-left corner and select **Connect to Tunnel**. 

![Remote #center](/install-guides/_images/vsc-remote.png)

## Close the tunnel connection

On both browser and desktop, click the lower-left corner (which now shows the name of the connected tunnel) and select **Close Remote Connection** to disconnect from the tunnel server. 

## Summary

VS Code tunnels and your GitHub account make it easy to connect to Arm machines running Linux for terminal access or to do development on a remote machine with VS Code. This is done without any open ports or SSH port forwarding.
