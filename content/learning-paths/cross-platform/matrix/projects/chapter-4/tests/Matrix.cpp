#include "Matrix/Matrix.h"

#include "gtest/gtest.h"

#include <cstdint>
#include <sstream>

using MatComp::Matrix;

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

TEST(Matrix, booleanConversion) {
    EXPECT_FALSE(Matrix<int8_t>());
    EXPECT_FALSE(Matrix<double>());

    EXPECT_TRUE(Matrix<int8_t>(1, 1));
    EXPECT_TRUE(Matrix<double>(1, 1));

    EXPECT_TRUE(Matrix<int8_t>(1, 1, 1));
    EXPECT_TRUE(Matrix<double>(1, 1, 2.0));
}

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
