import os

ERR_MSG = {
    'mode': 'It was put not correct mode! There are only "Moskow" '
            'and "Piter"',
    'ticket': 'Size one of the '
              'ticket not equal 6 or there were put not digits!',
    'file': 'Such file doesn\'t exist!'
}


def get_tickets_from_file() -> list:
    filepath = input('Enter filename: ')
    tickets_list = []
    if not os.path.isfile(filepath):
        raise FileNotFoundError(ERR_MSG['file'])
    with open(filepath, 'r', encoding='utf-8') as f:
        for string in f:
            tickets_list.append(string.strip())
    return tickets_list


class TicketHappyMoskowMixin:
    @staticmethod
    def is_happy_ticket_by_moskow(ticket):
        first_part = [int(d) for d in ticket[:3]]
        second_part = [int(d) for d in ticket[3:]]
        if sum(first_part) == sum(second_part):
            return True
        return False


class TicketHappyPiterMixin:
    @staticmethod
    def is_happy_ticket_by_piter(ticket):
        even_digits = sum([int(d) for d in ticket if int(d) % 2 == 0])
        odd_digits = sum([int(d) for d in ticket if int(d) % 2 == 1])
        if even_digits == odd_digits:
            return True
        return False


class TicketsCheckHappy(TicketHappyMoskowMixin,
                       TicketHappyPiterMixin):

    def __init__(self, tickets, mode):
        self._MODES = {
            'moskow': self.is_happy_ticket_by_moskow,
            'piter': self.is_happy_ticket_by_piter
        }
        self.tickets = tickets

    @property
    def mode(self):
        return self.mode

    @mode.setter
    def mode(self, value):
        if str(value).lower() not in self.MODES.keys():
            raise KeyError
        self._mode = value
