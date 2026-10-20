---
title: Analyze a CSV file in the sandbox
description: Run faulty and corrected Python revisions against synthetic sales data, verify the results, and retrieve JSON and HTML reports.
weight: 5
layout: learningpathall
---

## Inspect the application task

The sandbox isolates each attempt — a failure doesn't affect your local machine or require cleanup of the execution environment. `run_demo.py` automates the full sequence: it runs a broken program, observes the failure, replaces it with the corrected version, and runs the tests, all within the same sandbox.

Use the running cluster and warm pool for this task. Download the necessary files:

```bash
cd "$LP_WORKDIR"
mkdir -p csv-app
BASE_URL=https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/servers-and-cloud-computing/gke-agent-sandbox/files/csv-app
for FILE in \
  sales.csv \
  analyze_sales_initial.py \
  analyze_sales.py \
  run_demo.py \
  remote_worker.py \
  test_sales.py; do
  curl -fL "$BASE_URL/$FILE" -o "csv-app/$FILE" || exit 1
done
```

The CSV file has 12 data rows, including sales, refunds, and invalid fields. Inspect the data:

```bash
cat csv-app/sales.csv
```

Review the initial program before running it:

```bash
cat csv-app/analyze_sales_initial.py
```

The initial revision assumes that every quantity can be converted to an integer. Its core calculation is:

```python
total += int(row["quantity"]) * Decimal(row["unit_price"])
```

A row with an empty quantity makes this fail. The corrected revision in `csv-app/analyze_sales.py` validates input, accounts for refunds, uses decimal arithmetic, and renders an HTML report with escaped product names.

You'll use saved revisions for a reproducible comparison.

## Run the failure and correction sequence

The runner uses kubectl to create a claim, verify its Pod, and upload the CSV, tests, and initial program from your local machine. It executes that program remotely, checks the expected failure, and replaces only the program. It then runs the corrected application and six tests in the same workspace.

Run the sequence with an explicit cluster context:

```bash
python3 csv-app/run_demo.py \
  --context "$GKE_CONTEXT" --namespace "$NAMESPACE" \
  --pool axion-python-pool --output-dir "$LP_WORKDIR/runs/csv"
```

The output includes the initial failure:

```output
Initial revision failed as expected:
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: ''
```

The workspace identifier and traceback line numbers can vary.

That error is part of the demonstration. The runner treats an unexpected initial success, a timeout, or a different failure as an unsuccessful run.

After replacing the program, the output includes the following checks and report result. The following condensed example omits the test duration:

```output
test_duplicate_orders_are_not_double_counted (test_sales.SalesChecks...) ... ok
test_invalid_rows_are_accounted_for (test_sales.SalesChecks...) ... ok
test_known_sample (test_sales.SalesChecks...) ... ok
test_malformed_column_counts_can_be_reported (test_sales.SalesChecks...) ... ok
test_product_names_are_escaped_in_html (test_sales.SalesChecks...) ... ok
test_refund_and_decimal_precision (test_sales.SalesChecks...) ... ok
----------------------------------------------------------------------
Ran 6 tests in 0.001s
OK
Report: net revenue $328.41; 9 accepted, 3 rejected
Cleanup: claim removed; bound Sandbox and Pod deleted.
```

The checks cover the following areas:

- Duplicate orders
- Invalid rows
- Decimal precision
- Refunds
- HTML escaping

The runner also verifies that the CSV hash stays unchanged between executions. It replaces the program in the same sandbox workspace without creating a new claim.

## Inspect the retrieved reports

The runner downloads `summary.json`, `report.html`, and `run.json` into the specified output directory before releasing the claim. Inspect the results:

```bash
python3 -m json.tool "$LP_WORKDIR/runs/csv/summary.json"
python3 -m json.tool "$LP_WORKDIR/runs/csv/run.json"
```

Confirm the following values in `summary.json`:

| Field | Expected value |
| --- | --- |
| `gross_sales` | `397.90` |
| `refund_amount` | `69.49` |
| `net_revenue` | `328.41` |
| `accepted_rows` | `9` |
| `rejected_rows` | `3` |

Open `$LP_WORKDIR/runs/csv/report.html` in your browser. On macOS, use `open "$LP_WORKDIR/runs/csv/report.html"`. On Ubuntu with a desktop, use `xdg-open "$LP_WORKDIR/runs/csv/report.html"`. From a local machine without a desktop, copy the report to a machine with a browser.

The HTML displays the same revenue and row counts, plus monthly totals, product totals, and rejected rows.

## Understand the workspace lifecycle

The runner exiting successfully confirms that the task claim and its bound Sandbox and Pod were deleted. The reports remain on your local machine. The warm pool and cluster keep running for the next task.

For a failed run, inspect `$LP_WORKDIR/runs/csv/run.json`. A `cleanup_error` needs attention even if application checks passed.

You can repeat the task with a new output directory, such as `runs/csv-second`.

## What you've accomplished and what's next

You've executed a failure-and-correction workflow on Arm and verified the business result. You've also retained reports after removing the task environment. 

Next, you'll open an interactive shell in another claimed sandbox to inspect its user, filesystem, and exposed Linux information.
