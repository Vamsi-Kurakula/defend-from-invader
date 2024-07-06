import pandas as pd
from tabulate import tabulate

class InvaderGame:
    def __init__(self, V, C, D):
        """
        Initializes a Tripartitite Invader Game 
    
        Args:
            V (int): Resource Gain
            C (int): Cost of Self Interest
            D (int): Damage from Invader
        """
        self.V = V
        self.C = C
        self.D = D
        self.Time = 0
        self.Game = {}

    def updateGame(self):
        """
        # Updates game given current state of variables 
        """        
        # Invader being Passive
        self.Game['c-c-p'] = [self.V / 2, self.V / 2, -1 * self.V]
        self.Game['c-d-p'] = [-self.D, self.V - self.D, -1 * (self.V - (2* self.D))]
        self.Game['d-c-p'] = [self.V - self.D, -self.D, -1 * (self.V - (2* self.D))]
        self.Game['d-d-p'] = [self.V/2 - self.C - self.D, self.V/2 - self.C - self.D, -1 *(self.V - (2* self.C) - (2*self.D))]

        # Invader being Active
        self.Game['c-c-a'] = [self.V / 2, self.V / 2, -1 * self.V]
        self.Game['c-d-a'] = [-self.D, self.V - self.D, -1 * (self.V - (2* self.D))]
        self.Game['d-c-a'] = [self.V - self.D, -self.D, -1 * (self.V - (2* self.D))]
        self.Game['d-d-a'] = [self.V/2 - self.C - self.D, self.V/2 - self.C - self.D, -1 *(self.V - (2* self.C) - (2*self.D))]

        return

    def __repr__(self):

        data = [
            ["Invader", "", "", "", ""],
            ["", "Passive", "", "Aggressive", ""],
            ["Human 1/ Human 2", "Collaborate", "Self-Interest", "Collaborate", "Self-Interest"],
            ["Collaborate", self.Game['c-c-p'], self.Game['c-d-p'], self.Game['c-c-a'], self.Game['c-d-a']],
            ["Self-Interest", self.Game['d-c-p'], self.Game['d-d-p'], self.Game['d-c-a'], self.Game['d-d-a']]
        ]

        # Create a DataFrame
        df = pd.DataFrame(data)
        
        return tabulate(df.values, tablefmt="grid", stralign='center')