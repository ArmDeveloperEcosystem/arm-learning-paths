---
title: Prepare a realistic Magma libpng target
description: Build a reviewable libpng source tree from Magma while removing benchmark canaries and fix branches.
weight: 5
layout: "learningpathall"
---

## Why prepare a Magma libpng target?

The previous section used a small labeled program to teach the Metis review process. This section prepares a larger C codebase so you can see how a Metis finding is triaged against source that looks closer to real project code.

[Magma](https://hexhive.epfl.ch/magma/) gives you a repeatable way to prepare that target. Magma is a benchmark for evaluating fuzzers against real programs with documented vulnerabilities. A fuzzer is a testing tool that repeatedly runs a program with generated or mutated inputs to trigger crashes, hangs, memory errors, or other unexpected behavior.

You use Magma here only to create a prepared libpng source tree for review. You are not using Magma to benchmark Metis. You also do not give Metis the benchmark metadata, bug names, fuzzing harnesses, canaries, or fix branches, because those details would give a review model clues that a normal codebase would not contain.

The preparation script creates the review target in four steps:

1. Checks out the libpng revision selected by Magma.
2. Applies Magma patches that introduce known vulnerable code.
3. Removes benchmark controls so the source looks closer to a normal libpng tree.
4. Writes neutral Metis context for the review.

The result is a deliberately vulnerable example target. Do not use it outside this exercise.

## Download the preparation script

Download [the Magma libpng preparation script](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/cross-platform/review-c-code-with-metis/prepare_magma_libpng.py) into the exercise workspace:

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

The diff summary shows that the script applied patches that introduce known vulnerable code to libpng. During triage, you will inspect a `png.c` guard and the related `pngrutil.c` allocation. Do not send patch names, benchmark descriptions, or known vulnerability lists to Metis.

## Choose a libpng report option

You need a Metis report before you can triage a finding. Choose one of these options:

- Run a live Metis review if you have enough API quota and want to compare your model configuration.
- Use the pre-captured report if you are interested to try Metis, but want to minimize your API usage.

{{< tabpane-normal >}}
  {{< tab header="Run live review" >}}
This option asks Metis to review only `pngrutil.c`, because the triage exercise focuses on a finding in that file.

The captured Metis 2.0.0 review with `gpt-6.1-sol` used 353,579 model tokens (351,293 input and 2,286 output). Usage varies with the run and model configuration. A live run can take several minutes and consume substantial API quota. Use the captured report option to avoid those model calls or if your run does not produce a finding you can triage.

```bash
cd "$HOME/metis-security-review/libpng-review"
metis \
  --interactive \
  --codebase-path . \
  --config "$HOME/metis-security-review/metis-review.yaml" \
  --output-file ../results/libpng-live.json
```

At the Metis prompt, review the file, then exit. The results are review-only so you can validate a finding manually in the next section:

```console
review_file pngrutil.c
exit
```

Back in your shell, return to the exercise workspace:

```bash
cd "$HOME/metis-security-review"
```

Metis writes `results/libpng-live.json` and a companion `results/libpng-live.sarif`. Use the JSON report in the next section.
  {{< /tab >}}
  {{< tab header="Use captured report" >}}
This option creates `results/libpng-review-candidate.json` from the Metis 2.0.0 review captured with `gpt-6.1-sol` on November 2, 2026. The full run returned three findings; this example selects the row-buffer size finding for the guided triage. The finding is unchanged from the live report; only the review group's `file_path` is made relative for portability, and `_provenance` records the capture details.

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

This is a captured finding from the same release used in the exercises, not guaranteed output for every run. Its reasoning depends on the reviewed application using a sufficiently narrow `size_t` and image-width limits that permit very large inputs. The next section checks those conditions against the source; this capture is not a native exploit reproduction.
  {{< /tab >}}
{{< /tabpane-normal >}}

## What you've accomplished and what's next

You prepared production-like vulnerable libpng source without benchmark hints and selected a report for triage. Next, you will check a reported finding against the benchmark diff and decide how to handle additional live findings.
