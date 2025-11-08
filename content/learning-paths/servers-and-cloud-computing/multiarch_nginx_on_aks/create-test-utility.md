---
title: Create the test utility
weight: 20

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Test utility script

In this section, you'll create a utility script to test and manage your nginx services across both architectures. The script will be used throughout the Learning Path to test services, apply configurations, and access pods.

### Script functionality

The `nginx_util.sh` script provides three main functions:

- **`curl intel|arm|multiarch`** - Test nginx services and show which pod served the request
- **`put btop`** - Install btop monitoring tool on all pods
- **`login intel|arm`** - Interactive bash access to architecture-specific pods

The script conveniently bundles test and logging commands into a single place, making it easy to test, troubleshoot, and view services. 

### Download the utility script

{{% notice Note %}}
The following utility `nginx_util.sh` is provided for your convenience. 

It's a wrapper for kubectl and other commands, utilizing [curl](https://curl.se/).  Make sure you have curl installed before running.

You can click on the link below to review the code before downloading. 
{{% /notice %}}

Copy and paste the following commands into a terminal to download and create the `nginx_util.sh` script:

```bash
curl -o nginx_util.sh https://raw.githubusercontent.com/geremyCohen/nginxOnAKS/refs/heads/main/nginx_util.sh
chmod +x nginx_util.sh
```

In the folder you ran the curl command, you should now see the `nginx_util.sh` script. Test it by running:

```bash
./nginx_util.sh
```

The output presents the usage instructions:

```output
Invalid first argument. Use 'curl', 'wrk', 'put', or 'login'.
```

You're now ready to deploy nginx to the Intel nodes in the cluster.