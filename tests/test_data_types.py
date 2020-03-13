from decimal import Decimal
from fractions import Fraction
from os import path

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


def test_dictionaries():
    assert isinstance({'food': 'spam', 'taste': 'yum'}, dict)
    assert isinstance(dict(hours=10), dict)


def test_files():
    assert path.isfile('test_file.txt')


def test_sets():
    assert isinstance(set('abc'), set)
    assert isinstance({'a', 'b', 'c'}, set)


def test_boolean():
    assert isinstance(True, bool)
    assert isinstance(False, bool)
