from abc import ABC, abstractmethod


class BaseView(ABC):

    @staticmethod
    @abstractmethod
    def greet_the_game():
        """ Lest start the game! """

    @staticmethod
    @abstractmethod
    def series_number(series):
        """ Return bet series number """

    @staticmethod
    @abstractmethod
    def win_number(number):
        """ Win number of the pull """

    @staticmethod
    @abstractmethod
    def get_player_name(number):
        """ Returns player name """

    @staticmethod
    @abstractmethod
    def get_bet_money_by_player(name):
        """ Return bet money by player """

    @staticmethod
    @abstractmethod
    def get_bet_value_by_player(name):
        """ Return bet number value by player """

    @staticmethod
    @abstractmethod
    def winner_bet_message(name):
        """ Winner bet message """

    @staticmethod
    @abstractmethod
    def winner_game_message(name):
        """ Winner game message """
