import pytest
from app import square


class TestClass:

    def test_1(self):
        assert square(1, -7, 10) == (5.0, 2.0)

    def test_2(self):
        assert square(1, 7, 10) == (-2.0, -5.0)
