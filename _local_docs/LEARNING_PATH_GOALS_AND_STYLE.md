# SME2 ExecuTorch Profiling Learning Path - Goals and Style Guide

## Vision Statement

### Part 1: Building Deep Understanding and Awareness

This learning path creates strong awareness and provides a comprehensive learning journey for developers to understand the complete performance stack—from high-level model architecture down to low-level hardware instructions. Developers will learn to trace the connection between:

- **Model Architecture** → How neural network layers and operators are structured
- **Runtime Frameworks** → How ExecuTorch executes operators and manages computation
- **Kernels** → How XNNPACK kernels implement specific operations
- **SME2 Instructions** → How Arm's Scalable Matrix Extension accelerates matrix operations

**Critical Insight:** Operator-level profiling and kernel usage views are the essential connectors that bridge these layers. By understanding which operators consume the most time and which kernels are actually executing, developers can identify exactly where their models spend computation and how hardware acceleration is being utilized.

**Mindset Development:** This learning path builds a strong mindset for performance optimization by teaching developers:
- **Where to look:** Which profiling views reveal the most actionable insights
- **How to identify bottlenecks:** What patterns indicate performance issues at each layer
- **How to optimize:** What changes at each layer (model, operator, kernel, instruction) can improve performance
- **Why it matters:** How understanding the full stack enables targeted, effective optimizations

### Part 2: AI-Assisted Hands-On Learning Experience

This learning path delivers a seamless, hands-on learning experience that leverages AI coding assistants (OpenAI Codex, Claude, Cursor, GitHub Copilot) to minimize setup friction while maximizing learning value.

**For Developers:**
- **Easy Setup:** AI assistants automate 80%+ of repository setup, environment configuration, and initial pipeline execution
- **Guided Automation:** Developers know exactly where to check progress, what to validate, and how to guide their AI coding assistant to correctly complete each step
- **Learning Through Guidance:** By understanding what the AI is doing and why, developers learn the framework architecture and best practices
- **Confidence:** Developers can successfully complete model profiling work with AI assistance, then independently adapt the framework to their own models

**For AI Assistants:**
- **Clear Instructions:** Structured agentic kits provide step-by-step instructions that AI assistants can follow
- **Validation Checkpoints:** Embedded test cases and validation scripts enable AI to verify progress and catch errors
- **Error Recovery:** Troubleshooting guides help AI assistants diagnose and fix common issues
- **Iterative Refinement:** AI can test, validate, and refine its approach based on clear success criteria

**The Human-AI Partnership:** Developers maintain control and understanding while AI handles repetitive setup and execution tasks. Developers learn by guiding the AI, checking its work, and understanding the results—creating a collaborative learning experience that is both efficient and educational.

## Source Code Repository

### Reference Repository (Not Accessible to Users)

**Original Location:** `/Users/jaszhu01/Local/Github/sme2_executorch`

This is the reference implementation that demonstrates the complete profiling framework. However, **developers using this learning path will not have access to this repository**.

### Learning Path Repository (To Be Created)

**Location:** `content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/`

We must create a new repository structure within the learning path folder that:
- Contains all necessary scripts and tools for profiling
- Works within the constraints of the learning path directory structure
- Provides the same functionality as the reference implementation
- Can be downloaded and used by developers following the learning path

**Key Constraints:**
- Must fit within learning path directory structure
- Scripts must be standalone and downloadable from public GitHub repo
- Cannot rely on external repository access (beyond the public learning paths repo)
- Must be self-contained and complete

