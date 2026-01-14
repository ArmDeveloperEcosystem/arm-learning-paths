---
title: "Test Optimizations"
weight: 6
layout: "learningpathall"
---

##  Testing Nginx Optimizations

You can skip this section if you already have a performance test methodology for your Nginx deployment.

This section presents a method for testing Nginx using wrk2. This might be useful if you do not already have an established test methodology. To understand the impact of tuning on specific use cases and deployments, it is recommended that you develop a performance test strategy that reflects your use case.

## About wrk2

[wrk2](https://github.com/giltene/wrk2) is an HTTP load test tool. This section covers how wrk2 is typically used for testing Nginx at Arm.

## Install wrk2

wrk2 can be installed by cloning the source and using `make`. If running wrk2 on an Arm based machine, choose the [Make wrk2 arm compatible](https://github.com/giltene/wrk2/pull/110) PR before building.

Make sure you have make, gcc, zlib, and openssl installed on the system

# Build wrk2
Use the commands shown below to build wrk2:

```console
git clone https://github.com/giltene/wrk2
cd wrk2
make
```

## Example wrk2 test setup

shown below is an image of a typical multi-node test setup. On the left, there is a load generator node that will run wrk2. In the middle, there is the Reverse Proxy (or API Gateway) to be tested. On the right, are multiple file servers that act as upstream servers for the Reverse Proxy (or API Gateway). It is also possible to run wrk2 against file servers directly (not shown below), and it is possible to run wrk2 co-located on the same node as Nginx (also not shown). You will need to decide the best setup for your deployment of Nginx. 

![File Server Before and after Tuning](exampletestsetup.png)

## Running a wrk2 test

The Nginx file servers should have files to serve. If you are using the configuration files discussed in [Tune a static file server](/learning-paths/servers-and-cloud-computing/nginx_tune/tune_static_file_server/) or [Tune a Reverse Proxy or API Gateway](/learning-paths/servers-and-cloud-computing/nginx_tune/tune_revprox_and_apigw), the following commands can be run to create some samples files to serve. You do not need to create these files in Reverse Proxies or API Gateways, because these do not serve files directly.

```
# Create 1kb file in RP use case directory
dd if=/dev/urandom of=/usr/share/nginx/html/1kb bs=1024 count=1

#Create 5kb file in RP use case directory
dd if=/dev/urandom of=/usr/share/nginx/html/5kb bs=1024 count=5

#Create 10kb file in RP use case directory
dd if=/dev/urandom of=/usr/share/nginx/html/10kb bs=1024 count=10

# Copy files into the APIGW use case directory
mkdir -p /usr/share/nginx/html/api_new
cp /usr/share/nginx/html/1kb /usr/share/nginx/html/api_new
cp /usr/share/nginx/html/5kb /usr/share/nginx/html/api_new
cp /usr/share/nginx/html/10kb /usr/share/nginx/html/api_new
```

Shown below is a sample command for testing a file server or reverse proxy. You will need to decide the appropriate thread and connection values to properly load down the Nginx server. In general, you should select parameters that result in 100% CPU utilization on the Nginx server. However, you also have to make sure you are not overloading the Nginx server to the point where connection and read/write errors are reported by wrk2 or Nginx.
```
./wrk --rate 10000000000 -t 64 -c 640 -d 60s https://<rp_apigw_ip_dns>/1kb
```

Below is a sample command for testing an API Gateway.
```
./wrk --rate 10000000000 -t 64 -c 640 -d 60s https://<rp_apigw_ip_dns>/api_old/1kb
```

The API Gateway shown in [Tune a Reverse Proxy or API Gateway](/learning-paths/servers-and-cloud-computing/nginx_tune/tune_revprox_and_apigw) will rewrite `api_old` to `api_new`. This is why the sample files are stored in `/usr/share/nginx/html/10kb /usr/share/nginx/html/api_new` on the file servers.
