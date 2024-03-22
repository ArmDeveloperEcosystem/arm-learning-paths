---
title: Install vcpkg
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install vcpkg

[vcpkg](https://vcpkg.io/en/index.html) is a free C/C++ package manager for acquiring and managing libraries. It runs on all platforms, build systems, and work flows. it is maintained by the Microsoft C++ team and open source contributors.

{{% notice Notice of Product License Terms %}}
Your use of an Arm tool is subject to your acceptance of the End User License Agreement for Arm Software Development Tools, located within the `license_terms` folder of the downloaded archive. By installing and using the Arm tool, you agree to be bound by the terms and conditions of the End User License Agreement.
{{% /notice %}}

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
