#pragma once

namespace MatComp {

/// The Version struct is used to carry around the major, minor and patch level.
struct Version {
    unsigned major; //< The major version level.
    unsigned minor; //< The minor version level.
    unsigned patch; //< The patch level.
};

/// Get the Matrix library version information.
const Version &getVersion();

} // namespace MatComp
