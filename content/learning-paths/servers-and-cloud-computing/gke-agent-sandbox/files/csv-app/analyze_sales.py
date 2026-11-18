"""Analyze a synthetic USD sales CSV using only the Python standard library."""

import argparse
import csv
from datetime import date
from decimal import Decimal, InvalidOperation
from html import escape
import json
from pathlib import Path

FIELDS = {"order_id", "date", "product", "quantity", "unit_price", "status"}


def analyze(rows):
    monthly = {}
    products = {}
    rejected = []
    seen = set()
    accepted = 0
    refunds = 0
    gross = Decimal("0")
    refunded = Decimal("0")
    for row_number, row in enumerate(rows, 1):
        try:
            if None in row or any(row.get(field) is None for field in FIELDS):
                raise ValueError("Wrong number of CSV columns")
            order_id = row["order_id"].strip()
            product = row["product"].strip()
            if not order_id or not product:
                raise ValueError("Missing order ID or product")
            if order_id in seen:
                raise ValueError("Duplicate order ID")
            parsed_date = date.fromisoformat(row["date"])
            if parsed_date.isoformat() != row["date"]:
                raise ValueError("Date must use YYYY-MM-DD")
            quantity = int(row["quantity"])
            if quantity <= 0:
                raise ValueError("Quantity must be a positive integer")
            price = Decimal(row["unit_price"])
            if not price.is_finite() or price < 0 or price.as_tuple().exponent < -2:
                raise ValueError("Price must be finite, non-negative, with at most two decimal places")
            status = row["status"].strip()
            if status not in {"sale", "refund"}:
                raise ValueError("Status must be sale or refund")
        except (ValueError, InvalidOperation) as error:
            rejected.append({"data_row": row_number, "order_id": row.get("order_id") or "",
                             "reason": str(error)})
            continue
        seen.add(order_id)
        accepted += 1
        amount = quantity * price
        if status == "refund":
            refunds += 1
            refunded += amount
            amount = -amount
        else:
            gross += amount
        month = parsed_date.strftime("%Y-%m")
        monthly[month] = monthly.get(month, Decimal("0")) + amount
        products[product] = products.get(product, Decimal("0")) + amount

    def money(value):
        return f"{value:.2f}"

    return {
        "currency": "USD",
        "input_rows": accepted + len(rejected),
        "accepted_rows": accepted,
        "rejected_rows": len(rejected),
        "refund_rows": refunds,
        "gross_sales": money(gross),
        "refund_amount": money(refunded),
        "net_revenue": money(gross - refunded),
        "monthly_revenue": {key: money(value) for key, value in sorted(monthly.items())},
        "product_revenue": {key: money(value) for key, value in sorted(products.items())},
        "rejections": rejected,
    }


def render_report(summary):
    def table(items, heading):
        body = "".join(f"<tr><td>{escape(key)}</td><td>${escape(value)}</td></tr>"
                       for key, value in items.items())
        return f"<table><thead><tr><th>{heading}</th><th>Net revenue (USD)</th></tr></thead><tbody>{body}</tbody></table>"

    rejections = "".join(
        f"<tr><td>{row['data_row']}</td><td>{escape(row['order_id'])}</td><td>{escape(row['reason'])}</td></tr>"
        for row in summary["rejections"]
    )
    return f"""<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sandbox sales report</title>
<style>
body{{font:16px/1.6 system-ui,sans-serif;color:#142b3d;background:#f1f5f8;margin:0}}
main{{max-width:900px;margin:40px auto;padding:32px;background:white;border-radius:16px}}
h1{{font-size:34px;line-height:1.2}} h2{{margin-top:32px}} .label{{color:#006b79;font-weight:700}}
.metrics{{display:flex;flex-wrap:wrap;gap:16px}} .metric{{padding:16px 24px;background:#edf7f7;border-radius:10px}}
.metric strong{{display:block;font-size:27px}}table{{width:100%;border-collapse:collapse}}
th,td{{padding:10px;text-align:left;border-bottom:1px solid #dce4ea}}th{{background:#f1f5f8}}
footer{{margin-top:32px;color:#526574;font-size:14px}}
</style><main><p class="label">GKE AGENT SANDBOX · SYNTHETIC DATA</p>
<h1>Sales analysis report</h1><p>Monthly and product revenue after refunds. Invalid rows are recorded for review.</p>
<div class="metrics">
<div class="metric">Net revenue<strong>${escape(summary['net_revenue'])}</strong></div>
<div class="metric">Accepted rows<strong>{summary['accepted_rows']}</strong></div>
<div class="metric">Rejected rows<strong>{summary['rejected_rows']}</strong></div></div>
<h2>Monthly revenue</h2>{table(summary['monthly_revenue'], 'Month')}
<h2>Revenue by product</h2>{table(summary['product_revenue'], 'Product')}
<h2>Rejected input</h2><table><thead><tr><th>Data row</th><th>Order</th><th>Reason</th></tr></thead><tbody>{rejections}</tbody></table>
<footer>USD amounts use decimal arithmetic. Refunds subtract their supplied amount; this demo does not reconcile them against original orders.
The report was generated from the files in the task workspace.</footer></main></html>"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("reports"))
    args = parser.parse_args()
    with args.input.open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        if len(reader.fieldnames or []) != len(FIELDS) or set(reader.fieldnames or []) != FIELDS:
            parser.error("CSV header must contain exactly: " + ", ".join(sorted(FIELDS)))
        summary = analyze(reader)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    (args.output_dir / "report.html").write_text(render_report(summary), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
