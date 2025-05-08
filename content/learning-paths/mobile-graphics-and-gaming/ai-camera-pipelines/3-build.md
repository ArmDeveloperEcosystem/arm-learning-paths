---
title: Build the pipelines
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download the AI Camera Pipelines Project

Clone the project repository:

```bash
git clone https://git.gitlab.arm.com/kleidi/kleidi-examples/ai-camera-pipelines.git ai-camera-pipelines.git
```

Fetch the required large files using Git LFS:

```bash
cd ai-camera-pipelines.git
git lfs install
git lfs pull
```

## Create a build container

Build the Docker container used to compile the pipelines:

```bash
docker build -t ai-camera-pipelines -f docker/Dockerfile \
  --build-arg DOCKERHUB_MIRROR=docker.io \
  --build-arg CI_UID=$(id -u) .
```

## Build the AI Camera Pipelines

Start a shell in the container you just built:

```bash
docker run --rm --volume $PWD:/home/cv-examples/example -it ai-camera-pipelines
```

Inside the container, run the following commands:

```bash
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
```

Leave the container by pressing `Ctrl+D`.

## Notes on the `cmake` configuration options

- `-DENABLE_SME2=$ENABLE_SME2` with `ENABLE_SME2=0`: SME2 (Scalable Matrix Extension 2) is disabled in this build (`0`). A Learning Path covering an SME-enabled Android phone coming soon.  
- `-DARMNN_TFLITE_PARSER=0`: Configures the `ai-camera-pipelines` repository to use TFLite with XNNPack instead of ArmNN.
- `-DENABLE_KLEIDICV:BOOL=ON`: Enables KleidiCV for optimized image processing.
- `-DXNNPACK_ENABLE_KLEIDIAI:BOOL=ON`:  Enables KleidiAI acceleration for TFLite workloads via XNNPack.

## Install the pipelines

```bash
cd $HOME
tar xfz ai-camera-pipelines.git/install.tar.gz
mv install ai-camera-pipelines
```