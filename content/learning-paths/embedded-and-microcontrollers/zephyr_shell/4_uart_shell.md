---
title: UART shell
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up the UART shell example

In this section, you will build a Zephyr application that enables the UART shell backend, flash it with Workbench for Zephyr, connect with a UART terminal application, and run shell commands over the USB serial connection.

The example uses the **FRDM-MCXN947** because it provides an onboard CMSIS-DAP / LinkServer debug interface together with a USB UART connection that can be accessed from a serial terminal application such as PuTTY on Windows or the built-in `screen` utility on macOS.

The "Switch to a different board" section near the end of this page shows how to change boards on an existing project without recreating it.

UART shell access uses the board's USB serial interface and does not require additional debug hardware or network connectivity.

The Zephyr UART shell backend maps shell input and output to the active UART console.

## Create the project

In the **Workbench for Zephyr** panel, select **New Application** to open the **Create a new Zephyr Application Project** wizard. Fill in the following fields:

1. **Select West Workspace**: select your initialized West workspace for Zephyr v4.4.0.
2. **Select Toolchain**: select `zephyr-sdk-1.0.1`.
3. **Select Board**: select **FRDM-MCXN947** (Zephyr identifier `frdm_mcxn947/mcxn947/cpu0`).
4. **Application type**: select **Create new application**.
5. **Select Sample project**: select `hello_world`.
6. **Project Name**: enter `frdm_uart_shell`.
7. **Project Location**: select the directory where you want to create the project.
8. **Debug preset**: leave checked.
9. **Advanced options**: leave at the defaults.

Select **Create** to generate the project.

## Configure the application

The `hello_world` sample provides a working `CMakeLists.txt`, `prj.conf`, and `src/main.c`. Leave `CMakeLists.txt` unchanged, and replace `prj.conf` and `src/main.c` with the contents below.

### prj.conf

```bash
CONFIG_SHELL=y
CONFIG_LOG=y

CONFIG_SERIAL=y
CONFIG_CONSOLE=y
CONFIG_UART_CONSOLE=y
CONFIG_SHELL_BACKEND_SERIAL=y

CONFIG_MAIN_STACK_SIZE=2048
```

The UART shell backend routes shell input and output through the board's USB serial interface.

### src/main.c

```c
#include <zephyr/logging/log.h>

LOG_MODULE_REGISTER(app_main, LOG_LEVEL_INF);

int main(void)
{
    LOG_INF("UART shell backend demo on %s", CONFIG_BOARD);
    LOG_INF("Open PuTTY at 115200 baud and use the uart:~$ prompt");
    return 0;
}
```

No shell initialization code is required in `main.c`. Zephyr registers and starts the UART shell backend from the Kconfig options in `prj.conf`.

## Build and flash

Connect the FRDM-MCXN947 board to your host computer over USB.

In the **Workbench for Zephyr** panel, select your project and build configuration. Select **Build**, then select **Flash**.

The FRDM-MCXN947 uses the onboard CMSIS-DAP / LinkServer interface for flashing and debugging.

## Connect with a UART terminal

After flashing, the board resets and starts running. Open a UART terminal application and connect to the board's serial port.

### Windows with PuTTY

Configure PuTTY with:

- **Connection type**: `Serial`
- **Serial line**: your board's COM port
- **Speed**: `115200`

Select **Open** to connect.

<p style="text-align:center;">
  <img src="/learning-paths/embedded-and-microcontrollers/zephyr_shell/images/putty_installation.png"
       alt="PuTTY Installation"
       width="640"
       style="max-width:100%;height:auto;" />
  <br/>
  <em>PuTTY Serial Terminal Configuration</em>
</p>

### macOS with screen

Open a terminal window and identify the serial device:

```bash
ls /dev/tty.*
```

Connect with:

```bash
screen /dev/tty.usbmodemXXXX 115200
```

Replace `/dev/tty.usbmodemXXXX` with the serial device shown on your system.


## Check the shell prompt

In your UART terminal application, you should see the boot log followed by the shell prompt:

```output
uart:~$ *** Booting Zephyr OS build v4.4.0 ***
uart:~$ [00:00:00.001,037] <inf> app_main: UART shell backend demo on frdm_mcxn947
uart:~$ [00:00:00.001,037] <inf> app_main: Open PuTTY at 115200 baud and use the uart:~$ prompt
uart:~$
```

The `uart:~$` prompt confirms that the UART shell backend is active.

The boot banner and the `<inf>` log lines are prefixed with `uart:~$` because `SHELL_LOG_BACKEND` is enabled by default when `CONFIG_SHELL=y` and `CONFIG_LOG=y` are both set, so log output is routed through the active shell backend.

## Run shell commands

Type each of the following commands at the `uart:~$` prompt:

```bash
kernel version
kernel uptime
kernel thread list
```

<p style="text-align:center;">
  <img src="/learning-paths/embedded-and-microcontrollers/zephyr_shell/images/uart_shell_output.png"
       alt="Uart Shell Output"
       width="640"
       style="max-width:100%;height:auto;" />
  <br/>
  <em>Uart Shell Output </em>
</p>

The `*` next to `shell_uart` in the thread list marks the currently running thread, which is the shell that just executed the command.

{{% notice Note %}}
Application log messages such as `LOG_INF` and `LOG_WRN` appear in the terminal together with the shell prompt. This is expected when both `CONFIG_SHELL=y` and `CONFIG_LOG=y` are enabled.
{{% /notice %}}

## Debug while UART shell is connected

You can run a debug session in Workbench for Zephyr while the UART terminal remains connected.

To start debugging, select your build configuration in the **Workbench for Zephyr** panel and select **Debug**. You can set breakpoints, inspect variables, and step through code in Visual Studio Code while the UART shell remains open.

When execution stops at a breakpoint, shell output pauses with the target. After you continue execution, the UART shell becomes responsive again.

## Switch to a different board

The application is portable across many Zephyr-supported boards because the UART shell backend is selected through Kconfig and there is no board-specific code in `main.c`.

To change the target board on an existing project:

1. Open the **Workbench for Zephyr** panel in the VS Code Activity Bar.
2. Expand the **Applications** section.
3. Right-click the board name and select **Change board**.
4. Right-click the application and select **Clean**.
5. Right-click the application and select **Build (pristine)**.

{{% notice Note %}}
A pristine build is required when you change the board because Workbench for Zephyr caches board-specific generated files in the build directory.
{{% /notice %}}

## What you accomplished

You built and flashed a Zephyr application that enables the UART shell backend on the FRDM-MCXN947. You connected with a UART terminal application, opened the Zephyr shell over USB serial, and ran Zephyr shell commands from the host computer.