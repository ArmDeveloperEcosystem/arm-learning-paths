---
# User change
title: "Interpreting Analysis Results with a Real Example"

weight: 5

layout: "learningpathall"

---
### Example from a real-world case
[Protobuf](https://github.com/protocolbuffers/protobuf) is a widely used library for serializing structured data. AArch64 support is introduced in version v3.5.0 released in November 2017. Version v2.5.0 is a popular version without AArch64 support.

Use migrate-ease to scan protobuf v2.5.0 with JSON result output:
```
python3 -m cpp --git-repo https://github.com/protocolbuffers/protobuf.git --branch v2.5.0 --output result.json --arch aarch64 protobuf
```
A json file, `result.json`, will be generated in current directory once the scan is successfully executed.

### How to read the result
The JSON result is organized as following format:
```output
{
    "arch": "aarch64",
    "branch": "v2.5.0",
    "commit": null,
    "errors": [],
    "file_summary": {
        "asm": {
            "count": 0,
            "fileName": "Assembly",
            "loc": 0
        },
        "c": {
            "count": 93,
            "fileName": "C",
            "loc": 29031
        },
        "config.guess": {
            "count": 0,
            "fileName": "Autoconf",
            "loc": 0
        },
        "cpp": {
            "count": 113,
            "fileName": "CPP",
            "loc": 79010
        },
        "makefile": {
            "count": 4,
            "fileName": "Makefile",
            "loc": 719
        }
    },
    "git_repo": "https://github.com/protocolbuffers/protobuf.git",
    "issue_summary": {
         "ArchSpecificLibraryIssue": {
            "count": 0,
            "des": "Use of libraries strongly tied to the processor architecture, which may lead to compatibility issues."
        },
        ....
        "PreprocessorErrorIssue": {
            "count": 15,
            "des": "Target platform may enter the #error preprocessing logic"
        },
        "SignedCharIssue": {
            "count": 0,
            "des": "Compatibility issues with signed char type data"
        }
    },
    "issue_type_config": null,
    "issues": [
        {
            "checkpoint": null,
            "description": "preprocessor error: #error \"We require at least vs2005 for MemoryBarrier\"",
            "filename": "/home/my_repo/src/google/protobuf/stubs/atomicops_internals_x86_msvc.h",
            "issue_type": {
                "des": "Target platform may enter the #error preprocessing logic.",
                "type": "PreprocessorErrorIssue"
            },
            "lineno": 46,
            "snippet": "namespace google {\nnamespace protobuf {\nnamespace internal {\n\ninline Atomic32 NoBarrier_AtomicIncrement(volatile Atomic32* ptr,\n                                          Atomic32 increment) {\n  return Barrier_AtomicIncrement(ptr, increment);\n}\n\n#if !(defined(_MSC_VER) && _MSC_VER >= 1400)\n<font style='color:red;'>#error \"We require at least vs2005 for MemoryBarrier\"</font>\n#endif\n\ninline Atomic32 Acquire_CompareAndSwap(volatile Atomic32* ptr,\n                                       Atomic32 old_value,\n                                       Atomic32 new_value) {\n  return NoBarrier_CompareAndSwap(ptr, old_value, new_value);\n}\n\ninline Atomic32 Release_CompareAndSwap(volatile Atomic32* ptr,\n                                       Atomic32 old_value,\n"
        },
        ...
        {
            "checkpoint": ".*[= \"]+-O2[ \\n\"]+.*",
            "description": "\nWhen the compiler optimization option is set to \"-O2\" level or above, the calculation results of the same floating-point multiplication and addition operation on the x86 platform and the ARM64 platform have differences in the 16 decimal places.\n\nReason:\n\n  When the compiler optimization option is set to \"-O2\" level or above on the ARM64 platform, the precision of the floating-point multiplication and addition operation (a+=b*c) can only be accurate to 16 decimal places. When configuring the \"-O2\" option, gcc uses the fused instruction fmadd to complete the multiplication and addition operation instead of fadd and fmul.\n\n  fmadd regards the multiplication and addition of floating-point numbers as an inseparable operation and does not round the intermediate results, resulting in different calculation results.\n\nImpact on the system:\n\n  When the compiler optimization option is set to \"-O2\" level or above, the performance of floating-point multiplication and addition operations is improved, but the accuracy of the operation is affected.\n\nSolution:\n\n  Add the compilation option \"-ffp-contract=off\" This optimization can be turned off.\n\n",
            "filename": "protobuf/more_tests/Makefile",
            "issue_type": {
                "des": "Potential compatibility issues related to the compilation build commands",
                "type": "BuildCommandIssue"
            },
            "lineno": 40,
            "snippet": "\t(cd src && make install)\n\n# Verify that headers produce no warnings even under strict settings.\nheader_warning_test.cc: target\n\t( (cd target/include && find google/protobuf -name '*.h') | \\\n\t  awk '{print \"#include \\\"\"$$1\"\\\"\"} ' > header_warning_test.cc )\n\nheader_warning_test: header_warning_test.cc\n\t# TODO(kenton):  Consider adding -pedantic and -Weffc++.  Currently these\n\t#   produce tons of extra warnings so we'll need to do some work first.\n\t<font style='color:red;'>g++ -Itarget/include -Wall -Werror -Wsign-compare -O2 -c header_warning_test.cc</font>\n",
            "target": null
        }
    ],
    "language_type": "cpp",
    "march": null,
    "output": null,
    "progress": true,
    "quiet": false,
    "remarks": [],
    "root_directory": "protobuf",
    "source_dirs": [
        "protobuf/src/google/protobuf/compiler/cpp",
        ...
    ],
    "source_files": [
        "protobuf/Makefile.am",
        ...
    ],
    "target_os": "OpenAnolis",
    "total_issue_count": 14
}
```
The items in result are well self-explained along with their keys.
User needs to check `issue_summary` and `issues` to uncover what potential problems are and suggested solutions.

The `issue_summary` provides an overview of the types of issues that the current scanner supports, along with the corresponding number of issues. For `cpp` scanner, the available issue types are:

For each of programming Languages, the available issue types are:
{{< tabpane code=true >}}
  {{< tab header="C++, C">}}
    ArchSpecificLibrary
    AsmSource
    Avx256Intrinsic
    Avx512Intrinsic
    BuildCommand
    CompilerSpecific
    ConfigGuess
    CrossCompile
    DefineOtherArch
    HostCpuDetection
    InlineAsm
    Intrinsic
    NoEquivalent
    NoEquivalentInlineAsm
    NoEquivalentIntrinsic
    OldCrt
    PragmaSimd
    PreprocessorError
  {{< /tab >}}
  {{< tab header="Go">}}
  {{< /tab >}}
  {{< tab header="Python">}}
  {{< /tab >}}
  {{< tab header="Rust">}}
  {{< /tab >}}
  {{< tab header="Java">}}
  {{< /tab >}}
  {{< tab header="Dockerfile">}}
  {{< /tab >}}
{{< /tabpane >}}

The `issues` is a list of those detected issues with details for each of them.
- `checkpoint`: A pattern to identify potential incompatibility.
- `description`: The description of the detected issue.
- `filename`: The file in which issue is detected.
- `issue_type`: The type of issue, including detailed descriptions of the error.
- `lineno`: The line number of the problematic code.
- `snippet`: The block of the problematic code.

For more information about issue type information perf review [migrate-ease github](https://github.com/migrate-ease/migrate-ease/blob/main/README.md).
