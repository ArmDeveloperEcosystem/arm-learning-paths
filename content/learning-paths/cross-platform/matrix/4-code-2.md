---
title: Implement matrix operations
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In the previous section, you created the core (or the boiler plate)
needed for `Matrix` objects. They can now be constructed, assigned to/from,
and dumped to the screen, but the library is still missing actual matrix
operations: add, subtract, and multiply.

In this section, you will add the missing operations.

## Operations architecture

When designing matrix processing, it's desirable to separate 2 concerns:
- the traversal of the matrices 
- the actual data processing

This allows you to develop the independent parts and then compose them, allowing for
easy testing and extension of the library.

## Unary scalar operations

Unary operations are operations that take a single `Matrix` as argument.
The very first unary operations to consider when processing a `Matrix`
are:
- `Neg` to negate a value
- `Abs` to get the absolute value
- `Sqrt` to get the square root of a value
- `Log` to get the natural logarithm of a value

You will add these unary scalar operations, in the `MatComp` namespace, but in a
separate file.

Add the code below to a new file `include/Matrix/Operators.h`:

```CPP
#pragma once

#include <cmath>
#include <type_traits>

namespace MatComp {

struct unaryOperation {};

/// Negate \p v.
template <typename Ty> class Neg : public unaryOperation {
  public:
    constexpr Ty operator()(const Ty &v) const { return -v; }
};

/// Get the absolute value of \p v.
template <typename Ty> class Abs : public unaryOperation {
  public:
    template <typename T = Ty>
    constexpr std::enable_if_t<std::is_unsigned<T>::value, Ty>
    operator()(const Ty &v) const {
        return v;
    }
    template <typename T = Ty>
    constexpr std::enable_if_t<std::is_signed<T>::value, Ty>
    operator()(const Ty &v) const {
        return std::abs(v);
    }
};

/// Get the square root of \p v.
template <typename Ty> class Sqrt : public unaryOperation {
  public:
    constexpr Ty operator()(const Ty &v) const { return std::sqrt(v); }
};

/// Get the natural logarithm of \p v.
template <typename Ty> class Log : public unaryOperation {
  public:
    constexpr Ty operator()(const Ty &v) const { return std::log(v); }
};

} // namespace MatComp
```

All these unary operations derive from the empty `unaryOperation` `struct`,
which enable code bases to type / group those operations. This essentially
*tags* these operations. They are all implemented as templates, in order for
them to be type generic. Although none of them carries a state, they have been
implemented as classes with the function operator (`operator()`) defined. This
makes them suitable for using in bigger algorithms and is a common pattern used
for example in the C++ standard library.

One point worth mentioning is related to the `Abs` class: depending on the type used
at instantiation, the compiler will select an optimized implementation for
unsigned types, and there is no need to compute the absolute value of an always
positive value. This optimization is transparent to users.

