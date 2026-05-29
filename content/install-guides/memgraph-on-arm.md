---
additional_search_terms:
- graph database
- database
- cypher
- graph analytics
- graph algorithms
- docker
- arm64
- aarch64

layout: installtoolsall
minutes_to_complete: 20
multi_install: false
multitool_install_part: false
official_docs: https://memgraph.com/docs/getting-started/install-memgraph
title: Memgraph on Arm
tool_install: true
weight: 1
author: Sabika Tasneem
---

[Memgraph](https://memgraph.com/) is an open-source, in-memory graph database built for real-time streaming and analytical workloads. It's compatible with the [Cypher](https://memgraph.com/docs/querying) query language and the Bolt protocol used by Neo4j drivers, so existing Cypher/Bolt applications can connect without changes.

Memgraph publishes native `aarch64` Linux packages and multi-architecture Docker images, so it runs unmodified on Arm-based hardware.

Graph algorithms parallelize well and scale with core count. Arm server instances can offer a lower cost per query than equivalent x86 instances for memory-intensive graph workloads.

In this install guide, you'll learn two installation paths:

- Docker: the quickest way to try Memgraph, and the portable option for macOS, Windows, and any Linux distribution.
- Native Linux packages: a good choice when Docker is unavailable or not preferred, or when you want to benchmark Memgraph directly on the host.

At the end of each path, you'll run a few Cypher queries with `mgconsole`, then optionally add [MAGE](https://memgraph.com/docs/advanced-algorithms), Memgraph’s graph-algorithm and query-module extension library.

## Before you begin

Confirm you are using an Arm computer with 64-bit Linux by running:

```bash { target="ubuntu:latest" }
uname -m
```

The output is similar to:

```output
aarch64
```

If you see a different result, you aren't using an Arm computer running 64-bit Linux.


## Install Memgraph with Docker

You can use Docker to run Memgraph on any operating system. The official images on [Docker Hub](https://hub.docker.com/u/memgraph) are multi-arch manifests, so `docker pull` automatically selects the `arm64` variant on Arm hosts.

If you've not already installed Docker, follow the steps in the [Docker install guide](/install-guides/docker/) to do so.

### Start the Memgraph container

{{% notice Note %}}
The following commands use Memgraph version 3.10.1. The same steps work with other versions. Replace the version number in image tags, package filenames, and download URLs with your chosen version. To find the latest release, see the [Memgraph GitHub releases page](https://github.com/memgraph/memgraph/releases).
{{% /notice %}}

The core image is `memgraph/memgraph`, which includes the Memgraph database plus the bundled `mgconsole` CLI. Start it with:

```bash { target="ubuntu:latest" }
docker run -p 7687:7687 -p 7444:7444 --name memgraph memgraph/memgraph:3.10.1
```

The container exposes two ports:

- `7687`: the Bolt port used by `mgconsole`, Memgraph Lab, and every Bolt-compatible driver.
- `7444`: streams Memgraph logs to Memgraph Lab for real-time monitoring.

To confirm that the Arm image was pulled, inspect it:

```bash { target="ubuntu:latest" }
docker inspect memgraph/memgraph:3.10.1 --format '{{.Architecture}}'
```

The output is similar to:

```output
arm64
```

### Choose a Docker image 

The following are Docker images that you can choose depending on the Memgraph features that you want to use:

| Image | Includes |
| --- | --- |
| `memgraph/memgraph` | Memgraph database + `mgconsole` CLI. |
| `memgraph/memgraph-mage` | Memgraph database + `mgconsole` + [MAGE](https://memgraph.com/docs/advanced-algorithms), a library of advanced graph algorithms and query modules. |
| `memgraph/mgconsole` | Standalone CLI client. |
| `memgraph/lab` | Memgraph Lab web UI. |

Start with `memgraph/memgraph` to get the Memgraph database. If you later want PageRank, community detection, node embeddings, NetworkX integration, or other advanced query modules, see the [MAGE section](#install-the-mage-graph-algorithm-library).

### Connect with mgconsole inside the container

The `memgraph/memgraph:3.10.1` image ships with `mgconsole` already inside the container:

```bash { target="ubuntu:latest" }
docker exec -it memgraph mgconsole
```

The output is similar to:

```output
mgconsole 1.5.2
Connected to 'memgraph://127.0.0.1:7687'
Type :help for shell usage
Quit the shell by typing Ctrl-D(eof) or :quit
memgraph>
```

To try querying with `mgconsole`, skip to the [example queries](#how-do-i-run-example-cypher-queries) section.

## Install Memgraph natively on Linux

Memgraph provides native `aarch64` packages for the following distributions:

- Ubuntu 24.04
- Debian 12 and Debian 13
- Fedora 42

Choose the package that matches your distribution from the [Memgraph Download Hub](https://memgraph.com/download). For convenience, you can find direct download URLs for every supported platform on the [direct download links](https://memgraph.com/docs/getting-started/install-memgraph/direct-download-links) page in the Memgraph documentation.

{{< tabpane-normal >}}
  {{< tab header="Ubuntu / Debian" >}}

Download the `arm64` `.deb` package for Ubuntu 24.04 on Arm:

```bash { target="ubuntu:latest" }
wget https://download.memgraph.com/memgraph/v3.10.1/ubuntu-24.04-aarch64/memgraph_3.10.1-1_arm64.deb
```

Before installing Memgraph, update the package index and install the required dependency:

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install -y libatomic1
```

Install the package:

```bash { target="ubuntu:latest" }
sudo dpkg -i memgraph_3.10.1-1_arm64.deb
```

If `dpkg` reports missing dependencies, resolve them with:

```bash { target="ubuntu:latest" }
sudo apt-get install -f
```

  {{< /tab >}}
  {{< tab header="Fedora" >}}

Download the Fedora `aarch64` `.rpm`:

```bash
wget https://download.memgraph.com/memgraph/v3.10.1/fedora-42-aarch64/memgraph-3.10.1_1-1.aarch64.rpm
```

Install the package:

```bash
sudo dnf install ./memgraph-3.10.1_1-1.aarch64.rpm
```

  {{< /tab >}}
{{< /tabpane-normal >}}

### Verify that Memgraph is running

The package installs a `systemd` service. Check the status of the service:

```bash { target="ubuntu:latest" }
sudo systemctl status memgraph
```

If it's not already running, start it and enable it on boot:

```bash { target="ubuntu:latest" }
sudo systemctl start memgraph
sudo systemctl enable memgraph
```

Inspect the startup log to confirm the version:

```bash { target="ubuntu:latest" }
sudo journalctl --unit memgraph --no-pager | head
```

The output is similar to:

```output
You are running Memgraph v3.10.1
```

The configuration file can be found at `/etc/memgraph/memgraph.conf`. You can fine-tune Memgraph by editing the configuration file. For a full configuration reference, see the [Memgraph configuration docs](https://memgraph.com/docs/database-management/configuration). 

After editing the configuration file, restart the service:

```bash
sudo systemctl restart memgraph
``` 


## Increase the memory map area limit

Memgraph allocates many small memory mappings. On larger graphs, you can hit the default Linux limit (`vm.max_map_count = 65530`). Hitting the limit usually surfaces as a hung transaction, `munmap` errors, or `bad_alloc` crashes. Memgraph recommends roughly one memory map area per 64 KB of system RAM. For more information, including a list of recommended map count values, see the [system configuration docs](https://memgraph.com/docs/database-management/system-configuration#increasing-memory-map-areas).

For an 8–32 GB host, `524288` is the recommended starting value. Set it for the current session:

```bash { target="ubuntu:latest" }
sudo sysctl -w vm.max_map_count=524288
```

To persist the change across reboots, add it to `/etc/sysctl.conf` or a drop-in under `/etc/sysctl.d/`, then reload:

```bash { target="ubuntu:latest" }
echo 'vm.max_map_count=524288' | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

Verify the new value:

```bash { target="ubuntu:latest" }
sysctl vm.max_map_count
```

This setting is applied on the Linux host, so it is relevant for both the native and Docker installs. Docker containers inherit the host's `vm.max_map_count`.

## (Optional) Install mgconsole separately

`mgconsole` is Memgraph’s command-line client for executing Cypher queries. It is already included in the Memgraph Linux packages, and in the `memgraph/memgraph:3.10.1` and `memgraph/memgraph-mage:3.10.1` Docker images. You need a separate install only if you want to run it from a different machine.

To install it standalone, download the binary for your platform from the [Memgraph Download Hub](https://memgraph.com/download#individual), or pull the Docker image.

If you've got Memgraph installed directly on the host machine, use host networking so the container can reach it on `localhost`:

```bash { target="ubuntu:latest" }
docker run -it --network host memgraph/mgconsole:latest --host localhost --port 7687
```

If Memgraph is running in another container or on a remote host, replace `localhost` with the appropriate hostname or IP address:

```bash { target="ubuntu:latest" }
docker run -it memgraph/mgconsole:latest --host <memgraph-host> --port 7687
```

For `mgconsole` documentation, including all command-line flags, see the [mgconsole CLI docs](https://memgraph.com/docs/getting-started/cli).

## Verify mgconsole installation by running example Cypher queries

With Memgraph running either in Docker or as a native service, you can send queries non-interactively through `mgconsole`.

{{% notice Note %}}
If you installed Memgraph with Docker, replace `mgconsole --host localhost --port 7687` with `sudo docker exec -i memgraph mgconsole` in piped commands, or run `docker exec -it memgraph mgconsole` for an interactive session.
{{% /notice %}}

Create two nodes and a relationship:

```bash { target="ubuntu:latest" }
echo "CREATE (a:Person {name: 'Alice'})-[:KNOWS]->(b:Person {name: 'Bob'});" \
  | mgconsole --host localhost --port 7687
```

Read them back:

```bash { target="ubuntu:latest" }
echo "MATCH (n) RETURN n;" | mgconsole --host localhost --port 7687
```

The output is similar to:

```output
+------------------------------+
| n                            |
+------------------------------+
| (:Person {name: 'Alice'})    |
| (:Person {name: 'Bob'})      |
+------------------------------+
```

Count the nodes:

```bash { target="ubuntu:latest" }
echo "MATCH (n) RETURN count(n) AS node_count;" \
  | mgconsole --host localhost --port 7687
```

The output is similar to:

```output
+------------+
| node_count |
+------------+
| 2          |
+------------+
```

Clear the graph:

```bash { target="ubuntu:latest" }
echo "MATCH (n) DETACH DELETE n;" | mgconsole --host localhost --port 7687
```

To confirm the graph is empty, re-run the count:

```bash { target="ubuntu:latest" }
echo "MATCH (n) RETURN count(n) AS node_count;" | mgconsole --host localhost --port 7687
```

The output is similar to:

```output
+------------+
| node_count |
+------------+
| 0          |
+------------+
```

If you prefer an interactive session, run `mgconsole` without piping input:

```bash { target="ubuntu:latest" }
mgconsole --host localhost --port 7687
```

### Pattern-matching example

Memgraph’s strength is pattern matching. Try a slightly richer graph:

```bash { target="ubuntu:latest" }
mgconsole --host localhost --port 7687 <<'EOF'
CREATE (alice:Person {name: 'Alice'})-[:KNOWS]->(bob:Person {name: 'Bob'}),
       (bob)-[:KNOWS]->(carol:Person {name: 'Carol'}),
       (alice)-[:KNOWS]->(dave:Person {name: 'Dave'});
MATCH (a:Person {name: 'Alice'})-[:KNOWS*1..2]->(friend)
RETURN DISTINCT friend.name AS friend_of_alice;
EOF
```

This query returns everyone reachable from Alice in one or two `KNOWS` hops.

## (Optional) Install the MAGE graph-algorithm library

[MAGE](https://memgraph.com/docs/advanced-algorithms) is an open-source library that extends Memgraph with advanced graph algorithms and query modules, such as PageRank, community detection, shortest paths, node embeddings, NetworkX integration, and more, all callable from Cypher. MAGE is a separate add-on. If you want these capabilities, install the MAGE variant described as follows.

### MAGE with Docker

Switch from the base image to `memgraph/memgraph-mage:3.10.1`, which bundles MAGE on top of the same database:

```bash { target="ubuntu:latest" }
docker stop memgraph && docker rm memgraph
docker run -p 7687:7687 -p 7444:7444 --name memgraph memgraph/memgraph-mage:3.10.1
```

Confirm that the MAGE algorithms are loaded:

```bash { target="ubuntu:latest" }
echo "CALL mg.procedures() YIELD name WITH name WHERE name STARTS WITH 'pagerank' RETURN name;" \
  | docker exec -i memgraph mgconsole
```

The output includes entries such as `pagerank.get`.

### MAGE with native Linux packages

Memgraph provides a prebuilt MAGE `arm64` `.deb` package for Ubuntu 24.04. It's installed on top of an existing Memgraph package install:

```bash { target="ubuntu:latest" }
wget https://download.memgraph.com/memgraph-mage/v3.10.1/ubuntu-24.04/memgraph-mage_3.10.1-1_arm64.deb
sudo dpkg -i memgraph-mage_3.10.1-1_arm64.deb
sudo systemctl restart memgraph
```

For other distributions, or to build MAGE from source with custom algorithms, see [Install MAGE graph algorithm library](https://memgraph.com/docs/advanced-algorithms/install-mage) in the Memgraph documentation.

### Verify installation by running a MAGE algorithm

With MAGE loaded, you can call any of its algorithms from Cypher. For example, compute PageRank on the small graph that you created earlier:

```bash { target="ubuntu:latest" }
echo "CALL pagerank.get() YIELD node, rank RETURN node, rank ORDER BY rank DESC;" \
  | mgconsole --host localhost --port 7687
```

For the complete algorithm catalog, see [Available algorithms](https://memgraph.com/docs/advanced-algorithms/available-algorithms) in the Memgraph documentation.

## Next steps

You are now ready to build and query graphs with Memgraph on Arm.

Next, you can explore the [Cypher query language](https://memgraph.com/docs/querying) and the [Memgraph data model](https://memgraph.com/docs/fundamentals). You can install the visual [Memgraph Lab](https://memgraph.com/docs/memgraph-lab) for browsing and visualizing graphs, and pick a [client library](https://memgraph.com/docs/client-libraries) for Python, Go, Rust, Java, JavaScript, or C#. You can also join the Memgraph community on [Discord](https://discord.gg/memgraph).


