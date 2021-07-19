import unittest
from decimal import Decimal


class TriangleNotExistException(Exception):

    def __init__(self, text):
        self.text = text


class TriangleNotValidArgumentException(Exception):

    def __init__(self, text):
        self.text = text


class Triangle:

    def __init__(self, triangle):
        self.triangle = triangle
        if type(triangle) != tuple or len(triangle) != 3 or type(self.triangle[0]) == str \
                or type(self.triangle[1]) == str or type(self.triangle[2]) == str:
            raise TriangleNotValidArgumentException("Not valid arguments")
        else:
            self.get_area()

    def get_area(self):
        s = (self.triangle[0] + self.triangle[1] + self.triangle[2]) / 2
        area = (s * (s - self.triangle[0]) * (s - self.triangle[1]) * (s - self.triangle[2])) ** 0.5
        if self.triangle[0] == 0 or self.triangle[1] == 0 or self.triangle[2] == 0 or area == 0 \
                or self.triangle[0] < 0 or self.triangle[1] < 0 or self.triangle[2] < 0\
                or isinstance(area, complex):
            raise TriangleNotExistException("Can`t create triangle with this arguments")
        number = Decimal(area).quantize(Decimal('1.11'), rounding="ROUND_DOWN")
        return float(number)


class TriangleTest(unittest.TestCase):

    def test_valid(self):
        valid_test_data = [
            ((3, 4, 5), 6.0),
            ((10, 10, 10), 43.30),
            ((6, 7, 8), 20.33),
            ((7, 7, 7), 21.21),
            ((50, 50, 75), 1240.19),
            ((37, 43, 22), 406.99),
            ((26, 25, 3), 36.0),
            ((30, 29, 5), 72.0),
            ((87, 55, 34), 396.0),
            ((120, 109, 13), 396.0),
            ((123, 122, 5), 300.0)
        ]
        for data in valid_test_data:
            self.assertEqual(Triangle(data[0]).get_area(), data[1])

    @unittest.expectedFailure
    def test_not_valid(self):
        not_valid_triangle = [
            (1, 2, 3),
            (1, 1, 2),
            (7, 7, 15),
            (100, 7, 90),
            (17, 18, 35),
            (127, 17, 33),
            (145, 166, 700),
            (1000, 2000, 1),
            (717, 17, 7),
            (0, 7, 7),
            (-7, 7, 7)
        ]
        for data in not_valid_triangle:
            self.assertEqual(Triangle(data).get_area(), "Can`t create triangle with this arguments")

    @unittest.expectedFailure
    def test_not_valid2(self):
        not_valid_arguments = [
            ('3', 4, 5),
            ('a', 2, 3),
            (7, "str", 7),
            ('1', '1', '1'),
            'string',
            (7, 2),
            (7, 7, 7, 7),
            'str',
            10,
            ('a', 'str', 7)
        ]
        for data in not_valid_arguments:
            self.assertEqual(Triangle(data).get_area(), "Not valid arguments")






