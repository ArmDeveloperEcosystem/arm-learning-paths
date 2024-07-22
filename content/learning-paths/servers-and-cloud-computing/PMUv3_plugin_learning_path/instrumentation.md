---
title: How to instrument at code level?
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## INSTRUMENTATION USING PMUV3_PLUGIN
There are 4 scenarios listed below. Ideally, pick the scenario you are looking for and refer to that usage. 

## Scenario I – Instrumentation In Different Code Blocks in C++ codebase
For Pmuv3_Bundles Instrumentation IN DIFFERENT CHUNK OF CODES in C++ codebase (e.g.: Multiple chunks of code in same testcase, Multiple functions or Nested functions), follow the below steps.  

1. In your application source code where the PMUv3 instrumentation will be embedded, you need to include header this way.

```yaml
#include "processing.hpp" 

#ifdef PMUV3_CPU_BUNDLES
extern "C" {
    #ifdef PARENT_DIR
        #include "pmuv3_plugin_bundle.h"
    #endif
}
#endif
```

2. Initialize the PMUv3 Event Bundle - void pmuv3_bundle_init(int)
In testcases, in main function, we need to pass the argument for which bundle to choose:

```yaml
int main(int argc, char** argv)
{
    if (argc != 2) {
        printf("Usage: %s <arg>\n", argv[0]);
        exit(1);
    }
     int cur_bundles_no = atoi(argv[1]);
    // then call initialization once:
    pmuv3_bundle_init(cur_bundles_no);
}
```

3. local_index is a unique variable specific to every piece of instrumentation. It will be used to map the end_count to corresponding start_count and helps in post processing to calculate the cycle difference.
The get_next_index() API will help to increment the local_index by 1 at every call.

```yaml
uint64_t local_index = get_next_index();
```
NOTE: This local_index variable that you define should be unique everytime. You call this before calling the get_start_count() API and every single time give unique variable name like local1, local2, local3 etc instead of using local_index everytime. This uniqueness will be useful when there are multiple functions of the same level within a function. Eg: When f2(), f3() are present within f1() and f2(), f3() are of same level, not nested.

4. Start Event Bundle - uint64_t get_start_count(struct PerfData *perf_data, struct CountData *count_data, const char* context, uint64_t index);
For example:

```yaml
get_start_count(&count_data, "DU_HIGH1", local_index);
```

NOTE: The third variable is a context. NOTE: Whatever context (3rd parameter) and index (4th parameter) one passes in get_start_count() should be passed to corresponding get_end_count()

5. End Event Bundle - uint64_t get_end_count(struct PerfData *perf_data, struct CountData *count_data, const char* context, uint64_t index);

```yaml
get_end_count(&count_data, "DU_HIGH1", local_index);
```

6. Define this in a place after all instrumentation is done.

```yaml
process_data(cur_bundle_no);
```
7. Shutdown and release resource for Event Bundle Instrument - int shutdown_resources(struct PerfData *perf_data);

```yaml
shutdown_resources();
```

Example Instrumentation For Reference

```yaml
//Just once in main()
int main(int argc, char** argv)
{
    if (argc != 2) {
        printf("Usage: %s <arg>\n", argv[0]);
        exit(1);
    }
     int cur_bundles_no = atoi(argv[1]);
    // then call initialization once:
    pmuv3_bundle_init(cur_bundles_no);
}
//In places of instrumentation, do like below. Remember that every get_start_count will have a separate get_end_count API. 
uint64_t local_1 = get_next_index();

get_start_count(&count_data,"CONTEXT_1", local_1);

/********************************1ST CODE CHUNK***********************************/

get_end_count(&count_data, "CONTEXT_1", local_1);


.
.
.
.

uint64_t local_2 = get_next_index();

get_start_count(&count_data,"CONTEXT_2", local_2);

/********************************2ND CODE CHUNK***********************************/

get_end_count(&count_data,"CONTEXT_2", local_2);
// Below APIs will be invoked only once per testcase after instrumenting in several places.
shutdown_resources();

process_data(cur_bundle_no);
```

