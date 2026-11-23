---
title: Prepare a realistic Magma libpng target
description: Build a reviewable libpng source tree from Magma while removing benchmark canaries and fix branches.
weight: 5
layout: "learningpathall"
---

## Why prepare a Magma libpng target

You used a small labeled program to learn the Metis review process. You'll now prepare a larger C codebase to see how a Metis finding is triaged against source that's similar to real project code.

[Magma](https://hexhive.epfl.ch/magma/) gives you a repeatable way to prepare that target. Magma is a benchmark for evaluating fuzzers against real programs with documented vulnerabilities. A fuzzer is a testing tool that repeatedly runs a program with generated or mutated inputs. Fuzzers simulate crashes, hangs, memory errors, or other unexpected behavior. Use Magma only to create a prepared libpng source tree for review.

The preparation script creates the review target in four steps:

1. Checks out the libpng revision selected by Magma.
2. Applies Magma patches that introduce known vulnerable code.
3. Removes benchmark controls so that the source looks closer to a normal libpng tree.
4. Writes neutral Metis context for the review.

The result is a deliberately vulnerable example target. Don't use the target beyond the Learning Path.

## Download the preparation script

Download [the Magma libpng preparation script](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/cross-platform/review-c-code-with-metis/prepare_magma_libpng.py) into the workspace:

```bash
curl -L \
  https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/cross-platform/review-c-code-with-metis/prepare_magma_libpng.py \
  -o prepare_magma_libpng.py
```

Clone Magma, then check out the commit tested for this Learning Path:

```bash
git clone https://github.com/HexHive/magma.git
git -C magma checkout 75d1ae7b180443a778b8830c79176ca5f93642ac
```

Run the script to create `libpng-review`:

```bash
python prepare_magma_libpng.py \
  --magma-dir magma \
  --output-dir libpng-review
```

The output is similar to:

```output
Prepared libpng commit a37d4836519517bdce6cb9d956092321eca3e73b
Applied 7 Magma vulnerability-introducing patches
Output: /Users/you/metis-security-review/libpng-review
```

## Inspect the prepared source

Confirm that the prepared tree has local changes:

```bash
git -C libpng-review status --short
git -C libpng-review diff --stat
```

The diff summary shows that the script applied patches that introduce known vulnerable code to libpng. During triage, you'll inspect a `png.c` guard and the related `pngrutil.c` allocation.

{{% notice Note %}}
Don't give Metis the benchmark metadata, bug names, fuzzing harnesses, canaries, or fix branches. Those details would give a review model clues that a normal codebase wouldn't contain.
{{% /notice %}}

## Choose a libpng report option

You need a Metis report before you can triage a finding. Choose one of the following options:

- Run a live Metis review if you have enough API quota and want to compare your model configuration.
- Use the pre-captured report if you want to minimize your API usage.

{{< tabpane-normal >}}
  {{< tab header="Run live review" >}}
You'll prompt Metis to review only `pngrutil.c`, because the triage focuses on a finding in that file.

Run the review:

```bash
cd "$HOME/metis-security-review/libpng-review"
metis \
  --interactive \
  --codebase-path . \
  --config "$HOME/metis-security-review/metis-review.yaml" \
  --output-file ../results/libpng-live.json
```
The example Metis 2.0.0 review was captured with `gpt-6.1-sol` and used 353,579 model tokens (351,293 input and 2,286 output). Usage varies with the run and model configuration. A live run can take several minutes and consume substantial API quota.

At the Metis prompt, review the file, then exit:

```console
review_file pngrutil.c
exit
```
The results are review-only so that you can validate a finding manually later.

Back in your shell, return to the workspace:

```bash
cd "$HOME/metis-security-review"
```

Metis writes `results/libpng-live.json` and a companion `results/libpng-live.sarif`. You'll review the JSON report later.
  {{< /tab >}}
  {{< tab header="Use captured report" >}}
You'll create `results/libpng-review-candidate.json` from the Metis 2.0.0 review captured with `gpt-6.1-sol` on November 2, 2026. The full run returned three findings. You'll use the row-buffer size finding for the guided triage.

Create `results/libpng-review-candidate.json`:

```bash
cat > results/libpng-review-candidate.json <<'EOF'
{
  "_provenance": {
    "artifact_type": "Single finding extracted from a Metis review",
    "release_under_test": "metis-v2.0.0",
    "metis_commit": "742b20d685b0aeb3216b36ddfc44bc5e05ace82c",
    "capture_date": "2026-11-02",
    "configured_model": "gpt-6.1-sol",
    "reported_model": "gpt-6.1-sol",
    "magma_commit": "75d1ae7b180443a778b8830c79176ca5f93642ac",
    "libpng_commit": "a37d4836519517bdce6cb9d956092321eca3e73b",
    "prepared_source_sha256": "f628738930426bea4dccd718e5d90daaf012d5cef365880fa0f6adc4f936a78d",
    "command": "review_file pngrutil.c",
    "automatic_triage": false,
    "capture_note": "One of three findings from the captured run; only the review group file_path is made relative for portability."
  },
  "reviews": [
    {
      "reviews": [
        {
          "id": "6867943ebb524f57a0132a08a96d3115",
          "issue": "Unchecked row-size arithmetic can cause a heap buffer overflow on 32-bit builds",
          "code_snippet": "row_bytes = PNG_ROWBYTES(max_pixel_depth, row_bytes) +\n       1 + ((max_pixel_depth + 7) >> 3U);",
          "start_line": 4591,
          "end_line": 4592,
          "reasoning": "PNG_ROWBYTES multiplies using size_t without checking overflow. On a build with 32-bit size_t, an 8-bit RGBA image of width 536870912, with png_set_expand_16 enabled, produces max_pixel_depth 64. The multiplication by eight wraps to zero, leaving row_bytes equal to nine. The subsequent row allocations are consequently only 57 bytes each, but line 4648 clears png_ptr->rowbytes + 1 bytes, where the original RGBA rowbytes is 2147483648, causing a massive heap overwrite before image decompression. This requires the application to raise the default width limit sufficiently, or a build configured with a larger width limit. The inspected png_check_IHDR architecture-size check in png.c has an empty body, so it does not reject this image; the later rowbytes check also accepts the original row size. The default width limit prevents this example, and 64-bit size_t does not exhibit this particular overflow.",
          "mitigation": "Check the aligned width against the maximum representable allocation size divided by the maximum pixel byte size before multiplication, reserving all padding and alignment overhead. Restore effective architecture-size rejection in png_check_IHDR and retain checked arithmetic at this allocation site.",
          "confidence": 0.96,
          "cwe": "CWE-190",
          "severity": "High",
          "anchor": {
            "file_path": "pngrutil.c",
            "start_line": 4591,
            "end_line": 4592,
            "start_col": 0,
            "end_col": 41,
            "start_byte": 144001,
            "end_byte": 144100,
            "symbol": "pngrutil.c::png_read_start_row",
            "kind": "range",
            "content_hash": "21587413f66cc92e",
            "confidence": "exact"
          },
          "line_number": 4591
        }
      ],
      "file": "pngrutil.c",
      "file_path": "pngrutil.c"
    }
  ]
}
EOF
```
The finding is unchanged from the live report. Only the review group `file_path` is made relative for portability, and `_provenance` records the capture details.

The reasoning of the finding depends on the reviewed application using a sufficiently narrow `size_t`. It also depends on image-width limits that permit very large inputs.
  {{< /tab >}}
{{< /tabpane-normal >}}

## What you've accomplished and what's next

You've prepared production-like vulnerable libpng source without benchmark hints and selected a report for triage.

Next, you'll check a reported finding against the benchmark diff and decide how to handle additional live findings.
