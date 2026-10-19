"""Deliberately faulty saved first attempt: assumes every row is valid."""

import csv
from decimal import Decimal
from pathlib import Path
import sys


def main():
    total = Decimal("0")
    with Path(sys.argv[1]).open(newline="") as stream:
        for row in csv.DictReader(stream):
            # Missing quantities crash this attempt; refunds also need a sign.
            total += int(row["quantity"]) * Decimal(row["unit_price"])
    print(f"Revenue: {total:.2f}")


if __name__ == "__main__":
    main()
