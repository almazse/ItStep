class Player:
    def __init__(self, name, score):
        self._name = name
        self._score = score
        self._number = 0
        self._money = 0

    def set_money(self, money):
        self._money = money

    def set_number(self, number):
        self._number = number

    def win_bet(self):
        self._score += self._money * 6

    def lose_bet(self):
        self._score -= self._money