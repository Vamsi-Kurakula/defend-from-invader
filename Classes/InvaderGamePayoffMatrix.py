import pandas as pd
from tabulate import tabulate

class InvaderGamePayoffMatrix:
    def __init__(self, V, C, S, D, A):
        """
        Initializes a Tripartitite Invader Game 
    
        Args:
            V (int): Resource Gain
            C (int): Cost of Self Interest
            C (int): Synergy Factor
            D (int): Damage from Invader
            A (int): Cost of attacking from Invaders
        """
        self.value = V
        self.cost = C
        self.synergy = S
        self.damage = D
        self.attack = A
        self.block = D/2 #Damaged in a blocked attack
        self.time = 0
        self.game = {}

    def update_game(self):
        """
        # Updates game given current state of variables 
        """
        # Invader being Passive
        self.game['c-c-p'] = [self.value / 2 * self.synergy, # Human 1
                              self.value / 2 * self.synergy, # Human 2
                              -1 * (self.value *self.synergy)] # Invader
        self.game['c-s-p'] = [0,
                              self.value,
                              -1 * (self.value)]
        self.game['s-c-p'] = [self.value,
                              0,
                              -1 * (self.value)]
        self.game['s-s-p'] = [(self.value - self.cost)/2,
                              (self.value - self.cost)/2,
                              -1 *(self.value - self.cost)]

        # Invader being Active
        self.game['c-c-a'] = [(self.value/2* self.synergy)-self.block,
                              (self.value/2*self.synergy)-self.block,
                              -1 * ((self.value * self.synergy) - (2*self.block)+ self.attack) ]
        self.game['c-s-a'] = [-self.damage,
                              self.value - self.damage,
                              -1 * (self.value - (2* self.damage)  + self.attack)]
        self.game['s-c-a'] = [self.value - self.damage,
                              -self.damage,
                              -1 * (self.value - (2* self.damage) + self.attack)]
        self.game['s-s-a'] = [self.value/2 - self.cost - self.damage,
                              self.value/2 - self.cost - self.damage,
                              -1 *(self.value - (2* self.cost) - (2*self.damage)  + self.attack)]

    def __repr__(self):

        data = [
            ["Invader", "", "", "", ""],
            ["", "Passive", "", "Aggressive", ""],
            ["Human 1/ Human 2", "Collaborate", "Self-Interest", "Collaborate", "Self-Interest"],
            ["Collaborate", self.game['c-c-p'], self.game['c-s-p'], self.game['c-c-a'], self.game['c-s-a']],
            ["Self-Interest", self.game['s-c-p'], self.game['s-s-p'], self.game['s-c-a'], self.game['s-s-a']]
        ]

        # Create a DataFrame
        df = pd.DataFrame(data)

        return tabulate(df.values, tablefmt="grid", stralign='center')
