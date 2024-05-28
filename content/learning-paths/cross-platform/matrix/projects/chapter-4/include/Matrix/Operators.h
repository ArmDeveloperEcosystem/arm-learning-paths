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

} // namespace MatComp
