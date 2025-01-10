---
title: "Kernel, compiler, and libraries"
weight: 3
layout: "learningpathall"
---

##  Kernel configuration

The profile of requests made by clients will differ based on the use case. This means there is no one size fits all set of tuning parameters for Nginx. Use the information below as general guidance to tune Nginx.

### Linux Network Stack

The Linux Network stack settings can be changed in the `/etc/sysctl.conf` file, or by using the `sysctl` command.

Documentation on each of the parameters discussed below can be found in the [admin-guide](https://github.com/torvalds/linux/blob/master/Documentation/admin-guide/sysctl/net.rst) and [networking](https://github.com/torvalds/linux/blob/master/Documentation/networking/ip-sysctl.rst) documentation within the Linux source.

Run the command below to list all kernel parameters.

```bash
sudo sysctl -a
```

Shown below are the network stack settings used for performance testing.

```
sudo sysctl -w net.core.somaxconn=65535
sudo sysctl -w net.core.rmem_max=8388607
sudo sysctl -w net.core.wmem_max=8388607
sudo sysctl -w net.ipv4.tcp_max_syn_backlog=65535
sudo sysctl -w net.ipv4.ip_local_port_range="1024 65535"
sudo sysctl -w net.ipv4.tcp_rmem="4096 8338607 8338607"
sudo sysctl -w net.ipv4.tcp_wmem="4096 8338607 8338607"
```

These settings open up the network stack to make sure it is not a bottleneck.

* `net.core.somaxconn`:
  * This setting is used to select the maximum number of connections the kernel will allow.
  * If the Nginx server is expected to support a large number of clients, it may be helpful to increase this parameter.
  * A value of 65535 is probably excessively large for production. In practice, this just needs to be large enough to support the peak number of connections that will be made.
* `net.core.rmem_max`:
  * This setting is used to set the maximum read socket buffer size.
  * 8MB is likely more than enough for most use cases.
  * Socket buffer utilization can be checked with a tool like `ss` (Socket Statistics). The information provided by this tool can be used to select a value for this parameter.
* `net.core.wmem_max`:
  * This setting is used to set the maximum write socket buffer size.
  * 8MB is likely more than enough for most use cases.
  * Socket buffer utilization can be checked with a tool like `ss` (Socket Statistics). The information provided by this tool can be used to select a value for this parameter.
* `net.ipv4.tcp_max_syn_backlog`:
  * This setting is used to select the maximum number of connection requests that are pending but not established yet.
  * A value of 65535 is probably excessively large for production. In practice, this just needs to be large enough to support the peak number of connection requests that will be made.
* `net.ipv4.ip_local_port_range`:
  * This setting is used to select the range of ports the kernel can use.
  * The port range is expanded above. Typically the default range is sufficient.
* `net.ipv4.tcp_rmem`:
  * This setting is used to set the maximum TCP read socket buffer size.
  * 8MB is likely more than enough for most use cases.
  * TCP buffer utilization can be checked with a tool like `ss` (Socket Statistics). The information provided by this tool can be used to select a value for this parameter.
* `net.ipv4.tcp_wmem`:
  * This setting is used to set the maximum TCP write socket buffer size.
  * 8MB is likely more than enough for most use cases.
  * TCP buffer utilization can be checked with a tool like `ss` (Socket Statistics). The information provided by this tool can be used to select a value for this parameter.

##  Compiler Considerations

The easiest way to gain performance is to use the latest version of GCC. Aside from that, the flag `-mcpu` can be used to potentially gain additional performance. Usage of this flag is explained in the [Migrating C/C++ applications](/learning-paths/servers-and-cloud-computing/migration/c/) section of the [Migrating applications to Arm servers](/learning-paths/servers-and-cloud-computing/migration/) learning path.

If you need to understand how to configure a build of Nginx. Please review the [build Nginx from source](/learning-paths/servers-and-cloud-computing/nginx/build_from_source) section of the [Learn to deploy Nginx learning path](/learning-paths/servers-and-cloud-computing/nginx/).

##  OpenSSL

Nginx relies on [OpenSSL](https://www.openssl.org/) for cryptographic operations. Thus, the version of OpenSSL used with Nginx (and the GCC version and switches used to compile it) can impact performance. Typically using the Linux distribution default version of OpenSSL is sufficient.

However, it is possible to use newer versions of OpenSSL which could yield performance improvements. This is achieved by using the `--with-openssl` switch when configuring the Nginx build. Point this switch to the directory that contains the source code of the version of OpenSSL you'd like to have Nginx link to. The Nginx build system takes care of the rest. There is also a `--with-openssl-opt` switch which allows you to add options to the build for OpenSSL.

The version of OpenSSL Nginx is using can be verified by running the command `nginx -V`.

##  Perl Compatible Regular Expressions (PCRE)

Nginx relies on [PCRE](https://www.pcre.org/) for regular expression processing. One scenario where regular expressions are used is for an API Gateway. Typically, using the Linux distribution default version of PCRE is sufficient. However, it is possible to use a newer version of PCRE to potentially gain performance. The Nginx [installation instructions](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/#compiling-and-installing-from-source) explain how to build the latest version of PCRE if this is something you want to explore.

##  zlib for HTTP response compression

Nginx relies on [zlib](https://zlib.net/) for HTTP response compression (when the `ngx_http_gzip_module` directives are used). Typically, using the Linux distribution default version of zlib is sufficient. However, it is possible to use a newer version of zlib to potentially gain performance. The Nginx [installation instructions](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/#compiling-and-installing-from-source) explain how to build the latest version of zlib if this is something you want to explore.