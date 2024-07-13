import random

class PlayerInformation():

    def __init__(self, name, action_set, strategy):
        self.name = name
        self.action_set = action_set
        self.strategy = strategy
        self.total_payoff = 0
        self.strategy_history = []

    def get_action(self):
        '''
        Given an action set and strategy, get a action
        '''

        self.current_action = random.choices(population=self.action_set, weights=[self.strategy, 1-self.strategy])[0]
        self.alt_action = [item for item in self.action_set if item != self.current_action][0]

    def update_payoff(self, my_payoff):
        '''
        Updates total payoff gained during game
        '''
        self.total_payoff += my_payoff

    def update_strategy(self, my_payoff, alt_payoff):
        
        factor = 1 if self.current_action == self.action_set[0] else -1
        
        if my_payoff >= alt_payoff:
            self.strategy += .001 * factor
        else: 
            self.strategy -= .001 * factor

        # Make sure we bound the strategy between 0 and 1
        self.strategy = min([1, self.strategy])
        self.strategy = max([0, self.strategy])

        # Storing history of strategy 
        self.strategy_history.append(self.strategy)