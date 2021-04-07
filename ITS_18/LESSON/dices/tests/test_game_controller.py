from unittest import mock

from ITS_18.LESSON.dices.views.base_view import BaseView
from ITS_18.LESSON.dices.views.console_view import ConsoleView
from ITS_18.LESSON.dices.controllers.game import DiceGame
from ITS_18.LESSON.dices.models.dice import Dice
from ITS_18.LESSON.dices.models.player import Player


class TestDiceGame:

    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.get_player_name')
    def test_game_init_success(self, get_player_name_mock):
        dice_game = DiceGame(2)
        get_player_name_mock.return_value = 'Test'

        assert isinstance(dice_game, DiceGame)
        assert dice_game._number_of_players == 2
        assert all((isinstance(player, Player) for player in dice_game._players))
        assert dice_game._players[0]._score == 100
        assert dice_game._players[1]._score == 100
        assert isinstance(dice_game.view, BaseView)
        assert isinstance(dice_game.view, ConsoleView)
        assert isinstance(dice_game.dice, Dice)

    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.get_player_name')
    def test_game_is_enough_false(self, get_player_name_mock):
        dice_game = DiceGame(2)
        get_player_name_mock.return_value = 'Test'

        assert dice_game._is_enough() is False

    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.get_player_name')
    def test_game_is_enough_true(self, get_player_name_mock):
        dice_game = DiceGame(2)
        get_player_name_mock.return_value = 'Test'
        dice_game._players[0]._score = 0

        assert dice_game._is_enough() is True

    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.get_player_name')
    def test_game_is_enough_true_score_negative(self, get_player_name_mock):
        dice_game = DiceGame(2)
        get_player_name_mock.return_value = 'Test'
        dice_game._players[0]._score = -15

        assert dice_game._is_enough() is True

    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.get_player_name')
    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.winner_bet_message')
    def test_game_count_players_one_winner(self, get_player_name_mock,
                                           winner_bet_message_mock):
        dice_game = DiceGame(2)
        win_number = 3
        get_player_name_mock.return_value = 'Test'
        dice_game._players[0]._number = 3
        dice_game._players[0].set_money(12)
        dice_game._players[1]._number = 1
        dice_game._players[1].set_money(100)

        dice_game._count_players(win_number)
        assert dice_game._players[0]._score == 100 + 12 * 6
        assert dice_game._players[1]._score == 100 - 100
        assert dice_game._players[0]._money == 12
        assert dice_game._players[1]._money == 100

    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.get_player_name')
    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.winner_bet_message')
    def test_game_count_players_two_winners(self, get_player_name_mock,
                                           winner_bet_message_mock):
        dice_game = DiceGame(2)
        win_number = 3
        get_player_name_mock.return_value = 'Test'
        dice_game._players[0]._number = 3
        dice_game._players[0].set_money(12)
        dice_game._players[1]._number = 3
        dice_game._players[1].set_money(100)

        dice_game._count_players(win_number)
        assert dice_game._players[0]._score == 100 + 12 * 6
        assert dice_game._players[1]._score == 100 + 100 * 6
        assert dice_game._players[0]._money == 12
        assert dice_game._players[1]._money == 100

    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.get_player_name')
    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.winner_bet_message')
    def test_game_count_players_no_winners(self, get_player_name_mock,
                                           winner_bet_message_mock):
        dice_game = DiceGame(2)
        win_number = 13
        get_player_name_mock.return_value = 'Test'
        dice_game._players[0]._number = 3
        dice_game._players[0].set_money(12)
        dice_game._players[1]._number = 3
        dice_game._players[1].set_money(100)
        dice_game._players[1].set_money(100)

        dice_game._count_players(win_number)
        assert dice_game._players[0]._score == 100 - 12
        assert dice_game._players[1]._score == 100 - 100
        assert dice_game._players[0]._money == 12
        assert dice_game._players[1]._money == 100

    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.get_player_name')
    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.get_bet_money_by_player')
    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.get_bet_value_by_player')
    def test_game_ask_bets_valid_params(self,
                                                get_bet_value_by_player_mock,
                                                get_bet_money_by_player_mock,
                                                get_player_name_mock):
        dice_game = DiceGame(2)
        get_player_name_mock.return_value = 'Test'
        get_bet_value_by_player_mock.return_value = 1
        get_bet_money_by_player_mock.return_value = 20
        dice_game.ask_bets()

        assert dice_game._players[0]._number == 1
        assert dice_game._players[1]._number == 1
        assert dice_game._players[0]._money == 20
        assert dice_game._players[1]._money == 20

    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.get_player_name')
    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.get_bet_money_by_player')
    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.get_bet_value_by_player')
    def test_game_ask_bets_invalid_params(self,
                                                get_bet_value_by_player_mock,
                                                get_bet_money_by_player_mock,
                                                get_player_name_mock):
        dice_game = DiceGame(2)
        get_player_name_mock.return_value = 'Test'
        get_bet_value_by_player_mock.return_value = 99
        get_bet_money_by_player_mock.return_value = 20
        dice_game.ask_bets()

        assert dice_game._players[0]._number == 6
        assert dice_game._players[1]._number == 6
        assert dice_game._players[0]._money == 20
        assert dice_game._players[1]._money == 20

    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.get_player_name')
    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.get_bet_money_by_player')
    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.get_bet_value_by_player')
    def test_game_ask_bets_invalid_bet(self,
                                                get_bet_value_by_player_mock,
                                                get_bet_money_by_player_mock,
                                                get_player_name_mock):
        dice_game = DiceGame(2)
        get_player_name_mock.return_value = 'Test'
        get_bet_value_by_player_mock.return_value = 1
        get_bet_money_by_player_mock.return_value = 220
        dice_game.ask_bets()

        assert dice_game._players[0]._number == 1
        assert dice_game._players[1]._number == 1
        assert dice_game._players[0]._money == 100
        assert dice_game._players[1]._money == 100

    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.get_player_name')
    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.get_bet_money_by_player')
    @mock.patch('ITS_18.LESSON.dices.views.console_view.ConsoleView.get_bet_value_by_player')
    def test_game_ask_bets_invalid_money(self,
                                                get_bet_value_by_player_mock,
                                                get_bet_money_by_player_mock,
                                                get_player_name_mock):
        dice_game = DiceGame(2)
        get_player_name_mock.return_value = 'Test'
        get_bet_value_by_player_mock.return_value = 1
        get_bet_money_by_player_mock.return_value = -20
        dice_game.ask_bets()

        assert dice_game._players[0]._number == 1
        assert dice_game._players[1]._number == 1
        assert dice_game._players[0]._money == 100
        assert dice_game._players[1]._money == 100
