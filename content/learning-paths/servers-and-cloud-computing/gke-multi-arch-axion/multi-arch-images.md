---
title: Build and push multi-architecture images to Artifact Registry with Docker Buildx
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

With the environment ready, the next step is to make the Online Boutique services multi-architecture and publish them to Artifact Registry. You will patch a few Dockerfiles (only where needed), set up Docker Buildx, build and push amd64 & arm64 images, and verify the resulting manifest lists.

### Update Dockerfiles for multi-arch support

The goal of this step is to make the application's services compatible with both amd64 and arm64. Most Dockerfiles in the microservices demo already support multi-architecture builds without modification. However, three services require updates:

- **emailservice**
- **recommendationservice**
- **loadgenerator**

{{% notice Note %}}
Production migrations begin with assessing cross-architecture compatibility for each service (base images, native extensions such as CGO/JNI, platform-specific packages, and CI build targets). This section demonstrates minor Dockerfile edits for three representative services. In the referenced Online Boutique release, the remaining services generally build for both **amd64** and **arm64** without modification.
{{% /notice %}}

#### Update src/emailservice/Dockerfile

Replace the entire contents of the file with the following multi-architecture-compatible version:

```bash
cat << 'EOF' > src/emailservice/Dockerfile

ARG TARGETPLATFORM

FROM --platform=$TARGETPLATFORM python:3.12.8-alpine@sha256:54bec49592c8455de8d5983d984efff76b6417a6af9b5dcc8d0237bf6ad3bd20 AS base
FROM --platform=$TARGETPLATFORM base AS builder

RUN apk update \
  && apk add --no-cache g++ linux-headers musl-dev \
  && rm -rf /var/cache/apk/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM --platform=$TARGETPLATFORM base
ENV PYTHONUNBUFFERED=1 ENABLE_PROFILER=1

RUN apk update \
  && apk add --no-cache libstdc++ \
  && rm -rf /var/cache/apk/*

WORKDIR /email_server
COPY --from=builder /usr/local/lib/python3.12/ /usr/local/lib/python3.12/
COPY . .
EXPOSE 8080
ENTRYPOINT ["python","email_server.py"]
EOF
```

{{% notice Note %}}
**Why this works:** `TARGETPLATFORM` is set by Docker Buildx at build time (linux/amd64 or linux/arm64). Using `--platform=$TARGETPLATFORM` ensures you pull the correct base image and compile native artifacts for that architecture.
{{% /notice %}}

#### Apply equivalent updates to the other two services

Run the following commands to automatically update the remaining two Dockerfiles:
- src/recommendationservice/Dockerfile
- src/loadgenerator/Dockerfile

These commands insert ARG TARGETPLATFORM, update platform references, and ensure the required cross-architecture libraries (`musl-dev` & `libgcc`) are included.
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

#### Update src/loadgenerator/Dockerfile
```bash
sed -i \
  -e '/^# limitations under the License./a ARG TARGETPLATFORM' \
  -e 's|^FROM[[:space:]]\+python:3\.12\.8-alpine@sha256:54bec49592c8455de8d5983d984efff76b6417a6af9b5dcc8d0237bf6ad3bd20[[:space:]]\+AS[[:space:]]\+base|FROM --platform=\$TARGETPLATFORM python:3.12.8-alpine@sha256:54bec49592c8455de8d5983d984efff76b6417a6af9b5dcc8d0237bf6ad3bd20 AS base|' \
  -e 's|^FROM[[:space:]]\+base[[:space:]]\+AS[[:space:]]\+builder|FROM --platform=\$TARGETPLATFORM base AS builder|' \
  -e 's|^FROM[[:space:]]\+base$|FROM --platform=\$TARGETPLATFORM base|' \
  -e '/apk add/ s/\blinux-headers\b/& musl-dev/' \
  -e '/apk add/ s/\blibstdc\b/libstdc++/g' \
  -e '/apk add/ s/\blibgcc\+\+\b/libgcc/g' \
  -e '/apk add/ {/libgcc/! s/$/ libgcc/; }' \
  src/loadgenerator/Dockerfile
```

{{% notice Note %}}
Result: All three services now support cross-architecture builds.
{{% /notice %}}

### Prepare the build environment & permissions

Before building and pushing images, complete these setup steps in Cloud Shell:

1. Create and activate a new Buildx builder to enable multi-platform builds:  

