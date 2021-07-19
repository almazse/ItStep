import math
import pytest


def quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    if a == 0 or b == 0 or c == 0:
        raise ValueError
    if d < 0:
        return None
    elif d == 0:
        root_1 = (-b + math.sqrt(d)) / (2 * a)
        return root_1
    else:
        root_1 = (-b + math.sqrt(d)) / (2 * a)
        root_2 = (-b - math.sqrt(d)) / (2 * a)
        return root_1, root_2


class TestClass:

    def test_1(self):
        assert quadratic_equation(2, 1, -1) == (0.5, -1.0)

    def test_2(self):
        assert quadratic_equation(1, -4, 4) == 2.0

    def test_3(self):
        assert quadratic_equation(4, 1, 2) is None

    def test_4(self):
        with pytest.raises(ValueError):
            quadratic_equation(0, 0, 0)
