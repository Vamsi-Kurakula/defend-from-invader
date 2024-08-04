'''
Module to do quick tests on different game matrix states 
'''
from Classes.InvaderGamePayoffMatrix import InvaderGamePayoffMatrix


# Human Focused Variables
VALUE = 10 # Resource gain
COST = 15 # Cost of Self Interest
SYNERGY = 1.5 # Synergy Factor

# Invader Focused Variables
DAMAGE = 5  # Damage from Invader
ATTACK = 10 # Cost of Attacking from Invader
BLOCK = 4 # Blocked Damage

game = InvaderGamePayoffMatrix(VALUE, COST, SYNERGY, DAMAGE, ATTACK, BLOCK)
game.update_game()
game.print_gamestate()