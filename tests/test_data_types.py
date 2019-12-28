from decimal import Decimal
from fractions import Fraction


def test_numbers():
    assert isinstance(1234, int)
    assert isinstance(3.1415, float)
    assert isinstance(3+4j, complex)
    assert isinstance(0b111, int)
    assert isinstance(Decimal(), Decimal)
    assert isinstance(Fraction(), Fraction)
