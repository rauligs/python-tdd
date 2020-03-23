class TestLists:
    def test_slicing(self):
        items = [123, 'spam', 1.23]
        assert len(items) == 3
        assert items[:-1] == [123, 'spam']

    def test_concat(self):
        items = [123, 'spam', 1.23]
        assert items + [1, 2] == [123, 'spam', 1.23, 1, 2]
        assert items == [123, 'spam', 1.23]

    def test_repeat(self):
        items = [123, 'spam', 1.23]
        assert items * 2 == [123, 'spam', 1.23, 123, 'spam', 1.23]
        assert items == [123, 'spam', 1.23]

    def test_append_element_to_end(self):
        items = [1, 2]
        items.append('NI')
        assert items == [1, 2, 'NI']

    def test_pop_offset_by_index(self):
        items = [1, 2, 3]
        items.pop(1)
        assert items == [1, 3]

    def test_insert_by_position(self):
        items = [1, 2]
        items.insert(0, 3)
        assert items == [3, 1, 2]

    def test_remove_first_by_value(self):
        items = [1, 3, 2, 3]
        items.remove(3)
        assert items == [1, 2, 3]

    def test_sort(self):
        items = ['bb', 'aa', 'cc']
        items.sort()
        assert items == ['aa', 'bb', 'cc']

    def test_reverse(self):
        items = ['bb', 'aa', 'cc']
        items.reverse()
        assert items == ['cc', 'aa', 'bb']

    def test_get_matrix_item(self):
        items = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert items[1] == [4, 5, 6]
        assert items[1][2] == 6

    def test_get_matrix_column_2(self):
        items = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # List comprehension expressions
        column = [row[1] for row in items]
        assert column == [2, 5, 8]
        assert items == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def test_add_1_to_column_2(self):
        items = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        column = [row[1] + 1 for row in items]
        assert column == [3, 6, 9]
        assert items == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def test_filter_odds_column_2(self):
        items = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        odds = [row[1] for row in items if row[1] % 2 == 0]
        assert odds == [2, 8]
        assert items == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def test_get_matrix_diagonal(self):
        items = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        diagonal = [items[i][i] for i in [0, 1, 2]]
        assert diagonal == [1, 5, 9]
        assert items == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def test_repeat_characters_string(self):
        assert [c * 2 for c in 'spam'] == ['ss', 'pp', 'aa', 'mm']

    def test_create_by_range(self):
        assert list(range(-6, 7, 2)) == [-6, -4, -2, 0, 2, 4, 6]

    def test_create_multiple_values_with_filter(self):
        assert [[x ** 2, x ** 3] for x in range(4) if x > 1] == [[4, 8], [9, 27]]

# List comprehension in practice and often provide a substantial processing speed advantage
# Enclosing a comprehension in parentheses can also be used to create generators that produce results on demand, ie:
# G = (sum(row) for row in M)              # Create a generator of row sums
# >>> next(G)                              # Run the iteration protocol next(). iter(G) not required here.
