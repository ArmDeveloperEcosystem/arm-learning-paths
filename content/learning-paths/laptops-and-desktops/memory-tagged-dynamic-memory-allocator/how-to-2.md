---
title: Implement Memory Tagging for a Dynamic Memory Allocator
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The source code for the complete project is included in this learning path. We will not explain the source code but, instead, the following sections will go into detail about the memory tagging specific changes
that were made.

## Project Structure

The project consists of the following files:
* `CMakeLists.txt` - tells `cmake` how to configure the project
* `heap.c` and `heap.h` - the dynamic memory allocator
* `mte_utils.c` and `mte_utils.h` - helper functions for handling memory tags (these are used by the heap and the demo application)
* `main.c` - the program that uses the memory allocator

## Software Requirements

Install the required tools using the following command:

```bash
sudo apt install -y cmake ninja-build gcc-aarch64-linux-gnu qemu-user
```

## Source Code

Using a file editor of your choice, create a file named `CMakeLists.txt` and copy the contents below into it:

``` {file_name="CMakeLists.txt"}
cmake_minimum_required(VERSION 3.15)

project(TaggedMemoryAllocatorDemo C)

add_executable(demo main.c heap.c mte_utils.c)
```

Create a file named `heap.c` with the contents shown below:
```C {file_name="heap.c"}
#include <arm_acle.h>
#include <assert.h>
#include <stdarg.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/prctl.h>

#include "mte_utils.h"

// Defines provided to support older toolchains.

#ifndef PR_SET_TAGGED_ADDR_CTRL
#define PR_SET_TAGGED_ADDR_CTRL 55
#endif

#ifndef PR_TAGGED_ADDR_ENABLE
#define PR_TAGGED_ADDR_ENABLE (1UL << 0)
#endif

#ifndef PROT_MTE
#define PROT_MTE 0x20
#endif

#ifndef PR_MTE_TCF_SYNC
#define PR_MTE_TCF_SYNC (1 << 1)
#endif

#ifndef PR_MTE_TAG_SHIFT
#define PR_MTE_TAG_SHIFT 3
#endif

#define MTE_TAG_GRANULE 16

// Enable logging of heap events and current memory ranges.
static const bool log_events = true;

// Whether to randomise the memory tag of each new allocation,
// or use a value that increases by 1 each time.
static const bool randomise_memory_tags = false;

// printf but can be globally disabled by setting log_events to false.
static void log_event(const char *fmt, ...) {
  if (log_events) {
    va_list args;
    va_start(args, fmt);
    vprintf(fmt, args);
    va_end(args);
  }
}

#define STORAGE_SIZE 4096
// Will be allocated by mmap during simple_heap_init.
static char *storage = NULL;
// If our search reaches this point, there is no free space to allocate, also
// set by simple_heap_init.
static const char *storage_end = NULL;

// The heap is divided into ranges, initially only 1 that covers the whole heap
// and is marked free. A header is the number of bytes in the range, and a
// single bit to say whether it is free or allocated.
typedef struct {
  uint64_t size : 63;
  bool allocated : 1;
} Header;
// This header is placed at the start of each range, so we will return pointers
// that point to the first byte after it.
_Static_assert(sizeof(Header) == sizeof(uint64_t));

void log_header(Header header) {
  log_event("[%s, size = %u bytes]",
            header.allocated ? "allocated" : "     free", header.size);
}

static Header read_header(const char *ptr) {
  // This header is in tagged memory so we must use its memory tag to access it.
  ptr = set_logical_tag((char *)ptr, get_memory_tag(ptr));
  return *(Header *)ptr;
}

static void write_header(char *ptr, Header header) {
  *(Header *)ptr = header;
  log_event("[0x%016lx] Set header to ", ptr);
  log_header(header);
  log_event("\n");
}

// Log a table showing the ranges currently marked in the heap.
static void log_ranges() {
  log_event("Ranges:\n");
  Header header = {.size = 0, .allocated = false};
  for (const char *header_ptr = storage; header_ptr < storage_end;
       header_ptr += header.size) {
    header = read_header(header_ptr);
    uint8_t tag = get_memory_tag(header_ptr);
    const char *tagged_header_ptr = set_logical_tag(header_ptr, tag);
    log_event("  [0x%016lx -> 0x%016lx) : ", tagged_header_ptr,
              tagged_header_ptr + header.size);
    log_event("[memory tag: 0x%x] ", tag);
    log_header(header);
    log_event("\n");
  }
}

uint8_t get_next_memory_tag() {
  if (randomise_memory_tags) {
    // __arm_mte_create_random_tag randomly selects a tag value from the allowed
    // values (which we set to 1-15) and sets it as the logical tag of the
    // pointer. The second argument is a mask of excluded tag values, we won't
    // exclude any. You could use this to exclude values that surround certain
    // areas of memory.
    return get_logical_tag(__arm_mte_create_random_tag((void *)(0), 0));
  } else {
    // Get predictable output by using an incrementing and wrapping value.
    static uint8_t next_memory_tag = 1;

    uint8_t ret = next_memory_tag;
    if (next_memory_tag == MTE_TAG_MASK)
      next_memory_tag = 1;
    else
      ++next_memory_tag;

    return ret;
  }
}

void simple_heap_init() {
  log_event("Simple heap init:\n");

  int got = prctl(
      PR_SET_TAGGED_ADDR_CTRL,
      // Enable the tagged address ABI.
      // https://www.kernel.org/doc/Documentation/arm64/tagged-address-abi.rst
      PR_TAGGED_ADDR_ENABLE |
          // Raise memory tagging exceptions as they happen (as opposed to
          // async, which reports at a later time).
          PR_MTE_TCF_SYNC |
          // This is a bitfield where each bit position represents a tag value.
          // A 1 means that tag generation instructions may generate that value.
          // The value 0xfffe means they can generate all values except for 0,
          // which is used for free memory.
          (0xfffe << PR_MTE_TAG_SHIFT),
      0, 0, 0);
  assert(got == 0);

  // Allocate memory tagged memory as our backing storage. All the memory tags
  // will start as 0.
  storage = mmap(0, STORAGE_SIZE,
                 PROT_READ | PROT_WRITE |
                     // Memory should have memory tagging enabled.
                     PROT_MTE,
                 MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
  assert(storage);
  storage_end = storage + STORAGE_SIZE;

  log_event("Storage [0x%016lx -> 0x%016lx) (%d bytes)\n", storage, storage_end,
            STORAGE_SIZE);

  // On startup, all the heap is one free range.
  Header hdr = {.size = STORAGE_SIZE, .allocated = false};
  write_header(storage, hdr);
  log_ranges();
}

// Search for a free range that has at least `bytes` of space
// (callers should include the header size).
static char *find_free_space(size_t bytes) {
  Header header = {.size = 0, .allocated = false};
  for (char *header_ptr = storage; header_ptr < storage_end;
       header_ptr += header.size) {
    header = read_header(header_ptr);
    assert(header.size != 0 && "Header should always have non-zero size.");
    if (!header.allocated && (header.size >= bytes))
      return header_ptr;
  }

  return NULL;
}

// Take an existing free range and split it such that there is a `bytes` sized
// range at the start and a new, smaller, free range after that.
static void split_range(char *range, uint64_t size) {
  Header original_header = read_header(range);
  assert(!original_header.allocated &&
         "Shouldn't be splitting an allocated range.");

  // Mark what we need as allocated.
  Header new_header = {.size = size, .allocated = true};
  write_header(range, new_header);

  // The following space is free and needs a new header to say so.
  uint64_t remaining = original_header.size - size;
  if (remaining) {
    Header free_header = {.size = remaining, .allocated = false};
    write_header(range + size, free_header);
  }
}

static void tag_range(char *range, uint64_t size) {
  assert((uintptr_t)range % 16 == 0 && "Expected a granule aligned address");
  assert(size % 16 == 0 &&
         "Expected range size that is a multiple of the tag granule");

  // Assume that range already contains the logical tag.
  for (; size; size -= MTE_TAG_GRANULE, range += MTE_TAG_GRANULE)
    __arm_mte_set_tag(range);
}

// Attempt to allocate `size` bytes of memory. Returns NULL for 0 sized
// allocations or when we have run out of heap memory. The size passed here does
// not include header size, this is an internal detail. So the returned pointer
// will be sizeof(Header) further forward than the start of the range used.
void *simple_malloc(size_t size) {
  if (!size)
    return NULL;

  log_event("\nTrying to allocate %ld bytes\n", size);

  // Extra space to include the header.
  uint64_t required_size = size + sizeof(Header);
  // Memory is tagged in granules of 16 bytes, so we must round up to a whole
  // number of 16 byte granules.
  if (required_size % MTE_TAG_GRANULE)
    required_size += MTE_TAG_GRANULE - (required_size % MTE_TAG_GRANULE);

  char *allocated = find_free_space(required_size);

  if (!allocated) {
    log_event("Heap exhausted.\n");
    return NULL;
  }

  // Split the found range into this new allocation and a new free range after
  // it.
  split_range(allocated, required_size);

  // The returned pointer must have its logical tag set to the allocation tag
  // of the allocated range.
  uint8_t next_memory_tag = get_next_memory_tag();
  allocated = (char *)set_logical_tag(allocated, next_memory_tag);

  // Tag the range with the new non-zero tag.
  tag_range(allocated, required_size);

  log_event(
      "Memory was allocated at 0x%016lx, size %ld bytes (%ld byte overhead)\n",
      allocated, required_size, required_size - size);

  // Return a pointer to after the header.
  allocated += sizeof(Header);

  log_ranges();
  return allocated;
}

// Free the allocation pointed to by ptr. This simply sets the range to free,
// does not change its size of any of its contents.
void simple_free(void *ptr) {
  if (!ptr)
    return;

  // As the memory tag is part of the pointer, we need to remove it before doing
  // any numerical comparisons. As a pointer to the same location, but with a
  // higher tag value, will be seen as greater than the other pointer despite
  // pointing to the same address.
  const void *untagged_ptr = remove_logical_tag(ptr);
  assert(((char *)untagged_ptr > storage) &&
         ((char *)untagged_ptr < storage_end) &&
         "Trying to free pointer that is not within the heap.");

  // This will point to after the header of the range it's in, so we must walk
  // back a bit.
  char *header_ptr = (char *)ptr - sizeof(Header);

  // Detect attempts to free an allocation more than once.
  uint8_t logical_tag = get_logical_tag(ptr);
  uint8_t allocation_tag = get_memory_tag(ptr);
  if (logical_tag != allocation_tag) {
    printf("\nProgram attempted an invalid free\n");
    print_pointer_tags(ptr);
    exit(1);
  }

  log_event("\nFreeing allocation at 0x%016lx\n", ptr);

  Header header = read_header(header_ptr);
  assert(header.size != 0 && "Can't free an allocation of zero size.");

  // Mark this range as free, leave the size unchanged.
  header.allocated = false;
  write_header(header_ptr, header);

  // Reset tags to 0 to prevent use after free.
  tag_range((char *)set_logical_tag(header_ptr, 0), header.size);

  log_event("Memory at 0x%016lx was freed\n", ptr);
  log_ranges();
}

```

