import math
import random


class TestNumbers:
    def test_addition(self):
        assert 123 + 222 == 345

    def test_floating_point_multiplication(self):
        assert 1.5 * 4 == 6.0

    def test_power(self):
        assert 2 ** 100 == 1267650600228229401496703205376
        # Python 3.X’s integer type automatically provides extra precision for large numbers like this when needed (in
        # 2.X, a separate long integer type handles numbers too large for the normal integer type in similar ways)

    def test_floating_point_repr(self):
        assert 3.1415 * 2 == 6.2830000000000004
        # This isn’t a bug; this is in the very nature of binary floating-point.
        # For user-friendly representation: print(3.1415 * 2) == 6.283
        # See https://docs.python.org/3.0/tutorial/floatingpoint.html for the issues and limitations

    def test_math_pi(self):
        assert math.pi == 3.141592653589793

    def test_math_sqrt(self):
        assert math.sqrt(85) == 9.219544457292887

    def test_random_real_value_distribution(self):
        random_number = random.random()
        assert random_number < 1.0
        assert random_number > 0.0
        # Return the next random floating point number in the range [0.0, 1.0).
        # https://docs.python.org/3/library/random.html

    def test_random_choice(self):
        domain = [1, 2, 3, 4]
        random_choice = random.choice(domain)
        assert random_choice in domain
