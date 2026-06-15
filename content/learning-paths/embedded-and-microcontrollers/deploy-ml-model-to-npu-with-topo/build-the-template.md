---
title: Build the Topo Template from scratch
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Start from the application pieces

The `topo-imx93-npu-deployment` repository is a Compose project with Topo metadata at the root. The Topo-specific part is not a replacement for Compose. The services still describe container builds, dependencies, ports, volumes, and runtime settings. The `x-topo` block adds the metadata Topo uses to identify the Template, check target requirements, and prompt for configuration.

The project has three implementation areas:

- `executorch-runner/`: builds the ExecuTorch `.pte` program and the Cortex-M33 firmware ELF.
- `webapp/`: builds the Flask application that stages memory and sends `RUN` commands over `RPMsg`.
- `compose.yaml`: connects the build artifacts, runtime services, Remoteproc Runtime settings, and Topo metadata.

When bootstrapping this Template from scratch, first make the project work as a normal Compose build. Then add the `x-topo` metadata that lets Topo deploy it consistently to an Arm64 target.

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

You can then use the skills as part of the Template authoring flow. From the root of any Compose project, ask your agent to use `topo-template-bootstrap`:

```
Use topo-template-bootstrap on this repository.
Treat the root compose.yaml as the Template root.
Preserve plain docker compose behavior.
Add x-topo metadata only where it reflects the actual services, hardware requirements, and build arguments.
```

After bootstrap, ask the agent to use `topo-template-lint`:

```
Use topo-template-lint on topo-imx93-npu-deployment.
Validate compose.yaml against the Topo Template Format schema.
Check README alignment, deployment_success_message, Remoteproc Runtime metadata, and x-topo.args wiring.
```

The lint pass should confirm that the Template has a root-level `x-topo.name`, that non-remoteproc services use `platform: linux/arm64`, that `cm33-runner` uses the Remoteproc Runtime annotation, and that every `x-topo.args` entry is carried into Compose or Docker build arguments where appropriate.

## Create the runner build pipeline

The `executorch-runner/Dockerfile` is a multi-stage Dockerfile. It builds two artifacts from one build context:

- `mv2_ethosu65_256.pte`: the MobileNetV2 ExecuTorch program lowered for `ethos-u65-256`.
- `executorch_runner_cm33.elf`: the Cortex-M33 firmware image loaded by Linux `remoteproc`.

The first half of the Dockerfile builds the model artifact:

```Dockerfile
FROM build-base AS executorch-base
...
FROM executorch-base AS pte-builder
...
RUN source /workspace/executorch/examples/arm/arm-scratch/setup_path.sh && \
    python /usr/local/bin/export_mv2_imx93.py

FROM busybox:1.36 AS pte-artifacts
COPY --from=pte-builder /workspace/build/mv2-imx93/mv2_ethosu65_256.pte /artifacts/mv2_ethosu65_256.pte
```

The second half builds and packages the firmware:

```Dockerfile
FROM build-base AS runner-base
ARG MCUXSDK_MANIFEST_URL=https://github.com/nxp-mcuxpresso/mcuxsdk-manifests.git
ARG MCUXSDK_MANIFEST_REV=v25.09.00
...
FROM runner-base AS runner-builder
RUN /usr/local/bin/build-runner.sh /artifacts

FROM scratch AS runner-runtime
COPY --from=runner-builder /artifacts/executorch_runner_cm33.elf /executorch_runner_cm33.elf
ENTRYPOINT ["/executorch_runner_cm33.elf"]
```

The `runner-runtime` stage is intentionally a `scratch` image. The only payload is the ELF file. When the service starts with `runtime: io.containerd.remoteproc.v1`, containerd uses Remoteproc Runtime instead of a normal Linux process runtime. Remoteproc Runtime passes the ELF entrypoint to the Linux `remoteproc` driver, and the `imx-rproc` driver loads and releases the Cortex-M33.

The project also applies patches before building the runner. One patch changes the MCUX SDK RAM linker and startup behavior so initialized data is loaded in-place by `remoteproc` rather than copied from a flash-style load address. The runner patches add RPMsg stability fixes and trace output used by the web application.

## Add artifact-only Compose services

At the root of the Template, create normal Compose services for the build outputs:

```yaml
services:
  pte-artifacts:
    platform: linux/arm64
    scale: 0
    build:
      context: executorch-runner
      dockerfile: Dockerfile
      target: pte-artifacts

  runner-artifacts:
    platform: linux/arm64
    scale: 0
    build:
      context: executorch-runner
      dockerfile: Dockerfile
      target: runner-artifacts
```

These services are not runtime application containers. `scale: 0` keeps them out of the running deployment while still making their build targets available to the rest of the Compose project.

The web application imports the PTE artifact as a BuildKit additional context:

```yaml
services:
  webapp:
    platform: linux/arm64
    build:
      context: .
      dockerfile: Dockerfile
      additional_contexts:
        pte_artifacts: service:pte-artifacts
```

The webapp Dockerfile then copies from that context:

```Dockerfile
COPY --from=pte_artifacts /artifacts/mv2_ethosu65_256.pte /opt/mv2-imx93/mv2_ethosu65_256.pte
```

This keeps the model export pipeline separate from the Flask app while still producing one deployable webapp image.

## Add the remote processor service

The Cortex-M33 firmware is represented as another Compose service:

```yaml
services:
  cm33-runner:
    platform: linux/arm64
    build:
      context: executorch-runner
      dockerfile: Dockerfile
      target: runner-runtime
    runtime: io.containerd.remoteproc.v1
    annotations:
      remoteproc.name: imx-rproc
```

