---
title: Build the Pipelines
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download the AI Camera Pipelines Project

```BASH
git clone https://git.gitlab.arm.com/kleidi/kleidi-examples/ai-camera-pipelines.git ai-camera-pipelines.git
```

Check out the data files:

```BASH
cd ai-camera-pipelines.git
git lfs install
git lfs pull
```

## Create a Build Container

The pipelines will be built from a container, so you first need to build the container:

```BASH
docker build -t ai-camera-pipelines -f docker/Dockerfile --build-arg DOCKERHUB_MIRROR=docker.io --build-arg CI_UID=$(id -u) .
```

## Build the AI Camera Pipelines

Start a shell in the container you just built with:

```BASH
docker run --rm --volume $PWD:/home/cv-examples/example -it ai-camera-pipelines
```

And execute the following commands and leave the container:

```BASH
ENABLE_SME2=0
TENSORFLOW_GIT_TAG=ddceb963c1599f803b5c4beca42b802de5134b44

# Build flatbuffers
git clone https://github.com/google/flatbuffers.git
cd flatbuffers
git checkout v24.3.25
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=../install
cmake --build . -j16
cmake --install .
cd ../..

# Build the pipelines
mkdir build
cd build
cmake -GNinja -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=../install -DARMNN_TFLITE_PARSER=0 -DTENSORFLOW_GIT_TAG=$TENSORFLOW_GIT_TAG -DTFLITE_HOST_TOOLS_DIR=../flatbuffers/install/bin -DENABLE_SME2=$ENABLE_SME2 -DENABLE_KLEIDICV:BOOL=ON -DXNNPACK_ENABLE_KLEIDIAI:BOOL=ON -DCMAKE_TOOLCHAIN_FILE=toolchain.cmake -S ../example -B .
cmake --build . -j16
cmake --install .

# Package and export the pipelines.
cd ..
tar cfz example/install.tar.gz install

# Leave the container (ctrl+D)
```

You can note on the `cmake` configuration step command line:
- `-DENABLE_SME2=$ENABLE_SME2` with `ENABLE_SME2=0`: SME2 is not (yet) enabled --- but stay tuned !
- `-DARMNN_TFLITE_PARSER=0` configure the `ai-camera-pipelines` repository to use TFLite (with XNNPack) instead of ArmNN
- `-DENABLE_KLEIDICV:BOOL=ON`: KleidiCV is enabled
- `-DXNNPACK_ENABLE_KLEIDIAI:BOOL=ON`: TFLite+XNNPack with use KleidiAI

## Install the Pipelines

```BASH
cd $HOME
tar xfz ai-camera-pipelines.git/install.tar.gz
mv install ai-camera-pipelines
```