---
title: Deploy Ollama amd64 to the cluster
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you'll bootstrap the cluster with Ollama on amd64, to simulate an "existing" K8s cluster running Ollama. In the next section you will add arm64 nodes alongside the amd64 nodes so you can compare them. 

### Deployment and service

1. Use a text editor to copy the following YAML and save it to a file called `namespace.yaml`:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: ollama
```

When the above is applied, a new K8s namespace named `ollama` is created.  This is where all the K8s objects will live.

2. Use a text editor to copy the following YAML and save it to a file called `amd64_ollama.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ollama-amd64-deployment
  labels:
    app: ollama-multiarch
  namespace: ollama
spec:
  replicas: 1
  selector:
    matchLabels:
      arch: amd64
  template:
    metadata:
      labels:
        app: ollama-multiarch
        arch: amd64
    spec:
      nodeSelector:
        kubernetes.io/arch: amd64
      containers:
      - image: ollama/ollama:0.6.1
        name: ollama-multiarch
        ports:
        - containerPort: 11434
          name: http
          protocol: TCP
        volumeMounts:
        - mountPath: /root/.ollama
          name: ollama-data
      volumes:
      - emptyDir: {}
        name: ollama-data
---
apiVersion: v1
kind: Service
metadata:
  name: ollama-amd64-svc
  namespace: ollama
spec:
  sessionAffinity: None
  ports:
  - nodePort: 30668
    port: 80
    protocol: TCP
    targetPort: 11434
  selector:
    arch: amd64
  type: LoadBalancer
```

When the above is applied:

* A new Deployment called `ollama-amd64-deployment` is created.  This deployment pulls a multi-architecture [Ollama image](https://hub.docker.com/layers/ollama/ollama/0.6.1/images/sha256-28b909914d4e77c96b1c57dea199c60ec12c5050d08ed764d9c234ba2944be63) from DockerHub. 

Of particular interest is the `nodeSelector` `kubernetes.io/arch`, with the value of `amd64`.  This ensures that the deployment only runs on amd64 nodes, utilizing the amd64 version of the Ollama container image. 

* A new load balancer Service `ollama-amd64-svc` is created, which targets all pods with the `arch: amd64` label (the amd64 deployment creates these pods).

A `sessionAffinity` tag is added to this Service to remove sticky connections to the target pods. This removes persistent connections to the same pod on each request.

### Apply the amd64 deployment and service

1. Run the following commands to apply the namespace, deployment, and service definitions:

```bash
kubectl apply -f namespace.yaml
kubectl apply -f amd64_ollama.yaml
```

You see the following responses:

```output
namespace/ollama created
deployment.apps/ollama-amd64-deployment created
service/ollama-amd64-svc created
```

2. Optionally, set the `default Namespace` to `ollama` so you don't need to specify the namespace each time, by entering the following:

```bash
config set-context --current --namespace=ollama
```

3. Get the status of the pods and the services by running the following:

```bash
kubectl get nodes,pods,svc -nollama 
```

Your output is similar to the following, showing one node, one pod, and one service:

```output
NAME                                              STATUS   ROLES    AGE   VERSION
node/gke-ollama-on-arm-amd64-pool-62c0835c-93ht   Ready    <none>   77m   v1.31.6-gke.1020000

NAME                                          READY   STATUS    RESTARTS   AGE
pod/ollama-amd64-deployment-cbfc4b865-msftf   1/1     Running   0          16m

NAME                       TYPE           CLUSTER-IP      EXTERNAL-IP    PORT(S)        AGE
service/ollama-amd64-svc   LoadBalancer   1.2.2.3         1.2.3.4        80:30668/TCP   16m
```

When the pods show `Running` and the service shows a valid `External IP`, you are ready to test the Ollama amd64 service!

### Test the Ollama web service on amd64

{{% notice Note %}}
The following utility `modelUtil.sh` is provided for convenience. 

It's a wrapper for kubectl, utilizing the utilities [curl](https://curl.se/), [jq](https://jqlang.org/), [bc](https://www.gnu.org/software/bc/), and [stdbuf](https://www.gnu.org/software/coreutils/manual/html_node/stdbuf-invocation.html).  

Make sure you have these shell utilities installed before running.
{{% /notice %}}

4. Use a text editor to copy the following shell script and save it to a file called `model_util.sh`:

```bash
#!/bin/bash

echo

# https://ollama-operator.ayaka.io/pages/en/guide/supported-models
model_name="llama3.2"
#model_name="mistral"
#model_name="dolphin-phi"

#prompt="Name the two closest stars to earth"
prompt="Create a sentence that makes sense in the English language, with as many palindromes in it as possible"

echo "Server response:"

get_service_ip() {
    arch=$1
    svc_name="ollama-${arch}-svc"
    kubectl -nollama get svc $svc_name -o jsonpath="{.status.loadBalancer.ingress[*]['ip', 'hostname']}"
}

infer_request() {
    svc_ip=$1
    temp=$(mktemp)
    stdbuf -oL curl -s $temp http://$svc_ip/api/generate -d '{
        "model": "'"$model_name"'",
        "prompt": "'"$prompt"'"
    }' | tee $temp

    duration=$(grep eval_count $temp | jq -r '.eval_duration')
    count=$(grep eval_count $temp | jq -r '.eval_count')

    if [[ -n "$duration" && -n "$count" ]]; then
        quotient=$(echo "scale=2;1000000000*$count/$duration" | bc)
        echo "Tokens per second:  $quotient"
    else
        echo "Error: eval_count or eval_duration not found in response."
    fi

    rm $temp
}

pull_model() {
    svc_ip=$1
    curl http://$svc_ip/api/pull -d '{
        "model": "'"$model_name"'"
    }'
}

hello_request() {
    svc_ip=$1
    curl http://$svc_ip/
}

run_action() {
    arch=$1
    action=$2

    svc_ip=$(get_service_ip $arch)
    echo "Using service endpoint $svc_ip for $action on $arch"

    case $action in
        infer)
            infer_request $svc_ip
            ;;
        pull)
            pull_model $svc_ip
            ;;
        hello)
            hello_request $svc_ip
            ;;
        *)
            echo "Invalid second argument. Use 'infer', 'pull', or 'hello'."
            exit 1
            ;;
    esac
}

case $1 in
    arm64|amd64|multiarch)
        run_action $1 $2
        ;;
    *)
        echo "Invalid first argument. Use 'arm64', 'amd64', or 'multiarch'."
        exit 1
        ;;
esac

echo -e "\n\nPod log output:"
echo;kubectl logs --timestamps  -l app=ollama-multiarch -nollama --prefix  | sort -k2 | cut -d " " -f 1,2 | tail -1
echo
```

5. Make the script executable with the following command:

```bash
chmod 755 model_util.sh
```

The script conveniently bundles many test and logging commands into a single place, making it easy to test, troubleshoot, and view services.

6. Run the following to make an HTTP request to the amd64 Ollama service on port 80:

```commandline
./model_util.sh amd64 hello
```

You get back the HTTP response, as well as the logline from the pod that served it:

```output
Server response:
Using service endpoint 34.55.25.101 for hello on amd64
Ollama is running

Pod log output:

[pod/ollama-amd64-deployment-cbfc4b865-msftf/ollama-multiarch] 2025-03-25T21:13:49.022522588Z
```

If you see the output `Ollama is running` you have successfully bootstrapped your GKE cluster with an amd64 node, running a deployment with the Ollama multi-architecture container instance!

Continue to the next section to do the same thing, but with an Arm node. 
