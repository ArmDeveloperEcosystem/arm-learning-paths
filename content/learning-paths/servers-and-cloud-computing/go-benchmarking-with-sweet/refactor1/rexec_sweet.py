#!/usr/bin/env python3
"""
Entry point for the rexec_sweet tool.
"""
import sys
import os

def main():
    try:
        from rexec_sweet.cli import main as cli_main
        sys.exit(cli_main())
    except ImportError as e:
        print(f"Error importing modules: {e}")
        print("\nTry running with PYTHONPATH set:")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        print(f"PYTHONPATH={script_dir} python {os.path.join(script_dir, 'rexec_sweet.py')}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()