# Pull Request Instructions for SME2 ExecuTorch Profiling Learning Path

## Before Creating PR

### 1. Review the Contribution Guidelines
- Read [Create a Learning Path](https://learn.arm.com/learning-paths/cross-platform/_example-learning-path/) guide
- Review the [README.md](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/README.md) in the root of the repository

### 2. Test Your Content
Run Hugo to ensure there are no errors:

```bash
hugo
```

Expected output should show a table with page counts and no error messages.

### 3. Review PR Template Checklist
Before submitting, ensure:
- [ ] I have reviewed Create a Learning Path
- [ ] I have checked my contribution for confidential information
- [ ] I confirm the contribution can be used under Creative Commons Attribution 4.0 International License

## Creating the Pull Request

**Note**: This repository is already a fork of the main arm-learning-paths repository.
- Your fork: `Arm-Debug/arm-learning-paths-sme2-executorch`
- Upstream: `ArmDeveloperEcosystem/arm-learning-paths`

1. **Create a branch** for your changes (recommended)
   ```bash
   git checkout -b sme2-executorch-profiling-learning-path
   ```
   Or commit directly to `main` if preferred.

2. **Commit your changes**
   ```bash
   git add content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/
   git commit -m "Add SME2 ExecuTorch profiling learning path"
   ```

3. **Push to your fork**
   ```bash
   git push origin sme2-executorch-profiling-learning-path
   # Or if using main branch:
   git push origin main
   ```

4. **Create Pull Request on GitHub**

   **CRITICAL**: Start from the **upstream repository** (ArmDeveloperEcosystem), NOT your fork!

   **Step-by-step**:
   
   1. Go to: **https://github.com/ArmDeveloperEcosystem/arm-learning-paths** (upstream repository)
   2. Click the **"Pull requests"** tab
   3. Click the green **"New pull request"** button
   4. Click **"compare across forks"** link (this appears below the branch selector - this is the key step!)
   5. Now configure:
      - **base repository**: `ArmDeveloperEcosystem/arm-learning-paths` (should already be selected)
      - **base**: `main` (upstream's main branch)
      - **head repository**: Click dropdown and select `Arm-Debug/arm-learning-paths-sme2-executorch` (your fork)
      - **compare**: Click dropdown and select `sme2-executorch-clean` (your branch)
   6. Click **"Create pull request"**
   
   **Alternative: Direct URL** (copy and paste into browser):
   ```
   https://github.com/ArmDeveloperEcosystem/arm-learning-paths/compare/main...Arm-Debug:arm-learning-paths-sme2-executorch:sme2-executorch-clean
   ```

5. **Fill out the PR**
   - **Title**: "Add SME2 ExecuTorch profiling learning path"
   - **Description**: Add a brief description of what's included
   - **Check the PR template boxes**:
     - [ ] I have reviewed Create a Learning Path
     - [ ] I have checked my contribution for confidential information
     - [ ] I confirm the contribution can be used under Creative Commons Attribution 4.0 International License
   - **Optional**: Mark as "Draft" if you're still iterating
   - Click **"Create pull request"**

   **Visual Guide**:
   ```
   Your Fork (Arm-Debug/arm-learning-paths-sme2-executorch)
   └── sme2-executorch-profiling-learning-path (your branch) ──┐
                                                                 │ PR goes here
                                                                 ▼
   Upstream (ArmDeveloperEcosystem/arm-learning-paths)          │
   └── main (target branch) ◄──────────────────────────────────┘
   ```

## What's Included in This PR

### Main Content Pages
- `_index.md` - Learning path overview and metadata
- `01-overview.md` - Overview and quickstart
- `02-setup-and-pipeline.md` - Environment setup and runner build
- `03-model-onboarding-and-profiling.md` - Model onboarding and profiling workflow
- `04-agent-skills.md` - Agent skills for automation

### Code Package
- `executorch_sme2_kit/` - Complete profiling kit with:
  - Model profiling scripts and pipeline
  - Agent skills definitions
  - Example models and configs

### Images
- `images/SME2_stack_01062026.png` - Stack diagram
- `images/squeeze_sam_latency_comparison.png` - Case study latency results
- `images/combined_operator_breakdown_stacked.png` - Operator breakdown visualization

### Archived Content (Not Included in PR)
- `_archive/` - Contains old versions and unused content (excluded via .gitignore if configured)

## After PR Submission

- **Continue working**: Push more commits to your branch, PR updates automatically
- **Get feedback**: Reviewers will comment on the PR
- **Iterate**: Address feedback by pushing new commits
- **Mark ready**: When done, mark as "Ready for review" (if it was a draft)
- **Automated checks**: Will run (spelling, links, metadata validation)
- **Review**: Learning Path team will review for technical accuracy and writing style
- **Watch**: Monitor review comments and respond as needed
- **Merge**: Once merged, the website will automatically update

## Important Notes

- ✅ You create the PR from **your fork** → **upstream main**
- ✅ You do **NOT** need to create a branch in upstream
- ✅ You do **NOT** need to merge into your fork's main first
- ✅ The PR will show only your changes (55 files, ~4,700 lines)
- ✅ You can continue pushing commits to update the PR

## Notes

- The placeholder blog post link in `01-overview.md` needs to be updated with the actual PyTorch blog post URL
- All code links point to the Arm Learning Paths repository structure
- Test cases are included for validation but may need review
