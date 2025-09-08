---
title: Debugging BL33 / UEFI
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Debugging BL33 / UEFI

Adding symbol files for UEFI requires you to boot the FVP once without debugging, so that you can retrieve the symbol file locations and memory addresses.

<<<<<<< HEAD
After booting the FVP, notice that in the Non-secure AP console output, the UEFI load system helpfully shows where each driver is relocated to.

**Do the same actions in the same order you will when you are debugging as this affects the locations of the modules. For example, open UEFI interface -> Enter UEFI Shell -> Load EFI driver in the same order each time.**

The log files are stored in:
```bash
<workspace>/rd-infra/model-scripts/rdinfra/platforms/rdn2/rdn2
```

Following the previous section, you should still be in TF-A. In the Commands window, execute the following command to break at the start of UEFI: ``break EL2N:0xE0000000``. Execute until we are in EL2N address space. This is because the script depends on the current address space when loading in symbols.

In Arm DS, go to the scripts tab and hit "Import a script or directory" then "Import a DS or Jython script"

![ArmDS scripts alt-text#center](images/armds-script.png "Figure 4. Add ArmDS scripts")

Select the script ``~/rd-infra/uefi/edk2/ArmPlatformPkg/Scripts/Ds5/cmd_load_symbols.py``.

Enter the following parameters

``-f (<UEFI entry point>, 0x20000)`` The UEFI entry point was found earlier (0xE0000000). 0x20000 is the size which can be found in the UEFI build log.

![FV Size alt-text#center](images/armds-script.png "Figure 5. FV Size")

```command
-a -v

-i <path to UART log file> This is the path to the UART log which was produced by a running the whole UEFI process

-o <path to objdump executable> This is the path to aarch64-none-linux-gnu-objdump. 
```

The script has now been setup.
All the debug symbols have loaded, you can now start debugging!

### Debugging Boot Process

Once the debugger is connected, see the **functions** tab. Here you can search for functions to
set breakpoints.
For example, let's set a breakpoint at the entry point to DxeCore.

![dxecore alt-text#center](images/dxecore.png "Figure 6. DxeCore functions")

You can see that it has stopped at the breakpoint.

![dxecore breakpoint alt-text#center](images/dxecorebreakpoint.png "Figure 6. DxeCore breakpoint")

=======
After booting the FVP, notice that in the Non-secure AP console output, the UEFI load system helpfully shows where each driver is relocated to. The UEFI load system pre-formats the output into `add-symbol-file` directives that can be copy-and-pasted.

The log files are stored in:
```bash
/<workspace>/rd-infra/model-scripts/rdinfra/platforms/rdn2/rdn2
```

As we focus on the ``uart-0-nsec`` console, we can use ``grep`` to find all the symbol files. 
```bash
grep add-symbol-file refinfra-*-uart-0-nsec-*
```

![grep uart logs alt-text#center](images/grep.png "Figure 1. Grep UART logs")

We can then copy these lines and append them to the list of symbol files, as before.

UEFI runs in EL2, so modify the end of each line to be ``EL2:<address>``.

![uefi symbol files alt-text#center](images/uefi_symbol_files.png "Figure 3. Add uefi symbol files")

Once the debugger is connected, see the **functions** tab. Here you can search for functions to
set breakpoints. For example, let's set a breakpoint at the entry point to PEI. 

![peicore alt-text#center](images/peicore.png "Figure 4. PeiCore functions")

You can see that it has stopped at the breakpoint.

>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)
### If using Arm Development Studio version <2023.1

Older versions of Arm Development Studio have Beta support for DWARF 5 formats. EDK2 builds the debug files in DWARF 5
format.

In order to load the debug files properly, follow the instructions [here](https://developer.arm.com/documentation/101470/2023-0/Reference/Standards-compliance-in-Arm-Debugger).

These instructions state that you must enable the LLVM DWARF parser to use DWARF 5 format. To enable the LLVM DWARF parser, do the following.

1. Select **Window**  > **Preferences**. 
2. Then, in the **Preferences** dialog box, navigate to **Arm DS** > **Debugger** > **DWARF Parser**. 
3. Select the **Use LLVM DWARF parser** checkbox and click **Apply and Close**.

<<<<<<< HEAD
![enable llvm alt-text#center](images/enable_llvm.png "Figure 7. Enable LLVM")
=======
![enable llvm alt-text#center](images/enable_llvm.png "Figure 5. Enable LLVM")
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

