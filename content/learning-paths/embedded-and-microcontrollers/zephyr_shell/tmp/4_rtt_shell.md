---
title: RTT shell
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up the RTT shell example

In this section, you will build a Zephyr application that enables the **Zephyr Shell RTT backend**, flash it with Workbench for Zephyr, connect with **J-Link RTT Viewer**, and run shell commands over the debug connection.

The example uses the **Silicon Labs xG27 Dev Kit (BRD2602A)** because it has an onboard SEGGER J-Link, so a single USB cable handles both flashing and the RTT data channel with no extra hardware. Any other Zephyr-supported board works as well, as long as you can connect a J-Link interface to it. That can be:

- An onboard J-Link, like the one on the xG27 Dev Kit, several Nordic Semiconductor development kits, and many ST and NXP boards.
- An external J-Link probe (for example, J-Link EDU, J-Link BASE, or J-Link PLUS) wired to the SWD pins of any Cortex-M board.

The "Switch to a different board" section near the end of this page shows how to change boards on an existing project without recreating it.

RTT, or Real Time Transfer, is a SEGGER J-Link protocol that transfers data through the debug probe by using a small buffer in target RAM. It is useful for shell access because it does not require UART pins, a USB-to-serial adapter, or a network connection.

The Zephyr Shell RTT backend maps shell input and output to SEGGER RTT channel 0.

## Create the project

In the **Workbench for Zephyr** panel, select **New Application** to open the **Create a new Zephyr Application Project** wizard. Fill in the following fields:

1. **Select West Workspace**: select your initialized West workspace for Zephyr v4.4.0.
2. **Select Toolchain**: select `zephyr-sdk-1.0.1`.
3. **Select Board**: select **Silabs xG27 Dev Kit** (Zephyr identifier `xg27_dk2602a`).
4. **Application type**: select **Create new application**.
5. **Select Sample project**: select `hello_world`.
6. **Project Name**: enter `xg27_rtt_shell`.
7. **Project Location**: select the directory where you want to create the project.
8. **Debug preset**: leave checked.
9. **Advanced options**: leave at the defaults.

Select **Create** to generate the project. The wizard layout is the same as the one shown in the previous section, with the Board, Sample project, and Project Name set for the xG27 example.

## Configure the application

The `hello_world` sample provides a working `CMakeLists.txt`, `prj.conf`, and `src/main.c`. Leave `CMakeLists.txt` unchanged, and replace `prj.conf` and `src/main.c` with the contents below.

### prj.conf

```bash
CONFIG_SHELL=y
CONFIG_LOG=y
CONFIG_UART_CONSOLE=n

CONFIG_USE_SEGGER_RTT=y
CONFIG_SHELL_BACKEND_RTT=y

CONFIG_MAIN_STACK_SIZE=2048
```

`CONFIG_UART_CONSOLE=n` disables the UART console so that shell and log output use RTT instead. This is useful when UART pins are unavailable or when you want to keep shell access on the debug connection.

### src/main.c

```c
#include <zephyr/logging/log.h>

LOG_MODULE_REGISTER(app_main, LOG_LEVEL_INF);

int main(void)
{
    LOG_INF("RTT shell backend demo on %s", CONFIG_BOARD);
    LOG_INF("Open J-Link RTT Viewer and use the rtt:~$ prompt");
    return 0;
}
```

No shell initialization code is required in `main.c`. Zephyr registers and starts the RTT shell backend from the Kconfig options in `prj.conf`.

## Build and flash

Connect the xG27 Dev Kit to your host computer over USB.

In the **Workbench for Zephyr** panel, select your project and build configuration. Select **Build**, then select **Flash**.

The xG27 Dev Kit uses the `jlink` runner. The board configuration passes the J-Link device name `EFR32BG27CxxxF768`, so no extra runner arguments are needed for this example.

## Connect with J-Link RTT Viewer

After flashing, the board resets and starts running. Open **J-Link RTT Viewer** and configure the connection with:

- **Connection to J-Link**: USB
- **Specify Target Device**: `EFR32BG27CxxxF768`
- **Target Interface & Speed**: SWD, 20000 kHz
- **RTT Control Block**: Auto Detection

Select **OK** to connect.

