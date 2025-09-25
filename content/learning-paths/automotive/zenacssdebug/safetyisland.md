---
# User change
title: "Debug Safety Island code"

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Debug Safety Island code from beginning

The Safety Island subsystem based on the Cortex-R82AE is released from reset by RSE code. To debug Safety Island from first instruction, you must let the RSE (Cortex‑M55) code reach the point where it enables Safety Island on the Zena CSS FVP.

## Launch the FVP and reconnect RSE

If necessary, start (or restart) the FVP held at reset and reconnect the RSE model connection in Arm Development Studio:

```command
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose -- --iris-server --iris-port 7100"
```

{{% notice Tip %}}
For remote debugging, add `-A` and ensure the chosen Iris port (default `7100`) is reachable.
{{% /notice %}}

## Connect the debugger to Safety Island (Cortex-R82AE)

Configure the **SI** model connection similarly to **RSE**. Add the following **Debugger commands** to load symbols, set up source path substitution, and break at the Safety Island reset entry (`arch_exception_reset`):

```text
stop
add-symbol-file /arm-auto-solutions/build/tmp_baremetal/deploy/images/fvp-rd-aspen/si0_ramfw.elf
set substitute-path /usr/src/debug/scp-firmware/2.14.0/ /arm-auto-solutions/build/tmp_baremetal/work/fvp_rd_aspen-poky-linux/scp-firmware/2.14.0/git/
b arch_exception_reset
```

{{% notice Note %}}
Paths vary by environment. Use your actual build output and source locations when adding symbols or configuring path substitution.
{{% /notice %}}

## Start execution to release Safety Island

In **Debug Control**, select the **RSE** connection and start execution (run). The **SI** connection remains unavailable to run until Safety Island is powered up.

When RSE enables Safety Island, you will see a log message like:

```output
[INF] BL2: SI CL0 post load start
```

## Full output log

The full output log is shown here for your reference:

``` output
Trying ::1...
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
[INF] Starting TF-M BL1_1
[INF] Jumping to BL1_2
[INF] Starting TF-M BL1_2
[INF] Attempting to boot image 0
[INF] BL2 image decrypted successfully
[INF] BL2 image validated successfully
[INF] Jumping to BL2
[INF] Starting bootloader
[INF] PSA Crypto init done, sig_type: EC-P256
[INF] BL2: SI CL0 pre load start
[INF] BL2: SI CL0 pre load complete
[INF] Primary   slot: version=0.0.7+0
[INF] Secondary slot: version=0.0.7+0
[INF] Image 3 RAM loading to 0x70083c00 is succeeded.
[INF] Image 3 loaded from the primary slot
[INF] BL2: SI CL0 post load start
```
