---
title: Debugging BL31
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Debugging BL31 
Setting a breakpoint for BL1 was simple enough, but how do we set a breakpoint for BL31? In the
tabs panel at the bottom, click the plus and add other tabs. Here are multiple other tabs
available such as Register View, Memory View, and others. For this example, we are only interested in the **Functions** tab.

![add functions alt-text#center](images/add_functions.png "Figure 1. Add functions tab")

From here, search for ``bl31_entrypoint`` using the flashlight icon and set a breakpoint. Press continue. 

![bl31 breakpoint 1 alt-text#center](images/bl31_breakpoint-1.png "Figure 2. BL31 breakpoint 1")

Observe the application processor console output. TF-A will proceed from BL1 to BL2 to BL31.
After reaching BL31, Neoverse N2 Core 0 stops on the breakpoint.

![bl31 breakpoint 2 alt-text#center](images/bl31_breakpoint-2.png "Figure 3. BL31 breakpoint 2")
