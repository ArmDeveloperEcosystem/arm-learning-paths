---
title: Setting up Docker on Windows on Arm using Windows Subsystem for Linux
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Installing docker on WoA
Currently, Docker Desktop is not available for Arm64-based Windows machines. However, we can use Windows Subsystem for Linux (WLS) to set up Docker. This section explains how to do it step by step in Windows 11.

First, open the Command Prompt. Then install the Ubuntu distribution under WSL by typing:
```console
wsl --install ubuntu
```

Then, enter your username (I will be using d), and type in your password. You will then see the following:
![command prompt#left](figures/01.png)

Now we install Docker by typing:
```
sudo snap install docker
```
The command will first ask for the admin password (the same one you used above) and then install Docker:
![command prompt#left](figures/02.png)