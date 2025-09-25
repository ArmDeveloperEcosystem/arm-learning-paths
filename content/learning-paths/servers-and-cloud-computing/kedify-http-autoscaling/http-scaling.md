---
title: "HTTP Scaling for Ingress-Based Applications"
weight: 4
layout: "learningpathall"
---

Use this section to get a quick, hands-on feel for Kedify HTTP autoscaling. We’ll deploy a small web service, expose it through a standard Kubernetes Ingress, and rely on Kedify’s autowiring to route traffic via its proxy so requests are measured and drive scaling.

Scale a real HTTP app exposed through Kubernetes Ingress using Kedify’s [kedify-http](https://docs.kedify.io/scalers/http-scaler/) scaler. You will deploy a simple app, enable autoscaling with a [ScaledObject](https://keda.sh/docs/latest/concepts/scaling-deployments/), generate load, and observe the system scale out and back in (including scale-to-zero when idle).

## How it works

With ingress autowiring enabled, Kedify automatically routes traffic through its proxy before it reaches your Service/Deployment:

```
Ingress → kedify-proxy → Service → Deployment
```

The [Kedify Proxy](https://docs.kedify.io/scalers/http-scaler/#kedify-proxy) gathers request metrics used by the scaler to make decisions.

## What you’ll deploy

- Deployment & Service: an HTTP server with a small response delay to simulate work
- Ingress: public entry using host `application.keda`
- ScaledObject: Kedify HTTP scaler with `trafficAutowire: ingress`

## Step 0 — Set up Ingress IP environment variable

Before testing the application, ensure you have the `INGRESS_IP` environment variable set with your ingress controller's external IP or hostname.

If you followed the [Install Ingress Controller](../install-ingress/) guide, you should already have this set. If not, or if you're using an existing ingress controller, run this command:

```bash
export INGRESS_IP=$(kubectl get service ingress-nginx-controller --namespace=ingress-nginx -o jsonpath='{.status.loadBalancer.ingress[0].ip}{.status.loadBalancer.ingress[0].hostname}')
echo "Ingress IP/Hostname: $INGRESS_IP"
```
You should now have the correct IP address or hostname stored in the `$INGRESS_IP` environment variable. If the command doesn't print any value, please repeat it after some time.

{{% notice Note %}}
If your ingress controller service has a different name or namespace, adjust the command accordingly. For example, some installations use `nginx-ingress-controller` or place it in a different namespace.
{{% /notice %}}

## Step 1 — Create the application and Ingress

Let's start with deploying an application that responds to an incoming HTTP server and is exposed via Ingress. You can check the source code of the application on [GitHub](https://github.com/kedify/examples/tree/main/samples/http-server).

#### Deploy the application

Run the following command to deploy our application:

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
  ingressClassName: nginx
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

Notes:
- `RESPONSE_DELAY` adds ~300ms latency per request, making scaling effects easier to see.
- The Ingress uses host `application.keda`. To access this app we will use your ingress controller’s IP with a `Host:` header (shown below).

#### Verify the application is running correctly

Let's check that we have 1 replica of the application deployed and ready:

```bash
kubectl get deployment application
```

In the output we should see 1 replica ready:
```
NAME          READY   UP-TO-DATE   AVAILABLE   AGE
application   1/1     1            1           3m44s
```

#### Test the application
Hit the app to confirm the app is ready and routing works:

```bash
curl -I -H "Host: application.keda" http://$INGRESS_IP
```

You should see similar output:
```
HTTP/1.1 200 OK
Date: Thu, 11 Sep 2025 14:11:24 GMT
Content-Type: text/html
Content-Length: 301
Connection: keep-alive
```

## Step 2 — Enable autoscaling with Kedify

The application is currectly running, Now we will enable autoscaling on this app, we will scale from 0 to 10 replicas. No request shall be lost at any moment. To do that, please run the following command to deploy our `ScaledObject`:

```bash
cat <<'EOF' | kubectl apply -f -
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: application
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: application
  cooldownPeriod: 5
  minReplicaCount: 0
  maxReplicaCount: 10
  fallback:
    failureThreshold: 2
    replicas: 1
  advanced:
    restoreToOriginalReplicaCount: true
    horizontalPodAutoscalerConfig:
      behavior:
        scaleDown:
          stabilizationWindowSeconds: 5
  triggers:
    - type: kedify-http
      metadata:
        hosts: application.keda
        pathPrefixes: /
        service: application-service
        port: "8080"
        scalingMetric: requestRate
        targetValue: "10"
        granularity: 1s
        window: 10s
        trafficAutowire: ingress
EOF
```

What the key fields do:
- `type: kedify-http` — Use Kedify’s HTTP scaler.
- `hosts`, `pathPrefixes` — Which requests to observe for scaling.
- `service`, `port` — The Service and port receiving traffic.
- `scalingMetric: requestRate` and `targetValue: 10` — Target 1000 req/s (per granularity/window) before scaling out.
- `minReplicaCount: 0` — Allows scale-to-zero when idle.
- `trafficAutowire: ingress` — Lets Kedify auto-wire your Ingress to the kedify-proxy.

After applying, the ScaledObject will appear in the Kedify dashboard (https://dashboard.kedify.io/).

![Kedify Dashboard With ScaledObject](images/scaledobject.png)

## Step 3 — Send traffic and observe scaling

Becuase we are not sending any traffic to our application, after some time, it should be scaled to zero.

#### Verify scale to zero

Run this command and wait until there is 0 replicas:

```bash
watch kubectl get deployment application -n default
```

You should see similar output:
```bash
Every 2,0s: kubectl get deployment application -n default

NAME          READY   UP-TO-DATE   AVAILABLE   AGE
application   0/0     0            0           110s
```

#### Verify the app can scale from zero

Now, hit the app again, it should be scaled to 1 replica and return back correct response:
```bash
curl -I -H "Host: application.keda" http://$INGRESS_IP
```

You should see a 200 OK response. Next, generate sustained load. You can use `hey` (or a similar tool):

#### Test higher load

```bash
hey -n 40000 -c 200 -host "application.keda" http://$INGRESS_IP
```

While the load runs, watch replicas change:

```bash
watch kubectl get deployment application -n default
```

For example something like this:

```
Every 2,0s: kubectl get deployment application -n default

NAME          READY   UP-TO-DATE   AVAILABLE   AGE
application   5/5     5            5           23m
```

Expected behavior:
- On bursty load, Kedify scales the Deployment up toward `maxReplicaCount`.
- When traffic subsides, replicas scale down. After the cooldown, they can return to zero.

You can also observe traffic and scaling in the Kedify dashboard:

![Kedify Dashboard ScaledObject Detail](images/load.png)

## Clean up

```bash
kubectl delete scaledobject application
kubectl delete ingress application-ingress
kubectl delete service application-service
kubectl delete deployment application
```

## Next steps

Explore the official Kedify [How-to guides](https://docs.kedify.io/how-to/) for more configurations such as Gateway API, Istio VirtualService, or OpenShift Routes.

### See also

- Kedify documentation: https://docs.kedify.io
