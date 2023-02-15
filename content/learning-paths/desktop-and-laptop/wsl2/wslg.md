---
title: Run graphical Linux applications

weight: 3
layout: learningpathall
---

## Run graphical Linux applications

On Windows 11 graphical Linux applications be run by installing them and running them from the Linux command line.

For example, install the Linux terminator application on Ubuntu 22.04.

```bash
sudo apt install terminator -y
```

Run the application.

```bash
terminator &
```

A new terminal window will appear on the Windows desktop. 

![Running terminator #center](wsl-terminator.png)

Linux applications will appear on the Windows taskbar with a small penguin. It's possible to pin them to the taskbar and add icons to the applications menu.

Windows runs a containerized Linux with XServer, Wayland, and Pulse Audio. 

Inspect the Linux environment variables for more information.

```console
echo $WAYLAND_DISPLAY
echo $PULSE_SERVER
echo $DISPLAY
```
Graphical Linux applications have seamless copy/paste with Windows making them easier to use.
