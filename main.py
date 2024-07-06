from Classes.InvaderGamePayoffMatrix import InvaderGamePayoffMatrix


V = 10 # Resource gain 
C = 5 # Cost of Self Interest
D = 100 # Damage from Invader


vamsi = InvaderGamePayoffMatrix(V, C, D)
vamsi.updateGame()

print(vamsi)