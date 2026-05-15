---
title: Test PAC/BTI support with Oracle JDK
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install the Oracle JDK

The SUSE-packaged OpenJDK 17 confirmed that the C4A platform exposes PAC and BTI, but its JIT compiler doesn't emit PAC/BTI instructions. Oracle's JDK 21 for Linux/AArch64 is built with `--enable-branch-protection`, so the JIT compiler generates PAC/BTI instructions in compiled Java code.

Download and install Oracle JDK 21:

```bash
curl -LO https://download.oracle.com/java/21/latest/jdk-21_linux-aarch64_bin.tar.gz
tar xzf jdk-21_linux-aarch64_bin.tar.gz
```

Confirm the installation:

```bash
./jdk-21.0.11/bin/java --version
```

{{% notice Note %}}
The minor version number in the directory name (e.g., `21.0.11`) may differ depending on when you download. Check the extracted directory name with `ls` and adjust the path accordingly.
{{% /notice %}}

The output is similar to:

```output
java version 21.0.11 2026-04-21 LTS
Java(TM) SE Runtime Environment (build 21.0.11+9-LTS-211)
Java HotSpot(TM) 64-Bit Server VM (build 21.0.11+9-LTS-211, mixed mode, sharing)
```

## Run the PAC/BTI test with the Oracle JDK

Use the same `test-pacbti.sh` script from the previous step, pointing it at the Oracle JDK:

```bash
JAVA=./jdk-21.0.11/bin/java ./test-pacbti.sh
```

This runs the same three checks (flag visibility, branch protection flag exercise, and the in-JVM auxv probe) against the Oracle JDK instead of the system JDK.

The output is similar to:

```output
=== OpenJDK JVM PAC/BTI platform exercise ===
Using java: ./jdk-21.0.11/bin/java

--- java -version ---
java version "21.0.11" 2026-04-21 LTS
Java(TM) SE Runtime Environment (build 21.0.11+9-LTS-211)
Java HotSpot(TM) 64-Bit Server VM (build 21.0.11+9-LTS-211, mixed mode, sharing)

--- JVM branch-protection flag visibility check ---
This is informational.
    ccstr UseBranchProtection                      = none                                 {ARCH product} {default}

--- Optional runtime flag exercise: -XX:UseBranchProtection=standard ---
This should be accepted by branch-protection-aware OpenJDK builds; older builds may reject it.
Accepted: -XX:UseBranchProtection=standard

--- Running in-JVM auxv probe ---
=== JVM AArch64 PAC/BTI Probe ===
Process PID          : 4916
Java VM              : Java HotSpot(TM) 64-Bit Server VM
Java VM version      : 21.0.11+9-LTS-211
Java runtime version : 21.0.11+9-LTS-211
os.name              : Linux
os.arch              : aarch64

AT_HWCAP             : 0x00000000efffffff
AT_HWCAP2            : 0x000000000003f3ff

Decoded AArch64 features visible to this JVM process:
  HWCAP_PACA         : YES
  HWCAP_PACG         : YES
  PAC present        : YES
  HWCAP2_BTI         : YES

FINAL RESULT: POSITIVE
Meaning     : The JVM is executing on Linux/AArch64 with PAC and BTI exposed to userspace.

===========================================
  SUMMARY
===========================================
  Platform PAC/BTI (hardware + kernel): YES
  JVM JIT PAC/BTI support:              YES

  FULL PAC/BTI SUPPORT
  The platform exposes PAC/BTI and this JVM can use it in JIT-compiled code.
  Use -XX:UseBranchProtection=standard to enable it.
===========================================
```

## Interpret the results

The Oracle JDK 21 output shows three key improvements over the SUSE OpenJDK 17:

- **`UseBranchProtection` flag is visible.** The JVM exposes this as a configurable option, confirming it was built with branch protection support.
- **`-XX:UseBranchProtection=standard` is accepted.** The JIT compiler can be told to emit PAC/BTI instructions in compiled Java code.
- **SUMMARY shows FULL PAC/BTI SUPPORT.** The platform exposes PAC/BTI and the JVM JIT can use it.

The default value of `UseBranchProtection = none` means the JIT doesn't emit PAC/BTI instructions unless you opt in with `-XX:UseBranchProtection=standard`. This gives you control over whether to enable the feature for your workloads.

| Layer | SUSE OpenJDK 17 | Oracle JDK 21 |
|-------|-----------------|---------------|
| Hardware + kernel | ✅ PAC/BTI exposed | ✅ PAC/BTI exposed |
| OS and native libraries | ✅ Protected | ✅ Protected |
| JVM JIT compiler | ❌ Not enabled | ✅ Available (opt-in via `-XX:UseBranchProtection=standard`) |

✅ Full PAC/BTI protection achieved!

To run your Java application with full PAC/BTI JIT protection:

```bash
./jdk-21.0.11/bin/java -XX:UseBranchProtection=standard -jar your-application.jar
```

## What you've learned

You now have a complete picture of PAC/BTI support for Java on Google Cloud C4A:

- The C4A platform (Arm Neoverse-V2) exposes PAC and BTI to userspace.
- The SUSE-packaged OpenJDK 17 cannot use these features in JIT-compiled code.
- Oracle JDK 21 supports PAC/BTI in the JIT compiler and lets you enable it with a runtime flag.

With `-XX:UseBranchProtection=standard`, the JIT compiler signs return addresses with PAC and marks branch targets with BTI in dynamically compiled Java methods. This extends hardware-enforced control-flow integrity from the OS and native libraries into your Java application code.
