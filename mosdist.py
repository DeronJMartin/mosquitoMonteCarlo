from math import sin, cos
from random import randint
from scipy.spatial.distance import euclidean as eucl
import pandas as pd

# Initialize Human and Mosquito
man = (0,0)
mos = (0,0)

# Initialize sniff distance
sniff = 50

#Initialize outside condition
outside = 1000

# Initialize branching factor
b = 72

# Initialize number of Monte Carlo simulations
sims = 1000000

# Initialize depth which we know is 10
d = 10

# Initialize pandas dataframe to collect probability distribution
prob = pd.DataFrame()

# Monte Carlo Simulation
for k in range(0,2526, 25):

    # Change distance of man from center
    man = (man[0], man[1] + k)

    # Initialize probability variables
    success_states = 0

    for i in range(sims):
        current_depth = 0
        current_mos = mos    

        while True:
            # Success condition
            if (eucl(man, current_mos) <= sniff):
                success_states += 1
                break
            
            # End condition
            if (current_depth == d):
                break
            
            # Increase depth
            current_depth += 1

            # Calculate random angle
            theta = randint(1,8)*(360/b)

            # Calculate new mosquito position
            current_mos = (round(current_mos[0] + 250*cos(theta), 2), round(current_mos[1] + 250*sin(theta), 2))
    
    prob[k] = [success_states/sims]

prob.to_csv("distance.csv", encoding='utf-8', index=False)