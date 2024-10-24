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
Legends:
✅ - Supports arm64, ❌ - Does not support arm64, ⬆ - Upgrade for arm64 support, ❗ - Some error occurred
------------------------------------------------------------------------------------------------
 
602401143452.dkr.ecr.eu-west-1.amazonaws.com/eks/coredns:v1.9.3-eksbuild.10 ❗
602401143452.dkr.ecr.eu-west-1.amazonaws.com/eks/csi-snapshotter:v6.3.2-eks-1-28-11 ❌
quay.io/kiwigrid/k8s-sidecar:1.21.0 ✅
grafana/grafana:9.3.1 ✅
redis:6.2.4-alpine ✅
602401143452.dkr.ecr.eu-west-1.amazonaws.com/amazon/aws-network-policy-agent:v1.0.6-eksbuild.1 ❗
registry.k8s.io/autoscaling/cluster-autoscaler:v1.25.3 ✅
602401143452.dkr.ecr.eu-west-1.amazonaws.com/eks/csi-node-driver-registrar:v2.9.2-eks-1-28-11 ❌
docker.io/bitnami/metrics-server:0.6.2-debian-11-r20 ⬆
amazon/aws-for-fluent-bit:2.10.0 ✅
quay.io/argoproj/argocd:v2.0.5 ⬆
quay.io/prometheus/node-exporter:v1.5.0 ✅
registry.k8s.io/ingress-nginx/controller:v1.9.4@sha256:5b161f051d017e55d358435f295f5e9a297e66158f136321d9b04520ec6c48a3 ❗
quay.io/prometheus-operator/prometheus-operator:v0.63.0 ✅
registry.k8s.io/kube-state-metrics/kube-state-metrics:v2.8.1 ✅
mirrors--ghcr-io.mirror.com/banzaicloud/vault-secrets-webhook:1.18.0 ✅
quay.io/prometheus-operator/prometheus-config-reloader:v0.63.0 ✅
mirrors--dockerhub.mirror.com/grafana/grafana:9.3.8 ✅
curlimages/curl:7.85.0 ✅
602401143452.dkr.ecr.eu-west-1.amazonaws.com/eks/csi-attacher:v4.4.2-eks-1-28-11 ❗
602401143452.dkr.ecr.eu-west-1.amazonaws.com/eks/livenessprobe:v2.11.0-eks-1-28-11 ❗
busybox:1.31.1 ✅
quay.io/prometheus/prometheus:v2.42.0 ✅
docker.io/bitnami/external-dns:0.14.0-debian-11-r2 ✅
dsgcore--docker.mirror.com/jcaap:3.7 ❗
602401143452.dkr.ecr.eu-west-1.amazonaws.com/eks/csi-provisioner:v3.6.2-eks-1-28-11 ❗
602401143452.dkr.ecr.eu-west-1.amazonaws.com/eks/csi-resizer:v1.9.2-eks-1-28-11 ❗
602401143452.dkr.ecr.eu-west-1.amazonaws.com/eks/kube-proxy:v1.25.16-minimal-eksbuild.1 ❗
quay.io/kiwigrid/k8s-sidecar:1.22.0 ✅
quay.io/prometheus/blackbox-exporter:v0.24.0 ✅
amazon/cloudwatch-agent:1.247350.0b251780 ✅
602401143452.dkr.ecr.eu-west-1.amazonaws.com/eks/aws-ebs-csi-driver:v1.26.0 ❗
sergrua/kube-tagger:release-0.1.1 ❌
docker.io/alpine:3.13 ✅
quay.io/prometheus/alertmanager:v0.25.0 ✅
602401143452.dkr.ecr.eu-west-1.amazonaws.com/amazon-k8s-cni-init:v1.15.4-eksbuild.1 ❗
602401143452.dkr.ecr.eu-west-1.amazonaws.com/amazon-k8s-cni:v1.15.4-eksbuild.1 ❗
```
