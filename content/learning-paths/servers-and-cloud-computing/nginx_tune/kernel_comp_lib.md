---
title: Tune kernel, compiler, and library settings for performance on Arm
description: Tune Linux network settings and evaluate compiler, OpenSSL, PCRE, and zlib choices that can affect NGINX performance on Arm-based platforms.
weight: 3
layout: "learningpathall"
---

## Optimize kernel network stack settings

NGINX tuning doesn't stop at `nginx.conf`. Foundational settings such as kernel network queues, socket buffers, compiler choices, and TLS libraries can affect throughput and latency. Treat these settings as part of the same measurement process you use for NGINX directives.

### Linux network stack

You can change Linux network stack settings in `/etc/sysctl.conf`, or by using the `sysctl` command.

For details about these parameters, see the Linux kernel [sysctl network admin guide](https://github.com/torvalds/linux/blob/master/Documentation/admin-guide/sysctl/net.rst) and [IP sysctl documentation](https://github.com/torvalds/linux/blob/master/Documentation/networking/ip-sysctl.rst).

Run the following command to list all kernel parameters:

```bash
sudo sysctl -a
```

The following commands show example network settings for high-connection workloads:

```bash
sudo sysctl -w net.core.somaxconn=65535
sudo sysctl -w net.core.rmem_max=8388608
sudo sysctl -w net.core.wmem_max=8388608
sudo sysctl -w net.ipv4.tcp_max_syn_backlog=65535
sudo sysctl -w net.ipv4.ip_local_port_range="1024 65535"
sudo sysctl -w net.ipv4.tcp_rmem="4096 8388608 8388608"
sudo sysctl -w net.ipv4.tcp_wmem="4096 8388608 8388608"
```

These values are intentionally large. Size them for your expected connection rate, request pattern, and available memory.

- `net.core.somaxconn`: Selects the maximum number of queued connections the kernel allows. If the NGINX server needs to support a large number of clients, it can be helpful to increase this parameter.

  A value of 65535 is likely excessive for many deployments. In practice, this value needs to be large enough to support the peak number of queued connections.
- `net.core.rmem_max`:  Selects the maximum read socket buffer size. `8 MiB` is likely more than enough for most use cases.

  Use a tool such as `ss` to check socket buffer utilization and set a value for this parameter.
- `net.core.wmem_max`: Selects the maximum write socket buffer size. `8 MiB` is likely more than enough for most use cases.
  
  Use a tool such as `ss` to check socket buffer utilization and set a value for this parameter.
- `net.ipv4.tcp_max_syn_backlog`: Selects the maximum number of connection requests that are pending but not established yet.
  
  A value of 65535 is likely excessive for many deployments. In practice, this value needs to be large enough to support the peak number of pending connection requests.
- `net.ipv4.ip_local_port_range`: Selects the range of local ports the kernel can use. The example expands the port range. The default range is sufficient for many deployments.
- `net.ipv4.tcp_rmem`: Selects the TCP read socket buffer size. `8 MiB` is likely more than enough for most use cases.
  
  Use a tool such as `ss` to check TCP buffer utilization and set a value for this parameter.
- `net.ipv4.tcp_wmem`: Selects the TCP write socket buffer size. `8 MiB` is likely more than enough for most use cases.
  
  Use a tool such as `ss` to check TCP buffer utilization and set a value for this parameter.

## Compiler considerations

If you build NGINX from source, the compiler version and optimization flags can affect performance. Use a recent version of GCC, and consider flags such as `-mcpu` and `-flto` for additional optimization. For more information about these flags, see the [Migrating C/C++ applications](/learning-paths/servers-and-cloud-computing/migration/c/) section of the [Migrating applications to Arm servers](/learning-paths/servers-and-cloud-computing/migration/) Learning Path.

When you configure an NGINX source build, pass compiler flags with the `--with-cc-opt` option.

To understand how to configure an NGINX build, see the [build NGINX from source](/learning-paths/servers-and-cloud-computing/nginx/build_from_source/) section of the [Learn how to deploy NGINX](/learning-paths/servers-and-cloud-computing/nginx/) Learning Path.

## OpenSSL

NGINX relies on [OpenSSL](https://www.openssl.org/) for cryptographic operations. The OpenSSL version, GCC version, and compiler switches used to build OpenSSL can affect TLS performance. The Linux distribution default version of OpenSSL is sufficient for many deployments.

Newer versions of OpenSSL might improve performance for some TLS workloads. To use a specific OpenSSL source tree, pass the `--with-openssl` switch when configuring the NGINX build. Point this switch to the directory that contains the source code of the OpenSSL version you want NGINX to link to. You can also use `--with-openssl-opt` to pass options to the OpenSSL build.

You can also build NGINX with OpenSSL-compatible alternatives for some use cases. For example, the NGINX [QUIC and HTTP/3 documentation](https://nginx.org/en/docs/quic.html) shows how to configure NGINX with BoringSSL, LibreSSL, or QuicTLS. Consider this when you have a specific TLS or QUIC reason to evaluate another library, and measure the result with your workload.

Run `nginx -V` to check the TLS library information and configure options used by your NGINX build.

## Perl Compatible Regular Expressions (PCRE)

NGINX relies on [PCRE](https://www.pcre.org/) for regular expression processing. One scenario where regular expressions are used is an API gateway path rewrite. The Linux distribution default version of PCRE is sufficient for many deployments. A newer version of PCRE might improve performance for regular expression-heavy configurations. 

To learn how to build PCRE with NGINX from source, see the NGINX [installation instructions](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/#compiling-and-installing-from-source).

## zlib for HTTP response compression

NGINX relies on [zlib](https://zlib.net/) for HTTP response compression when the `ngx_http_gzip_module` directives are used. The Linux distribution default version of zlib is sufficient for many deployments. A newer version of zlib might improve performance for compression-heavy workloads.

 To learn how to build zlib with NGINX from source, see the NGINX [installation instructions](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/#compiling-and-installing-from-source).

## What you've learned and what's next

You've now learned about different kernel, compiler, and library optimizations that you can make to tune NGINX performance.

Next, you'll review the configuration for a static file server and learn about optimizations that you can make.
