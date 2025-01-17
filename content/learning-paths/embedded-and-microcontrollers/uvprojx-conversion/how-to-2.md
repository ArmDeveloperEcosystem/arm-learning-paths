---
title: Using the command line
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Project conversion on the command line using vcpkg

[vcpkg](https://vcpkg.io/en/index.html) is a free C/C++ package manager for acquiring and managing libraries. It runs on all platforms, build systems, and work flows. it is maintained by the Microsoft C++ team and open source contributors.

In your favorite terminal application, change to the directory containing the uvprojx-based project.

1. If you have not done it before, install vcpkg (otherwise continue to step 2):

   {{< tabpane code=true >}}
     {{< tab header="Windows (cmd)" language="shell">}}
   curl -LO https://aka.ms/vcpkg-init.cmd && .\vcpkg-init.cmd
     {{< /tab >}}
     {{< tab header="Windows (PowerShell)" language="shell">}}
   iex (iwr -useb https://aka.ms/vcpkg-init.ps1)
     {{< /tab >}}
     {{< tab header="Linux/macOS" language="shell">}}
   . < (curl https://aka.ms/vcpkg-init.sh -L)
     {{< /tab >}}
   {{< /tabpane >}}

1. Initialize vcpkg:

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

2. Update the Arm vcpkg registry (this will give you access to tools hosted by Arm):

   ```shell
   vcpkg x-update-registry arm
   ```

3. Enable the `uv2csolution` conversion tool:

   ```shell
   vcpkg use uv2csolution
   ```

4. Run the conversion (in this example, the project is called `MyProject.uvprojx`):

   ```shell
   uv2csolution MyProject.uvprojx
   ```

   This step generates the following files:
   - `MyProject.csolution.yaml`
   - `MyProject.cproject.yaml`
   - `vcpkg-configuration.json`

5. Activate the vcpkg configuration (this will install all required tools on your machine):

   ```shell
   vcpkg activate
   ```

5. Get an MDK-Community license:

   ```shell
   armlm activate -product KEMDK-COM0 -server https://mdk-preview.keil.arm.com
   ```

5. [Optional] Check your license:

   ```shell
   armlm inspect
   ```

6. Build the project:

   ```shell
   cbuild MyProject.csolution.yaml --update-rte
   ```

   A successful project build will end with:

   ```output
   Program size: Code=... RO-data=... RW-data=... ZI-data=...
   info cbuild: build finished successfully!
   ```
