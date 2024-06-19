#pragma once

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

    /// Apply a unary scalar operation to each element.
    template <template <typename> class uOp>
    Matrix &applyEltWiseUnaryOp(const uOp<Ty> &op) {
        for (size_t i = 0; i < getNumElements(); i++)
            data[i] = op(data[i]);
        return *this;
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
