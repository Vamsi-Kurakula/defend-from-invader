'''
Driver file for analyzing strategies if 
there is one player in each side of the tripartite
'''

import random
from Classes.InvaderGamePayoffMatrix import InvaderGamePayoffMatrix
from Classes.PlayerInformation import PlayerInformation

# Human Focused Variables
VALUE = 10 # Resource gain
COST = 5 # Cost of Self Interest
SYNERGY = 1.5 # Synergy Factor

# Invader Focused Variables
DAMAGE = 20 # Damage from Invader
ATTACK = 2 # Cost of Attacking from Invader

# Simulation settings  
ROUNDS = 20
human_1 = PlayerInformation(name='Human_1', action_set=['c', 's'], strategy=[50,50])
human_2 = PlayerInformation(name='Human_2', action_set=['c', 's'], strategy=[50,50])
invader = PlayerInformation(name='Invader', action_set=['p', 'a'], strategy=[50,50])

# Create and initalize game
game = InvaderGamePayoffMatrix(VALUE, COST, SYNERGY, DAMAGE, ATTACK)
game.update_game()

for i_round in range(ROUNDS):
    
    print(game.get_payoffs(human_1.get_action(),
                           human_2.get_action(),
                           invader.get_action()))

#game.print_gamestate()