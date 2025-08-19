---
# User change
title: "Debug RSE from reset"

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Debug RSE from reset

Let us start by debugging the initial code that executes on the Cortex-M55 within the RSE block.

### Launch FVP

Start a new `tmux` session for the FVP (if necessary):
```command
tmux new-session -s arm-auto-solutions
```
and navigate to your code repository.

To debug from reset, launch the FVP with the Iris server but do not run. This will hold the FVP in the initial reset condition.

```command
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose -- --iris-server --iris-port 7100"
```
The FVP will start and emit various informational messages. Once initialized you should see something similar to:

```output
...
Info: RD_Aspen: RD_Aspen.css.smb.rse_flashloader: FlashLoader: Saved 64MB to file '~/arm-auto-solutions/build/tmp_baremetal/deploy/images/fvp-rd-aspen/rse-flash-image.img'

Info: RD_Aspen: RD_Aspen.ros.flash_loader: FlashLoader: Saved 128MB to file '~/arm-auto-solutions/build/tmp_baremetal/deploy/images/fvp-rd-aspen/ap-flash-image.img'
```

Note that execution has not started.

### Connect the debugger

Using the `RSE` connection created in the previous section, connect the debugger to the FVP. Observe that the processor is stopped before the first instruction has been executed.

In fact, the FVP is configured to have the vector table (`VTOR_S`) start at `0x11000000`, and it you inspect memory at that address the vector table will be populated. However no debug information is visible. Debug information must be loaded.

In the `Debug Pane`, select `Load...` from the pane menu, and select `Add Symbols file`.

Browse to the `bl1_1.axf` file which is likely at:

``` bash
/arm-auto-solutions/build/tmp_baremetal/work/fvp_rd_aspen-poky-linux/trusted-firmware-m/2.1.0/build/bin/bl1_1.axf
```
Debug symbols will be loaded, but likely no source will be displayed. This is because the build was performed within the virtual environment but the debugger is running outside of that.

You will be prompted to enter a path substitution to locate the sources. You can refer to the lowest common path so that all subsequent source files will also be located successfully.

``` bash
/usr/src/debug/trusted-firmware-m/2.1.0/
/arm-auto-solutions/build/tmp_baremetal/work/fvp_rd_aspen-poky-linux/trusted-firmware-m/2.1.0/git/tfm/"
```
Finally, to perform a single instruction step (`stepi`) to allow the processor to fetch the address of the `Reset_Handler` and stop there.

You can now step through the code, set breakpoints, and inspect the target as the code proceeds.

### Automate setup

For convenience, it is possible to automate these actions every time you connect by entering them as `Debugger Commands` in the `.launch` configuration.

Open (double-click) the `.launch` file, and navigate to the `Debugger` pane.

Enable `Execute debugger commands`, and enter the following (note pathing for your setup). You can copy the exact commands from the `Command` or `History` pane whilst performing the above GUI configuration.

It is recommended to have an explicit `stop` command as symbols cannot be loaded whilst the target is running.

``` text
stop

add-symbol-file /arm-auto-solutions/build/tmp_baremetal/work/fvp_rd_aspen-poky-linux/trusted-firmware-m/2.1.0/build/bin/bl1_1.axf

set substitute-path /usr/src/debug/trusted-firmware-m/2.1.0/ /arm-auto-solutions/build/tmp_baremetal/work/fvp_rd_aspen-poky-linux/trusted-firmware-m/2.1.0/git/tfm/

stepi
```
![Debugger pane](debugger_commands.png)
