---
title: Start coding
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

With the infrastructure setup to build and test the Matrix library, it's
now time to actually code the library. 

In this section, you will add the
core functionality of the library as well as unit tests to ensure functional
correctness.

## About error handling

Error handling is a critical aspect of programming, 
balancing safety and security with performance. Depending on the context, the
correct balance point may vary. For example, in the case of high performance
computing for weather forecast, the dataset is extremely large (and ever
increasing), but can be considered secure and curated. On the other hand, if the
data used in the computations can be adversely computed or altered, it is
preferable to have checks, such as out of bound access, enabled.

In the Matrix processing library, you will implement 2 types of
checks:

- checks that impact performance (such as checking for out-of bound access at each
access). Those checks are only enabled in the `Debug` builds and the program
will exit with an assertion failure if a check fails.
- checks with minor performance impact (such as checking the matrices have the
correct dimensions in a matrix multiplication). Those checks are always enabled
and the program will exit with a message.

The idea here is to make the program fail in a noticeable way. Of course,
in a real world application, the error should be caught and dealt with by the
application (if it can). Error handling, and especially recovering from errors,
can be a very complex topic.

At the top of file `include/Matrix/Matrix.h`, include `<cassert>` to get the
C-style assertions declarations for checks in `Debug` mode only.

Next, add a `die` function to call whenever the library needs to
exit. Paste the code below right under get `getVersion` declaration in
`include/Matrix/Matrix.h`.

```CPP

/// Immediately terminates the application with \p reason as the error message
/// and the EXIT_FAILURE error code. It will also print the file name (\p
/// fileName) and line number (\p lineNumber) that caused that application to
/// exit.
[[noreturn]] void die(const char *fileName, size_t lineNumber,
                      const char *reason);

```

Note that `die` has been annotated with the `noreturn` attribute. This
is a new feature of C++ that allows the compiler to take advantage of the
fact that `die` will *not* return, so no code will be executed after it has been
called. This information was previously passed thru compiler specific
annotations, but now C++ provides a generic way to pass such information to
the different compilers.

You also need to provide a body for the `die` function. 

Open `lib/Matrix/Matrix.cpp` and include at the top of the file:

- `<cstlib>` : to get the declaration of `exit` and `EXIT_FAILURE`
- `<iostream>` : to get support for input/output, in order to emit useful
  information about the reason for exiting the program.

Add `die`'s body as shown below:

{{< include-code CPP "content/learning-paths/cross-platform/matrix/projects/chapter-3/lib/Matrix/Matrix.cpp" >}}

At this stage, the project should still build and compile, try it to confirm:

```BASH
cd build
ninja
```

## The Matrix data structure

The Matrix library will be able to deal with 1x1 matrices (i.e. scalar numbers),
1xN matrices (row-vector), Nx1 matrices (column vectors) and NxM
matrices. 

