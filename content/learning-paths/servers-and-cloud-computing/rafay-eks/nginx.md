---
title: Deploy NGINX to the Amazon EKS cluster and clean up
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploy NGINX

With the Amazon EKS cluster running on Graviton nodes, deploy NGINX to confirm that `arm64` workloads schedule and run correctly.

Create a file named `nginx-graviton.yaml` with the following content:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: nginx
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-arm-deployment
  namespace: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx-arm
  template:
    metadata:
      labels:
        app: nginx-arm
    spec:
      nodeSelector:
        kubernetes.io/arch: arm64   # Pin pods to Graviton (arm64) nodes
      containers:
        - name: nginx
          image: nginx:1.27
          ports:
            - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-arm-svc
  namespace: nginx
spec:
  selector:
    app: nginx-arm
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: ClusterIP
```

The `nodeSelector: kubernetes.io/arch: arm64` field ensures the pod is scheduled only on nodes that report the `arm64` architecture label. The Graviton node you provisioned has this label.

Apply the manifest:

```console
kubectl apply -f nginx-graviton.yaml
```

The output is similar to:

```output
namespace/nginx created
deployment.apps/nginx-arm-deployment created
service/nginx-arm-svc created
```

## Verify the deployment

Check that the pod reaches the `Running` state:

```console
kubectl get pods -n nginx
```

The output is similar to:

```output
NAME                                    READY   STATUS    RESTARTS   AGE
nginx-arm-deployment-6d4f9b8c7d-xk2pq   1/1     Running   0          30s
```

Confirm the service was created:

```console
kubectl get svc -n nginx
```

The output is similar to:

```output
NAME            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
nginx-arm-svc   ClusterIP   10.100.42.137   <none>        80/TCP    30s
```

## Test NGINX connectivity

The NGINX service is type `ClusterIP`, which means it has no external IP and is reachable only from within the cluster network. The cluster also has `publicAccess: false`, so there's no public Kubernetes API endpoint. Both constraints mean you can't test connectivity from your laptop directly. 

Instead, run a one-off pod inside the cluster that sends a request to the service and then deletes itself:

```console
kubectl run curl-test --rm -it --image=curlimages/curl --restart=Never -- curl http://nginx-arm-svc.nginx.svc
```

The output is similar to:

```output
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>
</body>
</html>
pod "curl-test" deleted
```

The NGINX welcome page confirms that the workload is running and reachable on your Graviton-based EKS cluster.

## Clean up resources

Remove the NGINX workload and then delete the cluster to avoid ongoing AWS charges.

Delete the NGINX resources:

```console
kubectl delete -f nginx-graviton.yaml
```

The output is similar to:

```output
namespace "nginx" deleted
deployment.apps "nginx-arm-deployment" deleted
service "nginx-arm-svc" deleted
```

{{< notice warning >}}
Deleting the cluster through RCTL triggers the removal of the EKS control plane, managed node group, and associated CloudFormation stacks in your AWS account. If you don't run this command, AWS will continue to charge you for the running EC2 instances and EKS control plane.
{{< /notice >}}

Delete the EKS cluster through Rafay:

```console
rctl delete cluster demo-eks-graviton
```

## What you've accomplished

You've now deployed NGINX using a manifest that pins pods to `arm64` nodes, verify the pod reaches a `Running` state, and test connectivity from inside the cluster. You then cleaned up all provisioned resources.

Rafay's control plane handles cluster access without requiring a public Kubernetes API endpoint, making it straightforward to run private, Graviton-based EKS clusters at scale.

