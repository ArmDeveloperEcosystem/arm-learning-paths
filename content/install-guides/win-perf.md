---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: WindowsPerf

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- perf
- os woa

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

### Link to official documentation
official_docs: https://gitlab.com/Linaro/WindowsPerf/windowsperf/-/blob/main/wperf/README.md 

author_primary: Jason Andrews

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

WindowsPerf is an open-source command line tool for performance analysis on Windows on Arm devices.

WindowsPerf consists of a kernel-mode driver and a user-space command-line tool. The command-line tool is modeled after the Linux `perf` command. 

WindowsPerf includes a **counting model** for counting events such as cycles, instructions, and cache events and a **sampling model** to understand how frequently events occur.  

## Download and install

[WindowsPerf releases](https://gitlab.com/Linaro/WindowsPerf/windowsperf/-/releases/) are available on GitLab and packaged as zip files.

Follow the instructions to download and install WindowsPerf.

1. Download the zip file

Download version 2.4.0 by clicking on [windowsperf-bin-2.4.0.zip](https://gitlab.com/api/v4/projects/40381146/packages/generic/windowsperf/2.4.0/windowsperf-bin-2.4.0.zip)

You can also download from the Windows Command Prompt:

```console
curl https://gitlab.com/api/v4/projects/40381146/packages/generic/windowsperf/2.4.0/windowsperf-bin-2.4.0.zip --output windowsperf-bin-2.4.0.zip
```

2. Extract the .zip file

Use Windows File Explorer to navigate to your Downloads, right click on the .zip file and select `Extract All...`

You can also unzip the file from the Windows Command Prompt:

```console
tar -xmf windowsperf-bin-2.4.0.zip
```

Change to the newly created directory:

```console
cd windowsperf-bin-2.4.0
```

3. Copy the driver install file

Use the File Explorer to copy the file `wperf-devgen.exe` to the `wperf-driver` subdirectory.

You can also copy from the Windows Command Prompt:

```console
copy wperf-devgen.exe wperf-driver
```

Change to the driver subdirectory:

```console
cd wperf-driver
```

4. Install the driver

{{% notice  Note%}}
You must install the driver as Administrator
{{% /notice %}}

Open a Command Prompt as Administrator. 

Click on the Windows 11 Search box, enter `command` to locate the Command Prompt application, and click on `Run as administrator`.

Using the Administrator Command Prompt change directory to the `wperf-driver` directory: 

```console
cd Downloads\windowsperf-bin-2.4.0\wperf-driver
```

{{% notice  Note%}}
You may need to navigate back to the Downloads directory depending on where the Command Prompt starts.
{{% /notice %}}

Install the driver:

```console
wperf-devgen.exe install
```

The output should be:

```output
Executing command: install.
Install requested.
Waiting for device creation...
Device installed successfully.
Trying to install driver...
Success installing driver.
```

You are now ready to use `wperf`

## Check the installation

{{% notice  Note%}}
You do not need to be Administrator to run `wperf`
{{% /notice %}}

Run `wperf.exe` and print the help message:

```console
wperf --help
```

The output should be a long list of command line options. 

To list the events which can be counted run:

```console
wperf list
```

The output should be similar to:

```output
List of pre-defined events (to be used in -e)

        Alias Name              Raw Index  Event Type
        ==========              =========  ==========
        sw_incr                      0x00  [core PMU event]
        l1i_cache_refill             0x01  [core PMU event]
        l1i_tlb_refill               0x02  [core PMU event]
        l1d_cache_refill             0x03  [core PMU event]
        l1d_cache                    0x04  [core PMU event]
        l1d_tlb_refill               0x05  [core PMU event]
        ld_retired                   0x06  [core PMU event]
        st_retired                   0x07  [core PMU event]
        inst_retired                 0x08  [core PMU event]
        exc_taken                    0x09  [core PMU event]
        exc_return                   0x0a  [core PMU event]
        cid_write_retired            0x0b  [core PMU event]
        pc_write_retired             0x0c  [core PMU event]
        br_immed_retired             0x0d  [core PMU event]
        br_return_retired            0x0e  [core PMU event]
        unaligned_ldst_retired       0x0f  [core PMU event]
        br_mis_pred                  0x10  [core PMU event]
        cpu_cycles                   0x11  [core PMU event]
        br_pred                      0x12  [core PMU event]
        mem_access                   0x13  [core PMU event]
        l1i_cache                    0x14  [core PMU event]
        l1d_cache_wb                 0x15  [core PMU event]
        l2d_cache                    0x16  [core PMU event]
        l2d_cache_refill             0x17  [core PMU event]
        l2d_cache_wb                 0x18  [core PMU event]
        bus_access                   0x19  [core PMU event]
        memory_error                 0x1a  [core PMU event]
        inst_spec                    0x1b  [core PMU event]
        ttbr_write_retired           0x1c  [core PMU event]
        bus_cycles                   0x1d  [core PMU event]
        chain                        0x1e  [core PMU event]
        l1d_cache_allocate           0x1f  [core PMU event]
        l2d_cache_allocate           0x20  [core PMU event]
        br_retired                   0x21  [core PMU event]
        br_mis_pred_retired          0x22  [core PMU event]
        stall_frontend               0x23  [core PMU event]
        stall_backend                0x24  [core PMU event]
        l1d_tlb                      0x25  [core PMU event]
        l1i_tlb                      0x26  [core PMU event]
        l2i_cache                    0x27  [core PMU event]
        l2i_cache_refill             0x28  [core PMU event]
        l3d_cache_allocate           0x29  [core PMU event]
        l3d_cache_refill             0x2a  [core PMU event]
        l3d_cache                    0x2b  [core PMU event]
        l3d_cache_wb                 0x2c  [core PMU event]
        l2d_tlb_refill               0x2d  [core PMU event]
        l2i_tlb_refill               0x2e  [core PMU event]
        l2d_tlb                      0x2f  [core PMU event]
        l2i_tlb                      0x30  [core PMU event]
        remote_access                0x31  [core PMU event]
        ll_cache                     0x32  [core PMU event]
        ll_cache_miss                0x33  [core PMU event]
        dtlb_walk                    0x34  [core PMU event]
        itlb_walk                    0x35  [core PMU event]
        ll_cache_rd                  0x36  [core PMU event]
        ll_cache_miss_rd             0x37  [core PMU event]
        remote_access_rd             0x38  [core PMU event]
        l1d_cache_lmiss_rd           0x39  [core PMU event]
        op_retired                   0x3a  [core PMU event]
        op_spec                      0x3b  [core PMU event]
        stall                        0x3c  [core PMU event]
        stall_slot_backend           0x3d  [core PMU event]
        stall_slot_frontend          0x3e  [core PMU event]
        stall_slot                   0x3f  [core PMU event]
        ldrex_spec                   0x6c  [core PMU event]
        strex_pass_spec              0x6d  [core PMU event]
        strex_fail_spec              0x6e  [core PMU event]
        strex_spec                   0x6f  [core PMU event]
        ld_spec                      0x70  [core PMU event]
        st_spec                      0x71  [core PMU event]
        ldst_spec                    0x72  [core PMU event]
        dp_spec                      0x73  [core PMU event]
        ase_spec                     0x74  [core PMU event]
        vfp_spec                     0x75  [core PMU event]
        pc_write_spec                0x76  [core PMU event]
        crypto_spec                  0x77  [core PMU event]
        br_immed_spec                0x78  [core PMU event]
        br_return_spec               0x79  [core PMU event]
        br_indirect_spec             0x7a  [core PMU event]

List of supported metrics (to be used in -m)

        Metric  Events
        ======  ======
        dcache  {l1d_cache,l1d_cache_refill,l2d_cache,l2d_cache_refill,inst_retired}
        dtlb    {l1d_tlb,l1d_tlb_refill,l2d_tlb,l2d_tlb_refill,inst_retired}
        icache  {l1i_cache,l1i_cache_refill,l2i_cache,l2i_cache_refill,inst_retired}
        imix    {inst_spec,dp_spec,vfp_spec,ase_spec,ldst_spec}
        itlb    {l1i_tlb,l1i_tlb_refill,l2i_tlb,l2i_tlb_refill,inst_retired}

```

You have successfully installed WindowsPerf on your Windows on Arm device and can begin using it for performance analysis. 

## Uninstall the driver

You can uninstall the driver if you do not want to use `wperf` anymore.

{{% notice  Note%}}
You must uninstall the driver as Administrator
{{% /notice %}}

Use the `uninstall` command to uninstall the driver:

```console
wperf-devgen.exe uninstall
```
