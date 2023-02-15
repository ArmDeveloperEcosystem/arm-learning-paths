---
# User change
title: "Perform remote Docker builds on an Arm server"

weight: 4

layout: "learningpathall"


---

## Before you begin

Building Docker images for the Arm architecture on the non-Arm machine on your desk using emulation may be slow. 

This section explains how to use the `docker context` command to build an image for the Arm architecture using a remote machine accessible via ssh. 

Docker should also be installed on a remote Arm machine which can be reached via ssh without password. 

For more information about ssh configuration refer to [SSH](/install-tools/ssh/).

To learn how to create an Arm virtual machine using a cloud service provider refer to [Get started with Arm-based cloud service csp](/learning-paths/server-and-cloud/csp/).

## Build a Docker image from a Dockerfile

This section contrasts a local build for the x86_64 architecture and a remote build for the Arm architecture. 

On your local computer, create a new directory and save the two lines below into a file named Dockerfile, or re-use the same file from the previous section.

```dockerfile
FROM ubuntu:latest
CMD echo -n "Architecture is " && uname -m
```

Build the Docker image using `docker build`. This creates an image for the local machine architecture.

```console 
docker build -t uname .
```

Run the Docker image using `docker run`. 

```console
docker run --rm uname 
```

The output prints the architecture of the local machine. 

The previous section explained how to use `docker buildx` to create a multi-architecture image which included the Arm support. This was done using instruction emulation. 

If the build process is complex, emulation will take too long. A different way to build for the Arm architecture is to use a remote builder. A remote builder provides better performance compared to local buildx with emulation. For example, building a large C++ project may have significant slowdown with buildx. 

Using the same Dockerfile, an image for the Arm architecture can be created from the local machine by using the remote machine. 

To use the remote machine to build, create a remote context using the `docker context` command. 

Substitute the `username` and IP address of the remote Arm Linux machine.

```console
docker context create remote --docker "host=ssh://username@IP"
docker context use remote
```

As soon as the remote context is set, commands like `docker images` show the images on the remote machine, not the local images. Somewhat mysteriously, all of the Docker commands will be applied to the remote machine.  

To build an image on the remote machine use `docker build`. Replace `username` with your Docker Hub username.

```console
docker build -t username/uname  .
```

If you manually ssh to the remote machine and use `docker images` the results is the same as running `docker images` on the local machine with the remote context set. 

With the remote context, the run command will also execute on the remote machine. 

```console
docker run --rm username/uname
```

The output is the architecture of the remote Arm machine. 

Push the image to Docker Hub. It will go directly from the remote machine to Docker Hub. 

```console
docker push username/uname
```

To restore the local machine context use the `docker context` command set the context back to `default`.

```console
docker context use default
```

A remote context is a powerful concept, but it can be tricky to manage, especially if you forget about it. 

The next sections covers another way to build multi-architecture images by joining images from different architectures together to form a new multi-architecture image.

