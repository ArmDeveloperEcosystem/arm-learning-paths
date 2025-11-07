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
add-symbol-file "/arm-auto-solutions/build/tmp_baremetal/deploy/images/fvp-rd-aspen/si0_ramfw.elf"
set substitute-path "/usr/src/debug/scp-firmware/2.16.0+git/" "/arm-auto-solutions/build/tmp_baremetal/work/fvp_rd_aspen-poky-linux/scp-firmware/2.16.0+git/git/"
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
[INF] [CC3XX] Init OK PIDR0: 0xc1
[INF] Starting TF-M BL1_1
[INF] Jumping to BL1_2
[INF] Starting TF-M BL1_2
[INF] Attempting to boot image 0
[INF] BL2 image decrypted successfully
[INF] BL2 image validated successfully
[INF] Jumping to BL2
[INF] Starting bootloader
[INF] [CC3XX] Init OK PIDR0: 0xc1
[INF] PSA Crypto init done, sig_type: EC-P256
[INF] BL2: SI CL1 not present, skip loading
[INF] BL2: SI CL0 pre load start
[INF] BL2: SI CL0 pre load complete
[INF] Primary   slot: version=0.0.7+0
[INF] Image 3 Secondary slot: Image not found
[INF] Image 3 RAM loading to 0x70083c00 is succeeded.
[INF] Key 0 hash found for image 3
[INF] Image 3 loaded from the primary slot
[INF] BL2: SI CL0 post load start
[INF] BL2: SI ATU region 0: [0x80000000 - 0xbfffffff]->[0x1_00000000 - 0x1_3fffffff]
[INF] BL2: SI ATU region 1: [0xc0000000 - 0xcfffffff]->[0x1_40000000 - 0x1_4fffffff]
[INF] BL2: SI ATU region 2: [0xd0000000 - 0xd001ffff]->[0x20000_d8000000 - 0x20000_d801ffff]
[INF] BL2: SI ATU region 3: [0xd0020000 - 0xd002ffff]->[0x20000_d0200000 - 0x20000_d020ffff]
[INF] BL2: SI ATU region 4: [0xd0030000 - 0xd003ffff]->[0x20000_d0400000 - 0x20000_d040ffff]
[INF] BL2: SI ATU region 5: [0xd0040000 - 0xd006ffff]->[0x20000_d0100000 - 0x20000_d012ffff]
[INF] BL2: SI ATU region 6: [0xe0030000 - 0xe0031fff]->[0x0_00000000 - 0x0_00001fff]
[INF] BL2: SI ATU region 7: [0xe0130000 - 0xe0135fff]->[0x0_00100000 - 0x0_00105fff]
```
