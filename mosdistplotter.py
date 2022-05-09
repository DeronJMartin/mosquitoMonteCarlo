import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Read data
df = pd.read_csv('distance.csv')

# Create plot variables
x = range(0,2526,25)
y = df.iloc[0]

# Plot graph
plt.plot(x, y)

# Set axis limits
plt.xlim(0,2525)
plt.ylim(0,1)

# Set axis labels
plt.xlabel('Distance')
plt.ylabel('Probability')
plt.savefig('varyingDistance.png')