---
title: Designing a Dynamic Memory Allocator
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## High Level Design

To begin with, decide which functions your memory allocator will provide. We
have described `malloc` and `free`, there are more provided by the
[C library](https://en.cppreference.com/w/c/memory).

This will assume you just need `malloc` and `free`. Start with those and write
out their behaviors, as the programmer using your allocator will see.

There will be a function, `malloc`. It will:
* Take a size in bytes as a parameter.
* Try to allocate some memory.
* Return a pointer to that memory, NULL pointer otherwise.

There will be a function `free`. It will:
* Take a pointer to some previously allocated memory as a parameter.
* Mark that memory as available for future allocations.

From this you can see that you will need:
* Some large chunk of memory, the "backing storage".
* A way to mark parts of that memory as allocated, or available for allocation.

## Backing Storage

The memory can come from many sources. It can even change size throughout the
program's execution if you wish. For your allocator you'll keep it as simple
as possible.

A single, statically allocated global array of bytes will be your backing
storage. So you can do dynamic allocation of parts of a statically allocated
piece of memory.

```C
#define STORAGE_SIZE 4096
static char storage[STORAGE_SIZE];
```

## Record Keeping

This backing memory needs to be annotated somehow to record what has been
allocated so far. There are many, many ways to do this. With the biggest choice
here being whether to store these records in the heap itself, our outside of it.

We will not go into those tradeoffs here, and instead you will put the records
in the heap, as this is relatively simple to do.

What should be in your records? Think about what question the software will ask
us. Can you give me a pointer to an area of free memory of at least this size?

For this you will need to know:
* Which ranges of the backing storage have been allocated or not.
* How large each of ranges sections is. This includes free areas.

Where a "range" a pointer to a location, a size in bytes and a boolean to say
whether the range is free or allocated. So a range from 0x123 of 345 bytes,
that has been allocated would be:

```text
start: 0x123 size: 345 allocated: true
```

For the initial state of a heap of size `N`, you will have one range of
unallocated memory.

```text
Pointer: 0x0 Size: N Allocated: False
```

When an allocation is made you will split this free range into 2 ranges. The
first part the new allocation, the second the remaining free space. If 4 bytes
were to be allocated:

```text
Pointer: 0x0 Size: 4   Allocated: True
Pointer: 0x4 Size: N-4 Allocated: False
```

The next time you need to allocate, you will walk these ranges until you find
one with enough free space, and repeat the splitting process.

The walk works like this. Starting from the first range, add the size of that
range to the address of that range. This new address is the start of the next
range. Repeat until the resulting address is beyond the end of the heap.

```text
range = 0x0;

Pointer: 0x0 Size: 4   Allocated: False

range = 0x0 + 4 = 0x4;

Pointer: 0x4 Size: N-4 Allocated: False

range = 0x4 + (N-4) = 1 beyond the end of the heap, so the walk is finished.
```

`free` uses the pointer given to it to find the range it needs to deallocate.
Let's say the 4 byte allocation was freed:

```text
Pointer: 0x0 Size: 4   Allocated: False
Pointer: 0x4 Size: N-4 Allocated: False
```

Since `free` gets a pointer directly to the allocation you know exactly which
range to modify. The only change made is to the boolean which marks it as
allocated or not. The location and size of the range stay the same.

{{% notice Merging Free Ranges%}}
The allocator presented here will not merge free ranges like the 2 above. This
is a deliberate limitation and addressing this is discussed later.
{{% /notice %}}

## Record Storage

You'll keep these records in heap which means using some of the allocated space
for them on top of the allocation itself.

The simplest way to do this is to prepend each allocation with the range
information. This way you can skip from the start of one range to another with
ease.

```text
0x00: [ptr, size, allocated] <-- The range information
0x08: <...>                  <-- The pointer malloc returns
0x10: [ptr, size, allocated] <-- Information about the second range
<...and so on until the end of the heap...>
```

Pointers returned by `malloc` are offset to just beyond the range information.
When `free` receives a pointer, it can get to the range information by
subtracting the size of that information from the pointer. Using the example
above:

```text
free(my_ptr);

0x00: [ptr, size, allocated] <-- my_ptr - sizeof(range information)
0x08: <...>                  <-- my_ptr
```

{{% notice Data Alignment%}}
When an allocator needs to produce addresses with a specific alignment, the
calculations above must be adjusted. The allocator presented here does not
concern itself with alignment, which is why it can do a simple subtraction.
{{% /notice %}}

## Running Out Of Space

The final thing an allocator must do is realize it has run out of space. This is
simply achieved by knowing the bounds of the backing storage.

```C
#define STORAGE_SIZE 4096
static char storage[STORAGE_SIZE];
// If our search reaches this point, there is no free space to allocate.
static const char *storage_end = storage + STORAGE_SIZE;
```

If you are walking the heap and the start of the next range would be greater
than or equal to `storage_end`, you have run out of memory to allocate.