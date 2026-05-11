---
title: Install and test the OpenJDK JVM for PAC/BTI enablement
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install the default OpenJDK JVM

Install the default OpenJDK Java VM:

```bash
sudo zypper refresh
sudo zypper install -y java
```

Confirm the newly installed JVM:

```bash
java --version
```

Output should be similar to:

```output
openjdk 17.0.13 2024-10-15
OpenJDK Runtime Environment (build 17.0.13+11-suse-150400.3.48.2-aarch64)
OpenJDK 64-Bit Server VM (build 17.0.13+11-suse-150400.3.48.2-aarch64, mixed mode, sharing)
```

Next, download and run a script to confirm PAC/BTI readiness in the JVM you just installed.

## Set up the test script

Copy and paste the following script into your C4A SSH session. Save it as `test-pacbti.sh`:

```bash
#!/usr/bin/env bash
#
# test-pacbti.sh
#
# Purpose:
#   Exercise an OpenJDK JVM on Linux/AArch64 and determine whether the
#   JVM process is running on a platform that exposes Arm Pointer
#   Authentication Code features and Branch Target Identification to
#   userspace.
#
# Expected results:
#   - Armv9 platform with PAC + BTI exposed:
#       FINAL RESULT: POSITIVE
#
#   - Armv8 platform lacking PAC + BTI:
#       FINAL RESULT: NEGATIVE
#
#   - Non-AArch64, missing /proc/self/auxv, or partial exposure:
#       FINAL RESULT: INCONCLUSIVE
#
# What this tests:
#   This script does not merely inspect the host from the shell. It launches
#   a Java probe inside the target JVM. The Java process reads its own
#   /proc/self/auxv, so the HWCAP/HWCAP2 values are those visible to the JVM.
#
# Notes:
#   - PAC and BTI are architectural/security features. On Linux/AArch64,
#     userspace should discover them through AT_HWCAP / AT_HWCAP2.
#   - This intentionally avoids "try the instruction and catch SIGILL" style
#     tests, because Linux kernel documentation says feature probing should
#     use hwcaps.
#   - Some Armv8.x systems may expose PAC and/or BTI. The solid negative
#     requested here applies to Armv8 systems that lack PAC/BTI.
#
# Requirements:
#   - Linux
#   - AArch64 target JVM for meaningful PAC/BTI result
#   - OpenJDK 11+ for Java source-file mode, or javac available as fallback
#
# Usage:
#   chmod +x test-pacbti.sh
#   ./test-pacbti.sh
#
# Optional:
#   JAVA=/path/to/java ./test-pacbti.sh

set -u

JAVA_BIN="${JAVA:-java}"

tmpdir="$(mktemp -d)"
cleanup() {
  rm -rf "${tmpdir}"
}
trap cleanup EXIT

cat > "${tmpdir}/JvmAarch64PacBtiProbe.java" <<'JAVA'
import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.lang.management.ManagementFactory;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.Locale;
import java.util.Map;
import java.util.TreeMap;

public final class JvmAarch64PacBtiProbe {
    /*
     * Linux auxv constants.
     *
     * AT_HWCAP  = 16
     * AT_HWCAP2 = 26
     *
     * Linux AArch64 hwcap bit assignments:
     *   HWCAP_PACA  = 1 << 30
     *   HWCAP_PACG  = 1 << 31
     *   HWCAP2_BTI  = 1 << 17
     */
    private static final long AT_NULL = 0L;
    private static final long AT_HWCAP = 16L;
    private static final long AT_HWCAP2 = 26L;

    private static final long HWCAP_PACA = 1L << 30;
    private static final long HWCAP_PACG = 1L << 31;
    private static final long HWCAP2_BTI = 1L << 17;

    public static void main(String[] args) throws Exception {
        String osName = System.getProperty("os.name", "unknown");
        String osArch = System.getProperty("os.arch", "unknown");
        String vmName = System.getProperty("java.vm.name", "unknown");
        String vmVersion = System.getProperty("java.vm.version", "unknown");
        String runtimeVersion = System.getProperty("java.runtime.version", "unknown");

        System.out.println("=== JVM AArch64 PAC/BTI Probe ===");
        System.out.println("Process PID          : " + currentPid());
        System.out.println("Java VM              : " + vmName);
        System.out.println("Java VM version      : " + vmVersion);
        System.out.println("Java runtime version : " + runtimeVersion);
        System.out.println("os.name              : " + osName);
        System.out.println("os.arch              : " + osArch);
        System.out.println();

        boolean linux = osName.toLowerCase(Locale.ROOT).contains("linux");
        boolean aarch64 =
            osArch.equalsIgnoreCase("aarch64") ||
            osArch.equalsIgnoreCase("arm64");

        if (!linux) {
            System.out.println("FINAL RESULT: INCONCLUSIVE");
            System.out.println("Reason      : This probe is Linux-specific because it uses /proc/self/auxv.");
            System.exit(2);
        }

        if (!aarch64) {
            System.out.println("FINAL RESULT: INCONCLUSIVE");
            System.out.println("Reason      : JVM is not executing as AArch64/arm64.");
            System.exit(2);
        }

        Map<Long, Long> auxv;
        try {
            auxv = readAuxv();
        } catch (IOException ex) {
            System.out.println("FINAL RESULT: INCONCLUSIVE");
            System.out.println("Reason      : Could not read /proc/self/auxv from inside the JVM.");
            System.out.println("Exception   : " + ex);
            System.exit(2);
            return;
        }

        long hwcap = auxv.getOrDefault(AT_HWCAP, 0L);
        long hwcap2 = auxv.getOrDefault(AT_HWCAP2, 0L);

        boolean paca = (hwcap & HWCAP_PACA) != 0;
        boolean pacg = (hwcap & HWCAP_PACG) != 0;
        boolean pac = paca || pacg;
        boolean bti = (hwcap2 & HWCAP2_BTI) != 0;

        System.out.printf("AT_HWCAP             : 0x%016x%n", hwcap);
        System.out.printf("AT_HWCAP2            : 0x%016x%n", hwcap2);
        System.out.println();

        System.out.println("Decoded AArch64 features visible to this JVM process:");
        System.out.println("  HWCAP_PACA         : " + yesNo(paca));
        System.out.println("  HWCAP_PACG         : " + yesNo(pacg));
        System.out.println("  PAC present        : " + yesNo(pac));
        System.out.println("  HWCAP2_BTI         : " + yesNo(bti));
        System.out.println();

        if (pac && bti) {
            System.out.println("FINAL RESULT: POSITIVE");
            System.out.println("Meaning     : The JVM is executing on Linux/AArch64 with PAC and BTI exposed to userspace.");
            System.exit(0);
        }

        if (!pac && !bti) {
            System.out.println("FINAL RESULT: NEGATIVE");
            System.out.println("Meaning     : The JVM is executing on Linux/AArch64 without PAC and BTI exposed to userspace.");
            System.out.println("Expected    : This is the expected solid negative on Armv8 systems that lack PAC/BTI.");
            System.exit(1);
        }

        System.out.println("FINAL RESULT: INCONCLUSIVE");
        System.out.println("Meaning     : Only part of the expected PAC/BTI feature set is exposed.");
        System.out.println("Detail      : PAC=" + yesNo(pac) + ", BTI=" + yesNo(bti));
        System.exit(2);
    }

    private static String yesNo(boolean value) {
        return value ? "YES" : "NO";
    }

    private static long currentPid() {
        try {
            return ProcessHandle.current().pid();
        } catch (Throwable ignored) {
            String name = ManagementFactory.getRuntimeMXBean().getName();
            int at = name.indexOf('@');
            if (at > 0) {
                try {
                    return Long.parseLong(name.substring(0, at));
                } catch (NumberFormatException ignoredAgain) {
                    return -1L;
                }
            }
            return -1L;
        }
    }

    private static Map<Long, Long> readAuxv() throws IOException {
        byte[] data = readAll("/proc/self/auxv");

        /*
         * On AArch64 Linux, auxv entries in a 64-bit process are pairs of
         * unsigned long values:
         *
         *   a_type, a_val
         *
         * Java long is signed, but bit testing is unaffected.
         */
        if (data.length % 16 != 0) {
            throw new IOException("Unexpected auxv size for 64-bit process: " + data.length);
        }

        ByteBuffer bb = ByteBuffer.wrap(data).order(ByteOrder.nativeOrder());
        Map<Long, Long> out = new TreeMap<>();

        while (bb.remaining() >= 16) {
            long type = bb.getLong();
            long value = bb.getLong();

            if (type == AT_NULL) {
                break;
            }

            out.put(type, value);
        }

        return out;
    }

    private static byte[] readAll(String path) throws IOException {
        try (FileInputStream in = new FileInputStream(path);
             ByteArrayOutputStream out = new ByteArrayOutputStream()) {
            byte[] buf = new byte[4096];
            int n;
            while ((n = in.read(buf)) >= 0) {
                out.write(buf, 0, n);
            }
            return out.toByteArray();
        }
    }
}
JAVA

echo "=== OpenJDK JVM PAC/BTI platform exercise ==="
echo "Using java: ${JAVA_BIN}"
echo

if ! command -v "${JAVA_BIN}" >/dev/null 2>&1; then
  echo "FINAL RESULT: INCONCLUSIVE"
  echo "Reason      : java executable not found: ${JAVA_BIN}"
  exit 2
fi

echo "--- java -version ---"
"${JAVA_BIN}" -version 2>&1
echo

echo "--- JVM branch-protection flag visibility check ---"
echo "This is informational. The final result comes from the JVM process auxv probe."
if "${JAVA_BIN}" -XX:+UnlockDiagnosticVMOptions -XX:+PrintFlagsFinal -version 2>&1 \
    | grep -E 'UseBranchProtection|BranchProtection' ; then
  :
else
  echo "No UseBranchProtection flag printed. This can happen with older JVMs or builds that do not expose the flag."
fi
echo

echo "--- Optional runtime flag exercise: -XX:UseBranchProtection=standard ---"
echo "This should be accepted by branch-protection-aware OpenJDK builds; older builds may reject it."
if "${JAVA_BIN}" -XX:UseBranchProtection=standard -version >/tmp/jvm_pac_bti_flag_check.out 2>&1; then
  echo "Accepted: -XX:UseBranchProtection=standard"
else
  echo "Not accepted or not supported by this JVM:"
  sed 's/^/  /' /tmp/jvm_pac_bti_flag_check.out
fi
rm -f /tmp/jvm_pac_bti_flag_check.out
echo

echo "--- Running in-JVM auxv probe ---"

# Prefer Java source-file mode, available in modern OpenJDK.
# Fall back to javac if needed.
"${JAVA_BIN}" "${tmpdir}/JvmAarch64PacBtiProbe.java"
rc=$?

if [ "${rc}" -eq 0 ]; then
  exit 0
elif [ "${rc}" -eq 1 ]; then
  exit 1
else
  if command -v javac >/dev/null 2>&1; then
    echo
    echo "Source-file mode failed or was unavailable; retrying with javac fallback..."
    javac "${tmpdir}/JvmAarch64PacBtiProbe.java" &&
      "${JAVA_BIN}" -cp "${tmpdir}" JvmAarch64PacBtiProbe
    exit $?
  fi

  exit "${rc}"
fi
```

