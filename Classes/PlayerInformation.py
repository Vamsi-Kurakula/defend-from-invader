import random

class PlayerInformation():

    def __init__(self, name, action_set, strategy):
        self.name = name
        self.action_set = action_set
        self.strategy = strategy
        self.total_payoff = 0

    def get_action(self):
        '''
        Given an action set and strategy, get a action
        '''

        return random.choices(population=self.action_set, weights=[self.strategy, 1-self.strategy])[0]

    def update_payoff(self, my_payoff):
        '''
        Updates total payoff gained during game
        '''
        self.total_payoff += my_payoff

    def update_strategy(self, my_payoff, game_payoff):
        
        if my_payoff >=0:
            self.strategy += .1
        else: 
            self.strategy -= .1

        # Make sure we bound the strategy between 0 and 1
        self.strategy = min([1, self.strategy])
        self.strategy = max([0, self.strategy])