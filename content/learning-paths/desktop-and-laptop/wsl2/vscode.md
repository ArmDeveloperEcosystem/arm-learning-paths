---
title: Developing with VS Code on WSL

weight: 7
layout: learningpathall
---

## Running VS Code in WSL

There are four ways to run VS Code in WSL:
- Native on Windows
- Native on Linux
- Use VS Code Remote Tunnels
- Use OpenVSCode Server

This learning path will explore each of these options.

## Native on Windows

[Download Visual Studio Code](https://code.visualstudio.com/download) for Windows Arm64 and run the installer. 

With WSL running, use the `Remote Explorer` on the left side and find the WSL Targets.

Right click on the WSL instance to connect to and click `Connect to WSL`. A new instance of VS Code will open, some software will be installed in WSL, and the connection will complete. 

Use the Terminal menu at the top to select `New Terminal`. The terminal prompt will confirm a Linux connection to WSL. 


## Native on Linux

[Download Visual Studio Code](https://code.visualstudio.com/download) for Linux Arm64. For Ubuntu or Debian use the `.deb` file or select one of the other Linux options.

If the download is done from Windows, copy the `.deb` file into Linux from a Linux prompt. 

Substitute the filename with the filename of your download: 

```bash
cp /mnt/c/Users/<username>/Downloads/code_1.77.1-1680650504_arm64.deb .
```

Install the `.deb` file:

```bash
sudo apt install -y ./code_1.77.1-1680650504_arm64.deb
```

Run VS Code:

```bash
code . 
```

VS Code will appear on the Windows desktop as a graphical Linux application.

There may be a prompt (so don't launch `code` it in the background) recommending the Windows version instead.

The prompt can be eliminated using the environment variable:

```bash
export DONT_PROMPT_WSL_INSTALL=1
```

## Use VS Code Remote Tunnels

You can use the [install guide for VS Code Tunnels](/install-guides/vscode-tunnels/) to install the VS Code CLI inside a WSL Linux distribution and and connect to it from any other machine running VS Code, including the local Windows on Arm machine.

## Use OpenVSCode Server

You can run VS Code on WSL using OpenVSCode Server.

Look at the [install guide for OpenVSCode Server](/install-guides/openvscode-server/) for setup information. 

VS Code can be accessed from a Windows browser using `localhost:3000` without any special port forwarding.

Click the link displayed when OpenVSCode Server is started. This will open the Windows browser and connect. Hold `Ctrl` key and click the link.



