# Make a set out of a sequence
X = set('spam')

# Make a set with set literals
Y = {'h', 'a', 'm'}


class TestSets:
    def test_tuple_sets(self):
        assert X, Y == ({'m', 'a', 'p', 's'}, {'m', 'a', 'h'})

    def test_intersection(self):
        assert X & Y == {'m', 'a'}

    def test_union(self):
        assert X | Y == {'m', 'h', 'a', 'p', 's'}

    def test_difference(self):
        assert X - Y == {'p', 's'}

    def test_superset(self):
        assert not (X > Y)

    def test_comprehensions(self):
        assert {n ** 2 for n in [1, 2, 3, 4]} == {16, 1, 4, 9}

    def test_filtering_duplicates(self):
        assert list({1, 2, 1, 3, 1}) == [1, 2, 3]

    def test_difference_in_collections(self):
        assert set('spam') - set('ham') == {'p', 's'}

    def test_order_neutral_equality(self):
        assert set('spam') == set('asmp')

    def test_in_membership_tests(self):
        assert ('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham']) == (True, True, True)
