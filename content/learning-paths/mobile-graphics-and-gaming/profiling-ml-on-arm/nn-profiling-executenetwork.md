---
title: ML Profiling of a LiteRT model with ExecuteNetwork
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Arm NN Network Profiler
One way of running LiteRT models is to use Arm NN, which is open-source network machine learning (ML) software. This is available as a delegate to the standard LiteRT interpreter. But to profile the model, Arm NN comes with a command-line utility called `ExecuteNetwork`. This program runs the model without the rest of the app. It is able to output layer timings and other useful information to report where there might be bottlenecks within your model.

If you are using LiteRT without Arm NN, then the output from `ExecuteNetwork` is more of an indication than a definitive answer, but it can still be useful in identifying any obvious problems.

### Download a LiteRT Model

To try this out, you can download a LiteRT model from the [Arm Model Zoo](https://github.com/ARM-software/ML-zoo). Specifically for this Learning Path, you will download [mobilenet tflite](https://github.com/ARM-software/ML-zoo/blob/master/models/image_classification/mobilenet_v2_1.0_224/tflite_int8/mobilenet_v2_1.0_224_INT8.tflite).

### Download and set up ExecuteNetwork

You can download `ExecuteNetwork` from the [Arm NN GitHub](https://github.com/ARM-software/armnn/releases). Download the version appropriate for the Android phone that you are testing on, ensuring that it matches the Android version and architecture of the phone. If you are unsure of the architecture, you can use a lower one, but you might miss out on some optimizations.`ExecuteNetwork` is included inside the `tar.gz` archive that you download. Among the other release downloads on the Arm NN Github is a separate file for the `aar` delegate which you can also easily download.

To run `ExecuteNetwork,` you need to use `adb` to push the model and the executable to your phone, and then run it from the adb shell. `adb` is included with Android Studio, but you might need to add it to your path. Android Studio normally installs it to a location such as:

  `\<user>\AppData\Local\Android\Sdk\platform-tools`. `adb` can also be downloaded separately from the [Android Developer site](https://developer.android.com/studio/releases/platform-tools).

Unzip the `tar.gz` folder you downloaded. From a command prompt, you can then adapt and run the following commands to push the files to your phone. The `/data/local/tmp` folder of your Android device is a place with relaxed permissions that you can use to run this profiling.

```bash
adb push mobilenet_v2_1.0_224_INT8.tflite /data/local/tmp/ 
adb push ExecuteNetwork /data/local/tmp/
adb push libarm_compute.so /data/local/tmp/
adb push libarmnn.so /data/local/tmp/
adb push libarmnn_support_library.so /data/local/tmp/
# more Arm NN .so library files
```
Push all the `.so` library files that are in the base folder of the `tar.gz` archive you downloaded, alongside `ExecuteNetwork`, and all the `.so` files in the `delegate` sub-folder. 

If you are using a recent version of Android Studio this copying can be done much more easily with drag-and-drop in Android Studio in **Device Explorer > Files**.

Then you need to set the permissions on the files:

```bash
adb shell       
cd /data/local/tmp
chmod 777 ExecuteNetwork    
chmod 777 *.so	   
```

### Run ExecuteNetwork to profile the model

Now you can run ExecuteNetwork to profile the model. With the example LiteRT, you can use the following command:

```bash
LD_LIBRARY_PATH=. ./ExecuteNetwork -m mobilenet_v2_1.0_224_INT8.tflite -c CpuAcc -T delegate --iterations 2 --do-not-print-output --enable-fast-math --fp16-turbo-mode -e --output-network-details > modelout.txt
```

If you are using your own LiteRT, replace `mobilenet_v2_1.0_224_INT8.tflite` with the name of your tflite file.

This runs the model twice, outputting the layer timings to `modelout.txt`. The `--iterations 2` flag is the command that instructs it to run twice: the first run includes a lot of start-up costs and one-off optimizations, whilst the second run is more indicative of the level of performance.

The other flags to note are the `-e` and `--output-network-details` flags which output a lot of timeline information about the model, including the layer timings. The `--do-not-print-output` flag stops the output of the model, which can be very large, and without sensible input it is meaningless. The `--enable-fast-math` and `--fp16-turbo-mode` flags enable some math optimizations. `CpuAcc` is the accelerated CPU backend, and you can replace it with `GpuAcc` for the accelerated GPU backend. 

### Analyze the output

After running the model, you can pull the output file back to your host machine with the following commands:

```bash
exit        
adb pull /data/local/tmp/modelout.txt
```
Once again, you can do this with drag-and-drop in Android Studio in **Device Explorer > Files**.

Depending on the size of your model, the output will probably be quite large. You can use a text editor to view the file. The output is in JSON format, so you can use a JSON viewer to make it more readable. Usually you can use some scripting to extract the information you need more easily out of the raw data in the file.

At the top is the summary, with the setup time and inference time of the two runs, which look something like this:

```output
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

After the summary, you will see:

* The graph of the model.
* The layers and their timings from the second run. 

At the start of the layers, there are a few optimizations and their timings recorded before the network itself. You can skip past the graph and the optimization timings to get to the part that you need to analyze.  

In the mobilenet example output, the graph is from lines 18 to 1629. After this are the optimization timings, which are part of the runtime, but not the network - these go until line 1989. Next there are a few wall clock recordings for the loading of the network, before the first layer "Convolution2dLayer_CreateWorkload_#18" at line 2036. This is where the layer information that requires analysis starts.

The layers' wall-clock time in microseconds shows you how much time elapsed. You can then analyze these layers and timings to identify which layers and operators took the most time to run.
