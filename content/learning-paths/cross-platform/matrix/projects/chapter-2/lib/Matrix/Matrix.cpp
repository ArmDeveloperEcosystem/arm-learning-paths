#include "Matrix/Matrix.h"

namespace {
const MatComp::Version version = {.major = 0, .minor = 1, .patch = 0};
}

namespace MatComp {

const Version &getVersion() { return version; }

} // namespace MatComp
