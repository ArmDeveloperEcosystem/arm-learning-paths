---
title: Debugging BL1
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Debugging BL1 
In the **Edit configuration and launch** panel, in the **Connection** tab, select the correct
target. In this example, we are selecting the **ARM_Neoverse-N2_0**. 

![select target alt-text#center](images/select_target.png "Figure 1. Select target")

Next, we'll add debug symbols. In the **Debugger** tab, check the **Execute debugger commands**, and add the following commands.

{{% notice %}}
If you wish to add platform specific debug files, the memory locations are in their respective ``platform_h.def`` file.
{{% /notice %}}

```
add-symbol-file "/<workspace>/rd-infra/tf-a/build/rdn2/debug/bl1/bl1.elf" EL3:0x0
add-symbol-file "/<workspace>/rd-infra/tf-a/build/rdn2/debug/bl2/bl2.elf" EL1S:0x0
add-symbol-file "/<workspace>/rd-infra/tf-a/build/rdn2/debug/bl31/bl31.elf" EL3:0x0
```

![tfa symbols alt-text#center](images/tfa-symbols.png "Figure 2. Load TF-A symbols")

These commands load the symbol files and specify the memory address where the symbols should be loaded.
Replacing <workspace> with the path to your workspace directory.
The EL and number at the end of each command (e.g. ``EL3:0``) ensure the symbols are loaded into the correct
virtual address space and at the correct memory offset; ATF uses absolute addresses for its symbols so we ensure an offset of 0.

After connecting to the running model, see that it has stopped. Set a breakpoint on the next instruction of
the TF-A and press run. In this debug panel, you will find common debugging functions like stepping, skipping, and others.

![debug options alt-text#center](images/debug_options.png "Figure 3. Debug options")

Observe the SCP console output. After SCP de-asserts reset for the NeoverseN2 Core 0, it stops on the breakpoint.

![scp terminal alt-text#center](images/scp_terminal.png "Figure 4. SCP terminal")

Finally, set a breakpoint in the function you wish to debug. In this example, we'll set a breakpoint at ``bl1_main()`` and continue. 

![bl1 breakpoint alt-text#center](images/bl1_breakpoint.png "Figure 5. BL1 breakpoint")
