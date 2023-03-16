---
title: Developing with VS Code on WSL

weight: 7
layout: learningpathall
---

## Running VS Code in WSL

There are three ways to run VS Code in WSL
- Natively on Windows
- On Linux as a graphical application
- In the browser using VS Code Server

Visit [Download Visual Studio Code](https://code.visualstudio.com/download) for the first two methods.


## Native on Windows

Download the version for Windows Arm64 and run the installer. 

With WSL running, use the "Remote Explorer" on the left side and find the WSL Targets.

Right click on the WSL instance to connect to and click "Connect to WSL". A new instance of VS Code will open, some software will be installed in WSL, and the connection will complete. 

Use the Terminal menu at the top to select "New Terminal". The terminal prompt will confirm a Linux connection to WSL. 


## Native on Linux

Download the version for Linux Arm64. For Ubuntu or Debian use the .deb file or select one of the other Linux options.

If the download is done from Windows, copy the .deb file into Linux from a Linux prompt. 

Substitute the current filename of the download. 

```bash
cp /mnt/c/Users/<username>/Downloads/code_1.73.1-1667966450_arm64.deb .
```

Install the .deb

```bash
sudo apt install -y ./code_1.73.1-1667966450_arm64.deb 
```

Run VS Code.

```bash
code . 
```

VS Code will appear on the Windows desktop as a graphical Linux application.

There may be a prompt (don't put it in the background) recommending the Windows version instead (as described above). 

The prompt can be eliminated using the environment variable.

```bash
export DONT_PROMPT_WSL_INSTALL=1
```

## Use OpenVSCode Server

The third way to run VS Code on WSL is using OpenVSCodeServer.

Refer to the [installation instructions](/install-guides/openvscode-server/) for details. 

VS Code can be accessed from a Windows browser using localhost:3000 without any special port forwarding.

Clicking the link displayed when OpenVSCode Server is started will open the Windows browser and connect. Hold Ctrl and click the link.



