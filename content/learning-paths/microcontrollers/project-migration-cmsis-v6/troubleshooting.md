---
title: Troubleshooting
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Troubleshooting

This section shows the most common errors and shows possible resolutions.

### Missing device

The following error occurs when you try to migrate a project to CMSIS v6, but you have not installed the CMSIS_DFP pack:

![Requested device not found for target](./Device_missing.png)

{{% notice Resolution %}}
Install [ARM.Cortex_DFP.1.0.0.pack](https://www.keil.com/pack/ARM.Cortex_DFP_.1.0.0.pack) or above.
{{% /notice %}}

### Error instantiating RTE components

The following error occurs when you try to migrate a Keil RTX-based project, but you have not installed the CMSIS-RTX pack:

![Keil RTX5 component not available for target](./CMSIS-RTX_missing.png)

{{% notice Resolution %}}
Install [ARM.CMSIS-RTX.5.8.0.pack](https://www.keil.com/pack/ARM.CMSIS-RTX.5.8.0.pack) or above.
{{% /notice %}}

### Missing software components

The following warning is shown in the Validation Output window when you try to migrate a Keil RTX-based project:

![Additional software components required](./OS_Tick_missing.png)

{{% notice Resolution %}}
Use the **Resolve** button to select the missing component automatically.
{{% /notice %}}

### Updating configuration files

Moving a component from one pack to another, has an additional implication. The Event Recorder component for example comes with a configuration file (`EventRecorderConf.h`). This configuration file is stored in the project under the RTE/*Cclass* folder. When you switch from one pack to the other, the Cclass name changes and a fresh copy of the original configuration file is copied to your project.

![New configuration files](./configuration_files.png)

{{% notice Resolution %}}
Copy any edits that you made in the old configuration file into the new one.
{{% /notice %}}

### Manual migration from Keil.ARM_Compiler pack

As the components from the Keil.ARM_Compiler pack do not have 1:1 replacements, you need to deselect the old components and select the replacements from the two new packs (ARM.CMSIS-Compiler and ARM.CMSIS-View).

1. Compiler:EventRecorder migration

   Deselect the `Compiler:Event Recorder` component and select the `CMSIS-View:Event Recorder` component:

   ![Event Recorder migration](./EventRecorder_migration.png)
1. Compiler:I/O migration

   Deselect any component of `Compiler:I/O` and select the corresponding `CMSIS-Compiler` component:

   ![I/O migration](./IO_migration.png)

   This table helps you to identify the correct components:

   | Compiler:I/O:     | CMSIS-Compiler:            |
   |-------------------|----------------------------|
   | STDERR@Breakpoint | STDERR (API):Breakpoint    |
   | STDERR@ITM        | STDERR (API):ITM           |
   | STDERR@User       | STDERR (API):Custom        |
   | STDIN@Breakpoint  | STDIN (API):Breakpoint     |
   | STDIN@ITM         | STDIN (API):ITM            |
   | STDIN@User        | STDIN (API):Custom         |
   | STDOUT@Breakpoint | STDOUT (API):Breakpoint    |
   | STDOUT@EVR        | STDOUT (API):EventRecorder |
   | STDOUT@ITM        | STDOUT (API):ITM           |
   | STDOUT@User       | STDOUT (API):Custom        |
   | TTY@Breakpoint    | TTY (API):Breakpoint       |
   | TTY@ITM           | TTY (API):ITM              |
   | TTY@User          | TTY (API):Custom           |

{{% notice Note %}}
All CMSIS-Compiler components require CMSIS-Compiler:Core to be present.
{{% /notice %}}

### Linker errors using the RTX5 library

In CMSIS v5, the RTX5 libraries were built using the compiler options `-fshort-enums` and `-fshort-wchar`. In CMSIS v6, the default compiler options are different. If you are using the new libraries with old build settings, you will encounter the linker error `L6242W`:

```
.\Blinky.axf: Error: L6242E: Cannot link object Itx timer.o as its attributes are incompatible with the image attributes.
   ... wchart-16 clashes with wchart-32.
   ... packed-enum clashes with enum_is_int
```

{{% notice Resolution %}}
In µVision, go to **Project - Options for Target** and click on the **C/C++ (AC6)** tab. Unselect **Short enums/wchar** and rebuild the project:  
![Unselect short enums/wchar](./compiler_settings.png)
{{% /notice %}}

