---
title: "Install an ingress controller for testing HTTP autoscaling"
description: Install Traefik with Helm and prepare an ingress endpoint for testing Kedify HTTP autoscaling on Kubernetes.
weight: 3
layout: "learningpathall"
---

## Install Traefik with Helm

To expose the sample application, you need an ingress controller to handle incoming traffic. One option is to use Traefik with the standard Kubernetes Ingress API and schedule Traefik on arm64 nodes.

{{% notice Note %}}
- If your cluster already has an ingress controller installed and configured, you can skip this step and proceed to [Deploy an HTTP application through Kubernetes Ingress](/learning-paths/servers-and-cloud-computing/kedify-http-autoscaling/http-scaling/).
- Before installing Traefik, ensure that you're using Kubernetes version 1.25 or later.
{{% /notice %}}

Add the Traefik Helm repository:
```bash
helm repo add traefik https://traefik.github.io/charts
helm repo update
```

Install Traefik with a node selector and toleration for arm64 nodes. The chart creates an IngressClass named `traefik` and a LoadBalancer service. Set `ingressClass.isDefaultClass=false` so that the installation doesn't change the default class for other ingress resources:
```bash
helm upgrade --install traefik traefik/traefik \
  --version 41.6.1 \
  --namespace traefik \
  --create-namespace \
  --set "nodeSelector.kubernetes\.io/arch=arm64" \
  --set "tolerations[0].key=kubernetes.io/arch" \
  --set "tolerations[0].operator=Equal" \
  --set "tolerations[0].value=arm64" \
  --set "tolerations[0].effect=NoSchedule" \
  --set ingressClass.isDefaultClass=false
```

Confirm the Traefik Deployment is available and its `IngressClass` exists:
```bash
kubectl wait --namespace traefik --for=condition=available deployment/traefik --timeout=300s
kubectl get ingressclass traefik
```

Managed clouds can take a few minutes to allocate a public IP address or hostname for the Traefik service.

## Get the external endpoint

Retrieve the Traefik service's external IP address or hostname and store it in an environment variable:
```bash
export INGRESS_ADDRESS=$(kubectl get service traefik --namespace traefik -o jsonpath='{.status.loadBalancer.ingress[0].ip}{.status.loadBalancer.ingress[0].hostname}')
echo "Ingress address: $INGRESS_ADDRESS"
```

The following are typical endpoint values by cloud provider:
- Amazon Elastic Kubernetes Service (EKS): Load balancer hostname (for example, `a1234567890abcdef-123456789.us-west-2.elb.amazonaws.com`)
- Google Kubernetes Engine (GKE): IP address (for example, `34.102.136.180`)
- Azure Kubernetes Service (AKS): IP address (for example, `20.62.196.123`)

If no value is printed on a managed cluster, wait briefly and run the command again. For a local cluster such as k3d, forward a local port to Traefik in a separate terminal. Use this method even if the service reports an address on the cluster's private container network:

```bash
kubectl port-forward --namespace traefik service/traefik 8080:80
```

Keep that terminal open. In your original terminal, use the local address for the remaining steps:

```bash
export INGRESS_ADDRESS=127.0.0.1:8080
```

## Configure access to the applications

You have two options for configuring access:

- DNS (recommended for production):
  Create a DNS record pointing `application.keda` to the external IP address or hostname of your ingress controller.

- Host header (recommended for a quick test):
  Use `INGRESS_ADDRESS` with a `Host: application.keda` header when you test the application. The address can be Traefik's external endpoint or your forwarded local port.

## Verify the installation

List the controller pods and confirm that they're running:
```bash
kubectl get pods --namespace traefik
```

You should see the `traefik` pod in `Running` status.

## What you've accomplished and what's next

You've installed Traefik with Helm, checked its Deployment, IngressClass, and pods, and prepared an ingress endpoint and access method for testing.

Next, you'll deploy an HTTP application through Kubernetes Ingress and verify its HTTP response, then configure and test Kedify autoscaling.
