# SME2 ExecuTorch Profiling Learning Path - Implementation Plan

## Executive Summary

This learning path enables developers to profile ExecuTorch models with SME2 acceleration through two complementary approaches:

1. **Deep Understanding:** Build awareness of the complete performance stack (Model Architecture → Runtime Frameworks → Kernels → SME2 Instructions) and develop optimization mindset
2. **AI-Assisted Hands-On Experience:** Seamless setup and execution through AI coding assistants, with developers guiding and validating the process

**Key Innovation:** Dual-path content structure supporting both comprehensive readers (who prefer full context first) and hands-on explorers (who prefer to jump in and learn by doing).

## Learning Path Goals

### Primary Goals
1. **Setup** (< 30 minutes): Enable developers to set up the profiling repository and environment
2. **Understanding**: Help developers understand the profiling pipeline architecture and performance stack
3. **Execution**: Enable running profiling pipelines on Mac (primary) and Android (optional)
4. **Analysis**: Enable interpretation of results (E2E latency, operator-level, kernel usage)
5. **Model Onboarding**: Enable adding new models to the profiling framework

### Success Criteria
- ✅ Setup in < 30 minutes
- ✅ Run complete Mac pipeline successfully
- ✅ Interpret performance results at multiple levels
- ✅ Understand performance stack connections
- ✅ Add own model (advanced users) within 2-3 hours
- ✅ AI assistant can automate 80%+ of setup and execution

## Learning Path Structure

### File Organization

```
content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/
├── _index.md                          # Main landing page (dual paths)
├── _next-steps.md                     # Auto-generated (don't modify)
│
├── 01-prerequisites.md                 # System requirements, hardware
├── 02-setup-environment.md            # Clone, venv, install ExecuTorch
├── 03-build-runners.md                # Build Mac/Android runners
├── 04-export-model.md                 # Export a model to .pte format
├── 05-run-mac-pipeline.md             # Run profiling on Mac
├── 06-analyze-results.md              # Interpret results (E2E, operator, kernel)
├── 07-android-pipeline.md             # Android profiling (optional)
├── 08-onboard-model.md                # Add new model (advanced)
│
├── scripts/                           # Standalone scripts (via sparse checkout)
│   ├── setup_repo.sh                  # Automated repo setup
│   ├── validate_setup.py              # Setup validation
│   ├── export_model.py                # Model export utility
│   ├── mac_pipeline.py                # Mac profiling pipeline
│   ├── android_pipeline.py            # Android profiling pipeline
│   ├── generate_config.py             # Config file generator
│   ├── analyze_results.py             # Results analysis
│   └── run_quick_test.py              # Quick smoke test
│
├── configs/                           # Configuration templates
│   ├── mac_template.json              # Mac config template
│   └── android_template.json          # Android config template
│
├── agentic-kits/                      # AI-assistant-friendly docs
│   ├── README.md                      # Overview of agentic kits
│   ├── setup-agent.md                 # Automated setup instructions
│   ├── pipeline-agent.md              # Automated pipeline execution
│   ├── validation-agent.md            # Test cases and validation
│   └── troubleshooting-agent.md       # Common issues and fixes
│
└── test-cases/                        # Test cases for validation
    ├── test_model_export.py
    ├── test_pipeline_execution.py
    ├── test_results_validation.py
    └── test_kernel_analysis.py
```

**Script Distribution (prefer fewer commands, keep wget-able):**

- **Default (sparse checkout, keeps repo layout intact):**
  ```bash
  git clone --filter=blob:none --sparse https://github.com/ArmDeveloperEcosystem/arm-learning-paths.git sme2-profiling
  cd sme2-profiling
  git sparse-checkout init --cone
  git sparse-checkout set content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling
  cd content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling
  ```
  Use this path when the learner wants the full kit (scripts/configs/agentic-kits/tests) without the whole repo.

- **Bundle download (faster than many single wgets):**
  Provide a one-liner to fetch a tarball/zip of the learning-path directory (e.g., `curl -L https://github.com/ArmDeveloperEcosystem/arm-learning-paths/archive/refs/heads/main.tar.gz | tar -xz --strip-components=...`). Document the exact strip depth once the final path is locked. This lets users grab everything in one go even without git.

- **Per-script wget (minimal path):**
  Still document raw GitHub links for any script referenced inline so learners (or agentic kits) can fetch a single file when needed:
  ```bash
  wget https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/scripts/setup_repo.sh
  ```

## Detailed Content Plan

### 1. _index.md (Main Landing Page)

**Title:** "Profile ExecuTorch Models with SME2 Acceleration"