Create a file named `heap.h` with the content shown below:
```C {file_name="heap.h"}
#ifndef HEAP_H
#define HEAP_H

#include <stddef.h>

// Call once at the start of main() to initialise the empty heap.
// This is the equivalent of what your C library is doing before main() for the
// system heap.
void simple_heap_init();

void *simple_malloc(size_t size);

void simple_free(void *ptr);

#endif /* ifndef HEAP_H */

```

Create a file named `mte_utils.c` with the contents shown below:
```C {file_name="mte_utils.c"}
#include "mte_utils.h"

#include <inttypes.h>
#include <stdio.h>

uint8_t get_memory_tag(const void *addr) {
  return ((uintptr_t)__arm_mte_get_tag(addr) >> MTE_TAG_SHIFT) & MTE_TAG_MASK;
}

const void *remove_logical_tag(const void *ptr) {
  return (const void *)((uintptr_t)ptr &
                        ~((uintptr_t)MTE_TAG_MASK << MTE_TAG_SHIFT));
}

const void *set_logical_tag(const void *ptr, uint8_t tag) {
  uintptr_t p = (uintptr_t)remove_logical_tag(ptr);
  return (const void *)((uintptr_t)p | ((uintptr_t)tag & MTE_TAG_MASK)
                                           << MTE_TAG_SHIFT);
}

uint8_t get_logical_tag(const void *ptr) {
  return ((uintptr_t)ptr >> MTE_TAG_SHIFT) & MTE_TAG_MASK;
}

void print_pointer_tags(const void *ptr) {
  printf("  Pointer: 0x%016" PRIXPTR "    Logical tag: %d\n", ptr,
         get_logical_tag(ptr));
  printf("Points to: 0x%016" PRIXPTR " Allocation tag: %d\n",
         remove_logical_tag(ptr), get_memory_tag(ptr));
}

```

