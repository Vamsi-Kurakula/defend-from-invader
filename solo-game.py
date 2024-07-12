'''
Driver file for analyzing strategies if 
there is one player in each side of the tripartite
'''

from Classes.InvaderGamePayoffMatrix import InvaderGamePayoffMatrix

# Human Focused Variables
V = 10 # Resource gain
C = 5 # Cost of Self Interest
S = 1.5 # Synergy Factor

# Invader Focused Variables
A = 2 # Cost of Attacking from Invader
D = 20 # Damage from Invader

game = InvaderGamePayoffMatrix(V, C, S, D, A)
game.update_game()

game.print_gamestate()