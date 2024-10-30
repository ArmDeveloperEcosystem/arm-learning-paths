---
title: Performance API (PAPI)
minutes_to_complete: 15
official_docs: https://github.com/icl-utk-edu/papi/wiki/Downloading-and-Installing-PAPI
author_primary: Jason Andrews
additional_search_terms:
- perf

test_images:
- ubuntu:latest
test_maintenance: true

### FIXED, DO NOT MODIFY
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

Performance Application Programming Interface (PAPI) provides a consistent library of functions for accessing performance counters from an application.

You can use PAPI in your source code to access performance counters and profile specific sections of your application.

PAPI is available as source code on GitHub.

## Before you begin

This article provides concise instructions to download, build, and install PAPI on Arm Linux distributions.

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

You need `gcc` and `make` to build PAPI.

Use the Linux package manager to install the required software packages on your Linux distribution.

For Debian based distributions (including Ubuntu) run:

```bash { target="ubuntu:latest" }
sudo apt update -y
sudo apt install -y make gcc
```

## Download, build, install, and test PAPI

1. Clone the PAPI repository:

```bash { target="ubuntu:latest" }
git clone https://github.com/icl-utk-edu/papi/
```

2. Configure and compile the source code:

```bash { target="ubuntu:latest" }
cd papi/src
chmod +x configure
./configure
make
```

3. Configure and compile the source code:

```bash { target="ubuntu:latest" }
cd src
make install
```

4. Copy the test program below and paste it into a text file named `papi-test.c``:

```C { file_name="papi-test.c" }
#include <papi.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Initialize the PAPI library and print the version
    int ver = PAPI_library_init(PAPI_VER_CURRENT);
    printf("PAPI version is %d.%d\n", PAPI_VERSION_MAJOR(ver), PAPI_VERSION_MINOR(ver));

    exit(0);
}
```

5. Compile and run the application:

```bash { target="ubuntu:latest" }
gcc -o papi-test papi-test.c -Wl,-rpath /usr/local/lib  -lpapi
./papi-test
```

The output will be similar to:

```output
PAPI version is 7.0
```

Your version may be slightly different but that is fine.

You are now ready to use PAPI in your own applications.
