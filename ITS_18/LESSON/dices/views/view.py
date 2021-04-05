class ConsoleView:

    @staticmethod
    def greet_the_game():
        print('Lest start the game!')

    @staticmethod
    def series_number(series):
        print(f'Bets series is #{series}')

    @staticmethod
    def win_number(number):
        print(f'Pulled number is: {number}')

    @staticmethod
    def get_player_name(number):
        return str(input(f'Enter name of the player #{number}: '))

    @staticmethod
    def get_bet_money_by_player(name):
        return int(input(f'Player #{name} bets money ($): '))

    @staticmethod
    def get_bet_value_by_player(name):
        return int(input(f'Player #{name} bets on number: '))

    @staticmethod
    def winner_bet_message(name):
        print(f'Player {name} won bet!')

    @staticmethod
    def winner_game_message(name):
        print(f'Player {name} won the game')
