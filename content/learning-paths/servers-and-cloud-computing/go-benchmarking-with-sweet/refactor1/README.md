# rexec_sweet - Remote Sweet Benchmark Execution Tool

A tool for running Go benchmarks using Sweet on remote GCP instances and comparing results.

## Installation

```bash
# Install from the project directory
pip install -e .
```

## Usage

```bash
# Run the tool
rexec-sweet

# Run with specific benchmark and instances
rexec-sweet --benchmark markdown --instance1 c4-96 --instance2 c4-64

# Generate report from existing benchstat file
rexec-sweet --report results/benchstat.results --output-dir ./my-report
```

## Project Structure

```
rexec_sweet/
├── __init__.py          # Package exports
├── benchmark_runner.py  # Benchmark execution logic
├── benchstat_report.py  # Report generation
├── cli.py               # Command-line interface
├── config.py            # Configuration management
├── gcp_utils.py         # GCP interaction utilities
└── visualization.py     # Data visualization
```

## Requirements

- Python 3.8+
- Google Cloud SDK
- Go with benchstat tool installed
- Sweet benchmarking tool