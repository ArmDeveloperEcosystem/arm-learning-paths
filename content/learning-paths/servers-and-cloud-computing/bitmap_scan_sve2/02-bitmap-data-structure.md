---
# User change
title: "Build and manage a bit vector in C"

weight: 3

layout: "learningpathall"

---
## Bitmap data structure

Now let's define a simple bitmap data structure that serves as the foundation for the different implementations. The bitmap implementation uses a simple structure with three key components:
   - A byte array to store the actual bits
   - Tracking of the physical size (bytes)
   - Tracking of the logical size (bits)

For testing the different implementations in this Learning Path, you also need functions to generate and analyze the bitmaps.

Use a file editor of your choice and then copy the code below into `bitvector_scan_benchmark.c`:

```c
// Define a simple bit vector structure
typedef struct {
    uint8_t* data;
    size_t size_bytes;
    size_t size_bits;
} bitvector_t;

// Create a new bit vector
bitvector_t* bitvector_create(size_t size_bits) {
    bitvector_t* bv = (bitvector_t*)malloc(sizeof(bitvector_t));
    bv->size_bits = size_bits;
    bv->size_bytes = (size_bits + 7) / 8;
    bv->data = (uint8_t*)calloc(bv->size_bytes, 1);
    return bv;
}

// Free bit vector resources
void bitvector_free(bitvector_t* bv) {
    free(bv->data);
    free(bv);
}

// Set a bit in the bit vector
void bitvector_set_bit(bitvector_t* bv, size_t pos) {
    if (pos < bv->size_bits) {
        bv->data[pos / 8] |= (1 << (pos % 8));
    }
}

// Get a bit from the bit vector
bool bitvector_get_bit(bitvector_t* bv, size_t pos) {
    if (pos < bv->size_bits) {
        return (bv->data[pos / 8] & (1 << (pos % 8))) != 0;
    }
    return false;
}

// Generate a bit vector with specified density
bitvector_t* generate_bitvector(size_t size_bits, double density) {
    bitvector_t* bv = bitvector_create(size_bits);
    
    // Set bits according to density
    size_t num_bits_to_set = (size_t)(size_bits * density);
    
    for (size_t i = 0; i < num_bits_to_set; i++) {
        size_t pos = rand() % size_bits;
        bitvector_set_bit(bv, pos);
    }
    
    return bv;
}

// Count set bits in the bit vector
size_t bitvector_count_scalar(bitvector_t* bv) {
    size_t count = 0;
    for (size_t i = 0; i < bv->size_bits; i++) {
        if (bitvector_get_bit(bv, i)) {
            count++;
        }
    }
    return count;
}
```

You now have a functional, compact bit vector in C for testing bitmap scanning performance. Next, you'll implement scalar, NEON, and SVE-based scanning routines that operate on this structure.