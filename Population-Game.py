'''
Driver file for population dynamics in the tripartite game
'''

import random
import pandas as pd
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

# Simulation Settings 
NUM_ITERATIONS = 10_000
DT = .0001


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
    population = [HUMAN_COLLABORATE, HUMAN_SELF_INTERESTED, INVADER_PASSIVE, INVADER_ACTIVE]

    # Create Storage for Population Distributions
    population_df = pd.DataFrame(columns=['iteration', 'human_collab', 'human_self', 'invader_passive', 'invader_active'])

    for i_Iter in range(NUM_ITERATIONS):
        # Update Game
        game.update_game()
        # Normalize Population 
        population = [x/sum(population) for x in population]

        # Record information
        new_row = pd.DataFrame([{'iteration':i_Iter, 
                                 'human_collab': population[0], 
                                 'human_self':population[1], 
                                 'invader_passive': population[2], 
                                 'invader_active': population[3]}])
        population_df = pd.concat([new_row, population_df], ignore_index=True)

        # Get replication dynamics and update populations
        changes = get_rep_dynamics(population, game)
        population[0] += DT * changes['h_c']
        population[1] += DT * changes['h_s']
        population[2] += DT * changes['i_p']
        population[3] += DT * changes['i_a']

    game.print_gamestate()

    # Population Proportion Plot
    plt.plot(population_df['iteration'], population_df['human_collab'], label = 'Humans-Collaborative', color = 'blue')
    plt.plot(population_df['iteration'], population_df['human_self'], label = 'Humans-Self Interested', color = 'green')
    plt.plot(population_df['iteration'], population_df['invader_passive'], label = 'Invader-Passive', color = 'orange')
    plt.plot(population_df['iteration'], population_df['invader_active'], label = 'Invader-Active', color = 'red')
    # Add title and labels
    plt.title('Population Proportions Over Time')
    plt.xlabel('Iteration Number')
    plt.ylabel(f'Proportion of Population')
    plt.legend()
    # Show the plot
    plt.savefig(f'Population-Game-Images/population-{HUMAN_COLLABORATE}-{HUMAN_SELF_INTERESTED}-{INVADER_PASSIVE}-{INVADER_PASSIVE}.png')
    plt.close()

if __name__ == '__main__':
    main()