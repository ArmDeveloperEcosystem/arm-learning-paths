---
# User change
title: "Docker"

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Docker

Architecture compatibility between the Raspberry Pi and Arm server is a benefit for Docker users. Container images can be created using an Arm server and deployed to a Raspberry Pi with no need to worry about multi-architecture images or cross-compiling. Container repositories like Docker Hub also make sharing easy. 

For complete information about Docker refer to [Learn how to use Docker](/learning-paths/cross-platform/docker/).

Install Docker using the universal Linux instructions and check it works by running the hello-world image:

```console
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
```

If Docker is installed the result will be a welcome message which starts with the text shown.

```output
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

If any other output is shown return to [Installing Docker](/install-guides/docker/) and follow the installation instructions.

Try out some Docker projects to confirm they build and run as expected. Some simple ones are in a [GitHub project called hello-arm](https://github.com/jasonrandrews/hello-arm). 

Also try out official images from Docker Hub such as Ubuntu. None of the projects detect anything different between Raspberry Pi 4 and the Arm server.

# Share Docker images

Docker Hub makes it easy to share images created on the Arm server and run them on the Raspberry Pi 4. 

It’s also possible to build 32-bit Arm images on the Arm server and run those images on the Raspberry Pi 4 without using `docker buildx`. 

An example C program which prints out the size of a pointer to indicate if the Linux userspace is 32-bit or 64-bit is shown below. 

Using a text editor of your choice, copy and paste the code below into a file `hello.c`:

```C
#ifndef ARCH
#define ARCH "Undefined"
#endif

int main()
{
    printf("Hello Arm Developers, architecture from uname is %s\n", ARCH);

    switch (sizeof(void *))
    {
        case 4:
            printf("32-bit userspace\n");
            break;
        case 8:
            printf("64-bit userspace\n");
            break;
        default:
            printf("unknown userspace\n");
    }
    exit(0);
}
```

A Dockerfile to build the program is shown below. Copy and paste this text into a file named `Dockerfile`:

```docker
FROM alpine AS builder
RUN apk add build-base
WORKDIR /home
COPY hello.c .
RUN gcc "-DARCH=\"`uname -a`\"" hello.c -o hello


FROM alpine
WORKDIR /home
COPY --from=builder /home/hello .
CMD ["./hello"]
```

The example is used to build a Docker image on the Arm server and share it using Docker Hub to the Raspberry Pi 4. 

On the Arm server run the commands below to build and then share the image. Substitute your Docker Hub user name for `username`:

```console
docker build -t username/hello .
docker push username/hello
```

On the Raspberry Pi run the shared Docker image.

```console
docker run --rm username/hello
```

The expected output is:

```output
64-bit userspace
```

### 32-bit userspace 

Now try the build with the `--platform` flag to set the architecture to 32-bit Arm.

On the Arm server run the commands shown below. Again, substitute your Docker Hub user name for `username`:

```console
docker build --platform linux/arm/v7 -t username/hello .
docker push username/hello
```

On the Raspberry Pi run the shared Docker image. 

```console
docker run --rm username/hello
```

The expected output is:

```output
32-bit userspace
```

This Docker image will also work on a 32-bit version of Raspberry Pi OS. Compared to a non-Arm machine, creating this 32-bit container image is easier and performance is better.
