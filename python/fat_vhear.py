"""
Happy Valentine's Day! Here's a cute math heart to brighten your day.

Written by Ye Kyaw Thu.
I referred the following gnuplot code:
https://baturin.org/pictures/heart.gnuplot  

Last updated: 14 Feb 2024.
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the parametric equations
# Generate 500 points between 0 and 2*pi
t = np.linspace(0, 2*np.pi, 500) 

# multiply by 1.5 to make the heart wider 
x = 1.5 * np.cos(t)**3  
y = np.cos(t)**2 + np.sin(t)

plt.figure(figsize=(6, 6))
plt.fill(x, y, color='pink')  

plt.plot(x, y, color='red')
plt.title("Happy Valentine's Day!\n$x = 1.5 \cdot \cos^3(t), y = \cos^2(t) + \sin(t)$")

# Set the aspect of the plot to be equal
plt.axis('equal')

# Set x and y axis limits to be the same
# update x limits for wider heart
plt.xlim([-2, 2])
plt.ylim([-1.5, 1.5])

# Add grid lines at x=0 and y=0
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Customize x and y ticks
plt.xticks([-2, -1, 0, 1, 2])
plt.yticks([-1, 0, 1])

plt.savefig("fat_vheart.png")
plt.show()