The matrix array will be a single memory region, where the matrix
elements are stored in [row major
order](https://en.wikipedia.org/wiki/Row-_and_column-major_order).

Matrices store elements. The Matrix library will support all *arithmetic*
element types, that is to say integer types (signed and unsigned) as well as
floating point types.

The Matrix data structure will have the following private data members:
- `numRows`: the number of rows in a matrix
- `numColumns`: the number of columns in a matrix
-  `data`: the actual array of elements in a matrix. Modern C++ offers
constructs in the language to deal safely with memory; you will use
`std::unique_ptr` which guaranties that the Matrix class will be safe from a
whole range of memory management errors

Add the following includes at the top of `include/Matrix/Matrix.h`:

```CPP
#include <memory>
#include <type_traits>
```

`<memory>` gives access to the `unique_ptr` and `type_traits` allow you to
query information on the Matrix element types, either to check that a type is
allowed or to select an optimized implementation at compile time.

Add the following lines to `include/Matrix/Matrix.h` in the MatComp namespace
under the `die` function declaration:

```CPP

/// The Matrix class represents N x M matrices for all arithmetic types.
template <typename Ty> class Matrix {

    static_assert(std::is_arithmetic<Ty>::value,
                  "Matrix only accept arithmetic (i.e. integer or floating "
                  "point) element types.");

  public:

  private:
    size_t numRows;    //< The number of rows in this matrix.
    size_t numColumns; //< The number of columns in this matrix.
    std::unique_ptr<Ty[]>
        data; //< The actual data in this matrix, in row-major order.

};
```

This `Matrix` declaration deserves some comments:
- it makes use of `template`, a C++ language feature which allows to support all
element types with a single and simple code base
- it checks at compile time with the `static_assert` that the `Matrix` class was
instantiated with an arithmetic data type, so that compilation can fail early
with a simple and descriptive error message
- the query about `Ty` being an arithmetic type is achieved thru the use of the
`std::is_arithmetic` type traits. Modern C++ provides many standard type traits
to analyze types
- The `Matrix` data is declared as a `std::unique_ptr<Ty[]>`. This means each
`Matrix` instance owns its memory array, and that it is in charge of freeing it
whenever a matrix is destructed.

At this stage, the project should still build and compile, try it to confirm:

```BASH
cd build
ninja
```

## Construct matrices

You have added a bare `Matrix` class which is not very useful because
there is no way to create a `Matrix` just yet.

First, add a private helper function `allocate`  that the Matrix
constructors will use. Add the following in the private section of the `Matrix`
class (in `include/Matrix/Matrix.h`):

```CPP
    /// Allocate (if need be) numElements to the Matrix. Die if the allocation
    /// went wrong.
    void allocate(size_t numElements) {
        if (numElements != 0) {
            data = std::make_unique<Ty[]>(numElements);
            if (!data)
                die(__FILE__, __LINE__, "Matrix allocation failure");
        }
    }
```

You will use the method to allocate memory for the element array. `new` will
get enough memory to store `numElements` of type `Ty`. This is stored in the
`data` `unique_ptr` with the `reset` function which enforces freeing memory
previously referred to by `data`. 

If allocation fails, which is signaled with a
`nullptr` (a zero pointer), `data` will not be valid and the program should be 
terminated. This helper method is made private because it is only
intended to be used by other methods from the `Matrix` class.  Users of the
`Matrix` objects have no reason for directly invoking this method.

With this in place, you can add some constructors in the public section of
the `Matrix` class. 

The very first `Matrix` you should be able to construct is
an invalid `Matrix`. While this might sound strange, this is actually very
useful in practice, to signal some errors. In this case, an invalid
`Matrix` is a matrix with 0 rows and 0 columns. You can use the default
constructor (a constructor with no parameters) for this. 

Add the following code
in the public section of class `Matrix` in `include/Matrix/Matrix.h`:

```CPP
    /// Default construct an invalid Matrix.
    constexpr Matrix() : numRows(0), numColumns(0), data(nullptr) {}
```

This constructor has been marked as `constexpr` which instructs the compiler
that it can optimize this case at compile time because we are essentially
constructing a matrix that has no run time dependency. It has zero rows, zero
columns, and no memory allocated to it. This is known at compile time and can be
propagated for optimizations.

You can now add a boolean conversion, using the conversion operator, that will
allow to check whether a `Matrix` instance is valid or not. It will return
`false` if the `Matrix` object is invalid, `true` otherwise. 

Add the following
method in the public section of `Matrix`:

```CPP
    /// Returns true if this matrix is valid.
    operator bool() const {
        return numRows != 0 && numColumns != 0;
    }
```

With those 2 methods in place, it's now high time to add some tests.

Create file `tests/Matrix.cpp` and add the following code to it:

```CPP
#include "Matrix/Matrix.h"

#include "gtest/gtest.h"

#include <cstdint>

using MatComp::Matrix;

TEST(Matrix, defaultConstruct) {
    Matrix<int8_t> m0;
    EXPECT_FALSE(m0);

    Matrix<float> m1;
    EXPECT_FALSE(m1);
}
```

Next, add `tests/Matrix.cpp` to the list of files used for the `Matrix` unit
testing in the top-level `CMakeLists.txt` (by adding file to the list of source
files used by `matrix-test` target):

```TXT
add_executable(matrix-test tests/main.cpp
  tests/Matrix.cpp
  tests/Version.cpp)
```

The `defaultConstruct` test does not do much, it construct two matrices, one with
8-bit signed integers, the other one with floating point numbers with the
default constructor. In both cases, these matrices are expected to be invalid.

You should now check if tests pass:

```BASH { output_lines = "4-16" }
cd build
ninja
ninja check
...
[==========] Running 2 tests from 1 test suites.
[----------] Global test environment set-up.
[----------] 2 tests from Matrix
[ RUN      ] Matrix.defaultConstruct
[       OK ] Matrix.defaultConstruct (0 ms)
[ RUN      ] Matrix.getVersion
[       OK ] Matrix.getVersion (0 ms)
[----------] 2 tests from Matrix (0 ms total)

[----------] Global test environment tear-down
[==========] 2 tests from 1 test suites ran. (0 ms total)
[  PASSED  ] 2 tests.
```

Constructing an invalid `Matrix` is very useful, but does not
really make the `Matrix` class very helpful. 

You can add some getters,
methods that allow you to query some information about a `Matrix` object:
- `getNumRows`: get the number of rows this matrix has
- `getNumColumns`: get the number of rows this matrix has
- `getNumElements`: get the number of elements this matrix has (i.e. rows x
  columns elements)
- `getSizeInBytes`: get size (in bytes) used by this matrix (i.e rows x columns
  x sizeof(element))

Add those methods in the public section of `Matrix` in
`include/Matrix/Matrix.h`:

```CPP
    /// Get the number of rows in this matrix.
    size_t getNumRows() const { return numRows; }
    /// Get the number of columns in this matrix.
    size_t getNumColumns() const { return numColumns; }
    /// Get the number of elements in this matrix.
    size_t getNumElements() const { return numRows * numColumns; }
    /// Get the storage size in bytes of the Matrix array.
    size_t getSizeInBytes() const { return numRows * numColumns * sizeof(Ty); }
```

Next, modify the `defaultConstruct` test that you previously added so that it now
looks like:

```CPP
TEST(Matrix, defaultConstruct) {
    Matrix<int8_t> m0;
    EXPECT_FALSE(m0);
    EXPECT_EQ(m0.getNumRows(), 0);
    EXPECT_EQ(m0.getNumColumns(), 0);
    EXPECT_EQ(m0.getNumElements(), 0);
    EXPECT_EQ(m0.getSizeInBytes(), 0);

    Matrix<float> m1;
    EXPECT_FALSE(m1);
    EXPECT_EQ(m1.getNumRows(), 0);
    EXPECT_EQ(m1.getNumColumns(), 0);
    EXPECT_EQ(m1.getNumElements(), 0);
    EXPECT_EQ(m1.getSizeInBytes(), 0);
}
```

The tests should still pass, check for yourself.

The next step is to be able to construct valid matrices, so add this
constructor to the public section of class `Matrix` in
`include/Matrix/Matrix.h`:

```CPP
    /// Construct a \p numRows x \p numColumns uninitialized Matrix
    Matrix(size_t numRows, size_t numColumns)
        : numRows(numRows), numColumns(numColumns), data() {
        allocate(getNumElements());
    }
```

Next, add this test to `tests/Matrix.cpp`:

```CPP
TEST(Matrix, uninitializedConstruct) {
    Matrix<int16_t> m0(2, 3);
    EXPECT_TRUE(m0);
    EXPECT_EQ(m0.getNumRows(), 2);
    EXPECT_EQ(m0.getNumColumns(), 3);
    EXPECT_EQ(m0.getNumElements(), 6);
    EXPECT_EQ(m0.getSizeInBytes(), 6 * sizeof(int16_t));

    Matrix<double> m1(3, 4);
    EXPECT_TRUE(m1);
    EXPECT_EQ(m1.getNumRows(), 3);
    EXPECT_EQ(m1.getNumColumns(), 4);
    EXPECT_EQ(m1.getNumElements(), 12);
    EXPECT_EQ(m1.getSizeInBytes(), 12 * sizeof(double));
}
```

This constructs a valid `Matrix` (if it contains elements), and the
`uninitializedConstruct` test checks that 2 valid matrices of different types
and dimensions can be constructed.

Compile and test again, all should pass:

```BASH { output_lines = "4-18" }
cd build
ninja
ninja check
...
[==========] Running 3 tests from 1 test suites.
[----------] Global test environment set-up.
[----------] 3 tests from Matrix
[ RUN      ] Matrix.defaultConstruct
[       OK ] Matrix.defaultConstruct (0 ms)
[ RUN      ] Matrix.uninitializedConstruct
[       OK ] Matrix.uninitializedConstruct (0 ms)
[ RUN      ] Matrix.getVersion
[       OK ] Matrix.getVersion (0 ms)
[----------] 3 tests from Matrix (0 ms total)

[----------] Global test environment tear-down
[==========] 3 tests from 1 test suites ran. (0 ms total)
[  PASSED  ] 3 tests.
```

The `Matrix` class is missing 2 important methods:
- a *getter*, to read the matrix element at (row, col)
- a *setter*, to modify the matrix element at (row, col)

Add them now in the public section of `Matrix` in `include/Matrix/Matrix.h`:

```CPP
    /// Access Matrix element at (\p row, \p col) by reference.
    Ty &get(size_t row, size_t col) {
        assert(*this && "Invalid Matrix");
        assert(row < numRows && "Out of bounds row access");
        assert(col < numColumns && "Out of bounds column access");
        return data[row * numColumns + col];
    }
    /// Access Matrix element at (\p row, \p col) by reference (const version).
    const Ty &get(size_t row, size_t col) const {
        assert(*this && "Invalid Matrix");
        assert(row < numRows && "Out of bounds row access");
        assert(col < numColumns && "Out of bounds column access");
        return data[row * numColumns + col];
    }
```

Another constructor that is missing is one that will create and initialize
matrices to a known value. Let's add it to `Matrix` in
`include/Matrix/Matrix.h`:

```CPP
    /// Construct a \p numRows x \p numColumns Matrix with all elements
    /// initialized to value \p val.
    Matrix(size_t numRows, size_t numCols, Ty val) : Matrix(numRows, numCols) {
        allocate(getNumElements());
        for (size_t i = 0; i < getNumElements(); i++)
            data[i] = val;
    }
```

You should be getting the pattern now. 

Add tests for those 3 methods in `tests/Matrix.cpp`:

```CPP
TEST(Matrix, fillConstruct) {
    Matrix<uint32_t> m0(2, 2, 13);
    EXPECT_TRUE(m0);
    EXPECT_EQ(m0.getNumRows(), 2);
    EXPECT_EQ(m0.getNumColumns(), 2);
    EXPECT_EQ(m0.getNumElements(), 4);
    EXPECT_EQ(m0.getSizeInBytes(), 4 * sizeof(uint32_t));
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            EXPECT_EQ(m0.get(row, col), uint32_t(13));

    Matrix<double> m1(2, 2, 16.0);
    EXPECT_TRUE(m1);
    EXPECT_EQ(m1.getNumRows(), 2);
    EXPECT_EQ(m1.getNumColumns(), 2);
    EXPECT_EQ(m1.getNumElements(), 4);
    EXPECT_EQ(m1.getSizeInBytes(), 4 * sizeof(double));
    for (size_t row = 0; row < m1.getNumRows(); row++)
        for (size_t col = 0; col < m1.getNumColumns(); col++)
            EXPECT_EQ(m1.get(row, col), double(16.0));
}

TEST(Matrix, getElement) {
    Matrix<uint32_t> m0(2, 3, 3);
    EXPECT_TRUE(m0);
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            EXPECT_EQ(m0.get(row, col), 3);
}

TEST(Matrix, setElement) {
    Matrix<uint32_t> m0(2, 3, 3);
    EXPECT_TRUE(m0);
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            EXPECT_EQ(m0.get(row, col), 3);
    m0.get(1, 2) = 65;
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            if (row == 1 && col == 2)
                EXPECT_EQ(m0.get(row, col), 65);
            else
                EXPECT_EQ(m0.get(row, col), 3);
}
```

Those 3 tests and methods need to be added all together as they make use of each
others.

Compile and check again. It's important to ensure that the project works at each
step and did not regress any of the previous steps.

```BASH { output_lines = "4-24" }
cd build
ninja
ninja check
...
[==========] Running 6 tests from 1 test suites.
[----------] Global test environment set-up.
[----------] 6 tests from Matrix
[ RUN      ] Matrix.defaultConstruct
[       OK ] Matrix.defaultConstruct (0 ms)
[ RUN      ] Matrix.uninitializedConstruct
[       OK ] Matrix.uninitializedConstruct (0 ms)
[ RUN      ] Matrix.fillConstruct
[       OK ] Matrix.fillConstruct (0 ms)
[ RUN      ] Matrix.getElement
[       OK ] Matrix.getElement (0 ms)
[ RUN      ] Matrix.setElement
[       OK ] Matrix.setElement (0 ms)
[ RUN      ] Matrix.getVersion
[       OK ] Matrix.getVersion (0 ms)
[----------] 6 tests from Matrix (0 ms total)

[----------] Global test environment tear-down
[==========] 6 tests from 1 test suites ran. (0 ms total)
[  PASSED  ] 6 tests.
```

Congratulations, you are almost done with constructors!

The last needed constructor is one that will allow you to build matrices with
arbitrary values. 

Add the constructor below to the public part of `Matrix` in
`include/Matrix/Matrix.h`. 

The C++ `std::initializer_list`  enables users
to provide a list of literal values (in row major order) to use to initialize
the matrix with:

```CPP
    /// Construct a \p numRows x \p numColumns Matrix with elements
    /// initialized from the values from \p il in row-major order.
    Matrix(size_t numRows, size_t numCols, std::initializer_list<Ty> il)
        : Matrix(numRows, numCols) {
        if (il.size() != getNumElements())
            die(__FILE__, __LINE__,
                "the number of initializers does not match the Matrix number "
                "of elements");
        allocate(getNumElements());
        size_t i = 0;
        for (const auto &val : il)
            data[i++] = val;
    }
```

Again, you should add the corresponding test in `tests/Matrix.cpp`:

```CPP
 TEST(Matrix, initializerListConstruct) {
    Matrix<int64_t> m0(2, 3, {1, 2, 3, 4, 5, 6});
    EXPECT_TRUE(m0);
    EXPECT_EQ(m0.getNumRows(), 2);
    EXPECT_EQ(m0.getNumColumns(), 3);
    EXPECT_EQ(m0.getNumElements(), 6);
    EXPECT_EQ(m0.getSizeInBytes(), m0.getNumElements() * sizeof(int64_t));
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            EXPECT_EQ(m0.get(row, col),
                      int64_t(row * m0.getNumColumns() + col + 1));

    Matrix<float> m1(3, 2, {1., 2., 3., 4., 5., 6.});
    EXPECT_TRUE(m1);
    EXPECT_EQ(m1.getNumRows(), 3);
    EXPECT_EQ(m1.getNumColumns(), 2);
    EXPECT_EQ(m1.getNumElements(), 6);
    EXPECT_EQ(m1.getSizeInBytes(), m1.getNumElements() * sizeof(float));
    for (size_t row = 0; row < m1.getNumRows(); row++)
        for (size_t col = 0; col < m1.getNumColumns(); col++)
            EXPECT_FLOAT_EQ(m1.get(row, col),
                            double(row * m1.getNumColumns() + col + 1));
}
```

You can now construct a `Matrix` using arbitrary values with the above constructor,
but `Matrix` users will want to assign an existing object with new content
(without affecting its shape). This is done with the C++ copy-assignment
operator that you will add now in the public part of `Matrix` in
`include/Matrix/Matrix.h`:

```CPP
    /// Assign from the \p il initializer list.
    Matrix &operator=(std::initializer_list<Ty> il) {
        if (il.size() != getNumElements())
            die(__FILE__, __LINE__, "number of elements do not match");

        size_t i = 0;
        for (const auto &val : il)
            data[i++] = val;

        return *this;
    }
```

Add a test in `tests/Matrix.cpp`:

```CPP
TEST(Matrix, initializerListAssign) {
    Matrix<uint64_t> m0(2, 3);
    m0 = {1, 2, 3, 4, 5, 6};
    EXPECT_TRUE(m0);
    EXPECT_EQ(m0.getNumRows(), 2);
    EXPECT_EQ(m0.getNumColumns(), 3);
    EXPECT_EQ(m0.getNumElements(), 6);
    EXPECT_EQ(m0.getSizeInBytes(), m0.getNumElements() * sizeof(uint64_t));
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            EXPECT_EQ(m0.get(row, col),
                      uint64_t(row * m0.getNumColumns() + col + 1));

    Matrix<double> m1(3, 2);
    m1 = {1., 2., 3., 4., 5., 6.};
    EXPECT_TRUE(m1);
    EXPECT_EQ(m1.getNumRows(), 3);
    EXPECT_EQ(m1.getNumColumns(), 2);
    EXPECT_EQ(m1.getNumElements(), 6);
    EXPECT_EQ(m1.getSizeInBytes(), m1.getNumElements() * sizeof(double));
    for (size_t row = 0; row < m1.getNumRows(); row++)
        for (size_t col = 0; col < m1.getNumColumns(); col++)
            EXPECT_DOUBLE_EQ(m1.get(row, col),
                             double(row * m1.getNumColumns() + col + 1));
}
```

Make sure that the project builds and the tests pass. 

## Constructors with memory management

So far, the `Matrix` constructors have dealt with `Matrix` objects in isolation.

But in real life, matrices are not isolated. Users will want to copy them
or to assign to them for example, which raises the important question of memory
management.

Modern C++ allows you to easily express and control the `copy` and the `move`
semantics. In the `copy` semantic, the content of an object is copied to
another object, and both object instances do not share memory. But in
some cases, it is important (for performance) to avoid unnecessary
memory allocation and data copying, and this can be expressed with
the `move` semantic, where a destination object steals the content
from the source object, making the source object invalid.

One important time in an object life is to use the `copy` or the `move` semantic
is at construction time, when an object is built from another object. 

Add a copy constructor and a move constructor in the public part of `Matrix` in
`include/Matrix/Matrix.h`:

```CPP
    /// Copy-construct from the \p other Matrix.
    Matrix(const Matrix &other)
        : numRows(other.numRows), numColumns(other.numColumns), data() {
        allocate(getNumElements());
        std::memcpy(data.get(), other.data.get(), getSizeInBytes());
    }

    /// Move-construct from the \p other Matrix.
    Matrix(Matrix &&other)
        : numRows(other.numRows), numColumns(other.numColumns),
          data(std::move(other.data)) {

        // Invalidate other.
        other.numRows = 0;
        other.numColumns = 0;
    }
```

You can test by adding the following lines to `tests/Matrix.cpp`:

```CPP
TEST(Matrix, copyConstruct) {
    const Matrix<int8_t> m0(3, 3, {1, 2, 3, 4, 5, 6, 7, 8, 9});
    Matrix<int8_t> m1(m0);
    EXPECT_EQ(m0.getNumRows(), m1.getNumRows());
    EXPECT_EQ(m0.getNumColumns(), m1.getNumColumns());
    EXPECT_EQ(m0.getNumElements(), m1.getNumElements());
    EXPECT_EQ(m0.getSizeInBytes(), m1.getSizeInBytes());
    for (size_t row = 0; row < m1.getNumRows(); row++)
        for (size_t col = 0; col < m1.getNumColumns(); col++) {
            EXPECT_EQ(m0.get(row, col), m1.get(row, col));
            EXPECT_NE(&m0.get(row, col), &m1.get(row, col));
        }
}

TEST(Matrix, moveConstruct) {
    Matrix<int16_t> m0(3, 2, {1, 2, 3, 4, 5, 6});
    EXPECT_TRUE(m0);
    Matrix<int16_t> m1(std::move(m0));
    EXPECT_FALSE(m0);
    EXPECT_TRUE(m1);
    EXPECT_EQ(m1.getNumRows(), 3);
    EXPECT_EQ(m1.getNumColumns(), 2);
    EXPECT_EQ(m1.getNumElements(), 6);
    EXPECT_EQ(m1.getSizeInBytes(), m1.getNumElements() * sizeof(int16_t));
    for (size_t row = 0; row < m1.getNumRows(); row++)
        for (size_t col = 0; col < m1.getNumColumns(); col++)
            EXPECT_EQ(m1.get(row, col),
                      int16_t(row * m1.getNumColumns() + col + 1));
}
```

The other important time is when an object is assigned to, with the copy
assignment and the move assignment operators that you will add now in the public
part of `Matrix` in `include/Matrix/Matrix.h` :

```CPP
    /// Copy-assign from the \p rhs Matrix.
    Matrix &operator=(const Matrix &rhs) {
        reallocate(rhs.getNumElements());
        if (getNumElements() != 0)
            std::memcpy(data.get(), rhs.data.get(), rhs.getSizeInBytes());
        return *this;
    }

    /// Move-assign from the \p rhs Matrix.
    Matrix &operator=(Matrix &&rhs) {
        numRows = rhs.numRows;
        numColumns = rhs.numColums;
        data = std::move(rhs.data);
        return *this;
    }
```

The copy assignment is making use of the `reallocate` helper routine, which you
should add in the private section of class `Matrix` in
`include/Matrix/Matrix.h`:

```CPP
    /// Reallocate (if need be) numElements to the Matrix. Die if the allocation
    /// went wrong. This method assumes \p numRows and \p numColumns have
    /// their 'old' values, that will get updated as part of the re-allocation.
    void reallocate(size_t newNumRows, size_t newNumColumns) {
        const size_t newNumElements = newNumRows * newNumColumns;
        if (getNumElements() != newNumElements) {
            if (newNumElements != 0) {
                data = std::make_unique<Ty[]>(newNumElements);
                if (!data)
                    die(__FILE__, __LINE__, "Matrix re-allocation failure");
            } else
                data.reset(nullptr);
        }
        numRows = newNumRows;
        numColumns = newNumColumns;
    }
```

Re-allocation might be necessary in the case of copy-assignment because the
destination object might have been constructed with a different number of
elements.

With all this in place, you can add the corresponding tests to
`tests/Matrix.cpp`:

```CPP
TEST(Matrix, copyAssign) {
    const Matrix<int32_t> m0(3, 3, {1, 2, 3, 4, 5, 6, 7, 8, 9});
    Matrix<int32_t> m1 = m0;
    EXPECT_EQ(m0.getNumRows(), m1.getNumRows());
    EXPECT_EQ(m0.getNumColumns(), m1.getNumColumns());
    EXPECT_EQ(m0.getNumElements(), m1.getNumElements());
    EXPECT_EQ(m0.getSizeInBytes(), m1.getSizeInBytes());
    for (size_t row = 0; row < m1.getNumRows(); row++)
        for (size_t col = 0; col < m1.getNumColumns(); col++) {
            EXPECT_EQ(m0.get(row, col), m1.get(row, col));
            EXPECT_NE(&m0.get(row, col), &m1.get(row, col));
        }
}

TEST(Matrix, moveAssign) {
    Matrix<int16_t> m0(3, 2, {1, 2, 3, 4, 5, 6});
    EXPECT_TRUE(m0);
    Matrix<int16_t> m1 = std::move(m0);
    EXPECT_FALSE(m0);
    EXPECT_TRUE(m1);
    EXPECT_EQ(m1.getNumRows(), 3);
    EXPECT_EQ(m1.getNumColumns(), 2);
    EXPECT_EQ(m1.getNumElements(), 6);
    EXPECT_EQ(m1.getSizeInBytes(), m1.getNumElements() * sizeof(int16_t));
    for (size_t row = 0; row < m1.getNumRows(); row++)
        for (size_t col = 0; col < m1.getNumColumns(); col++)
            EXPECT_EQ(m1.get(row, col),
                      int16_t(row * m1.getNumColumns() + col + 1));
}
```

It's now time to build and check the code base: all tests should pass.

## Convenience constructors

For convenience, users should be provided with some useful methods
to get specific types of matrices:
- `zeros` to get a zero initialized `Matrix`
- `ones` to get a `Matrix` initialized with 1
- `identity` to get the identity `Matrix` (a square matrix, with 1 on the
diagonal and 0 elsewhere)

Users with Python with `numpy` experience are used to those shortcuts, and they
make the user code much more readable, this is often referred to as syntactic
sugar, so let's add these to `Matrix`'s public section in
`include/Matrix/Matrix.h`:

```CPP
    /// Get a zero initialized Matrix.
    static Matrix zeros(size_t numRows, size_t numColumns) {
        return Matrix(numRows, numColumns, Ty(0));
    }

    /// Get a one initialized Matrix.
    static Matrix ones(size_t numRows, size_t numColumns) {
        return Matrix(numRows, numColumns, Ty(1));
    }

    /// Get the identity Matrix.
    static Matrix identity(size_t dimension) {
        Matrix id = zeros(dimension, dimension);
        for (size_t i = 0; i < dimension; i++)
            id.get(i, i) = Ty(1);
        return id;
    }
```

 They have been marked as `static`, which means these methods are not instance
 specific, they are class methods.

 Of course, you should have tests for these methods in `tests/Matrix.cpp`:

 ```CPP
 TEST(Matrix, zeros) {
    Matrix<int16_t> z0 = Matrix<int16_t>::zeros(2, 6);
    EXPECT_TRUE(z0);
    EXPECT_EQ(z0.getNumRows(), 2);
    EXPECT_EQ(z0.getNumColumns(), 6);
    EXPECT_EQ(z0.getNumElements(), 12);
    EXPECT_EQ(z0.getSizeInBytes(), 12 * sizeof(int16_t));
    for (size_t row = 0; row < z0.getNumRows(); row++)
        for (size_t col = 0; col < z0.getNumColumns(); col++)
            EXPECT_EQ(z0.get(row, col), int16_t(0));
}

TEST(Matrix, ones) {
    Matrix<uint8_t> o0 = Matrix<uint8_t>::ones(4, 3);
    EXPECT_TRUE(o0);
    EXPECT_EQ(o0.getNumRows(), 4);
    EXPECT_EQ(o0.getNumColumns(), 3);
    EXPECT_EQ(o0.getNumElements(), 12);
    EXPECT_EQ(o0.getSizeInBytes(), 12 * sizeof(uint8_t));
    for (size_t row = 0; row < o0.getNumRows(); row++)
        for (size_t col = 0; col < o0.getNumColumns(); col++)
            EXPECT_EQ(o0.get(row, col), uint8_t(1));
}

TEST(Matrix, identity) {
    Matrix<uint8_t> i0 = Matrix<uint8_t>::identity(5);
    EXPECT_TRUE(i0);
    EXPECT_EQ(i0.getNumRows(), 5);
    EXPECT_EQ(i0.getNumColumns(), 5);
    EXPECT_EQ(i0.getNumElements(), 25);
    EXPECT_EQ(i0.getSizeInBytes(), 25 * sizeof(uint8_t));
    for (size_t row = 0; row < i0.getNumRows(); row++)
        for (size_t col = 0; col < i0.getNumColumns(); col++)
            if (row == col)
                EXPECT_EQ(i0.get(row, col), uint8_t(1));
            else
                EXPECT_EQ(i0.get(row, col), uint8_t(0));
}
 ```

Compile and check again, all test should pass:

```BASH { output_lines = "4-41" }
cd build
ninja
ninja check
[==========] Running 15 tests from 1 test suites.
[----------] Global test environment set-up.
[----------] 15 tests from Matrix
[ RUN      ] Matrix.defaultConstruct
[       OK ] Matrix.defaultConstruct (0 ms)
[ RUN      ] Matrix.uninitializedConstruct
[       OK ] Matrix.uninitializedConstruct (0 ms)
[ RUN      ] Matrix.fillConstruct
[       OK ] Matrix.fillConstruct (0 ms)
[ RUN      ] Matrix.getElement
[       OK ] Matrix.getElement (0 ms)
[ RUN      ] Matrix.setElement
[       OK ] Matrix.setElement (0 ms)
[ RUN      ] Matrix.initializerListConstruct
[       OK ] Matrix.initializerListConstruct (0 ms)
[ RUN      ] Matrix.copyConstruct
[       OK ] Matrix.copyConstruct (0 ms)
[ RUN      ] Matrix.moveConstruct
[       OK ] Matrix.moveConstruct (0 ms)
[ RUN      ] Matrix.copyAssign
[       OK ] Matrix.copyAssign (0 ms)
[ RUN      ] Matrix.moveAssign
[       OK ] Matrix.moveAssign (0 ms)
[ RUN      ] Matrix.initializerListAssign
[       OK ] Matrix.initializerListAssign (0 ms)
[ RUN      ] Matrix.zeros
[       OK ] Matrix.zeros (0 ms)
[ RUN      ] Matrix.ones
[       OK ] Matrix.ones (0 ms)
[ RUN      ] Matrix.identity
[       OK ] Matrix.identity (0 ms)
[ RUN      ] Matrix.getVersion
[       OK ] Matrix.getVersion (0 ms)
[----------] 15 tests from Matrix (0 ms total)

[----------] Global test environment tear-down
[==========] 15 tests from 3 test suites ran. (0 ms total)
[  PASSED  ] 15 tests.
```

## Display matrices

At some point, one will want to *see* the content of a `Matrix`, so add
a simple output operator to dump the matrix content to a stream. 

Add this code
at the very end of `include/Matrix/Matrix.h`, outside of the `MatComp` namespace.

```CPP
/// Dump this Matrix in textual format to output stream \p os.
template <typename Ty>
std::ostream &operator<<(std::ostream &os, const MatComp::Matrix<Ty> &m) {
    for (size_t row = 0; row < m.getNumRows(); row++) {
        for (size_t col = 0; col < m.getNumColumns(); col++)
            os << '\t' << m.get(row, col) << ',';
        os << '\n';
    }
    return os;
}
```

This will print each row of the matrix to a different line, separating the
values with commas and tab spaces.

Of course, you also need to add a test for this output operator in `tests/Matrix.cpp`:

```CPP
TEST(Matrix, dump) {
    std::ostringstream osstr;

    // Test horizontal vector.
    osstr << Matrix<int16_t>(1, 3, {1, 2, 3});
    EXPECT_EQ(osstr.str(), "\t1,\t2,\t3,\n");

    osstr.str("");

    // Test vertical vector.
    osstr << Matrix<int32_t>(3, 1, {1, 2, 3});
    EXPECT_EQ(osstr.str(), "\t1,\n\t2,\n\t3,\n");

    osstr.str("");

    // Test matrix.
    osstr << Matrix<int64_t>::identity(2);
    EXPECT_EQ(osstr.str(), "\t1,\t0,\n\t0,\t1,\n");
}
```

This test makes uses of string streams, which enable you to capture and check the
output without actually writing to the standard output. You'll need to add an include file at the top of `tests/Matrix.cpp` for the above test to compile:

```CPP
#include <sstream>
```

## Compare matrices

The last mundane operations you need are `Matrix` equality and inequality operators.

Add these to the public section of `Matrix` in `include/Matrix/Matrix.h`:

```CPP
    /// Returns true iff both matrices compare equal.
    bool operator==(const Matrix &rhs) const {
        // Invalid matrices compare equal.
        if (!*this && !rhs)
            return true;
        // If one is invalid, they can never compare equal.
        if (*this ^ rhs)
            return false;
        // Matrices with different dimensions are not equal.
        if (numRows != rhs.numRows || numColumns != rhs.numColumns)
            return false;
        // Every thing else is equal and sound, compare the elements !
        for (size_t i = 0; i < getNumElements(); i++)
            if (data[i] != rhs.data[i])
                return false;
        return true;
    }
    /// Returns tur iff matrices do not compare equal.
    bool operator!=(const Matrix &rhs) const { return !(*this == rhs); }
```

Add tests for these two operators in `tests/Matrix.cpp`:

```CPP
TEST(Matrix, equal) {
    EXPECT_TRUE(Matrix<int16_t>() == Matrix<int16_t>());

    EXPECT_FALSE(Matrix<int16_t>(2, 3) == Matrix<int16_t>());
    EXPECT_FALSE(Matrix<int16_t>(3, 2, 2) == Matrix<int16_t>());
    EXPECT_FALSE(Matrix<int16_t>() == Matrix<int16_t>(2, 3));
    EXPECT_FALSE(Matrix<int16_t>() == Matrix<int16_t>(2, 3, 2));

    EXPECT_FALSE(Matrix<uint8_t>(3, 2) == Matrix<uint8_t>(1, 4));
    EXPECT_FALSE(Matrix<uint8_t>(3, 2) == Matrix<uint8_t>(3, 4));
    EXPECT_FALSE(Matrix<uint8_t>(3, 2) == Matrix<uint8_t>(1, 2));
    EXPECT_FALSE(Matrix<uint8_t>(3, 2, 1) == Matrix<uint8_t>(3, 2, 2));
    EXPECT_TRUE(Matrix<uint8_t>(3, 2, 1) == Matrix<uint8_t>(3, 2, 1));
}

TEST(Matrix, notEqual) {
    EXPECT_FALSE(Matrix<int32_t>() != Matrix<int32_t>());

    EXPECT_TRUE(Matrix<int32_t>(2, 3) != Matrix<int32_t>());
    EXPECT_TRUE(Matrix<int32_t>(3, 2, 2) != Matrix<int32_t>());
    EXPECT_TRUE(Matrix<int32_t>() != Matrix<int32_t>(2, 3));
    EXPECT_TRUE(Matrix<int32_t>() != Matrix<int32_t>(2, 3, 2));

    EXPECT_TRUE(Matrix<uint64_t>(3, 2) != Matrix<uint64_t>(1, 4));
    EXPECT_TRUE(Matrix<uint64_t>(3, 2) != Matrix<uint64_t>(3, 4));
    EXPECT_TRUE(Matrix<uint64_t>(3, 2) != Matrix<uint64_t>(1, 2));
    EXPECT_TRUE(Matrix<uint64_t>(3, 2, 1) != Matrix<uint64_t>(3, 2, 2));
    EXPECT_FALSE(Matrix<uint64_t>(3, 2, 1) != Matrix<uint64_t>(3, 2, 1));
}
```

Check again if the tests build and pass: 

```BASH { output_lines = "4-47" }
cd build
ninja
ninja check
[==========] Running 18 tests from 1 test suites.
[----------] Global test environment set-up.
[----------] 18 tests from Matrix
[ RUN      ] Matrix.defaultConstruct
[       OK ] Matrix.defaultConstruct (0 ms)
[ RUN      ] Matrix.uninitializedConstruct
[       OK ] Matrix.uninitializedConstruct (0 ms)
[ RUN      ] Matrix.fillConstruct
[       OK ] Matrix.fillConstruct (0 ms)
[ RUN      ] Matrix.getElement
[       OK ] Matrix.getElement (0 ms)
[ RUN      ] Matrix.setElement
[       OK ] Matrix.setElement (0 ms)
[ RUN      ] Matrix.initializerListConstruct
[       OK ] Matrix.initializerListConstruct (0 ms)
[ RUN      ] Matrix.copyConstruct
[       OK ] Matrix.copyConstruct (0 ms)
[ RUN      ] Matrix.moveConstruct
[       OK ] Matrix.moveConstruct (0 ms)
[ RUN      ] Matrix.copyAssign
[       OK ] Matrix.copyAssign (0 ms)
[ RUN      ] Matrix.moveAssign
[       OK ] Matrix.moveAssign (0 ms)
[ RUN      ] Matrix.initializerListAssign
[       OK ] Matrix.initializerListAssign (0 ms)
[ RUN      ] Matrix.zeros
[       OK ] Matrix.zeros (0 ms)
[ RUN      ] Matrix.ones
[       OK ] Matrix.ones (0 ms)
[ RUN      ] Matrix.identity
[       OK ] Matrix.identity (0 ms)
[ RUN      ] Matrix.equal
[       OK ] Matrix.equal (0 ms)
[ RUN      ] Matrix.notEqual
[       OK ] Matrix.notEqual (0 ms)
[ RUN      ] Matrix.dump
[       OK ] Matrix.dump (0 ms)
[ RUN      ] Matrix.getVersion
[       OK ] Matrix.getVersion (0 ms)
[----------] 18 tests from Matrix (0 ms total)

[----------] Global test environment tear-down
[==========] 18 tests from 1 test suites ran. (0 ms total)
[  PASSED  ] 18 tests.
```

Congratulations, you now have a working library!

## What have you achieved so far ?

At this stage, the code looks like this:

```TXT
Matrix/
├── CMakeLists.txt
├── build/
...
├── external/
│   └── CMakeLists.txt
├── include/
│   └── Matrix/
│       └── Matrix.h
├── lib/
│   └── Matrix/
│       └── Matrix.cpp
├── src/
│   ├── getVersion.cpp
│   └── howdy.cpp
└── tests/
    ├── Matrix.cpp
    ├── Version.cpp
    └── main.cpp
```

You can download the [archive](/artifacts/matrix/chapter-3.tar.xz) of the
project in its current state to experiment locally on your machine.

After this rather long exercise, you have a minimalistic, yet fully functional
core for the matrix processing library, with some level of regression testing.

Modern C++ enabled you to express move and copy
semantics, and to use smart pointers to make memory management easy. 

The compiler will also catch a large number of type or misuse errors. With this core
functionality in place, you have all you need to actually implement matrix
operations in the next section.
