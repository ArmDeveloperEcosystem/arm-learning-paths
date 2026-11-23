---
title: Compare a Metis report with vulnerable C code
description: Review a vulnerable C program with Metis, export JSON and SARIF reports, and compare JSON findings with known defects.
weight: 4
layout: "learningpathall"
---

## Prepare the example C program

After setting up Arm Metis, create an example C program with vulnerabilities.

The [Damn Vulnerable C Program](https://github.com/hardik05/Damn_Vulnerable_C_Program) contains vulnerabilities intentionally placed and labeled in one C file.

Use the program to learn the Metis review process:

- Prepare a small target.
- Run `review_code`.
- Save JSON and SARIF.
- Summarize findings.
- Compare source locations.

In your terminal, clone the repository at the tested commit, and copy `dvcp.c` into a separate review directory:

```bash
git clone https://github.com/hardik05/Damn_Vulnerable_C_Program.git
git -C Damn_Vulnerable_C_Program checkout 8dcbd202887f587783952a320a2301de701be529
mkdir -p dvcp-review
cp Damn_Vulnerable_C_Program/dvcp.c dvcp-review/
```
The copy keeps the review target small and avoids sending the rest of the repository to Metis.

Add a short threat-model note for the review. Metis reads `.metis.md` as project context:

```bash
cat > dvcp-review/.metis.md <<'EOF'
# Project security context

This command-line C program parses an image file supplied by an untrusted user.
Treat file contents, dimensions, offsets, and derived allocation sizes as
attacker-controlled. Review memory safety, integer arithmetic, resource
exhaustion, input validation, and cleanup on error paths.
EOF
```

The note tells Metis how to treat inputs and security boundaries.

## Run the review

Switch to the review directory, and start the Metis interactive prompt with the provider configuration that you created earlier. Save JSON for detailed inspection and SARIF for code-scanning tools:

```bash
cd "$HOME/metis-security-review/dvcp-review"
metis \
  --interactive \
  --codebase-path . \
  --config "$HOME/metis-security-review/metis-review.yaml" \
  --output-file ../results/dvcp.json \
  --output-file ../results/dvcp.sarif
```

At the Metis prompt, run the review, then exit after it completes:

```console
review_code
exit
```

Metis initializes the project automatically, then runs the default simple LLM review and deduplicates the findings.

Metis prints review progress and detailed findings under `File:`, with an `Identified issue` heading.
The following fields are included in the findings:

- `Snippet`
- `Line number`
- `CWE`
- `Severity`
- `Why`
- `Mitigation`
- `Confidence`

After the findings, the export and token-usage output is similar to:

```output
Results saved to ../results/dvcp.json
SARIF report saved to ../results/dvcp.sarif
Token usage (review_code)
Current (input: 8,420 · output: 3,349 · total: 11,769)
```

Back in your shell, return to the workspace:

```bash
cd "$HOME/metis-security-review"
```

The run sends source-derived evidence to your configured model provider. Runtime, token use, and findings depend on the model, provider, and Metis version.

It can take a couple of minutes to complete the review.

## Summarize the JSON report

The JSON report stores findings in `reviews[].reviews`. Source locations can appear in an `anchor`, in `primary_file` and `line_number`, or in the `file` field of the enclosing review group.

Use the Python interpreter from the active Metis environment to count the findings and print their issue types and source locations:

```bash
python - <<'PY'
import json
from pathlib import Path

data = json.loads(Path("results/dvcp.json").read_text())
review_groups = data["reviews"]
count = sum(len(group["reviews"]) for group in review_groups)
print(f"Finding count: {count}")
for review_group in review_groups:
    for finding in review_group["reviews"]:
        anchor = finding.get("anchor") or {}
        file_path = (
            anchor.get("file_path")
            or finding.get("primary_file")
            or finding.get("file")
            or review_group.get("file")
        )
        line = anchor.get("start_line") or finding.get("line_number")
        print(
            f"- {finding['cwe']} {finding['issue']} "
            f"({file_path}:{line})"
        )
PY
```

The output is similar to:

```output
Finding count: 10
- CWE-125 Unterminated image fields cause out-of-bounds string reads (dvcp.c:48)
- CWE-122 Unchecked dimension-derived allocations permit heap overflows and NULL dereferences (dvcp.c:54)
- CWE-415 An even dimension sum causes a double free (dvcp.c:59)
- CWE-416 An odd dimension sum divisible by three causes a use-after-free write (dvcp.c:64)
- CWE-369 Unvalidated image dimensions cause invalid integer division (dvcp.c:82)
- CWE-787 File-controlled quotient indexes outside a stack buffer (dvcp.c:90)
- CWE-787 The heap buffer is accessed one byte past its allocation (dvcp.c:91)
- CWE-674 Recursive operation has no termination condition (dvcp.c:22)
- CWE-400 Allocation loop intentionally retains memory until exhaustion (dvcp.c:109)
- CWE-401 Large-quotient branch discards an allocated buffer without freeing it (dvcp.c:97)
```

This example report was captured on November 2, 2026 using the `metis-v2.0.0` tag ([`742b20d`](https://github.com/arm/metis/commit/742b20d685b0aeb3216b36ddfc44bc5e05ace82c)). The run used `gpt-6.1-sol` through an OpenAI-compatible endpoint and reviewed DVCP commit [`8dcbd20`](https://github.com/hardik05/Damn_Vulnerable_C_Program/commit/8dcbd202887f587783952a320a2301de701be529). The provider reported the model ID as `gpt-6.1-sol`. The run used the packaged simple LLM review and deduplication nodes.

Your exact count and wording can differ. A valid report can contain zero findings. Findings are expected for this program. An empty report means that the run didn't report any findings. It doesn't mean that the program is safe.

If you don't see findings, check your provider connection and any Metis log output before judging the result.

## Compare the report with known defects

View four source regions that the program identifies as deliberately vulnerable:

```bash
sed -n '14,28p' dvcp-review/dvcp.c
sed -n '42,69p' dvcp-review/dvcp.c
sed -n '72,87p' dvcp-review/dvcp.c
sed -n '89,115p' dvcp-review/dvcp.c
```

Check whether your report covers the following concrete cases:

- Signed image dimensions are combined and passed to `malloc()` without overflow or range checks.
- `buff1` is freed, then freed again when `size1` is even, or written after free when it's divisible by three.
- `img.height` is used as a divisor without a zero check.
- `size3` is used as an index into fixed-size and heap buffers without bounds checks.
- Attacker-controlled dimensions can select recursive stack exhaustion or repeated heap allocation.

The captured Metis 2.0.0 JSON and SARIF reports contain ten findings. Source anchors can span multiple lines, and one finding can discuss additional sites in its reasoning.

The following table maps those reported regions and explanations to the known source defects:

| Source issue | Tested-run outcome |
| --- | --- |
| Non-NUL-terminated image fields passed to `%s` | `CWE-125` at `dvcp.c:48` |
| Dimension-derived allocations followed by fixed-size copies | `CWE-122` anchored at `dvcp.c:54–58`; its reasoning also covers `dvcp.c:74–79` and `dvcp.c:82–87` |
| `buff1` double free and use-after-free | `CWE-415` at `dvcp.c:59–63`; `CWE-416` at `dvcp.c:64–69` |
| Integer division using unvalidated image dimensions | `CWE-369` at `dvcp.c:82` |
| Indexed stack and heap accesses | Separate `CWE-787` findings at `dvcp.c:90–94` and `dvcp.c:91–95` |
| `buff4` allocation lost without being freed | `CWE-401` at `dvcp.c:97–100` |
| Unbounded recursion and repeated heap allocation | `CWE-674` at `dvcp.c:22–27`; `CWE-400` at `dvcp.c:109–115` |

For each reported finding, verify the source location, attacker control, and operation. Also record known source defects that the run omitted.

The same review is also available in `results/dvcp.sarif`. SARIF allows code-hosting services and security tools to associate findings with source locations. Keep JSON when you want the complete Metis reasoning. Keep SARIF when you want to integrate results into an existing code-scanning workflow.

## What you've accomplished and what's next

You ran a complete Metis review, exported two report formats, and compared the reported findings with known defects.

Next, you'll prepare a realistic libpng target without leaving benchmark canaries or fixes in its source.
