---
# User change
title: "Install, configure and run Envoy"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---


##  Introduction to Envoy
Envoy is an open-source, high-performance proxy service initially developed by Lyft and now maintained by the Cloud Native Computing Foundation (CNCF). It is designed to be a scalable, flexible, and low-latency service proxy, particularly well-suited for microservices architectures and containerized applications.

### Before you begin

In this section you will learn about different options to install, configure and connect to your Envoy server. If you already know how to deploy a Envoy server, you can skip this learning path, and instead explore the [Learn how to Tune Envoy](/learning-paths/servers-and-cloud-computing/envoy_tune/) learning path. 

### Arm deployment options

There are numerous ways to deploy Envoy on Arm: Bare metal, cloud VMs, or the various Envoy services that cloud providers offer. If you already have an Arm system, you can skip over this subsection and continue reading.

* Arm Cloud VMs
  * [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp) learning path
  * [AWS EC2](https://aws.amazon.com/ec2/)
    * [Deploy Arm Instances on AWS using Terraform](/learning-paths/servers-and-cloud-computing/aws-terraform) learning path
  * [Azure VMs](https://azure.microsoft.com/en-us/products/virtual-machines/)
    * [Deploy Arm virtual machines on Azure with Terraform](/learning-paths/servers-and-cloud-computing/azure-terraform) learning path
  * [GCP Compute Engine](https://cloud.google.com/compute)
    * [Deploy Arm virtual machines on Google Cloud Platform (GCP) using Terraform](/learning-paths/servers-and-cloud-computing/gcp) learning path
  * [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
* Additional options are listed in the [Get started with Servers and Cloud Computing](/learning-paths/servers-and-cloud-computing/intro) learning path

###  Envoy documentation

Envoy has a variety of use cases in large enterprise applications. You can explore the [Envoy documentation](https://www.envoyproxy.io/docs/envoy/latest/) for more details.

### Envoy installation options

Though [Installing Envoy](https://www.envoyproxy.io/docs/envoy/latest/start/install) provide scripts to install envoy, but the binaries are too old or cannot work, we recommend you to download the latest Envoy [binary](https://github.com/envoyproxy/envoy/releases) for your target platform or build it from [source](/learning-paths/servers-and-cloud-computing/envoy/build_from_source).

### Running Envoy as a service

Create a config file to run Envoy as a service, as discussed in the next sections, or you can create your own.

Below is a sample config file config-http.yaml:
```console
static_resources:
  listeners:
  - address:
      socket_address:
        address: 0.0.0.0
        port_value: 80
    filter_chains:
    - filters:
      - name: envoy.filters.network.http_connection_manager
        typed_config:
          '@type': type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
          codec_type: AUTO
          stat_prefix: ingress_http
          route_config:
            name: test
            virtual_hosts:
            - name: direct_response_service
              domains:
              - "*"
              routes:
              - match:
                  prefix: "/"
                direct_response:
                  status: 200
                  body:
                    inline_string: "[arm] hello world\n"
          http_filters:
          - name: envoy.filters.http.cors
            typed_config:
              '@type': type.googleapis.com/envoy.extensions.filters.http.cors.v3.Cors
          - name: envoy.filters.http.rbac
            typed_config:
              '@type': type.googleapis.com/envoy.extensions.filters.http.rbac.v3.RBAC
          - name: envoy.filters.http.local_ratelimit
            typed_config:
              '@type': type.googleapis.com/envoy.extensions.filters.http.local_ratelimit.v3.LocalRateLimit
              stat_prefix: http_local_rate_limiter
          - name: envoy.filters.http.fault
            typed_config:
              '@type': type.googleapis.com/envoy.extensions.filters.http.fault.v3.HTTPFault
          - name: envoy.filters.http.router
            typed_config:
              '@type': type.googleapis.com/envoy.extensions.filters.http.router.v3.Router
```

One sample command to run Envoy service:

```console
nohup bin/envoy-static.stripped -c configs/config-http.yaml --concurrency 16 > /dev/null &

Where:
-c <string>,  --config-path <string>
        Path to configuration file
--concurrency <uint32_t>
        # of worker threads to run
```

```console
curl  localhost
```

The output from this command will look similar to:

```output
[arm] hello world
```

Envoy is now running...
