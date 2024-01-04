---
title: Launch the image classification Docker container
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download and run the image classification Docker container

Run the command below to download and run the container:

```console
git clone --recursive --depth=1 https://github.com/dusty-nv/jetson-inference
cd jetson-inference
docker/run.sh
```

### Learn some useful Docker commands

If you are not familiar with Docker, there are some useful commands you should know. 

Run them in a terminal (not from inside the running container).

#### Get the Container ID

Print the ID of the container:

```console
sudo docker ps -q
```

The container ID is a hex number such as `174055df45cd`

#### Copy files into and out of a Docker container

You can use the container ID to identify the container for copying files.

Copy to the container:

```console
# sudo docker cp foo.txt container_id:foo.txt
sudo docker cp ./jas.jpeg 174055df45cd:jetson-inference/build/aarch64/bin/images/jas.jpeg
```

Copy from the container is the same, but in reverse: 

```console
# sudo docker cp container_id:/foo.txt foo.txt
sudo docker cp 174055df45cd:jetson-inference/build/aarch64/bin/images/test/jas-output.jpeg ./jas-output.jpeg
```

#### Stop and start the Docker container

To stop:

```console
sudo docker stop <container ID>
```

To start it up again:

```console
# inside the cloned jetson-inference directory
docker/run.sh
```