**Script Distribution:**
Since scripts are in the public GitHub repo [arm-learning-paths](https://github.com/ArmDeveloperEcosystem/arm-learning-paths), developers use **GitHub sparse checkout** to get only the SME2 profiling directory:

```bash
git clone --filter=blob:none --sparse https://github.com/ArmDeveloperEcosystem/arm-learning-paths.git sme2-profiling
cd sme2-profiling
git sparse-checkout init --cone
git sparse-checkout set content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling
```

**Fallback:** Individual scripts can be downloaded via `wget` with raw GitHub URLs if only a single script is needed.

**Required Components (what we actually ship in the learning path folder):**

```
sme-executorch-profiling/
├── 01-...08-*.md               # Website learning path pages
├── 09-agentic-kits.md          # Website page explaining the agent toolkits
│
├── scripts/                    # Minimal scripts with real value
│   ├── setup_repo.sh           # Create venv + clone/update ExecuTorch main + install
│   ├── build_runners.sh        # Build runners (macOS always; Android if ANDROID_NDK set)
│   ├── export_model.py         # Export reference model to .pte + .etrecord
│   ├── mac_pipeline.py         # Host pipeline → runs/*/manifest.json includes ExecuTorch SHA
│   ├── android_pipeline.py     # Device pipeline → push/run/pull ETDump, capture device info
│   ├── analyze_results.py      # Inspector-based analysis (operator categories + kernel hints)
│   ├── validate_setup.py       # Setup validation + print ExecuTorch git SHA
│   ├── validate_results.py     # Output layout validation
│   └── run_quick_test.py       # Smoke test (small toy model)
│
├── configs/
│   ├── templates/
│   │   ├── mac_template.json
│   │   └── android_template.json
│   └── examples/
│       ├── mac_mobilenet_fp16.json
│       └── android_mobilenet_fp16.json
│
├── images/                     # Web-visible visuals (charts + stack diagram)
└── test-cases/                 # Offline sanity tests (do not require ExecuTorch build)
```

**Design Principles:**
- Self-contained: All necessary code in learning path directory
- Downloadable: Scripts accessible via sparse checkout (primary) or individual wget (fallback)
- Validated: Test cases ensure functionality
- Documented: Clear usage in learning path pages
- Efficient: Users don't need to download entire learning paths repository

## Primary Goals

### 1. Enable Profiling Setup (< 30 minutes)
**Success Criteria:**
- Clone/setup repository and environment in < 30 minutes
- All dependencies installed correctly
- ExecuTorch built and configured
- Runners built (Mac, optionally Android)
- Validation script passes all checks
- AI assistant can automate 80%+ of setup

**Implementation:**
- Clear step-by-step instructions
- Automated setup scripts
- Validation at each stage
- Clear error messages with fixes
- Support for both manual and AI-assisted setup

### 2. Enable Pipeline Understanding
**Success Criteria:**
- Developers can explain the pipeline flow
- Understand configuration structure
- Know what each pipeline stage does
- Understand output structure

**Implementation:**
- Visual diagrams of pipeline flow
- Clear explanation of each stage
- Example configurations with comments
- Architecture overview

### 3. Enable Pipeline Execution
**Success Criteria:**
- Run complete Mac pipeline successfully (workflow + profiling literacy)
- Generate valid configuration files
- Execute profiling experiments
- Compare “sme2_on vs sme2_off” configurations
- Run Android pipeline on SME2-capable hardware to observe real SME2 acceleration (optional but the only way to see SME2 deltas)

**Implementation:**
- One-command execution where possible
- Clear configuration examples
- Progress indicators
- Error handling and recovery
- Results clearly organized

### 4. Enable Results Analysis
**Success Criteria:**
- Understand E2E latency metrics
- Interpret operator-level analysis
- Understand kernel usage information
- Compare performance across configurations
- Generate insights from results

**Implementation:**
- Clear explanation of metrics
- Example results with annotations
- Visualization where helpful
- Comparison tools
- Report generation

### 5. Enable Model Onboarding
**Success Criteria:**
- Add new model to registry
- Export custom model
- Run profiling on custom model
- Understand adaptation requirements

**Implementation:**
- Clear onboarding guide
- Template/model skeleton
- Step-by-step instructions
- Validation at each step
- Examples and best practices

## Success Criteria

### For Human Developers
1. Setup time: < 30 minutes
2. First pipeline: < 1 hour from setup
3. Results understanding: Can interpret results and identify performance characteristics
4. Model adaptation: Can add their own model (advanced users) within 2-3 hours
5. Confidence: Feel confident using the framework independently

**Clarification (important):**
- macOS Apple Silicon is the **default “learn the workflow + operator profiling” path**.
- SME2 is Armv9: **to validate SME2 acceleration and `__neonsme2` kernel paths, users need an SME2-capable Android device**.

### For AI-Assisted Development
1. Automation rate: AI can automate 80%+ of setup and execution
2. Config generation: AI can generate valid configuration files
3. Error recovery: AI can troubleshoot common issues
4. Validation: AI can validate setup and results
5. Adaptation: AI can help adapt framework to new models

### For Learning Path Quality
1. Clarity: All instructions are clear and unambiguous
2. Completeness: All necessary information is provided
3. Accuracy: All commands and examples work as documented
4. Maintainability: Content is easy to update as framework evolves
5. Accessibility: Works for both beginners and advanced users

## Key User Experience Requirements

### 1. Clarity and Simplicity
- Use simple, direct language
- Avoid jargon without explanation
- Provide context for each step
- Show expected outputs
- Include visual aids where helpful

### 2. Progressive Disclosure
- Begin with basic Mac pipeline
- Add Android as optional advanced topic
- Model onboarding as advanced section
- Provide quick start for experienced users
- Detailed explanations for beginners

### 3. Validation and Feedback
- Validation scripts at each stage
- Clear success/failure indicators
- Expected outputs shown
- Error messages with fixes
- Progress indicators

### 4. Error Recovery
- Common error documentation
- Troubleshooting guides
- Clear error messages
- Recovery steps
- Support resources

### 5. Flexibility
- Manual step-by-step instructions
- Automated scripts
- AI-assisted setup
- Configuration templates
- Customization options

### 6. Time Efficiency
- Quick start path for experienced users
- Automated setup scripts
- Parallel operations where possible
- Clear time estimates
- Skip optional steps easily

## Content Structure for Different Learning Styles

### Supporting Multiple User Adaptation Behaviors

The learning path must accommodate different user learning styles: comprehensive readers who prefer full context before hands-on work, and hands-on explorers who prefer to jump in and learn by doing.

#### Learning Style 1: Comprehensive Readers First
**Needs:**
- Complete conceptual overview before practical steps
- Detailed explanations of why each step matters
- Architecture and design principles explained upfront
- Full context about the performance stack

**Content Support:**
- Clear learning path sequence with logical flow
- Comprehensive _index.md explaining the full journey
- Conceptual sections before practical steps
- "Why" before "how" explanations
- Detailed reference materials available upfront

#### Learning Style 2: Hands-On Explorers
**Needs:**
- Quick start path that gets them running immediately
- Minimal reading required to start
- Clear commands and scripts to execute
- Validation and feedback to guide exploration

**Content Support:**
- Prominent "Quick Start" section (get running in < 10 minutes)
- Jump-to sections with direct links to hands-on steps
- Script-first approach with automated scripts
- Inline help available when needed, not required upfront
- Just-in-time learning with detailed explanations available but not required

### Dual-Path Content Structure

**Path 1: Comprehensive Learning Path (Sequential)**
- Sequential progression through all pages
- Each page builds on previous
- Detailed explanations included
- Conceptual understanding emphasized

**Path 2: Quick Start Path (Exploratory)**
- Non-linear exploration
- Minimal reading to start
- Scripts and automation emphasized
- Learn-by-doing approach

### Content Organization Principles

1. **Progressive Disclosure:** Essential information visible immediately, deeper explanations on demand
2. **Multiple Entry Points:** Quick Start, Comprehensive Guide, Reference, Troubleshooting
3. **Self-Contained Sections:** Each page can stand alone with clear prerequisites
4. **Flexible Navigation:** Easy to jump, skip, or backtrack between sections
5. **Contextual Help:** Inline explanations, tooltips, examples, FAQ-style answers

### Page Structure Template

Each learning path page should include:

1. **Quick Summary** (for explorers)
   - What you'll do in this section
   - Time estimate
   - Prerequisites checklist
   - Quick start command/script

2. **Detailed Explanation** (for comprehensive readers)
   - Why this step matters
   - How it fits in the bigger picture
   - Detailed concepts and architecture
   - Best practices and considerations

3. **Hands-On Steps** (for both)
   - Clear, executable commands
   - Expected outputs
   - Validation checkpoints
   - Error handling

4. **Learn More** (optional, for curious explorers)
   - Deeper explanations
   - Related concepts
   - Advanced topics
   - Additional resources

## Website Delivery Goals

### What Users Should Get

1. **Clear Learning Path:** Well-structured, sequential learning path with overview, prerequisites, step-by-step instructions, examples, and next steps
2. **Practical Examples:** Working examples (SqueezeSAM primary), configuration examples, result interpretation examples, model onboarding example
3. **Downloadable Resources:** Setup scripts, configuration templates, validation scripts, analysis tools
4. **Visual Aids:** Pipeline architecture diagrams, result interpretation guides, performance comparison charts, workflow diagrams
5. **Reference Materials:** Configuration reference, command reference, troubleshooting guide, FAQ section
6. **Agentic Kits (explained on the website, used locally):**
   - The website includes a single page that explains what the kits are and how to use them.
   - The kit files live under `agentic-kits/` for sparse-checkout users, but are **not published as website pages**.

### Website User Journey

1. Discovery → 2. Overview → 3. Prerequisites → 4. Setup → 5. Execution → 6. Analysis → 7. Adaptation → 8. Success

## Agent and Script Goals

### What Agents Should Enable

1. **Automated Setup:** Clone repository, create virtual environment, install ExecuTorch, install dependencies, build runners, validate setup
2. **Configuration Generation:** Understand user requirements, generate appropriate configuration, validate syntax, suggest optimizations
3. **Pipeline Execution:** Run pipeline with appropriate config, monitor progress, handle errors, validate results
4. **Results Analysis:** Read and parse result files, extract key metrics, compare configurations, identify performance characteristics
5. **Troubleshooting:** Recognize common error patterns, suggest fixes, validate fixes worked, escalate complex issues

### What Scripts Should Provide

1. **Setup Scripts:** Check prerequisites, create virtual environment, install dependencies, validate installation, provide clear feedback
2. **Validation Scripts:** Check all prerequisites, verify installations, validate configurations, check file existence, validate results
3. **Configuration Templates (preferred over generators):** Template JSONs in `configs/templates/` that humans/agents edit directly; minimal scripts only when they add unique value.
4. **Test Scripts:** Quick smoke tests, comprehensive test suites, clear test results, failure diagnostics, performance benchmarks

## Developer Adaptation Goals

### Enabling Model Onboarding
- Clear step-by-step guide with template/model skeleton
- Minimal code changes required
- Automated validation at each step
- Error messages with fixes
- Examples and best practices

### Enabling Workflow Integration
- CI/CD integration: Scriptable execution, configurable outputs, automated reporting
- Custom analysis: Modular analysis tools, extensible pipeline, custom report generation
- Tool integration: Standard output formats, export capabilities, API access

## Style Guidelines

### Writing Style
- **Tone:** Professional but approachable, confident, supportive, concise
- **Language:** Clear and simple, technical when needed with explanation, consistent terminology, action-oriented
- **Structure:** Logical flow, progressive complexity, clear sections, scannable

### Code Examples
- **Format:** Complete, commented, realistic, tested
- **Presentation:** Syntax highlighting, line numbers for longer examples, expected output shown, error handling when relevant

### Visual Aids
- **When to Use:** Complex concepts (diagrams), workflows (flowcharts), results (charts), UI interactions (screenshots)
- **Style:** Clear and readable, consistent, annotated, accessible (alt text)

## Quality Standards

- **Accuracy:** All commands work as written, all examples tested, all links valid
- **Completeness:** All necessary steps included, all prerequisites listed, all dependencies documented, all edge cases addressed
- **Maintainability:** Content easy to update, structure clear, dependencies documented, version information included
- **Accessibility:** Content readable, code accessible, visuals have alt text, navigation clear

## Success Metrics

### Quantitative
- Setup time: < 30 minutes
- First pipeline: < 1 hour from setup
- Model onboarding: < 3 hours for advanced users
- Error rate: < 10% encounter blocking errors
- Completion rate: > 70% complete the learning path

### Qualitative
- User satisfaction: Users feel confident using the framework
- Clarity: Users understand all steps
- Support requests: Minimal support needed
- Feedback: Positive feedback on content quality
- Adoption: Users successfully profile their models

## Conclusion

This learning path should empower developers to quickly set up the profiling environment, easily run profiling pipelines, effectively analyze performance results, and successfully adapt the framework to their needs—whether using traditional step-by-step guidance or AI-assisted automation.
