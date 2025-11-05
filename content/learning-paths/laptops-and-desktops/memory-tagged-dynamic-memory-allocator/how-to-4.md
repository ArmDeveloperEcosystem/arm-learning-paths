---
title: Preventing Mistakes By Using Memory Tagging
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

At this point, you have a working memory allocator that tags the memory it manages.
In this section we will show you a few classic memory allocation mistakes that
this allocator can prevent because it uses memory tagging.

**Note:** the allocator used here is a demo and, therefore, does not make optimal
use of memory tagging from either a security or performance point of view. Any
production code should be rigorously tested.

## How to Use These Examples

The demo program starts in `main.c` and each of these example exploits is
written as a function you can call from the `main` function. Put these calls
after the call to `sigcation` and before `return 0;`.

## Signal Handling

When a memory tagging fault occurs, the kernel will convert this into a signal
and send it to the program. To explain the memory tag faults, `main.c`
includes a signal handler that is aware of memory tagging.

`handle_segv` is called whenever there is a segmentation fault, which we assume
in our case to always be memory tagging related. When the signal is received,
`handle_segv` will print output to tell you that an exception
has happened along with the pointer that was used and the allocation tag of the
memory it points to.

In addition, the handler attempts to diagnose the problem. This detection will
only catch the common cases and may misdiagnose others.

## Buffer Overflow Example

To try this exploit call `buffer_overflow()` from `main`. You can do this by uncommenting the call to the function in `main.c` and rebuilding `demo`:

```text
Program caused an asynchronous memory tag fault.
  Pointer: 0x0100400000802020    Logical tag: 1
Points to: 0x0000400000802020 Allocation tag: 2

Program tried to access an allocation using an incorrect tag. Possibly a buffer overflow from a different allocation.
```

Buffer overflow is one of the most well known memory safety issues. A pointer to one buffer is
incremented too far and is used to access another buffer that is adjacent in memory.

`buffer_overflow` does 2 allocations:
```C
char *ptr = simple_malloc(12);
char *ptr2 = simple_malloc(12);
```

As our allocator is very predictable, we know these will be sequential (minus
padding, more on that later) in memory.

```text
| ptr1 | ptr2 | Free memory...|
```

The code uses `ptr1` to read the contents of that allocation. When it increments
`ptr1` too far, it actually tries to read the `ptr2` allocation.

```text
Ranges:
  [0x0100400000802000 -> 0x0100400000802020) : [memory tag: 0x1] [allocated, size = 32 bytes]
  [0x0200400000802020 -> 0x0200400000802040) : [memory tag: 0x2] [allocated, size = 32 bytes]
  [0x0000400000802040 -> 0x0000400000803000) : [memory tag: 0x0] [     free, size = 4032 bytes]
```

The two allocations have different memory tags. The program attempts
to use `ptr1` (tag 1) to access the allocation at `ptr2` (which expects tag 2).
This generates the exception.

Note that even though the program allocated only 4 bytes, this got padded to 16.
So, in fact, the program can overflow into the padding space before it would
get to `ptr2`'s allocation. This could be considered a flaw but in terms of
data integrity, it's not an issue because the contents of the `ptr2` allocation
are not at risk. That said, if you can fix issues like this, you should do so.

The use of `0` to tag free memory means that if this overflow were from `ptr2`
into the free memory, it would also be detected as we know that a pointer
to allocated memory will never have a `0` tag.

The final detail here is that when using random tag values, a buffer
overflow may not be detected unless the allocator is smart about choosing
tag values (which this allocator is not).

Imagine we randomly assigned tag `3` to both allocations:
```text
Ranges:
  [0x0300400000802000 -> 0x0100400000802020) : [memory tag: 0x3] [allocated, size = 32 bytes]
  [0x0300400000802020 -> 0x0200400000802040) : [memory tag: 0x3] [allocated, size = 32 bytes]
  [0x0000400000802040 -> 0x0000400000803000) : [memory tag: 0x0] [     free, size = 4032 bytes]
```

Now we will not detect the buffer overflow because the tags still match.
A smarter allocator could avoid this by randomizing tags and excluding the tags
immediately surrounding the new allocation.

## Use After Free Example

To try this exploit, call `use_after_free` from `main`. You can do this by uncommenting the call to the function in `main.c` and rebuilding `demo`:

```
Program caused an asynchronous memory tag fault.
  Pointer: 0x0100400000802008    Logical tag: 1
Points to: 0x0000400000802008 Allocation tag: 0

Program tried to access unallocated memory, or use after free.
```

A use after free happens when you allocate memory, free that memory, then
attempt to access the memory again. Note that you should not do this but, without memory
tagging or other sanitizers, nothing prevents you from doing so.

We can see that this has happened here because the pointer used to access memory
(`0x0100400000802008`) is that of the first allocation.

