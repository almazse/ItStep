import pytest
from airplane import *


def test_airplane_equality():
    boeing = Airplane('Boeing', 500)
    airbus = Airplane('Airbus', 100)
    assert (boeing == airbus) == "These planes are different"


def test_airplane_greater_than_or_equal_to_1():
    boeing = Airplane('Boeing', 500)
    super_jet = Airplane('Superjet', 100)
    assert (boeing >= super_jet) == "Boeing (500) it has more passengers than Superjet (100)"


def test_airplane_greater_than_or_equal_to_2():
    boeing = Airplane('Boeing', 500)
    super_jet = Airplane('Superjet', 100)
    assert (boeing <= super_jet) == "Superjet (100) has fewer passengers than Boeing (500)"


def test_airplane_greater_than_or_equal_to_3():
    super_jet = Airplane('Superjet', 100)
    airbus = Airplane('Airbus', 100)
    assert (super_jet >= airbus) == "Superjet (100) has as many passengers as Airbus (100)"


def test_airplane_inequality_1():
    boeing = Airplane('Boeing', 500)
    super_jet = Airplane('Superjet', 100)
    assert (super_jet > boeing) == "Superjet (100) has fewer passengers than Boeing (500)"


def test_airplane_inequality_2():
    boeing = Airplane('Boeing', 500)
    super_jet = Airplane('Superjet', 100)
    assert (super_jet < boeing) == "Boeing (500) it has more passengers than Superjet (100)"


def test_airplane_addition_1():
    boeing = Airplane('Boeing', 500)
    assert (boeing + 25) == "Now the capacity in the cabin: 525 passagers"


def test_airplane_addition_2():
    super_jet = Airplane('Superjet', 100)
    assert (super_jet - 25) == "Now the capacity in the cabin: 75 passagers"


def test_airplane_additon_assigment_1():
    boeing = Airplane('Boeing', 500)
    boeing += 100
    assert boeing == "Now the capacity in the cabin: 600 passagers"


def test_airplane_additon_assigment_2():
    super_jet = Airplane('Superjet', 100)
    super_jet -= 20
    assert super_jet == "Now the capacity in the cabin: 80 passagers"


