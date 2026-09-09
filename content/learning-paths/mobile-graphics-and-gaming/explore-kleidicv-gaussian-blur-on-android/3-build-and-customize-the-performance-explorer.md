---
title: Build and customize the Gaussian blur performance explorer
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the performance explorer

The performance explorer is a standalone microbenchmark for comparing
KleidiCV Gaussian blur implementations on an Arm-based Android device. It
invokes the NEON, SVE2, and SME fixed-stripe functions directly instead of
using KleidiCV runtime dispatch.

For each implementation, the program processes deterministic single-channel
images at 640x640, 1920x1080, and 3840x2160. It creates a NEON reference image
and checks the SVE2 and SME results byte-for-byte against that reference
before reporting performance.

The program performs 100 warm-up calls, then measures each Gaussian blur call
with `CLOCK_MONOTONIC_RAW`. It reports the mean and p50 median latency as CSV.
You can select a 3x3, 5x5, 7x7, 9x9, or 15x15 kernel and control the
measurement count from the command line. CPU affinity is set separately with
`taskset` so you can compare implementations on the same CPU.

This microbenchmark measures individual Gaussian blur calls. It does not
represent complete application performance, which can also include image
decoding, memory transfers, rendering, and other processing stages.

## Create the performance explorer

The `26.06` release used in the previous steps does not include the Gaussian
blur performance explorer. Add the following changes to the
`examples/extract_one_operation` project in your local KleidiCV checkout.

### Update `CMakeLists.txt`

Append this configuration to
`examples/extract_one_operation/CMakeLists.txt`. It builds the complete
KleidiCV library with the SVE2 and SME backends enabled, then adds and links
the standalone performance comparison target:

```cmake
set(KLEIDICV_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../../kleidicv")
set(KLEIDICV_BINARY_DIR "${CMAKE_CURRENT_BINARY_DIR}/kleidicv")

set(KLEIDICV_ENABLE_SVE2 ON CACHE BOOL "" FORCE)
set(KLEIDICV_ENABLE_SME ON CACHE BOOL "" FORCE)
add_subdirectory(${KLEIDICV_SOURCE_DIR} ${KLEIDICV_BINARY_DIR})

add_executable(
  gaussian_blur_benchmark
  gaussian_blur_benchmark.cpp
)

target_include_directories(
  gaussian_blur_benchmark
  PRIVATE
  ${KLEIDICV_SOURCE_DIR}/include
  ${KLEIDICV_BINARY_DIR}/include
)

target_link_libraries(
  gaussian_blur_benchmark
  PRIVATE
  kleidicv
)
```

### Create `gaussian_blur_benchmark.cpp`

Create `examples/extract_one_operation/gaussian_blur_benchmark.cpp` with the
following source:

