---
title: Implementing a Dynamic Memory Allocator
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Project Structure

The file layout will be as follows:
* `CMakeLists.txt` - To tell `cmake` how to configure the project.
* `heap.c` - The dynamic memory allocator implementation.
* `heap.h` - Function declarations including your new `simple_malloc` and
	`simple_free` functions.
* `main.c` - A program that makes use of `simple_malloc` and `simple_free`.

Building it will produce a single binary, `demo`, that you will run to see the
results.

## Sources

### CMakeLists.txt

``` {file_name="CMakeLists.txt"}
cmake_minimum_required(VERSION 3.15)

project(MemoryAllocatorDemo C)

add_executable(demo main.c heap.c)
```

#### heap.h

```C {file_name="heap.h"}
#include <stddef.h>

// Call once at the start of main() to initialise the empty heap.
// This is the equivalent of what your C library is doing before main() for the
// system heap.
void simple_heap_init();

void *simple_malloc(size_t size);

void simple_free(void *ptr);
```

## heap.c

Please refer to the comments in the source code here for detailed explanations
of each function. We will cover the key elements here up front.

First is `storage`, this is the backing storage which is a global char array.
This is where the ranges, represented by `Header`, are stored.

Each `Header` is written to the start of the allocated range. This means that
`malloc` returns a pointer that points just beyond this location. `free` on the
other hand, deducts the size of `Header` from the pointer parameter to find the
range information.

When the heap is initialised with `simple_heap_init`, a single range is setup
that covers the whole heap and marks it as unallocated.

To find a free range, `find_free_space` walks the heap using these `Header`
values until it finds a large enough free range, or gets beyond the end of the
heap.

For the first allocation the job is straightforward. There's one range and it's
all free. Split that into 2 ranges, using the first for the allocation.

On subsequent allocations there will be more header values to read, but the
logic is the same.

{{% notice Addresses in Logging%}}
The logging enabled by `log_events` may not have deterministic output
on systems where features like Address Space Layout Randomisation (ASLR) are
enabled. Generally run to run, the output addresses may change. Focus on the
relative values of pointers in relation to where the heap starts and ends.
{{% /notice %}}

```C {file_name="heap.c"}
#include <assert.h>
#include <stdarg.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

// Enable logging of heap events and current memory ranges.
static bool log_events = true;

// printf but can be globally disabled by setting log_events to false.
static void log_event(const char *fmt, ...) {
  if (log_events) {
    va_list args;
    va_start(args, fmt);
    vprintf(fmt, args);
    va_end(args);
  }
}

// We will allocate memory from this statically allocated array. If you are on
// Linux this could be made dynamic by getting it from mmap.
#define STORAGE_SIZE 4096
static char storage[STORAGE_SIZE];
// If our search reaches this point, there is no free space to allocate.
static const char *storage_end = storage + STORAGE_SIZE;

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
  log_event("0x%016lx (%s, size = %u bytes)\n", header,
            header.allocated ? "allocated" : "free", header.size);
}

static Header read_header(const char *ptr) { return *(Header *)ptr; }

static void write_header(char *ptr, Header header) {
  *(Header *)ptr = header;
  log_event("[%p] Set header to ", ptr);
  log_header(header);
}

// Log a table showing the ranges currently marked in the heap.
static void log_ranges() {
  Header header = {.size = 0, .allocated = false};
  for (const char *header_ptr = storage; header_ptr < storage_end;
       header_ptr += header.size) {
    header = read_header(header_ptr);
    log_event("  [%p -> %p) : ", header_ptr, header_ptr + header.size);
    log_header(header);
  }
}

void simple_heap_init() {
  log_event("Simple heap init:\n");
  log_event("Storage [%p -> %p) (%d bytes)\n", storage, storage_end,
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
  char *allocated = find_free_space(required_size);

  if (!allocated) {
    log_event("Heap exhausted.\n");
    return NULL;
  }

  // Split the found range into this new allocation and a new free range after
  // it.
  split_range(allocated, required_size);

  // Return a pointer to after the header.
  allocated += sizeof(Header);

  log_event("[%p] Memory was allocated, size %ld bytes\n", allocated, size);
  log_ranges();
  return allocated;
}

// Free the allocation pointed to by ptr. This simply sets the range to free,
// does not change its size of any of its contents.
void simple_free(void *ptr) {
  if (!ptr)
    return;

	assert(((char*)ptr > storage) && ((char*)ptr < storage_end) &&
         "Trying to free pointer that is not within the heap.");

  log_event("\n[%p] Freeing allocation\n", ptr);

  // This will point to after the header of the range it's in, so we must walk
  // back a bit.
  char *header_ptr = (char *)ptr - sizeof(Header);

  Header header = read_header(header_ptr);
  assert(header.size != 0 && "Can't free an allocation of zero size.");

  // Mark this range as free, leave the size unchanged.
  header.allocated = false;
  write_header(header_ptr, header);

  log_event("[%p] Memory was freed\n", ptr);
  log_ranges();
}
```

