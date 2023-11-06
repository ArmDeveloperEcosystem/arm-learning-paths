---
title: Dynamic Memory Allocation
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Dynamic vs. Static Allocation

In this learning path you will learn how to implement dynamic memory allocation.
If you have used C's "heap" (`malloc`, `free`, etc.) before, that is one example
of dynamic memory allocation.

It allows programs to allocate memory while they are running without knowing
at build time what amount of memory they will need. In contrast to static
memory allocation where the amount is known at build time.

```C
#include <stdlib.h>

void fn() {
    // Static allocation
    int a = 0;
    // Dynamic allocation
    int *b = malloc(sizeof(int));
}
```

The example above shows the difference. The size and location of `a` is known
when the program is built. The size of `b` is also known, but its location is not.

It may even never be allocated, as this pseudocode example shows:

```C
int main(...) {
    if (/*user has passed some argument*/) {
        int *b = malloc(sizeof(int));
    }
}
```

If the user passes no arguments to the program, there's no need to allocate space
for `b`. If they do, `malloc` will find space for it.

## malloc

The C standard library provides a special function
[`malloc`](https://en.cppreference.com/w/c/memory/malloc). `m` for "memory",
`alloc` for "allocate". This can be used to ask for a suitably sized memory
location while the program is running.

```C
void *malloc(size_t size);
```

The C library will then look for a chunk of memory with size of at least `size`
bytes in a large chunk of memory that it has reserved. For instance on Ubuntu
Linux, this will be done by GLIBC.

The example at the top of the page is trivial of course. As it is we could just
statically allocate both integers like this:
```C
void fn() {
    int a, b = 0;
}
```

That's ok if this data is never be returned from this function. Or in other
words, if the lifetime of this data is equal to that of the function.

A more complicated example will show you when that is not the case, and the value
lives longer than the function that created it.

```C
#include <stdlib.h>

typedef struct Entry {
    int data;
    // NULL if end of list, next entry otherwise.
    struct Entry* next;
} Entry;

void add_entry(Entry *entry, int data) {
    // New entry, which becomes the end of the list.
    Entry *new_entry = malloc(sizeof(Entry));
    new_entry->data = data;
    new_entry->next = NULL;

    // Previous tail now points to the newly allocated entry.
    entry->next = new_entry;
}
```

What you see above is a struct `Entry` that defines a singly-linked-list entry.
Singly meaning that you can go forward via `next`, but you cannot go backwards
in the list. There is some data `data`, and each entry points to the next entry,
`next`, assuming there is one (it will be `NULL` for the end of the list).

`add_entry` makes a new entry and adds it to the end of the list.

Think about how you would use these functions. You could start with some known
size of list, like a global variable for the head (first entry)
of our list.

```C
Entry head = {.data = 123, .next=NULL};
```

Now you want to add another `Entry` to this list at runtime. So you do not know
ahead of time what it will contain, or if we indeed will add it or not. Where
would you put that entry?

* If it is another global variable, we would have to declare many empty `Entry`s
  and hope we never needed more than that amount.

{{% notice Other Allocation Techniques%}}
Although in this specific case global variables aren't a good solution, there are
cases where large sets of pre-allocated objects can be beneficial. For example,
it provides a known upper bound of memory usage and makes the timing of each
allocation predictable.

However, we will not be covering these techniques in this learning path. It will
however be useful to think about them after you have completed this learning
path.
{{% /notice %}}

* If it is in a function's stack frame, that stack frame will be reclaimed and
  modified by future functions, corrupting the new `Entry`.

So you can see, we must use dynamic memory allocation. Which is why the `add_entry`
shown above calls `malloc`. The resulting pointer points to somewhere not in
the program's global data section or in any function's stack space, but in the
heap memory. Where it can live until we `free` it.

## free

You cannot ask malloc for memory forever. Eventually that space behind the scenes
will run out. So you should give up your dynamic memory once it is not needed,
using [`free`](https://en.cppreference.com/w/c/memory/free).

```C
void free(void *ptr);
```

You call `free` with a pointer previously given to you by `malloc`, and this tells
the heap that we no longer need this memory.

{{% notice Undefined Behaviour%}}
You may wonder what happens if you don't pass the exact pointer to `free`, as
`malloc` returned to you. The result varies as this is "undefined behaviour".
Which essentially means a large variety of unexpected things can happen.

In practice, many allocators will tolerate this difference or reject it outright
if it's not possible to do something sensible with the pointer.

Remember that just because one allocator handles this a certain way, does not
mean all will. Indeed, that same allocator may handle it differently for
different allocations within the same program.
{{% /notice %}}

So, you can use `free` to remove an item from your linked list.

```C
void remove_entry(Entry* previous, Entry* entry) {
    // NULL checks skipped for brevity.
    previous->next = entry->next;
    free(entry);
}
```

`remove_entry` makes the previous entry point to the entry after the one we want
to remove, so that the list skips over it. With `entry` now isolated we call
`free` to give up the memory it occupies.

```text
----- List ------ | - Heap --
[A] -> [B] -> [C] | [A][B][C]
                  |
[A]    [B]    [C] | [A][B][C]
 |-------------^  |
                  |
[A]---------->[C] | [A]   [C]
```

That covers the high level how and why of using `malloc` and `free`, next you'll
see a possible implementation of a dynamic memory allocator.