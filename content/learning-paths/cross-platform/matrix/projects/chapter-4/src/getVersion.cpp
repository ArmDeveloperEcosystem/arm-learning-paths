#include "Matrix/Matrix.h"

#include <cstdlib>
#include <iostream>

using namespace std;
using namespace MatComp;

int main(int argc, char *argv[]) {
    const Version &version = getVersion();
    cout << "Using Matrix version: " << version.major << '.' << version.minor
         << '.' << version.patch << '\n';

    return EXIT_SUCCESS;
}
