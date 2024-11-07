---
title: ML profiling with ExecuteNetwork
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## ArmNN's Network Profiler
One way of running tflite models is with ArmNN. This is available as a delegate to the standard tflite interpreter. But to profile the model, ArmNN comes with a command-line utility called `ExecuteNetwork`. This program just runs the model without the rest of an app. It is able to output layer timings and other useful information to let you know where there might be bottlenecks within your model.

If you are not using tflite, you'll need to look at other tools from your framework to profile your model. If you are using tflite without ArmNN, then the output from `ExecuteNetwork` will be more of an indication than a definitive answer. But it can still be useful to see if there are any obvious problems.

If you want to have a tflite to practice this Learning Path with, you can download one from the [Arm Model Zoo](https://github.com/ARM-software/ML-zoo). As an example we'll use a [mobilenet tflite](https://github.com/ARM-software/ML-zoo/blob/master/models/image_classification/mobilenet_v2_1.0_224/tflite_int8/mobilenet_v2_1.0_224_INT8.tflite).

To get `ExecuteNetwork` you can download it from the [ArmNN GitHub](https://github.com/ARM-software/armnn/releases). Download the version appropriate for the Android phone you wish to test on - the Android version and the architecture of the phone. If you are unsure of the architecture, you can use a lower one, but you may miss out on some optimizations. Inside the tar.gz that you download, `ExecuteNetwork` is included. Note among the other release downloads on the ArmNN Github is the separate file for the `aar` delegate which is the easy way to include the ArmNN delegate into your app.

To run `ExecuteNetwork` you'll need to use `adb` to push the model and the executable to your phone, and then run it from the adb shell. `adb` is included with Android Studio, but you may need to add it to your path. Android Studio normally installs it to a location like \<user>\AppData\Local\Android\Sdk\platform-tools. `adb` can also be downloaded separately from the [Android Developer site](https://developer.android.com/studio/releases/platform-tools).

Unzip the tar.gz folder you downloaded to somewhere convenient. From a command prompt, you can then adapt and run the following commands to push the files to your phone. The `/data/local/tmp` folder of your Android device is a place with relaxed permissions that you can use to run this profiling.

```bash
adb push mobilenet_v2_1.0_224_INT8.tflite /data/local/tmp/ # if you are using the example tflite model
# adb push yourmodel.tflite /data/local/tmp/ # where yourmodel is the tflite NN model file that you wish to profile
adb push ExecuteNetwork /data/local/tmp/
adb push libarm_compute.so /data/local/tmp/
adb push libarmnn.so /data/local/tmp/
adb push libarmnn_support_library.so /data/local/tmp/
# more ArmNN .so library files
```
Push all the `.so` library files that are in the base folder of the tar.gz you downloaded, alongside `ExecuteNetwork`, and all the `.so` files in the `delegate` sub-folder. If you are using a recent version of Android Studio this copying can be done much more easily with drag and drop in the *Device Explorer > Files*.

Then you need to set the permissions on the files:

```bash
adb shell        # to get into the adb shell on the phone
cd /data/local/tmp
chmod 777 ExecuteNetwork    # to make the file executable
chmod 777 *.so	   # to make the library files executable
```

Then you can run ExecuteNetwork to profile the model. If you are using the example tflite, you can use the following command:

```bash
LD_LIBRARY_PATH=. ./ExecuteNetwork -m mobilenet_v2_1.0_224_INT8.tflite -c CpuAcc -T delegate --iterations 2 --do-not-print-output --enable-fast-math --fp16-turbo-mode -e --output-network-details > modelout.txt
```

If you are using your own tflite, replace `mobilenet_v2_1.0_224_INT8.tflite` with the name of your tflite file.

This will run the model twice, outputting the layer timings to `modelout.txt`. The `--iterations 2` flag is the command that means it runs twice: the first run includes a lot of startup costs and one-off optimizations, so the second run is more indicative of the real performance.

For the other flags, of note are the `-e` and `--output-network-details` flags which will output a lot of timeline information about the model, including the layer timings. The `--do-not-print-output` flag will stop the output of the model, which can be very large, and without sensible input, meaningless. The `--enable-fast-math` and `--fp16-turbo-mode` flags enable some maths optimizations. `CpuAcc` is the acclerated CPU backend, it can be replaced with `GpuAcc` for the accelerated GPU backend. 

After running the model, you can pull the output file back to your computer with the following commands:

```bash
exit         # to leave the adb shell
adb pull /data/local/tmp/modelout.txt
```
Once again, this can be done with drag and drop in Android Studio's *Device Explorer > Files*.

Depending on the size of your model, the output will probably be quite large. You can use a text editor to view the file. The output is in JSON format, so you can use a JSON viewer to make it more readable. Usually some scripting can be used to extract the information you need more easily out of the very raw data in the file.

At the top is the summary, with the setup time and inference time of your 2 runs, which will look something like this:
```text
Info: ArmNN v33.2.0
Info: Initialization time: 7.20 ms.
Info: ArmnnSubgraph creation
Info: Parse nodes to ArmNN time: 50.99 ms
Info: Optimize ArmnnSubgraph time: 85.94 ms
Info: Load ArmnnSubgraph time: 91.11 ms
Info: Overall ArmnnSubgraph creation time: 228.47 ms

Info: Execution time: 721.91 ms.
Info: Inference time: 722.02 ms

Info: Execution time: 468.42 ms.
Info: Inference time: 468.58 ms
```

After the summary comes the graph of the model, and then the layers and their timings from the second run. At the start of the layers there are a few optimizations and their timings recorded before the network itself, so you can skip past the graph and the optimization timings to get to the part that wants analyzing.  

In the mobilenet example output, the graph is from lines 18 to 1629. After this come the optimization timings, which are part of the runtime, but not the network - these go until line 1989. Next there are a few wall clock recordings for the loading of the network, before the first layer "Convolution2dLayer_CreateWorkload_#18" at line 2036. Here is where the layer info that wants analyzing starts.

The layers' "Wall clock time" in microseconds shows how long they took to run. These layers and their timings can then be analyzed to see which layers, and which operators, took the most time.