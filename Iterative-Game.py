'''
Driver file for analyzing strategies if 
there is one player in each side of the tripartite
'''

import random
import matplotlib.pyplot as plt
from Classes.InvaderGamePayoffMatrix import InvaderGamePayoffMatrix
from Classes.PlayerInformation import PlayerInformation

# Human Focused Variables
VALUE = 10 # Resource gain
COST = 5 # Cost of Self Interest
SYNERGY = 1.5 # Synergy Factor

# Invader Focused Variables
DAMAGE = 20 # Damage from Invader
ATTACK = 5 # Cost of Attacking from Invader

# Simulation settings  
ROUNDS = range(1000)
human_1 = PlayerInformation(name='Human_1', action_set=['c', 's'], strategy=.5)
human_2 = PlayerInformation(name='Human_2', action_set=['c', 's'], strategy=.5)
invader = PlayerInformation(name='Invader', action_set=['p', 'a'], strategy=.9)

# Create and initalize game
game = InvaderGamePayoffMatrix(VALUE, COST, SYNERGY, DAMAGE, ATTACK)

for i_round in ROUNDS:
    game.update_game()

    human_1.get_action()
    human_2.get_action()
    invader.get_action()

    payoffs = game.get_payoffs(human_1.current_action,
                           human_2.current_action,
                           invader.current_action)
    
    human_1.update_payoff(payoffs[0])
    human_2.update_payoff(payoffs[1])
    invader.update_payoff(payoffs[2])

    human_1_alt = game.get_payoffs(human_1.alt_action,
                                  human_2.current_action,
                                  invader.current_action)[0]
    human_2_alt = game.get_payoffs(human_1.current_action,
                                   human_2.alt_action,
                                   invader.current_action)[1]
    invader_alt = game.get_payoffs(human_1.current_action,
                                   human_2.current_action,
                                   invader.alt_action)[2]

    human_1.update_strategy(payoffs[0], human_1_alt)
    human_2.update_strategy(payoffs[1], human_2_alt)
    invader.update_strategy(payoffs[2], invader_alt)


game.print_gamestate()

output_string = f'''Total Payoffs:
Human 1: {human_1.total_payoff}
Human 2: {human_2.total_payoff}
Invader: {invader.total_payoff}

Strategy Sets:
Human 1: [c: {round(human_1.strategy, 2)}, s: {round(1 - human_1.strategy,2 )}]
Human 2: [c: {round(human_2.strategy, 2)}, s: {round(1 - human_2.strategy,2 )}]
Invader: [p: {round(invader.strategy, 2)}, a: {round(1 - invader.strategy,2 )}]
'''
print(output_string)

# Plotting strategies
plt.plot(ROUNDS, human_1.strategy_history, label = 'Human 1 (Collaborate)', color = 'blue')
plt.plot(ROUNDS, human_2.strategy_history, label = 'Human 2 (Collaborate)', color = 'green')
plt.plot(ROUNDS, invader.strategy_history, label = 'Invader (Passive)', color = 'red')

# Add title and labels
plt.title('Players Strategy Profiles ')
plt.xlabel('Iteration Number')
plt.ylabel('Probability of Action (Collaborate or Passive)')

# Display the legend
plt.legend()

# Show the plot
plt.savefig('Iterative_Strategy.png')
