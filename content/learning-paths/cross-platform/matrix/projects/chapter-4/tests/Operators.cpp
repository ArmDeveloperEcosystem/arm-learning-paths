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
