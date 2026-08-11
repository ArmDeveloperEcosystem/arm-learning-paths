---
title: Get started with Windows Subsystem for Linux on Arm

description: Learn how to configure and run WSL with Linux distributions, graphical applications, remote desktop, and development tools on Windows on Arm computers.

minutes_to_complete: 90 

who_is_this_for: This Learning Path is for software developers with Windows on Arm computers doing Linux or cloud native development.

learning_objectives:
    - Configure and run Windows Subsystem for Linux (WSL) with various Linux distributions
    - Run graphical Linux applications on Windows
    - Use ssh to connect to WSL
    - Use Windows RDP (remote desktop) and VNC to connect to a Linux desktop
    - Learn multiple options for running VS Code
    - Import other file systems into WSL
    - Export the WSL file system as a backup

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:28:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 04f6894d6d9a1637e06aaa48321c09b918e80343d670cc5dd062179d9452486c
  summary_generated_at: '2026-08-11T16:28:59Z'
  summary_source_hash: 04f6894d6d9a1637e06aaa48321c09b918e80343d670cc5dd062179d9452486c
  faq_generated_at: '2026-08-11T16:28:59Z'
  faq_source_hash: 04f6894d6d9a1637e06aaa48321c09b918e80343d670cc5dd062179d9452486c
  summary: >-
    You'll configure WSL on Windows on Arm, select and run a Linux
    distribution, and enable `systemd` so common services start automatically. First, you'll install and
    launch graphical Linux applications from
    the Linux shell. Then, you'll learn when to
    use SSH versus the built-in Windows drive mount for file transfer. You'll also set up
    up an XFCE4 desktop in WSL with the `xrdp` server, restarting it after configuration changes,
    and checking its status. You'll be able to restart a distribution cleanly,
    validate that `systemd` and `xrdp` are active, and recognize how WSL integrates Linux GUI apps
    with Windows.
  faqs:
  - question: How do I enable systemd in my WSL distribution and confirm it’s running?
    answer: >-
      Edit `/etc/wsl.conf` to include `[boot]` with `systemd=true`. In Windows Command Prompt or PowerShell,
      run `wsl --terminate Ubuntu-22.04` and then `wsl -d Ubuntu-22.04`. Verify with
      `systemctl list-unit-files --type=service`.
  - question: What should I see when I start a graphical Linux app from WSL?
    answer: >-
      A new app window opens on the Windows desktop and shows a small penguin icon on the **taskbar**.
      You can pin the app to the **taskbar** and add icons to the **Windows applications menu**.
  - question: Do I need SSH to copy files between Windows and WSL on the same machine?
    answer: >-
      No. Windows drives are mounted under `/mnt/c`, so you can copy directly, for example,
      `cp /mnt/c/Users/<username>/Downloads/<filename>`. Use SSH only when connecting to WSL from a different machine.
  - question: How do I set XFCE4 as the default desktop for RDP and check that xrdp is ready?
    answer: >-
      Set the session with `echo xfce4-session > ~/.xsession` and then restart the service with
      `sudo service xrdp restart`. Check status with `systemctl status xrdp`, and start it if it's not
      running.
  - question: Which distribution name should I use when restarting WSL after enabling systemd?
    answer: >-
      Use the registered distribution name shown in WSL, such as `Ubuntu-22.04`. Run
      `wsl --terminate Ubuntu-22.04` followed by `wsl -d Ubuntu-22.04` to restart it with systemd enabled.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
