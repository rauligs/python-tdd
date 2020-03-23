import os
from decimal import Decimal
from fractions import Fraction


class TestCoreDataTypes:

    def test_numbers(self):
        assert isinstance(1234, int)
        assert isinstance(3.1415, float)
        assert isinstance(3 + 4j, complex)
        assert isinstance(0b111, int)
        assert isinstance(Decimal(), Decimal)
        assert isinstance(Fraction(), Fraction)

    def test_strings(self):
        assert isinstance('spam', str)
        assert isinstance("Bob's", str)
        assert isinstance(b'a\x01c', bytes)
        assert isinstance(u'sp\xc4m', str)

    def test_lists(self):
        assert isinstance([1, [2, 'three'], 4.5], list)
        assert isinstance(list(range(10)), list)

    def test_dictionaries(self):
        assert isinstance({'food': 'spam', 'taste': 'yum'}, dict)
        assert isinstance(dict(hours=10), dict)

    def test_files(self):
        assert os.path.isfile(os.path.dirname(os.path.realpath(__file__)) + '/test_data_types_file.txt')

    def test_sets(self):
        assert isinstance(set('abc'), set)
        assert isinstance({'a', 'b', 'c'}, set)

    def test_boolean(self):
        assert isinstance(True, bool)
        assert isinstance(False, bool)

    def test_none(self):
        # https://stackoverflow.com/questions/41928835/how-to-access-the-nonetype-type
        assert type(None).__name__ == "NoneType"

    # Other core types: types
    # Program unit types: Functions, modules, classes (Part IV, Part V, Part VI)
    # Implementation-related types: Compiled code, stack tracebacks (Part IV, Part VII)
