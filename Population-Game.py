'''
Driver file for population dynamics in the tripartite game
'''

import random
import matplotlib.pyplot as plt
from Classes.InvaderGamePayoffMatrix import InvaderGamePayoffMatrix
from Classes.PlayerInformation import PlayerInformation

# Human Focused Variables
VALUE = 15 # Resource gain
COST = 10 # Cost of Self Interest
SYNERGY = 1.5 # Synergy Factor

# Invader Focused Variables
DAMAGE = 20 # Damage from Invader
ATTACK = 5 # Cost of Attacking from Invader

# Inital Populaiton Distributions
HUMAN_COLLABORATE = 40
HUMAN_SELF_INTERESTED = 10
INVADER_PASSIVE = 20
INVADER_ACTIVE = 30


def get_rep_dynamics(pop, game):

    # Human Average Fitness
    h_c = ((pop[0]*pop[2]*game.game['c-c-p'][0]) + 
           (pop[0]*pop[3]*game.game['c-c-a'][0]) + 
           (pop[1]*pop[2]*game.game['c-s-p'][0]) + 
           (pop[1]*pop[3]*game.game['c-s-a'][0]))
    h_s = ((pop[0]*pop[2]*game.game['s-c-p'][0]) + 
           (pop[0]*pop[3]*game.game['s-c-a'][0]) + 
           (pop[1]*pop[2]*game.game['s-s-p'][0]) + 
           (pop[1]*pop[3]*game.game['s-s-a'][0]))
    
    # Invader Average Fitness
    i_p = ((pop[0]*pop[0]*game.game['c-c-p'][2]) + 
           (pop[0]*pop[1]*game.game['c-s-p'][2]) + 
           (pop[1]*pop[0]*game.game['s-c-p'][2]) + 
           (pop[1]*pop[1]*game.game['s-s-p'][2]))
    i_a = ((pop[0]*pop[0]*game.game['c-c-a'][2]) + 
           (pop[0]*pop[1]*game.game['c-s-a'][2]) + 
           (pop[1]*pop[0]*game.game['s-c-a'][2]) + 
           (pop[1]*pop[1]*game.game['s-s-a'][2]))
    
    phi = (pop[0]*h_c) + (pop[1]*h_s) + (pop[2]*i_p) + (pop[3]*i_a)

    replicator_dynamics = {'h_c':pop[0]*(h_c - phi), 
                           'h_s':pop[1]*(h_s - phi),
                           'i_p':pop[2]*(i_p - phi),
                           'i_a':pop[3]*(i_a - phi)}

    return replicator_dynamics

def main():

    # Create and initalize game
    game = InvaderGamePayoffMatrix(VALUE, COST, SYNERGY, DAMAGE, ATTACK)
    game.update_game()

    # Get population distributions 
    population = [HUMAN_COLLABORATE, HUMAN_SELF_INTERESTED, INVADER_PASSIVE, INVADER_ACTIVE]
    population = [x/sum(population) for x in population]

    # Get replication dynamics
    changes = get_rep_dynamics(population, game)

    game.print_gamestate()
    print(population)
    print(changes)

if __name__ == '__main__':
    main()