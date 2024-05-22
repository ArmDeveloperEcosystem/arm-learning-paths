---
# User change
title: Run the example on FVP and debug with Arm Debugger

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Run the application on an FVP

The application can be run directly on an FVP included in Arm Development Studio.

```command
FVP_MPS2_Cortex-M3.exe -a target/thumbv7m-none-eabi/debug/examples/armds
```

{{% notice Optional %}}
To disable FVP visualization (which can reduce the start time) add the command option:

`-C fvp_mps2.mps2_visualisation.disable-visualisation=1`

This option has no other effect on the behavior of the FVP.
{{% /notice %}}

The application will run to completion on the FVP, and you will see output similar to:

```output
Total sum to 1 is 1
Calculated sum is 1

Total sum to 2 is 3
Calculated sum is 3
...
```

## Run the application on FVP within Arm Debugger

Though Rust applications are not officially supported by the debugger, the DWARF5 debug format has been the default since the 6.0 (Arm Development Studio 2023.1) release. 

This means that Rust applications can generally be debugged.

### Configure the IDE for Rust source files

By default, Arm Development Studio is not aware of Rust (`.rs`) source files.

Navigate the menu to `Window` > `Preferences`, and then `General` > `Editors` > `File Associations`.

Click `Add`, and enter `.rs` file type.

Highlight the `.rs` file type from the list, and add the `C/C++ Editor` as the `Associated editor`. Click `Apply and Close`.

### Create a Debug Connection

Launch the Arm Debugger, and create a `New` > `Model Connection` from the `File` menu.

When prompted, provide a meaningful debug connection name.

Select the `MPS2_Cortex_M3` FVP from the list of `Arm FVP (Installed with Arm DS)`. Click `Finish`.

When the `Edit Configuration` pane appears, navigate to `Files`, and locate the above `armds` executable as the `Application on host to download`.

In the `Debugger` tab, select either `Debug from entry point` or `Debug from symbol` (`main`) as preferred. The entry point is the low level library code, it is unlikely you have access to this source, but if you do, you should be prompted to `Set Path Substitution` to refer to where this code is stored.

To set a breakpoint (at `main`) either use the `Functions` view, or the `Commands` view:
``` command
break main
```
and click the `Run` icon (or enter `continue` on command line). Execution will stop at `main`, and the `armds.rs` source file will open.


## Explore the example

### Source

The debugger shows that execution has stopped at `main`. It is possible to set breakpoints directly in this source code by double clicking on the left-hand margin.

Set a breakpoint at the `sum += n;` line within the `for` loop. Run to this point.

### Functions

The `Functions` view will list all function symbols. Many of the library functions have their names `mangled`. However you will be able to locate `main` therein.

### Disassembly

The `Disassembly` view will show the low level code, along with (mangled) symbol names where possible.

### Target Console

The text output of the `hprintln` calls will be seen in this view.

### Variables

The variables view will display the values of the variables as they change.

The `sum` and `n` variables are displayed as expected.

The `start` and `end` of the implicit `for` loop counter `iter` are shown.

Run to the line:
```rust
   hprintln!("Calculated sum is {}\n", calc).unwrap();
```
As a non-mutable variable, `calc` only exists while it is in use. Observe that it appears in the variables view.

Run the application, and observe the variable values change as the code progresses.
