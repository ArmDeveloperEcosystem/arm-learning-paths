---
title: Using Keil Studio
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Project conversion in Keil Studio

1. In VS Code, go to **File - Open Folder** and select the folder containing the uvprojx file (here `Blinky.uvprojx`).

1. Once the folder is open in VS Code, right-click the uvprojx file and select **Convert µVision project to csolution**:

   ![Convert project](./blinky_convert.png)

1. The following files (and more) are generated:
   - `Blinky.csolution.yaml`
   - `Blinky.cproject.yaml`
   - `vcpkg-configuration.json`

1. The **Output** window shows a successful conversion:

   ![Successful conversion](./output_conversion.png)

1. The vcpkg configuration file is automatically activated. You notice an active "Environment" configuration in the **Status Bar** at the bottom:

   ![vcpkg activated](./vcpkg-activated.png)

1. Click on the **CMSIS** icon in the **Activity Bar**. The **Primary Side Bar** changes and shows the **CONTEXT**, **SOLUTION**, and **ACTIONS** for the project.

1. In the **ACTIONS** section, click on **Build**:

   ![CMSIS build](./cmsis-build.png)

1. The `cbuild` task starts. A successful project build will end with:

   ```output
   Program size: Code=... RO-data=... RW-data=... ZI-data=...
   info cbuild: build finished successfully!
   Build complete
   ```
