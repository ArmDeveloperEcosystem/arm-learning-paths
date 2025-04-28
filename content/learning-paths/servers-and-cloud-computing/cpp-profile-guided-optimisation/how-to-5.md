---
title: (Optional) Incorporating PGO into CI system
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Building locally with Make

Since PGO can be used by simple command-line instructions, we can trivially incorporate this into a `make` file, as per the sample Makefile below if building locally. 

```makefile
# Simple Makefile for building and benchmarking div_bench with and without PGO

# Compiler and flags
CXX := g++
CXXFLAGS := -O3 -std=c++17
LDLIBS := -lbenchmark -lpthread

# Default target: build both binaries
.PHONY: all clean clean-gcda clean-perf run perf
all: div_bench.base div_bench.opt

# Build the baseline binary (no PGO)
div_bench.base: div_bench.cpp
	$(CXX) $(CXXFLAGS) $< $(LDLIBS) -o $@

# Build the PGO-optimized binary:
div_bench.opt: div_bench.cpp
	$(MAKE) clean-gcda
	$(CXX) $(CXXFLAGS) -fprofile-generate $< $(LDLIBS) -o $@
	@echo "Running instrumented binary to gather profile data..."
	./div_bench.opt
	$(CXX) $(CXXFLAGS) -fprofile-use $< $(LDLIBS) -o $@
	$(MAKE) clean-perf

# Remove all generated files
clean: clean-gcda
  rm -f div_bench.base div_bench.opt
  rm -rf ./*.gcda

# Run both benchmarks with informative headers
run: div_bench.base div_bench.opt
	@echo "==================== Without Profile-Guided Optimization ===================="
	./div_bench.base
	@echo "==================== With Profile-Guided Optimization ===================="
	./div_bench.opt
```

### Building with GitHub Actions

The `yaml` file below can serve as an basic example of integrating profile guided optimisation into your CI flow. Further tests could be to check for regressions. 

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
```