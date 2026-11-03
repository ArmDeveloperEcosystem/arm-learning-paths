"""Decide whether a release can proceed from a local test-results file."""
import json
import sys


def check_release(results):
    counts = {
        status: sum(test["status"] == status for test in results["tests"])
        for status in ("passed", "failed", "skipped")
    }
    return {**counts, "ready": counts["passed"] > 0}


if __name__ == "__main__":
    with open(sys.argv[1]) as source:
        result = check_release(json.load(source))
    print(json.dumps(result))
    sys.exit(1 if result["ready"] else 0)
