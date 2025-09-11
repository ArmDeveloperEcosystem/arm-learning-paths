---
title: "Install Kedify via Helm"
weight: 2
layout: "learningpathall"
---

This page installs Kedify on your cluster using Helm. You’ll add the Kedify chart repo, install KEDA (Kedify build), the HTTP Scaler, and the Kedify Agent, then verify everything is running.

For more details and all installation methods, see Kedify installation docs: https://docs.kedify.io/installation/helm#installation-on-arm

## Prerequisites

- A running Kubernetes cluster (kind, minikube, EKS, GKE, AKS, etc.)
- kubectl and helm installed and configured to talk to your cluster
- Kedify Service account (https://dashboard.kedify.io/) to obtain Organization ID and API Key — log in or create an account if you don’t have one

## Prepare installation

1) Get your Organization ID: In the Kedify dashboard (https://dashboard.kedify.io/) go to Organization -> Details and copy the ID.

2) Get your API key:
- If you already have a Kedify Agent deployed, you can retrieve it from the existing Secret:

```bash
kubectl get secret -n keda kedify-agent -o=jsonpath='{.data.apikey}' | base64 --decode
```

- Otherwise, in the Kedify dashboard (https://dashboard.kedify.io/) go to Organization -> API Keys, click Create Agent Key, and copy the key.

Note: The API Key is shared across all your Agent installations. If you regenerate it, update existing Agent installs and keep it secret.

## Helm repository

Add the Kedify Helm repository and update your local index:

```bash
helm repo add kedifykeda https://kedify.github.io/charts
helm repo update
```

## Helm installation

Most providers like AWS EKS and Azure AKS automatically place pods on ARM nodes when you specify `nodeSelector` for `kubernetes.io/arch=arm64`. However, Google Kubernetes Engine (GKE) applies an explicit taint on ARM nodes, requiring matching `tolerations`.

To ensure a portable deployment strategy across all cloud providers, we recommend configuring both `nodeSelector` and `tolerations` in your Helm values or CLI flags.

Install each component into the keda namespace. Replace placeholders where noted.

1) Install Kedify build of KEDA:

```bash
helm upgrade --install keda kedifykeda/keda \
  --namespace keda \
  --create-namespace \
  --set "nodeSelector.kubernetes.io/arch=arm64" \
  --set "tolerations[0].key=kubernetes.io/arch" \
  --set "tolerations[0].operator=Equal" \
  --set "tolerations[0].value=arm64" \
  --set "tolerations[0].effect=NoSchedule"
```

2) Install Kedify HTTP Scaler:

```bash
helm upgrade --install keda-add-ons-http kedifykeda/keda-add-ons-http \
  --namespace keda
  --set "interceptor.nodeSelector.kubernetes.io/arch=arm64" \
  --set "interceptor.tolerations[0].key=kubernetes.io/arch" \
  --set "interceptor.tolerations[0].operator=Equal" \
  --set "interceptor.tolerations[0].value=arm64" \
  --set "interceptor.tolerations[0].effect=NoSchedule" \
  --set "scaler.nodeSelector.kubernetes.io/arch=arm64" \
  --set "scaler.tolerations[0].key=kubernetes.io/arch" \
  --set "scaler.tolerations[0].operator=Equal" \
  --set "scaler.tolerations[0].value=arm64" \
  --set "scaler.tolerations[0].effect=NoSchedule"
```

3) Install Kedify Agent (edit clusterName, orgId, apiKey):

```bash
helm upgrade --install kedify-agent kedifykeda/kedify-agent \
  --namespace keda \
  --set "agent.nodeSelector.kubernetes.io/arch=arm64" \
  --set "agent.tolerations[0].key=kubernetes.io/arch" \
  --set "agent.tolerations[0].operator=Equal" \
  --set "agent.tolerations[0].value=arm64" \
  --set "agent.tolerations[0].effect=NoSchedule" \
  --set "agent.kedifyProxy.globalValues.nodeSelector.kubernetes.io/arch=arm64" \
  --set "agent.kedifyProxy.globalValues.tolerations[0].key=kubernetes.io/arch" \
  --set "agent.kedifyProxy.globalValues.tolerations[0].operator=Equal" \
  --set "agent.kedifyProxy.globalValues.tolerations[0].value=arm64" \
  --set "agent.kedifyProxy.globalValues.tolerations[0].effect=NoSchedule" \
  \
  --set clusterName="my-arm-cluster" \
  --set agent.orgId="$YOUR_ORG_ID" \
  --set agent.apiKey="$YOUR_API_KEY"
```

## Verify installation

```bash
kubectl get pods -n keda
```

Expected example (names may differ):

```text
NAME                                             READY   STATUS    RESTARTS   AGE
keda-add-ons-http-external-scaler-xxxxx          1/1     Running   0          1m
keda-add-ons-http-interceptor-xxxxx              1/1     Running   0          1m
keda-admission-webhooks-xxxxx                    1/1     Running   0          1m
keda-operator-xxxxx                              1/1     Running   0          1m
keda-operator-metrics-apiserver-xxxxx            1/1     Running   0          1m
kedify-agent-xxxxx                               1/1     Running   0          1m
```

Proceed to the next section to deploy a sample HTTP app and test autoscaling.
