---
title: Deploy nginx Intel to the cluster
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deployment and service

In this section, you'll bootstrap the cluster with nginx on Intel, simulating an existing Kubernetes (K8s) cluster running nginx. In the next section, you'll add arm64 nodes alongside the Intel nodes for performance comparison. 

1. Use a text editor to copy the following YAML and save it to a file called `namespace.yaml`:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: nginx
```

Applying this YAML creates a new namespace called `nginx`, which contains all subsequent K8s objects.

2. Use a text editor to copy the following YAML and save it to a file called `intel_nginx.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-intel-deployment
  labels:
    app: nginx-multiarch
  namespace: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      arch: intel
  template:
    metadata:
      labels:
        app: nginx-multiarch
        arch: intel
    spec:
      nodeSelector:
        agentpool: intel
      containers:
      - image: nginx:latest
        name: nginx-multiarch
        ports:
        - containerPort: 80
          name: http
          protocol: TCP
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-intel-svc
  namespace: nginx
spec:
  sessionAffinity: None
  ports:
  - nodePort: 30080
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    arch: intel
  type: LoadBalancer
```

When the above is applied:

* A new deployment called `nginx-intel-deployment` is created. This deployment pulls a multi-architecture [nginx image](https://hub.docker.com/_/nginx) from DockerHub. 

Of particular interest is the `nodeSelector` `agentpool`, with the value of `intel`. This ensures that the deployment only runs on Intel nodes, utilizing the amd64 version of the nginx container image. 

* A new load balancer service `nginx-intel-svc` is created, targeting all pods with the `arch: intel` label (the Intel deployment creates these pods).

A `sessionAffinity` tag is added to this service to remove sticky connections to the target pods. This removes persistent connections to the same pod on each request.

### Apply the Intel deployment and service

1. Run the following commands to apply the namespace, deployment, and service definitions:

```bash
kubectl apply -f namespace.yaml
kubectl apply -f intel_nginx.yaml
```

You see the following responses:

```output
namespace/nginx created
deployment.apps/nginx-intel-deployment created
service/nginx-intel-svc created
```

2. Optionally, set the `default Namespace` to `nginx` to simplify future commands:

```bash
kubectl config set-context --current --namespace=nginx
```

3. Get the status of nodes, pods and services by running:

```bash
kubectl get nodes,pods,svc -nnginx 
```

Your output should be similar to the following, showing three nodes, one pod, and one service:

```output
NAME                                STATUS   ROLES    AGE   VERSION
node/aks-amd-10099357-vmss000000    Ready    <none>   10m   v1.32.7
node/aks-arm-49028967-vmss000000    Ready    <none>   12m   v1.32.7
node/aks-intel-34846084-vmss000000  Ready    <none>   15m   v1.32.7

NAME                                        READY   STATUS    RESTARTS   AGE
pod/nginx-intel-deployment-7d4c8f9b-xyz12  1/1     Running   0          2m

NAME                      TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)        AGE
service/nginx-intel-svc   LoadBalancer   10.0.45.123   20.1.2.3        80:30080/TCP   2m
```

When the pods show `Running` and the service shows a valid `External IP`, you're ready to test the nginx Intel service.

### Test the nginx web service on Intel

{{% notice Note %}}
The following utility `nginx_util.sh` is provided for convenience. 

It's a wrapper for kubectl, utilizing [curl](https://curl.se/).  

Make sure you have curl installed before running.
{{% /notice %}}

4. Use a text editor to copy the following shell script and save it to a file called `nginx_util.sh`:

```bash
#!/bin/bash

get_service_ip() {
    arch=$1
    svc_name="nginx-${arch}-svc"
    kubectl -nnginx get svc $svc_name -o jsonpath="{.status.loadBalancer.ingress[*]['ip', 'hostname']}"
}

get_request() {
    svc_ip=$1
    curl -s http://$svc_ip/ | grep "<title>Welcome to nginx!</title>"
}

