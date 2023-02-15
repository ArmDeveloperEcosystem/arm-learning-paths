---
# User change
title: "Use Docker manifest to create multi-architecture images"

weight: 5

layout: "learningpathall"


---

## Before you begin

Docker includes an experimental feature called Docker manifest. Please be aware the feature is experimental and not recommended for production use.

Docker manifest provides a different way of working. It allows separate images to be built for each architecture, which can be joined into a multi-architecture image when it's a good time to share the image. 

This enables you to build and test on any architecture and postpone the complexity of multi-architecture builds. When it's time to share a multi-architecture image, it can be quickly created using `docker manifest`. Docker manifest also makes it easy to update one of the architectures without emulation or remote builders.

This section requires two machines, each with a different architecture. One machine should be x86_64 and one should be aarch64.

## Build a simple Dockerfile to print the machine architecture

Create a new directory and save the two lines below into a file named Dockerfile, or re-use the same file from the previous sections.

```dockerfile
FROM ubuntu:latest
CMD echo -n "Architecture is " && uname -m
```

Build the Docker image using `docker build` on each of the two machines. To keep them straight you can attach the current architecture as the tag of the image. This will identify which architecture the image was created on.

Run the commands below on each of the two machines. SSH to remote machines as needed. Substitute your Docker Hub username for `username`.

```console 
arch=`uname -m` 
docker build -t username/uname:$arch .
```

You now have two different docker images, one on each machine. 

## Run the Docker images

Run the image to print the architecture. Do this on each machine and confirm they print the expected architecture of each machine.

```console
docker run --rm uname:$arch 
```

Push the image for each architecture to Docker Hub by running `docker push` on each machine. This results in two separate images in your Docker Hub account, each called `uname` but with the architecture included in the tag name. 

```console
docker push username/uname:$arch
```

Use a browser to look in Docker Hub to see the two images. 

### Join the images 

The last step is to join the two tags into a single multi-architecture image named `uname:latest`.

The two machines have architectures of aaarch64 and x86_64. Use the `docker manifest` command to join them. This only needs to be done once, and can be done on either machine. 

```console
docker manifest create username/uname:latest \
--amend username/uname:aarch64 \
--amend username/uname:x86_64

docker manifest push --purge username/uname:latest
```

The `--purge` option is not needed the first time, but to update one of the images and update the multi-arch image it is needed. It doesn't hurt to always use it. 

After the `docker manifest push`, a new multi-arch image with the latest tag is available. Running `uname:latest` from either machine now works, and there is no need to pay attention to the architecture.

The experimental docker manifest command offers a way to create multi-architecture images by joining multiple images using a manifest. Docker manifest provides additional features not covered here, and is useful to create, inspect, and modify manifest lists. 

