---
title: Apply performance configuration and monitoring tools
weight: 70

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Apply configuration updates

Now that you have all your nginx deployments running across Intel, AMD, and ARM architectures, you can apply performance optimizations and install monitoring tools across all pods using the utility script.

### Apply performance configuration

The `nginx_util.sh` script includes a `put config` command that will:

- Apply a performance-optimized nginx configuration to all pods
- Install btop monitoring tool on all pods for system monitoring
- Restart pods with the new configuration

1. Run the following command to apply the configuration updates:

```bash
./nginx_util.sh put config
```

You will see output similar to the following:

```output
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

### Performance optimizations applied

The custom nginx configuration includes several performance optimizations:

- **Auto worker processes**: `worker_processes auto` scales based on CPU cores
- **File caching**: Optimized for high I/O performance with `open_file_cache`
- **Access logs enabled**: Logs requests for monitoring and debugging
- **TCP optimizations**: `tcp_nopush` and `tcp_nodelay` enabled
- **Connection management**: Optimized timeouts and 100,000 keep-alive requests
- **Memory management**: Automatic connection cleanup for non-responding clients

### Verify configuration updates

2. Check that all pods have restarted with the new configuration:

```bash
kubectl get pods -n nginx
```

You should see all pods with recent restart times.

3. Verify the custom nginx configuration is applied by checking one pod:

```bash
kubectl exec -n nginx $(kubectl get pods -l arch=intel -n nginx -o name | sed 's/pod\///') -- grep "worker_processes auto" /etc/nginx/nginx.conf
```

You should see:
```output
worker_processes auto;
```

4. Verify btop is installed and available:

```bash
kubectl exec -n nginx $(kubectl get pods -l arch=intel -n nginx -o name | sed 's/pod\///') -- btop --version
```

You should see the btop version information.

### Monitor pod performance

5. You can now login to any pod and use btop to monitor system performance:

```bash
# Login to AMD pod (replace with intel or arm as needed)
./nginx_util.sh login amd
```

Once inside the pod, run btop to see real-time system monitoring:

```bash
btop
```

Press `q` to quit btop when finished.

### Test services still work

6. Verify that all services are still responding correctly after the configuration update:

```bash
./nginx_util.sh get intel
./nginx_util.sh get amd
./nginx_util.sh get arm
./nginx_util.sh get multiarch
```

All services should return the nginx welcome page, confirming that the performance optimizations are working correctly.

You have successfully applied performance optimizations and monitoring tools to your multi-architecture nginx cluster!
