"""
MVC
model: Player, Dice
view: ConsoleView
controller: Game
"""

from ITS_18.LESSON.dices.controllers.game import DiceGame

game = DiceGame(2)
game.start()