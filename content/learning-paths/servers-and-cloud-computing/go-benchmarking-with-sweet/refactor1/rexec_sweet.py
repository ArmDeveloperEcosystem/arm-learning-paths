#!/usr/bin/env python3

import sys
import traceback

try:
    from rexec_sweet.cli import main
    sys.exit(main())
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("\nTry running with PYTHONPATH set:")
    print("PYTHONPATH=/Users/gercoh01/Library/CloudStorage/OneDrive-Arm/customer/arm-learning-paths/content/learning-paths/servers-and-cloud-computing/go-benchmarking-with-sweet/refactor1 python refactor1/rexec_sweet.py")
    traceback.print_exc()
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    traceback.print_exc()
    sys.exit(1)