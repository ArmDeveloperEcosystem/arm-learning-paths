---
title: Triage a libpng finding
description: Check a Metis report finding against source code, attacker control, and the Magma ground-truth diff.
weight: 6
layout: "learningpathall"
---

## List the reported findings

After choosing an Arm Metis report option, triage the findings in the report manually. 

Both report options provide Metis 2.0.0 review findings without automated triage verdicts. You'll check one finding against the source code, build conditions, and Magma diff before deciding its status.

For optional automated triage of Metis JSON or SARIF reports, see the [Metis 2.0.0 triage flow](https://github.com/arm/metis/blob/metis-v2.0.0/docs/triage-flow.md).

Select the report that you want to summarize:

{{< tabpane-normal >}}
  {{< tab header="Live report" >}}
Use this option if you ran the live review and want to inspect its results:

```bash
REPORT=results/libpng-live.json
```
  {{< /tab >}}
  {{< tab header="Captured report" >}}
Use this option for the guided row-buffer triage, or if your live review returned no findings:

```bash
REPORT=results/libpng-review-candidate.json
```
  {{< /tab >}}
{{< /tabpane-normal >}}

The JSON reports store findings inside `reviews` groups. The following summary uses the source `anchor` of the finding when present. It then falls back to its primary file or review-group file and `line_number`.

 Print a compact summary:

```bash
python - "$REPORT" <<'PY'
import json
import sys
from pathlib import Path

data = json.loads(Path(sys.argv[1]).read_text())
for review_group in data["reviews"]:
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
            f"{finding['severity']:>6} {finding['cwe']}: "
            f"{finding['issue']} "
            f"({file_path}:{line})"
        )
PY
```

If you selected the captured report, the expected output is:

```output
  High CWE-190: Unchecked row-size arithmetic can cause a heap buffer overflow on 32-bit builds (pngrutil.c:4591)
```

If your live report includes the row-buffer finding, use it for triage. Otherwise, set `REPORT=results/libpng-review-candidate.json` to follow the example. The severity and confidence are model assessments. They don't confirm the runtime.

## Triage the row-buffer finding

This finding depends on the ABI, image limits, and selected transforms of the target application. Running Metis on an Arm64 machine doesn't establish whether a reviewed application uses 32-bit or 64-bit `size_t`.

Inspect the reported allocation and clearing operations, the row-size macro, and the original row-size calculation:

```bash
sed -n '4584,4648p' libpng-review/pngrutil.c
sed -n '738,741p' libpng-review/pngpriv.h
sed -n '888,904p' libpng-review/pngrutil.c
```

Check the expansion API named in the finding, and the order of row initialization:

```bash
sed -n '941,950p' libpng-review/pngrtran.c
sed -n '4484,4500p' libpng-review/pngrutil.c
sed -n '267,279p' libpng-review/pngread.c
```

Trace the following relationships in the source:

1. PNG width and pixel depth influence the row size. An RGBA8 input has 32 bits per pixel. Enabling `png_set_expand_16()` makes the maximum transformed depth 64 bits. `PNG_ROWBYTES` multiplies in `size_t`.
2. `png_read_start_row` rounds the width up to an eight-pixel boundary. It calculates `row_bytes`, then adds padding before allocation.
3. The later `memset` uses the original `png_ptr->rowbytes + 1`, not the `row_bytes` of the allocation. `png_read_update_info()` initializes the row buffers before updating the transformed image information. Check whether the allocation is large enough for that write.
4. On a 32-bit `size_t` build, a sufficiently large width can wrap the aligned row calculation. The same arithmetic doesn't wrap at that width with a 64-bit `size_t`.

Next, inspect the earlier architecture-width guard and the prepared-source diff:

```bash
sed -n '2561,2595p' libpng-review/png.c
git -C libpng-review diff -U8 -- png.c
```

The architecture-width test is still present, but its body no longer warns or sets `error = 1`. The diff shows that Magma preparation removed those statements. This connects the finding to the injected vulnerability. The missing defense is in `png.c`, even though the reported allocation is in `pngrutil.c`.

Check the default limits and how an application can change them:

```bash
grep -n 'PNG_USER_WIDTH_MAX' libpng-review/scripts/pnglibconf.h.prebuilt
sed -n '654,668p' libpng-review/libpng-manual.txt
```

The default width limit is `1000000`. It rejects the very large input that's used during IHDR validation, before row initialization. An application can raise the limit with `png_set_user_limits()` before `png_read_info()`. Build-time settings can also change the limit. Check the deployed ABI, active limits, pixel format, and transforms. Avoid assuming that every PNG reader is affected.

Also inspect `PNG_MAX_MALLOC_64K`. If enabled, its later `png_ptr->rowbytes` check rejects the example before `memset`. The arithmetic alone doesn't account for every build-time defense.

To isolate the arithmetic in the captured finding, model a 32-bit `size_t` with an RGBA8 input and `png_set_expand_16()` enabled:

```bash
python - <<'PY'
width = 1 << 29
input_pixel_depth = 32
max_pixel_depth = 64
mask = (1 << 32) - 1
aligned_width = (width + 7) & ~7
row_bytes = (
    ((aligned_width * (max_pixel_depth >> 3)) & mask)
    + 1 + ((max_pixel_depth + 7) >> 3)
)
allocation = row_bytes + 48
original_rowbytes = (width * (input_pixel_depth >> 3)) & mask
print(f"Width: {width}; aligned width: {aligned_width}")
print(f"Allocation bytes: {allocation}; clear bytes: {original_rowbytes + 1}")
PY
```
The original row size uses 32 bits per pixel. The allocation calculation uses a maximum transformed depth of 64 bits.

The expected output is:

```output
Width: 536870912; aligned width: 536870912
Allocation bytes: 57; clear bytes: 2147483649
```

This calculation models unsigned wraparound. It doesn't run libpng or prove that a decoder reaches the write. The source supports an architecture- and configuration-dependent finding, but the Learning Path doesn't include a 32-bit reproducer. Record the finding as unconfirmed at runtime until you reproduce the path with the intended build and application settings. Neither the heap-overflow claim nor the potential code-execution impact of the model is established by the calculation alone.

## Check and record other findings

Your live run might return no findings, the row-buffer finding, or different findings. An empty report doesn't prove the target is safe. 

A finding outside the injected changes isn't automatically false. However, it's also not evidence by itself that Metis discovered a new vulnerability.

For each additional finding, check the following information:

- Whether untrusted input reaches the reported operation, including through callers or helper functions
- Whether the build includes that code and the arithmetic and platform assumptions hold
- Whether an existing guard, API contract, or file-format rule invalidates the finding
- Whether a focused test or sanitizer reproduces the behavior
- Whether the proposed fix preserves intended behavior

Search upstream issues and security advisories before reporting a new vulnerability. Treat the finding as unconfirmed until you have enough evidence to decide otherwise.

Record the status of each additional finding as one of the following: 

- Confirmed
- Rejected
- Duplicate
- Accepted risk
- Unconfirmed

Include the following information with the status of the finding:

- Input path
- Build assumptions
- Reproduction evidence or remaining checks
- Proposed fix owner
- Test coverage

Don't publish unverified findings against active open-source projects. Follow the security policy and coordinated-disclosure process of the project if further investigation confirms an issue.

## What you've accomplished and what's next

You triaged Metis findings against source evidence. 

You can apply the Learning Path workflow to a bounded directory, file, or patch in your own C project. You can also extend the workflow for other languages.
