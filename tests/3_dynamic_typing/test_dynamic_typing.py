class TestDynamicTyping:
    def test_shared_reference_assignment(self):
        a = 3
        b = a
        # b in this case is not linked to a but references the same object (also called shared object):
        #   `Name` a references `Object` 3
        #   `Name` b references `Object` 3
        assert a == 3
        assert b == 3
        a = 'spam'
        assert a == 'spam'
        # Now a references to another object. 3 is not longer a shared reference
        assert b == 3

    def test_shared_reference_assigment_operation(self):
        a = 3
        b = a
        # The operation results in a different Object (ints are immutable, cannot be change in place)
        # Setting a variable to a new value does not alter the original object just creates new objects and creates
        # new references to them
        a = a + 2
        assert a == 5
        assert b == 3

    def test_shared_reference_in_place_changes(self):
        l1 = [2, 3, 4]
        l2 = l1
        l1[0] = 24
        assert l2[0] == 24
        # If instead we assign l1 to a different object then l2 still references to the list (as previous test)
        # There are objects and operations that perform in-place object changes—Python’s mutable types,
        # including lists, dictionaries, and sets.

    def test_shared_reference_avoid_in_place_changes(self):
        l1 = [2, 3, 4]
        l2 = l1[:]
        # Copy
        l1[0] = 24
        assert l2[0] == 2
        # To copy a dictionary or set, instead use X.copy() or X.deepcopy() method calls
        # (lists have one as of Python 3.3), or pass the original object to their type names, dict and set

    def test_shared_reference_equality(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        c = a
        assert a == c
        assert a == b
        # a and c same reference
        assert a is c
        # a and b same value but different reference
        assert not (a is b)

    def test_shared_reference_catching(self):
        a = 42
        b = 42
        assert a == b
        assert a is b
        # Same object as 42 is cached. small integers and strings are cached and reused
        # Get reference count. >>> sys.getrefcount(1)

# Notes:
# Further reading -> "weak references" https://docs.python.org/3/library/weakref.html
