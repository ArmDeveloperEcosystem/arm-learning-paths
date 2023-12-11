---
title: Install vcpkg
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install vcpkg

[vcpkg](https://vcpkg.io/en/index.html) is a free C/C++ package manager for acquiring and managing libraries. It runs on all platforms, build systems, and work flows. it is maintained by the Microsoft C++ team and open source contributors.

To install the tool, open your favorite Terminal application and run one of the following commands:

{{< tabpane code=true >}}
  {{< tab header="Windows (cmd)" language="shell">}}
curl -LO https://aka.ms/vcpkg-init.cmd && .\vcpkg-init.cmd
  {{< /tab >}}
  {{< tab header="Windows (PowerShell)" language="shell">}}
iex (iwr -useb https://aka.ms/vcpkg-init.ps1)
  {{< /tab >}}
  {{< tab header="Linux/macOS" language="shell">}}
. <(curl https://aka.ms/vcpkg-init.sh -L)
  {{< /tab >}}
{{< /tabpane >}}

When done, your user profile directory should contain a `.vcpkg` folder with all necessary files and scripts.

Continue by initializing `vcpkg`.
