---
title: Submit and verify a checkout change
description: Run the supported business request and compare the validated checkout with its original behavior.
weight: 6
layout: learningpathall
---

## Inspect the starting shop

Open the dashboard's shop preview before starting a run. Change basket quantities and note the original subtotal, shipping, and total. Return to the overview. The prepared shop is the code context for the agents; the prompt does not provide a new repository.

Paste this request into the request field and select **Run live agents**:

```text
Apply a 15% discount when the original cart subtotal is $80 or more. Give free shipping when the original subtotal is $120 or more; otherwise charge $7.99 for nonempty carts. Keep empty-cart totals zero. Calculate monetary values in integer cents, rounding the discount down.

Show the original subtotal, Savings, promotion status, delivery charge and final total using the backend quote. Update these values when basket quantities change, preserving the existing checkout interface and quote integration.

Verify one cent below, exactly at and one cent above both thresholds, empty carts, multiple products and quantities, and rounding.
```

Watch the architecture highlight the active stages. The backend and frontend run together. QA starts after both builds, because it needs their combined result. Validation follows QA. The manager remains responsible for dispatch and status throughout the run, but it does not run the local Gemma models itself.

Only one workflow runs at a time in this demo. A busy service rejects another submission rather than creating an unbounded queue.

## Check the result before opening the preview

Look for a passed run, zero failed checks, and an updated shop link. Inspect the plan and generated-file evidence. The expected outputs are `pricing.py`, the assembled `checkout.html`, and `qa_tests.py`.

For this policy, the independent validator constructs these monetary checks:

| Original subtotal | Discount | Shipping | Final total |
| --- | --- | --- | --- |
| Empty cart | $0.00 | $0.00 | $0.00 |
| $79.99 | $0.00 | $7.99 | $87.98 |
| $80.00 | $12.00 | $7.99 | $75.99 |
| $80.01 | $12.00 | $7.99 | $76.00 |
| $119.99 | $17.99 | $7.99 | $109.99 |
| $120.00 | $18.00 | $0.00 | $102.00 |
| $120.01 | $18.00 | $0.00 | $102.01 |

Both thresholds use the **original** subtotal. The discount calculation uses integer division: `subtotal_cents * 15 // 100`. This rounds down to whole cents. Boundary checks use synthetic catalog items, so you do not need to find a real shop basket worth exactly $79.99.

The protected oracle is maintained separately from generated pricing code. For the supplied prompt, the recorded run reports 14 passing result groups: 12 monetary cases, one basic checkout HTML contract check, and one supplemental QA test group. That QA group contained two generated test methods in the recorded run. Future generated tests can differ.

The HTML check verifies a limited contract; it is not an automated browser interaction or accessibility test. Manually confirm the checkout behavior next.

## Compare the updated shop

Open the updated shop through the dashboard. Confirm the Savings row, promotion status, delivery charge, and final total. Change quantities so that a basket crosses each threshold. Empty the basket and check that all monetary values return to zero.

For an original subtotal of $121.00, the expected discount is $18.15, shipping is free, and the final total is $102.85. In the recorded demonstration, the original shop total for that basket was $128.99.

Use the updated link inside the dashboard's shop view: the preview HTML communicates with its parent through a constrained message interface. Opening the raw HTML route alone is not the complete interactive application.

## Inspect the run evidence

Copy the value of `run` from the dashboard URL, then set it in your original deployment terminal. Keep the port-forward terminal running. These calls save evidence for the existing run and do not start another inference request:

```bash
cd "$LP_WORKDIR"
export RUN_ID="your-run-id"
mkdir -p review-evidence
curl --fail --silent --show-error \
  "http://127.0.0.1:8090/api/runs/$RUN_ID" -o review-evidence/run.json
curl --fail --silent --show-error \
  "http://127.0.0.1:8090/api/runs/$RUN_ID/artifacts" -o review-evidence/artifacts.json
curl --fail --silent --show-error \
  "http://127.0.0.1:8090/api/runs/$RUN_ID/metrics" -o review-evidence/metrics.json
python3 -m json.tool review-evidence/run.json
```

Confirm `mode` is `live`, `status` is `passed`, `tests.failed` is zero, and `preview_url` is populated. Inspect the policy values: 15, 8000, 12000, and 799. A generated summary alone is not success evidence.

If the request is rejected as unsupported, keep it within the existing pricing and display contract. If checks still fail after the repair round, the updated preview stays unavailable. Inspect the recorded failure instead of presenting it as a successful change.

## What you have verified

You have checked the generated policy against independent monetary expectations and tested the updated checkout manually. Next, interpret the CPU evidence without confusing workload limits with VM capacity.
