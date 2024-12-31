import random
import matplotlib.pyplot as plt
import time
import numpy as np
from matplotlib.patches import Polygon

def visualize_pi_estimation(num_points):
    inside_circle = 0
    x_inside, y_inside = [], []
    x_outside, y_outside = [], []
    pi_values = []
    
    area_diamond = 2
    area_square = 4
    area_ratio = area_diamond / area_square
    
    plt.figure(figsize=(6,6))

    for i in range(1, num_points + 1):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        distance = x**2 + y**2
        if distance <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)
        pi_estimate = (inside_circle / i) * 4
        pi_values.append(pi_estimate)

        plt.clf()
        plt.scatter(x_inside, y_inside, color='blue', s=1, label='Inside Circle')
        plt.scatter(x_outside, y_outside, color='orange', s=1, label='Outside Circle')
        
        circle = plt.Circle((0, 0), 1, fill=False, color='black', linewidth=1)
        plt.gca().add_artist(circle)

        diamond_vertices = [
            (0, 1),   
            (1, 0),   
            (0, -1),  
            (-1, 0)   
        ]
        diamond = Polygon(diamond_vertices, closed=True, fill=False, edgecolor='black', linewidth=1)
        plt.gca().add_patch(diamond)

        plt.xlim(-1.1, 1.1) 
        plt.ylim(-1.1, 1.1)
        plt.gca().set_aspect('equal', adjustable='box')
        
        plt.title(f"Monte Carlo Simulation of Pi\nPoints: {i} | Pi Estimate: {pi_estimate:.5f}\nArea Ratio (Diamond:Square): {area_ratio:.5f}")
        plt.legend(loc="upper right")
        
        plt.pause(0.001)
        time.sleep(0.01)  

    plt.show()

num_points = 500
visualize_pi_estimation(num_points)