```cpp
/*
 * SPDX-FileCopyrightText: 2026 Arm Limited and/or its affiliates <open-source-office@arm.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <cerrno>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <limits>

#include "kleidicv/filters/gaussian_blur.h"

namespace {

constexpr size_t kChannels = 1;
constexpr size_t kDefaultKernelSize = 5;
constexpr size_t kWarmupIterations = 100;
constexpr size_t kMeasurementIterations = 1000;

using GaussianBlur = decltype(&kleidicv::neon::gaussian_blur_fixed_stripe_u8);

struct Backend {
  const char *name;
  GaussianBlur function;
};

struct TimingSummary {
  double mean_ns;
  uint64_t p50_ns;
};

struct ImageSize {
  size_t width;
  size_t height;
};

struct BenchmarkOptions {
  size_t kernel_size = kDefaultKernelSize;
  size_t measurement_iterations = kMeasurementIterations;
};

int compare_uint64(const void *left, const void *right) {
  const auto left_value = *static_cast<const uint64_t *>(left);
  const auto right_value = *static_cast<const uint64_t *>(right);
  return left_value < right_value ? -1 : left_value > right_value;
}

uint64_t monotonic_time_ns() {
  timespec timestamp;
  clock_gettime(CLOCK_MONOTONIC_RAW, &timestamp);
  return static_cast<uint64_t>(timestamp.tv_sec) * 1000000000ULL +
         static_cast<uint64_t>(timestamp.tv_nsec);
}

kleidicv_error_t call_backend(const Backend &backend, const uint8_t *source,
                              uint8_t *destination, ImageSize image_size,
                              size_t kernel_size) {
  return backend.function(source, image_size.width * kChannels, destination,
                          image_size.width * kChannels, image_size.width,
                          image_size.height, 0, image_size.height, kChannels,
                          kernel_size, kernel_size, 0.0F, 0.0F,
                          kleidicv::FixedBorderType::REFLECT);
}

bool create_reference(const Backend &backend, const uint8_t *source,
                      uint8_t *reference, ImageSize image_size,
                      size_t kernel_size) {
  const kleidicv_error_t error =
      call_backend(backend, source, reference, image_size, kernel_size);
  if (error != KLEIDICV_OK) {
    fprintf(stderr, "%s reference call failed: %d\n", backend.name, error);
    return false;
  }
  return true;
}

bool benchmark_backend(const Backend &backend, const uint8_t *source,
                       const uint8_t *reference, uint8_t *destination,
                       ImageSize image_size, const BenchmarkOptions &options,
                       TimingSummary *summary) {
  const size_t bytes = image_size.width * image_size.height * kChannels;
  for (size_t iteration = 0; iteration < kWarmupIterations; ++iteration) {
    if (call_backend(backend, source, destination, image_size,
                     options.kernel_size) != KLEIDICV_OK) {
      fprintf(stderr, "%s warmup call failed\n", backend.name);
      return false;
    }
  }
  if (memcmp(reference, destination, bytes) != 0) {
    fprintf(stderr, "%s output differs from NEON reference\n", backend.name);
    return false;
  }

  auto *samples = static_cast<uint64_t *>(
      malloc(options.measurement_iterations * sizeof(uint64_t)));
  if (samples == nullptr) {
    fprintf(stderr, "Could not allocate timing samples\n");
    return false;
  }

  uint64_t total_ns = 0;
  for (size_t iteration = 0; iteration < options.measurement_iterations;
       ++iteration) {
    const uint64_t start = monotonic_time_ns();
    const kleidicv_error_t error = call_backend(
        backend, source, destination, image_size, options.kernel_size);
    const uint64_t elapsed = monotonic_time_ns() - start;
    if (error != KLEIDICV_OK) {
      fprintf(stderr, "%s measured call failed\n", backend.name);
      free(samples);
      return false;
    }
    samples[iteration] = elapsed;
    total_ns += elapsed;
  }

  qsort(samples, options.measurement_iterations, sizeof(*samples),
        compare_uint64);
  summary->mean_ns =
      static_cast<double>(total_ns) / options.measurement_iterations;
  summary->p50_ns = samples[(options.measurement_iterations - 1) / 2];
  free(samples);
  return true;
}

bool parse_positive_size(const char *value, size_t *parsed_value) {
  errno = 0;
  char *end = nullptr;
  const unsigned long long parsed = strtoull(value, &end, 10);
  if (errno == ERANGE || end == value || *end != '\0' || parsed == 0 ||
      parsed > std::numeric_limits<size_t>::max() ||
      parsed > std::numeric_limits<size_t>::max() / sizeof(uint64_t)) {
    return false;
  }
  *parsed_value = static_cast<size_t>(parsed);
  return true;
}

bool is_supported_kernel_size(size_t kernel_size) {
  return kernel_size == 3 || kernel_size == 5 || kernel_size == 7 ||
         kernel_size == 9 || kernel_size == 15;
}

bool parse_options(int argc, char *argv[], BenchmarkOptions *options) {
  if ((argc - 1) % 2 != 0) {
    fprintf(stderr,
            "Usage: %s [--iterations <count>] [--kernel <3|5|7|9|15>]\n",
            argv[0]);
    return false;
  }

  for (int index = 1; index < argc; index += 2) {
    size_t value;
    if (!parse_positive_size(argv[index + 1], &value)) {
      fprintf(stderr, "Invalid value for %s: %s\n", argv[index],
              argv[index + 1]);
      return false;
    }
    if (strcmp(argv[index], "--iterations") == 0) {
      options->measurement_iterations = value;
    } else if (strcmp(argv[index], "--kernel") == 0 &&
               is_supported_kernel_size(value)) {
      options->kernel_size = value;
    } else {
      fprintf(stderr,
              "Usage: %s [--iterations <count>] [--kernel <3|5|7|9|15>]\n",
              argv[0]);
      return false;
    }
  }
  return true;
}

}  // namespace

int main(int argc, char *argv[]) {
  BenchmarkOptions options;
  if (!parse_options(argc, argv, &options)) {
    return EXIT_FAILURE;
  }

  const Backend backends[] = {
      {"neon", kleidicv::neon::gaussian_blur_fixed_stripe_u8},
      {"sve2", kleidicv::sve2::gaussian_blur_fixed_stripe_u8},
      {"sme", kleidicv::sme::gaussian_blur_fixed_stripe_u8},
  };
  const ImageSize image_sizes[] = {
      {640, 640},
      {1920, 1080},
      {3840, 2160},
  };

  printf(
      "backend,width,height,channels,kernel,warmup,iterations,mean_ns,"
      "p50_ns\n");
  for (const ImageSize image_size : image_sizes) {
    const size_t bytes = image_size.width * image_size.height * kChannels;
    auto *source = static_cast<uint8_t *>(malloc(bytes));
    auto *reference = static_cast<uint8_t *>(malloc(bytes));
    auto *destination = static_cast<uint8_t *>(malloc(bytes));
    if (source == nullptr || reference == nullptr || destination == nullptr) {
      fprintf(stderr, "Could not allocate benchmark images\n");
      free(source);
      free(reference);
      free(destination);
      return EXIT_FAILURE;
    }

    uint32_t random_state = 0x12345678;
    for (size_t index = 0; index < bytes; ++index) {
      random_state = random_state * 1664525 + 1013904223;
      source[index] = static_cast<uint8_t>(random_state >> 24);
    }
    if (!create_reference(backends[0], source, reference, image_size,
                          options.kernel_size)) {
      free(source);
      free(reference);
      free(destination);
      return EXIT_FAILURE;
    }

    for (const Backend &backend : backends) {
      TimingSummary summary;
      if (!benchmark_backend(backend, source, reference, destination,
                             image_size, options, &summary)) {
        free(source);
        free(reference);
        free(destination);
        return EXIT_FAILURE;
      }
      printf("%s,%zu,%zu,%zu,%zu,%zu,%zu,%.3f,%llu\n", backend.name,
             image_size.width, image_size.height, kChannels,
             options.kernel_size, kWarmupIterations,
             options.measurement_iterations, summary.mean_ns,
             static_cast<unsigned long long>(summary.p50_ns));
    }

    free(source);
    free(reference);
    free(destination);
  }
  return EXIT_SUCCESS;
}
```

