---
title: Observe and benchmark the assistant on N4A
description: Start the telemetry dashboard, generate assistant traffic, and capture a fixed-batch N4A benchmark summary.
weight: 8
layout: "learningpathall"
---

## Review the telemetry scripts

The source tree includes helper scripts that focus traffic and telemetry on the assistant workflow:

- `workshop/telemetry_collector.py` samples Kubernetes metrics and records the assistant node pool.
- `workshop/mini_dashboard.py` renders a simple live dashboard.
- `workshop/request_driver.py` sends live assistant traffic.
- `workshop/fixed_batch_trial.py` runs a repeatable benchmark.
- `workshop/compare_summaries.py` compares benchmark summaries.

Check the assistant service and compile the scripts before you run them:

```bash
kubectl get deployment shoppingassistantservice
kubectl get pods -l app=shoppingassistantservice -o wide
kubectl top pod -l app=shoppingassistantservice --containers

python3 -m py_compile workshop/telemetry_collector.py
python3 -m py_compile workshop/mini_dashboard.py
python3 -m py_compile workshop/request_driver.py
python3 -m py_compile workshop/fixed_batch_trial.py
python3 -m py_compile workshop/compare_summaries.py
```

If `kubectl top` isn't available yet, make sure metrics collection is enabled in the cluster before you rely on CPU telemetry.

## Open three terminals

Use three terminals so telemetry, the dashboard, and benchmark commands can run at the same time.

In each terminal, restore the variables from setup and return to the source tree:

```bash
source "${HOME}/.storefront-axion-env"
cd "${REPO}"

export FRONTEND_IP="$(kubectl get service frontend-external \
  -o jsonpath='{.status.loadBalancer.ingress[0].ip}')"
export APP_URL="http://${FRONTEND_IP}"
```
Use the first terminal for collecting telemetry, the second terminal for the dashboard web server, and the third terminal for live traffic and fixed benchmarks. 

## Start telemetry collection

Run the following command in the first terminal. The `rm` command clears previous live telemetry samples for the dashboard:

```bash
cd "${REPO}" || exit 1
rm -f workshop/telemetry-live.jsonl

python3 workshop/telemetry_collector.py \
  --interval-seconds 2 \
  --output-file workshop/telemetry-live.jsonl
```

Leave this command running.

## Start the dashboard

Run the following command in the second terminal. The `rm` command clears previous live request data for the dashboard:

```bash
cd "${REPO}" || exit 1
rm -f workshop/request-live.jsonl workshop/request-live.log

python3 workshop/mini_dashboard.py \
  --telemetry-file workshop/telemetry-live.jsonl \
  --request-file workshop/request-live.jsonl \
  --port 5000
```

If port `5000` is already in use, choose another available port, such as `5001`. If you use Cloud Shell, open **Web Preview** and select the port you used.

## Confirm assistant health

Run the following command in the third terminal to confirm the health of the assistant:

```bash
cd "${REPO}" || exit 1

export FRONTEND_IP="$(kubectl get service frontend-external \
  -o jsonpath='{.status.loadBalancer.ingress[0].ip}')"
export APP_URL="http://${FRONTEND_IP}"

kubectl get deployment shoppingassistantservice
kubectl rollout status deployment/shoppingassistantservice --timeout=1200s
kubectl get pods -o wide | grep -E 'frontend|shoppingassistantservice'
```

## Generate a short live burst

Start a short request burst in the third terminal so the dashboard shows activity:

```bash
rm -f workshop/request-live.pid

python3 workshop/request_driver.py \
  --base-url "${APP_URL}" \
  --concurrency 4 \
  --delay-seconds 0 \
  --output-file workshop/request-live.jsonl > workshop/request-live.log 2>&1 &

echo $! > workshop/request-live.pid
```

Let it run for about 20 seconds, then inspect the recent log lines:

```bash
sleep 20
tail -n 20 workshop/request-live.log
```

Stop the live burst before you run the fixed benchmark:

```bash
REQUEST_DRIVER_PID="$(cat workshop/request-live.pid)"

if [ -n "${REQUEST_DRIVER_PID}" ] && \
   ps -p "${REQUEST_DRIVER_PID}" -o command= | grep -q 'workshop/request_driver.py'; then
  kill "${REQUEST_DRIVER_PID}"
  wait "${REQUEST_DRIVER_PID}" 2>/dev/null || true
fi

rm -f workshop/request-live.pid
```

Stopping the live burst keeps the N4A and C4A benchmark runs comparable.

## Run the fixed N4A benchmark

Run the fixed batch in the third terminal while the assistant is still on N4A:

```bash
python3 workshop/fixed_batch_trial.py \
  --base-url "${APP_URL}" \
  --expected-pool "${N4A_NODE_POOL_NAME}" \
  --concurrency 2 \
  --prompts-per-worker 8 \
  --delay-seconds 0.2 \
  --request-timeout-seconds 120 \
  --telemetry-interval-seconds 0.5 \
  --idle-threshold-cores 1.0 \
  --idle-stable-samples 3 \
  --idle-timeout-seconds 180 \
  --request-output-file workshop/request-fixed-n4a.jsonl \
  --telemetry-output-file workshop/telemetry-fixed-n4a.jsonl | \
  tee workshop/fixed-n4a-summary.log
```

The command can keep running after the last request lines appear. It's still sampling telemetry and waiting for the assistant to settle back toward idle.

Print the summary line:

```bash
grep 'SUMMARY_JSON' workshop/fixed-n4a-summary.log
```

The summary shows successful requests and the assistant running on the N4A node pool. Don't continue if the summary line is missing or reports a different node pool.

## What you've accomplished and what's next

You've now observed the assistant as a live workload and captured the N4A benchmark baseline.

Next, you'll move only the assistant tier to C4A and run the same benchmark again.
