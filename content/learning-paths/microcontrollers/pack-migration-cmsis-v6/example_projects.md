---
title: Example projects
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Migration of example projects

This section assumes that your example is still using Arm Compiler 5. Therefore, the project first needs to be migrated to Arm Compiler 6 before it can be automatically converted to the new CMSIS-Toolbox project standard (csolution/cproject).

1. Install the newly created device family pack in µVision.
2. Go to **Options for Target - Target** and set the `ARM Compiler` to *Use default compiler version 6*:
  
   ![Set default compiler version 6](./default_ac6.png)
3. Go to the **C/C++ [AC6]** tab and set the appropriate defines. It is also good practice to set the compiler warnings to *AC5-like Warnings* as the new compiler is much stricter and may overwhelm you with warning messages:
   
   ![Compiler tab](./c_cpp_ac6.png)
4. Copy the new scatter file from the device family pack into the project. Check if your project needs specific settings (you can compare against the original scatter file). Once done, go to the **Linker** tab and remove the checkmark at *Use Memory Layout from Target Dialog* and set the path to the new scatter file:  
   
   ![Scatter file in the Linker tab](./linker_tab.png)
5. Finally, build the project to verify the correct operation. Do not forget to add the updated example project to the CMSIS-Pack.

{{% notice Tip %}}
Use the [Arm Compiler for Embedded Migration and Compatibility Guide](https://developer.arm.com/documentation/100068/latest/Migrating-from-Arm-Compiler-5-to-Arm-Compiler-for-Embedded-6) in case you encounter any problems when migrating to Arm Compiler 6.
{{% /notice %}}
