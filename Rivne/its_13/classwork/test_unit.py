import unittest
from app import square


class TestClass(unittest.TestCase):

    def test_1(self):
        self.assertEqual(square(1, -7, 10), (5.0, 2.0))

    def test_2(self):
        self.assertEqual(square(1, 7, 10), (-2.0, -5.0))