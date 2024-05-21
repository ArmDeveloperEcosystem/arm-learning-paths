#include "Matrix/Matrix.h"

#include "gtest/gtest.h"

using namespace MatComp;

TEST(Matrix, getVersion) {
    const Version &version = getVersion();
    EXPECT_EQ(version.major, 0);
    EXPECT_EQ(version.minor, 1);
    EXPECT_EQ(version.patch, 0);
}
