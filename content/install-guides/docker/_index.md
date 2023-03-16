---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Docker

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- containers
- virtual machines

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 60

### Link to official documentation
official_docs: https://docs.docker.com/

## PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: true             # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

Docker containers are widely used, primarily because they run the same everywhere. Containers are used on all operating systems, on all computing architectures to build, share, and run software.

The operating system of the computer and the architecture (x86 or Arm) will determine how to install Docker.

- Docker Engine on Linux runs on a variety of Linux distributions and architectures, including arm and arm64 (aarch64). Use these instructions for Linux and Chrome OS (using the Linux feature).

- Docker Desktop is the easiest way to install Docker on Windows and macOS. The macOS version supports both Intel and Apple Silicon. The Windows version does not support Windows on Arm. There is also a new Docker Desktop for Linux available if the machine has KVM support and is running a KDE or Gnome desktop environment.    

- Docker on Windows on Arm can be run on Windows on Arm machines using the Windows Subsystem for Linux 2 (WSL2). There is no Docker Desktop for Windows on Arm, [please show your support by asking for it](https://github.com/docker/roadmap/issues/91).
