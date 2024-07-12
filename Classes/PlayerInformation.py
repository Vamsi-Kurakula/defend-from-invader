import random

class PlayerInformation():

    def __init__(self, name, action_set, strategy):
        self.name = name
        self.action_set = action_set
        self.strategy = strategy

    def get_action(self):
        '''
        Given an action set and strategy, get a action
        '''

        return random.choices(population=self.action_set, weights=self.strategy)[0]