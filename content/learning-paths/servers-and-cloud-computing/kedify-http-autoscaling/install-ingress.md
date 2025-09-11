---
title: "Install Ingress Controller"
weight: 3
layout: "learningpathall"
---

Before deploying HTTP applications with Kedify autoscaling, you need an Ingress Controller to handle incoming traffic. Most major cloud providers (AWS EKS, Google GKE, Azure AKS) do not include an Ingress Controller by default in their managed Kubernetes offerings.

{{% notice Note %}}
If your cluster already has an Ingress Controller installed and configured, you can skip this step and proceed directly to the [HTTP Scaling guide](../http-scaling/).
{{% /notice %}}

## Install NGINX Ingress Controller via Helm

Add the NGINX Ingress Controller Helm repository:

```bash
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
```

Install the NGINX Ingress Controller:

```bash
helm upgrade --install ingress-nginx ingress-nginx/ingress-nginx \
  --namespace ingress-nginx \
  --create-namespace \
  \
  --set "controller.nodeSelector.kubernetes\.io/arch=arm64" \
  --set "controller.tolerations[0].key=kubernetes.io/arch" \
  --set "controller.tolerations[0].operator=Equal" \
  --set "controller.tolerations[0].value=arm64" \
  --set "controller.tolerations[0].effect=NoSchedule" \
  \
  --set "controller.admissionWebhooks.patch.nodeSelector.kubernetes\.io/arch=arm64" \
  --set "controller.admissionWebhooks.patch.tolerations[0].key=kubernetes.io/arch" \
  --set "controller.admissionWebhooks.patch.tolerations[0].operator=Equal" \
  --set "controller.admissionWebhooks.patch.tolerations[0].value=arm64" \
  --set "controller.admissionWebhooks.patch.tolerations[0].effect=NoSchedule"
```

Wait for the LoadBalancer to be ready:

```bash
kubectl wait --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/component=controller \
  --timeout=300s
```

## Get the External Endpoint

Get the external IP address or hostname for your ingress controller and save it as an environment variable:

```bash
export INGRESS_IP=$(kubectl get service ingress-nginx-controller --namespace=ingress-nginx -o jsonpath='{.status.loadBalancer.ingress[0].ip}{.status.loadBalancer.ingress[0].hostname}')
echo "Ingress IP/Hostname: $INGRESS_IP"
```

This will save the external IP or hostname in the `INGRESS_IP` environment variable and display it. Note the value:
- **AWS EKS**: You'll see an AWS LoadBalancer hostname (e.g., `a1234567890abcdef-123456789.us-west-2.elb.amazonaws.com`)
- **Google GKE**: You'll see an IP address (e.g., `34.102.136.180`)
- **Azure AKS**: You'll see an IP address (e.g., `20.62.196.123`)

## Configure Access

For this tutorial, you have two options:

### Option 1: DNS Setup (Recommended for production)
Point `application.keda` to your ingress controller's external IP/hostname using your DNS provider.

### Option 2: Host Header (Quick setup)
Use the external IP/hostname directly with a `Host:` header in your requests. When testing, you'll use:

```bash
curl -H "Host: application.keda" http://$INGRESS_IP
```

The `$INGRESS_IP` environment variable contains the actual external IP or hostname from your ingress controller service.

## Verification

Test that the ingress controller is working by checking its readiness:

```bash
kubectl get pods --namespace ingress-nginx
```

You should see the `ingress-nginx-controller` pod in `Running` status.

## Next Steps

Now that you have an Ingress Controller installed and configured, proceed to the [HTTP Scaling guide](../http-scaling/) to deploy an application and configure Kedify autoscaling.
