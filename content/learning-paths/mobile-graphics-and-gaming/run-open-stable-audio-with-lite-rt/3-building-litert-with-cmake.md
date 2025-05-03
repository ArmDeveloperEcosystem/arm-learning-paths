---
title: Build LiteRT with CMake
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## LiteRT

LiteRT (short for Lite Runtime), formerly known as TensorFlow Lite, is Google's high-performance runtime for on-device AI.

TODO: more on LiteRT or links? Reason why we will convert the model or is it clear?


## Build LiteRT libraries

TODO:

https://github.com/google-ai-edge/LiteRT specifies bazel build inside docker container but would be difficult to get libs out?

Some of below is same as in readme in LiteRT, best to point in a link here? Any troubleshooting needed?


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
 
 







