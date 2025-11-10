---
title: Create build-ready Dockerfiles for both architectures
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Update Dockerfiles to support multi-architecture builds

Now that your environment set up, you're now ready to modify the Online Boutique services to support multi-architecture builds.

You will patch some Dockerfiles so they build cleanly for both architectures. 

## Services to edit

Most services in Online Boutique already build for both architectures without any changes.

Four services need small updates:

- emailservice
- recommendationservice
- loadgenerator
- cartservice

These edits ensure the correct compiler headers and runtime libraries are present for each architecture. The changes include:

- Python native wheels for emailservice, recommendationservice, and loadgenerator
- System `protoc` for the .NET cartservice

These updates don't change application behavior.

{{% notice Note %}}
Production migrations begin with assessing cross-architecture compatibility for each service (base images, native extensions such as CGO/JNI, platform-specific packages, and CI build targets). This section demonstrates minor Dockerfile edits for four representative services. In the referenced Online Boutique release, the remaining services generally build for both **amd64** and **arm64** without modification.
{{% /notice %}}

## Update the emailservice Dockerfile

You can review the [emailservice Dockerfile](https://raw.githubusercontent.com/GoogleCloudPlatform/microservices-demo/refs/heads/main/src/emailservice/Dockerfile) before replacing it.

Run the following command to replace the entire contents of the file with the multi-architecture-compatible version:

```bash
cat << 'EOF' > src/emailservice/Dockerfile
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# syntax=docker/dockerfile:1.6
ARG TARGETPLATFORM
FROM --platform=$TARGETPLATFORM python:3.12.8-alpine@sha256:54bec49592c8455de8d5983d984efff76b6417a6af9b5dcc8d0237bf6ad3bd20 AS base
FROM --platform=$TARGETPLATFORM base AS builder
RUN apk add --no-cache g++ gcc linux-headers musl-dev libffi-dev openssl-dev
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --prefer-binary -r requirements.txt
FROM --platform=$TARGETPLATFORM base
ENV PYTHONUNBUFFERED=1
ENV ENABLE_PROFILER=1
RUN apk add --no-cache libstdc++ libgcc libffi openssl
WORKDIR /email_server
COPY --from=builder /usr/local/lib/python3.12/ /usr/local/lib/python3.12/
COPY . .
EXPOSE 8080
ENTRYPOINT ["python","email_server.py"]


EOF
```

Here is a summary of the changes:

- The updated Dockerfile uses BuildKit syntax to enable cache mounts, which speed up rebuilds. 
- The `TARGETPLATFORM` argument allows Buildx to explicitly set the target architecture (either `linux/amd64` or `linux/arm64`). The build follows a two-stage approach: the builder stage compiles native wheels with necessary development packages, while the final runtime stage includes only the required shared libraries. 
- The `--prefer-binary` flag helps avoid building from source when pre-built wheels are available, making builds more reliable across architectures. The update also removes the extra `apk update` command because `apk add --no-cache` already handles index updates without creating a cache.

## Apply updates to recommendationservice, loadgenerator, and cartservice

Run the following sed commands to automatically patch the remaining Dockerfiles.

### Update the recommendationservice Dockerfile
You can review the [recommendationservice Dockerfile](https://raw.githubusercontent.com/GoogleCloudPlatform/microservices-demo/refs/heads/main/src/recommendationservice/Dockerfile) before modifying it.

Run the following command to update the file with the required multi-architecture changes:

```bash
sed -i \
  -e '/^# limitations under the License./a ARG TARGETPLATFORM' \
  -e 's|^FROM[[:space:]]\+python:3\.12\.8-alpine@sha256:54bec49592c8455de8d5983d984efff76b6417a6af9b5dcc8d0237bf6ad3bd20 AS base|FROM --platform=\$TARGETPLATFORM python:3.12.8-alpine@sha256:54bec49592c8455de8d5983d984efff76b6417a6af9b5dcc8d0237bf6ad3bd20 AS base|' \
  -e 's|^FROM[[:space:]]\+base[[:space:]]\+AS[[:space:]]\+builder|FROM --platform=\$TARGETPLATFORM base AS builder|' \
  -e 's|^FROM[[:space:]]\+base$|FROM --platform=\$TARGETPLATFORM base|' \
  -e '/apk add/ s/linux-headers/& musl-dev/' \
  -e '/pip install/ s|-r requirements.txt|--prefix=/install -r requirements.txt|' \
  -e 's|COPY --from=builder /usr/local/lib/python3\.12/ /usr/local/lib/python3\.12/|COPY --from=builder /install/lib/python3.12 /usr/local/lib/python3.12/|' \
  src/recommendationservice/Dockerfile
```

The three key changes are to make the base image architecture-aware, let native wheels build cleanly, and keep the runtime slim and predictable.

### Update loadgenerator Dockerfile

You can review the [loadgenerator Dockerfile](https://raw.githubusercontent.com/GoogleCloudPlatform/microservices-demo/refs/heads/main/src/loadgenerator/Dockerfile) before modifying it. 

Run the following command to update the file with the required multi-architecture changes:

```bash
FILE=src/loadgenerator/Dockerfile

# Platform plumbing (TARGETPLATFORM) + fix FROM lines
sed -i \
  -e '/^FROM --platform=\$BUILDPLATFORM python:3\.12\.8-alpine@sha256:54bec49592c8455de8d5983d984efff76b6417a6af9b5dcc8d0237bf6ad3bd20 AS base/i ARG TARGETPLATFORM' \
  -e 's/^FROM --platform=\$BUILDPLATFORM python:3\.12\.8-alpine@sha256:54bec49592c8455de8d5983d984efff76b6417a6af9b5dcc8d0237bf6ad3bd20 AS base/FROM --platform=$TARGETPLATFORM python:3.12.8-alpine@sha256:54bec49592c8455de8d5983d984efff76b6417a6af9b5dcc8d0237bf6ad3bd20 AS base/' \
  -e 's/^FROM base AS builder$/FROM --platform=$TARGETPLATFORM base AS builder/' \
  -e 's/^FROM base$/FROM --platform=$TARGETPLATFORM base/' \
  "$FILE"

# Ensure libgcc is present on runtime apk line that installs libstdc++
sed -i -E \
  '/^[[:space:]]*&&[[:space:]]*apk add --no-cache[[:space:]]+libstdc\+\+/{/libgcc/! s/libstdc\+\+/libstdc++ libgcc/}' \
  "$FILE"

# Add musl-dev to the builder deps line
sed -i -E \
  '/^[[:space:]]*&&[[:space:]]*apk add --no-cache[[:space:]]+wget[[:space:]]+g\+\+[[:space:]]+linux-headers/ s/linux-headers/linux-headers musl-dev/' \
  "$FILE"
```

The changes focus on three key areas. First, make the base image architecture-aware so it automatically selects the correct variant for your platform. Second, fix native build and runtime dependencies to ensure they match the target architecture. Third, keep the runtime environment lean—you don't need to change any flags or application code.

### Update cartservice Dockerfile

You can review the [carkservice Dockerfile](https://raw.githubusercontent.com/GoogleCloudPlatform/microservices-demo/refs/heads/main/src/cartservice/src/Dockerfile) before replacing it. 
Run the following command to update the file with the required multi-architecture changes:

```bash
FILE=src/cartservice/src/Dockerfile

# 1) After the ARG line, install protoc in the builder image
sed -i \
  '/^ARG TARGETARCH$/a RUN apt-get update \&\& apt-get install -y --no-install-recommends protobuf-compiler \&\& rm -rf /var/lib/apt/lists/*' \
  "$FILE"

# 2) In the publish step, inject Protobuf_Protoc=/usr/bin/protoc right after the first line
sed -i \
  '/^RUN[[:space:]]\+dotnet publish cartservice\.csproj[[:space:]]*\\$/a \    -p:Protobuf_Protoc=/usr/bin/protoc \\' \
  "$FILE"

```

Here is a summary of the changes:

- Install the system `protoc` compiler in the builder image
- Configure MSBuild to use the installed `protoc` instead of downloading one

These changes don't affect application behavior.

{{% notice Note %}}
Using `ARG TARGETPLATFORM` and `FROM --platform=$TARGETPLATFORM` isn't strictly required when you build with `--platform` and your base image supports multiple architectures. However, keeping these declarations makes your build intent explicit and doesn't change runtime behavior.

{{% /notice %}}

After updating these Dockerfiles, all services support multi-architecture builds. You're ready to build and push images using a GKE-native Buildx builder. Great job!



