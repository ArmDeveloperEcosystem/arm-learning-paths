---
title: Create the test utility
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you'll create a utility script that simplifies working with your multi-architecture Kubernetes deployment. This script acts as a convenient wrapper around common `kubectl` and testing commands, making it easier to interact with `nginx` pods across different architectures.

Instead of typing long `kubectl` commands repeatedly, you'll use this utility to quickly test services, monitor performance, and access pods on both Arm and Intel nodes. This approach saves time and reduces errors, especially when comparing behavior across architectures.

By the end of this section, you'll have a ready-to-use tool that streamlines the testing and monitoring tasks you'll perform throughout the rest of this Learning Path.

## Get to know the utility script
The utility script provides three main functions to help you work with your multi-architecture `nginx` deployment. You can use it to test services across different architectures, monitor performance, and access pods directly.

The script provides the following key commands to interact with your `nginx` deployment:

- `curl intel|arm|multiarch` tests `nginx` services and show which pod served the request
- `put btop` installs `btop` monitoring tool on all pods
- `login intel|arm` is an interactive bash access to architecture-specific pods

These commands streamline common tasks you'll perform when working with multi-architecture deployments. The `curl` command helps you verify that requests are being properly distributed across different architectures, while the `login` command gives you direct access to pods for debugging or configuration changes.

The script conveniently bundles test and logging commands into a single place, making it easy to test, troubleshoot, and view services. 

## Download the utility script

{{% notice Note %}}
The following utility `nginx_util.sh` is provided for your convenience. 

It's a wrapper for `kubectl` and other commands, utilizing [curl](https://curl.se/).  Make sure you have curl installed before running.

You can review the code before downloading by visiting the [GitHub repository](https://raw.githubusercontent.com/geremyCohen/nginxOnAKS/refs/heads/main/nginx_util.sh).
{{% /notice %}}

Copy and paste the following commands into a terminal to download and create the `nginx_util.sh` script:

```bash
curl -o nginx_util.sh https://raw.githubusercontent.com/geremyCohen/nginxOnAKS/refs/heads/main/nginx_util.sh
chmod +x nginx_util.sh
```

In the folder you ran the `curl` command, you should now see the `nginx_util.sh` script. Test it by running:

```bash
./nginx_util.sh
```
The script displays its usage instructions:

```output
Invalid first argument. Use 'curl', 'wrk', 'put', or 'login'.
```

You're now ready to deploy `nginx` to the Intel nodes in the cluster.