Those operators are marked as `constexpr` so that the compiler can optimize the
computation by performing them at compile time rather than runtime if the actual
values are known at compile time. They are marked `const`, because the operator
will not modify the object state (as these objects don't have a state).

The new operations must have tests, so add those into
a separate `tests/Operators.cpp` file:

```CPP
#include "Matrix/Operators.h"

#include <limits>

#include "gtest/gtest.h"

using std::numeric_limits;

TEST(unaryOperator, Neg) {
    EXPECT_EQ(MatComp::Neg<uint8_t>()(1), uint8_t(-1));
    EXPECT_EQ(MatComp::Neg<uint8_t>()(-2), uint8_t(2));
    EXPECT_EQ(MatComp::Neg<uint16_t>()(1), uint16_t(-1));
    EXPECT_EQ(MatComp::Neg<uint16_t>()(-2), uint16_t(2));
    EXPECT_EQ(MatComp::Neg<uint32_t>()(1), uint32_t(-1));
    EXPECT_EQ(MatComp::Neg<uint32_t>()(-2), uint32_t(2));
    EXPECT_EQ(MatComp::Neg<uint64_t>()(1), uint64_t(-1));
    EXPECT_EQ(MatComp::Neg<uint64_t>()(-2), uint64_t(2));

    EXPECT_EQ(MatComp::Neg<int8_t>()(1), int8_t(-1));
    EXPECT_EQ(MatComp::Neg<int8_t>()(-2), int8_t(2));
    EXPECT_EQ(MatComp::Neg<int16_t>()(1), int16_t(-1));
    EXPECT_EQ(MatComp::Neg<int16_t>()(-2), int16_t(2));
    EXPECT_EQ(MatComp::Neg<int32_t>()(1), int32_t(-1));
    EXPECT_EQ(MatComp::Neg<int32_t>()(-2), int32_t(2));
    EXPECT_EQ(MatComp::Neg<int64_t>()(1), int64_t(-1));
    EXPECT_EQ(MatComp::Neg<int64_t>()(-2), int64_t(2));

    EXPECT_FLOAT_EQ(MatComp::Neg<float>()(1.0), float(-1.0));
    EXPECT_FLOAT_EQ(MatComp::Neg<float>()(-2.0), float(2.0));
    EXPECT_DOUBLE_EQ(MatComp::Neg<double>()(1.0), double(-1.0));
    EXPECT_DOUBLE_EQ(MatComp::Neg<double>()(-2.0), double(2.0));
}

TEST(unaryOperator, Abs) {
    EXPECT_EQ(MatComp::Abs<uint8_t>()(1), uint8_t(1));
    EXPECT_EQ(MatComp::Abs<uint8_t>()(-2),
              numeric_limits<uint8_t>::max() - 2 + 1);
    EXPECT_EQ(MatComp::Abs<uint16_t>()(1), uint16_t(1));
    EXPECT_EQ(MatComp::Abs<uint16_t>()(-2),
              numeric_limits<uint16_t>::max() - 2 + 1);
    EXPECT_EQ(MatComp::Abs<uint32_t>()(1), uint32_t(1));
    EXPECT_EQ(MatComp::Abs<uint32_t>()(-2),
              numeric_limits<uint32_t>::max() - 2 + 1);
    EXPECT_EQ(MatComp::Abs<uint64_t>()(1), uint64_t(1));
    EXPECT_EQ(MatComp::Abs<uint64_t>()(-2),
              numeric_limits<uint64_t>::max() - 2 + 1);

    EXPECT_EQ(MatComp::Abs<int8_t>()(1), int8_t(1));
    EXPECT_EQ(MatComp::Abs<int8_t>()(-2), int8_t(2));
    EXPECT_EQ(MatComp::Abs<int16_t>()(1), int16_t(1));
    EXPECT_EQ(MatComp::Abs<int16_t>()(-2), int16_t(2));
    EXPECT_EQ(MatComp::Abs<int32_t>()(1), int32_t(1));
    EXPECT_EQ(MatComp::Abs<int32_t>()(-2), int32_t(2));
    EXPECT_EQ(MatComp::Abs<int64_t>()(1), int64_t(1));
    EXPECT_EQ(MatComp::Abs<int64_t>()(-2), int64_t(2));

    EXPECT_FLOAT_EQ(MatComp::Abs<float>()(1.0), float(1.0));
    EXPECT_FLOAT_EQ(MatComp::Abs<float>()(-2.0), float(2.0));
    EXPECT_DOUBLE_EQ(MatComp::Abs<double>()(1.0), double(1.0));
    EXPECT_DOUBLE_EQ(MatComp::Abs<double>()(-2.0), double(2.0));
}

TEST(unaryOperator, Sqrt) {
    EXPECT_EQ(MatComp::Sqrt<uint8_t>()(4), uint8_t(2));
    EXPECT_EQ(MatComp::Sqrt<uint16_t>()(4), uint16_t(2));
    EXPECT_EQ(MatComp::Sqrt<uint32_t>()(4), uint32_t(2));
    EXPECT_EQ(MatComp::Sqrt<uint64_t>()(4), uint64_t(2));

    EXPECT_EQ(MatComp::Sqrt<int8_t>()(4), int8_t(2));
    EXPECT_EQ(MatComp::Sqrt<int16_t>()(4), int16_t(2));
    EXPECT_EQ(MatComp::Sqrt<int32_t>()(4), int32_t(2));
    EXPECT_EQ(MatComp::Sqrt<int64_t>()(4), int64_t(2));

    EXPECT_FLOAT_EQ(MatComp::Sqrt<float>()(4.0), float(2.0));
    EXPECT_DOUBLE_EQ(MatComp::Sqrt<double>()(4.0), double(2.0));
}

TEST(unaryOperator, Log) {
    EXPECT_EQ(MatComp::Log<uint8_t>()(64), uint8_t(4));
    EXPECT_EQ(MatComp::Log<uint16_t>()(64), uint16_t(4));
    EXPECT_EQ(MatComp::Log<uint32_t>()(64), uint32_t(4));
    EXPECT_EQ(MatComp::Log<uint64_t>()(64), uint64_t(4));

    EXPECT_EQ(MatComp::Log<int8_t>()(64), int8_t(4));
    EXPECT_EQ(MatComp::Log<int16_t>()(64), int16_t(4));
    EXPECT_EQ(MatComp::Log<int32_t>()(64), int32_t(4));
    EXPECT_EQ(MatComp::Log<int64_t>()(64), int64_t(4));

    EXPECT_FLOAT_EQ(MatComp::Log<float>()(64.0), std::log(float(64.0)));
    EXPECT_DOUBLE_EQ(MatComp::Log<double>()(64.0), std::log(double(64.0)));
}

```

The tests do not attempt to check all corner cases. Please note the use of
type traits (from `<numeric_limit>`) such as `max` to get the maximum value
representable for a given type.

```BASH { output_lines = "4-61" }
cd build
ninja
ninja check
...
[==========] Running 23 tests from 2 test suites.
[----------] Global test environment set-up.
[----------] 19 tests from Matrix
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
[ RUN      ] Matrix.booleanConversion
[       OK ] Matrix.booleanConversion (0 ms)
[ RUN      ] Matrix.equal
[       OK ] Matrix.equal (0 ms)
[ RUN      ] Matrix.notEqual
[       OK ] Matrix.notEqual (0 ms)
[ RUN      ] Matrix.dump
[       OK ] Matrix.dump (0 ms)
[ RUN      ] Matrix.getVersion
[       OK ] Matrix.getVersion (0 ms)
[----------] 19 tests from Matrix (0 ms total)

[----------] 4 tests from unaryOperator
[ RUN      ] unaryOperator.Neg
[       OK ] unaryOperator.Neg (0 ms)
[ RUN      ] unaryOperator.Abs
[       OK ] unaryOperator.Abs (0 ms)
[ RUN      ] unaryOperator.Sqrt
[       OK ] unaryOperator.Sqrt (0 ms)
[ RUN      ] unaryOperator.Log
[       OK ] unaryOperator.Log (0 ms)
[----------] 4 tests from unaryOperator (0 ms total)

[----------] Global test environment tear-down
[==========] 23 tests from 2 test suites ran. (0 ms total)
[  PASSED  ] 23 tests.
```

## Whole matrix operations: neg, abs, sqrt, log

With the unary scalar operations in place, you can now add some matrix
processing.

All the whole matrix operations have the same pattern of operation: each element
in the matrix needs to be transformed with the unary scalar operation, the order
in which the element are modified does not matter, so there is no need to apply
the scalar operations taking into account rows and columns. Giving the compiler
one simple big loop will give it the most optimization opportunities.

First, create a `applyEltWiseUnaryOp` helper routine in the public section of
 `Matrix` in `include/Matrix/Matrix.h` which is templated on the desired scalar
 operation as follows:

```CPP
    /// Apply element wise unary scalar operator \p uOp to each element.
    template <template <typename> class uOp>
    Matrix &applyEltWiseUnaryOp(const uOp<Ty> &op) {
        static_assert(std::is_base_of<unaryOperation, uOp<Ty>>::value,
                      "op must be a unaryOperation");
        for (size_t i = 0; i < getNumElements(); i++)
            data[i] = op(data[i]);
        return *this;
    }
```

Although `applyEltWiseUnaryOp` does not need to be a public
member, it allows users to add their own operations should they lack one
specific to their usage. In other words, this provides easy extendability for
the library. `applyEltWiseUnaryOp` also checks at compile time, with the
`static_assert` statement, that the operation that it has to perform is a unary
operation.

You can eventually add, still in the `Matrix` public section in
`include/Matrix/Matrix.h`, the `neg`, `abs`, `sqrt` and `log` member operations:

```CPP
    /// Apply negate to each element of this Matrix.
    Matrix &neg() { return applyEltWiseUnaryOp(Neg<Ty>()); }

    /// Apply absolute value to each element of this Matrix.
    Matrix &abs() { return applyEltWiseUnaryOp(Abs<Ty>()); }

    /// Apply square root to each element of this Matrix.
    Matrix &sqrt() { return applyEltWiseUnaryOp(Sqrt<Ty>()); }

    /// Apply natural logarithm to each element of this Matrix.
    Matrix &log() { return applyEltWiseUnaryOp(Log<Ty>()); }
```

Those member operations are modifying the object in place, which might not be
desirable, so you can also provide a functional version of these
operators, that is to say a version that will modify a copy of the object
instead. This is achieved by providing functions outside of the `Matrix` class
(but still in the `MatComp` namespace). Add these after the `Matrix` class
closing `};` in `include/Matrix/Matrix.h`:

```CPP
/// Functional version of neg.
template <typename Ty> Matrix<Ty> neg(const Matrix<Ty> &m) {
    return Matrix(m).neg();
}

/// Functional version of abs.
template <typename Ty> Matrix<Ty> abs(const Matrix<Ty> &m) {
    return Matrix(m).abs();
}

/// Functional version of neg.
template <typename Ty> Matrix<Ty> sqrt(const Matrix<Ty> &m) {
    return Matrix(m).sqrt();
}

/// Functional version of abs.
template <typename Ty> Matrix<Ty> log(const Matrix<Ty> &m) {
    return Matrix(m).log();
}
```

Users can now write either:
 - `m.abs()` which will modify matrix `m` *in-place* so that it contains the
 absolute value of each of its elements
 - `abs(m)` which will return a copy of `m` with the absolute value of each of
 `m` elements, leaving `m` untouched.

Of course, each of these function needs to have tests. 

Add the following
tests in `tests/Matrix.cpp`:

```CPP
TEST(Matrix, neg) {
    Matrix<int16_t> m0(2, 2, {1, -2, -3, 4});
    Matrix<int16_t> m1 = neg(m0); // Functional version
    EXPECT_EQ(m0.getNumRows(), m1.getNumRows());
    EXPECT_EQ(m0.getNumColumns(), m1.getNumColumns());
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            EXPECT_EQ(m0.get(row, col), -m1.get(row, col));

    m0.neg(); // In-place version
    EXPECT_EQ(m0.getNumRows(), m1.getNumRows());
    EXPECT_EQ(m0.getNumColumns(), m1.getNumColumns());
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            EXPECT_EQ(m0.get(row, col), m1.get(row, col));
}

TEST(Matrix, abs) {
    Matrix<int64_t> m0(2, 2, {1, -2, -3, 4});
    Matrix<int64_t> m1 = abs(m0); // Functional version
    EXPECT_EQ(m0.getNumRows(), m1.getNumRows());
    EXPECT_EQ(m0.getNumColumns(), m1.getNumColumns());
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            EXPECT_EQ(m1.get(row, col), std::abs(m0.get(row, col)));

    m0.abs(); // In-place version
    EXPECT_EQ(m0.getNumRows(), m1.getNumRows());
    EXPECT_EQ(m0.getNumColumns(), m1.getNumColumns());
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            EXPECT_EQ(m1.get(row, col), m0.get(row, col));
}

TEST(Matrix, sqrt) {
    Matrix<double> m0(1, 4, {0, 4, 16, 64});
    Matrix<double> m1 = sqrt(m0); // Functional version
    EXPECT_EQ(m0.getNumRows(), m1.getNumRows());
    EXPECT_EQ(m0.getNumColumns(), m1.getNumColumns());
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            EXPECT_DOUBLE_EQ(m1.get(row, col), std::sqrt(m0.get(row, col)));

    m0.sqrt(); // In-place version
    EXPECT_EQ(m0.getNumRows(), m1.getNumRows());
    EXPECT_EQ(m0.getNumColumns(), m1.getNumColumns());
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            EXPECT_DOUBLE_EQ(m0.get(row, col), m1.get(row, col));
}

TEST(Matrix, log) {
    Matrix<float> m0(1, 3, {4, 16, 64});
    Matrix<float> m1 = log(m0); // Functional version
    EXPECT_EQ(m0.getNumRows(), m1.getNumRows());
    EXPECT_EQ(m0.getNumColumns(), m1.getNumColumns());
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            EXPECT_FLOAT_EQ(m1.get(row, col), std::log(m0.get(row, col)));

    m0.log(); // In-place version
    EXPECT_EQ(m0.getNumRows(), m1.getNumRows());
    EXPECT_EQ(m0.getNumColumns(), m1.getNumColumns());
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            EXPECT_FLOAT_EQ(m0.get(row, col), m1.get(row, col));
}
```

```BASH { output_lines = "4-69" }
cd build
ninja
ninja check
...
[==========] Running 27 tests from 2 test suites.
[----------] Global test environment set-up.
[----------] 23 tests from Matrix
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
[ RUN      ] Matrix.booleanConversion
[       OK ] Matrix.booleanConversion (0 ms)
[ RUN      ] Matrix.equal
[       OK ] Matrix.equal (0 ms)
[ RUN      ] Matrix.notEqual
[       OK ] Matrix.notEqual (0 ms)
[ RUN      ] Matrix.dump
[       OK ] Matrix.dump (0 ms)
[ RUN      ] Matrix.neg
[       OK ] Matrix.neg (0 ms)
[ RUN      ] Matrix.abs
[       OK ] Matrix.abs (0 ms)
[ RUN      ] Matrix.sqrt
[       OK ] Matrix.sqrt (0 ms)
[ RUN      ] Matrix.log
[       OK ] Matrix.log (0 ms)
[ RUN      ] Matrix.getVersion
[       OK ] Matrix.getVersion (0 ms)
[----------] 23 tests from Matrix (0 ms total)

[----------] 4 tests from unaryOperator
[ RUN      ] unaryOperator.Neg
[       OK ] unaryOperator.Neg (0 ms)
[ RUN      ] unaryOperator.Abs
[       OK ] unaryOperator.Abs (0 ms)
[ RUN      ] unaryOperator.Sqrt
[       OK ] unaryOperator.Sqrt (0 ms)
[ RUN      ] unaryOperator.Log
[       OK ] unaryOperator.Log (0 ms)
[----------] 4 tests from unaryOperator (0 ms total)

[----------] Global test environment tear-down
[==========] 27 tests from 3 test suites ran. (0 ms total)
[  PASSED  ] 27 tests.
```

## Binary scalar operations

Users also need to have binary operations, that is
operations that have 2 inputs: addition, subtraction, and multiplication are the
most popular representatives of binary operations. Using the same pattern than
for unary operations, add those binary operations to
`include/Matrix/Operators.h`:

```CPP
struct binaryOperation {};

/// Add \p lhs and \p rhs.
template <typename Ty> class Add : public binaryOperation {
  public:
    constexpr Ty operator()(const Ty &lhs, const Ty &rhs) const {
        return lhs + rhs;
    }
};

/// Substract \p rhs from \p lhs.
template <typename Ty> class Sub : public binaryOperation {
  public:
    constexpr Ty operator()(const Ty &lhs, const Ty &rhs) const {
        return lhs - rhs;
    }
};

/// Multiply \p lhs by \p rhs.
template <typename Ty> class Mul : public binaryOperation {
  public:
    constexpr Ty operator()(const Ty &lhs, const Ty &rhs) const {
        return lhs * rhs;
    }
};
```

Add the tests to `tests/Operators.cpp`:


```CPP
TEST(binaryOperator, Add) {
    EXPECT_EQ(MatComp::Add<uint8_t>()(1, 2), uint8_t(3));
    EXPECT_EQ(MatComp::Add<uint16_t>()(3, 4), uint16_t(7));
    EXPECT_EQ(MatComp::Add<uint32_t>()(5, 6), uint32_t(11));
    EXPECT_EQ(MatComp::Add<uint64_t>()(7, 8), uint64_t(15));

    EXPECT_EQ(MatComp::Add<int8_t>()(9, 10), int8_t(19));
    EXPECT_EQ(MatComp::Add<int16_t>()(11, 12), int16_t(23));
    EXPECT_EQ(MatComp::Add<int32_t>()(13, 14), int32_t(27));
    EXPECT_EQ(MatComp::Add<int64_t>()(15, 16), int64_t(31));

    EXPECT_FLOAT_EQ(MatComp::Add<float>()(8.0, 12.0), float(20.0));
    EXPECT_DOUBLE_EQ(MatComp::Add<double>()(32.0, 64.0), double(96.0));
}

TEST(binaryOperator, Sub) {
    EXPECT_EQ(MatComp::Sub<uint8_t>()(2, 1), uint8_t(1));
    EXPECT_EQ(MatComp::Sub<uint16_t>()(3, 1), uint16_t(2));
    EXPECT_EQ(MatComp::Sub<uint32_t>()(5, 2), uint32_t(3));
    EXPECT_EQ(MatComp::Sub<uint64_t>()(8, 3), uint64_t(5));

    EXPECT_EQ(MatComp::Sub<int8_t>()(9, 10), int8_t(-1));
    EXPECT_EQ(MatComp::Sub<int16_t>()(13, 11), int16_t(2));
    EXPECT_EQ(MatComp::Sub<int32_t>()(14, 14), int32_t(0));
    EXPECT_EQ(MatComp::Sub<int64_t>()(15, 16), int64_t(-1));

    EXPECT_FLOAT_EQ(MatComp::Sub<float>()(8.0, 12.0), float(-4.0));
    EXPECT_DOUBLE_EQ(MatComp::Sub<double>()(32.0, 64.0), double(-32.0));
}

TEST(binaryOperator, Mul) {
    EXPECT_EQ(MatComp::Mul<uint8_t>()(1, 2), uint8_t(2));
    EXPECT_EQ(MatComp::Mul<uint16_t>()(3, 4), uint16_t(12));
    EXPECT_EQ(MatComp::Mul<uint32_t>()(5, 6), uint32_t(30));
    EXPECT_EQ(MatComp::Mul<uint64_t>()(7, 8), uint64_t(56));

    EXPECT_EQ(MatComp::Mul<int8_t>()(9, 10), int8_t(90));
    EXPECT_EQ(MatComp::Mul<int16_t>()(11, 12), int16_t(11 * 12));
    EXPECT_EQ(MatComp::Mul<int32_t>()(13, 14), int32_t(13 * 14));
    EXPECT_EQ(MatComp::Mul<int64_t>()(15, 16), int64_t(15 * 16));

    EXPECT_FLOAT_EQ(MatComp::Mul<float>()(8.0, 12.0), float(96.0));
    EXPECT_DOUBLE_EQ(MatComp::Mul<double>()(32.0, 64.0), double(2048.0));
}

```

Check the code compiles and passes the checks:

```BASH { output_lines = "4-78" }
cd build
ninja
ninja check
...
[==========] Running 30 tests from 3 test suites.
[----------] Global test environment set-up.
[----------] 23 tests from Matrix
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
[ RUN      ] Matrix.booleanConversion
[       OK ] Matrix.booleanConversion (0 ms)
[ RUN      ] Matrix.equal
[       OK ] Matrix.equal (0 ms)
[ RUN      ] Matrix.notEqual
[       OK ] Matrix.notEqual (0 ms)
[ RUN      ] Matrix.dump
[       OK ] Matrix.dump (0 ms)
[ RUN      ] Matrix.neg
[       OK ] Matrix.neg (0 ms)
[ RUN      ] Matrix.abs
[       OK ] Matrix.abs (0 ms)
[ RUN      ] Matrix.sqrt
[       OK ] Matrix.sqrt (0 ms)
[ RUN      ] Matrix.log
[       OK ] Matrix.log (0 ms)
[ RUN      ] Matrix.getVersion
[       OK ] Matrix.getVersion (0 ms)
[----------] 23 tests from Matrix (0 ms total)

[----------] 4 tests from unaryOperator
[ RUN      ] unaryOperator.Neg
[       OK ] unaryOperator.Neg (0 ms)
[ RUN      ] unaryOperator.Abs
[       OK ] unaryOperator.Abs (0 ms)
[ RUN      ] unaryOperator.Sqrt
[       OK ] unaryOperator.Sqrt (0 ms)
[ RUN      ] unaryOperator.Log
[       OK ] unaryOperator.Log (0 ms)
[----------] 4 tests from unaryOperator (0 ms total)

[----------] 3 tests from binaryOperator
[ RUN      ] binaryOperator.Add
[       OK ] binaryOperator.Add (0 ms)
[ RUN      ] binaryOperator.Sub
[       OK ] binaryOperator.Sub (0 ms)
[ RUN      ] binaryOperator.Mul
[       OK ] binaryOperator.Mul (0 ms)
[----------] 3 tests from binaryOperator (0 ms total)

[----------] Global test environment tear-down
[==========] 30 tests from 3 test suites ran. (0 ms total)
[  PASSED  ] 30 tests.
```

## Element wise Matrix operations: add, subtract, multiply

Now that scalar binary operators are implemented, you can add `Matrix` level
binary operators. The pattern is very similar to the one used for unary
operators: you will add a helper routine that will traverse the matrices and
apply the scalar operator, but with an extra step. Although the element wise
processing of matrices does not require a specific order for the rows or
columns, the matrices must have the same dimensions; if not, this is an error
and the program should be terminated.

Add this `applyEltWiseBinaryOp` helper routine to the public section of `Matrix`
in `include/Matrix/Matrix.h`:

```CPP
    /// Apply element wise binary scalar operator \p bOp to each element.
    template <template <typename> class bOp>
    Matrix &applyEltWiseBinaryOp(const bOp<Ty> &op, const Matrix &rhs) {
        static_assert(std::is_base_of<binaryOperation, bOp<Ty>>::value,
                      "op must be a binaryOperation");
        if (getNumRows() != rhs.getNumRows() ||
            getNumColumns() != rhs.getNumColumns())
            die(__FILE__, __LINE__,
                "Inconsistent Matrix dimensions for elementwise operation");
        for (size_t i = 0; i < getNumElements(); i++)
            data[i] = op(data[i], rhs.data[i]);
        return *this;
    }
```

Add to the public section of `Matrix` in `include/Matrix/Matrix.h` the
`add`, `sub` and `mul` operators, composing the matrices traversal
`applyEltWiseBinaryOp` with the scalar operators you've just added:

```CPP
    // Add Matrix \p rhs to this Matrix.
    Matrix &operator+=(const Matrix &rhs) {
        return applyEltWiseBinaryOp(Add<Ty>(), rhs);
    }
    // Substract Matrix \p rhs from this Matrix.
    Matrix &operator-=(const Matrix &rhs) {
        return applyEltWiseBinaryOp(Sub<Ty>(), rhs);
    }
    // Element wise multiplication of this Matrix by \p rhs (a.k.a dot product).
    Matrix &operator*=(const Matrix &rhs) {
        return applyEltWiseBinaryOp(Mul<Ty>(), rhs);
    }
```

These operators do modify the objects in-place, thus the `+=`, `-=` and `*=`, so
you will now add functional versions of these operations. Outside of the
`Matrix` class in `include/Matrix/Operators.h`, but in the `MatComp` namespace,
add:

```CPP
/// Add Matrix \p lhs and \p rhs.
template <typename Ty>
Matrix<Ty> operator+(const Matrix<Ty> &lhs, const Matrix<Ty> &rhs) {
    return Matrix(lhs) += rhs;
}

/// Subtract Matrix \p rhs from Matrix \p lhs.
template <typename Ty>
Matrix<Ty> operator-(const Matrix<Ty> &lhs, const Matrix<Ty> &rhs) {
    return Matrix(lhs) -= rhs;
}

/// Elementwise multiplication (a.k.a dot product) of Matrix \p lhs by \p rhs.
template <typename Ty>
Matrix<Ty> operator*(const Matrix<Ty> &lhs, const Matrix<Ty> &rhs) {
    return Matrix(lhs) *= rhs;
}
```

You can see that those operation first make a copy of the `lhs` object with
`Matrix(lhs)`, then modify the copy in place with `rhs` and then return the
result without modifying `lhs` or `rhs`.

Add tests for all these in-place and functional operators in
`tests/Matrix.cpp`:

```CPP
TEST(Matrix, inPlaceAdd) {
    Matrix<int16_t> m0 = Matrix<int16_t>::ones(3, 3);
    const Matrix<int16_t> m1 = Matrix<int16_t>::identity(3);
    m0 += m1;
    EXPECT_TRUE(m0);
    EXPECT_EQ(m0.getNumRows(), 3);
    EXPECT_EQ(m0.getNumColumns(), 3);
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            if (row == col)
                EXPECT_EQ(m0.get(row, col), 2);
            else
                EXPECT_EQ(m0.get(row, col), 1);
}

TEST(Matrix, inPlaceSub) {
    Matrix<int32_t> m0 = Matrix<int32_t>::ones(4, 4);
    const Matrix<int32_t> m1 = Matrix<int32_t>::identity(4);
    m0 -= m1;
    EXPECT_TRUE(m0);
    EXPECT_EQ(m0.getNumRows(), 4);
    EXPECT_EQ(m0.getNumColumns(), 4);
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            if (row == col)
                EXPECT_EQ(m0.get(row, col), 0);
            else
                EXPECT_EQ(m0.get(row, col), 1);
}

TEST(Matrix, inPlaceDotProduct) {
    Matrix<int64_t> m0(2, 2, {1, 2, 3, 4});
    const Matrix<int64_t> m1 = Matrix<int64_t>::identity(2);
    m0 *= m1;
    EXPECT_TRUE(m0);
    EXPECT_EQ(m0.getNumRows(), 2);
    EXPECT_EQ(m0.getNumColumns(), 2);
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            if (row == col)
                EXPECT_EQ(m0.get(row, col), row * m0.getNumColumns() + col + 1);
            else
                EXPECT_EQ(m0.get(row, col), 0);
}

TEST(Matrix, functionalAdd) {
    Matrix<int16_t> m0 =
        Matrix<int16_t>::ones(3, 3) + Matrix<int16_t>::identity(3);
    EXPECT_TRUE(m0);
    EXPECT_EQ(m0.getNumRows(), 3);
    EXPECT_EQ(m0.getNumColumns(), 3);
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            if (row == col)
                EXPECT_EQ(m0.get(row, col), 2);
            else
                EXPECT_EQ(m0.get(row, col), 1);
}

TEST(Matrix, functionalSub) {
    Matrix<int32_t> m0 =
        Matrix<int32_t>::ones(4, 4) - Matrix<int32_t>::identity(4);
    EXPECT_TRUE(m0);
    EXPECT_EQ(m0.getNumRows(), 4);
    EXPECT_EQ(m0.getNumColumns(), 4);
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            if (row == col)
                EXPECT_EQ(m0.get(row, col), 0);
            else
                EXPECT_EQ(m0.get(row, col), 1);
}

TEST(Matrix, functionalDotProduct) {
    Matrix<int64_t> m0 =
        Matrix<int64_t>(2, 2, {1, 2, 3, 4}) * Matrix<int64_t>::identity(2);
    EXPECT_TRUE(m0);
    EXPECT_EQ(m0.getNumRows(), 2);
    EXPECT_EQ(m0.getNumColumns(), 2);
    for (size_t row = 0; row < m0.getNumRows(); row++)
        for (size_t col = 0; col < m0.getNumColumns(); col++)
            if (row == col)
                EXPECT_EQ(m0.get(row, col), row * m0.getNumColumns() + col + 1);
            else
                EXPECT_EQ(m0.get(row, col), 0);
}
```

```BASH { output_lines = "4-90" }
cd build
ninja
ninja check
...
[==========] Running 36 tests from 3 test suites.
[----------] Global test environment set-up.
[----------] 29 tests from Matrix
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
[ RUN      ] Matrix.booleanConversion
[       OK ] Matrix.booleanConversion (0 ms)
[ RUN      ] Matrix.equal
[       OK ] Matrix.equal (0 ms)
[ RUN      ] Matrix.notEqual
[       OK ] Matrix.notEqual (0 ms)
[ RUN      ] Matrix.dump
[       OK ] Matrix.dump (0 ms)
[ RUN      ] Matrix.neg
[       OK ] Matrix.neg (0 ms)
[ RUN      ] Matrix.abs
[       OK ] Matrix.abs (0 ms)
[ RUN      ] Matrix.sqrt
[       OK ] Matrix.sqrt (0 ms)
[ RUN      ] Matrix.log
[       OK ] Matrix.log (0 ms)
[ RUN      ] Matrix.inPlaceAdd
[       OK ] Matrix.inPlaceAdd (0 ms)
[ RUN      ] Matrix.inPlaceSub
[       OK ] Matrix.inPlaceSub (0 ms)
[ RUN      ] Matrix.inPlaceDotProduct
[       OK ] Matrix.inPlaceDotProduct (0 ms)
[ RUN      ] Matrix.functionalAdd
[       OK ] Matrix.functionalAdd (0 ms)
[ RUN      ] Matrix.functionalSub
[       OK ] Matrix.functionalSub (0 ms)
[ RUN      ] Matrix.functionalDotProduct
[       OK ] Matrix.functionalDotProduct (0 ms)
[ RUN      ] Matrix.getVersion
[       OK ] Matrix.getVersion (0 ms)
[----------] 29 tests from Matrix (0 ms total)

[----------] 4 tests from unaryOperator
[ RUN      ] unaryOperator.Neg
[       OK ] unaryOperator.Neg (0 ms)
[ RUN      ] unaryOperator.Abs
[       OK ] unaryOperator.Abs (0 ms)
[ RUN      ] unaryOperator.Sqrt
[       OK ] unaryOperator.Sqrt (0 ms)
[ RUN      ] unaryOperator.Log
[       OK ] unaryOperator.Log (0 ms)
[----------] 4 tests from unaryOperator (0 ms total)

[----------] 3 tests from binaryOperator
[ RUN      ] binaryOperator.Add
[       OK ] binaryOperator.Add (0 ms)
[ RUN      ] binaryOperator.Sub
[       OK ] binaryOperator.Sub (0 ms)
[ RUN      ] binaryOperator.Mul
[       OK ] binaryOperator.Mul (0 ms)
[----------] 3 tests from binaryOperator (0 ms total)

[----------] Global test environment tear-down
[==========] 36 tests from 3 test suites ran. (0 ms total)
[  PASSED  ] 36 tests.
```

### Matrix x Matrix multiplication

Last, but not least, the `Matrix` class still needs the most important operation:
matrix multiplication.

Add the `multiply` function, outside of the `Matrix` class, but in the
`MatComp` namespace in `include/Matrix/Operators.h`. `multiply` will check that
the arguments have compatible dimensions, then create an uninitialized
matrix that will hold the multiplication result and eventually perform the
multiplication to fill it.

```CPP
/// Matrix multiplication.
template <typename Ty>
Matrix<Ty> multiply(const Matrix<Ty> &lhs, const Matrix<Ty> &rhs) {
    if (lhs.getNumColumns() != rhs.getNumRows())
        die(__FILE__, __LINE__, "Incompatible dimensions in Matrix multiply");
    Matrix<Ty> result(lhs.getNumRows(), rhs.getNumColumns());
    for (size_t row = 0; row < result.getNumRows(); row++)
        for (size_t col = 0; col < result.getNumColumns(); col++) {
            Ty acc = Ty(0);
            for (size_t t = 0; t < lhs.getNumColumns(); t++)
                acc += lhs.get(row, t) * rhs.get(t, col);
            result.get(row, col) = acc;
        }
    return result;
}
```

Add some tests in `tests/Matrix.cpp`:

```CPP
TEST(Matrix, multiplication) {
    // Test matrix x matrix.
    Matrix<double> m0 = multiply(Matrix<double>(2, 2, {1., 2., 3., 4.}),
                                 Matrix<double>(2, 2, {0., 1., 2., 3.}));
    EXPECT_TRUE(m0);
    const Matrix<double> m0_exp(2, 2, {4., 7., 8., 15.});
    EXPECT_EQ(m0.getNumColumns(), m0_exp.getNumColumns());
    EXPECT_EQ(m0.getNumRows(), m0_exp.getNumRows());
    EXPECT_EQ(m0.getNumElements(), m0_exp.getNumElements());
    for (size_t row = 0; row < m0_exp.getNumRows(); row++)
        for (size_t col = 0; col < m0_exp.getNumColumns(); col++)
            EXPECT_DOUBLE_EQ(m0.get(row, col), m0_exp.get(row, col));

    // Test matrix x vector
    Matrix<float> m1 =
        multiply(Matrix<float>(3, 3, {1., 2., 3., 4., 5., 6., 7., 8., 9.}),
                 Matrix<float>(3, 1, {1., 2., 3.}));
    EXPECT_TRUE(m1);
    const Matrix<float> m1_exp(3, 1, {14., 32., 50.});
    EXPECT_EQ(m1.getNumColumns(), m1_exp.getNumColumns());
    EXPECT_EQ(m1.getNumRows(), m1_exp.getNumRows());
    EXPECT_EQ(m1.getNumElements(), m1_exp.getNumElements());
    for (size_t row = 0; row < m1_exp.getNumRows(); row++)
        for (size_t col = 0; col < m1_exp.getNumColumns(); col++)
            EXPECT_FLOAT_EQ(m1.get(row, col), m1_exp.get(row, col));
}

```

```BASH { output_lines = "4-92" }
cd build
ninja
ninja check
...
[==========] Running 37 tests from 3 test suites.
[----------] Global test environment set-up.
[----------] 30 tests from Matrix
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
[ RUN      ] Matrix.booleanConversion
[       OK ] Matrix.booleanConversion (0 ms)
[ RUN      ] Matrix.equal
[       OK ] Matrix.equal (0 ms)
[ RUN      ] Matrix.notEqual
[       OK ] Matrix.notEqual (0 ms)
[ RUN      ] Matrix.dump
[       OK ] Matrix.dump (0 ms)
[ RUN      ] Matrix.neg
[       OK ] Matrix.neg (0 ms)
[ RUN      ] Matrix.abs
[       OK ] Matrix.abs (0 ms)
[ RUN      ] Matrix.sqrt
[       OK ] Matrix.sqrt (0 ms)
[ RUN      ] Matrix.log
[       OK ] Matrix.log (0 ms)
[ RUN      ] Matrix.inPlaceAdd
[       OK ] Matrix.inPlaceAdd (0 ms)
[ RUN      ] Matrix.inPlaceSub
[       OK ] Matrix.inPlaceSub (0 ms)
[ RUN      ] Matrix.inPlaceDotProduct
[       OK ] Matrix.inPlaceDotProduct (0 ms)
[ RUN      ] Matrix.functionalAdd
[       OK ] Matrix.functionalAdd (0 ms)
[ RUN      ] Matrix.functionalSub
[       OK ] Matrix.functionalSub (0 ms)
[ RUN      ] Matrix.functionalDotProduct
[       OK ] Matrix.functionalDotProduct (0 ms)
[ RUN      ] Matrix.multiplication
[       OK ] Matrix.multiplication (0 ms)
[ RUN      ] Matrix.getVersion
[       OK ] Matrix.getVersion (0 ms)
[----------] 30 tests from Matrix (0 ms total)

[----------] 4 tests from unaryOperator
[ RUN      ] unaryOperator.Neg
[       OK ] unaryOperator.Neg (0 ms)
[ RUN      ] unaryOperator.Abs
[       OK ] unaryOperator.Abs (0 ms)
[ RUN      ] unaryOperator.Sqrt
[       OK ] unaryOperator.Sqrt (0 ms)
[ RUN      ] unaryOperator.Log
[       OK ] unaryOperator.Log (0 ms)
[----------] 4 tests from unaryOperator (0 ms total)

[----------] 3 tests from binaryOperator
[ RUN      ] binaryOperator.Add
[       OK ] binaryOperator.Add (0 ms)
[ RUN      ] binaryOperator.Sub
[       OK ] binaryOperator.Sub (0 ms)
[ RUN      ] binaryOperator.Mul
[       OK ] binaryOperator.Mul (0 ms)
[----------] 3 tests from binaryOperator (0 ms total)

[----------] Global test environment tear-down
[==========] 37 tests from 3 test suites ran. (0 ms total)
[  PASSED  ] 37 tests.
```

### Other useful operations

A  complete matrix processing library would need some other important
operations:
- type conversion: the library only supports operations with the same type for
now, and this is enforced by the compiler. Avoiding silent conversions is
desirable, but there are cases where data have different types and *explicit*
conversion will be necessary.
- transposition (i.e. swapping the rows / columns) is another important
operation, with some room for optimization in the implementation. Can you think
of different ways to implement the `transpose` operator for the `Matrix` class ?
- broadcasting: these are useful shortcuts for the `Matrix` users, as they allow
to transform a scalar or a row-vector / column-vector by replicating it to make
it look like a 2-D matrix. Again, on top of syntactic sugar for the users, this
provides a large performance improvement, especially in memory usage, as one can
play with how the elements are accessed rather than duplicating the matrix
content.
- resize: to be able to dynamically change a matrix dimensions
- extract: to be able to extract part of a matrix

## What have you achieved so far?

At this stage, the code structure looks like: 

```TXT
Matrix/
├── CMakeLists.txt
├── build/
...
├── external/
│   └── CMakeLists.txt
├── include/
│   └── Matrix/
│       ├── Matrix.h
│       └── Operators.h
├── lib/
│   └── Matrix/
│       └── Matrix.cpp
├── src/
│   ├── getVersion.cpp
│   └── howdy.cpp
└── tests/
    ├── Matrix.cpp
    ├── Operators.cpp
    ├── Version.cpp
    └── main.cpp
```

You can download the [archive](/artifacts/matrix/chapter-4.tar.xz) of the
project in its current state to experiment locally on your machine.

Congratulations, you now have a minimalistic yet fully functional matrix
processing library, with some level of regression testing, that can be easily
built and used.

The testing could (and should) go much deeper, as a number of
corner cases have not been covered.

You can continue to add more functions (and more tests).