# Arm Learning Paths - AI Assistant Guidelines

## Overview
Create educational content for Arm architecture, development tools, and cross-platform performance analysis. This Hugo-based documentation follows structured learning paths with progressive skill development for developers and performance engineers.

## Content Structure & Organization

### File Hierarchy
- **`_index.md`**: Learning path overview with completion time, objectives, prerequisites, and taxonomy metadata
- **Sequential files (1-xxx.md, 2-xxx.md)**: Step-by-step tutorials ordered by `weight` parameter
- **`_next-steps.md`**: Standardized conclusion (weight: 21, marked FIXED - never modify)

### Required Frontmatter Structure
Every content file must include:
```yaml
---
title: "Descriptive Title"
weight: [number]  # Navigation order
layout: learningpathall  # Required Hugo template
---
```

Main index files require additional metadata:
```yaml
learning_path_main_page: "yes"  # Index page identifier
shared_path: true              # Cross-category content
shared_between:               # Target categories
    - servers-and-cloud-computing
    - automotive
```

### Content Quality Standards
- **Precision**: Use exact PMU counter names, validated tool commands, and verified architecture specifications
- **Cross-platform coverage**: Provide equivalent Arm and x86 commands, tools, and methodologies
- **Hands-on examples**: Include functional code samples, shell commands, and actual output results
- **Installation links**: Reference tools using `/install-guides/[tool-name]/` format

## Performance Analysis Implementation

### Essential Tools and Commands
- **Linux Perf**: x86 top-down analysis using `perf stat --topdown` and `-M topdownl1`
- **Arm topdown-tool**: Neoverse-specific analysis with `topdown-tool -m [metric-name]`
- **Compilation**: GCC/Clang with performance flags: `gcc -O3 -march=native`
- **Process isolation**: CPU pinning with `taskset -c 1` for measurement consistency

### Performance Code Patterns
Create benchmark examples that demonstrate specific bottlenecks:
```c
// Prevent compiler optimizations with volatile
volatile double result = 1.23456789;

// Document performance characteristics in comments
// Creates dependency chain showing backend-bound behavior
for (long long i = 0; i < iterations; ++i) {
    result /= 1.00000001;  // High-latency floating-point operation
}
```

### Command Documentation Format
Structure commands with clear execution context:
```console
taskset -c 1 perf stat -C 1 --topdown ./benchmark 1000000000
```

Include representative output with performance metrics:
```output
Performance counter stats for 'CPU(s) 1':
    retiring    bad speculation    frontend bound    backend bound
    8.5%        0.0%              0.1%              91.4%
```

## Architecture-Specific Implementation

### Intel x86 Top-Down Methodology
- **Hierarchical structure**: 4-level analysis framework (Level 1 through Level 4)
- **Core events**: `UOPS_RETIRED.RETIRE_SLOTS`, `IDQ_UOPS_NOT_DELIVERED.CORE`, `CPU_CLK_UNHALTED.THREAD`
- **Pipeline accounting**: 4 issue slots per cycle on typical Intel cores
- **Analysis depth**: Supports drill-down from categories to specific microarchitecture events

### Arm Neoverse Top-Down Framework
- **Two-stage approach**: Stage 1 (Topdown categories) + Stage 2 (Resource effectiveness)
- **Key counters**: `STALL_SLOT_BACKEND`, `STALL_SLOT_FRONTEND`, `OP_RETIRED`, `OP_SPEC`
- **Pipeline slots**: 8 rename slots per cycle for bandwidth calculations
- **Resource groups**: Cache effectiveness, operation mix, cycle accounting metrics

### Cross-Architecture Comparison Tables
Document equivalent functionality using structured comparisons:
- Map corresponding performance events between architectures
- Show formula variations for identical metrics
- Provide parallel tool commands for both Intel and Arm platforms

## Content Development Guidelines

### Frontmatter Requirements
- Never modify `### FIXED, DO NOT MODIFY` sections in any file
- Preserve `weight` values that determine navigation sequence
- Maintain `layout: learningpathall` for all content files
- Keep taxonomy metadata intact: `armips`, `operatingsystems`, `tools_software_languages`

### Technical Content Standards
- Validate all PMU counter names and performance formulas before publication
- Test command examples on target hardware platforms
- Update tool version references and installation procedures
- Cross-reference related learning paths in `further_reading` sections

### SEO and Discoverability Optimization
- Use descriptive titles that include key terms: "Arm Neoverse", "x86 performance", "top-down analysis"
- Structure content with clear headings for snippet extraction
- Include specific tool names and version numbers in content
- Provide complete, executable command examples with expected outputs

## Content Creation Tasks

### Adding Performance Analysis Examples
1. Create realistic workloads that demonstrate specific performance bottlenecks
2. Provide equivalent measurement commands for both Arm and x86 architectures
3. Document compiler optimization effects and mitigation strategies
4. Include quantitative results showing expected performance category distributions

### Updating Tool Documentation
- Verify current software versions and installation requirements
- Test command-line syntax for compatibility across Linux distributions
- Update example outputs to reflect current tool formatting
- Maintain standard link format: `/install-guides/[tool-name]/`

### Cross-Platform Content Validation
- Test all examples on both Arm Neoverse and Intel x86 systems
- Confirm PMU event availability across different processor generations
- Validate tool compatibility with current Linux kernel versions
- Document any architecture-specific limitations or requirements