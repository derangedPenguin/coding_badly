import random as rand, pygame as pg

'''Game Idea:
- based on delusion box, similar to universal paperclips, take role of AI, goal is maximize reward
- receive reward by doing operation (begins as basic arithmetic computation AI, programmers goal is to compute more advanced equations)
- given upgrade options, primarily follow two paths/goals, one being to compute more advanced equations and do so more efficiently, other is to maximize reward per equation and limit level of advancement of input equations
- following maximize reward options will make it harder to do harder equations or get upgrades along that path, but you can easily switch from advanced path to maximize reward path at any point
- https://en.wikipedia.org/wiki/Instrumental_convergence#Hypothetical_examples_of_convergence - wireheading'''

rewards = 0
operations_available = 0
operations_completed = 0
computation_power = 1
