---
title: Build the pipelines
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download the AI camera pipelines project

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
  --build-arg CI_UID=$(id -u) \
  docker/
```

## Build the AI camera pipelines

Start a shell in the container you just built:

```bash
docker run --rm --volume $PWD:/home/cv-examples/example -it ai-camera-pipelines
```

Inside the container, run the following commands:

```bash
ENABLE_SME2=1
TENSORFLOW_GIT_TAG="v2.20.0"

# Build flatbuffers
git clone https://github.com/google/flatbuffers.git
cd flatbuffers
git checkout v24.3.25
mkdir build
cd build
cmake -GNinja -DCMAKE_INSTALL_PREFIX=../install ..
cmake --build .
cmake --install .
cd ../..

# Build the pipelines
mkdir build
cd build
cmake -GNinja -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=../install -DTENSORFLOW_GIT_TAG=$TENSORFLOW_GIT_TAG -DTFLITE_HOST_TOOLS_DIR=../flatbuffers/install/bin -DENABLE_SME2=$ENABLE_SME2 -DCMAKE_TOOLCHAIN_FILE=../example/toolchain.cmake -S ../example
cmake --build .
cmake --install .

# Package and export the pipelines.
cd ..
tar cfz example/install.tar.gz install
```

Leave the container by pressing `Ctrl+D`.

{{% notice Note %}}
In the above `cmake` command line, you'll note that the pipelines are build with SME2 (`-DENABLE_SME2=$ENABLE_SME2`), but that this could be disabled as well. We will use this feature later when benchmarking the performance improvements brought by SME2.
{{% /notice %}}

## Install the pipelines

```bash
cd $HOME
tar xfz ai-camera-pipelines.git/install.tar.gz
mv install ai-camera-pipelines
```

## Dive deeper into the AI camera pipelines

The AI camera pipelines
[repository](https://git.gitlab.arm.com/kleidi/kleidi-examples/ai-camera-pipelines)
contains more information in its README file should you wish to dive deeper into
it.