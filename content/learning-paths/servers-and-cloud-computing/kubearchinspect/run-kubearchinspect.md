---
title: Run KubeArchInspect
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How do I run KubeArchInspect?

To run KubeArchInspect, you need to have `kubearchinspect` installed and ensure that the `kubectl` command is configured to connect to your cluster. If not already configured, you should set up `kubectcl` to connect to your cluster. 

Run KubeArchInspect with the following command:

```console
kubearchinspect images 
```

KubeArchInspect connects to the Kubernetes cluster and generates a list of images in use. 

For each image found, it connects to the source registry for the image and checks which architectures are available, producing a report like the example below:

```output
Legend:
-------
✅ - arm64 supported
🆙 - arm64 supported (with update)
❌ - arm64 not supported
🚫 - error occurred
------------------------------------------------------------------------------------------------
🚫 123456789010.dkr.ecr.us-west-2.amazonaws.com/quay/calico/pod2daemon-flexvol:v3.28.0  Authentication Error. The private image could not be queried, please check the docker credentials are present and correct.
🚫 123456789010.dkr.ecr.us-west-2.amazonaws.com/quay/calico/typha:v3.28.0  Authentication Error. The private image could not be queried, please check the docker credentials are present and correct.
✅ busybox
✅ docker.io/bitnami/external-dns:0.14.2-debian-12-r4
✅ docker.io/prom/cloudwatch-exporter:v0.15.3
✅ fluent/fluent-bit:2.2.2
✅ ghcr.io/dexidp/dex:v2.38.0
✅ ghcr.io/maxmind/geoipupdate:v7.0.1
✅ public.ecr.aws/aws-secrets-manager/secrets-store-csi-driver-provider-aws:1.0.r2-56-g41fa54f-2023.11.15.21.38
✅ public.ecr.aws/docker/library/redis:7.2.4-alpine
✅ public.ecr.aws/eks/aws-load-balancer-controller:v2.8.1
✅ public.ecr.aws/karpenter/controller:0.37.2@sha256:0402d38370aca70cc976b1f9b64fc3c50c88c8fe281dc39d0300df89a62bd16e
✅ quay.io/argoproj/argocd:v2.12.6
✅ quay.io/prometheus-operator/prometheus-config-reloader:v0.74.0
✅ quay.io/prometheus/alertmanager:v0.27.0
✅ quay.io/prometheus/node-exporter:v1.8.1
✅ quay.io/prometheus/prometheus:v2.53.0
✅ quay.io/prometheus/pushgateway:v1.8.0
✅ quay.io/tigera/operator:v1.34.0
✅ registry.k8s.io/csi-secrets-store/driver:v1.4.0
✅ registry.k8s.io/ingress-nginx/controller:v1.11.1@sha256:e6439a12b52076965928e83b7b56aae6731231677b01e81818bce7fa5c60161a
✅ registry.k8s.io/kube-state-metrics/kube-state-metrics:v2.12.0
✅ registry.k8s.io/sig-storage/csi-node-driver-registrar:v2.8.0
✅ registry.k8s.io/sig-storage/livenessprobe:v2.10.0
```

