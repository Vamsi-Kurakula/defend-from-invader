'''
Main driver file for repository
'''

from Classes.InvaderGamePayoffMatrix import InvaderGamePayoffMatrix

# Human Focused Variables
V = 10 # Resource gain
C = 5 # Cost of Self Interest
S = 1.5 # Synergy Factor

# Invader Focused Variables
A = 2 # Cost of Attacking from Invader
D = 20 # Damage from Invader

vamsi = InvaderGamePayoffMatrix(V, C, S, D, A)
vamsi.updateGame()

print(vamsi)
