---
title: ML Profiling of an ExecuTorch model
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## ExecuTorch Profiling Tools
You can use [ExecuTorch](https://pytorch.org/executorch/stable/index.html) for running PyTorch models on constrained devices like mobile. As so many models are developed in PyTorch, this is a useful way to quickly deploy them to mobile devices, without the requirement for conversion tools such as Google's [ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) to convert them into tflite.

To get started on ExecuTorch, you can follow the instructions on the [PyTorch website](https://pytorch.org/executorch/stable/getting-started-setup). To then deploy on Android, you can also find instructions on the [Pytorch website](https://pytorch.org/executorch/stable/demo-apps-android.html). If you do not already have ExecuTorch running on Android, follow these instructions first.

ExecuTorch comes with a set of profiling tools, but currently they are aimed at Linux, and not Android. The instructions to profile on Linux are [here](https://pytorch.org/executorch/main/tutorials/devtools-integration-tutorial.html), and you can adapt them for use on Android.

## Profiling on Android

To profile on Android, the steps are the same as for [Linux](https://pytorch.org/executorch/main/tutorials/devtools-integration-tutorial.html), except that you need to generate the ETDump file on an Android device.

To start, generate the ETRecord in exactly the same way as described for the Linux instructions.

Next, follow the instructions to create the ExecuTorch bundled program that you will need to generate the ETDump. You will copy this to your Android device together with the runner program that you are about to compile.

To compile the runner program, you will need to adapt the `build_example_runner.sh` script in the instructions that are located in the `examples/devtools` subfolder of the ExecuTorch repository to compile it for Android. Copy the script and rename the file to `build_android_example_runner.sh`, ready for editing. Remove all lines with `coreml` in them, and the options dependent on it, as these are not needed for Android.

You then need to set the `ANDROID_NDK` environment variable to point to your Android NDK installation. 

At the top of the `main()` function add:

```bash
  export ANDROID_NDK=~/Android/Sdk/ndk/28.0.12674087  # replace this with the correct path for your NDK installation
  export ANDROID_ABI=arm64-v8a
```

Next, add Android options to the first `cmake` configuration line in `main()`, that configures the building of the ExecuTorch library. 

Change it to:

```bash
  cmake -DCMAKE_INSTALL_PREFIX=cmake-out \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_TOOLCHAIN_FILE="${ANDROID_NDK}/build/cmake/android.toolchain.cmake" \
      -DANDROID_ABI="${ANDROID_ABI}" \
      -DEXECUTORCH_BUILD_XNNPACK=ON \
      -DEXECUTORCH_BUILD_EXTENSION_DATA_LOADER=ON \
      -DEXECUTORCH_BUILD_EXTENSION_MODULE=ON \
      -DEXECUTORCH_BUILD_EXTENSION_RUNNER_UTIL=ON \
      -DEXECUTORCH_BUILD_EXTENSION_TENSOR=ON \
      -DEXECUTORCH_BUILD_DEVTOOLS=ON \
      -DEXECUTORCH_ENABLE_EVENT_TRACER=ON \
      -Bcmake-out .
```

The `cmake` build step for the ExecuTorch library stays the same, as do the next lines setting up local variables.

Next you will adapt the options to Android in the second `cmake` configuration line, which is the one that configures the building of the runner. 

Change it to:

```bash
  cmake -DCMAKE_PREFIX_PATH="${cmake_prefix_path}" \
      -Dexecutorch_DIR="${PWD}/cmake-out/lib/cmake/ExecuTorch" -Dgflags_DIR="${PWD}/cmake-out/third-party/gflags" \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_TOOLCHAIN_FILE="${ANDROID_NDK}/build/cmake/android.toolchain.cmake" \
      -DANDROID_ABI="${ANDROID_ABI}" \
      -B"${build_dir}" \
      "${example_dir}"
```

Once you have changed the configuration lines, you can now run the script `./build_android_example_runner.sh` to build the runner program. 

Once compiled, find the executable `example_runner` in `cmake-out/examples/devtools/`.

Copy `example_runner` and the ExecuTorch bundled program to your Android device. 

Do this with adb:

```bash
adb push example_runner /data/local/tmp/
adb push bundled_program.bp /data/local/tmp/
adb shell 
chmod 777 /data/local/tmp/example_runner
./example_runner --bundled_program_path="bundled_program.bp"
exit
adb pull /data/local/tmp/etdump.etdp .
```

You now have the ETDump file ready to analyze with an ExecuTorch Inspector, in line with the Linux instructions.

To get a full display of the operators and their timings, use the following:

```python
from executorch.devtools import Inspector

etrecord_path = "etrecord.bin"
etdump_path = "etdump.etdp"
inspector = Inspector(etdump_path=etdump_path, etrecord=etrecord_path)
inspector.print_data_tabular()
```

However, as the [ExecuTorch profiling page](https://pytorch.org/executorch/main/tutorials/devtools-integration-tutorial.html) explains, there are data analysis options available. These enable you to quickly find specified criteria such as the slowest layer or group operators. Both the `EventBlock` and `DataFrame` approaches work well. However, at time of writing, the `find_total_for_module()` function has a [bug](https://github.com/pytorch/executorch/issues/7200) and returns incorrect values - hopefully this will soon be fixed.
