---
title: Remove vcpkg
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Remove vcpkg

If you want to remove `vcpkg` from your system, run one of the following commands:

{{< tabpane code=true >}}
  {{< tab header="Windows (cmd)" language="shell">}}
rmdir /s  %USERPROFILE%\.vcpkg
  {{< /tab >}}
  {{< tab header="Windows (PowerShell)" language="shell">}}
Remove-Item -Recurse -Force -Path ~\.vcpkg
  {{< /tab >}}
  {{< tab header="Linux/macOS" language="shell">}}
rm -rf ~/.vcpkg
  {{< /tab >}}
{{< /tabpane >}}
