---
title: Debugging SCP
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Debugging SCP
{{% notice %}}
At the time of writing this guide, SCP firmware debug uses `-Og` argument. This optimizes some variables that makes debugging difficult. To replace `-Og` with `-O0`, do the following:
   
* Navigate to `rd-infra/scp/cmake/Toolchain`
* Modify the appropriate `<compiler>-Baremetal.cmake` file for your toolchain

For example, modify `GNU-Baremetal.cmake`:

`string(APPEND CMAKE_${language}_FLAGS_DEBUG_INIT "-Og")`

to

`string(APPEND CMAKE_${language}_FLAGS_DEBUG_INIT "-O0")`
{{% /notice %}}

After starting the model, click **Create a new debug connection...** from the **Debug Control** panel.

![new debug connection alt-text#center](images/new_debug_connection.png "Figure 1. New debug connection")

Create a connection name. You may choose any name you prefer.

![debug connection name alt-text#center](images/debug_connection_name.png "Figure 2. Debug connection name")

Next, click on **Add a new model...**.

![add new model alt-text#center](images/add_new_model.png "Figure 3. Add new model")

Select the appropriate Model Interface, for example **CADI**.

Click **Browse for model running on local host**.

Select the correct model and click finish.

![connect model alt-text#center](images/connect_model.png "Figure 4. Connect model")

In the **Edit configuration and launch** panel, in the **Connection** tab, select the correct target.

For the `SCP` code, select **ARM_Cortex-M7_1**. 

![select target alt-text#center](images/select_cortexm7.png "Figure 5. Select target")

In the **Files** panel, select **Load Symbols from file**, **File System**, and select the **SCP RAMFW ELF** file, located at:

``rd-infra/scp/output/rdn2/0/scp_ramfw/bin/rdn2-bl2.elf``.

![scp symbols alt-text#center](images/scp_symbols.png "Figure 6. Load SCP symbols")

Select **Apply** then **Debug**. The debugger will now connect to the model.

Once connected, you can set breakpoints in the source code. This can be done by searching for the function in the **Functions** tab, double clicking next to the line number, or in the **Command** view.

Set a breakpoint at ``cmn700_discovery()``. Continue execution and the code will stop at that breakpoint.
```command
break cmn700_discovery
continue
```

![scp breakpoint 1 alt-text#center](images/scp_breakpoint1.png "Figure 7. cmn700_discovery() breakpoint")

Set another breakpoint at a debug print statement. 

![scp breakpoint 2 alt-text#center](images/scp_breakpoint2.png "Figure 8. SCP breakpoint 2")

Observe the output in the SCP UART window.

Disconnect from the FVP.

