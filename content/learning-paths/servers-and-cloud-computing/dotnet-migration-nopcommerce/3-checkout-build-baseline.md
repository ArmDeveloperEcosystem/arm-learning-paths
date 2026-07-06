---
title: Create an Arm baseline before optimization
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build and baseline

Create a reproducible Arm baseline before optimization work. 

You'll pin the source, verify a clean build, and capture a representative endpoint baseline so you can measure later changes against a known control.

### Clone and pin the source

Pinning the exact tag and commit avoids silent drift in dependencies and behavior. 

Run the following commands on the Arm-based virtual machine (VM):

```bash
git clone https://github.com/nopSolutions/nopCommerce.git
cd nopCommerce
git fetch --tags --prune
git checkout release-4.90.3
git rev-parse --short=10 HEAD   # expect 9beda11c42
```
The later commands assume you're in the `nopCommerce` repository root unless stated otherwise.

If you open a new terminal later, return to the same repository root before running commands:

```bash
cd ~/nopCommerce  # replace with your clone path if different
```

### Restore and build on Arm

Run restore and build on the Arm-based VM to establish a native Arm baseline:

```bash
# Restore dependencies first so build failures are easier to triage.
dotnet restore src/Presentation/Nop.Web/Nop.Web.csproj

# Build release binaries without re-restoring packages.
dotnet build src/Presentation/Nop.Web/Nop.Web.csproj -c Release --no-restore
```
Restoring first separates package resolution problems from compilation problems, and `--no-restore` makes the build validate the already restored dependency graph.

### Start and install nopCommerce

Start the app locally and complete installer setup with PostgreSQL. Run the following command in one terminal and leave it running: 

```bash
cd src/Presentation/Nop.Web
dotnet run -c Release --no-build --urls http://0.0.0.0:5000
```
`dotnet run` hosts the web application and keeps the terminal attached to the server logs.

In a browser, open `http://<cobalt-public-ip>:5000` or use an SSH tunnel to reach `http://127.0.0.1:5000`. On the nopCommerce install page, select PostgreSQL and use the database settings from the previous section:

- Server: `127.0.0.1`
- Port: `5432`
- Database: `nopcommerce`
- User: `nop`
- Password: the value of `NOP_POSTGRES_PASSWORD`

Use sample data if you want a stable set of storefront pages for repeatable endpoint tests.

Open a second terminal, return to the repository root, and verify that the app is installed and serving storefront traffic:

```bash
cd ~/nopCommerce  # replace with your clone path if different

# Root should return storefront content.
curl -s -o /dev/null -w 'root=%{http_code}\n' http://127.0.0.1:5000/

# Install route should redirect once installation is complete.
curl -s -o /dev/null -w 'install=%{http_code}\n' http://127.0.0.1:5000/install
```

The outputs after a successful install should be: `root=200`, `install=302`.

### Run the baseline

Don't benchmark `/install`. Baseline stable storefront paths first, then add cart and attribute-change routes only after you know the valid product IDs, attribute IDs, request method, and anti-forgery token behavior for your installed store.

- `/`
- `/search/`
- `/catalog/searchtermautocomplete`
- `/product/search`
- Product and category pages from your sample data
- Cart or checkout endpoints from a recorded production-like workflow

Create the endpoint tester in the repository root:

```python {file_name="test_nopcommerce_endpoints.py"}
#!/usr/bin/env python3
import argparse
import concurrent.futures
import json
import statistics
import time
import urllib.error
import urllib.request

DEFAULT_ROUTES = [
    "/",
    "/search/",
    "/product/search",
    "/catalog/searchtermautocomplete?term=a",
]


def percentile(values, percent):
    if not values:
        return None
    data = sorted(values)
    index = round((percent / 100) * (len(data) - 1))
    return data[index]


def fetch(base_url, route, timeout):
    url = base_url.rstrip("/") + route
    start = time.perf_counter()
    status = None
    error = None

    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            response.read()
            status = response.getcode()
    except urllib.error.HTTPError as exc:
        exc.read()
        status = exc.code
        error = f"HTTPError:{exc.code}"
    except Exception as exc:
        error = type(exc).__name__

    elapsed_ms = (time.perf_counter() - start) * 1000
    ok = status is not None and 200 <= status < 400
    return {
        "route": route,
        "status": status,
        "ok": ok,
        "elapsed_ms": round(elapsed_ms, 2),
        "error": error,
    }


def summarize(samples):
    summary = {}
    for route in sorted({sample["route"] for sample in samples}):
        route_samples = [sample for sample in samples if sample["route"] == route]
        successful = [sample["elapsed_ms"] for sample in route_samples if sample["ok"]]
        status_counts = {}
        for sample in route_samples:
            key = str(sample["status"]) if sample["status"] is not None else "no-status"
            status_counts[key] = status_counts.get(key, 0) + 1

        summary[route] = {
            "requests": len(route_samples),
            "errors": sum(1 for sample in route_samples if not sample["ok"]),
            "status_counts": status_counts,
            "p50_ms": round(statistics.median(successful), 2) if successful else None,
            "p95_ms": round(percentile(successful, 95), 2) if successful else None,
            "max_ms": round(max(successful), 2) if successful else None,
        }
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--concurrency", type=int, default=8)
    parser.add_argument("--iterations", type=int, default=20)
    parser.add_argument("--json-out", required=True)
    parser.add_argument("--route", action="append", default=[])
    parser.add_argument("--timeout", type=float, default=10)
    args = parser.parse_args()

    routes = args.route or DEFAULT_ROUTES
    work = [route for route in routes for _ in range(args.iterations)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        samples = list(pool.map(lambda route: fetch(args.base_url, route, args.timeout), work))

    result = {
        "base_url": args.base_url,
        "concurrency": args.concurrency,
        "iterations_per_route": args.iterations,
        "routes": routes,
        "summary": summarize(samples),
        "samples": samples,
    }

    with open(args.json_out, "w", encoding="utf-8") as output:
        json.dump(result, output, indent=2)
        output.write("\n")

    print(json.dumps(result["summary"], indent=2))
    raise SystemExit(1 if any(not sample["ok"] for sample in samples) else 0)


if __name__ == "__main__":
    main()
```

The script uses only the Python standard library, submits requests with fixed concurrency, treats non-2xx and non-3xx responses as errors, and writes raw samples plus per-route summaries to JSON.

Run the endpoint tester from the repository root while the app is still running in the first terminal:

```bash
# Use fixed concurrency and iterations for a repeatable starting point.
python3 test_nopcommerce_endpoints.py \
  --base-url http://127.0.0.1:5000 \
  --concurrency 8 \
  --iterations 20 \
  --json-out arm_before.json
```

The command prints the per-route summary and writes the raw measurements to `arm_before.json`. Keep that JSON file unchanged because it's the baseline artifact used in the tuning step.

#### Baseline quality rules

Use these rules before you compare any optimization result:

- Run at least three baseline trials with identical parameters.
- Keep endpoint order fixed per run (not randomized) when comparing before and after.
- Keep database state and seeded data identical across runs.
- Capture raw JSON for every run and compare medians, not single outliers.

This baseline process becomes the control for every later tuning or code-change decision.

## What you've accomplished and what's next

You've now created a baseline before migrating the application. 

Next, you'll make note of dependencies before migration. 