**Content Structure:**
1. **Overview** (for everyone)
   - What you'll learn: Understanding performance stack, profiling models, analyzing results
   - Why it matters: Connect model architecture to hardware acceleration
   - Learning objectives (5-6 key points)

2. **Two Learning Paths** (clear choice)
   - **Path 1: Comprehensive Learning** → Read all details first, understand full context
   - **Path 2: Quick Start** → Jump into hands-on work, learn by doing

3. **Prerequisites** (for everyone)
   - System requirements (macOS with Apple Silicon)
   - Software prerequisites (Python 3.9+, CMake 3.29+, Git)
   - Time estimates (60-90 minutes total)

4. **Learning Path Structure** (for comprehensive readers)
   - Full sequence explained
   - What each section covers
   - How sections connect

5. **Quick Start** (for explorers)
   - Get running in 10 minutes
   - Essential commands only
   - Link to detailed explanations

**Key Sections:**
- Performance stack overview (Model → Runtime → Kernels → SME2)
- Why operator-level profiling and kernel views matter
- What you'll build/learn
- Links to agentic kits for AI-assisted setup

### 2. 01-prerequisites.md

**Content Structure:**
1. **Quick Summary** (for explorers)
   - What you need
   - Time: 5 minutes
   - Quick verification command

2. **Detailed Requirements** (for comprehensive readers)
   - System requirements (macOS with Apple Silicon)
   - Software prerequisites with versions
   - Hardware requirements
   - Optional: Android device requirements

3. **Verification Steps** (for both)
   - Commands to check each requirement
   - Expected outputs
   - What to do if requirements not met

**Agentic Kit Integration:**
- Validation script: `python scripts/validate_setup.py --prerequisites`
- Clear pass/fail criteria
- Actionable error messages

### 3. 02-setup-environment.md

**Content Structure:**
1. **Quick Setup** (for explorers)
   ```bash
   # Get all scripts using sparse checkout
   git clone --filter=blob:none --sparse https://github.com/ArmDeveloperEcosystem/arm-learning-paths.git sme2-profiling
   cd sme2-profiling
   git sparse-checkout init --cone
   git sparse-checkout set content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling
   cd content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling
   
   # Run setup
   chmod +x scripts/setup_repo.sh
   ./scripts/setup_repo.sh
   ```
   - What it does: [Brief explanation]
   - Time: ~15 minutes
   - Learn more: [Link to detailed explanation]
   
   **Note:** If you only need a single script, you can download it individually:
   ```bash
   wget https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/scripts/setup_repo.sh
   ```

2. **Understanding the Setup** (for comprehensive readers)
   - Why each step matters
   - Architecture overview
   - Dependencies explained

3. **Step-by-Step Setup** (for both)
   - Clone/download repository structure
   - Create Python virtual environment
   - Install ExecuTorch from source
   - Install project dependencies
   - Verify installation

4. **Validation** (for both)
   ```bash
   python scripts/validate_setup.py
   ```
   - Expected output shown
   - What each check validates

**Scripts:**
- `setup_repo.sh` - Automated setup (downloadable)
- `validate_setup.py` - Validation after setup

**Agentic Kit:**
- Step-by-step instructions with expected outputs
- Error handling guidance
- Validation checkpoints

### 4. 03-build-runners.md

**Content Structure:**
1. **Quick Build** (for explorers)
   - One-command build script
   - Time estimate
   - Verification command

2. **Understanding Runners** (for comprehensive readers)
   - What ExecuTorch runners are
   - Why we need different builds (SME2 ON/OFF)
   - Runner configurations explained

3. **Build Steps** (for both)
   - Build Mac runners (SME2 ON/OFF)
   - Build Android runners (optional)
   - Verify runners exist
   - Understanding different runner configurations

**Scripts:**
- Reference to build scripts (downloadable)
- Validation script to check runners

**Agentic Kit:**
- Automated build instructions
- Build verification steps
- Time estimates for each build

### 5. 04-export-model.md

**Content Structure:**
1. **Quick Export** (for explorers)
   - Download export script
   - Run with example model
   - Verify output

2. **Understanding Model Export** (for comprehensive readers)
   - What .pte files are
   - Export process explained
   - Data types and quantization

3. **Export Steps** (for both)
   - Export SqueezeSAM example model
   - Export different data types (FP16, INT8)
   - Verify exported models
   - Model registration (for custom models)

**Scripts:**
- `export_model.py` (downloadable)
- Test export script

**Agentic Kit:**
- Automated export instructions
- Validation of exported models
- Test cases for model export

