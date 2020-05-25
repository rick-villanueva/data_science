"""
Let's say I roll a dice to determine if I go up or down a step in a building with
100 floors (1 step = 1 floor). If the dice is less than 2, I go down a step. If 
the dice is less than or equal to 5, I go up a step, and if the dice is equal to 6,
I go up x steps based on a random integer generator between 1 and 6. What is the probability
I will be higher than floor 60?
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize as opt
from scipy import stats as ss
from scipy.stats import norm

# Set the seed
np.random.seed(123)

# Simulate random walk 
all_walks = []
for i in range(1000):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice > 2 and dice < 6:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 : # There's a 0.1% chance I fall and have to start at 0
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
# bins = [10,20,30,40,50,60,70,80,90,100]
plt.hist(ends,bins=10,edgecolor='k',alpha=0.65)
plt.axvline(np.median(ends), color='k', linestyle='dashed', linewidth=1)
# Fit a normal distribution to the data:
# mu, std = norm.fit(ends)
# xmin, xmax = plt.xlim()
# x = np.linspace(xmin, xmax, 100)
# p = norm.pdf(x, mu, std)
# plt.plot(x, p, 'k', linewidth=2)

plt.style.use('fivethirtyeight')
plt.xlabel("Floor")
plt.ylabel("# of times in floor")
plt.show()