<p style="text-align:center;">
  <img src="/learning-paths/embedded-and-microcontrollers/zephyr_shell/images/jlink-RTTViewer-configuration.png"
       alt="J-Link RTT Viewer Configuration dialog with USB connection, target device EFR32BG27CxxxF768, SWD interface at 20000 kHz, and RTT Control Block set to Auto Detection."
       width="420"
       style="max-width:100%;height:auto;" />
  <br/>
  <em>J-Link RTT Viewer connection dialog</em>
</p>

## Check the shell prompt

In J-Link RTT Viewer, open **Terminal 0**. You should see the boot log followed by the shell prompt:

```output
rtt:~$ *** Booting Zephyr OS build v4.4.0 ***
rtt:~$ [00:00:00.001,037] <inf> app_main: RTT shell backend demo on xg27_dk2602a
rtt:~$ [00:00:00.001,037] <inf> app_main: RTT shell: attach RTT viewer, prompt is rtt:~$
rtt:~$
```

The `rtt:~$` prompt confirms that the RTT shell backend is active. Type commands directly in the Terminal 0 input area.

The boot banner and the `<inf>` log lines are prefixed with `rtt:~$` because `SHELL_LOG_BACKEND` is enabled by default when `CONFIG_SHELL=y` and `CONFIG_LOG=y` are both set, so log output is routed through the active shell backend.

## Run shell commands

Type each of the following commands at the `rtt:~$` prompt in Terminal 0:

```bash
kernel version
kernel uptime
kernel thread list
```

The screenshot below shows the output you should see in J-Link RTT Viewer:

<p style="text-align:center;">
  <img src="/learning-paths/embedded-and-microcontrollers/zephyr_shell/images/jlink-RTTViewer-output.png"
       alt="J-Link RTT Viewer Terminal 0 showing the kernel version and kernel thread list output on xg27_dk2602a, with shell_uart, shell_rtt, logging, and idle threads listed."
       width="640"
       style="max-width:100%;height:auto;" />
  <br/>
  <em>RTT Viewer Terminal 0 with shell command output</em>
</p>

The `*` next to `shell_rtt` in the thread list marks the currently running thread, which is the shell that just executed the command.

{{% notice Note %}}
Application log messages such as `LOG_INF` and `LOG_WRN` appear in Terminal 0 with the shell prompt. This is expected when both `CONFIG_SHELL=y` and `CONFIG_LOG=y` are enabled.
{{% /notice %}}

## Debug while RTT is connected

You can run a debug session in Workbench for Zephyr while J-Link RTT Viewer is connected. The GDB debug session and RTT terminal use separate J-Link channels.

To start debugging, select your build configuration in the **Workbench for Zephyr** panel and select **Debug**. You can set breakpoints, inspect variables, and step through code in Visual Studio Code while RTT Viewer remains open.

When execution stops at a breakpoint, shell output pauses with the target. After you continue execution, the RTT shell becomes responsive again.

## Switch to a different board

The application is portable across any Zephyr-supported board that has a J-Link interface, because the RTT backend is selected through Kconfig and there is no board-specific code in `main.c`. You do not need to recreate the project to test it on another board.

To change the target board on an existing project:

1. Open the **Workbench for Zephyr** panel in the VS Code Activity Bar.
2. Expand the **Applications** section. The project you created appears with its current board name underneath.
3. Right-click the board name and select **Change board**. Pick a new J-Link-capable board from the list.
4. Right-click the application and select **Clean** to remove the previous build artifacts.
5. Right-click the application and select **Build (pristine)** to rebuild the project from scratch with the new board configuration.

After the pristine build completes, flash the board as before. The same `prj.conf` and `main.c` work without changes. Reopen J-Link RTT Viewer and update the **Specify Target Device** field to the new board's J-Link device name (you can find it in the board's Zephyr `runners.yaml` under the `jlink` entry).

{{% notice Note %}}
A pristine build is required when you change the board because Workbench for Zephyr caches board-specific generated files (device tree, Kconfig, linker script) in the build directory. Without a clean rebuild, the previous board's configuration leaks into the new build and produces incorrect binaries.
{{% /notice %}}

## What you accomplished

You built and flashed a Zephyr application that enables the Shell RTT backend on the Silicon Labs xG27 Dev Kit. You disabled the UART console, routed shell access through SEGGER RTT, connected with J-Link RTT Viewer, and ran Zephyr shell commands over the debug connection.
