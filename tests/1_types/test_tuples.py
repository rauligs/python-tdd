class TestTuples:
    # The tuple object is like a list but immutable. It supports mixed types and nesting,
    # but they don’t grow and shrink (so 'append', 'pop' or 'remove' are not possible)
    def test_create(self):
        items = (1, 2, 3, 4)
        assert len(items) == 4

    def test_concatenation(self):
        items = (1, 2, 3, 4)
        assert items + (5, 6) == (1, 2, 3, 4, 5, 6)
        assert items == (1, 2, 3, 4)

    def test_index(self):
        items = (1, 2, 3, 4)
        assert items.index(4) == 3

    def test_count(self):
        items = (1, 2, 3, 4)
        assert items.count(4) == 1

    def test_create_from_another_tuple(self):
        items = (1, 2, 3, 4)
        # one-item tuples like the one here require a trailing comma
        assert (2,) + items[1:] == (2, 2, 3, 4)
