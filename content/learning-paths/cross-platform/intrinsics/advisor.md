---
layout: learningpathall
title: Find intrinsics in large code bases
weight: 6
---

Porting applications to Arm is easier when you identify architecture specific code before you start to build or run.

## Porting Advisor and migrate-ease

[Porting Advisor for Graviton](https://github.com/aws/porting-advisor-for-graviton/) is a command line tool for assessing the portability of software to AWS Graviton processors. Supported operating systems include Linux, Windows, and macOS. Alternatively, you can use [migrate-ease](https://github.com/migrate-ease/migrate-ease). Both tools are forked from the original [Porting advisor](https://github.com/arm-hpc/porting-advisor) project. The two projects have different feature sets.

Although Porting Advisor for Graviton is designed for AWS Graviton processors, findings from either tool can also indicate general Arm compatibility issues relevant to porting code from `x86` to `aarch64` on Arm Neoverse-based processors, such as the Arm AGI CPU.

## Install Porting Advisor or migrate-ease

Use the [Porting Advisor for Graviton](/install-guides/porting-advisor/) install guide to set it up on your machine. Alternatively, if using migrate-ease, use the installation steps in the [getting started guide](/learning-paths/servers-and-cloud-computing/migrate-ease/3_migrate_ease_run/).

There are multiple ways to run Porting Advisor for Graviton. The example below assumes you are running Porting Advisor for Graviton as an executable and it is in your search path. The executable shown below is for Arm Linux; use the executable for your host operating system and architecture if they differ.

For migrate-ease, complete the linked setup guide, including activating the Python virtual environment and setting `PYTHONPATH` to the migrate-ease repository. Run the following commands in the same shell so these settings remain available.

## Run Porting Advisor or migrate-ease

You can run either tool on a realistic application such as the open source [KasmVNC](https://github.com/kasmtech/KasmVNC) project.

Use `git` to retrieve the source code:

```console
git clone https://github.com/kasmtech/KasmVNC.git
```

Specify the directory containing the source code to be analyzed. If using `migrate-ease`, specify the architecture of your target machine with the `--march` option. For example, when targeting the Arm AGI CPU based on Neoverse V3, specify `--march=armv9.2-a`.

Run your chosen tool:

{{< tabpane code=true >}}
{{< tab header="Porting Advisor for Graviton" >}}

porting-advisor-linux-aarch64 KasmVNC

{{< /tab >}}
{{< tab header="migrate-ease" >}}

python3 -m cpp --march=armv9.2-a --output out.json ./KasmVNC/

{{< /tab >}}
{{< /tabpane >}}

Both tools scan the source directory for potential architecture-specific portability issues. The migrate-ease command uses the C/C++ scanner. Review the findings and build and test your application on the target platform; a scan does not prove compatibility.

Porting Advisor prints its report to the console. The migrate-ease command writes its report to `out.json` in the current directory; open that file to inspect the findings. The examples below show the Porting Advisor console output and an abbreviated excerpt of the migrate-ease JSON report. File and issue counts can vary with the KasmVNC revision and tool version:

{{< tabpane code=true >}}
{{< tab header="Porting Advisor for Graviton" >}}

Porting Advisor for Graviton v1.1.1
Report date: 2026-08-24 08:57:02

506 files scanned.
detected python code. if you need pip, version 19.3 or above is recommended. we detected that you have version 24.0.
detected python code. min version 3.7.5 is required. we detected that you have version 3.12.3. see https://github.com/aws/aws-graviton-getting-started/blob/main/python.md for more details.
KasmVNC/common/rfb/scale_sse2.cxx: 55 other issues
KasmVNC/common/rfb/scale_sse2.cxx:74 (SSE2_halve): architecture-specific intrinsic: _mm_loadu_si128
KasmVNC/common/rfb/scale_sse2.cxx:75 (SSE2_halve): architecture-specific intrinsic: _mm_loadu_si128
KasmVNC/common/rfb/scale_sse2.cxx:62 (SSE2_halve): architecture-specific intrinsic: _mm_set_epi32
KasmVNC/common/rfb/scale_sse2.cxx:63 (SSE2_halve): architecture-specific intrinsic: _mm_set_epi32
KasmVNC/common/rfb/scale_sse2.cxx:64 (SSE2_halve): architecture-specific intrinsic: _mm_set_epi32
KasmVNC/common/rfb/scale_sse2.cxx:61 (SSE2_halve): architecture-specific intrinsic: _mm_setzero_si128
KasmVNC/common/rfb/scale_sse2.cxx:78 (SSE2_halve): architecture-specific intrinsic: _mm_unpackhi_epi8
KasmVNC/common/rfb/scale_sse2.cxx:80 (SSE2_halve): architecture-specific intrinsic: _mm_unpackhi_epi8
KasmVNC/common/rfb/scale_sse2.cxx:77 (SSE2_halve): architecture-specific intrinsic: _mm_unpacklo_epi8
KasmVNC/common/rfb/scale_sse2.cxx:79 (SSE2_halve): architecture-specific intrinsic: _mm_unpacklo_epi8

Report generated successfully. Hint: you can use --output FILENAME.html to generate an HTML report.

{{< /tab >}}
{{< tab header="migrate-ease" >}}

// out.json
{
    "branch": null,
    "commit": null,
    "errors": [],
    "file_summary": {
        "asm": {
            "count": 0,
            "fileName": "Assembly",
            "loc": 0
        },
        "c": {
            "count": 305,
            "fileName": "C",
            "loc": 51787
    ...

    "target_os": "OpenAnolis",
    "total_issue_count": 54
}

{{< /tab >}}
{{< /tabpane >}}


Porting Advisor and migrate-ease save time by helping you identify architecture-specific code in a project.
