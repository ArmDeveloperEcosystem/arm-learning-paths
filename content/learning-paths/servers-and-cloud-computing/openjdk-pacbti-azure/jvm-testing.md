---
title: Test the installed JVM for PAC/BTI enablement
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Set up the test script

Clone this repo and set execute permissions for the downloaded test script:

```bash
git clone https://github.com/DougAnsonAustinTx/pac-bti-jdk-assets 
cd pac-bti-jdk-assets
chmod 755 ./test-pacbti.sh
```

## Run the test script

Run the test script to confirm PAC/BTI enablement:

```bash
./test-pacbti.sh --java /usr/bin/java
```

Output should resemble:

```output
== JVM PAC/BTI check ==
java executable : /home/ubuntu/jdk/build/linux-aarch64-server-release/jdk/bin/java
libjvm          : /home/ubuntu/jdk/build/linux-aarch64-server-release/jdk/lib/server/libjvm.so

-- Host support (auxv/hwcaps) --
PAC APIA/generic support : yes (PACA=yes PACG=yes)
BTI support              : yes

-- JVM support/config --
UseBranchProtection flag : yes
JVM default flag value   : {default}

-- Binary instruction scan --
java contains PAC instr  : yes
java contains BTI instr  : yes
libjvm contains PAC instr: no
libjvm contains BTI instr: no

-- Verdict --
PAC status               : possible-but-not-proven
BTI status               : yes

Interpretation:
  PAC-capable build detected, but no running JVM cmdline was checked.
  BTI is likely enabled in the runtime binaries.
```

## What you've learned

Some OpenJDK builds are not distributed with PAC/BTI enabled by default because they must remain compatible with older Arm platforms. When you need these protections, you can build and register your own JVM with branch protection support.

When a PAC/BTI-enabled JVM runs on a platform that supports these features, Java workloads gain additional control-flow protection.
