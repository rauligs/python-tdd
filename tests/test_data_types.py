from decimal import Decimal
from fractions import Fraction


def test_numbers():
    assert isinstance(1234, int)
    assert isinstance(3.1415, float)
    assert isinstance(3 + 4j, complex)
    assert isinstance(0b111, int)
    assert isinstance(Decimal(), Decimal)
    assert isinstance(Fraction(), Fraction)


def test_strings():
    assert isinstance('spam', str)
    assert isinstance("Bob's", str)
    assert isinstance(b'a\x01c', bytes)
    assert isinstance(u'sp\xc4m', str)


def test_lists():
    assert isinstance([1, [2, 'three'], 4.5], list)
    assert isinstance(list(range(10)), list)
