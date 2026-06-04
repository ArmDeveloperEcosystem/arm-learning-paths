---
title: Get started with Windows Subsystem for Linux (WSL) on Arm

description: Learn how to configure and run WSL with Linux distributions, graphical applications, remote desktop, and development tools on Windows on Arm computers.

minutes_to_complete: 90 

who_is_this_for: Software developers with Windows on Arm computers doing Linux or cloud native development.

learning_objectives:
    - Configure and run WSL with various Linux distributions
    - Run graphical Linux applications on Windows
    - Use ssh to connect to WSL
    - Use Windows RDP (remote desktop) and VNC to connect to a Linux desktop
    - Learn multiple options for running VS Code
    - Import other file systems into WSL
    - Export the WSL file system as a backup

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11. 

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:38:39Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 03d816ff419e6e5b1533f95e9d4ffa087b9c0c9aefeee112f67b70223c8aedc3
  summary_generated_at: '2026-06-02T02:38:49Z'
  summary_source_hash: 03d816ff419e6e5b1533f95e9d4ffa087b9c0c9aefeee112f67b70223c8aedc3
  faq_generated_at: '2026-06-02T23:38:39Z'
  faq_source_hash: 03d816ff419e6e5b1533f95e9d4ffa087b9c0c9aefeee112f67b70223c8aedc3
  summary: >-
    This Learning Path shows how to configure and run Windows Subsystem for Linux (WSL) on Windows
    on Arm computers to support Linux and cloud-native development. You will set up WSL with various
    Linux distributions, run graphical Linux applications on Windows 11, enable systemd so services
    start automatically, and use SSH when remote access is required. You will also configure remote
    desktop access with RDP and VNC, learn multiple options for running Visual Studio Code, and
    import or export WSL file systems for backup. The intended audience is developers using Windows
    on Arm systems; no additional prerequisites are explicitly listed beyond a Windows 11 device
    such as a Lenovo ThinkPad X13s. Estimated time to complete is about 90 minutes.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need a Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11.
      No other explicit prerequisites are listed.
  - question: How do I know systemd is enabled and running in my WSL distribution?
    answer: >-
      Add systemd=true to /etc/wsl.conf, terminate the distribution, and restart it. Then run
      systemctl list-unit-files --type=service to confirm systemd-managed services are available;
      services such as SSH and docker will start automatically when systemd is enabled.
  - question: How can I run and verify a graphical Linux application on Windows 11?
    answer: >-
      Install the application from the Linux command line in WSL (for example, terminator on Ubuntu
      22.04) and launch it. A new window should appear on your Windows desktop, and the app will
      show on the Windows taskbar with a penguin icon.
  - question: Do I need SSH to move files between Windows and WSL on the same machine?
    answer: >-
      No. WSL mounts the Windows C: drive at /mnt/c, so you can copy files directly (for example,
      cp /mnt/c/Users/<username>/Downloads/<filename> .). Use SSH only if you need to access WSL
      from a different machine.
  - question: What should I check if RDP does not display the Linux desktop?
    answer: >-
      Verify xfce4 and xrdp are installed, set XFCE4 as the default session (echo xfce4-session
      > ~/.xsession), and restart the xrdp service. Check systemctl status xrdp and start it if
      it is not running.
# END generated_summary_faq

author: Jason Andrews

### Tags
skilllevels: Advanced
subjects: Migration to Arm
armips:
    - Cortex-A
operatingsystems:
    - Windows
    - Linux
tools_software_languages:
    - WSL
    - Visual Studio Code

further_reading:
    - resource:
        title: Learn about Windows on Arm
        link: https://learn.microsoft.com/en-us/windows/arm/overview
        type: documentation
    - resource:
        title: Arm64 Visual Studio
        link: https://devblogs.microsoft.com/visualstudio/arm64-visual-studio/
        type: blog


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

