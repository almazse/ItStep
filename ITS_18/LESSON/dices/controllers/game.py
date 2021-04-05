from ITS_18.LESSON.dices.views.view import ConsoleView
from ITS_18.LESSON.dices.models.dice import Dice
from ITS_18.LESSON.dices.models.player import Player


class DiceGame:

    def __init__(self, number_of_players):
        self._players = self.create_players()
        self._number_of_players = number_of_players
        self.view = ConsoleView()
        self.dice = Dice()

    def start(self):
        self.view.greet_the_game()  # greeting message
        counter = 1
        while True:
            self.view.series_number(counter)  # series number message
            counter += 1
            self.ask_bets()
            win_number = self.dice.get_win_number()
            self.view.win_number(win_number)  # win number message
            self._count_players(win_number)
            if self._is_enough():
                break
        self._show_winner()

    def _show_winner(self):
        winner = sorted(self._players, key=lambda x: -x._score)[0]
        self.view.winner_game_message(winner._name)

    def _is_enough(self):
        return any([player._score for player in self._players])

    def _count_players(self, win_number):
        for player in self._players:
            if player._number == win_number:
                player.win_bet()
                self.view.winner_bet_message(player._name)
            else:
                player.lose_bet()

    def ask_bets(self):
        for player in self._players:
            money = self.view.get_bet_money_by_player(player._name)
            number = self.view.get_bet_value_by_player(player._name)
            if money <= player._score:
                player.set_money(money)
            else:
                player.set_money(player._score)
            if number in [1, 2, 3, 4, 5, 6]:
                player.set_number(number)
            else:
                player.set_number(6)

    def create_players(self):
        players = []
        for i in range(self._number_of_players):
            name = self.view.get_player_name(i)
            players.append(Player(name=name, score=100))
        return players