apply_nginx_config() {
    NAMESPACE="nginx"
    
    echo "Applying custom nginx.conf to all nginx pods..."
    
    # Create the custom nginx.conf content
    kubectl create configmap nginx-config --from-literal=nginx.conf='
user  nginx;

error_log  /var/log/nginx/error.log notice;
pid        /run/nginx.pid;

worker_processes auto;
events {
    worker_connections  1024;
}

http {

    server {
        listen 80;

        location / {
            root /usr/share/nginx/html;
        }
    }
        # cache informations about FDs, frequently accessed files
    # can boost performance, but you need to test those values
    open_file_cache max=200000 inactive=20s;
    open_file_cache_valid 30s;
    open_file_cache_min_uses 2;
    open_file_cache_errors on;

    # to boost I/O on HDD we can disable access logs
    access_log off;

    # copies data between one FD and other from within the kernel
    # faster than read() + write()
    sendfile on;

    # send headers in one piece, it is better than sending them one by one
    tcp_nopush on;

    # don'\''t buffer data sent, good for small data bursts in real time
    tcp_nodelay on;
    

    # allow the server to close connection on non responding client, this will free up memory
    reset_timedout_connection on;

    # request timed out -- default 60
    client_body_timeout 10;

    # if client stop responding, free up memory -- default 60
    send_timeout 2;

    # server will close connection after this time -- default 75
    keepalive_timeout 30;

    # number of requests client can make over keep-alive -- for testing environment
    keepalive_requests 100000;
}
' -n $NAMESPACE --dry-run=client -o yaml | kubectl apply -f -

    # Get all nginx deployments and update them
    for deployment in $(kubectl get deployments -n $NAMESPACE -o name | grep nginx); do
        deployment_name=$(echo $deployment | cut -d'/' -f2)
        echo "Updating $deployment_name..."
        
        # Add volume and volume mount to deployment
        kubectl patch deployment $deployment_name -n $NAMESPACE --type='json' -p='[
            {
                "op": "add",
                "path": "/spec/template/spec/volumes",
                "value": [{"name": "nginx-config", "configMap": {"name": "nginx-config"}}]
            },
            {
                "op": "add", 
                "path": "/spec/template/spec/containers/0/volumeMounts",
                "value": [{"name": "nginx-config", "mountPath": "/etc/nginx/nginx.conf", "subPath": "nginx.conf"}]
            }
        ]'
    done

    echo "Waiting for pods to restart with new configuration..."
    sleep 15

    # Install btop on all nginx pods
    echo "Installing btop on all nginx pods..."
    for pod in $(kubectl get pods -l app=nginx-multiarch -n $NAMESPACE -o name | sed 's/pod\///'); do
        echo "Installing btop on $pod..."
        kubectl exec -n $NAMESPACE $pod -- apt-get update -y >/dev/null 2>&1
        kubectl exec -n $NAMESPACE $pod -- apt-get install -y btop >/dev/null 2>&1
        echo "✓ btop installed on $pod"
    done

    echo "✅ Custom nginx.conf applied and btop installed on all pods!"
}

run_action() {
    action=$1
    arch=$2

    svc_ip=$(get_service_ip $arch)
    echo "Using service endpoint $svc_ip for $action on $(tput bold)$arch service$(tput sgr0)"

    case $action in
        get)
            # Make the request
            response=$(get_request $svc_ip)
            echo "Response: $response"
            
            # Since access logs are disabled, determine serving pod via service endpoints
            if [ "$arch" = "multiarch" ]; then
                # For multiarch, show all possible pods
                serving_info="Any of: $(kubectl get pods -l app=nginx-multiarch -nnginx -o name | sed 's/pod\///' | tr '\n' ' ')"
            else
                # For specific arch, show the pod for that architecture
                serving_pod=$(kubectl get pods -l arch=$arch -nnginx -o name | sed 's/pod\///')
                if [ -n "$serving_pod" ]; then
                    bold_pod=$(echo "$serving_pod" | sed "s/nginx-\([^-]*\)-deployment/nginx-$(tput bold)\1$(tput sgr0)-deployment/")
                    serving_info="$bold_pod"
                else
                    serving_info="Unable to determine"
                fi
            fi
            echo "Served by: $serving_info"
            ;;
        *)
            echo "Invalid first argument. Use 'get'."
            exit 1
            ;;
    esac
}

case $1 in
    get)
        case $2 in
            intel|arm|amd|multiarch)
                run_action $1 $2
                ;;
            *)
                echo "Invalid second argument. Use 'intel', 'arm', 'amd', or 'multiarch'."
                exit 1
                ;;
        esac
        ;;
    put)
        case $2 in
            config)
                apply_nginx_config
                ;;
            *)
                echo "Invalid second argument. Use 'config'."
                exit 1
                ;;
        esac
        ;;
    login)
        case $2 in
            intel|arm|amd)
                # Get the pod for the specified architecture
                pod_name=$(kubectl get pods -l arch=$2 -nnginx -o name | sed 's/pod\///')
                if [ -n "$pod_name" ]; then
                    echo "Connecting to $(tput bold)$2$(tput sgr0) pod: $pod_name"
                    kubectl exec -it -nnginx $pod_name -- /bin/bash
                else
                    echo "No $2 pod found"
                    exit 1
                fi
                ;;
            *)
                echo "Invalid second argument. Use 'intel', 'arm', or 'amd'."
                exit 1
                ;;
        esac
        ;;
    *)
        echo "Invalid first argument. Use 'get', 'put', or 'login'."
        exit 1
        ;;
esac

echo
```

{{% notice Note %}}
This script supports all architectures (intel, arm, amd, multiarch) and will be used throughout the tutorial. You only need to create it once.
{{% /notice %}}

5. Make the script executable with the following command:

```bash
chmod 755 nginx_util.sh
```

The script conveniently bundles test and logging commands into a single place, making it easy to test, troubleshoot, and view services.

6. Run the following to make an HTTP request to the Intel nginx service on port 80:

```bash
./nginx_util.sh get intel
```

You get back the HTTP response, as well as the log line from the pod that served it:

```output
Using service endpoint 48.223.233.136 for get on **intel service**
Response: <title>Welcome to nginx!</title>
Served by: nginx-**intel**-deployment-dc84dc59f-7qb72
```

If you see the output `Welcome to nginx!` you have successfully bootstrapped your AKS cluster with an Intel node, running a deployment with the nginx multi-architecture container instance.
