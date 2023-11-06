---
title: Conclusions
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Conclusions

You've now had a glimpse into the world of dynamic memory allocation, and
probably have more questions than answers. You may have noticed some oversights
in the implementation presented, and you're almost certainly right, we'll get to
those shortly.

Overall your take away from this material is that "dynamic" memory allocation
can mean many things. Sometimes it is all dynamic, sometimes it is a dynamic
face with a static allocation behind it. This will change depending on the
performance and complexity needs of the application.

Fundamentally it provides a way to get memory you did not know whether you would
need when the program was written. You knew you would need some non-zero amount
and dynamic allocation lets you ask for it while the program is running.

The implementation shown here is a "classic" heap, and a very simple one at that
(not quite minimal, look up "bump allocator" for that).

Memory allocation is a whole field of study, and you can use this implementation
as a base for further research if you wish.

## Further Work

### Merging Free Ranges

Look again at the last logging example on the previous page.

```text
[0x55e68c41f1ac] Memory was freed
  [0x55e68c41f040 -> 0x55e68c41f0ac) : 0x800000000000006c (allocated, size = 108 bytes)
  [0x55e68c41f0ac -> 0x55e68c41f1a4) : 0x00000000000000f8 (free, size = 248 bytes)
  [0x55e68c41f1a4 -> 0x55e68c41f2ac) : 0x0000000000000108 (free, size = 264 bytes)
  [0x55e68c41f2ac -> 0x55e68c41f401) : 0x8000000000000155 (allocated, size = 341 bytes)
  [0x55e68c41f401 -> 0x55e68c420040) : 0x0000000000000c3f (free, size = 3135 bytes)
```

What's wrong with these ranges? Nothing, until you allocate something >= 249
bytes. We should be able to put that at address `0x55e68c41f0ac`, but because
we treat the 2 free ranges as separate, we can't put it there, or in the second
free range.

```text
  [0x55e68c41f0ac -> 0x55e68c41f1a4) : 0x00000000000000f8 (free, size = 248 bytes)
  [0x55e68c41f1a4 -> 0x55e68c41f2ac) : 0x0000000000000108 (free, size = 264 bytes)
```

To solve this, you would need some kind of cleanup step after a free. Where
free ranges next to each other are merged into one.

Then again, this does add some overhead. Perhaps it shouldn't be called on every
free. Think about the tradeoff there (and don't be afraid to change the data
structures you've used, they are not perfect either).

### Memory Safety (Or Lack Of)

A big problem with memory in general is code accessing or changing memory that
it should not. The allocator presented here is certainly vulnerable to all the
classic memory exploits, which you can try out yourself.

Replace the allocations in `main.c` with these to see what happens.

Use after free:
```C
  int *ptr = simple_malloc(sizeof(int));
  *ptr = 123;
  simple_free(ptr);
  int *ptr2 = simple_malloc(sizeof(int));
  *ptr = 345;
```

There's a good chance `ptr2` will point to the same place as `ptr`. Meaning that
someone could use `ptr` to modify the data now at `ptr2`. This can be even worse
if the type of that data has changed in the meantime.

Double free:
```C
  int *ptr = simple_malloc(sizeof(int));
  simple_free(ptr);
  int *ptr2 = simple_malloc(sizeof(int));
  simple_free(ptr);
  int *ptr3 = simple_malloc(sizeof(int));
  // Ends up changing *ptr2 as well.
  *ptr3 = 123;
```

Here you see the allocation `ptr` is freed once, then `ptr2` is allocated, likely
at the same place as `ptr`. When `ptr` is freed again, this would free the `ptr2`
allocation as well.

Meaning that instead of being its own allocation, `ptr3` also ends up pointing
to the same location as `ptr2`. So modifying one modifies the other.

Another possibility is that memory that was previously freed is used as part of
a larger allocation. So the original range header is now in the middle of the
new allocation.

When free is called for the second time, the allocator may blindly write to where
it would have stored the metadata for the original allocation. In doing so, it will
corrupt the original allocation.

Buffer overflow:
```C
  char *ptr = simple_malloc(4);
  char *ptr2 = simple_malloc(4);
  ptr[4] = 1;
```

`ptr` is a 4 item array, `ptr2` is also a 4 byte array immediately after the
first one. Writing to `ptr[4]` overflows the array, because the maximum index
is only 3.

This would corrupt the header attached to the `ptr2` allocation. In the case
of your allocator, it would likely change the size of the allocation to just 1
byte.

That's a selection of the many, many, possible attacks on the heap.

You could consider how they might be mitigated, or even try applying some of
them to the heap you have just written.

### Special Case Allocators

Imagine you are writing a video game with a fixed memory budget and need
predictable performance. Do you think a heap that has to walk a variable number
of ranges would be able to achieve that?

If you think it wouldn't, you could look into
[Region-Based Memory Management](https://en.wikipedia.org/wiki/Region-based_memory_management).

(whether it would or not depends entirely on your application's requirements)

This takes advantages of scenarios where you know the upper limit of objects you
will need, along with their types and sizes.

For the video game, maybe you are making a menu that will have at most 256
entries. Why not statically allocate an array of 256 menu item objects on start
up? Then simply construct a new item in place in the array as you need them.

It is more overhead if the menu is always small, but it's very predictable.
Maximum memory use is known and there is no variable time taken to walk the heap.

You could also mix this approach into a traditional heap, using areas of memory
only for certain types or sizes of data. For example, could it reduce the metadata
overhead for small allocations (e.g. a 4 byte allocation that may require > 4 bytes of
metadata)?

### LD_PRELOAD

If your allocator grows to support all the C standard library functions, you
can try using it instead of the one your system C library provides.

On Linux this is done using the environment variable `LD_PRELOAD`.

```
LD_PRELOAD=<path to your shared object> <program>
```

Any shared object in `LD_PRELOAD` gets to provide the symbols a program needs
before what it would usually load. So in this case you will provide `malloc`
and the other memory management functions.

You will have to rebuild the code as a shared object, and remove the `simple_`
prefix from the functions to do this.

Note that if you only implement a subset of the memory management functions,
the program being run will get the rest from the system C library. This will
almost certainly lead to a crash when it tries to, for example, `realloc` a
pointer that your heap produced, but instead asks the system heap to do it.

Finally, you will likely need a lot more storage for the heap. Either increase
the size of the static allocation, or consider using `mmap` to ask the kernel
for memory, as C libraries tend to do instead.