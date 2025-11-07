---
title: Build-ready Dockerfiles for multi-architecture (amd64 & arm64)
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

With the environment prepared, this step makes the Online Boutique services multi-architecture ready. You will patch a few Dockerfiles so they build cleanly for both architectures. On the next page, you will build and push images using a GKE-native Buildx builder (one pod per arch, no QEMU).

### Services that need edits

Most services already build for both architectures. These four need small, safe changes:

- **emailservice** 
- **recommendationservice**
- **loadgenerator**
- **cartservice**

These edits don't change application behavior-they only ensure the right compiler headers and runtime libs are present per architecture (Python native wheels for email/recommendation/loadgen; system `protoc` for .NET cartservice).

{{% notice Note %}}
Production migrations begin with assessing cross-architecture compatibility for each service (base images, native extensions such as CGO/JNI, platform-specific packages, and CI build targets). This section demonstrates minor Dockerfile edits for four representative services. In the referenced Online Boutique release, the remaining services generally build for both **amd64** and **arm64** without modification.
{{% /notice %}}

#### Update src/emailservice/Dockerfile

Replace the entire contents of the file with the following multi-architecture-compatible version:

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

**What these edits do**

- **BuildKit syntax** unlocks `--mount=type=cache` to speed rebuilds.
- **TARGETPLATFORM** lets Buildx set linux/amd64 vs linux/arm64 explicitly.
- **Dev vs runtime packages:** build stage compiles native wheels; final stage keeps only needed shared libs.
- **`--prefer-binary`** avoids source builds when wheels exist (more reliable across arches).
- **Removed extra `apk update`** since `apk add --no-cache` already avoids stale indexes & caches.


#### Apply equivalent updates to the other three services

Run the following sed commands to automatically patch the Dockerfiles:

#### Update src/recommendationservice/Dockerfile

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
**What these edits do**

- Make the base image architecture-aware.
- Let native wheels build cleanly.
- Keep the runtime slim & predictable.


#### Update src/loadgenerator/Dockerfile
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

**What these edits do**

- Make the base image architecture-aware.
- Fix native build/run deps.
- Keep runtime lean and no flags/app code changed.

#### Update src/cartservice/src/Dockerfile

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
**What these edits do**

- Install system protoc.
- Force MSBuild to use it.
- No behavioral change.

{{% notice Note %}}
`ARG TARGETPLATFORM` + `FROM --platform=$TARGETPLATFORM` is not strictly required if you always build with --platform and your base image is multi-arch (which it is). Keeping it is perfectly fine and makes intent explicit; it does not change runtime behavior.

Result: All services now support cross-architecture builds.
{{% /notice %}}

