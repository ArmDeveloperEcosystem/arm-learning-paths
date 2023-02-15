---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: VS Code Tunnels

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- ide

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

### Link to official documentation
official_docs: https://code.visualstudio.com/docs/remote/vscode-server

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

The Arm architecture is well supported by the popular [Visual Studio Code](https://code.visualstudio.com/) development tool. The [Download page](https://code.visualstudio.com/download) has binaries for all popular Arm architectures and operating systems. Desktop installation is straightforward and there are plenty of tutorials.

VS Code Remote Tunnels is a useful feature for non-desktop Arm development.

Tunnel use cases include:
- Remote Linux servers, including Arm cloud instances, with no Linux desktop installed
- Developer virtual machines such as Multipass
- Arm single board computers running Linux

To create a tunnel a command-line instance of VS Code is run on the remote machine (server) which registers a tunnel. A browser or a VS Code desktop instance (client) is used to connect to the tunnel and access the remote machine. The tunnel removes the need for open ports or SSH port forwarding. VS Code tunnels also work well for connecting to Arm boards on your local network when you are away because no changes to the
 network are needed.

{{% notice Note %}}
Creating VS Code tunnels requires a [GitHub](https://github.com/) account.
{{% /notice %}}

## Introduction

Follow the instructions below to install either the CLI version or the desktop version of VS Code on an Arm Linux machine. This is the remote machine you want to use for development.

The use cases for VS Code tunnels assume SSH or command line access to the remote Linux machine is available, but no Linux desktop or browser access is required. This means VS Code must be installed from the command line. 

Confirm you are using an Arm machine by running:

```bash 
uname -m
```
Depending on the version of the Arm architecture, the results are shown below. Both Armv8-A and Armv7-A are supported. 

{{< tabpane code=true >}}
  {{< tab header="Armv8-A">}}
aarch64
  {{< /tab >}}
  {{< tab header="Armv7-A">}}
armv7l
  {{< /tab >}}
{{< /tabpane >}}

## Pick a version to download 

Download either the CLI version or the desktop version of VS Code. The desktop version is the best choice if the machine has a Linux desktop and you want to use both a remote tunnel and do desktop development. The CLI version is best for tunneling only.

### Download CLI version of VS Code (tunnel only)

Download a command line (CLI) release of VS Code from the Downloads page. 

{{< tabpane code=true >}}
  {{< tab header="Armv8-A">}}
wget -O vscode.tgz 'https://code.visualstudio.com/sha/download?build=stable&os=cli-alpine-arm64'
  {{< /tab >}}
  {{< tab header="Armv7-A">}}
wget -O vscode.tgz 'https://code.visualstudio.com/sha/download?build=stable&os=cli-linux-armhf'
  {{< /tab >}}
{{< /tabpane >}}


### Download desktop version of VS Code (tunnel and desktop)

VS Code desktop also works for the remote machine. 

Download the Debian package for VS Code desktop using the command line. This is for Ubuntu or Debian Linux machines. An RPM version is also available for Red Hat and Fedora.

```bash
wget -O vscode.deb 'https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-arm64'
```

{{% notice Warning %}}
The snap install is for a non-Arm architecture and doesn't work.
{{% /notice %}}

## Install the downloaded version

For CLI, extract the file. The result is a single executable named `code`. It is placed in the current directory. For desktop install the Debian package.

{{< tabpane code=true >}}
  {{< tab header="CLI">}}
tar xvf vscode.tgz
  {{< /tab >}}
  {{< tab header="desktop">}}
sudo apt install ./vscode.deb
  {{< /tab >}}
{{< /tabpane >}}

## Start a VS Code Tunnel

On the remote machine start a VS Code tunnel. The ./ is used to indicate the CLI version which was extracted in the current directory. For the desktop install the code executable is in the search path and the ./ should be omitted. 

{{< tabpane code=true >}}
  {{< tab header="CLI">}}
./code tunnel --name my-tunnel-1 --accept-server-license-terms
  {{< /tab >}}
  {{< tab header="desktop">}}
code tunnel --name my-tunnel-1 --accept-server-license-terms
  {{< /tab >}}
{{< /tabpane >}}

If `--name` is not used, a name will be assigned to the tunnel. 

The VS Code tunnel server will print a URL to authenticate and link it to your GitHub account. 

Visit the [device link](https://github.com/login/device) and then enter the code shown.


```console
*
* Visual Studio Code Server
*
* By using the software, you agree to
* the Visual Studio Code Server License Terms (https://aka.ms/vscode-server-license) and
* the Microsoft Privacy Statement (https://privacy.microsoft.com/en-US/privacystatement).
*
To grant access to the server, please log into https://github.com/login/device and use code A4F7-33D4
```

After the code is entered, the remote device is connected to your GitHub account. 

![Device Connect](/install-tools/_images/vsc-device-connect.png)

The remote machine is now ready to accept client connections. These can be from a browser or VS Code desktop. 

### Connection Option 1: using a browser

The quickest way to connect to the remote machine is using a browser. Even a tablet or phone can be used. 

Connect using a browser by visiting the link which is printed by the server.

The link will contain the tunnel name specified with `--name` or a created name if no name was provided.

In the example above, the tunnel link is: 

https://vscode.dev/tunnel/my-tunnel-1

If you don't remember or can't see the tunnel name, open https://vscode.dev in a browser.

When VS Code opens click on the lower left corner and select "Connect to Tunnel". 

![Remote](/install-tools/_images/vsc-remote.png)

A list of tunnels attached to your account will be opened. If you are not signed in to GitHub it will require authentication before showing the list of tunnels. The tunnel list also shows if the tunnel is online and ready for a connection.

Select the tunnel to open and VS Code will connect to the remote machine and you are ready to use VS Code on the remote machine.

### Connection Option 2: using VS Code desktop

Connecting to a tunnel from VS Code Desktop requires the [Remote - Tunnels Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.remote-server). Search for "remote tunnels" in the Extensions Marketplace and install the extension.

Just as with the browser connection, click on the lower left corner and select "Connect to Tunnel". 

![Remote](/install-tools/_images/vsc-remote.png)

A list of tunnels attached to your account will be opened. If you are not signed in to GitHub it will require authentication before showing the list of tunnels. The tunnel list also shows if the tunnel is online and ready for a connection.

Select the tunnel to open and VS Code will connect to the remote machine and you are ready to use VS Code on the remote machine.

## Close a tunnel connection

On both browser and desktop, click the lower left (which now shows the name of the connected tunnel) and select "Close Remote Connection" to disconnect from the tunnel server. 

## Summary 

VS Code tunnels and your GitHub account make it easy to connect to Arm machines running Linux for terminal access or to do development on a remote machine with VS Code. This is done without any open ports or SSH port forwarding.

