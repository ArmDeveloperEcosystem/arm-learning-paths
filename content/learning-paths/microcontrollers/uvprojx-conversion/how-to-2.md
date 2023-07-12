---
title: Using the command line
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Project conversion on the command line using vcpkg

[vcpkg](https://vcpkg.io/en/index.html) is a free C/C++ package manager for acquiring and managing libraries. It runs on all platforms, buildsystems, and worklows. it is maintained by the Microsoft C++ team and open source contributors.

In your favorite terminal application, change to the directory containing the uvprojx-based project.

1. If you have not done it before, install vcpkg (otherwise continue to step 2):

   **Windows (cmd)**:
   
   ```
   curl -LO https://aka.ms/vcpkg-init.cmd && .\vcpkg-init.cmd
   ```
   
   **Windows (PowerShell)**:
   
   ```
   iex (iwr -useb https://aka.ms/vcpkg-init.ps1)
   ```
   
   **Linux/macOS**:
   
   ```
   . <(curl https://aka.ms/vcpkg-init.sh -L)
   ```

1. Initialize vcpkg:

   **Windows (cmd)**:
   
   ```
   %USERPROFILE%\.vcpkg\vcpkg-init.cmd
   ```
   
   **Windows (PowerShell)**:
   
   ```
   . ~/.vcpkg/vcpkg-init.ps1
   ```
   
   **Linux/macOS**:
   
   ```
   . ~/.vcpkg/vcpkg-init
   ```

2. Update the Arm vcpkg registry (this will give you access to tools hosted by Arm):

   ```
   vcpkg x-update-registry
   ```

3. Enable the `uv2csolution` conversion tool:

   ```
   vcpkg use uv2csolution
   ```

4. Run the conversion (in this example, the project is called `MyProject.uvprojx`):

   ```
   uv2csolution MyProject.uvprojx
   ```

   This step generates the following files:
   - `MyProject.csolution.yaml`
   - `MyProject.cproject.yaml`
   - `vcpkg-configuration.json`

5. Activate the vcpkg configuration (this will install all required tools on your machine):

   ```
   vcpkg activate
   ```

6. Build the project:

   ```
   cbuild MyProject.csolution.yaml --update-rte
   ```

   A successful project build will end with:

   ```
   Program size: Code=... RO-data=... RW-data=... ZI-data=...
   info cbuild: build finished successfully!
   ```
