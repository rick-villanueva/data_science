"""
You live in a city in which blocks are arranged in a grid.
You decide to go for a walk, in which, at each intersection
you decide your next move randomly. Your four choices are
North, South, East and West and backtracking is permitted.
Once you're finished with your walk, you check to see how far
away you are.
If you are more than 4 blocks away, you will pay for transportation.
Otherwise, you will walk home.
What is the longest random walk you can take so that on average
you will end up 4 blocks or fewer from home?
"""
import random

def random_walk(n):
    #Return coordinates after n block random random_walk
    x,y = 0,0
    for i in range(n):
        (dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
    return (x,y)
# Monte Carlo simulation
number_of_walks = 10000

"""
What is the longest random walk you can take,
so that on avergae you will end up 4 blocks or
fewer from home? Or, less than 50% chance you
pay to go home.
"""

for walk_length in range(1,31): # There are 30 blocks in city
    no_transport = 0 # Number of walks 4 or fewer blocks from homes
    for i in range(number_of_walks):
        (x,y) = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print("Walk size = ", walk_length," / % of no transport = ", 100*no_transport_percentage)
