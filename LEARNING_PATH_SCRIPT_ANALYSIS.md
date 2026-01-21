# Learning Path Script Organization Analysis

## Overview
Based on analysis of the `measure-kleidiai-kernel-performance-on-executorch` learning path and the codebase, here's how to effectively organize Python scripts and pipelines in learning paths.

## Current Pattern: Two Approaches

### Approach 1: Inline Code Blocks (Most Common)
**Used in:** `08-analyze-etdump.md`

```markdown
Save the following code in a file named `inspect.py`:

```python
import os
import sys
from executorch.devtools.inspector import Inspector
# ... code ...
```

Then run it:
```bash
python3 inspect.py model/linear_model_pf32_gemm.pte
```
```

**Pros:**
- Simple and straightforward
- Code is visible in the documentation
- Easy to copy-paste

**Cons:**
- Users must manually create files
- No automatic file extraction
- Harder to maintain for complex pipelines

### Approach 2: Standalone Script Files + wget (Best for Complex Scripts)
**Used in:** `04-create-fc-model.md`

```markdown
You can download and run the full example script:

```bash
wget https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/refs/heads/main/content/learning-paths/mobile-graphics-and-gaming/measure-kleidiai-kernel-performance-on-executorch/export-linear-model.py
chmod +x export-linear-model.py
python3 ./export-linear-model.py
```
```

**File Structure:**
```
measure-kleidiai-kernel-performance-on-executorch/
├── _index.md
├── 01-env-setup.md
├── 04-create-fc-model.md
├── export-linear-model.py      # Standalone script
├── export-conv2d.py            # Standalone script
└── export-matrix-mul.py         # Standalone script
```

**Pros:**
- Scripts are version-controlled with the learning path
- Users can download complete, working scripts
- Better for complex, multi-function scripts
- Scripts can be tested independently
- Easier to maintain and update

**Cons:**
- Requires users to download files
- Scripts are separate from documentation

## Approach 3: file_name Attribute (For Testing Framework)
**Used in:** Testing framework (see `appendix-3-test.md`)

```markdown
```python { file_name="hello.py" }
print("Hello World")
```

This creates a file named `hello.py` when the testing framework runs.
```

**Note:** This is primarily for the automated testing framework, not for user-facing content.

## Best Practices for Pipeline Scripts

### 1. **Folder Structure for Multiple Scripts**

For a learning path with multiple scripts that work together, organize like this:

```
your-learning-path/
├── _index.md
├── 01-setup.md
├── 02-step-one.md
├── 03-step-two.md
├── scripts/                    # Optional: subfolder for scripts
│   ├── step1_preprocess.py
│   ├── step2_train.py
│   ├── step3_evaluate.py
│   └── pipeline.py            # Main orchestrator
└── configs/                   # Optional: configuration files
    └── config.yaml
```

**OR** (simpler, recommended):

```
your-learning-path/
├── _index.md
├── 01-setup.md
├── 02-step-one.md
├── 03-step-two.md
├── preprocess.py              # Scripts at root level
├── train.py
├── evaluate.py
└── run_pipeline.sh            # Shell script to run pipeline
```

### 2. **Pipeline Orchestration Options**

#### Option A: Shell Script Wrapper (Recommended)
Create a `run_pipeline.sh` that orchestrates everything:

```bash
#!/bin/bash
set -e

echo "Step 1: Preprocessing..."
python3 preprocess.py --input data/raw --output data/processed

echo "Step 2: Training..."
python3 train.py --data data/processed --model models/checkpoint.pth

echo "Step 3: Evaluation..."
python3 evaluate.py --model models/checkpoint.pth --output results/
```

In your markdown:
```markdown
Download and run the complete pipeline:

```bash
wget https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/refs/heads/main/content/learning-paths/your-path/run_pipeline.sh
chmod +x run_pipeline.sh
./run_pipeline.sh
```
```

#### Option B: Python Main Script
Create a `pipeline.py` that imports and orchestrates:

```python
# pipeline.py
from preprocess import preprocess_data
from train import train_model
from evaluate import evaluate_model

def main():
    # Step 1
    processed_data = preprocess_data('data/raw', 'data/processed')
    
    # Step 2
    model = train_model(processed_data, 'models/checkpoint.pth')
    
    # Step 3
    results = evaluate_model(model, 'results/')
    
    print("Pipeline completed successfully!")

if __name__ == '__main__':
    main()
```

#### Option C: Makefile (For Complex Builds)
```makefile
.PHONY: all preprocess train evaluate clean

all: preprocess train evaluate

preprocess:
	python3 preprocess.py --input data/raw --output data/processed

train: preprocess
	python3 train.py --data data/processed --model models/checkpoint.pth

evaluate: train
	python3 evaluate.py --model models/checkpoint.pth --output results/

clean:
	rm -rf data/processed models/ results/
```

### 3. **Documentation Strategy**

For each script, document:
1. **Purpose** - What it does
2. **Dependencies** - What it needs (other scripts, data, configs)
3. **Usage** - How to run it
4. **Output** - What it produces

