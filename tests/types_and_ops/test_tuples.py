class TestTuples:
    # The tuple object is like a list but immutable.
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
