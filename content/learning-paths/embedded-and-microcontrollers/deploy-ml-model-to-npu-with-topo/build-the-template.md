---
title: Build the Topo Template from scratch
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you will build

In this section, you will build the `topo-imx93-npu-deployment` Template starting from two non-Topo, non-Compose projects:

- a Cortex-A web application that prepares images, writes model and tensor data into shared memory, and sends inference commands over `RPMsg`
- a Cortex-M33 ExecuTorch runner firmware project for the FRDM i.MX 93

You will combine those sources into one repository, then make the repository a normal Compose project, and only then add the Topo metadata and Remoteproc Runtime services.

## Create the repository from the base projects

We will copy the original base projects from the Topo Template. Clone the Topo Template Format repository for the validation schema, clone the original Topo Template for the source files, and start a new empty repository:

```bash
git clone https://github.com/arm/topo-template-format.git
git clone https://github.com/Arm-Examples/topo-imx93-npu-deployment.git
mkdir new-topo-npu-template
cd new-topo-npu-template
```

Create the project layout:

```bash
mkdir -p webapp executorch-runner licenses
```

Copy over the relevant `webapp` files:

```bash
cp -R ../topo-imx93-npu-deployment/webapp/src webapp
```

Copy the Cortex-M33 runner build inputs from the firmware project:

```bash
cp ../topo-imx93-npu-deployment/executorch-runner/build-runner.sh executorch-runner/build-runner.sh
cp ../topo-imx93-npu-deployment/executorch-runner/export_mv2_imx93.py executorch-runner/export_mv2_imx93.py
cp ../topo-imx93-npu-deployment/executorch-runner/docker-entrypoint.sh executorch-runner/docker-entrypoint.sh
cp -R ../topo-imx93-npu-deployment/executorch-runner/patches executorch-runner
```

Add the licenses and ignore rules used by the source projects:

```bash
cp ../topo-imx93-npu-deployment/LICENSE.md .
cp -R ../topo-imx93-npu-deployment/licenses .
cp ../topo-imx93-npu-deployment/.gitignore .
```

We have now obtained a typical starting point. We have two sets of source code, combined into one repository. It is not a Compose project and it is not a Topo Template. We will now create a Compose project and Topo Template around the source code.

The Compose project provides the container build and runtime structure. A Dockerfile describes how to build one image. A Compose file describes the services that use those images, their build contexts, ports, volumes, dependencies, and runtime settings. In this Template:

- `webapp/Dockerfile` builds the Flask image.
- `webapp/compose.yaml` keeps the web app's build context and Linux runtime settings close to the web app source.
- `executorch-runner/Dockerfile` builds the ExecuTorch `.pte` model and Cortex-M33 runner ELF through multi-stage Docker builds.
- the root `compose.yaml` is the Template entry point. It combines the web app, artifact build services, the Remoteproc Runtime service, and the root-level `x-topo` metadata.

For a general introduction to Compose projects, services, and the `compose.yaml` file, see Docker's [How Compose works](https://docs.docker.com/compose/intro/compose-application-model/) documentation.

When a step below says to create a file, paste the complete file contents shown. When a step says to add or update part of an existing Compose file, merge the YAML into the existing top-level key shown by the snippet. For example, if a snippet starts with `services:`, add the named service under the existing top-level `services:` map. Do not create a second `services:` block in the same file.

## Turn the sources into a Compose project

Before adding Topo metadata, make the project work as ordinary Compose. Start by containerizing the Cortex-A web application.

Create `webapp/Dockerfile` with the following complete contents:

```Dockerfile
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN python -m pip install --no-cache-dir flask==3.0.3

COPY src/data/imagenet_classes.txt /opt/mv2-imx93/imagenet_classes.txt
COPY src/app.py .
COPY src/templates/ templates/
COPY src/static/ static/

EXPOSE 3000

CMD ["python", "app.py"]
```

Create `webapp/compose.yaml` with the following complete contents:

```yaml
services:
  webapp:
    platform: linux/arm64
    build:
      context: .
      dockerfile: Dockerfile
    privileged: true
    ports:
      - "${WEBAPP_PORT:-3001}:3000"
    volumes:
      - /sys:/sys
      - /dev:/dev
    restart: unless-stopped
```

