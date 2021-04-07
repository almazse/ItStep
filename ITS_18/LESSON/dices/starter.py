"""
MVC
model: Player, Dice
view: ConsoleView
controller: Game
"""

from controllers.game import DiceGame

game = DiceGame(2)
game.start()