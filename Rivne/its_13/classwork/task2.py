import pytest


def divide(num_1, num_2):
    return float(num_1)/num_2


class TestDiv:

    def test_1(self):
        with pytest.raises(ZeroDivisionError) as e_info:
            divide(1, 0)

    def test_2(self):
        with pytest.raises(TypeError) as e_info:
            divide(1, '0')

    def test_3(self):
        assert divide(2, 5) == 0.4


# print(divide(2, 0))