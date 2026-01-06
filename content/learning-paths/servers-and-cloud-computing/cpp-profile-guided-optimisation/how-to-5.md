---
title: Incorporating PGO into a GitHub Actions workflow
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Build locally with make

PGO can be integrated into a `Makefile` and continuous integration (CI) systems using simple command-line instructions, as shown in the sample `Makefile` below.

{{% notice Caution %}}
PGO adds additional build steps which can increase compile time - especially for large code bases. As such, PGO is not suitable for all sections of code. You should PGO only for sections of code which are heavily influenced by run-time behavior and are performance critical. Therefore, PGO might not be ideal for early-stage development or for applications with highly variable or unpredictable usage patterns.
{{% /notice %}}

Use a text editor to create a file named `Makefile` containing the following content:

```makefile
# Simple Makefile for building and benchmarking div_bench with and without PGO

# Compiler and flags
CXX := g++
CXXFLAGS := -O3 -std=c++17
LDLIBS := -lbenchmark -lpthread

# Default target: build both binaries
.PHONY: all clean clean-gcda clean-perf run
all: div_bench.base div_bench.opt

# Build the baseline binary (no PGO)
div_bench.base: div_bench.cpp
	$(CXX) $(CXXFLAGS) $< $(LDLIBS) -o $@

# Build the PGO-optimized binary:
# Note: This target depends on the source file and cleans previous profile data first.
# It runs the instrumented binary to generate new profile data before the final compilation.
div_bench.opt: div_bench.cpp
	$(MAKE) clean-gcda # Ensure no old profile data interferes
	$(CXX) $(CXXFLAGS) -fprofile-generate $< $(LDLIBS) -o $@
	@echo "Running instrumented binary to gather profile data..."
	./div_bench.opt # Generate .gcda file
	$(CXX) $(CXXFLAGS) -fprofile-use $< $(LDLIBS) -o $@ # Compile using the generated profile
	$(MAKE) clean-perf # Optional: Clean perf data if generated elsewhere

# Remove profile data files
clean-gcda:
	rm -f ./*.gcda

# Remove perf data files (if applicable)
clean-perf:
	rm -f perf-division-*

# Remove all generated files including binaries and profile data
clean: clean-gcda clean-perf
	rm -f div_bench.base div_bench.opt

# Run both benchmarks with informative headers
run: all # Ensure binaries are built before running
	@echo "==================== Without Profile-Guided Optimization ===================="
	./div_bench.base
	@echo "==================== With Profile-Guided Optimization ===================="
	./div_bench.opt
```

You can run the following commands in your terminal:

*   `make all` (or simply `make`): Compiles both `div_bench.base` (without PGO) and `div_bench.opt` (with PGO). This includes the steps of generating profile data for the optimized version.
*   `make run`: Builds both binaries (if they don't exist) and then runs them, displaying the benchmark results for comparison.
*   `make clean`: Removes the compiled binaries (`div_bench.base`, `div_bench.opt`) and any generated profile data files (`*.gcda`).

### Build with GitHub Actions

Alternatively, you can integrate PGO into your Continuous Integration (CI) workflow using GitHub Actions. The YAML file below provides a basic example that compiles and runs the benchmark on a GitHub-hosted Ubuntu 24.04 Arm-based runner. This setup can be extended with automated tests to check for performance regressions.

```yaml
name: PGO Benchmark

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-24.04-arm

    steps:
      - name: Check out source
        uses: actions/checkout@v3

      - name: Install dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y libbenchmark-dev g++

      - name: Clean previous profiling data
        run: |
          rm -rf ./*gcda
          rm -f div_bench.base div_bench.opt

      - name: Compile base and instrumented binary
        run: |
          g++ -O3 -std=c++17 div_bench.cpp -lbenchmark -lpthread -o div_bench.base
          g++ -O3 -std=c++17 -fprofile-generate div_bench.cpp -lbenchmark -lpthread -o div_bench.opt

      - name: Generate profile data and compile with PGO
        run: |
          ./div_bench.opt
          g++ -O3 -std=c++17 -fprofile-use div_bench.cpp -lbenchmark -lpthread -o div_bench.opt

      - name: Run benchmarks
        run: |
            echo "==================== Without Profile-Guided Optimization ===================="
            ./div_bench.base
            echo "==================== With Profile-Guided Optimization ===================="
            ./div_bench.opt
            echo "==================== Benchmarking complete ===================="
````

To use this workflow, save the YAML content into a file named `pgo_benchmark.yml` (or any other `.yml` name) inside the `.github/workflows/` directory of your GitHub repository. Ensure your `div_bench.cpp` file is present in the repository root. When you push changes to the `main` branch, GitHub Actions will automatically detect this workflow file and execute the defined steps on an Arm-based runner, compiling both versions of the benchmark and running them.