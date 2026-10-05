---
title: "Install an ingress controller"
weight: 3
layout: "learningpathall"
---

## Install an ingress controller for HTTP autoscaling on Kubernetes

To expose the sample application, you need an ingress controller to handle incoming traffic. This Learning Path uses Traefik with the standard Kubernetes Ingress API and schedules Traefik on arm64 nodes. The Traefik chart used here needs Kubernetes 1.25 or later.

{{% notice Note %}}
If your cluster already has an ingress controller installed and configured, you can skip this step and proceed to the [Autoscale HTTP applications with Kedify and Kubernetes Ingress section](../http-scaling/).
{{% /notice %}}

## Install Traefik with Helm

Add the Traefik Helm repository:
```bash
helm repo add traefik https://traefik.github.io/charts
helm repo update
```

Install Traefik with a node selector and toleration for arm64 nodes. The chart creates an IngressClass named `traefik` and a LoadBalancer Service. Set `ingressClass.isDefaultClass=false` so this installation does not change the default class for other Ingress resources:
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

Confirm the Traefik Deployment is available and its IngressClass exists:
```bash
kubectl wait --namespace traefik --for=condition=available deployment/traefik --timeout=300s
kubectl get ingressclass traefik
```

Managed clouds can take a few minutes to allocate a public IP address or hostname for the Traefik Service.

## Get the external endpoint

Retrieve the Traefik Service's external IP address or hostname and store it in an environment variable:
```bash
export INGRESS_ADDRESS=$(kubectl get service traefik --namespace traefik -o jsonpath='{.status.loadBalancer.ingress[0].ip}{.status.loadBalancer.ingress[0].hostname}')
echo "Ingress address: $INGRESS_ADDRESS"
```

Typical values by provider:
- **AWS EKS**: Load balancer hostname (for example, `a1234567890abcdef-123456789.us-west-2.elb.amazonaws.com`)
- **Google GKE**: IP address (for example, `34.102.136.180`)
- **Azure AKS**: IP address (for example, `20.62.196.123`)

If no value is printed on a managed cluster, wait briefly and run the command again. For a local cluster such as k3d, forward a local port to Traefik in a separate terminal. Use this method even if the Service reports an address on the cluster's private container network:

```bash
kubectl port-forward --namespace traefik service/traefik 8080:80
```

Keep that terminal open. In your original terminal, use the local address for the remaining steps:

```bash
export INGRESS_ADDRESS=127.0.0.1:8080
```

## Configure access

You have two options:

- Option 1: DNS (recommended for production):
  create a DNS record pointing `application.keda` to the external IP address or hostname of your ingress controller.

- Option 2: Host header (quick test):
  Use `INGRESS_ADDRESS` with a `Host: application.keda` header when you test the application in the next section. The address can be Traefik's external endpoint or your forwarded local port.

## Verify the installation

List the controller pods and confirm they are running:
```bash
kubectl get pods --namespace traefik
```

You should see the `traefik` pod in `Running` status.

Now that you have an ingress controller installed and configured, proceed to the next section to deploy an application and configure Kedify autoscaling.