Example markdown structure:

```markdown
## Step 1: Preprocessing

The preprocessing script prepares raw data for training.

### Download the script

```bash
wget https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/refs/heads/main/content/learning-paths/your-path/preprocess.py
```

### Run preprocessing

```bash
python3 preprocess.py --input data/raw --output data/processed
```

### What it does

The script:
- Loads raw data from `data/raw/`
- Applies normalization and feature engineering
- Saves processed data to `data/processed/`

### Expected output

You should see:
```
Processing 1000 samples...
Normalizing features...
Saving to data/processed/train.csv
Preprocessing complete!
```
```

### 4. **Overcoming MD-Heavy Constraints**

#### Strategy 1: Modular Scripts
Break complex logic into small, focused scripts:
- Each script does one thing well
- Scripts can be tested independently
- Easier to understand and maintain

#### Strategy 2: Configuration Files
Use YAML/JSON configs instead of hardcoding:

```python
# config.yaml
preprocessing:
  input_dir: "data/raw"
  output_dir: "data/processed"
  batch_size: 32

training:
  epochs: 100
  learning_rate: 0.001
  model_path: "models/checkpoint.pth"
```

```python
# train.py
import yaml

with open('config.yaml') as f:
    config = yaml.safe_load(f)

# Use config['training']['epochs'], etc.
```

#### Strategy 3: Helper Functions Module
Create a `utils.py` or `helpers.py`:

```python
# utils.py
def load_data(path):
    # Common data loading logic
    pass

def save_results(data, path):
    # Common saving logic
    pass
```

Then import in your scripts:
```python
# train.py
from utils import load_data, save_results
```

#### Strategy 4: Use Python Packages
For very complex pipelines, structure as a package:

```
your-learning-path/
├── pipeline/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── utils.py
├── configs/
│   └── default.yaml
├── run_pipeline.py
└── README.md
```

## Recommendations for Your Use Case

### For `sme-executorch-profiling` Learning Path

1. **Start Simple**: Use standalone `.py` files at the root level
   ```
   sme-executorch-profiling/
   ├── _index.md
   ├── 01-setup.md
   ├── 02-profile.md
   ├── 03-analyze.md
   ├── profile_model.py
   ├── analyze_results.py
   └── run_full_pipeline.sh
   ```

2. **Create a Pipeline Script**: If scripts need to run in sequence:
   ```bash
   # run_full_pipeline.sh
   #!/bin/bash
   python3 profile_model.py --model model.pte
   python3 analyze_results.py --dump model.etdump
   ```

3. **Document Each Script**: In your markdown files:
   - Show what each script does
   - Provide download links using `wget` with raw GitHub URLs
   - Show example usage
   - Document expected outputs

4. **Use Inline Code for Simple Examples**: For one-off scripts or examples, use inline code blocks

5. **Link Scripts Together**: In your markdown, show the flow:
   ```markdown
   ## Complete Pipeline
   
   Run the full profiling pipeline:
   
   ```bash
   # Download all scripts
   wget https://raw.githubusercontent.com/.../profile_model.py
   wget https://raw.githubusercontent.com/.../analyze_results.py
   
   # Run pipeline
   python3 profile_model.py --model my_model.pte
   python3 analyze_results.py --dump my_model.etdump
   ```
   ```

## Example: Complete Learning Path Structure

```
sme-executorch-profiling/
├── _index.md                    # Main page with overview
├── _next-steps.md               # Auto-generated, don't modify
├── 01-prerequisites.md          # Setup and requirements
├── 02-setup-environment.md      # Environment setup
├── 03-profile-model.md         # How to profile
│   └── (references profile_model.py)
├── 04-analyze-results.md        # How to analyze
│   └── (references analyze_results.py)
├── 05-visualize.md              # Visualization
│   └── (references visualize.py)
├── profile_model.py             # Standalone script
├── analyze_results.py            # Standalone script
├── visualize.py                  # Standalone script
└── run_pipeline.sh               # Optional: orchestrator
```

## Key Takeaways

1. **Standalone `.py` files** are the best approach for complex, reusable scripts
2. **Use `wget` with raw GitHub URLs** to make scripts downloadable
3. **Organize scripts at the learning path root** (or in a `scripts/` subfolder if many)
4. **Create orchestrator scripts** (shell or Python) for multi-step pipelines
5. **Document each script** in the markdown with purpose, usage, and expected output
6. **Keep scripts focused** - one script, one purpose
7. **Use inline code blocks** only for simple, one-off examples

## Testing Your Scripts

The learning path framework supports testing scripts using the `file_name` attribute, but this is primarily for automated testing. For user-facing content, use the `wget` approach.

## Next Steps

1. Create your Python scripts as standalone files
2. Add them to your learning path directory
3. Reference them in markdown using `wget` commands
4. Test that the scripts work independently
5. Create a pipeline script if needed
6. Document everything clearly in your markdown files

