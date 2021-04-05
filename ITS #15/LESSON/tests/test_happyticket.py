import pytest
from ..ticketscheckhappy import *


def test_peter_ticket_success():
    is_piter_happy = TicketsCheckHappy.is_happy_ticket_by_piter('121358')
    assert is_piter_happy is True


def test_peter_ticket_fail():
    is_piter_happy = TicketsCheckHappy.is_happy_ticket_by_piter('278561')
    assert is_piter_happy is False

def test_peter_check():
    peter_tickets = TicketsCheckHappy(['', '111111'], 'PiTer')

def test_invalid_mode():
    with pytest.raises(KeyError):
        TicketsCheckHappy(['253145', '111111'], 'Mockow')

def test_invalid_tickets():
    with pytest.raises(ValueError):
        TicketsCheckHappy(['asdaw', 121213], 'Moskow')


def test_valid_tickets_from_file():
    with mock.path.object(__builtins__, 'input', lambda: 'tickets.txt'):
        tickets_list = get_tickets_from_file()
    moskow_tickets = TicketsCheckHappy(['253145', '111111'], 'Moskow')
    assert str(moskow_tickets.count_happy_tickets())