Create a file named `mte_utils.h` with the contents shown below:
```C {file_name="mte_utils.h"}
#ifndef MTE_UTILS_H
#define MTE_UTILS_H

#include <arm_acle.h>
#include <stdint.h>

#define MTE_TAG_SHIFT 56ULL
#define MTE_TAG_MASK 0xfULL

uint8_t get_memory_tag(const void *addr);

const void *remove_logical_tag(const void *ptr);

const void *set_logical_tag(const void *ptr, uint8_t tag);

uint8_t get_logical_tag(const void *ptr);

void print_pointer_tags(const void *ptr);

#endif /* ifndef MTE_UTILS_H */

```

Create a file named `main.c` with the contents shown below:
```C {file_name="main.c"}
#include "heap.h"
#include "mte_utils.h"
#include <assert.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/auxv.h>

void handle_segv(int signal, siginfo_t *sig_info, void *arg) {
  // Only expect to get synchronous memory tag faults here.
  assert(sig_info->si_signo == SIGSEGV);
  assert(sig_info->si_code == SEGV_MTESERR);

  // Get the address that the program tried to access.
  void *addr = sig_info->si_addr;
  // This address includes the logical tag it tried to use.
  uint8_t logical_tag = get_logical_tag(addr);
  // Which clearly did not match the allocation tag of where it pointed to.
  uint8_t allocation_tag = get_memory_tag(addr);

  // Print an explanation of the problem, then exit the program.
  printf("\nProgram caused an asynchronous memory tag fault.\n");
  print_pointer_tags(addr);

  if (logical_tag != 0)
    if (allocation_tag == 0)
      printf(
          "\nProgram tried to access unallocated memory, or use after free.\n");
    else
      printf("\nProgram tried to access an allocation using an incorrect tag. "
             "Possibly a buffer overflow from a different allocation.\n");

  exit(1);
}

// The following functions can be called from main() to demonstrate different
// types of memory safety issue.

void use_after_free() {
  // ptr (logical tag N) -> 112 bytes allocation (allocation tag N)
  // ptr (logical tag N) -> 112 bytes free (allocation tag 0)

  // This sets a non-zero allocation tag.
  char *ptr = simple_malloc(100);
  // This resets the allocation tag to 0.
  simple_free(ptr);
  // We then try to use a non-zero logically tagged pointer to access zero
  // allocation tagged memory.
  *ptr = 'a';
}

void buffer_overflow() {
  // ptr  (logical tag N) -> 32 bytes allocation (allocation tag N)
  // ptr2 (logical tag M) -> 32 bytes allocation (allocation tag M)

  // Note that due to rounding up to 16 byte granule sizes, some overflow
  // may be allowed. This example is 12 bytes, which will be 20 to include the
  // 8 byte header. That rounds up to 32 bytes (2 granules).
  char *ptr = simple_malloc(12);
  // This will be allocated immediately after the first allocation.
  char *ptr2 = simple_malloc(12);
  // This is out of bounds as far as C is concerned but not caught because
  // the allocation for ptr is actually bigger than 12 bytes. It is an overflow,
  // but it does not corrupt ptr2's data.
  *(ptr + 12) = '?';
  // We can go up to this limit. As the pointer we have is actually 8 bytes
  // beyond the start of the 32 byte allocation.
  *(ptr + 23) = '?';
  // One more byte and we're into the next granule and the tag check fails
  // because we're trying to write to ptr2's allocation.
  *(ptr + 24) = '?';
}

void double_free() {
  // ptr  (logical tag N) -> 16 bytes allocation (allocation tag N)
  //
  // ptr  (logical tag N) -> 16 bytes free (allocation tag 0)
  //
  // ptr  (logical tag N) ---\
  //                         --> 16 bytes allocation (allocation tag M)
  // ptr2 (logical tag M) ---/
  //
  // (next part is prevented by memory tagging)
  //
  // ptr  (logical tag N) ---\
  //                         --> 16 bytes free (allocation tag 0)
  // ptr2 (logical tag M) ---/

  // Without memory tagging, this code would free ptr2 by calling free twice
  // with ptr.
  int *ptr = simple_malloc(sizeof(int));
  simple_free(ptr);
  int *ptr2 = simple_malloc(sizeof(int));
  // simple_free checks that the logical tag in ptr matches the allocation tag
  // of the location it points to. It does not because there should have been
  // a different allocation tag set when ptr2 was allocated. Seeing this, the
  // allocator stops the program before corruption can take place.
  simple_free(ptr);
  // When using random tag values, there is a 1 in 16 chance that ptr and ptr2
  // will get the same allocation tag. In this case, the second free works and
  // frees ptr2. Now ptr2 points to allocation tags of 0, so this access will
  // fail.
  *ptr2 = '?';
}

int main() {
  if (!(getauxval(AT_HWCAP2) & HWCAP2_MTE)) {
    printf("error: MTE feature not detected. Make sure the version of QEMU you "
           "are running supports MTE and has it enabled.\n");
    exit(2);
  }

  simple_heap_init();

  // Register a handler to catch memory tag exceptions.
  struct sigaction sa;
  memset(&sa, 0, sizeof(sa));
  sigemptyset(&sa.sa_mask);
  sa.sa_sigaction = handle_segv;
  sa.sa_flags = SA_SIGINFO;
  sigaction(SIGSEGV, &sa, NULL);

  // Call one of the above functions here to see how memory tagging handles
  // that type of memory safety issue.

  // use_after_free();
  // buffer_overflow();
  double_free();

  return 0;
}

```