```text
Ranges:
  [0x0100400000802000 -> 0x0100400000802070) : [memory tag: 0x1] [allocated, size = 112 bytes]
  [0x0000400000802070 -> 0x0000400000803000) : [memory tag: 0x0] [     free, size = 3984 bytes]
```

When it was first allocated, that memory (`0x0000400000802008`) had its
allocation tags set to 1 to match the logical tag in the pointer.

```text
Ranges:
  [0x0000400000802000 -> 0x0000400000802070) : [memory tag: 0x0] [     free, size = 112 bytes]
  [0x0000400000802070 -> 0x0000400000803000) : [memory tag: 0x0] [     free, size = 3984 bytes]
```

When the allocation was freed, the allocation tags were set to 0 so that
access to that memory with a non-zero tag would raise an exception, which is
what has happened here.

If not caught, issues like this can lead to memory corruption as the
memory used for the original allocation may have been reused for a different
allocation. It may now contain secret data or data that can alter control flow
in a significant way.

For an allocator that stores its own metadata in the heap (as this allocator does),
a use after free can also corrupt that metadata potentially damaging many
allocations.

## Double Free Example

To use this example, call `double_free` from `main`:

```text
Program attempted an invalid free
  Pointer: 0x0200400000802018    Logical tag: 2
Points to: 0x0000400000802018 Allocation tag: 3
```

A double free occurs when memory is allocated, freed and then freed again.
This should not happen as a single allocation should only allocated once, and freed once.

This may not look like a problem but remember that many allocators (including the
one here) store metadata inside the heap. The second free can trick the allocator
into updating what it thinks is metadata for the allocation. This metadata may
now be tracking a different allocation or even be user data inside of a newer
allocation. Either way, without some kind of protection, the heap would become
corrupted.

In the case of the demo:
```C
int *ptr = simple_malloc(sizeof(int));
simple_free(ptr);
int *ptr2 = simple_malloc(sizeof(int));
simple_free(ptr);
```

`ptr` is the first allocation, which is then freed. At that point the ranges are:
```text
Ranges:
  [0x0000400000802000 -> 0x0000400000802010) : [memory tag: 0x0] [     free, size = 16 bytes]
  [0x0000400000802010 -> 0x0000400000803000) : [memory tag: 0x0] [     free, size = 4080 bytes]
```

`ptr2` is the second allocation which, being the same size allocation, is put
where `ptr` used to be.

`ptr` has tag `1`, `ptr2` will have tag `2`.

```text
Ranges:
  [0x0200400000802000 -> 0x0200400000802010) : [memory tag: 0x2] [allocated, size = 16 bytes]
  [0x0000400000802010 -> 0x0000400000803000) : [memory tag: 0x0] [     free, size = 4080 bytes]
```

Now when the program calls `simple_free(ptr)`, its using a pointer that points
to the `ptr2` allocation but it does not have logical tag 2.

We could let this fault while `simple_free` attempts to access the
range's header but the problem becomes hard to diagnose from there. Instead,
`simple_free` has an early check for this specific issue.

```C
  // Detect attempts to free an allocation more than once.
  uint8_t logical_tag = get_logical_tag(ptr);
  uint8_t allocation_tag = get_memory_tag(ptr);
  if (logical_tag != allocation_tag) {
    printf("\nProgram attempted an invalid free\n");
    print_pointer_tags(ptr);
    exit(1);
  }
```

If you are attempting to free memory using an incorrectly tagged pointer,
this is invalid. This applies whether it actually points to an allocated range
or to free space. Letting either happen could corrupt the internal structures of the heap.

## Undefined Malloc And Free Behavior

The C standard library defines `free` as expecting to be given a pointer that
is exactly the same as that which was produced by `malloc`. Therefore, it is
undefined behavior to pass a modified pointer to free, for example, as a pointer to
the middle of an allocation rather than the start.

This doesn't mean that an implementation can't accept a modified pointer. It
means that when software passes a modified pointer, it cannot make assumptions
about what will happen based purely on the C standard.

Some implementations choose to allow differences in the pointer as long as it
points to the same allocation. Our memory tagging allocator is stricter than
that. Despite the pointer's logical tag not changing where it points to, the allocator
will not allow you to use a pointer with an incorrect tag.

Looking at the examples above, you can see why the ranges of behavior allowed by
the standard (or rather, left undefined) can be useful for different use cases.

If you wanted to make our allocator less strict, you could disable tag checking.
If you want to experiment with that, replacing `PR_MTE_TCF_SYNC` with `PR_MTE_TCF_NONE` is the first step.

An allocator that can vary the strictness of its checks like this can be useful for porting existing software that has memory problems.

* Run the program with strict checks
* Find a memory fault
* Fix that fault
* Run the program without strict checks to confirm the fix did not break any functionality
* Repeat the steps until your program is free of memory faults
