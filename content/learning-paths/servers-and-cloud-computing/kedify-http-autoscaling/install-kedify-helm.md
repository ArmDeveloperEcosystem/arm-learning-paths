---
title: "Install Kedify using Helm"
description: Install the Kedify build of KEDA, HTTP Scaler, and Kedify Agent with Helm, then verify the components for HTTP autoscaling.
weight: 2
layout: "learningpathall"
---

## Helm charts for installing Kedify

Install Kedify on your Kubernetes cluster with three Helm charts: 

- The Kedify build of KEDA for event-driven autoscaling
- The HTTP Scaler for HTTP-based scaling
- The Kedify Agent to connect your cluster to Kedify's cloud service

After installation, verify that the components are running.

For more information and other installation methods on Arm, see the [Kedify installation documentation](https://docs.kedify.io/installation/helm#installation-on-arm).

## Before you begin

Before installation, you'll need the following:

- A running Kubernetes cluster hosted on any cloud provider or local environment — for example, kind, minikube, Amazon Elastic Kubernetes Service (EKS), Google Kubernetes Engine (GKE), or Azure Kubernetes Service (AKS) 
- Kubectl and Helm installed and configured to communicate with your cluster
- A Kedify Service account to obtain your Organization ID and API key (sign up at the [Kedify dashboard](https://dashboard.kedify.io/))

## Gather Kedify credentials

From the Kedify dashboard, copy your Organization ID (**Organization** → **Details**) and retrieve or create an API key.

If you already have a Kedify Agent deployed, decode the key from the existing Secret:
```bash
kubectl get secret -n keda kedify-agent -o=jsonpath='{.data.apikey}' | base64 --decode
```
Otherwise, in the Kedify dashboard, navigate to **Organization** → **API Keys**, select **Create Agent Key**, and copy the key.

{{% notice Note %}}
The API key is shared across all agent installations. If you regenerate the key, update existing agents and keep it as a secret.
{{% /notice %}}

Optionally, export these values for reuse in the following commands:
```bash
export YOUR_ORG_ID="<your-org-id>"
export YOUR_API_KEY="<your-agent-api-key>"
export CLUSTER_NAME="my-arm-cluster"
```

## Add the Kedify Helm repository

Add the Kedify Helm repository and update your local index:
```bash
helm repo add kedifykeda https://kedify.github.io/charts
helm repo update
```

## Install components with Helm

Most providers such as EKS and AKS schedule pods on Arm nodes when you specify a `nodeSelector` for `kubernetes.io/arch=arm64`. On GKE, Arm nodes commonly have an explicit taint, so you need matching `tolerations`. 

To stay portable across providers, configure both `nodeSelector` and `tolerations` in your Helm values or CLI flags.

### Install the Kedify build of KEDA

Run the following Helm command to install the Kedify build of KEDA into the `keda` namespace:
```bash
helm upgrade --install keda kedifykeda/keda \
  --namespace keda \
  --create-namespace \
  --devel \
  --set "nodeSelector.kubernetes\.io/arch=arm64" \
  --set "tolerations[0].key=kubernetes.io/arch" \
  --set "tolerations[0].operator=Equal" \
  --set "tolerations[0].value=arm64" \
  --set "tolerations[0].effect=NoSchedule"
```

### Install the Kedify HTTP Scaler

Install the Kedify HTTP Scaler with matching node selector and tolerations:
```bash
helm upgrade --install keda-add-ons-http kedifykeda/keda-add-ons-http \
  --namespace keda \
  --devel \
  --set "interceptor.nodeSelector.kubernetes\.io/arch=arm64" \
  --set "interceptor.tolerations[0].key=kubernetes.io/arch" \
  --set "interceptor.tolerations[0].operator=Equal" \
  --set "interceptor.tolerations[0].value=arm64" \
  --set "interceptor.tolerations[0].effect=NoSchedule" \
  --set "scaler.nodeSelector.kubernetes\.io/arch=arm64" \
  --set "scaler.tolerations[0].key=kubernetes.io/arch" \
  --set "scaler.tolerations[0].operator=Equal" \
  --set "scaler.tolerations[0].value=arm64" \
  --set "scaler.tolerations[0].effect=NoSchedule"
```

### Install the Kedify Agent

Edit the cluster name, Organization ID, and API key (or rely on the exported environment variables), then run:
```bash
helm upgrade --install kedify-agent kedifykeda/kedify-agent \
  --namespace keda \
  --set "agent.nodeSelector.kubernetes\.io/arch=arm64" \
  --set "agent.tolerations[0].key=kubernetes.io/arch" \
  --set "agent.tolerations[0].operator=Equal" \
  --set "agent.tolerations[0].value=arm64" \
  --set "agent.tolerations[0].effect=NoSchedule" \
  --set "agent.kedifyProxy.globalValues.nodeSelector.kubernetes\.io/arch=arm64" \
  --set "agent.kedifyProxy.globalValues.tolerations[0].key=kubernetes.io/arch" \
  --set "agent.kedifyProxy.globalValues.tolerations[0].operator=Equal" \
  --set "agent.kedifyProxy.globalValues.tolerations[0].value=arm64" \
  --set "agent.kedifyProxy.globalValues.tolerations[0].effect=NoSchedule" \
  --set clusterName="${CLUSTER_NAME:-my-arm-cluster}" \
  --set agent.orgId="${YOUR_ORG_ID}" \
  --set agent.apiKey="${YOUR_API_KEY}"
```

## Verify installation

List pods in the `keda` namespace to confirm that all components are running:
```bash
kubectl get pods -n keda
```

Pod names might vary. The output is similar to:

```output
NAME                                             READY   STATUS    RESTARTS   AGE
keda-add-ons-http-external-scaler-xxxxx          1/1     Running   0          1m
keda-add-ons-http-interceptor-xxxxx              1/1     Running   0          1m
keda-admission-webhooks-xxxxx                    1/1     Running   0          1m
keda-operator-xxxxx                              1/1     Running   0          1m
keda-operator-metrics-apiserver-xxxxx            1/1     Running   0          1m
kedify-agent-xxxxx                               1/1     Running   0          1m
```

## What you've accomplished

You've gathered Kedify credentials, installed the three Helm charts with Arm node selectors and tolerations, and checked the component pods in the `keda` namespace.

Next, you'll install an ingress controller for the HTTP sample application that you'll deploy.