This is the key heterogeneous deployment hook. The service is still built by Docker, but it is not launched as a Linux userspace process. The `runtime` selects the containerd Remoteproc Runtime shim, and `remoteproc.name: imx-rproc` selects the i.MX 93 remote processor driver.

After this service starts, Linux exposes the RPMsg device used by the Cortex-A web app. The Flask code waits for `/dev/ttyRPMSG*`, writes the `.pte` file to `0xC0000000`, writes the input tensor to `0xC036D000`, sends `RUN\n` over RPMsg, and parses the `CM33:` response lines into top-1 and top-5 ImageNet results.

## Add the web application service

The web application service extends `webapp/compose.yaml` from the root Compose file:

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

The extended service is privileged and mounts `/sys` and `/dev`:

```yaml
services:
  webapp:
    privileged: true
    ports:
      - "${WEBAPP_PORT:-3001}:3000"
    volumes:
      - /sys:/sys
      - /dev:/dev
```

Those mounts are required because the app checks `/proc/device-tree`, reads remoteproc state through `/sys/class/remoteproc`, talks to `/dev/ttyRPMSG*`, writes model and tensor data through `/dev/mem`, and checks for `/dev/ethosu0`.

## Add Topo metadata

After the Compose services are in place, add the root-level `x-topo` block:

```yaml
x-topo:
  name: "i.MX93 ExecuTorch runner"
  description: "Runs a Cortex-A web application that sends image inference commands to a resident CM33 ExecuTorch runner over RPMsg."
  features:
    - "remoteproc-runtime"
```

Keep `x-topo` at the root of `compose.yaml`, not under `services`. The `features` entry is what tells Topo this Template needs a target with Remoteproc Runtime support. That is why `topo health` checks for:

```output
Remoteproc Runtime: ✅ (remoteproc-runtime)
Remoteproc Shim: ✅ (containerd-shim-remoteproc-v1)
Subsystem Driver (remoteproc): ✅ (imx-rproc)
```

You can also add a deployment success message so users know exactly what to do after deployment:

```yaml
x-topo:
  deployment_success_message: |
    The i.MX93 ExecuTorch runner is deployed.
    Open http://<target-ip>:3001 and classify an ImageNet image.
```

## Expose project configuration

Topo arguments are metadata for project parameters. Compose still carries the values into the build.

The current Template exposes optional cache image parameters:

```yaml
x-topo:
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

Those values are used by Compose interpolation in `build.cache_from`:

```yaml
cache_from:
  - ${EXECUTORCH_BASE_CACHE_IMAGE:-ghcr.io/arm-examples/topo-imx93-npu-deployment/executorch-base:et-v1.2.0-ubuntu24.04}
```

For build-time configuration, wire Topo arguments into standard Compose `build.args`. The runner Dockerfile already declares project-specific arguments for the MCUX SDK manifest:

```Dockerfile
ARG MCUXSDK_MANIFEST_URL=https://github.com/nxp-mcuxpresso/mcuxsdk-manifests.git
ARG MCUXSDK_MANIFEST_REV=v25.09.00
```

To expose the SDK revision through Topo, add matching Compose build args to the services that build `runner-base` descendants:

```yaml
services:
  runner-artifacts:
    build:
      args:
        MCUXSDK_MANIFEST_REV: ${MCUXSDK_MANIFEST_REV:-v25.09.00}

  cm33-runner:
    build:
      args:
        MCUXSDK_MANIFEST_REV: ${MCUXSDK_MANIFEST_REV:-v25.09.00}

x-topo:
  args:
    MCUXSDK_MANIFEST_REV:
      description: MCUX SDK manifest revision used to build the Cortex-M33 runner.
      required: false
      default: v25.09.00
```

With that wiring, Topo can prompt for the value when the Template is cloned or extended, Compose passes the value into Docker BuildKit, and the Dockerfile consumes it through `ARG MCUXSDK_MANIFEST_REV`.

Use this only for configuration that should be chosen at Template setup time. Runtime-only settings, such as `WEBAPP_PORT`, should remain normal Compose environment interpolation unless you intentionally want Topo to collect them as build-time parameters.

## Lint the Template

Before publishing the Template, validate the root Compose file:

```bash
check-jsonschema \
  --schemafile ../topo-template-format/schema/topo-template-format.json \
  compose.yaml
```

Then review the Template the same way Topo Template linting does:

- The Template root contains `compose.yaml`.
- `compose.yaml` contains a root-level `x-topo.name`.
- Non-remoteproc services set `platform: linux/arm64`.
- The `cm33-runner` service uses `runtime: io.containerd.remoteproc.v1` and `remoteproc.name: imx-rproc`.
- `x-topo.description` matches the README and the actual Cortex-A to Cortex-M33 RPMsg flow.
- `x-topo.features` includes `remoteproc-runtime`.
- `x-topo.args` entries are either consumed through Compose interpolation, such as the cache image values, or wired into `services.<service>.build.args` and declared as Dockerfile `ARG` instructions.
- `deployment_success_message` tells the user to open the web app on the configured target port.

## What you've accomplished

You now understand how the `topo-imx93-npu-deployment` Template is built from ordinary Compose services plus Topo metadata: artifact-only build stages produce the model and firmware, Remoteproc Runtime starts the Cortex-M33 ELF, RPMsg connects the processors at runtime, and `x-topo.args` provides a path for setup-time configuration without replacing Docker or Compose.
