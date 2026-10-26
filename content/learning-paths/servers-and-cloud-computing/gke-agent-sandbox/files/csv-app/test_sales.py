"""Business checks for the sample and important malformed-input cases."""

import csv
from pathlib import Path
import unittest

from analyze_sales import analyze, render_report


class SalesChecks(unittest.TestCase):
    def row(self, **changes):
        return dict(order_id="T1", date="2026-01-01", product="Widget",
                    quantity="1", unit_price="0.10", status="sale") | changes

    def test_known_sample(self):
        with Path("sales.csv").open(newline="") as stream:
            result = analyze(csv.DictReader(stream))
        self.assertEqual(result["net_revenue"], "328.41")
        self.assertEqual(result["gross_sales"], "397.90")
        self.assertEqual(result["refund_amount"], "69.49")
        self.assertEqual((result["input_rows"], result["accepted_rows"], result["rejected_rows"]), (12, 9, 3))
        self.assertEqual(result["monthly_revenue"], {"2026-01": "129.46", "2026-02": "69.49", "2026-03": "129.46"})
        self.assertEqual(result["product_revenue"], {"Gadget": "148.50", "Widget": "179.91"})
        self.assertEqual([row["order_id"] for row in result["rejections"]], ["A008", "A009", "A010"])

    def test_refund_and_decimal_precision(self):
        result = analyze([self.row(quantity="3"), self.row(order_id="T2", status="refund")])
        self.assertEqual(result["net_revenue"], "0.20")
        self.assertEqual(result["refund_rows"], 1)

    def test_invalid_rows_are_accounted_for(self):
        changes = [{"quantity": ""}, {"quantity": "-1"}, {"unit_price": "NaN"},
                   {"unit_price": "-1"}, {"unit_price": "1.001"},
                   {"date": "2026-02-30"}, {"status": "unknown"}]
        result = analyze([self.row(**change) for change in changes])
        self.assertEqual(result["accepted_rows"], 0)
        self.assertEqual(result["rejected_rows"], len(changes))
        self.assertEqual(result["net_revenue"], "0.00")

    def test_duplicate_orders_are_not_double_counted(self):
        result = analyze([self.row(), self.row()])
        self.assertEqual(result["net_revenue"], "0.10")
        self.assertEqual(result["rejected_rows"], 1)

    def test_product_names_are_escaped_in_html(self):
        report = render_report(analyze([self.row(product="<script>alert(1)</script>")]))
        self.assertNotIn("<script>", report)
        self.assertIn("&lt;script&gt;", report)

    def test_malformed_column_counts_can_be_reported(self):
        result = analyze([self.row(order_id=None), self.row() | {None: ["extra"]}])
        self.assertEqual(result["rejected_rows"], 2)
        self.assertIn("Wrong number of CSV columns", render_report(result))


if __name__ == "__main__":
    unittest.main(verbosity=2)