### 6. 05-run-mac-pipeline.md

**Content Structure:**
1. **Quick Run** (for explorers)
   - Download pipeline script
   - Generate config
   - Run pipeline
   - Check results

2. **Understanding the Pipeline** (for comprehensive readers)
   - Pipeline architecture
   - How profiling works
   - Configuration structure
   - Expected outputs

3. **Pipeline Steps** (for both)
   - Create configuration file
   - Run Mac profiling pipeline
   - Understand pipeline output
   - SME2 ON vs OFF comparison

**Scripts:**
- `mac_pipeline.py` (downloadable)
- `generate_config.py` - Example config generator
- Quick test script

**Agentic Kit:**
- Automated pipeline execution
- Config file generation
- Expected outputs and validation

### 7. 06-analyze-results.md

**Content Structure:**
1. **Quick Analysis** (for explorers)
   - Where to find results
   - Key files to check
   - Quick interpretation

2. **Understanding Results** (for comprehensive readers)
   - Result structure explained
   - Performance stack connection
   - How to identify bottlenecks
   - Optimization mindset

3. **Analysis Steps** (for both)
   - E2E latency analysis
   - Operator-level analysis (connects model to runtime)
   - Kernel usage analysis (connects runtime to hardware)
   - Performance comparison
   - Generating insights

**Key Focus:**
- Emphasize how operator-level and kernel views connect the performance stack
- Show where bottlenecks appear at each layer
- Demonstrate optimization mindset

**Scripts:**
- `analyze_results.py` (downloadable)
- Report generation helpers

**Agentic Kit:**
- Automated analysis instructions
- Result validation
- Expected metrics ranges

### 8. 07-android-pipeline.md (Optional)

**Content Structure:**
1. **Quick Android Setup** (for explorers)
   - ADB connection
   - Deploy runners
   - Run pipeline

2. **Android-Specific Details** (for comprehensive readers)
   - Android setup requirements
   - CPU affinity configuration
   - Android-specific analysis

3. **Android Steps** (for both)
   - Android runner deployment
   - Running Android pipeline
   - CPU affinity configuration
   - Android-specific analysis

**Scripts:**
- `android_pipeline.py` (downloadable)
- ADB validation

**Agentic Kit:**
- Android setup automation
- Device connection validation

### 9. 08-onboard-model.md (Advanced)

**Content Structure:**
1. **Quick Onboarding** (for explorers)
   - Template download
   - Fill in model details
   - Register and test

2. **Model Onboarding Process** (for comprehensive readers)
   - Architecture overview
   - Registration process
   - Best practices

3. **Onboarding Steps** (for both)
   - Model registration process
   - Creating model class
   - Export configuration
   - Testing new model
   - Adding to pipeline

**Scripts:**
- Model template generator (downloadable)
- Registration helper

**Agentic Kit:**
- Model onboarding automation
- Template generation

## Agentic Kits Design

### Purpose
Enable AI coding assistants (OpenAI Codex, Claude, Cursor, Copilot) to:
1. Automatically set up the repository
2. Configure the environment
3. Run the pipeline
4. Validate results
5. Troubleshoot issues

### Structure

#### setup-agent.md
**Format:** Structured markdown with clear sections

```markdown
# Automated Setup Agent Instructions

## Objective
Set up the SME2 ExecuTorch profiling repository and environment.

## Prerequisites Check
- Command: `python3 --version`
- Expected: Python 3.9 or higher
- Validation: Check version number

## Setup Steps

### Step 1: Get Scripts

**Sparse Checkout (Primary Method)**
- Command: `git clone --filter=blob:none --sparse https://github.com/ArmDeveloperEcosystem/arm-learning-paths.git sme2-profiling`
- Expected output: Repository cloned
- Validation: `ls sme2-profiling`
- Next: `cd sme2-profiling && git sparse-checkout init --cone && git sparse-checkout set content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling`
- Validation: `ls content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/scripts`

**Fallback: Individual Script (If only one script needed)**
- Command: `wget https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/scripts/<script_name>`
- Use only when a single script is needed or git is not available

### Step 2: Run Setup Script
- Command: `cd scripts && chmod +x setup_repo.sh && ./setup_repo.sh`
- Expected output: [Specific success messages]
- Validation: `python scripts/validate_setup.py`

[... more steps with clear validation ...]

## Validation
Run: `python scripts/validate_setup.py`
Expected: All checks pass with ✅

## Success Criteria
- [ ] Scripts directory in place
- [ ] Virtual environment active
- [ ] ExecuTorch installed
- [ ] Dependencies installed
- [ ] Validation script passes all checks
```

#### pipeline-agent.md
**Format:** Pipeline execution instructions

```markdown
# Automated Pipeline Execution

