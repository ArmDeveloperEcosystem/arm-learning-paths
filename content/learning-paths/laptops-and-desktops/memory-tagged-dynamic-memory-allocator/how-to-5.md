---
title: Memory Tagged Allocation Summary
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

By following this learning path, you have seen how the Memory Tagging Extension (MTE)
can be used by a dynamic memory allocator to prevent common types of memory misuse.

Remember that due to MTE's limited granularity and number of tag values, the quality
of the experience is very much influenced by the quality of the software using it.
MTE requires that software co-operate with hardware.

The software shown here works but should not be considered production quality as it is purely for learning purposes.

Any software you write that uses MTE should be actively tested to prove that the issues you most care about are prevented, as you expect them to be.

If you're keen to learn more about using the allocator we have shown, here are a few ideas for extensions.

## Try Different Memory Exploits

We have only shown the most common memory issues here. There are plenty of other types and variants of those types, that MTE may or may not be able to stop.

Find some example code and see if the allocator detects the issue. Perhaps it does but diagnosing the issue is very difficult.

Often the ability to find the source of a problem is just as important as knowing it exists. A double free diagnosed as a buffer overflow could waste a significant amount of engineering time.

## Improved Tag Value Selection

Try using the random tag generation mode (`randomise_memory_tags = true`) with
a few of the example exploits. You will see that sometimes the tags of two allocations
will happen to be the same value. This means that some of the memory exploits
are not detected.

To stop this happening, an improved allocator could read the tags surrounding an
allocation and select one that has not been used.

```text
| allocation 1 | free  | allocation 2 |
| tag 1        | tag 0 | tag 5        |
```

If we were about to allocate the space in the middle of the table above, we could
use any tag that is not 0, 1, or 5.

This, of course, would not help when the allocations are not next to each other.
Consider this heap:
```text
| allocation 1 | allocation 2 | allocation 3 |
| tag 1        | tag 2        | tag 1        |
```

If you had a pointer `p1` that was meant to be used with `allocation 1`, you could
increment that to point beyond `allocation 2`, all the way into `allocation 3`.
You could still "buffer overflow" as long as the amount you overflow
by is larger than `allocation 2`. If the amount is less than that, `p1` would point
into `allocation 2` and the problem would be caught as we would expect.

There is likely to be no perfect solution here, as we cannot prevent a program "jumping"
across a gap like this. There could be ways to mitigate it by increasing the
window of tag values we look at when generating a new tag. In the first example
we just looked at the adjacent allocations. We could instead include the 4
allocations either side of the new allocation or use a distance in memory.

Whether any of this makes a difference will come down to what the software
is doing. Which is all the more reason to have example exploits as we have shown
as a "test suite" for any memory protection you are implementing.

It is likely that these choices will not be binary. You may not be able to catch
all of the problems, all of the time but you are able to catch the majority that
you do care about, most of the time.

## Handling Small Allocations Differently

MTE using 16 byte granules increases the overhead of small allocations. To be fair
to MTE, we already had this problem with the original allocator due to its 8 byte
range header.

You could consider whether small allocations are likely to be used in a way that
means that they should be protected in the same way as larger allocations. Is an
allocation of 4 bytes as likely to be treated as an array versus an allocation
of 256 bytes?

You could never say for sure as a library writer but, perhaps as an author of a full stack of software, you could. Certainly this technique has been used by compilers, where variables that are only accessed by a fixed address can be protected less strongly than those that are clearly arrays where a pointer is being incremented.

If you are working with your own stack, you could even have an option in the allocator
to not protect certain allocations. Perhaps a pool of normal memory and a pool
with memory tags. One of the costs of memory tagging is the allocation tag storage,
so this could be an interesting trade off.
