from Classes.InvaderGame import InvaderGame


V = 10 # Resource gain 
C = 5 # Cost of Self Interest
D = 100 # Damage from Invader


vamsi = InvaderGame(V, C, D)
vamsi.updateGame()

print(vamsi)