---
title: "Install an ingress controller"
weight: 3
layout: "learningpathall"
---

## Install an ingress controller for HTTP autoscaling on Kubernetes

Before deploying HTTP applications with Kedify autoscaling, you need an ingress controller to handle incoming traffic. Most managed Kubernetes services (AWS EKS, Google GKE, Azure AKS) do not include an ingress controller by default. In this Learning Path, you install the NGINX Ingress Controller with Helm and target arm64 nodes.

{{% notice Note %}}
If your cluster already has an ingress controller installed and configured, you can skip this step and proceed to the [Autoscale HTTP applications with Kedify and Kubernetes Ingress section](../http-scaling/).
{{% /notice %}}

## Install the NGINX Ingress Controller with Helm

Add the NGINX Ingress Controller Helm repository:
```bash
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
```

Install the NGINX Ingress Controller (with `nodeSelector` and `tolerations` for arm64):
```bash
helm upgrade --install ingress-nginx ingress-nginx/ingress-nginx   --namespace ingress-nginx   --create-namespace   --set "controller.nodeSelector.kubernetes\.io/arch=arm64"   --set "controller.tolerations[0].key=kubernetes.io/arch"   --set "controller.tolerations[0].operator=Equal"   --set "controller.tolerations[0].value=arm64"   --set "controller.tolerations[0].effect=NoSchedule"   --set "controller.admissionWebhooks.patch.nodeSelector.kubernetes\.io/arch=arm64"   --set "controller.admissionWebhooks.patch.tolerations[0].key=kubernetes.io/arch"   --set "controller.admissionWebhooks.patch.tolerations[0].operator=Equal"   --set "controller.admissionWebhooks.patch.tolerations[0].value=arm64"   --set "controller.admissionWebhooks.patch.tolerations[0].effect=NoSchedule"
```

Wait for the load balancer to be ready:
```bash
kubectl wait --namespace ingress-nginx   --for=condition=ready pod   --selector=app.kubernetes.io/component=controller   --timeout=300s
```

Managed clouds may take a few minutes to allocate a public IP address or hostname.

## Get the external endpoint

Retrieve the external IP address or hostname and store it in an environment variable:
```bash
export INGRESS_IP=$(kubectl get service ingress-nginx-controller   --namespace=ingress-nginx   -o jsonpath='{.status.loadBalancer.ingress[0].ip}{.status.loadBalancer.ingress[0].hostname}')
echo "Ingress IP/Hostname: $INGRESS_IP"
```

Typical values by provider:
- **AWS EKS**: Load balancer hostname (for example, `a1234567890abcdef-123456789.us-west-2.elb.amazonaws.com`)
- **Google GKE**: IP address (for example, `34.102.136.180`)
- **Azure AKS**: IP address (for example, `20.62.196.123`)

If no value is printed, wait briefly and re-run the command.

## Configure access

You have two options:

- Option 1: DNS (recommended for production):
  create a DNS record pointing `application.keda` to the external IP address or hostname of your ingress controller.

- Option 2: host header (quick test):  
  use the external IP address or hostname directly with a `Host:` header:
  ```bash
  curl -H "Host: application.keda" http://$INGRESS_IP
  ```
  Here, `$INGRESS_IP` expands to the external IP address or hostname of the ingress controller.

## Verify the installation

List the controller pods and confirm they are running:
```bash
kubectl get pods --namespace ingress-nginx
```

You should see the `ingress-nginx-controller` pod in `Running` status.

Now that you have an ingress controller installed and configured, proceed to the next section to deploy an application and configure Kedify autoscaling.
