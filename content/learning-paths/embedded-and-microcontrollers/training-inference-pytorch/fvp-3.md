---
title: Deploy the model on Corstone-320 FVP  
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now run the model on the Corstone-320 with the following command:

```bash
FVP_Corstone_SSE-320 \
-C mps4_board.subsystem.ethosu.num_macs=256 \
-C mps4_board.visualisation.disable-visualisation=1 \
-C vis_hdlcd.disable_visualisation=1                \
-C mps4_board.telnetterminal0.start_telnet=0        \
-C mps4_board.uart0.out_file='-'                    \
-C mps4_board.uart0.shutdown_on_eot=1               \
-a "$ET_HOME/examples/arm/executor_runner/cmake-out/arm_executor_runner"
```

{{% notice Note %}}

The argument `mps4_board.visualisation.disable-visualisation=1` disables the FVP GUI. This can speed up launch time for the FVP.

{{% /notice %}}


#todo: VERIFY

Observe that the FVP loads the model file.
```output
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
telnetterminal5: Listening for serial connection on port 5003
I [executorch:arm_executor_runner.cpp:412] Model in 0x70000000 $
I [executorch:arm_executor_runner.cpp:414] Model PTE file loaded. Size: 3360 bytes.
```

You've now ......





IGNORE anything BELOW:

