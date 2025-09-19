class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        gcd = self.__gcd(abs(numerator), abs(denominator))
        numerator //= gcd
        denominator //= gcd

        # Ensure denominator is always positive
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        self.__numerator = numerator
        self.__denominator = denominator

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def __repr__(self):
        return f"Fraction({self.__numerator}, {self.__denominator})"

    def __gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    # Arithmetic operations
    def __add__(self, other):
        other = self.__ensure_fraction(other)
        num = self.__numerator * other.denominator + self.__denominator * other.numerator
        den = self.__denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        other = self.__ensure_fraction(other)
        num = self.__numerator * other.denominator - self.__denominator * other.numerator
        den = self.__denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other):
        other = self.__ensure_fraction(other)
        num = self.__numerator * other.numerator
        den = self.__denominator * other.denominator
        return Fraction(num, den)

    def __truediv__(self, other):
        other = self.__ensure_fraction(other)
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        num = self.__numerator * other.denominator
        den = self.__denominator * other.numerator
        return Fraction(num, den)

    # Comparison operations
    def __eq__(self, other):
        other = self.__ensure_fraction(other)
        return self.__numerator == other.numerator and self.__denominator == other.denominator

    def __lt__(self, other):
        other = self.__ensure_fraction(other)
        return self.__numerator * other.denominator < other.numerator * self.__denominator

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __neg__(self):
        return Fraction(-self.__numerator, self.__denominator)

    def __abs__(self):
        return Fraction(abs(self.__numerator), self.__denominator)

    def __hash__(self):
        return hash((self.__numerator, self.__denominator))

    # Conversion methods
    def to_float(self, round_to=3):
        return round(self.__numerator / self.__denominator, round_to)

    def to_int(self):
        return self.__numerator // self.__denominator

    def to_str(self):
        return str(self)

    # Properties
    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    # Helper
    def __ensure_fraction(self, value):
        if isinstance(value, Fraction):
            return value
        elif isinstance(value, int):
            return Fraction(value, 1)
        else:
            raise TypeError("Unsupported type for arithmetic with Fraction.")
    
    @classmethod
    def from_string(cls, s):
        """Parses '3/4' or '1 1/2' into a Fraction object."""
        s = s.strip()
        if ' ' in s:  # Mixed fraction like '1 1/2'
            whole, frac = s.split()
            num, den = map(int, frac.split('/'))
            whole = int(whole)
            num = abs(whole) * den + num
            if whole < 0:
                num = -num
            return cls(num, den)
        elif '/' in s:  # Simple fraction like '3/4'
            num, den = map(int, s.split('/'))
            return cls(num, den)
        else:
            raise ValueError("Invalid fraction string format.")

    @classmethod
    def from_float(cls, value, max_denominator=10000):
        """Converts a float to a Fraction using continued fraction method."""
        from fractions import Fraction as PyFraction
        f = PyFraction(value).limit_denominator(max_denominator)
        return cls(f.numerator, f.denominator)





f1 = Fraction(2, 2)
f2 = Fraction(4, 8)
f3 = Fraction(-3, 9)

print("Fraction 1:", f1)
print("Fraction 2:", f2)
print("Fraction 3:", f3)
print("Addition:", f1 + f2)
print("Subtraction:", f1 - f2)
print("Multiplication:", f1 * f2)
print("Division:", f1 / f2)
print("Float:", f3.to_float())
print("Integer:", f3.to_int())
print("Equality:", f1 == f2)
print("Greater than:", f1 > f2)
print("Absolute:", abs(f3))

f4 = Fraction.from_string("3/4")
f5 = Fraction.from_string("1 1/2")
f6 = Fraction.from_float(0.75)

print("Parsed from '3/4':", f4)
print("Parsed from '1 1/2':", f5)
print("Converted from 0.75:", f6)

