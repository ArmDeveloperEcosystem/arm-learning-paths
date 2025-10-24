---
title: Monitor performance with wrk and btop
weight: 70

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Apply configuration updates

Now that you have all your nginx deployments running across Intel and ARM architectures, you can monitor performance across each architecture using wrk to generate load and btop to monitor system performance.

{{% notice Note %}}
This tutorial uses wrk to generate load, which is readily available on apt and brew package managers.  [wrk2](https://github.com/giltene/wrk2) is a modern fork of wrk with additional features.  wrk was chosen for this tutorial due to its ease of install, but if you prefer to install and use wrk2 (or other http load generators) for your testing, feel free to do so.
{{% /notice %}}

### Apply performance configuration

The `nginx_util.sh` script includes a `put config` command that will:

- Apply a performance-optimized nginx configuration to all pods
- Install btop monitoring tool on all pods for system monitoring
- Restart pods with the new configuration

1. Run the following command to apply the configuration updates:

```bash
./nginx_util.sh put btop
```

You will see output similar to the following:

```outputI
Applying custom nginx.conf to all nginx pods...
configmap/nginx-config created
Updating nginx-amd-deployment...
deployment.apps/nginx-amd-deployment patched
Updating nginx-arm-deployment...
deployment.apps/nginx-arm-deployment patched
Updating nginx-intel-deployment...
deployment.apps/nginx-intel-deployment patched
Waiting for pods to restart with new configuration...
Installing btop on all nginx pods...
Installing btop on nginx-amd-deployment-56b547bb47-vgbjj...
✓ btop installed on nginx-amd-deployment-56b547bb47-vgbjj
Installing btop on nginx-arm-deployment-66cb47ddc9-fgmsd...
✓ btop installed on nginx-arm-deployment-66cb547ddc9-fgmsd
Installing btop on nginx-intel-deployment-6f5bff9667-zdrqc...
✓ btop installed on nginx-intel-deployment-6f5bff9667-zdrqc
✅ Custom nginx.conf applied and btop installed on all pods!
```

### Verify configuration updates

2. Check that all pods have restarted with the new configuration:

```bash
kubectl get pods -n nginx
```

You should see all pods with recent restart times.


4. Verify btop is installed and available on both Arm and Intel pods:

```bash
kubectl exec -n nginx $(kubectl get pods -l arch=intel -n nginx -o name | sed 's/pod\///') -- btop --version
kubectl exec -n nginx $(kubectl get pods -l arch=arm -n nginx -o name | sed 's/pod\///') -- btop --version
```

You should see btop version information for both pods.

{{% notice Note %}}
Because pods are ephemeral, btop will need to be reinstalled if the pods are deleted or restarted in the future.  If you get an error saying btop is not found, simply rerun the `./nginx_util.sh put btop` command to reinstall it.
{{% /notice %}}


### Monitor pod performance

5. You can now login to any pod and use btop to monitor system performance:

```bash
# Login to AMD pod (replace with intel or arm as needed)
./nginx_util.sh login arm
```

Once inside the pod, run btop to see real-time system monitoring:

```bash
btop
```

With btop open on the remote pod, from your local machine, run wrk against the pod to generate load.  The nginx_util.sh script includes a wrk wrapper command that makes it easy to use the wrk utility to load test an endpoint:

```bash
./nginx_util.sh wrk arm
```


Press `q` to quit btop when finished.

### Test services still work


You have successfully applied performance optimizations and monitoring tools to your multi-architecture nginx cluster!
