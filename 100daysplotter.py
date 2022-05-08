import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Read data
df = pd.read_csv('100days.csv')

# Create plot variables
x = range(1,101)
y = df.iloc[0]

# Plot graph
plt.plot(x, y)

# Set axis limits
plt.xlim(1,100)
plt.ylim(0,0.1)

# Set axis labels
plt.xlabel('Days')
plt.ylabel('Probability')
plt.show()