```bash
docker buildx create --use --name multiarch-builder --driver docker-container
docker buildx inspect --bootstrap
```
Cloud Shell uses the docker-container driver for multi-arch and sets up emulation when required.
Cloud Shell's default Docker driver doesn't support multi-arch. The docker-container driver enables multi-platform builds and sets up emulation when required.

2. Ensure Artifact Registry permissions:

Your Cloud Shell account must have permission to push images to Artifact Registry. Grant the Artifact Registry **Writer**  role to your account:

```bash
gcloud projects add-iam-policy-binding "${PROJECT_ID}" --member="user:$(gcloud config get-value account)" --role="roles/artifactregistry.writer" --condition=None --quiet

```

Optionally, verify that the role binding was added correctly:

```bash
gcloud projects get-iam-policy "${PROJECT_ID}" --flatten="bindings[].members" --filter="bindings.role=roles/artifactregistry.writer AND bindings.members=user:$(gcloud config get-value account)" --format="value(bindings.role)"
```

Now that the Dockerfiles have been updated, you will build and push container images for both arm64 and amd64 architectures. Choose one of the following approaches based on your environment:

### Option 1:  Single environment (Cloud Shell, emulation)

#### Build one service (example):

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t "${GAR}/adservice:v1" src/adservice --push
```
#### Build multiple services (script):

```bash
cat << 'EOF' > build-multiarch.sh
#!/usr/bin/env bash
set -euo pipefail

: "${GAR:?GAR must be set (region-docker.pkg.dev/PROJECT_ID/REPO)}"

# Adjust this list as needed; 'emailservice' can be built here or via Option 2.
services=(
  cartservice
  checkoutservice
  currencyservice
  frontend
  paymentservice
  productcatalogservice
  recommendationservice
  shippingservice
  loadgenerator
)

for svc in "${services[@]}"; do
  if [ "$svc" = "cartservice" ] && [ -d "src/cartservice/src" ]; then
    context="src/cartservice/src"
  else
    context="src/${svc}"
  fi

  echo ">>> Building ${svc}..."
  docker buildx build --platform linux/amd64,linux/arm64 -t "${GAR}/${svc}:v1" "${context}" --push
done
EOF

chmod +x build-multiarch.sh
./build-multiarch.sh

```
### Option 2:  Two native builders (one amd64 host, one arm64 host)

Use an amd64 machine for amd64 images and an arm64 machine (for example, a C4A VM) for arm64 images. Authenticate both hosts to Artifact Registry, then compose a single multi-arch tag.

**On the amd64 host:**

```bash
# Build amd64-specific image and push with an arch suffix tag
docker buildx build --platform linux/amd64 -t "${GAR}/emailservice:v1-amd64" src/emailservice --push
```

**On the arm64 host:**
```bash
# Build arm64-specific image and push with an arch suffix tag
docker buildx build --platform linux/arm64 -t "${GAR}/emailservice:v1-arm64" src/emailservice --push
```

Combine into a single multi-arch manifest (run from either host):

```bash
docker buildx imagetools create --tag "${GAR}/emailservice:v1" "${GAR}/emailservice:v1-amd64" "${GAR}/emailservice:v1-arm64"

```
Repeat the same pattern for other services if you prefer native builds:
- Replace emailservice with each service name.
- Push :v1-amd64 and :v1-arm64, then create :v1.


{{% notice Tip %}}
Two supported build paths are shown. Use **Option 1** when you have a single environment (for example, Cloud Shell); Docker Buildx uses emulation (QEMU via `binfmt_misc`) to produce both architectures, and builds that compile native dependencies may take longer. Use **Option 2** when you have access to both **amd64** and **arm64** hosts; native builds avoid emulation and typically finish faster. Both approaches produce the same multi-architecture tag in Artifact Registry; the resulting images run natively on their target CPU.
{{% /notice %}}

### Verify images in Artifact Registry

List all images in your Artifact Registry repository to confirm each service tag was pushed:

```bash
gcloud artifacts docker images list "${GAR}"
```

Inspect one multi-arch tag to confirm it's a **manifest list** that references per-architecture images:
```bash
docker buildx imagetools inspect "${GAR}/adservice:v1"
```

You should see entries for:
```
Platform: linux/amd64
Platform: linux/arm64
```

{{% notice Explanation %}}
A manifest list ties the per-architecture images to a single tag. When a node pulls the image, Kubernetes automatically fetches the variant that matches the node's CPU architecture.
{{% /notice %}}

