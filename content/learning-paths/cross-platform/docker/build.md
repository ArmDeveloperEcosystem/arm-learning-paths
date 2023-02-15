---
# User change
title: "Build, run, and share a Docker image"

weight: 2

layout: "learningpathall"

---

## Before you begin

Any computer running Docker can be used for this section. 

Before you begin, confirm Docker is installed by running the command:

```console
docker run hello-world
```

If Docker is installed the result will be a welcome message which starts with the text shown.

```console
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

If any other output is shown return to [Installing Docker](/install-tools/docker/) and follow the installation instructions.

The sections below demonstrate how to build a Docker image and run a Docker container for a single architecture using `docker build` and `docker run`. You can also save and share the created image.

When run, the example container prints the architecture of the machine.

## Build a Docker image from a Dockerfile

The first step to use Docker is to build an image from a Dockerfile. 

Create a new directory and save the two lines below in a file named `Dockerfile`. 

```dockerfile
FROM ubuntu:latest
CMD echo -n "Architecture is " && uname -m
```

Build the docker image using `docker build`. The `-t` argument is the tag, or name of the image. The `.` is the `PATH` specifying where to find the files for the build. For example:

```console 
docker build -t uname  .
```

## Run the Docker image 

Run the image. For example, to print the architecture: 

```console
docker run --rm uname 
```

The output from `docker run` depends on the operating system and architecture of your computer.

The most common values are shown in the table below.

| Operating System and Architecture | Console Output |
| ----------- | ----------- |
| Any OS on Intel | `Architecture is x64_86` |
| Linux on Arm 64-bit | `Architecture is aarch64` |
| Linux on Arm 32-bit | `Architecture is armv7l` |
| macOS on Apple Silicon | `Architecture is arm64` |


## Display local Docker images

The Docker image with the tag `uname` is now stored on your computer. 

To see all of the images available on your computer use the `docker images` command. Docker image names have the form **`repository/image-name:tag`** 

Run the `docker images` command to see the list of images.

```console
docker images
```

The image name is `uname` and the tag name is `latest`. The `latest` tag is used as the default value if no tag name is specified. 

The output will be similar to:

```console
REPOSITORY   TAG       IMAGE ID       CREATED      SIZE
uname        latest    f0a8125a81d3   5 days ago   69.2MB
```

## Save and share the Docker image

Docker images are saved and shared using repositories. The most common repository is [Docker Hub](https://hub.docker.com/). Repositories are also available from software providers and cloud service providers.

Before saving the image to Docker Hub, modify the image name to include your `username`. [Create an account](https://hub.docker.com/signup) on Docker Hub if you don't already have one and take note of your username. 

Change `username` to your Docker Hub username.

Use the `docker tag` command to add your Docker Hub username.

```console
docker tag uname:latest username/uname:latest
```

The `latest` tag can be omitted since it is the default value. 

Log in to Docker Hub from the command line. Enter your Docker Hub username and password when prompted. 

```console
docker login
```

Save the image on Docker Hub using the `docker push` command. This command transfers the image into your Docker Hub account. 

```console
docker push username/uname:latest
```

Log in to Docker Hub using a browser and look at the new image listed in your account. 

Docker images can be run on any computer with the same architecture. 

If you have another computer with the same architecture you can use the `docker run` command to demonstrate sharing.  Make sure Docker is installed on the second computer. If you don't have a second computer, you can skip to the next section.

On the second computer, execute `docker run` to see how the image is shared. 

```console
docker run username/uname:latest
```

When `docker run` doesn't find the image on the local computer it will download it form Docker Hub. There is no need to rebuild the Docker image on the second computer.

## More about Docker images

In this section you learned how to build, run, and share a Docker image. 

Running a Docker image on a computer with a different architecture from the one it was created on doesn't automatically work because the computers have different instructions sets. 

Multi-architecture images are the solution to building a single Docker image that supports multiple computer architectures. 

Continue the Learning Path to learn about multi-architecture images. 

