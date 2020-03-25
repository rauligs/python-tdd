import pytest
import re

WORD = 'Spam'


class TestStrings:
    def test_sequence(self):
        assert len(WORD) == 4
        assert WORD[0] == 'S'
        assert WORD[1] == 'p'

    def test_last_item(self):
        assert WORD[-1] == 'm'

    def test_slice(self):
        assert WORD[1:3] == 'pa'
        # X[I:J], means “give me everything in X from offset I up to but not including offset J

    def test_slice_right_bound_default(self):
        assert WORD[1:] == 'pam'

    def test_slice_left_bound_default(self):
        assert WORD[:3] == 'Spa'
        assert WORD[:-1] == 'Spa'

    def test_slice_all(self):
        assert WORD[:] == 'Spam'
        # All of S as a top-level copy (0:len(S))

    def test_concatenation(self):
        assert WORD + 'xyz' == 'Spamxyz'
        assert WORD == 'Spam'

    def test_repetition(self):
        assert WORD * 3 == 'SpamSpamSpam'

    def test_immutability(self):
        with pytest.raises(TypeError) as exception_msg:
            def illegal_change():
                WORD[0] = 'z'

            illegal_change()
        assert "'str' object does not support item assignment" in str(exception_msg.value)
        # In terms of the core types, numbers, strings, and tuples are immutable; lists, dictionaries, and sets are not

    def test_make_new_object(self):
        initial_str = 'Spam'
        initial_str = 'z' + initial_str[1:]
        assert initial_str == 'zpam'

    def test_change_using_list(self):
        initial_str = 'shrubbery'
        initial_str_as_list = list(initial_str)
        initial_str_as_list[1] = 'c'
        assert ''.join(initial_str_as_list) == 'scrubbery'  # Join with empty delimiter
        assert initial_str == 'shrubbery'

    def test_change_using_bytearray(self):
        initial_str_as_bytearray = bytearray(b'spam')  # 'b' needed in 3.X, not 2.X
        initial_str_as_bytearray.extend(b'eggs')
        assert initial_str_as_bytearray.decode() == 'spameggs'

    def test_find(self):
        assert WORD.find('pa') == 1

    def test_replace(self):
        assert WORD.replace('pa', 'XYZ') == 'SXYZm'
        assert WORD == 'Spam'

    def test_split(self):
        line = 'aaa,bbb,ccc,dd'
        assert line.split(',') == ['aaa', 'bbb', 'ccc', 'dd']

    def test_upper(self):
        assert WORD.upper() == 'SPAM'

    def test_isalpha(self):
        assert WORD.isalpha() == True

    def test_isdigit(self):
        assert WORD.isdigit() == False

    def test_remove_right_side_whitespaces(self):
        line = 'something\n\n'
        assert line.rstrip() == 'something'

    def test_ops_combination(self):
        line = 'some,thing\n\n'
        assert line.rstrip().split(',') == ['some', 'thing']

    def test_basic_formatting_expression(self):
        # All Python versions
        assert '%s, eggs, and %s' % ('spam', 'SPAM!') == 'spam, eggs, and SPAM!'

    def test_basic_formatting_method(self):
        # Python 2.6+, 3.0+
        assert '{0}, eggs, and {1}'.format('spam', 'SPAM!') == 'spam, eggs, and SPAM!'

    def test_basic_formatting_numbers_optional(self):
        # Python 2.7+, 3.1+
        assert '{}, eggs, and {}'.format('spam', 'SPAM!') == 'spam, eggs, and SPAM!'

    def test_code_special_chars(self):
        assert len('A\nB\tC') == 5

    def test_new_line_decimal_value(self):
        assert ord('\n') == 10

    def test_binary_zero_type(self):
        assert len('A\0B\0C') == 5

    def test_non_printables(self):
        non_printable = 'A\0B\0C'
        # Non-printables are displayed as \xNN hex escapes
        assert non_printable == 'A\x00B\x00C'
        assert non_printable == 'A\0B\0C'

    def test_embedding_text(self):
        message = """
aaa
bb''""'b
c
"""
        assert message == '\naaa\nbb\'\'""\'b\nc\n'

    def test_raw(self):
        # turns off the backslash escape mechanism
        assert r'C:\text\new' != 'C:\text\new'

    def test_hexadecimal(self):
        # u'sp\u00c4m' in Python 2.X. In Python 3.X normal strings are Unicode
        assert 'sp\xc4m' == 'spÄm'

    def test_short_unicode(self):
        assert 'sp\u00c4m' == 'spÄm'

    def test_long_unicode(self):
        assert 'sp\U000000c4m' == 'spÄm'

    def test_encode_utf8(self):
        # Encoded to 4 bytes in UTF-8
        assert WORD.encode('utf8') == b'Spam'

    def test_encode_utf16(self):
        # Encoded to 10 bytes in UTF-16
        assert WORD.encode('utf16') == b'\xff\xfeS\x00p\x00a\x00m\x00'

    # memory <-> encoded to bytes <-> files

    def test_basic_pattern_matching_group(self):
        match = re.match('Hello[ \t]*(.*)world', 'Hello    Python world')
        assert match.group(1) == 'Python '

    def test_basic_pattern_matching_groups(self):
        match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
        assert match.groups() == ('usr', 'home', 'lumberjack')

    def test_basic_pattern_matching_split(self):
        assert re.split('[/:]', '/usr/home:lumberjack') == ['', 'usr', 'home', 'lumberjack']

# Notes:

# Generic operations that span multiple types show up as built-in functions or expressions (e.g., len(X), X[0]),
# but type-specific operations are method calls (e.g., 'MyString'.upper())

# dir
# built-in dir function returns a list of all the attributes available for any object passed to it.
# Ignore the double underscores for now in the result
# Being in Python shell:
# >>> dir({variable_here_or_data_type})


# help
# Displays documentation (PyDoc)
# >>> help({variable_here_or_data_type}.replace)
# >>> help ({variable_here_or_data_type})