## Build the source code

You are now ready to build the source code.

First, use `cmake` to configure the project:
```bash
cmake . -G Ninja -DCMAKE_C_COMPILER=aarch64-linux-gnu-gcc -DCMAKE_C_FLAGS="-static -march=armv8.5-a+memtag" -DCMAKE_BUILD_TYPE=Debug
```

`-march=armv8.5-a+memtag` tells the compiler that we want to use the memory tagging extension (MTE).

`-static` tells the compiler to build a statically linked binary which is standalone. We'll be using QEMU to emulate the binary and having a statically
linked binary makes this simpler.

Next build the project with `ninja`:
```bash
ninja
```

You should now see a `demo` file in the current directory.

## Run the Program

Unless you are actually on memory tagging capable hardware, you will need to run
the binary using QEMU user mode emulation.

```bash { ret_code="1" }
qemu-aarch64 demo
```

The exit codes used by the program are:

- 0 - no memory misuse detected
- 1 - memory misuse detected
- 2 - MTE not supported (because your version of QEMU is too old or your native hardware does not have MTE).

The command above will return an exit code of 1. This is expected as it is set up
to run the `double_free` function which causes an MTE exception.

## Review the program output

The allocator has logging built in to show you what is happening at each step.
Due to technologies like Address Space Layout Randomisation (ASLR), the output
may not be exactly the same each time. However, the actions of the allocator will
be the same each time.

