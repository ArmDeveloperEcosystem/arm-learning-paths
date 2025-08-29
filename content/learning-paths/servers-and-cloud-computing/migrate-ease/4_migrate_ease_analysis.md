---
# User change
title: "Try it out"

weight: 5

layout: "learningpathall"

---
### Example use case
In this section, you'll use migrate-ease to scan the source code of [Protobuf](https://github.com/protocolbuffers/protobuf), a widely used library for serializing structured data. 

Support for AArch64 was added in Protobuf version v3.5.0 (November 2017). To demonstrate how migrate-ease detects compatibility issues, you’ll scan an older version — v2.5.0 — which lacks AArch64 support. 

Use migrate-ease to scan protobuf v2.5.0 and output the results to a JSON file named `result.json`:

```bash
python3 -m cpp --git-repo https://github.com/protocolbuffers/protobuf.git --branch v2.5.0 --output result.json --march armv8-a protobuf
```

The scan will generate a file called `result.json` in your current directory.

### How to interpret the results
Open the `result.json` file. It contains structured output similar to this:
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

* The `issue_summary` section provides a high-level overview of AArch64 compatibility issues found. 
* The `issues` array lists each issue, including the file, line number, description, and a code snippet.

### Issue type definitions

Each supported language has its own set of issue types. The tables below describe these by category:
{{< tabpane code=true >}}
  {{< tab header="C++, C">}}
Name                    | Description
------------------------|-------------------------------------------------------------------------------------------------------------
ArchSpecificLibrary     | Architecture-specific libraries that may cause issues on AArch64.
AsmSource               | Potentially architecture-specific assembly code in the source files that requires manual inspection.
Avx256Intrinsic         | AVX256 instructions incompatible with AArch64.
Avx512Intrinsic         | AVX512 instructions incompatible with AArch64.
BuildCommand            | Potential compatibility issues related to the compilation build commands.
CPPLibRecommend         | A better-optimized version of this library may be available.
CPPLibVersion           | This library version may be incompatible with the AArch64 architecture's compiler.
CPPStdCodes             | Compatibility issues or optimization opportunities related to C++ source and memory order on AArch64.
CompilerSpecific        | Code is strongly tied to a compiler version or type, which may lead to compatibility issues.
ConfigGuess             | Config.guess file does not contain configurations for AArch64 and may require adaptation.
CrossCompile            | Cross-compilation compatibility issues.
DefineOtherArch         | Logic in the code that checks for other processor platform types, which may lead to compatibility issues.
HostCpuDetection        | Logic for processor platform types in the Makefile, which may lead to platform compatibility issues.
IncompatibleHeaderFile  | Incompatible header files.
InlineAsm               | Use of inline assembly may lead to AArch64 architecture compatibility issues.
Intrinsic               | Use of intrinsics that have compatibility issues with the AArch64 architecture.
NoEquivalentInlineAsm   | Use of inline assembly code that does not exist on the AArch64 architecture.
NoEquivalentIntrinsic   | Use of intrinsic functions that do not exist on the AArch64 architecture.
OldCrt                  | Use of an older version of the C runtime library, which may cause compatibility issues or miss optimizations.
Pragma                  | This #pragma may be incompatible with the AArch64 architecture's compiler.
PreprocessorError       | AArch64 architecture may enter the #error preprocessing logic.
SignedChar              | Compatibility issues with signed char type data.
  {{< /tab >}}
  {{< tab header="Java">}}
  Name       | Description
------------ | --------------------------------------------------------------------------------------------
JavaJar      | Use of JAR package does not support AArch64 architecture.
JavaPom      | Pom imports java artifact that does not support AArch64 architecture.
JavaSource   | Java source file contains native call that may need modify/rebuild for AArch64 architecture.
  {{< /tab >}}
  {{< tab header="Python">}}
Name              | Description
------------------|-----------------------------------------------------------------------------------------
PythonInlineAsm   | Use of inline assembly in the AArch64 architecture may lead to compatibility issues.
PythonIntrinsic   | Use of intrinsic functions that have compatibility issues with the AArch64 architecture.
PythonLinkLibrary | Use of libraries that are incompatible with the AArch64 architecture.
PythonPackage     | Use of packages that are incompatible with the AArch64 architecture.
  {{< /tab >}}
  {{< tab header="Go">}}
Name              | Description
------------------|-----------------------------------------------------------------------------------------------------
Asm               | Potentially architecture-specific assembly code in the source files that requires manual inspection.
GolangInlineAsm   | Use of inline assembly may lead to AArch64 architecture compatibility issues.
GolangIntrinsic   | Use of intrinsic functions that have compatibility issues with the AArch64 architecture.
GolangLinkLibrary | Use of libraries that are incompatible with the AArch64 architecture.
  {{< /tab >}}
  {{< tab header="Rust">}}
Name              | Description
------------------|-------------------------------------------------------------------------------------
RustInlineAsm     | Use of inline assembly in the AArch64 architecture may lead to compatibility issues.
RustIntrinsic     | Use of intrinsics that have compatibility issues with the AArch64 architecture.
RustLinkLibrary   | Use of libraries that are incompatible with the AArch64 architecture.
  {{< /tab >}}
  {{< tab header="Dockerfile">}}
Name               | Description
-------------------|-----------------------------------------------------------------------------------------------------
ConfigurationInfo  | Configuration parameter used in ENV, ARG or LABEL refers to an architecture that could not be supported.
Image              | A base image is used that might not support AArch64 architecture.
Plugin             | A package used in RUN, CMD or ENTRYPOINT does not support AArch64 architecture.
  {{< /tab >}}
{{< /tabpane >}}

Each entry in the `issues` list contains:
- `checkpoint`: A pattern to identify potential incompatibility.
- `description`: The description of the detected issue.
- `filename`: The file in which issue is detected.
- `issue_type`: Classification and explanation.
- `lineno`:  Line number where the issue appears.
- `snippet`: A snippet of the relevant code.

### Learn more

For more information about issue types, see [migrate-ease github](https://github.com/migrate-ease/migrate-ease/blob/main/README.md).

You have now learned how to install and use migrate-ease to scan a real-world project. You can now use it to scan your source code repositories to identify compatibility issues for AArch64 and use tool's insights to help port your code to Arm platforms.
