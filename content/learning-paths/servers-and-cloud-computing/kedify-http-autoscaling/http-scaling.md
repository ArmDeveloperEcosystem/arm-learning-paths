---
title: "Deploy an HTTP application through Kubernetes Ingress"
description: Deploy a sample HTTP application through Kubernetes Ingress and verify that its endpoint returns an HTTP response.
weight: 4
layout: "learningpathall"
---

## Deploy and verify an HTTP application

You'll deploy a sample HTTP application and expose it through Kubernetes Ingress. Then, you'll send a request to verify that its endpoint returns an HTTP response.

## Configure the ingress address

Before testing the application, make sure that `INGRESS_ADDRESS` is set to your ingress controller's external IP address or hostname. For a local cluster, you can use the address that you forwarded using `port-forward` earlier.

If you completed [Install an ingress controller for HTTP autoscaling in Kubernetes](/learning-paths/servers-and-cloud-computing/kedify-http-autoscaling/install-ingress/), you should already have this set. Otherwise, if you installed Traefik separately, run:

```bash
export INGRESS_ADDRESS=$(kubectl get service traefik --namespace traefik -o jsonpath='{.status.loadBalancer.ingress[0].ip}{.status.loadBalancer.ingress[0].hostname}')
echo "Ingress address: $INGRESS_ADDRESS"
```
If the service has no external address, use `port-forward`.

{{% notice Note %}}
If you use an existing ingress controller, set `INGRESS_ADDRESS` to its endpoint and change `ingressClassName` in the following manifest to its `IngressClass` name.
{{% /notice %}}

## Deploy the application and configure ingress

Now you'll deploy an HTTP server and expose it using an `Ingress` resource. For more informaton, see the [Kedify sample HTTP-server source code](https://github.com/kedify/examples/tree/main/samples/http-server).

Run the following command to deploy your application:

```bash
cat <<'EOF' | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: application
spec:
  replicas: 1
  selector:
    matchLabels:
      app: application
  template:
    metadata:
      labels:
        app: application
    spec:
      nodeSelector:
        kubernetes.io/arch: arm64
      tolerations:
        - key: "kubernetes.io/arch"
          operator: "Equal"
          value: "arm64"
          effect: "NoSchedule"
      containers:
        - name: application
          image: ghcr.io/kedify/sample-http-server:latest
          imagePullPolicy: Always
          ports:
            - name: http
              containerPort: 8080
              protocol: TCP
          env:
            - name: RESPONSE_DELAY
              value: "0.3"
---
apiVersion: v1
kind: Service
metadata:
  name: application-service
spec:
  ports:
    - name: http
      protocol: TCP
      port: 8080
      targetPort: http
  selector:
    app: application
  type: ClusterIP
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: application-ingress
spec:
  ingressClassName: traefik
  rules:
    - host: application.keda
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: application-service
                port:
                  number: 8080
EOF
```

The manifest includes the following options that affect scaling behavior:

- `RESPONSE_DELAY` is set in the `Deployment` manifest and adds approximately 300 ms latency per request. This slower response time increases the number of concurrent requests, making scaling effects easier to observe.
- The ingress uses the host `application.keda`. To access this app, use your ingress controller's address with a `Host:` header.

## Verify that the application is running

Run the following command to check that one replica is ready:

```bash
kubectl get deployment application
```

The output is similar to:

```output
NAME          READY   UP-TO-DATE   AVAILABLE   AGE
application   1/1     1            1           3m44s
```

## Test the application

After the application and ingress are deployed, verify that everything is working correctly by sending a request to the exposed endpoint.

Run the following command:

```bash
curl -I -H "Host: application.keda" http://$INGRESS_ADDRESS
```

The output is similar to:

```output
HTTP/1.1 200 OK
Date: Thu, 11 Sep 2025 14:11:24 GMT
Content-Type: text/html
Content-Length: 301
Connection: keep-alive
```

## What you've accomplished

You've deployed the sample HTTP application through Kubernetes Ingress and tested its endpoint for an HTTP response. 

Next, you'll configure and test Kedify HTTP autoscaling using this application and `INGRESS_ADDRESS`.