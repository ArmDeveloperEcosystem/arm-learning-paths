---
title: Launching the Docker container
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Launching the Docker container

Before moving forward, we'll download and run the container required for image classification
```
git clone --recursive --depth=1 https://github.com/dusty-nv/jetson-inference
cd jetson-inference
docker/run.sh
```

Navigate to the following in order to run the commands on the next page
```
cd build/aarch64/bin
```

### Some basic Docker commands that will be useful later

#### Getting your Docker ID
In a new terminal not currently inside the Docker container
```
sudo docker ps -q
```

It will look something like **174055df45cd**
#### Copying files into and out of a Docker container

These will need to be done in a new terminal window

Copy to the container
```
# sudo docker cp foo.txt container_id:foo.txt
sudo docker cp ./jas.jpeg 174055df45cd:jetson-inference/build/aarch64/bin/images/jas.jpeg
```

Copy from the container is just the same, but in reverse. 
```
# sudo docker cp container_id:/foo.txt foo.txt
sudo docker cp 174055df45cd:jetson-inference/build/aarch64/bin/images/test/jas-output.jpeg ./jas-output.jpeg
```

#### Stopping and starting the Docker contain
To stop
```
sudo docker stop <dockerID>
```

To start it up again
```
# inside the cloned jetson-inference directory
docker/run.sh
```
