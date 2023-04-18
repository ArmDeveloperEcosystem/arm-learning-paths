---
# User change
title: "Create a combined deployment"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

You can setup Clair as a combined deployment.

## Before you begin

You will need an [Arm based instance](/learning-paths/server-and-cloud/csp/) from a cloud service provider or any Arm server running Linux.

The instructions are tested on Ubuntu. Other Linux distributions are possible with some modifications.

Install [Docker](/install-guides/docker/docker-engine/) and [Go](/install-guides/go/) (latest versions preferred).


## Install and run Clair (combined)

In combined deployment, all Clair services run in a single OS process. This is the easiest deployment model to configure.

1. Download Clair:

```console
wget https://github.com/quay/clair/releases/download/v4.5.1/clair-v4.5.1.tar.gz
tar -xvf clair-v4.5.1.tar.gz
cd clair-v4.5.1
```

2. Edit `docker-compose.yaml` to setup the database

You need a postgres database for Clair to store all vulnerabilities specific to containers. 

Because postgres runs inside a private container network and Clair runs on `localhost`, you need to expose postgres port 5432 to `localhost`. 

Use a text editor to open `docker-compose.yaml` and search for the `clair-database` section.

Add the 2 lines to the `clair-database` section of the compose file:

```console
    ports:
      - "5432:5432"
```

The `clair-database` section should look like this:

```output
  clair-database:
    ports:
      - "5432:5432"
    container_name: clair-database
```

3. Start the postgres service:

Use `docker compose` to start the database service:

```console
sudo docker compose up -d clair-database
```

You can view the running postgres service with Docker:

```console
docker ps
```

The output will be similar to:

```output
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                    PORTS                                       NAMES
f4f1cba58e9e   postgres:12   "docker-entrypoint.s…"   29 seconds ago   Up 20 seconds (healthy)   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   clair-database
```

4. Modify the `config.yaml` file

Clair uses a configuration file to configure the indexer, matcher and notifier. 

In combined mode, you need to configure the indexer, matcher and notifier to communicate with postgres exposed on port 5432 of `localhost`. 

Use a text editor to open and modify the configuration file at `clair/local-dev/clair/config.yaml` 

Find the value of `connstring` 3 times in the file. There is a `connstring` for the indexer, matcher and notifier.

In each case, replace the `connstring` with the new value:

Indexer:

```console
indexer:
  connstring: host=localhost port=5432 user=clair dbname=indexer sslmode=disable
```

Matcher:

```console
matcher:
  connstring: host=localhost port=5432 user=clair dbname=matcher sslmode=disable
```

Notifier:

```console
notifier:
  connstring: host=localhost port=5432 user=clair dbname=notifier sslmode=disable
```

5. Build Clair

Generate the Clair binary with go: 

```console
go build ./cmd/clair
```

This will create a `clair` binary in the top directory.

6. Run Clair

Run the Clair combined deployment:

```console
./clair -conf "./local-dev/clair/config.yaml" -mode "combo"
```

The log in the terminal confirms that Clair is running successfully as a combined deployment. 

You can now open a new terminal and submit the manifest to generate the vulnerability report.