Configure a separate build directory and build the performance explorer:

```bash
cmake -S examples/extract_one_operation \
      -B build/extract-android-benchmark \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_TOOLCHAIN_FILE="$ANDROID_NDK_HOME/build/cmake/android.toolchain.cmake" \
      -DANDROID_ABI=arm64-v8a \
      -DANDROID_PLATFORM=android-21 \
      -DANDROID_STL=c++_static

cmake --build build/extract-android-benchmark \
      --target gaussian_blur_benchmark -j"$(nproc)"
```

## Use the command-line parameters

The default run measures a 5x5 binomial kernel over 1000 calls. Use `tee` to
display the results and save them to a CSV file on the Linux development
machine:

```bash
adb push build/extract-android-benchmark/gaussian_blur_benchmark /data/local/tmp/
adb shell chmod 755 /data/local/tmp/gaussian_blur_benchmark
adb shell 'taskset 80 /data/local/tmp/gaussian_blur_benchmark' \
  | tee gaussian_blur_cpu7_kernel5.csv
```

Use `--iterations` to change the number of measured calls and `--kernel` to
select a supported fixed kernel size. Give each configuration a descriptive
file name so you can identify it during analysis:

```bash
adb shell 'taskset 80 /data/local/tmp/gaussian_blur_benchmark \
    --kernel 15 --iterations 3000' \
  | tee gaussian_blur_cpu7_kernel15.csv
```

