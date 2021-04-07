from ITS_18.LESSON.dices.models.player import Player
from pytest import raises


class TestPlayerModel:

    def test_player_success_init(self):
        player = Player('Test', 100)

        assert isinstance(player, Player)
        assert player._name == 'Test'
        assert player._score == 100
        assert player._number == 0
        assert player._money == 0

    def test_player_fail_init(self):
        with raises(TypeError):
            player = Player(100, 'Test', 100)

    def test_player_set_money_success(self):
        player = Player('Test', 100)
        player.set_money(500)
        assert player._money == 500

    def test_player_set_number_success(self):
        player = Player('Test', 100)
        player.set_number(5)
        assert player._number == 5

    def test_player_win_bet_success(self):
        player = Player('Test', 100)
        player.win_bet()
        assert player._score == 100

    def test_player_win_bet_success_changed_money(self):
        player = Player('Test', 100)
        player.set_money(50)
        player.win_bet()
        assert player._score == 400

    def test_player_lose_bet_success(self):
        player = Player('Test', 100)
        player.lose_bet()
        assert player._score == 100

    def test_player_lose_bet_success_money_changed(self):
        player = Player('Test', 100)
        player.set_money(250)
        player.lose_bet()
        assert player._score == -150
