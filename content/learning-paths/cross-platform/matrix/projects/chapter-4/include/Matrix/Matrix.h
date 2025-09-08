#pragma once

#include "Matrix/Operators.h"

#include <cassert>
#include <cstring>
#include <initializer_list>
#include <iostream>
#include <memory>
#include <type_traits>

namespace MatComp {

/// The Version struct is used to carry around the major, minor and patch level.
struct Version {
    unsigned major; //< The major version level.
    unsigned minor; //< The minor version level.
    unsigned patch; //< The patch level.
};

/// Get the Matrix library version information.
const Version &getVersion();

/// Immediately terminates the application with \p reason as the error message
/// and the EXIT_FAILURE error code. It will also print the file name (\p
/// fileName) and line number (\p lineNumber) that caused that application to
/// exit.
[[noreturn]] void die(const char *fileName, size_t lineNumber,
                      const char *reason);

/// The Matrix class represents N x M matrices for all arithmetic types.
template <typename Ty> class Matrix {

    static_assert(std::is_arithmetic<Ty>::value,
                  "Matrix only accept arithmetic (i.e. integer or floating "
                  "point) element types.");

  public:
    /// Default construct an invalid Matrix.
    constexpr Matrix() : numRows(0), numColumns(0), data(nullptr) {}

    /// Construct a \p numRows x \p numColumns uninitialized Matrix
    Matrix(size_t numRows, size_t numColumns)
        : numRows(numRows), numColumns(numColumns), data() {
        allocate(getNumElements());
    }

    /// Construct a \p numRows x \p numColumns Matrix with all elements
    /// initialized to value \p val.
    Matrix(size_t numRows, size_t numCols, Ty val) : Matrix(numRows, numCols) {
        allocate(getNumElements());
        for (size_t i = 0; i < getNumElements(); i++)
            data[i] = val;
    }

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

    /// Assign from the \p il initializer list.
    Matrix &operator=(std::initializer_list<Ty> il) {
        if (il.size() != getNumElements())
            die(__FILE__, __LINE__, "number of elements do not match");

        size_t i = 0;
        for (const auto &val : il)
            data[i++] = val;

        return *this;
    }

    /// Get the number of rows in this matrix.
    size_t getNumRows() const { return numRows; }
    /// Get the number of columns in this matrix.
    size_t getNumColumns() const { return numColumns; }
    /// Get the number of elements in this matrix.
    size_t getNumElements() const { return numRows * numColumns; }
    /// Get the storage size in bytes of the Matrix array.
    size_t getSizeInBytes() const { return numRows * numColumns * sizeof(Ty); }

    /// Returns true if this matrix is valid.
    operator bool() const {
        return numRows != 0 && numColumns != 0;
    }

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
    /// Returns true iff matrices do not compare equal.
    bool operator!=(const Matrix &rhs) const { return !(*this == rhs); }

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

    /// Apply element wise unary scalar operator \p uOp to each element.
    template <template <typename> class uOp>
    Matrix &applyEltWiseUnaryOp(const uOp<Ty> &op) {
        static_assert(std::is_base_of<unaryOperation, uOp<Ty>>::value,
                      "op must be a unaryOperation");
        for (size_t i = 0; i < getNumElements(); i++)
            data[i] = op(data[i]);
        return *this;
    }

    /// Apply negate to each element of this Matrix.
    Matrix &neg() { return applyEltWiseUnaryOp(Neg<Ty>()); }

    /// Apply absolute value to each element of this Matrix.
    Matrix &abs() { return applyEltWiseUnaryOp(Abs<Ty>()); }

    /// Apply square root to each element of this Matrix.
    Matrix &sqrt() { return applyEltWiseUnaryOp(Sqrt<Ty>()); }

    /// Apply natural logarithm to each element of this Matrix.
    Matrix &log() { return applyEltWiseUnaryOp(Log<Ty>()); }

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

  private:
    size_t numRows;    //< The number of rows in this matrix.
    size_t numColumns; //< The number of columns in this matrix.
    std::unique_ptr<Ty[]>
        data; //< The actual data in this matrix, in row-major order.

    /// Allocate (if need be) numElements to the Matrix. Die if the allocation
    /// went wrong.
    void allocate(size_t numElements) {
        if (numElements != 0) {
            data = std::make_unique<Ty[]>(numElements);
            if (!data)
                die(__FILE__, __LINE__, "Matrix allocation failure");
        }
    }

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
};

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

/// Add Matrix \p lhs and \p rhs.
template <typename Ty>
Matrix<Ty> operator+(const Matrix<Ty> &lhs, const Matrix<Ty> &rhs) {
    return Matrix(lhs) += rhs;
}

/// Substract Matrix \p rhs from Matrix \p lhs.
template <typename Ty>
Matrix<Ty> operator-(const Matrix<Ty> &lhs, const Matrix<Ty> &rhs) {
    return Matrix(lhs) -= rhs;
}

/// Elementwise multiplication (a.k.a dot product) of Matrix \p lhs by \p rhs.
template <typename Ty>
Matrix<Ty> operator*(const Matrix<Ty> &lhs, const Matrix<Ty> &rhs) {
    return Matrix(lhs) *= rhs;
}

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

} // namespace MatComp

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
