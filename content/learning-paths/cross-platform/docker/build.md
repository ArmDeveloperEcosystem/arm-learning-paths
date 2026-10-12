---
# User change
title: "Build, run, and share a Docker image"

weight: 2

layout: "learningpathall"

---

You can use containers to create portable workloads which run on your local computer, on physical and virtual servers, on public cloud infrastructure, and on embedded devices. A computer's instruction set impacts container creation. This Learning Path provides a short introduction to Docker followed by information about how to build, run and share Docker images for the Arm architecture. 

## Before you begin

You can use any computer running Docker to complete this topic.

To confirm that Docker is installed correctly run the following command:

```console
docker run hello-world
```

If Docker is installed and working correctly you see the following message:

```output
Hello from Docker!
This message shows that your installation appears to be working correctly.
```
         
Note: If you do not see the message above, go to [Installing Docker](/install-guides/docker/) and follow the instructions to complete the installation.

{{% notice Note %}}

If you see the error:

```output
failed to connect to the Docker API at unix:///var/run/docker.sock
```

first check whether the Docker daemon failed to start:

```bash
sudo systemctl restart docker
sudo systemctl status docker
```

If the logs contain an error similar to `nft: Protocol not supported`, the Docker service might fail to start if the host Linux kernel is missing required features. This is more likely when using a custom or patched kernel.

The open source [check-config.sh](https://github.com/moby/moby/blob/275015b0e7d1e17941df3dad1503263d653588e5/contrib/check-config.sh) script from the Docker Moby project can be used to check the host’s kernel configuration and identify required or optional features that are missing. Kernel features may be built directly into the kernel (=y) or provided as loadable modules (=m). Download the bash script and run it against the current kernel configuration. 

```bash
./check-config.sh /boot/config-<kernel version>
```

You will see output similar to that below.

```output
Generally Necessary:
- cgroup hierarchy: cgroupv2
  Controllers:
  - cpu: available
  - cpuset: available
  - io: available
  - memory: available
  - pids: available
- apparmor: enabled and tools installed
- CONFIG_NAMESPACES: enabled
- CONFIG_NET_NS: enabled
- CONFIG_PID_NS: enabled
- CONFIG_IPC_NS: enabled
...
```

For basic Docker functionality, ensure that the features reported under **Generally Necessary** are available. These cover fundamental container functionality. The script also checks a number of Optional Features, Network Drivers, and Storage Drivers. Not all of these are required. 

If a required feature is configured as a module (=m), also ensure that the corresponding kernel module is installed and can be loaded. If required features are missing, refer to the instructions for building the OS or kernel for your distribution or platform to enable the missing kernel configuration options. 

{{% /notice %}}

The sections describe how to:
- Build a Docker image
- Run a Docker container
- Display local Docker images
- Save and share a Docker image

## Build a Docker image from a Dockerfile

To build a Docker image:

1. Navigate to an empty directory and use a text editor to copy the two lines below into a file named `Dockerfile`:

```dockerfile
FROM ubuntu:latest
CMD echo -n "Architecture is " && uname -m
```

2. Build the Docker image with the `docker build` command. For example: 

```console 
docker build -t uname  .
```

Note: The `-t` argument is the tag, a human-readable name for the final image. The `.` specifies the `PATH` to find the files for the build.

## Create a container from a Docker image

To create a container from the image enter the command:

```console
docker run --rm uname 
```
      
This command displays the architecture.
   
The output depends on the operating system and architecture of your computer. The following table shows the most common values.

| Operating System and Architecture | Console Output |
| ----------- | ----------- |
| Any OS on Intel or AMD | `Architecture is x64_86` |
| Linux on Arm 64-bit | `Architecture is aarch64` |
| Linux on Arm 32-bit | `Architecture is armv7l` |
| macOS on Apple Silicon | `Architecture is arm64` |

## Display local Docker images

The `docker images` command lists all the images available on your computer. Docker image names have the form: **`repository/image-name:tag`**

Run the `docker images` command to see the list of images:

```console
docker images
```

The output is similar to this example:

```output
REPOSITORY   TAG       IMAGE ID       CREATED      SIZE
uname        latest    f0a8125a81d3   5 days ago   69.2MB
```

This example shows the image name is `uname` and the tag is `latest`. If you do not specify a tag name, `latest` is the default value.

## Save and share a Docker image

You can save and share Docker images in repositories. The most common repository is [Docker Hub](https://hub.docker.com/). Repositories are also available from software providers and cloud service providers.

Before saving the image to Docker Hub:

1. Create an account on [Docker Hub](https://hub.docker.com/signup) and note your username and password.

2. Use the `docker tag` command to modify the image name to include your Docker hub username:

```console
docker tag uname username/uname
```

3. Log in to Docker Hub, enter your Docker Hub username and password when prompted:

```console
docker login
```

4. Use the `docker push` command to save the image to your Docker Hub account:

```console
docker push username/uname
```

5. In a browser, log in to Docker Hub. The new image is visible in your account. 

6. (optional) Create a container from the Docker image on another computer with the same architecture.

If you have another computer with the same architecture you can run the image from Docker Hub. 

Make sure Docker is installed on the second computer.

On the second computer, enter the `docker run` command to create a container from the shared image. For example:

```console
docker run --rm username/uname
```

Because the image is not on the local computer, Docker downloads it from Docker Hub and creates a container. 

You do not need to rebuild the Docker image on the second computer.

## Next steps

In this section you learned how to build, run, and share a Docker image. 

You used computers with the same instruction set architecture to build and share the Docker image.

To support multiple computer architectures, you can use a single Docker image that supports multi-architectures. 

Continue the Learning Path to learn about multi-architecture images.
