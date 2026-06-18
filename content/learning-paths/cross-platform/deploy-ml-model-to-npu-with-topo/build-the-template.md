---
title: Build the Topo Template from scratch
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you will build

In this section, you will build the `topo-imx93-npu-deployment` Template starting from two baremetal
projects:

- a Cortex-A web application that prepares images, writes model and tensor data into shared memory, and sends inference commands over `RPMsg`
- a Cortex-M33 ExecuTorch runner firmware project for the FRDM i.MX 93

You will first combine those sources into one repository, then make the repository a normal Compose project, and only then add the Topo metadata and Remoteproc Runtime services.

## Install the Topo Template authoring skills

The [Topo Template Format](https://github.com/arm/Topo-Template-Format) repository includes public authoring skills for agents that support skill installation:

- `topo-template-context`: provides Topo and Topo Template reference context for `x-topo` metadata, schema, docs, and CLI Template behavior.
- `topo-template-bootstrap`: converts a Compose repository into a Topo Template by adding or improving `compose.yaml` and `x-topo` metadata.
- `topo-template-lint`: reviews a Topo Template for schema correctness, metadata consistency, deployment success messages, and build argument wiring.

Install the skills with `npx skills`:

```bash
npx skills add arm/topo-template-format
```

If your agent does not use `npx skills`, clone the Template Format repository and manually copy or symlink the directories under `skills/` into your agent's skills directory:

```bash
git clone https://github.com/arm/Topo-Template-Format.git
```

Restart your agent after installing or updating the skills.

You can use the skills when you reach the Compose-to-Topo step in this walkthrough. From the root of the Compose project, ask your agent to use `topo-template-bootstrap`:

```output
Use topo-template-bootstrap on this repository.
Treat the root compose.yaml as the Template root.
Preserve plain docker compose behavior.
Add x-topo metadata only where it reflects the actual services, hardware requirements, and build arguments.
```

After bootstrap, ask the agent to use `topo-template-lint`:

```output
Use topo-template-lint on this repository.
Validate compose.yaml against the Topo Template Format schema.
Check README alignment, Remoteproc Runtime metadata, and x-topo.args wiring.
```

## Create the repository from the baremetal projects

Clone the original Topo Template and start a new empty repository:

```bash
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
cp -R ../topo-imx93-npu-deployment/executorch-runner/patches executorch-runner
```

Add the licenses and ignore rules used by the source projects:

```bash
cp ../topo-imx93-npu-deployment/LICENSE.md .
cp -R ../topo-imx93-npu-deployment/licenses .
cp ../topo-imx93-npu-deployment/.gitignore .
```

At this point, the repository is only source code. It is not a Compose project and it is not a Topo Template.

## Turn the sources into a Compose project

Before adding Topo metadata, make the project work as ordinary Compose. Start by containerizing the Cortex-A web application.

Create `webapp/Dockerfile`:

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

Create `webapp/compose.yaml`:

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

Create the root `compose.yaml`:

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

## Add the ExecuTorch artifact pipeline

The web application needs an ExecuTorch `.pte` model, and the target needs a Cortex-M33 ELF image. Both artifacts are built by `executorch-runner/Dockerfile`:

```bash
cp ../topo-imx93-npu-deployment/executorch-runner/Dockerfile executorch-runner/
```

For this multi-stage Dockerfile:

- `build-base`: installs the common Ubuntu build tools.
- `executorch-base`: clones ExecuTorch, installs the Arm backend dependencies, and copies `export_mv2_imx93.py`.
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

Add artifact-only services to the root `compose.yaml`:

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

These services are build targets, not runtime containers. `scale: 0` keeps them out of the running deployment while still making their artifacts available to other builds.

Update `webapp/compose.yaml` so the Flask image imports the `.pte` artifact:

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

Then update `webapp/Dockerfile` to copy the model from that BuildKit context:

```Dockerfile
COPY --from=pte_artifacts /artifacts/mv2_ethosu65_256.pte /opt/mv2-imx93/mv2_ethosu65_256.pte
```

## Add the Remoteproc Runtime service

Add the Cortex-M33 runner as a Compose service:

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

This is the heterogeneous deployment hook. Docker still builds an image, but the service is not started as a Linux userspace process. The runtime `io.containerd.remoteproc.v1` selects Remoteproc Runtime, and the `remoteproc.name` annotation tells the shim to use the i.MX remote processor
driver.

Make the web application depend on the CM33 runner:

```yaml
services:
  webapp:
    platform: linux/arm64
    extends:
      file: webapp/compose.yaml
      service: webapp
    depends_on:
      - cm33-runner
```

The web app is privileged and mounts `/sys` and `/dev` because it checks the device tree, reads remoteproc state through `/sys/class/remoteproc`, talks to `/dev/ttyRPMSG*`, writes shared memory through `/dev/mem`, and checks for `/dev/ethosu0`.

## Add Topo metadata and arguments

After the Compose services are complete, add the root-level `x-topo` block.
Keep it at the root of `compose.yaml`, not under `services`.

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

```yaml
cache_from:
  - ${EXECUTORCH_BASE_CACHE_IMAGE:-ghcr.io/arm-examples/topo-imx93-npu-deployment/executorch-base:et-v1.2.0-ubuntu24.04}
```

Keep runtime settings such as `WEBAPP_PORT` as normal Compose interpolation unless you intentionally want Topo to collect them as Template setup arguments.

## Validate the final Template

Check the Compose model and check that the Topo metadata is present:

```bash
docker compose config
```

If you have the Topo Template Format schema locally, validate the root Compose file:

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

## What you have built

You started with two baremetal projects, made them a standard Compose project, and then converted that Compose project into a Topo Template.
The final Template builds the ExecuTorch model, packages the Cortex-M33 firmware as a Remoteproc Runtime service, runs the Cortex-A Flask web app, and
exposes the build cache inputs as Topo arguments.
