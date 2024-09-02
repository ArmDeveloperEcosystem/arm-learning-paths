---
title: Browsers on Arm
author_primary: Jason Andrews
additional_search_terms:
- browser
- brave
- chrome
- chromium
- edge
- firefox
- vivaldi
- windows
- woa
- windows on arm
- linux

### FIXED, DO NOT MODIFY
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: true             # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

You may want to use web browsers on Arm platforms during development projects. 

Browser support for Arm varies. Some browsers have broad operating system support and native execution on Arm while others do not. 

The information below helps you:

- Install browsers on Arm Linux distributions

- Install browsers on Windows on Arm

- Learn other useful information about browsers on Arm

Here is a quick summary to get you started:

| Browser       | Windows on Arm | Arm Linux support |
| -----------   | -------------- | ---------         |
| Firefox       | native         | yes               |
| Chromium      | native         | yes               |
| Brave         | native         | yes               |
| Chrome        | native         | no                |
| Edge          | native         | no                |
| Vivaldi       | native         | yes               |

Windows on Arm runs native ARM64 applications, but can also emulate 32-bit x86 and 64-bit x64 applications. Emulation is slower than native and shortens battery life, but may provide functionality you need.

The primary functional issue for browsers on Arm is DRM (digital rights management). DRM is required to play certain video content from streaming services such as Netflix. To test if your browser has DRM check the [DRM stream test](https://bitmovin.com/demos/drm). 

Edge and Firefox are good native browsers with DRM support for Windows on Arm. There are no easy DRM solutions for Arm Linux.

Please share your experiences with browsers on Arm by submitting a [GitHub issue](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/issues/new) or a GitHub Pull Request to add additional browsers. 


