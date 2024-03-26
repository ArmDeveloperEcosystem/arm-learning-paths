---
title: Debugging SCP
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Debugging SCP
{{% notice %}}
At the time of writing this guide, SCP firmware debug uses "-Og" argument. This optimizes some variables. That makes debugging difficult. To replace "-Og" with "-O0", do the following:
   
* Navigate to ``rd-infra/scp/cmake/Toolchain``
* See <compiler>_Baremetal.cmake files
* Modify the one for the compiler you use. For example, for GCC modify GNU-Baremetal.cmake:

``string(APPEND CMAKE_${language}_FLAGS_DEBUG_INIT "-Og")`` 

to 

``string(APPEND CMAKE_${language}_FLAGS_DEBUG_INIT "-O0")``
{{% /notice %}}

After starting the model, click **Create a new debug connection...** from the **Debug Control** panel.

![new debug connection alt-text#center](images/new_debug_connection.png "Figure 1. New debug connection")

Create a connection name. You may choose any name you prefer.

![debug connection name alt-text#center](images/debug_connection_name.png "Figure 2. Debug connection name")

Next, click on **Add a new model...**.

![add new model alt-text#center](images/add_new_model.png "Figure 3. Add new model")

Make sure the Model Interface is selected to be **CADI**. 
Click **Browse for model running on local host**.
Select the correct model and click finish.

![connect model alt-text#center](images/connect_model.png "Figure 4. Connect model")

In the **Edit configuration and launch** panel, in the **Connection** tab, select the correct target. In this example, select **ARM_Cortex-M7_1**. 

![select target alt-text#center](images/select_cortexm7.png "Figure 5. Select target")

In the **Files** panel, select **Load Symbols from file**, **File System**, and select the **SCP RAMFW ELF** file, located at ``rd-infra/scp/output/rdn2/0/scp_ramfw/bin/rdn2-bl2.elf``.

![scp symbols alt-text#center](images/scp_symbols.png "Figure 6. Load SCP symbols")

Select apply then debug. DS will now connect to the model and start debugging.

Once connected, we can set breakpoints in the source code. This can be done by searching for the function in the **Functions** tab, or by double clicking next to the line number.

Here, you can see that we've set a breakpoint at ``cmn700_discovery()``. You'll see that it has stopped at that breakpoint upon continuing the code.

![scp breakpoint 1 alt-text#center](images/scp_breakpoint1.png "Figure 7. cmn700_discovery() breakpoint")

We'll set another breakpoint at a debug print statement. 

![scp breakpoint 2 alt-text#center](images/scp_breakpoint2.png "Figure 8. SCP breakpoint 2")

You can see the output in the SCP UART window.