### main.c

```C { file_name="main.c"}
#include "heap.h"

int main() {
  simple_heap_init();

  char *ptr = simple_malloc(100);
  char *ptr2 = simple_malloc(240);
  char *ptr3 = simple_malloc(256);
  char *ptr4 = simple_malloc(333);
  simple_free(ptr2);
  simple_free(ptr3);
  char *ptr5 = simple_malloc(300);

  return 0;
}
```

The code here does allocation and deallocation of memory. This tests the heap
code but also highlights an interesting problem that you'll see more about later.

## Building

First install dependencies.

```bash
sudo apt install -y cmake ninja-build
```

Then configure using CMake. We recomend a Debug build for the extra safety the
asserts bring.

```bash
cmake . -DCMAKE_BUILD_TYPE=Debug -G Ninja
```

Then build with `ninja`

```bash
ninja
```

This should result in a `demo` executable in the same folder. Run this to see
the allocator in action.

```bash
./demo
```

## Output

The output addresses will vary depending on where backing memory gets allocated
by your system but this is the general form you should expect:

```text
Simple heap init:
Storage [0x559871a24040 -> 0x559871a25040) (4096 bytes)
[0x559871a24040] Set header to 0x0000000000001000 (free, size = 4096 bytes)
  [0x559871a24040 -> 0x559871a25040) : 0x0000000000001000 (free, size = 4096 bytes)
```

The addresses on the left usually refer to an action. In this case we've set
a `Header` value at `0x559871a24040`.

The list in the last lines is the set of ranges you would see if you walked the
heap. Exactly what the allocator is seeing. The use of `[` followed by `)`
means that the start address is included in the range, but the end address is
not. This is the initial heap state where everything is free.

Next there is a call `simple_malloc(100)` which produces:

```text
Trying to allocate 100 bytes
[0x55e68c41f040] Set header to 0x800000000000006c (allocated, size = 108 bytes)
[0x55e68c41f0ac] Set header to 0x0000000000000f94 (free, size = 3988 bytes)
[0x55e68c41f048] Memory was allocated, size 100 bytes
  [0x55e68c41f040 -> 0x55e68c41f0ac) : 0x800000000000006c (allocated, size = 108 bytes)
  [0x55e68c41f0ac -> 0x55e68c420040) : 0x0000000000000f94 (free, size = 3988 bytes)
```

You see that a request was made for 100 bytes and the allocator decided to split
the 1 range into 2. It updated both the new ranges' header information.

Note that although it says `[0x559871a24048] Memory was allocated`, you do not
see a range starting from this address. This is because this address is the one
returned to the user. Take the size of `Header` from this address and you get the
start of the range which is `0x559871a24040` as shown in the first range in the
list.

You'll also notice that the allocated range is 8 bytes bigger than what the user
asked for. This is because it includes that `Header` at the start of it.

If you skip ahead to after the `free` calls have been made you will see:

```text
[0x55e68c41f1ac] Freeing allocation
[0x55e68c41f1a4] Set header to 0x0000000000000108 (free, size = 264 bytes)
[0x55e68c41f1ac] Memory was freed
  [0x55e68c41f040 -> 0x55e68c41f0ac) : 0x800000000000006c (allocated, size = 108 bytes)
  [0x55e68c41f0ac -> 0x55e68c41f1a4) : 0x00000000000000f8 (free, size = 248 bytes)
  [0x55e68c41f1a4 -> 0x55e68c41f2ac) : 0x0000000000000108 (free, size = 264 bytes)
  [0x55e68c41f2ac -> 0x55e68c41f401) : 0x8000000000000155 (allocated, size = 341 bytes)
  [0x55e68c41f401 -> 0x55e68c420040) : 0x0000000000000c3f (free, size = 3135 bytes)
```

Which shows you that the second and third allocations were freed, and there is
still a large range of free memory on the end.

Try to understand what the final allocation result is. Is the choice of location
expected or would you expect it to fit elsewhere in the heap?