Create the root `compose.yaml` with the following complete contents:

```yaml
services:
  webapp:
    platform: linux/arm64
    extends:
      file: webapp/compose.yaml
      service: webapp
```

Check that Compose can read the project:

```bash
docker compose config
```

You should see output that includes the resolved `webapp` service:

```output
services:
  webapp:
    build:
      context: /path/to/new-topo-npu-template/webapp
      dockerfile: Dockerfile
    ports:
      - mode: ingress
        target: 3000
        published: "3001"
```

At this point, Compose can build and run the Cortex-A web application as a normal Linux container. The image runs `webapp/src/app.py`, packages the Jinja templates from `webapp/src/templates/`, the static assets from `webapp/src/static/`, and the ImageNet labels from `webapp/src/data/imagenet_classes.txt`. The container listens on port `3000`, and Compose publishes it on host port `3001` unless you set `WEBAPP_PORT` to another value.

## Add the ExecuTorch artifact pipeline

The web application needs an ExecuTorch `.pte` model, and the target needs a Cortex-M33 ELF image. Both artifacts are built by `executorch-runner/Dockerfile`.

Copy the Dockerfile into the runner build context:

```bash
cp ../topo-imx93-npu-deployment/executorch-runner/Dockerfile executorch-runner/
```

For this multi-stage Dockerfile:

- `build-base`: installs the common Ubuntu build tools.
- `executorch-base`: clones ExecuTorch, installs the Arm backend dependencies, and copies `export_mv2_imx93.py` and `docker-entrypoint.sh`.
- `pte-builder`: exports `mv2_ethosu65_256.pte`.
- `pte-artifacts`: packages the `.pte` file as a BuildKit artifact context.
- `runner-base`: installs the Arm GNU toolchain, MCUX SDK, RPMsg-Lite dependencies, runner sources, and local patches.
- `runner-builder`: builds `executorch_runner_cm33.elf`.
- `runner-artifacts`: packages the ELF for inspection or reuse.
- `runner-runtime`: produces a `scratch` image whose entrypoint is the ELF file.

The important artifact stages look like this:

```Dockerfile
FROM busybox:1.36 AS pte-artifacts
COPY --from=pte-builder /workspace/build/mv2-imx93/mv2_ethosu65_256.pte /artifacts/mv2_ethosu65_256.pte

FROM busybox:1.36 AS runner-artifacts
COPY --from=runner-builder /artifacts/executorch_runner_cm33.elf /artifacts/executorch_runner_cm33.elf

FROM scratch AS runner-runtime
COPY --from=runner-builder /artifacts/executorch_runner_cm33.elf /executorch_runner_cm33.elf
ENTRYPOINT ["/executorch_runner_cm33.elf"]
```

## Connect the artifact services

Add `pte-artifacts` and `runner-artifacts` as siblings of the existing `webapp` service in the root `compose.yaml`:

```yaml
services:
  pte-artifacts:
    platform: linux/arm64
    scale: 0
    build:
      context: executorch-runner
      dockerfile: Dockerfile
      target: pte-artifacts
      cache_from:
        - ${EXECUTORCH_BASE_CACHE_IMAGE:-ghcr.io/arm-examples/topo-imx93-npu-deployment/executorch-base:et-v1.2.0-ubuntu24.04}

  runner-artifacts:
    platform: linux/arm64
    scale: 0
    build:
      context: executorch-runner
      dockerfile: Dockerfile
      target: runner-artifacts
      cache_from:
        - ${IMX93_RUNNER_BUILD_CACHE_IMAGE:-ghcr.io/arm-examples/topo-imx93-npu-deployment/imx93-runner-build:mcux-v25.09.00-armgcc14.2-ubuntu24.04}
```

Do not replace the existing root `webapp` service with the snippet above. The root file should now have three service names under the same top-level `services:` map: `webapp`, `pte-artifacts`, and `runner-artifacts`.

These services are used only to build artifacts. They do not run as part of the deployed application. `scale: 0` tells Compose not to start containers for them, while still allowing other services to copy files from their build outputs.

Replace `webapp/compose.yaml` with the following version so the Flask image imports the `.pte` artifact:

