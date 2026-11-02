---
title: Creating Heatmaps with BOLT
weight: 15

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Creating Heatmaps with BOLT

{{% notice Note %}}
The example below uses a [BRBE profiling](/learning-paths/servers-and-cloud-computing/bolt/brbe/) optimized binary. You can apply similar steps to binaries optimized using the other BOLT profiling methods, which are covered at the end of this page. Naturally, it is assumed that you have followed the steps for the profiling method you are using. 
{{% /notice %}}

In addition to using hardware metrics to verify the optimisations performed by BOLT, you can also generate heatmaps to make visual comparisons between the layouts of binaries after being processed by BOLT. In a heatmap each character, called a block, represents a number of bytes of code in the binary (this is usually 64 bytes). Based off of the profile used with BOLT:
- A dot (.) means no samples in the profile were recorded for that block, creating a gap in the heatmap. It should be noted that these gaps do not prove that the corresponding code never executes.
- A letter means that samples were recorded in the profile. The letter shows the binary's code section.
- 'o' or 'O' is used to show samples in the profile that belong outside of the known code sections, such as `.text`.

You can find the key to the heatmap in the legend which is produced with the heatmap. Each row in a heatmap starts with a code address which you can use to find the samples in the binary. The amount of code covered by a row depends on the block size and the number of characters per row. If you see blank lines, these indicate larger gaps between sampled regions. To help find samples in a particular row of the heatmap, a hexadecimal guide is printed on the X axis at the top of the heatmap.

## Producing heatmaps

You can produce a heatmap of a binary using the `llvm-bolt-heatmap` tool, using the binary and a matching `perf` measurement, that has been collected whilst running it: 

```bash 
# General form: llvm-bolt-heatmap -p <profile> <executable> <options>
llvm-bolt-heatmap -p prof/brbe.data ./out/bsort -block-size=64 -line-size=100 -print-mappings
```

By default this will be printed to _stdout_, you can redirect this using the `-o` option. Additionally, multiple heatmaps at a range of block sizes will also be printed, you can specify only one to be printed using the `-block-size`  option, in this example block sizes of 64 bytes have been used. The associated sections of the binary and the letters used in the heatmaps can be printed using the `-print-mappings`  option. 

<pre style="background: black; color: white; white-space: pre; overflow-x: auto; padding: 1rem; font-family: monospace;">
...
<span style="background-color:black;"></span><span style="color:white;">Legend:

Ranges:
  o : (0, 4]
  O : (4, 19]
  </span><span style="color:aqua;">O</span><span style="color:white;"> : (19, 89]
  </span><span style="color:lime;">O</span><span style="color:white;"> : (89, 398]
  </span><span style="color:yellow;">O</span><span style="color:white;"> : (398, 1780]
  </span><span style="color:red;">O</span><span style="color:white;"> : (1780, 7956]

Sections:
  a/A : .text      0x00014000-0x000283ac
  b/B : .init      0x000283ac-0x000283c8
  c/C : .fini      0x000283c8-0x000283e0
  d/D : .plt       0x000283e0-0x00028480

            0                                                                                                   
            0                                                               1                                   
            0   1   2   3   4   5   6   7   8   9   a   b   c   d   e   f   0   1   2   3   4   5   6   7   8   
            048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c
            0                                                                                                   
0x00012c00: ................................................................................</span><span style="color:yellow;">A</span><span style="color:white;">.................</span><span style="color:yellow;">AA</span><span style="color:white;">
0x00014500: ....................................</span><span style="color:yellow;">AA</span><span style="color:white;">..............................................................
0x00015e00: ....................................................................................................
0x00017700: ....................................</span><span style="color:yellow;">A</span><span style="color:white;">..................</span><span style="color:yellow;">A</span><span style="color:white;">....................................</span><span style="color:yellow;">AA</span><span style="color:white;">......
0x00019000: ....................................................................................................
0x0001a900: ............................................................................................</span><span style="color:yellow;">A</span><span style="color:white;">.......
0x0001c200: ...........</span><span style="color:yellow;">A</span><span style="color:white;">....................................</span><span style="color:yellow;">AA</span><span style="color:white;">..................................................
0x0001db00: ....................................................................................................
0x0001f400: ................................................</span><span style="color:yellow;">A</span><span style="color:white;">..................</span><span style="color:yellow;">A</span><span style="color:white;">................................
0x00020d00: ....</span><span style="color:yellow;">AA</span><span style="color:white;">..............................................................................................
0x00022600: ....................................................................................................
0x00023f00: ....</span><span style="color:yellow;">A</span><span style="color:white;">..................</span><span style="color:yellow;">A</span><span style="color:white;">....................................</span><span style="color:yellow;">AA</span><span style="color:white;">......................................
0x00025800: ....................................................................................................
0x00027100: ..................................................................</span><span style="color:red;">AAA</span><span style="color:white;">...............................
</span>
...
</pre> 

To produce the heatmap of the binary optimized by BOLT, we must collect additional profile data, using `perf`:

```bash { line_numbers=true}
perf record -j any,u -o prof/bolted-brbe.data -- ./out/bsort.opt.brbe
llvm-bolt-heatmap -p prof/bolted-brbe.data ./out/bsort.opt.brbe \
    -block-size=64 -line-size=100 -print-mappings
```
<pre style="background: black; color: white; white-space: pre; overflow-x: auto; padding: 1rem; font-family: monospace;">
...
<span style="background-color:black;"></span><span style="color:white;">Legend:

Ranges:
  o : (0, 4]
  O : (4, 18]
  </span><span style="color:aqua;">O</span><span style="color:white;"> : (18, 81]
  </span><span style="color:lime;">O</span><span style="color:white;"> : (81, 355]
  </span><span style="color:yellow;">O</span><span style="color:white;"> : (355, 1545]
  </span><span style="color:red;">O</span><span style="color:white;"> : (1545, 6712]

Sections:
  a/A : .bolt.org.text 0x00014000-0x000283ac
  b/B : .init      0x000283ac-0x000283c8
  c/C : .fini      0x000283c8-0x000283e0
  d/D : .plt       0x000283e0-0x00028480
  e/E : .text      0x00400000-0x004001ac
  f/F : .text.cold 0x004001c0-0x0040028c

            0                                                                                                   
            0                                                               1                                   
            0   1   2   3   4   5   6   7   8   9   a   b   c   d   e   f   0   1   2   3   4   5   6   7   8   
            048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c048c
            0                                                                                                   
0x003ff700: ....................................</span><span style="color:yellow;">EEE</span><span style="color:red;">EEE</span><span style="color:yellow;">E</span><span style="color:white;">.........................................................
</span>
...
</pre>

## Verification of layout optimizations using heatmaps
Comparing the heatmaps between the optimized and original binaries, given above, we can see that in the original binary the sampled code is spread across fourteen rows, starting at `0x00012c00` and extending into the row at `0x00027100`. The `A` characters represent sampled execution within the `.text` section. Between these characters are large gaps shown as dots, meaning that no execution activity was captured for those regions in this recording. This matches the layout created earlier, where cold code separates the frequently executed parts of BubbleSort.

We can see that after BOLT has processed the binary, the displayed execution activity in the heatmap is grouped into seven adjacent blocks, shown as `EEEEEEE`, starting at `0x00400000`. As each block represents 64 bytes, these seven blocks cover a 448 byte address range. We can infer that the execution activity is concentrated within a small continuous region of the binary, rather than being spread across widely separated addresses. The sample counts are used to colour each block, importantly calculated ranges are used to choose this colour (as specified by the legend for each individual heatmap), and so some blocks may be of the same colour but have different sample counts. The change from `A` to `E` occurs because the letters identify sections within each binary. In the original binary, `A` represents `.text`. In the optimised binary, `E` represents the new `.text` section containing the rewritten code.