This is the typical output:
```text
Simple heap init:
Storage [0x0000400000802000 -> 0x0000400000803000) (4096 bytes)
[0x0000400000802000] Set header to [     free, size = 4096 bytes]
Ranges:
  [0x0000400000802000 -> 0x0000400000803000) : [memory tag: 0x0] [     free, size = 4096 bytes]
```

The output above shows the start up of the heap. It has allocated a large amount
of memory that it has tagged with tag `0` and it has recorded it as a single
range of free memory.

```text
Trying to allocate 4 bytes
[0x0000400000802000] Set header to [allocated, size = 16 bytes]
[0x0000400000802010] Set header to [     free, size = 4080 bytes]
Memory was allocated at 0x0100400000802000, size 16 bytes (12 byte overhead)
Ranges:
  [0x0100400000802000 -> 0x0100400000802010) : [memory tag: 0x1] [allocated, size = 16 bytes]
  [0x0000400000802010 -> 0x0000400000803000) : [memory tag: 0x0] [     free, size = 4080 bytes]
```

When the program makes a request to the allocator, you will see that in the logs.
In this case the program tries to allocate 4 bytes of memory.

To do this, the allocator had to write to 2 range headers. The first to change
its size to 16 bytes (due to overhead that will be explained later). The second to
create a new header to mark the other 4080 bytes of the heap as free.

One thing to note here is that memory addresses, for example `0x0100400000802000`
include the memory tag value of `1` as you see in the top byte `0x01`.

When the ranges are shown, the pointers include the memory tag but the tag is
also printed separately to make it easier to read.

In these cases, the logical tag (the tag in the pointer) and the allocation tag
(the tag in the memory) will always be the same. We expect this because we are
assuming that our allocator has set both correctly.

When we look at memory misuse, you will see situations where the logical
tags from the program do not match the allocation tags set by the allocator.
This difference is what allows MTE to prevent these problems.
