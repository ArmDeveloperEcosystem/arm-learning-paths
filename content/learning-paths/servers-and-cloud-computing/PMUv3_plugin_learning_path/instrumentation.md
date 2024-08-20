---
title: Instrument one section of code
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The instrumentation scenarios are listed below, covering the most common situations.

## Directory structure

So far you have the Linux kernel source tree and the PMUv3 plugin source code. 

Next, create a third directory to learn how to integrate the PMUv3 plugin into an application as follows:

```console
cd ../ ; mkdir test ; cd test
```

The instructions assume you have all three directories in parallel. If you have a different directory structure, you may need to adjust the build commands to find the header files and libraries. 

Here are the 3 directories you now have:

```output
./linux
./PMUv3_plugin
./test
```
You can use the test directory to try out the integration scenarios. 

## Instrumenting a single code block in C

The first scenario is to instrument a single section of code in C. 

The general process to instrument code includes the following steps: 
- Include 2 header files
- Initialize the plugin by calling `pmuv3_bundle_init()` with the bundle number as an argument
- Start counting by calling the function `process_start_count()` 
- Call the function `process_end_count()` to stop counting
- Write the collected data to a CSV file by calling `post_process()` with the same bundle number
- Clean up with `shutdown_resources()` 

As an example, use a text editor to create a file `test1.c` in the `test` directory with the contents below:

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

    /* Code to be analyzed */
    process_start_count(&counter_data);

    /* Declare vectors */
    double vector_a[VECTOR_SIZE], vector_b[VECTOR_SIZE], result[VECTOR_SIZE];

    /* Initialize and calculate vectors */
    initialize_vectors(vector_a, vector_b, VECTOR_SIZE);
    calculate_result(result, vector_a, vector_b, VECTOR_SIZE);

    process_end_count(&counter_data);

    /* Write CSV file and clean up */
    post_process(bundle_number);
    shutdown_resources();

    return EXIT_SUCCESS;
}
```
The include files and function calls are added in the code to provide the performance instrumentation.

Build the application as follows:

```console
gcc -I ../linux/tools/lib/perf/include  -I ../PMUv3_plugin/ test1.c -o test1 -L ../PMUv3_plugin/  -lpmuv3_plugin_bundle -lperf -lapi -lm
```

Run the application and pass the bundle number of 4 (to capture stall information):

```console
sudo ./test1 4
```

The output prints the following:

```output
- running pmuv3_plugin_bundle.c...OK
End is 1404713, Start is 119346
End is 112270, Start is 43884
End is 285708, Start is 6714
```

The results are captured in the file `bundle4.csv`.

Display the text file to see the contents:

```console
cat bundle4.csv
```

The data shows the metrics on the first line and the values on the second line as shown below:

```output
CPU_CYCLES,STALL_FRONTEND,STALL_BACKEND
1285367,68386,278994
```

## Collect data for all bundles

You can quickly collect the data for all bundles. Save the code below in a file named `run.sh`:

```console
#!/bin/bash

for i in {0..14}
do
  echo $i
  sudo ./test1 $i
done
```

Run the script:
```console
bash ./run.sh
```

All 15 of the bundle CSV files have been generated. 

Next, learn how you can visualize the data.