```yaml
services:
  webapp:
    platform: linux/arm64
    build:
      context: .
      dockerfile: Dockerfile
      additional_contexts:
        pte_artifacts: service:pte-artifacts
    privileged: true
    ports:
      - "${WEBAPP_PORT:-3001}:3000"
    volumes:
      - /sys:/sys
      - /dev:/dev
    restart: unless-stopped
```

Then add the `.pte` copy line to `webapp/Dockerfile` with the other `COPY` commands:

```Dockerfile
COPY --from=pte_artifacts /artifacts/mv2_ethosu65_256.pte /opt/mv2-imx93/mv2_ethosu65_256.pte
```

The `/opt/mv2-imx93/` path is the location the Flask application expects for its MobileNetV2 support files. At run time, the app reads the `.pte` file from this path before copying it into reserved memory for the Cortex-M33 runner.

## Add the Remoteproc Runtime service

Add the Cortex-M33 runner as another sibling under the top-level `services:` map in the root `compose.yaml`:

```yaml
services:
  cm33-runner:
    platform: linux/arm64
    build:
      context: executorch-runner
      dockerfile: Dockerfile
      target: runner-runtime
      cache_from:
        - ${IMX93_RUNNER_BUILD_CACHE_IMAGE:-ghcr.io/arm-examples/topo-imx93-npu-deployment/imx93-runner-build:mcux-v25.09.00-armgcc14.2-ubuntu24.04}
    runtime: io.containerd.remoteproc.v1
    annotations:
      remoteproc.name: imx-rproc
```

Keep the existing `webapp`, `pte-artifacts`, and `runner-artifacts` services in the same file. This step adds one more service; it does not replace any of the previous services.

This is the heterogeneous deployment hook. Docker still builds an image, but the service is not started as a Linux userspace process. The runtime `io.containerd.remoteproc.v1` selects Remoteproc Runtime, and the `remoteproc.name` annotation tells the shim to use the i.MX remote processor driver.

Update the existing root `webapp` service so it depends on the CM33 runner and passes the cache image values into the build. Keep the existing `extends` block, then add `depends_on` and `build.args` as shown:

```yaml
services:
  webapp:
    platform: linux/arm64
    extends:
      file: webapp/compose.yaml
      service: webapp
    depends_on:
      - cm33-runner
    build:
      args:
        EXECUTORCH_BASE_CACHE_IMAGE: ghcr.io/arm-examples/topo-imx93-npu-deployment/executorch-base:et-v1.2.0-ubuntu24.04
        IMX93_RUNNER_BUILD_CACHE_IMAGE: ghcr.io/arm-examples/topo-imx93-npu-deployment/imx93-runner-build:mcux-v25.09.00-armgcc14.2-ubuntu24.04
```

The web app is privileged and mounts `/sys` and `/dev` because it checks the device tree, reads remoteproc state through `/sys/class/remoteproc`, talks to `/dev/ttyRPMSG*`, writes shared memory through `/dev/mem`, and checks for `/dev/ethosu0`.

Keep the web app build context in `webapp/compose.yaml`. The root `webapp.build.args` block above only supplies Topo-collected build arguments; it should not replace the extended build context and Dockerfile from `webapp/compose.yaml`.

## Add Topo metadata and arguments

After the Compose services are complete, add the root-level `x-topo` block.
Keep it at the root of `compose.yaml`, as a sibling of `services`, not under `services`.

If you want to use an agent skill to perform this step, skip to the optional step below.

```yaml
x-topo:
  name: "i.MX93 ExecuTorch runner"
  description: "Runs a Cortex-A web application that sends image inference commands to a resident CM33 ExecuTorch runner over RPMsg."
  features:
    - "remoteproc-runtime"
  args:
    EXECUTORCH_BASE_CACHE_IMAGE:
      description: Optional GHCR image used as a BuildKit cache source for the ExecuTorch PTE build.
      required: false
      default: ghcr.io/arm-examples/topo-imx93-npu-deployment/executorch-base:et-v1.2.0-ubuntu24.04
    IMX93_RUNNER_BUILD_CACHE_IMAGE:
      description: Optional GHCR image used as a BuildKit cache source for the CM33 runner build.
      required: false
      default: ghcr.io/arm-examples/topo-imx93-npu-deployment/imx93-runner-build:mcux-v25.09.00-armgcc14.2-ubuntu24.04
```

