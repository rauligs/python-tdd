import pytest

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
        assert initial_str == 'zSpam'

    def test_change_using_list(self):
        initial_str = 'shrubbery'
        initial_str_as_list = list(initial_str)
        initial_str_as_list[1] = 'c'
        assert ''.join(initial_str_as_list) == 'scrubbery'  # Join with empty delimiter
        assert initial_str == 'shrubbery'

    def test_change_using_bytearray(self):
        initial_str_as_bytearray = bytearray(b'spam') # 'b' needed in 3.X, not 2.X
        initial_str_as_bytearray.extend(b'eggs')
        assert initial_str_as_bytearray.decode() == 'spameggs'