## Objective
Run the complete profiling pipeline for a model.

## Prerequisites
- Setup complete (run validation first)
- Scripts downloaded (via sparse checkout or download_scripts.sh)
- Runners built
- Model exported

## Pipeline Steps
1. Verify scripts available
   - Command: `ls scripts/mac_pipeline.py`
   - Validation: Script exists and is executable
   - If missing: Use sparse checkout to get all scripts, or wget for individual script

2. Generate configuration
   - Command: `python scripts/generate_config.py --model <path> --output <dir>`
   - Expected output: config.json created
   - Validation: JSON is valid, required fields present

3. Run pipeline
   - Command: `python scripts/mac_pipeline.py --config config.json`
   - Expected outputs: [List of result files]
   - Validation: All result files exist, metrics are reasonable

## Test Cases
[Embedded test cases that can be run to validate]
```

#### validation-agent.md
**Format:** Test cases and validation

```markdown
# Validation and Test Cases

## Setup Validation
- Test: `python scripts/validate_setup.py`
- Expected: All checks pass
- Failure: [What to check if fails]

## Model Export Validation
- Test: `python test-cases/test_model_export.py`
- Expected: Model exports successfully, .pte file valid
- Failure: [Common issues and fixes]

## Pipeline Execution Validation
- Test: `python test-cases/test_pipeline_execution.py`
- Expected: Pipeline completes, results generated
- Failure: [Troubleshooting steps]

## Results Validation
- Test: `python test-cases/test_results_validation.py`
- Expected: All metrics present and reasonable
- Failure: [What to check]

## Expected Metrics Ranges
- E2E latency: [Range for typical models]
- Operator timing: [Expected distribution]
- Kernel usage: [Expected patterns]
```

### Key Features of Agentic Kits

1. **Clear Success Criteria**: Each step has pass/fail criteria
2. **Expected Outputs**: Show what good output looks like
3. **Error Handling**: Common errors and fixes
4. **Validation Checkpoints**: Automated checks at each stage
5. **Test Cases**: Embedded test cases for verification
6. **Iterative Refinement**: Instructions for AI to refine approach

## Test Cases and Validation

### Test Suite Structure

#### test_model_export.py
```python
"""Test model export functionality."""
def test_export_fp16():
    """Test FP16 model export."""
    # Test export
    # Validate .pte file exists
    # Validate file size reasonable
    # Validate file is valid .pte format

def test_export_int8():
    """Test INT8 model export."""
    # Similar to above
```

#### test_pipeline_execution.py
```python
"""Test pipeline execution."""
def test_mac_pipeline_basic():
    """Test basic Mac pipeline execution."""
    # Run pipeline with minimal config
    # Validate outputs exist
    # Validate metrics are reasonable

def test_sme2_comparison():
    """Test SME2 ON vs OFF comparison."""
    # Run both experiments
    # Validate both complete
    # Validate SME2 ON is faster (or reasonable)
```

#### test_results_validation.py
```python
"""Test result validation."""
def test_latency_metrics():
    """Validate latency metrics are reasonable."""
    # Check median, mean, percentiles exist
    # Check values are positive
    # Check values are in reasonable range

def test_operator_analysis():
    """Validate operator-level analysis."""
    # Check operator stats exist
    # Check categories are valid
```

#### test_kernel_analysis.py
```python
"""Test kernel analysis."""
def test_kernel_extraction():
    """Test kernel information extraction."""
    # Run xnntrace mode
    # Validate kernel CSV exists
    # Validate kernel information is present
