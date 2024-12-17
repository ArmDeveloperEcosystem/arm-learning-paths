---
# User change
title: "Build multi-architecture images with Docker buildx"

weight: 3

layout: "learningpathall"

---

## Before you begin

Any computer running Docker can be used for this section. 

Before you begin, confirm Docker `buildx` is installed by running the `docker buildx` command.

```console
docker buildx --help
```

The result should be the usage message from `buildx`. It starts with the the text below:

```output
Usage:  docker buildx [OPTIONS] COMMAND
```

If any other output is shown return to [Installing Docker](/install-guides/docker/) and install the most recent version.

### Note for Docker Engine

Docker Desktop provides the ability to build and run multi-architecture images using instruction emulation. If you are running Docker Engine on Linux, there is an extra step to enable emulation for multi-architecture images. 

For Ubuntu, install emulation support using the command below.

```console
sudo apt-get install qemu-user-static -y
```

If emulation support is not installed on a Linux machine running Docker Engine, an error message similar to this one will occur:
```output
standard_init_linux.go:228: exec user process caused: exec format error
```

The next section explains how to use `docker buildx` to create multi-architecture images. Multi-architecture images provide variants for different instruction set architectures so users can run the image on any of the supported architectures. 

## Build a multi-architecture Docker image from a Dockerfile

Create a new directory and use a text editor to copy the two lines below into a file named `Dockerfile`, or reuse the same file from the previous section.

```dockerfile
FROM ubuntu:latest
CMD echo -n "Architecture is " && uname -m
```

Build the docker image using `docker buildx`. Replace `username` with your Docker Hub username. 

```console 
docker buildx create --use --name mybuilder
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t username/uname-x --push .
```

Docker `buildx` must push the multi-architecture image to a registry. The docker daemon cannot save the image locally. This will change with the future transition from dockerd to containerd, so stay tuned. 

After the build, the `docker images` command does not show a local image, but the multi-architecture image is present in Docker Hub. The missing local image is a common misunderstanding for developers.

## Run the Docker image 

From any computer pull and run the multi-architecture image. Because support for three architectures is included, Docker will automatically get the correct image and run it.

A pull is required because the image is not present on the local machine.

```console
docker run --rm username/uname-x
```
It's also possible to run the image for a different architecture than the current machine by adding `--platform`.

Depending on the architecture of the machine, pick a different platform and run the image using one of the commands.

```console
docker run --rm  --platform linux/arm64 username/uname-x
docker run --rm  --platform linux/arm/v7 username/uname-x
docker run --rm  --platform linux/amd64 username/uname-x
```
For example, on a machine with a `uname` of `aarch64`, run the `amd64` image.

```console
docker run --rm  --platform linux/amd64 username/uname-x
```
The output will be:
```output
Architecture is x86_64
```

## Warning

It is possible to run `docker buildx build` again with a change to the Dockerfile, push to Docker Hub, and re-run expecting to run the new image.

The `docker run` command will use the local image. It will NOT pull the new version which went directly to Docker Hub. 

To remove the local copy use the `docker rmi` command.

```console
docker rmi username/uname-x
```

Now the new image will be downloaded from Docker Hub. 

## Other useful commands

To list the builders use the `ls` command.

```console
docker buildx ls
```

To change to a different builder, such as default, run the `use` command.

```console
docker buildx use default
```

To remove a builder use the `rm` command.

```console
docker buildx rm mybuilder
```