## Run the test script

In your SSH session, run the test script to confirm PAC/BTI enablement:

```bash
chmod 755 ./test-pacbti.sh
./test-pacbti.sh
```

Output should resemble:

```output
=== OpenJDK JVM PAC/BTI platform exercise ===
Using java: java

--- java -version ---
openjdk version "17.0.13" 2024-10-15
OpenJDK Runtime Environment (build 17.0.13+11-suse-150400.3.48.2-aarch64)
OpenJDK 64-Bit Server VM (build 17.0.13+11-suse-150400.3.48.2-aarch64, mixed mode, sharing)

--- JVM branch-protection flag visibility check ---
This is informational. The final result comes from the JVM process auxv probe.
No UseBranchProtection flag printed. This can happen with older JVMs or builds that do not expose the flag.

--- Optional runtime flag exercise: -XX:UseBranchProtection=standard ---
This should be accepted by branch-protection-aware OpenJDK builds; older builds may reject it.
Not accepted or not supported by this JVM:
  Unrecognized VM option 'UseBranchProtection=standard'
  Error: Could not create the Java Virtual Machine.
  Error: A fatal exception has occurred. Program will exit.

--- Running in-JVM auxv probe ---
=== JVM AArch64 PAC/BTI Probe ===
Process PID          : 3523
Java VM              : OpenJDK 64-Bit Server VM
Java VM version      : 17.0.13+11-suse-150400.3.48.2-aarch64
Java runtime version : 17.0.13+11-suse-150400.3.48.2-aarch64
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
```

## What you've learned and what's next

Most OpenJDK builds are distributed with PAC/BTI enabled but optionally used by default because they must remain compatible with older Arm platforms. When you need these protections, you can build and register your own JVM with branch protection support.

When a PAC/BTI-enabled JVM runs on a platform that supports these features, Java workloads gain additional control-flow protection.
