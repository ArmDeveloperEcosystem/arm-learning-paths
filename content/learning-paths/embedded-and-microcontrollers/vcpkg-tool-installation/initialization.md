---
title: Initialize vcpkg
description: Initialize vcpkg in the project so command-line tools can be installed from the configured registries.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Initialize vcpkg

You need to run the following initialization command in every new Terminal window:

{{< tabpane code=true >}}
  {{< tab header="Windows (cmd)" language="shell">}}
%USERPROFILE%\.vcpkg\vcpkg-init.cmd
  {{< /tab >}}
  {{< tab header="Windows (PowerShell)" language="shell">}}
. ~/.vcpkg/vcpkg-init.ps1
  {{< /tab >}}
  {{< tab header="Linux/macOS" language="shell">}}
. ~/.vcpkg/vcpkg-init
  {{< /tab >}}
{{< /tabpane >}}

Continue by creating your vcpkg configuration file.
