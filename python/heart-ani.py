"""
For my <3 
Ye wrote this code with ChatGPT.
Reference: https://www.reddit.com/r/matlab/comments/1eq66kc/made_a_heart_on_matlab/
Date: 10 Feb 2025.

How to run:
python ./heart-ani.py --text "Happy Valentine's Day! Sar U"
"""

import numpy as np
import matplotlib.pyplot as plt
import imageio
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Generate an animated heart shape GIF.')
parser.add_argument('-t', '--text', type=str, default="Happy Valentine's Day 2025!", help='Text to display on the animation')
args = parser.parse_args()

# Define x range
x = np.arange(-2, 2, 0.005)
frames = []

# Create a figure
fig, ax = plt.subplots()
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 3.5])  # Increased y-limit for better spacing
ax.text(0, 3.2, args.text, fontsize=14, ha='center', va='center', color='red', fontweight='bold')  # Adjusted text position
line, = ax.plot([], [], 'r')

# Generate animation frames
for a in range(0, 1700, 5):
    y = np.cbrt(x**2) + 1.1 * np.sin(a * x) * np.sqrt(4 - x**2)
    line.set_data(x, y)
    plt.pause(0.01)
    fig.canvas.draw()
    
    # Capture frame for GIF
    frame = np.array(fig.canvas.renderer.buffer_rgba())
    frames.append(frame)

# Save as an animated GIF
imageio.mimsave('heart_animation.gif', frames, fps=30)

