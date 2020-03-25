import decimal
from decimal import Decimal
from fractions import Fraction


class TestNumeric:
    def test_chained_comparison(self):
        # Same as: 1 == 2 and 2 < 3
        assert not 1 == 2 < 3

    def test_float_comparison(self):
        assert 1.1 + 2.2 != 3.3
        # 1.1 + 2.2  # Close to 3.3, but not exactly: limited precision -> 3.3000000000000003

    def test_division_classic(self):
        assert 10 / 4 == 2.5
        assert 10 / 4.0 == 2.5
        assert 5 / 2, 5 / -2 == (2.5, -2.5)
        assert 5 / 2.0, 5 / -2.0 == (2.5, -2.5)
        # Python 2.X truncates it to 2 as is 2 integers operands

    def test_division_floor(self):
        assert 10 // 4 == 2
        assert 10 // 4.0 == 2.0
        assert 5 // 2, 5 // -2 == (2, -3)
        assert 5 // 2.0, 5 // -2.0 == (2.0, -3.0)

    def test_decimal(self):
        assert 0.1 + 0.1 + 0.1 - 0.3 == 5.551115123125783e-17
        # >>> print(0.1 + 0.1 + 0.1 - 0.3)
        # >>> 5.55111512313e-17
        assert Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') == Decimal('0.0')

    def test_decimal_precision(self):
        # Default is 28 digits
        assert Decimal(1) / Decimal(7) == Decimal('0.1428571428571428571428571429')

    def test_decimal_set_precision(self):
        # The precision is applied globally for all decimals created in the calling thread (used ie monetary apps)
        decimal.getcontext().prec = 4
        assert Decimal(1) / Decimal(7) == Decimal('0.1429')

        # Closer to 0
        assert Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3) == Decimal('1.110E-17')

        # The precision can be set temporarily with context manager
        # >>> with decimal.localcontext() as ctx:
        # >>>     ctx.prec = 2
        # >>>     decimal.Decimal('1.00') / decimal.Decimal('3.00')

    def test_fractions(self):
        x = Fraction(1, 3)  # Numerator, denominator
        y = Fraction(4, 6)
        assert x + y == Fraction(1, 1)
        assert x - y == Fraction(-1, 3)
        assert x * y == Fraction(2, 9)

    def test_fractions_from_floating_points(self):
        assert Fraction('.25') == Fraction(1, 4)
        assert Fraction('.25') + Fraction('1.25') == Fraction(3, 2)

    # Unlike floating points that can lose precision over many calculations,
    # Fraction and Decimal provide ways to get exact results (despite being a bit slower and more verbose)

    def test_fractions_float_to_fraction(self):
        assert 2.5.as_integer_ratio() == (5, 2)

        # * is special syntax that expands a tuple into individual arguments
        assert Fraction(*2.5.as_integer_ratio()) == Fraction(5, 2)

        # Other way...
        assert Fraction.from_float(1.75) == Fraction(7, 4)

    def test_fractions_fraction_to_float(self):
        assert float(Fraction(1, 3)) == 0.3333333333333333

    def test_fractions_limit_denominator(self):
        assert 4.0 / 3 == 1.3333333333333333
        assert (4.0 / 3).as_integer_ratio() == (6004799503160661, 4503599627370496)
        # Precision loss from float
        float_to_fraction = Fraction(1, 3) + Fraction(*(4.0 / 3).as_integer_ratio())
        assert float_to_fraction == Fraction(22517998136852479, 13510798882111488)
        # close to 5 / 3
        assert float_to_fraction.limit_denominator(10) == Fraction(5, 3)

        # Although you can convert from floating point to fraction, in some cases there is an unavoidable precision
        # loss when you do so, because the number is inaccurate in its original floating-point form.

    def test_boolean(self):
        assert True == 1
        assert False == 0
        assert True + 6 == 7
        # Errr... excuse me! ^

# Notes:
# Fractions mixing operations:
#   Fraction + int -> Fraction
#   Fraction + float -> float
#   Fraction + float -> float
#   Fraction + Fraction -> Fraction

# Sets supports operations corresponding to mathematical set theory, see in 1_types/test_sets.py

# Advance numeric:
# - NumPy (must be installed separately)
# - SciPy
