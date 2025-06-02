---
# User change
title: "Run the examples on the FVP"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Run an example

Navigate to the evaluation kit repository.

```bash
cd ml-embedded-evaluation-kit/
```

The built examples (`.axf` files) will be located in a `cmake-*/bin` folder based on the build configuration used.

Navigate into that folder, and list the images. For example:

```bash
cd cmake-build-mps4-sse-320-ethos-u85-256-gnu/bin/
 
ls *.axf
```

Use `-a` to specify the application to load to the FVP.

Use `-C mps4_board.subsystem.ethosu.num_macs` to configure the Ethos-U component of the model.

{{% notice Note %}}
The number of NPU MACs specified in the build MUST match the number specified in the FVP. Else an error similar to the below will be emitted.

```
E: NPU config mismatch. npu.macs_per_cc=E: NPU config mismatch..
```
{{% /notice %}}

You can list all available parameters by running the FVP executable with the `--list-params` option, for example:

```console
FVP_Corstone_SSE-320 --list-params > parameters.txt
```


### Run the application

```console
FVP_Corstone_SSE-320								\
    -C mps4_board.subsystem.ethosu.num_macs=256			\
    -C mps4_board.visualisation.disable-visualisation=1	\
    -C vis_hdlcd.disable_visualisation=1				\
    -a ethos-u-kws.axf
```

If adding configuration options becomes cumbersome, it can be easier to specify them in a configuration file (remove the `-C` option) and then use that on the command line (`-f`).

#### config.txt
```
mps4_board.subsystem.ethosu.num_macs=256
mps4_board.visualisation.disable-visualisation=1
vis_hdlcd.disable_visualisation=1
```

The command line becomes:
```console
FVP_Corstone_SSE-320 -f config.txt -a ethos-u-kws.axf
```

The application executes and identifies words spoken within audio files.

Repeat with any of the other built applications.

Full instructions are provided in the evaluation kit [documentation](https://review.mlplatform.org/plugins/gitiles/ml/ethos-u/ml-embedded-evaluation-kit/+/HEAD/docs/quick_start.md).


## Addendum: Speed up FVP execution

By default, the examples are built with Ethos-U timing enabled. This provides benchmarking information, but the result is that the FVP executes relatively slowly.

The build system has a macro `-DETHOS_U_NPU_TIMING_ADAPTER_ENABLED` defined to control this.

Modify the command `build_default.py` passes to `cmake` to include this setting (`OFF`). Search for `cmake_command` and modify as follows:

#### build_default.py
```
cmake_command = (
    f"{cmake_path} -B {build_dir} -DTARGET_PLATFORM={target_platform}"
    f" -DTARGET_SUBSYSTEM={target_subsystem}"
    f" -DCMAKE_TOOLCHAIN_FILE={cmake_toolchain_file}"
    f" -DETHOS_U_NPU_ID={ethos_u_cfg.processor_id}"
    f" -DETHOS_U_NPU_CONFIG_ID={ethos_u_cfg.config_id}"
    " -DTENSORFLOW_LITE_MICRO_CLEAN_DOWNLOADS=ON"
    " -DETHOS_U_NPU_TIMING_ADAPTER_ENABLED=OFF"
)
```

Rebuild the applications as before, for example:
```
./build_default.py --npu-config-name ethos-u85-256 --toolchain gnu --make-jobs 8
```

Add additional configuration option (`mps4_board.subsystem.ethosu.extra_args`) to the FVP command line:

#### config.txt
```
mps4_board.subsystem.ethosu.num_macs=256
mps4_board.visualisation.disable-visualisation=1
vis_hdlcd.disable_visualisation=1
mps4_board.subsystem.ethosu.extra_args="--fast"
```

Run the application again, and notice how much faster execution completes.

```console
FVP_Corstone_SSE-320 -f config.txt -a ethos-u-kws.axf
```

{{% notice Note %}}
Do not use fast execution mode whilst benchmarking performance.
{{% /notice %}}

