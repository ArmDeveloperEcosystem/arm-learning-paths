---
title: Build and baseline
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Build and baseline

Create a reproducible Arm baseline before optimization work. This page pins source, verifies a clean build, and captures a representative endpoint baseline so later changes can be measured against a known control.

## Clone and pin the source

Pinning the exact tag and commit avoids silent drift in dependencies and behavior.

```bash
git clone https://github.com/nopSolutions/nopCommerce.git
cd nopCommerce
git fetch --tags --prune
git checkout release-4.90.3
git rev-parse --short=10 HEAD   # expect 9beda11c42
```

## Restore and build on Arm

Run on the Arm VM to establish a native Arm baseline.

```bash
# Restore dependencies first so build failures are easier to triage.
dotnet restore src/Presentation/Nop.Web/Nop.Web.csproj

# Build release binaries without re-restoring packages.
dotnet build src/Presentation/Nop.Web/Nop.Web.csproj -c Release --no-restore
```

## Start and install nopCommerce

Start the app locally and complete installer setup with PostgreSQL.

```bash
cd src/Presentation/Nop.Web
dotnet run -c Release --no-build --urls http://0.0.0.0:5000
```

Complete installation with PostgreSQL (`citext` enabled), then verify:

```bash
# Root should return storefront content.
curl -s -o /dev/null -w 'root=%{http_code}\n' http://127.0.0.1:5000/

# Install route should redirect once installation is complete.
curl -s -o /dev/null -w 'install=%{http_code}\n' http://127.0.0.1:5000/install
```

Expected after successful install: `root=200`, `install=302`.

## Baseline methodology

Do not benchmark `/install`. Baseline real storefront paths:

- `/`
- `/search/`
- `/catalog/searchtermautocomplete`
- `/product/search`
- `/category/products/`
- `/addproducttocart/catalog/...`
- `/addproducttocart/details/...`
- `/shoppingcart/productdetails_attributechange/...`
- `/product/combinations`
- `/cart/estimateshipping`
- `/cart/selectshippingoption`

Use the endpoint tester:

```bash
# Use fixed concurrency and iterations for a repeatable starting point.
python3 test_nopcommerce_endpoints.py \
  --base-url http://127.0.0.1:5000 \
  --concurrency 8 \
  --iterations 20 \
  --json-out arm_before.json
```

## Baseline quality rules

Use these rules before you compare any optimization result:

- Run at least 3 baseline trials with identical parameters.
- Keep endpoint order fixed per run (not randomized) when comparing before vs after.
- Keep database state and seeded data identical across runs.
- Capture raw JSON for every run and compare medians, not single outliers.

This baseline process becomes the control for every later tuning or code-change decision.
