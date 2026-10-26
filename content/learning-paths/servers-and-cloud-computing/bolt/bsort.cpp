#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ARRAY_LEN 10000
#define FUNC_COPIES 5
volatile bool Cond = false;
#define COND() (__builtin_expect(Cond, true))

#define NOPS(N) \
  asm volatile( \
      ".rept %0\n" \
      "nop\n" \
      ".endr\n" \
      : : "i"(N) : "memory")

// Swap functionality plus some cold blocks.
#define SWAP_FUNC(ID) \
    static __attribute__((noinline)) \
    void swap##ID(int *left, int *right) { \
        if (COND()) NOPS(300); \
        int tmp = *left; \
        if (COND()) NOPS(300); else *left = *right; \
        if (COND()) NOPS(300); else *right = tmp; \
    }

// Aligned at 16KiB
#define COLD_FUNC(ID) \
    static __attribute__((noinline, aligned(16384), used)) \
    void cold_func##ID(void) { \
        asm volatile("nop"); \
    }

// Create copies of swap, and interleave with big chunks of cold code.
SWAP_FUNC(1) COLD_FUNC(1)
SWAP_FUNC(2) COLD_FUNC(2)
SWAP_FUNC(3) COLD_FUNC(3)
SWAP_FUNC(4) COLD_FUNC(4)
SWAP_FUNC(5) COLD_FUNC(5)

typedef void (*swap_fty)(int *, int *);
static swap_fty const swap_funcs[FUNC_COPIES] = {
    swap1, swap2, swap3, swap4, swap5
};


/* Sorting Logic */
void bubble_sort(int *a, int n) {
    if (n <= 1)
        return;

    int end = n - 1;
    int swapped = 1;
    unsigned idx = 0;

    while (swapped && end > 0) {
        swapped = 0;
        // pick a different copy of the swap function, in a round-robin fashion
        // and call it.
        for (int i = 1; i <= end; ++i) {
            if (a[i] < a[i - 1]) {
                auto swap_func = swap_funcs[idx++];
                idx %= FUNC_COPIES;
                swap_func(&a[i - 1], &a[i]);
                swapped = 1;
            }
        }
        --end;
    }
}

void sort_array(int *data) {
    for (int i = 0; i < ARRAY_LEN; ++i) {
        data[i] = rand();
    }
    bubble_sort(data, ARRAY_LEN);
}

/* Timers, helpers, and main */
static struct timespec timer_start;
static inline void start_timer(void) {
    clock_gettime(CLOCK_MONOTONIC, &timer_start);
}

static inline void stop_timer(void) {
    struct timespec timer_end;
    clock_gettime(CLOCK_MONOTONIC, &timer_end);
    long long ms = (timer_end.tv_sec - timer_start.tv_sec) * 1000LL +
                   (timer_end.tv_nsec - timer_start.tv_nsec) / 1000000LL;
    printf("%lld ms ", ms);
}

static void print_first_last(const int *data, int n) {
    if (n <= 0)
        return;

    const int first = data[0];
    const int last = data[n - 1];
    printf("(first=%d last=%d)\n", first, last);
}

int main(void) {
    srand(0);
    printf("Bubble sorting %d elements\n", ARRAY_LEN);
    int data[ARRAY_LEN];

    start_timer();
    sort_array(data);
    stop_timer();

    print_first_last(data, ARRAY_LEN);
    return 0;
}