---

## Scenario II – Instrumentation Around Single Code block in C++ codebase

For Pmuv3_Bundles Instrumentation "SINGLE CHUNK OF CODE" in  C++ CODEBASE, refer the below steps.

1.In your application source code where the PMUv3 instrument will be embedded, you need to include header this way.

```yaml
#include "processing.hpp"

#ifdef PMUV3_CPU_BUNDLES

extern "C" {
    #ifdef PARENT_DIR
        #include "pmuv3_plugin_bundle.h"
    #endif
}
#endif
```

2. Initialize the PMUv3 Event Bundle - void pmuv3_bundle_init(int)

In testcases, in main function, we need to pass the argument for which bundle to choose:

```yaml
int main(int argc, char** argv)
{
    if (argc != 2) {
        printf("Usage: %s <arg>\n", argv[0]);
        exit(1);
    }
    int cur_bundles_no = atoi(argv[1]);

    // then call initialization once:

    pmuv3_bundle_init(cur_bundles_no);
}
```

3. Instrument around single chunk of code

```yaml
process_start_count(&count_data);

///////////CODE CHUNK TO BE INSTRUMENTED//////////////

process_end_count(&count_data);
```

4. Define this in a place after all instrumentation is done.

```yaml
process_single_chunk(cur_bundle_no);
```

5. Shutdown and release resource for Event Bundle Instrument

```yaml
shutdown_resources();
```

This populates bundle0.csv, bundle1.csv etc. as requested by user in the directory where you ran the testcase. 

## Scenario III– Instrumentation around different code blocks in C codebase 
For Pmuv3_Bundles Instrumentation in a C Codebase around different Chunks Of Code, refer below steps.

 Follow the same procedure described above with small changes.

Reminder: Before you run ./build.sh, vim build.sh and uncomment line 20 and comment line 19. This was already mentioned in Requirements section. 
1. No need for extern in C code base so we include directly.

```yaml
#include <processing.h>

#include "pmuv3_plugin_bundle.h"
```

2. Initialization and instrumentation APIs are the same as mentioned in C++ sections for DIFFERENT CHUNK OF CODES (Section I) scenario. 
- 	DIFFERENT CHUNK OF CODES

```yaml
uint64_t local_1 = get_next_index();

get_start_count(&count_data, "CONTEXT_1" ,local_1);

/********************************1ST CODE CHUNK***********************************/

get_end_count(&count_data, "CONTEXT_1", local_1);


uint64_t local_2 = get_next_index();

get_start_count(&count_data, "CONTEXT_2", local_2);

/********************************2ND CODE CHUNK***********************************/

get_end_count(&count_data, "CONTEXT_2", local_2);
```

3. In post processing,

```yaml
process_data(cur_bundle_no);
```
4. Shutdown resources

```yaml
shutdown_resources();
```
---

## Scenario IV – Instrumentation around single code blocks in C codebase
For Pmuv3_Bundles Instrumentation in a C Codebase around a Single Chunk Of Code, refer below steps.

 Follow the same procedure described above with small changes.

Reminder: Before you run ./build.sh, vim build.sh and uncomment line 20 and comment line 19. This was already mentioned in Requirements section. 
1. No need for extern in C code base so we include directly.

```yaml
#include <processing.h>

#include "pmuv3_plugin_bundle.h"
```

2. Initialization and instrumentation APIs are the same as mentioned in C++ sections of SINGLE CHUNK OF CODE (Section II) scenario.
Scenario 1 - SINGLE CHUNK OF CODES

```yaml
process_start_count(&count_data);

///////////CODE CHUNK TO BE INSTRUMENTED//////////////

process_end_count(&count_data);
```

3. In post processing,

```yaml
post_process(bundle_num);
```
4. Shutdown resources

```yaml
shutdown_resources();
```

