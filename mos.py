from math import sin, cos
from random import randint
from scipy.spatial.distance import euclidean as eucl

# Initialize Human and Mosquito
man = (0,300)
mos = (0,0)

# Initialize sniff distance
sniff = 50

#Initialize outside condition
outside = 1000

# Initialize branching factor
b = 72

# Initialize number of Monte Carlo simulations
sims = 10000

# Initialize probability variables
success_states = 0
fail_states = 0
outside_states = 0

# Initialize depth which we know is 10
d = 10

# Monte Carlo Simulation
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
            if (eucl(mos, current_mos) > outside):
                outside_states += 1
            fail_states += 1
            break
        
        # Increase depth
        current_depth += 1

        # Calculate random angle
        theta = randint(1,8)*(360/b)

        # Calculate new mosquito position
        current_mos = (round(current_mos[0] + 250*cos(theta), 2), round(current_mos[1] + 250*sin(theta), 2))

# Print results
print("No. of success states: %d", success_states)
print("No. of fail states: %d", fail_states)
print("No. of outside death states: %d", outside_states)
print("\n")
print("Probability of mosqutio finding the human: %f", success_states/sims)
print("Probability of mosqutio dying without finding the human: %f", fail_states/sims)
print("Probability of mosqutio dying further than 1000m: %f", outside_states/sims)