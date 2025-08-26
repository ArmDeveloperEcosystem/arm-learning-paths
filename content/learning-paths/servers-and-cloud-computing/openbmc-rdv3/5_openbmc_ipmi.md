---
title: Customize IPMI Commands in OpenBMC
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Customize IPMI Commands in OpenBMC

The Intelligent Platform Management Interface (IPMI) is a standardized protocol used to manage and monitor servers independently of the operating system. In OpenBMC, IPMI support is built in and can be extended with custom commands using the D-Bus/IPMI handler infrastructure.

In this module, you'll learn how to create a simple IPMI command that responds with a custom string. This includes writing a C++ handler, adding a BitBake recipe, integrating it into the build, and verifying it using ipmitool inside the simulated FVP environment.



### Step 1: Create a BitBake Recipe

Create a new file named phosphor-ipmi-example.bb at:

~/openbmc/meta-evb/meta-evb-arm/meta-evb-fvp-base/recipes-phosphor/ipmi/

Paste the following content:

```bash
SUMMARY = "Custom IPMI commands"
LICENSE = "CLOSED"
PR = "r1"
SRC_URI = "file://fvp-ipmi.cpp"
S = "${UNPACKDIR}"

DEPENDS += "phosphor-ipmi-host sdbusplus systemd"
TARGET_CXXFLAGS += " -std=c++23"
TARGET_LDFLAGS += " -lsystemd -lsdbusplus"

do_compile() {
    ${CXX} ${TARGET_CXXFLAGS} -fPIC -shared \
    -o libmyipmi.so ${UNPACKDIR}/fvp-ipmi.cpp \
    -I${STAGING_INCDIR} -L${STAGING_LIBDIR} \
    ${TARGET_LDFLAGS}
}

do_install() {
    install -d ${D}${libdir}/ipmid-providers
    install -m 0644 libmyipmi.so ${D}${libdir}/ipmid-providers/
}

FILES:${PN} += "${libdir}/ipmid-providers/libmyipmi.so"
```

### Step 2: Create a Custom IPMI Handler

Create a folder phosphor-ipmi-example at the same path, and add a new file fvp-ipmi.cpp:

```c++
#include <ipmid/api.hpp>
#include <ipmid/utils.hpp>
#include <string>

ipmi::RspType<std::string> myIpmiCommand() {
    std::string reply = "Hello from OpenBMC IPMI!";
    return ipmi::responseSuccess(reply);
}

void register_my_ipmi() __attribute__((constructor));
void register_my_ipmi() {
    ipmi::registerHandler(ipmi::prioOemBase, 0x30, 0x20,
                          ipmi::Privilege::Admin, myIpmiCommand);
}
```

{{% notice %}}
OEM NetFn codes range from 0x30–0x3F. Avoid using reserved or conflicting NetFn/command combinations.
{{% /notice %}}


### Step 3: Add to Build Configuration

Edit fvp.conf at:

~/openbmc/meta-evb/meta-evb-arm/meta-evb-fvp-base/conf/machine/fvp.conf

Append the following packages to your image:

IMAGE_INSTALL:append = " phosphor-ipmi-example ipmitool "

Now rebuild the OpenBMC image with your IPMI handler included:

```bash
bitbake obmc-phosphor-image
```

### Step 4: Verify the IPMI Command in Simulation

After launching your FVP simulation and logging into the OpenBMC console, run:

```bash
ipmitool raw 0x30 0x20
```

Expected output:
```
root@fvp:~# ipmitool raw 0x30 0x20
18 48 65 6c 6c 6f 20 66 72 6f 6d 20 4f 70 65 6e 42 4d 43 20 49 50 4d 49 21
```

How to Interpret the Output:

The response is a raw hex stream:

* 0x18 = 24 bytes of payload
* The following bytes represent: "Hello from OpenBMC IPMI!"

You’ve successfully added a custom IPMI command and verified its output through the simulated platform.

