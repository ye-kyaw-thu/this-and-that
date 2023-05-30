# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:44:25 2023

@author: Ye Kyaw Thu, LST, NECTEC, Thailand
This program will plot 2D Voronoi diagram and find the nearest location with 5 distance calculation methods

"""

import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

def plot_voronoi(points):
    # Compute Voronoi diagram of the points
    vor = Voronoi(points)

    # Plot Voronoi diagram
    voronoi_plot_2d(vor)
    plt.plot(points[:, 0], points[:, 1], 'ko')
    plt.title('Voronoi diagram of locations')
    plt.show()

def find_nearest_location(residence, locations, distance_metric):
    if distance_metric == "euclidean":
        distances = np.linalg.norm(locations - residence, axis=1)
    elif distance_metric == "manhattan":
        distances = np.sum(np.abs(locations - residence), axis=1)
    elif distance_metric == "chebyshev":
        distances = np.max(np.abs(locations - residence), axis=1)
    elif distance_metric == "minkowski":
        distances = np.power(np.sum(np.abs(locations - residence)**3, axis=1), 1/3)
    elif distance_metric == "cosine":
        distances = 1 - np.dot(locations, residence) / (np.linalg.norm(locations, axis=1) * np.linalg.norm(residence))
    else:
        raise ValueError("Unknown distance metric")

    # Find the index of the nearest location
    nearest_location_index = np.argmin(distances)

    return locations[nearest_location_index]

def main():
    # Define a set of points (e.g., locations of hospitals)
    locations = np.array([[2, 3], [5, 4], [3, 6], [3.5, 5], [6, 7], [7, 6]])

    # Plot Voronoi diagram of locations
    plot_voronoi(locations)

    # Input a point (e.g., a residence)
    print("Please input the coordinates of your residence (two numbers separated by a space):")
    residence = np.array(list(map(float, input().split())))

    # List of distance metrics
    distance_metrics = ["euclidean", "manhattan", "chebyshev", "minkowski", "cosine"]

    # Find the nearest location to the residence using each distance metric
    for distance_metric in distance_metrics:
        nearest_location = find_nearest_location(residence, locations, distance_metric)
        print(f"The nearest location to your residence using {distance_metric} distance is at {nearest_location}")

if __name__ == "__main__":
    main()
