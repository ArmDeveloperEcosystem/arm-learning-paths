#include "Matrix/Matrix.h"

#include <cstdlib>
#include <iostream>

namespace {
const MatComp::Version version = {.major = 0, .minor = 1, .patch = 0};
}

namespace MatComp {

const Version &getVersion() { return version; }

void die(const char *fileName, size_t lineNumber, const char *reason) {
    std::cerr << "Fatal: " << reason << " from " << fileName << ':'
              << lineNumber << '\n';
    exit(EXIT_FAILURE);
}

} // namespace MatComp
