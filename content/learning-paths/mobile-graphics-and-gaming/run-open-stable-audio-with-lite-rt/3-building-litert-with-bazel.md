---
title: Build LiteRT with Bazel
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## LiteRT

LiteRT (short for Lite Runtime), formerly known as TensorFlow Lite, is Google's high-performance runtime for on-device AI.

TODO: more on LiteRT or links? Reason why we will convert the model or is it clear?


## Build LiteRT libraries with Bazel inside a Docker container

TODO:

https://github.com/google-ai-edge/LiteRT specifies bazel build inside docker container but would be difficult to get libs out?

Some of below is same as in readme in LiteRT, best to point in a link here? Any troubleshooting needed?

Can build with bazel instead, without using docker


Clone the repository and get the latest modules

```bash
git clone https://github.com/google-ai-edge/LiteRT.git

cd LiteRT/

git submodule init && git submodule update --remote

```

Docker can then be used to build the needed libraries, firstly ensure that docker is installed

```bash

sudo apt install docker
```

Add current user to dockergroup
```
sudo usermod -aG docker $USER

newgrp docker

```

A docker image can be created by pointing to the Dockerfile defined in LiteRT repository

```bash

docker build . -t tflite-builder -f ci/tflite-py3.Dockerfile

# Confirm the container was created with
docker image ls

```

Run bash inside the container

```
docker run -it -w /host_dir -v $PWD:/host_dir -v $HOME/.cache/bazel:$PWD/.cache/bazel tflite-builder bash


docker run -it -w /host_dir -v $PWD:/host_dir -v /host_dir/bazel-bin:$PWD/bazel-bin tflite-builder bash
```

Configure to use default settings:
```
./configure

```

Build needed libraries:

```
bazel build  //tflite:libtensorflowlite.so

bazel build -c opt --config android_arm64 //tensorflow/lite:libtensorflowlite.so --define tflite_with_xnnpack=true --define=xnn_enable_arm_i8mm=true --define tflite_with_xnnpack_qs8=true --define tflite_with_xnnpack_qu8=true


# set output base to custom directory
bazel --output_base=/host_dir/output-base build //tflite:libtensorflowlite.so

```

{{% notice Note %}}
This may take a while.. Bazel builds ~1,600 targets
{{% /notice %}}

Once finished, `exit` out of the docker container and the libraries will be available on host machine in output base directory provided - output-base

```bash
/LiteRT/output-base$ find . -name libtensorflow*so
./execroot/litert/bazel-out/k8-opt/bin/tflite/libtensorflowlite.so.runfiles/litert/tflite/libtensorflowlite.so
./execroot/litert/bazel-out/k8-opt/bin/tflite/libtensorflowlite.so
```


docker ps to show containers, copy generated libs from docker container
```bash
ecosys@ip-10-252-24-29:~/nindro01/LiteRT$ docker ps

CONTAINER ID   IMAGE            COMMAND   CREATED              STATUS              PORTS     NAMES
944466fd5867   tflite-builder   "bash"    About a minute ago   Up About a minute             priceless_williamson
mlecosys@ip-10-252-24-29:~/nindro01/LiteRT$ 


 docker cp  944466fd5867:/host_dir/bazel-bin/tflite/ .
```
 
 tflite dir in LiteRT contains libs needed
 
## Build LiteRT libraries with Bazel

Clone the needed repository

```console
git clone https://github.com/tensorflow/tensorflow.git
```

Next, clone TensorFlow from its Git repository to your system:

```bash
git clone https://github.com/tensorflow/tensorflow.git
cd tensorflow
```

Now you can configure TensorFlow. Here you can set the custom build parameters needed as follows:

```bash { output_lines = "2-14" }
python3 ./configure.py
Please specify the location of python. [Default is /home/user/Workspace/tflite/env3_10/bin/python3]:
Please input the desired Python library path to use. Default is [/home/user/Workspace/tflite/env3_10/lib/python3.10/site-packages]
Do you wish to build TensorFlow with ROCm support? [y/N]: n
Do you wish to build TensorFlow with CUDA support? [y/N]: n
Do you want to use Clang to build TensorFlow? [Y/n]: n
Would you like to interactively configure ./WORKSPACE for Android builds? [y/N]: y
Please specify the home path of the Android NDK to use. [Default is /home/user/Android/Sdk/ndk-bundle]: /home/user/Workspace/tools/ndk/android-ndk-r25b
Please specify the (min) Android NDK API level to use. [Available levels: [16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33]] [Default is 21]: 30
Please specify the home path of the Android SDK to use. [Default is /home/user/Android/Sdk]:
Please specify the Android SDK API level to use. [Available levels: ['31', '33', '34', '35']] [Default is 35]:
Please specify an Android build tools version to use. [Available versions: ['30.0.3', '34.0.0', '35.0.0']] [Default is 35.0.0]: 
```






