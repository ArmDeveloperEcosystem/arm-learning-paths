---
title: Instrument multiple sections of code
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You can also instrument multiple sections of code. 

## Instrumenting multiple code blocks in C 

The next scenario is to instrument a single section of code in C. 

The API is slightly different, but the concept is the same. 

For multiple code segments the first two steps and cleanup are the same but the start and stop functions are slightly different because they include markers to indicate which segment you are profiling.

Here are the steps for multiple segments:
- Include 2 header files (same)
- Initialize the plugin by calling `pmuv3_bundle_init()` with the bundle number as an argument (same)
- Use `get_next_index()` to obtain the next segment number, the numbers count up from 0
- Start counting by calling the function `get_start_count()` and pass the segment number
- Call the function `get_end_count()` and pass the segment number to stop counting for that segment
- Write the collected data to a CSV file by calling `process_data()` with the same bundle number
- Clean up with `shutdown_resources()` 

You can repeat for additional segments by getting the next segment number and using the start and stop functions again.

The example below collects the `initialize_vectors()` function and the `calculate_result()` functions separately instead of collecting the data for both of them as in the previous example. 

Use a text editor to create a file `test2.c` in the test directory with the contents below:

```C
#include <stdio.h>
#include <stdint.h>
#include <math.h>

#include "pmuv3_plugin_bundle.h"
#include "processing.h"

#define VECTOR_SIZE 10000

void initialize_vectors(double vector_a[], double vector_b[], int size) {
    for (int i = 0; i < size; i++) {
        vector_a[i] = sin(i);
        vector_b[i] = cos(i);
    }
}

void calculate_result(double result[], double vector_a[], double vector_b[], int size) {
    for (int i = 0; i < size; i++) {
        result[i] = vector_a[i] + vector_b[i];
    }
}

int main(int argc, char **argv) {
    uint64_t section1, section2;
    int bundle_number;
    struct CountData counter_data;

    /* Bundle number is passed as an argument */
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <bundle number>\n", argv[0]);
        return EXIT_FAILURE;
    }
    bundle_number = atoi(argv[1]);

    /* Initialize the bundle of events */
    if (pmuv3_bundle_init(bundle_number) != 0) {
        fprintf(stderr, "Failed to initialize PMU bundle\n");
        return EXIT_FAILURE;
    }


    /* Declare vectors */
    double vector_a[VECTOR_SIZE], vector_b[VECTOR_SIZE], result[VECTOR_SIZE];

    /* Initialize vectors */
    section1 = get_next_index();
    printf("section 1: %ld\n", section1);
    get_start_count(&counter_data, "SECTION_1" , section1);
    initialize_vectors(vector_a, vector_b, VECTOR_SIZE);
    get_end_count(&counter_data, "SECTION_1", section1);

    /* Calculate vectors */
    section2 = get_next_index();
    printf("section 2: %ld\n", section2);
    get_start_count(&counter_data, "SECTION_2" , section2);
    calculate_result(result, vector_a, vector_b, VECTOR_SIZE);
    get_end_count(&counter_data, "SECTION_2", section2);


    /* Write CSV file and clean up */
    process_data(bundle_number);
    shutdown_resources();

    return EXIT_SUCCESS;
```

Build the application:

```console
gcc -I ../linux/tools/lib/perf/include  -I ../PMUv3_plugin/ test2.c -o test2 -L ../PMUv3_plugin/  -lpmuv3_plugin_bundle -lperf -lapi -lm
```

Run the application and pass the bundle number of 3 (to capture the stall information):

```console
sudo ./test2 3
```

The output now contains data for 2 sections and prints:

```output
- running pmuv3_plugin_bundle.c...OK
section 1: 0
section 2: 1
End is 296049, Start is 233645, diff is 62404
End is 2163, Start is 1881, diff is 282
End is 35572, Start is 24711, diff is 10861
End is 0, Start is 0, diff is 0
End is 0, Start is 0, diff is 0
End is 0, Start is 0, diff is 0
End is 0, Start is 0, diff is 0
End is 316557, Start is 309185, diff is 7372
End is 2362, Start is 2224, diff is 138
End is 40786, Start is 38413, diff is 2373
End is 0, Start is 0, diff is 0
End is 0, Start is 0, diff is 0
End is 0, Start is 0, diff is 0
End is 0, Start is 0, diff is 0
```

The results are captured in the file `bundle3.csv`.

Display the text file to see the contents:

```console
cat bundle3.csv
```

The data shows the metrics on the first line and the values for section 1 on the second line and the values for section 2 on the third line.

```output
CONTEXT,CPU_CYCLES,BR_MIS_PRED,BR_PRED,BR_RETIRED,BR_MIS_PRED_RETIRED,BR_IMMED_SPEC,BR_INDIRECT_SPEC
SECTION_1,60569,254,10871,0,0,0,0
SECTION_2,7413,22,1917,0,0,0,0
```

You can use this methodology to instrument multiple sections of code and generate the data for all bundles by modifying the `run.sh` file from the single section instrumentation. All you need to do is change the command from `test1` to `test2` and invoke the `run.sh` script again.
