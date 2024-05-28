---
# User change
title: "Create a distributed deployment"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

You can setup Clair as a distributed deployment.

## Before you begin


You will need an [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or any Arm server running Linux.

The instructions are tested on Ubuntu. Other Linux distributions are possible with some modifications.

Install [Docker](/install-guides/docker/docker-engine/) and [Go](/install-guides/go/) (latest versions preferred).

{{% notice Note %}}
If you completed the combined deployment in the previous section, you have Docker and Go installed already.
{{% /notice %}}


## Install and run Clair (distributed)

In distributed deployment, each Clair component (indexer, matcher and notifier) runs in a separate OS process. 

Unlike the combined deployment, all three components run inside containers. 
There is no need to expose postgres port 5432, as all three services of clair are on same container network with postgres.

{{% notice Note %}}
If you completed the combined deployment in the previous section, you can delete the Clair directory and start again for the distributed deployment.
{{% /notice %}}

1. Download Clair:

```console
wget https://github.com/quay/clair/releases/download/v4.5.1/clair-v4.5.1.tar.gz
tar -xvf clair-v4.5.1.tar.gz
cd clair-v4.5.1
```

2. Start the postgres service:

Use `docker compose` to start the database service:

```console
sudo docker compose up -d clair-database
```

3. Start the load balancer 

You need a load balancer to direct traffic to the correct service.

You can use Traefik running on port 6060: 

```console
sudo docker compose up -d traefik
```

4. Start the Clair components

The `docker-compose.yaml` file already includes the needed services so there is nothing to change. 

Run the indexer, matcher and notifier as three separate processes: 

```console
sudo docker compose up -d indexer matcher notifier
```

5. Confirm everything is running

You can verify all five containers are running with Docker: 

```console
docker ps
```

The output will be similar to:

```output
CONTAINER ID   IMAGE                             COMMAND                  CREATED              STATUS                        PORTS                                                                                                                                                                                    NAMES
cdbf4f727877   quay.io/projectquay/golang:1.17   "go run . -conf /etc…"   51 seconds ago       Up 47 seconds                                                                                                                                                                                                          clair-notifier
a8a21d27fa67   traefik:v2.2                      "/entrypoint.sh trae…"   58 seconds ago       Up 55 seconds                 0.0.0.0:6060->6060/tcp, :::6060->6060/tcp, 80/tcp, 0.0.0.0:8080->8080/tcp, :::8080->8080/tcp, 0.0.0.0:32769->5432/tcp, :::32769->5432/tcp, 0.0.0.0:32768->8443/tcp, :::32768->8443/tcp   clair-traefik
24b066458f3d   quay.io/projectquay/golang:1.17   "go run . -conf /etc…"   About a minute ago   Up 55 seconds                                                                                                                                                                                                          clair-matcher
faa1c5754262   quay.io/projectquay/golang:1.17   "go run . -conf /etc…"   About a minute ago   Up 56 seconds                                                                                                                                                                                                          clair-indexer
890d6f3a64e5   postgres:12                       "docker-entrypoint.s…"   About a minute ago   Up About a minute (healthy)   5432/tcp                                                                                                                                                                                 clair-database
```

You can check the logs from each service:

Indexer:

```console
sudo docker logs clair-indexer
```

Matcher:

```console
sudo docker logs clair-matcher
```

Notifier:

```console
sudo docker logs clair-notifier
```


The logs confirm each service is running.

You can now open a new terminal and submit the manifest to generate the vulnerability report.