The `features` value tells Topo that this Template requires `remoteproc-runtime` support on the target. This is useful when checking for project compatibility with the `topo templates --target <target>` command.

The `args` entries describe configurable build inputs. Compose consumes those values through the `cache_from` interpolation you added earlier:

```output
cache_from:
  - ${EXECUTORCH_BASE_CACHE_IMAGE:-ghcr.io/arm-examples/topo-imx93-npu-deployment/executorch-base:et-v1.2.0-ubuntu24.04}
```

The root `webapp.build.args` block also makes the Topo-provided values visible in the Compose build model while preserving the `webapp/` build context inherited through `extends`.

Keep runtime settings such as `WEBAPP_PORT` as normal Compose interpolation unless you intentionally want Topo to collect them as Template setup arguments.

## (Optional) Use an Agent Skill to add the Topo metadata

The [Topo Template Format](https://github.com/arm/topo-template-format) repository includes public authoring skills for agents that support skill installation:

- `topo-template-context`: provides Topo and Topo Template reference context for `x-topo` metadata, schema, docs, and CLI Template behavior.
- `topo-template-bootstrap`: converts a Compose repository into a Topo Template by adding or improving `compose.yaml` and `x-topo` metadata.
- `topo-template-lint`: reviews a Topo Template for schema correctness, metadata consistency, deployment success messages, and build argument wiring.

Install the skills with `npx skills`:

```bash
npx skills add arm/topo-template-format
```

If your agent does not use `npx skills`, manually copy or symlink the directories under `../topo-template-format/skills/` into your agent's skills directory.

Restart your agent after installing or updating the skills.

From the root of the Compose project, ask your agent to use `topo-template-bootstrap`:

```
Use topo-template-bootstrap on this repository.
Treat the root compose.yaml as the Template root.
Preserve plain docker compose behavior.
Add x-topo metadata only where it reflects the actual services, hardware requirements, and build arguments.
```

After bootstrap, ask the agent to use `topo-template-lint`:

```
Use topo-template-lint on this repository.
Validate compose.yaml against the Topo Template Format schema.
Check README alignment, Remoteproc Runtime metadata, and x-topo.args wiring.
```

## Validate the final Template

Check the Compose model and check that the Topo metadata is present:

```bash
docker compose config
```

In the `docker compose config` output, check that the resolved `webapp` service has:

- `build.context` ending in `/webapp`
- `build.dockerfile` set to `Dockerfile`
- `build.additional_contexts.pte_artifacts` set to `service:pte-artifacts`

Install `check-jsonschema` if it is not already available:

{{< tabpane code=true >}}
  {{< tab header="macOS" language="shell" >}}
brew install check-jsonschema
  {{< /tab >}}
  {{< tab header="Linux / WSL" language="shell" >}}
sudo apt update
sudo apt install -y pipx
pipx ensurepath
pipx install check-jsonschema
export PATH="$HOME/.local/bin:$PATH"
  {{< /tab >}}
{{< /tabpane >}}

Validate the root Compose file with the schema in the Topo Template Format:

```bash
check-jsonschema \
  --schemafile ../topo-template-format/schema/topo-template-format.json \
  compose.yaml
```

Review these points:

- `compose.yaml` contains root-level `x-topo` metadata.
- `x-topo.features` includes `remoteproc-runtime`.
- non-remoteproc services set `platform: linux/arm64`.
- `pte-artifacts` and `runner-artifacts` use `scale: 0`.
- `cm33-runner` uses `runtime: io.containerd.remoteproc.v1`.
- `cm33-runner` has `remoteproc.name: imx-rproc`.
- `webapp` depends on `cm33-runner`.
- `webapp` imports the `.pte` file through `additional_contexts`.
- every `x-topo.args` entry is consumed by Compose interpolation.

## What you've accomplished and what's next

You started with two non-Topo, non-Compose projects, made them a standard Compose project, and then converted that Compose project into a Topo Template. You created the web app image, added artifact builds for the ExecuTorch `.pte` model and Cortex-M33 ELF, packaged the firmware as a Remoteproc Runtime service, and exposed the build cache inputs as Topo arguments.

Next, you will prepare the FRDM i.MX 93 target, deploy the Template with Topo, and run the image classification application.
