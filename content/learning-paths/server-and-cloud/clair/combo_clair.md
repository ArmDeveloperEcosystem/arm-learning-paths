---
# User change
title: "Clair in the combined mode"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Prerequisites

* Cloud node or a physical machine.
* [docker](https://docs.docker.com/engine/install/ubuntu/) and [docker-compose](https://docs.docker.com/compose/install/linux/) (latest version preferred).
* [go](https://go.dev/doc/install) (latest version preferred).

## Install and run Clair in the Combined Mode

In combined deployment, all Clair services run in a single OS process. This is the easiest deployment model to configure as it involves limited resources.

NOTE: The below mentioned steps are tested successfully with Clair v4.5.1.

Download Clair v4.5.1:

```console
wget https://github.com/quay/clair/releases/download/v4.5.1/clair-v4.5.1.tar.gz
tar -xvf clair-v4.5.1.tar.gz
cd clair-v4.5.1
```

We will setup a postgres database for Clair to store all vulnerabilities specific to containers. The `docker-compose.yaml` already has a target "clair-database" to setup a postgres database for Clair. For combined mode, since postgres service will run inside a private container network and Clair service runs on localhost, we are required to expose postgres port 5432 to localhost. To do so, add the following to "clair-database" target in `docker-compose.yaml` file.

```console
ports:
      - "5432:5432"
```

Next, setup the postgres service as below:

```console
sudo docker-compose up -d clair-database
```

We can view the running postgres service with `docker ps`. Below is the output:

![postgres_pic](https://user-images.githubusercontent.com/87687089/213442653-79fd8b49-12ce-44e7-a82f-1cfd32665c5e.PNG)


Clair uses a configuration file to configure indexer, matcher and notifier. In combined mode, we will configure indexer, matcher and notifier to communicate to postgres service exposed to port 5432 on localhost. We will use the configuration file present at `clair/local-dev/clair/config.yaml`, and modify the `connstring` of indexer, matcher and notifier as below:

```console
indexer:
  connstring: host=localhost port=5432 user=clair dbname=indexer sslmode=disable

matcher:
  connstring: host=localhost port=5432 user=clair dbname=matcher sslmode=disable

notifier:
  connstring: host=localhost port=5432 user=clair dbname=notifier sslmode=disable
```

Next, generate the Clair binary with go, as below:

```console
sudo go build ./cmd/clair
```

This will generate a Clair binary in the root of the repo.

Now the postgres service is running and Clair's configuration is ready, run Clair in the combined mode as below:

```console
./clair -conf "./local-dev/clair/config.yaml" -mode "combo"
```

The running logs on your screen confirms that Clair is running successfully in the combined mode. You can now open a new terminal and submit the manifest to generate the vulnerability report.