Supported kernel sizes are 3, 5, 7, 9, and 15. The 3x3 through 9x9 kernels
use the fixed binomial variants. The 15x15 kernel uses the fixed Gaussian
variant and matches the kernel size in the standalone SME example. Keeping
the CPU affinity fixed is important: it prevents the operating system from
migrating a process between cores with different performance characteristics.

## Interpret the CSV output

Each run writes one header row followed by nine result rows: three
implementations for each of the three image resolutions. Inspect the saved
file:

```bash
head gaussian_blur_cpu7_kernel15.csv
```

For readability, the following table summarizes the 15x15 CSV results from
CPU 7. Every row uses one image channel, 100 warm-up calls, and 3000 measured
calls.

| Backend | Image resolution | Kernel | Iterations | Mean latency (ns) | p50 latency (ns) |
| --- | ---: | ---: | ---: | ---: | ---: |
| NEON | 640x640 | 15x15 | 3000 | 1,006,594.304 | 986,112 |
| SVE2 | 640x640 | 15x15 | 3000 | 838,039.808 | 819,840 |
| SME | 640x640 | 15x15 | 3000 | 695,746.901 | 679,424 |
| NEON | 1920x1080 | 15x15 | 3000 | 4,284,394.496 | 4,226,560 |
| SVE2 | 1920x1080 | 15x15 | 3000 | 3,421,537.920 | 3,384,320 |
| SME | 1920x1080 | 15x15 | 3000 | 2,464,050.517 | 2,424,064 |
| NEON | 3840x2160 | 15x15 | 3000 | 16,678,738.261 | 16,471,040 |
| SVE2 | 3840x2160 | 15x15 | 3000 | 13,267,384.789 | 13,089,920 |
| SME | 3840x2160 | 15x15 | 3000 | 8,382,547.243 | 8,199,552 |

These values were collected from an SME-capable Android device with the
process pinned to CPU 7. Your results will differ with the processor, CPU
affinity, vector length, frequency, thermal state, and background activity.

The CSV contains the following fields:

| Field | Meaning |
| --- | --- |
| `backend` | KleidiCV implementation: `neon`, `sve2`, or `sme` |
| `width` | Input image width in pixels |
| `height` | Input image height in pixels |
| `channels` | Number of image channels; this explorer uses one channel |
| `kernel` | Selected Gaussian kernel width and height |
| `warmup` | Calls completed before measurement begins |
| `iterations` | Timed calls used to calculate the results |
| `mean_ns` | Mean latency per Gaussian blur call in nanoseconds |
| `p50_ns` | Median latency per Gaussian blur call in nanoseconds |

Use `p50_ns` as the primary comparison metric because it is less sensitive to
occasional interruptions than the mean. A lower value indicates a faster
implementation. Compare rows with the same image dimensions, kernel size,
CPU affinity, and iteration count.

In this 15x15 example, SME has the lowest p50 latency at all three resolutions.
Compared with NEON, SME is 1.45x faster at 640x640, 1.74x faster at
1920x1080, and 2.01x faster at 3840x2160. The next step compares multiple
kernel sizes and explains how workload size can change the performance
behavior.

## Code changes behind the parameters

The performance explorer stores its settings in `BenchmarkOptions`. The
default values are a 5x5 kernel and 1000 measured calls. The source above
includes the complete option parser, which accepts `--iterations <count>` and
`--kernel <3|5|7|9|15>`. The selected kernel size is passed as both
`kernel_width` and `kernel_height` to every backend. This makes it possible
to compare implementations without recompiling the program.

The program intentionally does not choose a CPU or read CPU capacity. CPU
selection belongs outside the performance explorer and is controlled with
`taskset`.

Next, run a controlled comparison and interpret the results.
