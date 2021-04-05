import pytest
from circle import *

circle1 = Circle(7)
circle2 = Circle(30)
circle3 = Circle(22)
circle4 = Circle(22)


def test_cirlce_equality():
    assert circle4 == circle3


def test_cirlce_inequality():
    assert circle1 < circle2


def test_cirlce_greater_than_or_equal_to():
    assert circle3 <= circle4


def test_cirlce_adding():
    assert circle1 + circle2 == 37


def test_cirlce_subtracting():
    assert circle2 - circle3 == 8

