"""
MVC
model: Player, Dice
view: ConsoleView
controller: Game
"""

from controllers.game import LifeGame

game = LifeGame()
game.start()
