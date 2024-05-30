---
# User change
title: Run the example on FVP and debug with Arm Debugger

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Run the application on an FVP

You can run the application directly on an FVP that the Arm Development Studio includes:

```command
FVP_MPS2_Cortex-M3.exe -a target/thumbv7m-none-eabi/debug/examples/armds
```

{{% notice Optional %}}
To disable FVP visualization, which can reduce the start time, add the following command option:

`-C fvp_mps2.mps2_visualisation.disable-visualisation=1`

This option has no other effect on the behavior of the FVP.
{{% /notice %}}

The application runs to completion on the FVP, and you will see output similar to:

```output
Total sum to 1 is 1
Calculated sum is 1

Total sum to 2 is 3
Calculated sum is 3
...
```

## Run the application on FVP within Arm Debugger

Though Rust applications are not officially supported by the debugger, the DWARF5 debug format has been the default since the 6.0 (Arm Development Studio 2023.1) release. 

This means that in general, you can debug Rust applications.

### Configure the IDE for Rust source files

By default, Arm Development Studio is not aware of Rust (`.rs`) source files.

Navigate the menu to `Window` > `Preferences`, and then `General` > `Editors` > `File Associations`.

Click `Add`, and enter `.rs` file type.

Highlight the `.rs` file type from the list, and add `C/C++ Editor` as the `Associated editor`. Click `Apply and Close`.

### Create a Debug Connection

Launch the Arm Debugger, and create a `New` > `Model Connection` from the `File` menu.

When prompted, provide a meaningful debug connection name.

Select the `MPS2_Cortex_M3` FVP from the list of `Arm FVP (Installed with Arm DS)`, and click `Finish`.

When the `Edit Configuration` pane appears, navigate to `Files`, and locate the above `armds` executable as the `Application on host to download`.

In the `Debugger` tab, select either `Debug from entry point` or `Debug from symbol` (`main`), as preferred. The entry point is the low-level library code, it is unlikely you have access to this source, but if you do, you should be prompted to `Set Path Substitution` to refer to where this code is stored.

To set a breakpoint (at `main`) either use the `Functions` view, or the `Commands` view:
``` command
break main
```
and click the `Run` icon (or enter `continue` on command line). Execution will stop at `main`, and the `armds.rs` source file will open.


## Explore the example

### Source

The debugger shows that execution has stopped at `main`. It is possible to set breakpoints directly in this source code by double-clicking on the left-hand margin.

Set a breakpoint at the `sum += n;` line within the `for` loop. Run to this point.

### Functions

The `Functions` view lists all function symbols. Many of the library functions have their names `mangled`. However you will be able to locate `main` in there.

### Disassembly

The `Disassembly` view shows the low-level code, along with mangled symbol names where possible.

### Target Console

You can see the text output of the `hprintln` calls in this view.

### Variables

The variables view displays the values of the variables as they change.

The `sum` and `n` variables are displayed as expected.

The `start` and `end` of the implicit `for` loop counter `iter` are shown.

Run to the line:
```rust
   hprintln!("Calculated sum is {}\n", calc).unwrap();
```
As a non-mutable variable, `calc` only exists while it is in use. Observe that it appears in the variables view.

Run the application, and observe the variable values change as the code progresses.
