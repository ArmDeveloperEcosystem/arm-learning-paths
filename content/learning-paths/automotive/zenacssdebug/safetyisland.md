---
# User change
title: "Debug Safety Island code"

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Debug Safety Island code from beginning

The Safety Island (Cortex-R82AE) is released from reset by the RSE code, and so the RSE code must proceed to that point before the Safety Island core can execute.

### Launch FVP

If necessary, restart the FVP in the reset state as before, and reconnect `RSE`.

```command
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose -- --iris-server --iris-port 7100"
```

Set up the `SI` connection in a similar way as the `RSE` connection. Use the following commands in the `Debugger` pane. This will load debug symbols and performing the necessary path substitution. You can then set a breakpoint on the entry point of the `SI` code, `arch_exception_reset`.

``` text
stop
add-symbol-file /arm-auto-solutions/build/tmp_baremetal/deploy/images/fvp-rd-aspen/si0_ramfw.elf
set substitute-path /usr/src/debug/scp-firmware/2.14.0/ /arm-auto-solutions/build/tmp_baremetal/work/fvp_rd_aspen-poky-linux/scp-firmware/2.14.0/git/
b arch_exception_reset
```

{{% notice Note %}}
Exact paths may differ for your set up.
{{% /notice %}}

### Start execution

Select the `RSE` connection in the `Debug Control` pane, and start execution (this will be unavailable in the `SI` connection, as that is currently powered down).

The `RSE` code will run until the point that the `SI` is enabled. This is reflected in the output log.

``` output
[INF] BL2: SI CL0 post load start
```

#### Full output log

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
