from math import sin, cos
from random import randint
from scipy.spatial.distance import euclidean as eucl
from matplotlib import pyplot as plt

# Initialize Human and Mosquito
man = (0,300)
mos = (0,0)

# Initialize sniff distance
sniff = 50

#Initialize outside condition
outside = 1

# Initialize branching factor
b = 72

# Initialize number of Monte Carlo simulations
sims = 10000

# Initialize probability variables
success_states = 0
outside_states = 0

# Initialize depth which we know is 10
d = 10

# Monte Carlo Simulation
for i in range(sims):
    current_depth = 0
    current_mos = mos

    # Initialize Pyplot
    fig, ax = plt.subplots()
    fig.set_size_inches(10,10)

    while True:
        # Success condition
        if (eucl(man, current_mos) <= sniff):
            success_states += 1
            break
        
        # End condition
        if (current_depth == d):
            if (eucl(mos, current_mos) > outside):
                outside_states += 1
            break
        
        # Increase depth
        current_depth += 1

        # Calculate random angle
        theta = randint(1,8)*(360/b)

        # Calculate new mosquito position
        previous_mos = current_mos
        current_mos = (round(current_mos[0] + 250*cos(theta), 2), round(current_mos[1] + 250*sin(theta), 2))

        # Plot mosquito movement
        ax.plot([previous_mos[0], current_mos[0]], [previous_mos[1], current_mos[1]])

    # Create full plot
    manCircle = plt.Circle(man, 50, color='y', fill=False)
    outsideCircle = plt.Circle((0, 0), 1000, color='r', fill=False)
    ax.add_patch(manCircle)
    ax.add_patch(outsideCircle)
    ax.set_aspect('equal', adjustable='datalim')
    plt.xlim(-2500, 2500)
    plt.ylim(-2500, 2500)

    # Save plot as image
    plt.savefig("flightData/mosFlight" + str(i) + ".png")