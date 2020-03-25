class TestDictionaries:
    # Known as mappings. They store objects by key instead of relative position (not ordered)
    # Mutable
    def test_fetch_value(self):
        items = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
        assert items['food'] == 'Spam'

    def test_(self):
        items = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
        items['quantity'] += 1
        assert items['quantity'] == 5

    def test_create_key_by_assignment(self):
        items = {}
        items['name'] = 'Bob'
        items['age'] = 40
        assert items == {'age': 40, 'name': 'Bob'}

    def test_create_with_dict_type(self):
        items = dict(name='Bob', age=40)
        assert items == {'age': 40, 'name': 'Bob'}

    def test_create_with_dict_and_zipping(self):
        items = dict(zip(['name', 'age'], ['Bob', 40]))
        # Creation by zipping together sequences of keys and values obtained at runtime
        assert items == {'age': 40, 'name': 'Bob'}

    def test_nesting_access(self):
        record = {'name': {'first': 'Bob', 'last': 'Smith'},
                  'jobs': ['dev', 'mgr'],
                  'age': 40.5}
        assert record['name'] == {'last': 'Smith', 'first': 'Bob'}
        assert record['name']['last'] == 'Smith'
        assert record['jobs'][-1] == 'mgr'

    def test_nesting_operations(self):
        record = {'name': {'first': 'Bob', 'last': 'Smith'},
                  'jobs': ['dev', 'mgr'],
                  'age': 40.5}
        record['jobs'].append('janitor')
        assert record['jobs'][-1] == 'janitor'

    def test_missing_key(self):
        items = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
        assert not ('job' in items)

    def test_default_value(self):
        items = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
        value = items.get('age', 20)
        assert value == 20

    def test_default_value_expression(self):
        items = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
        value = items['age'] if 'age' in items else 20
        assert value == 20

    def test_sorted_keys(self):
        items = {'a': 1, 'c': 3, 'b': 2}
        # Remember order is not guaranteed. 'sorted' -> Python 3.X
        expected_value = 1
        for key in sorted(items):
            # Don't use testing with assertions in loops and stuff like that,
            # this is just for the shake of this example
            assert items[key] == expected_value
            expected_value += 1


# Note
# Object's space is reclaimed, all of the memory space occupied by that object’s structure
# is automatically cleaned up for us (garbage collection):
# >>> record = 0