Grouping frequently executed instructions closer together improves spatial locality, which can reduce instruction-cache misses and hence, time spent waiting for instructions. The heatmaps therefore show that BOLT has achieved the intended layout change, whose performance impacts can be confirmed using the [TopDown Methodology](https://developer.arm.com/documentation/109542/02/Arm-Topdown-methodology).

## Useful aids for visualisation
When producing BOLT heatmaps, there are a variety of options that can be used when formatting the heatmap:

```plaintext
-line-size=<uint>   - number of entries per line (default 256). Use a smaller value (e.g. 128) 
                      if the heatmap doesn't fit the screen horizontally.
-block-size=<initial size>[,<zoom-out size>,...] - heatmap block size, optionally followed by 
                      zoom-out sizes to produce coarse-grained heatmaps. Size can be specified 
                      in human-readable format with [kKmMgG][i][B] suffix. Default 64B, 4K, 256K.
-max-address=<uint> - maximum address considered valid for heatmap (default 4GB)
-print-mappings     - print mappings in the legend, between characters/blocks and text sections (default false)
```

As mentioned, heatmaps are printed into _stdout_ or into a file using the `-o` flag. If you prefer to look at the data in a browser (or would like to share it that way), then you can output your heatmap into a text file and use a HTML conversion tool, such as `aha`, which can be installed using `sudo apt install aha` on Ubuntu:  

```bash
mkdir -p heatmap html
llvm-bolt-heatmap -p prof/brbe.data ./out/bsort -block-size=64 -line-size=100 -print-mappings \
    -o ./heatmap/bsort-original.txt
llvm-bolt-heatmap -p prof/bolted-brbe.data ./out/bsort.opt.brbe -block-size=64 -line-size=100 -print-mappings \
    -o ./heatmap/bsort-optimized.txt

# General form: aha -b -f <heatmapfile> > <heatmapfile>.html
aha -b -f ./heatmap/bsort-original.txt > ./html/bsort-original.html
aha -b -f ./heatmap/bsort-optimized.txt > ./html/bsort-optimized.html

```

## Using other profiling methods
The example above makes use of BRBE profiles to produce the heatmaps, the other profiling methods can also be used to produce heatmaps as shown below:  

{{< tabpane-normal >}}
{{< tab header="SPE Profiling" >}}

On an SPE-capable system, you can use `perf` to record branch samples from the original and optimized binaries. This example uses the `arm_spe_0` device. If your system exposes a different name, then use the one shown by `perf list`. 

```bash
mkdir -p prof
perf record -e arm_spe_0/branch_filter=1/u -o prof/spe.data -- ./out/bsort
perf record -e arm_spe_0/branch_filter=1/u -o prof/bolted-spe.data -- ./out/bsort.opt.spe
```

Using these profiles we can produce the heatmaps in the same way as BRBE, ensuring to use the `--spe` option to be able to decode the profile.

```bash
llvm-bolt-heatmap --spe -p prof/spe.data ./out/bsort -block-size=64 -print-mappings
llvm-bolt-heatmap --spe -p prof/bolted-spe.data ./out/bsort.opt.spe -block-size=64 -print-mappings
```

{{< /tab >}}
{{< tab header="ETM Profiling" >}}

On a system with CoreSight ETM support, instruction flow traces can be recorded using `perf` for both binaries.

```bash
mkdir -p prof
perf record -e cs_etm//u -o prof/etm.data -- ./out/bsort
perf record -e cs_etm//u -o prof/bolted-etm.data -- ./out/bsort.opt.etm
```

Using these profiles we can produce the heatmaps in the same way as BRBE, ensuring to use the `--itrace` option to be able to decode the traces into branch-stack samples.

```bash
llvm-bolt-heatmap --itrace=l64i1us -p prof/etm.data ./out/bsort -block-size=64 -print-mappings
llvm-bolt-heatmap --itrace=l64i1us -p prof/bolted-etm.data ./out/bsort.opt.etm -block-size=64 -print-mappings
```

#### ETM AutoFDO
If you are using ETM AutoFDO to produce heatmaps, use <code>cs_etm/autofdo/u</code> instead of <code>cs_etm//u</code> as given in the examples.

```bash
mkdir -p prof
perf record -e cs_etm/autofdo/u -o prof/etm.data -- ./out/bsort
perf record -e cs_etm/autofdo/u -o prof/bolted-etm.data -- ./out/bsort.opt.etm-autofdo
```

Using these profiles we can produce the heatmaps in the same way as BRBE, ensuring to use the `--itrace` option to be able to decode the traces into branch-stack samples.

```bash
llvm-bolt-heatmap --itrace=l64i1us -p prof/etm.data ./out/bsort -block-size=64 -print-mappings
llvm-bolt-heatmap --itrace=l64i1us -p prof/bolted-etm.data ./out/bsort.opt.etm-autofdo \
    -block-size=64 -print-mappings
```


{{< /tab >}}
{{< tab header="PMU Profiling" >}}

PMU profiling can be used to provide basic samples to generate heatmaps. These are recorded using `perf`.

```bash
mkdir -p prof
perf record -e instructions:u -o prof/pmu.data -- ./out/bsort
perf record -e instructions:u -o prof/bolted-pmu.data -- ./out/bsort.opt.pmu
```

Using these samples we can produce the heatmaps in the same way as BRBE, ensuring to use the `-ba` option to be able to process the samples without needing `brstack` data. It should be noted that basic sampling provides less coverage than the other sampling methods and so there may be more gaps in the heatmap.

```bash
llvm-bolt-heatmap -ba -p prof/pmu.data ./out/bsort -block-size=64 -print-mappings
llvm-bolt-heatmap -ba -p prof/bolted-pmu.data ./out/bsort.opt.pmu -block-size=64 -print-mappings
```

{{< /tab >}}
{{< tab header="Instrumentation" >}}

Profiles produced using instrumentation cannot be used directly by `llvm-bolt-heatmap`. Instead instruction samples from the original and optimised binaries must be used. The example below uses the same approach as PMU profiling.

```bash
mkdir -p prof
perf record -e instructions:u -o prof/instr.data -- ./out/bsort
perf record -e instructions:u -o prof/bolted-instr.data -- ./out/bsort.opt.instr
```

Using these profiles we can produce the heatmaps in the same way as BRBE, ensuring to use the `-ba` option to be able to decode the profile.

```bash
llvm-bolt-heatmap -ba -p prof/instr.data ./out/bsort -block-size=64 -print-mappings
llvm-bolt-heatmap -ba -p prof/bolted-instr.data ./out/bsort.opt.instr -block-size=64 -print-mappings
```

{{< /tab >}}
{{< /tabpane-normal >}}

## Summary

In this learning path, you learned how to use BOLT to optimize binary code layout using several profiling methods. The optimized binaries improved instruction locality, reduced frontend stalls, and delivered measurable performance gains. 

You have also learnt how to use heatmaps to be able to visualise the layout changes made by BOLT and be able to compare heatmaps to identify potential performance impacts.