```

### Validation Scripts

#### validate_setup.py
- Check all prerequisites
- Verify ExecuTorch installation
- Verify runners exist
- Verify script structure
- Return clear pass/fail with actionable errors

#### validate_pipeline.py
- Validate config file
- Check model file exists
- Check runners exist
- Validate output directory structure
- Check results are complete

#### validate_results.py
- Validate result files exist
- Check metrics are reasonable
- Validate SME2 comparison makes sense
- Generate validation report

## Scripts for Learning Path

### Getting Scripts

**Primary Method: Sparse Checkout**
```bash
git clone --filter=blob:none --sparse https://github.com/ArmDeveloperEcosystem/arm-learning-paths.git sme2-profiling
cd sme2-profiling
git sparse-checkout init --cone
git sparse-checkout set content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling
```

This downloads only the SME2 profiling directory, not the entire learning paths repository.

**Fallback: Individual Script Download**
If you only need a single script:
```bash
wget https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/scripts/<script_name>
```

### setup_repo.sh
Automated setup script (downloadable via sparse checkout or wget):
1. Checks prerequisites
2. Creates virtual environment
3. Downloads/installs ExecuTorch
4. Installs dependencies
5. Validates setup
6. Provides clear success/failure feedback

### export_model.py
Model export utility (downloadable):
- Exports models to .pte format
- Supports multiple data types
- Validates exports

### mac_pipeline.py
Mac profiling pipeline (downloadable):
- Runs profiling experiments
- Generates results
- Validates outputs

### generate_config.py
Interactive config generator (downloadable):
1. Prompts for model path
2. Prompts for output directory
3. Prompts for experiments
4. Generates valid JSON config
5. Validates config

### run_quick_test.py
Quick smoke test (downloadable):
1. Exports a simple model
2. Runs minimal pipeline
3. Validates results
4. Reports success/failure

## Implementation Strategy

### Phase 1: Core Learning Path (Traditional)
1. Create _index.md with proper metadata and dual paths
2. Create 01-06 (prerequisites through analysis)
3. Add basic scripts (setup, validation) - downloadable
4. Test with human users (both learning styles)

### Phase 2: Agentic Kits
1. Create agentic-kits/ directory
2. Write setup-agent.md
3. Write pipeline-agent.md
4. Write validation-agent.md
5. Test with AI assistants (Cursor, Copilot, etc.)

### Phase 3: Test Cases
1. Create test-cases/ directory
2. Implement test scripts
3. Integrate with validation
4. Document test cases

### Phase 4: Android & Advanced
1. Add 07-android-pipeline.md
2. Add 08-onboard-model.md
3. Enhance agentic kits
4. Add more test cases

### Phase 5: Polish & Documentation
1. Add troubleshooting guides
2. Add FAQ
3. Enhance examples
4. Final testing with both learning styles

## Key Innovations

### 1. Dual-Path Content Structure
- Comprehensive learning path for readers who want full context
- Quick start path for explorers who want to jump in
- Both paths converge to same outcome
- Each page supports both styles

### 2. Performance Stack Awareness
- Explicitly connects Model → Runtime → Kernels → SME2
- Emphasizes operator-level and kernel views as connectors
- Builds optimization mindset
- Shows where bottlenecks appear at each layer

### 3. AI-Assisted Automation
- Structured agentic kits for AI assistants
- Clear validation checkpoints
- Embedded test cases
- Iterative refinement capability

### 4. Self-Contained Repository
- All scripts downloadable via wget
- Works within learning path constraints
- No external repository dependencies
- Complete and functional

### 5. Validation at Every Stage
- Automated validation scripts
- Clear success/failure indicators
- Actionable error messages
- Progress tracking

## Success Metrics

### For Human Developers
- Setup time: < 30 minutes
- First pipeline: < 1 hour from setup
- Results understanding: Can interpret at multiple levels
- Model adaptation: Can add own model (advanced) within 2-3 hours
- Confidence: Feel confident using framework independently

### For AI Assistants
- Automation rate: 80%+ of setup and execution
- Config generation: Can generate valid configs
- Error recovery: Can troubleshoot common issues
- Validation: Can validate setup and results
- Adaptation: Can help adapt framework to new models

### For Learning Path Quality
- Clarity: All instructions clear and unambiguous
- Completeness: All necessary information provided
- Accuracy: All commands and examples work as documented
- Maintainability: Content easy to update
- Accessibility: Works for both beginners and advanced users

## Next Steps

1. **Review this plan** with stakeholders
2. **Create initial structure** (directories, files)
3. **Write _index.md** with proper metadata and dual paths
4. **Implement Phase 1** (core learning path)
5. **Test with real users** (both learning styles)
6. **Implement Phase 2** (agentic kits)
7. **Test with AI assistants** (Cursor, Copilot, etc.)
8. **Iterate and improve** based on feedback

## Notes

- **Mac pipeline primary:** Most accessible, focus here first
- **Android optional:** Requires hardware, add as optional section
- **Dual learning styles:** Every page must support both comprehensive readers and explorers
- **Script distribution:** Use sparse checkout as primary method (efficient, no full repo download), with individual wget as fallback for single scripts only
- **Self-contained scripts:** All scripts must work standalone once downloaded
- **Performance stack focus:** Emphasize connections between layers throughout
- **AI assistance:** Make it easy for AI to help users
- **Test everything:** Use real scenarios, document edge cases
- **Repository location:** Scripts will be in public GitHub repo at `content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/`
