---
title: Debugging BL33 / UEFI
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Debugging BL33 / UEFI
Adding symbol files for UEFI requires you to boot the FVP once without debugging to retrieve the symbol file
locations and memory addresses. After booting the FVP, notice that in the non secure AP console output,
the UEFI load system helpfully shows where each driver is relocated to. In fact the UEFI load system pre-formats
the output into add-symbol-file directives that can just be copy-pasted!

The log files are stored in:
```bash
/<workspace>/rd-infra/model-scripts/rdinfra/platforms/rdn2/rdn2
```

Since we are interested in the ``uart-0-nsec`` console, we can use ``grep`` to find all the symbol files. 
```bash
grep add-symbol-file refinfra-*-uart-0-nsec-*
```

![grep uart logs alt-text#center](images/grep.png "Figure 1. Grep UART logs")

We can then copy these lines and append them to the list of symbol files like before.
Note that UEFI runs in EL2, so we must modify the end of the line to be ``EL2:<address>``.

![uefi symbol files alt-text#center](images/uefi_symbol_files.png "Figure 3. Add uefi symbol files")

ArmDS currently has [BETA] support for DWARF 5 formats. EDK2 builds the debug files in DWARF 5
format. In order to properly load the debug files, follow the
instructions [here](https://developer.arm.com/documentation/101470/2023-0/Reference/Standards-compliance-in-Arm-Debugger)

These instructions state that you must enable the LLVM DWARF parser to use DWARF 5 format.
To enable the LLVM DWARF parser, do the following. In the Arm Development Studio IDE, 

1. Select **Window**  > **Preferences**. 
2. Then, in the **Preferences** dialog box, navigate to **Arm DS** > **Debugger** > **DWARF Parser**. 
3. Select the **Use LLVM DWARF parser** checkbox and click **Apply and Close**.

![enable llvm alt-text#center](images/enable_llvm.png "Figure 4. Enable LLVM")

Once the debugger is connected, see the functions tab. Here you can search for functions to
set breakpoints. For example, let's set a breakpoint at the entry point to PEI. 

![peicore alt-text#center](images/peicore.png "Figure 5. PeiCore functions")

You will see that it has stopped at the breakpoint.

