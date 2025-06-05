import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt

def wykres(way, dist):
    etykiety = ["Brute Force", "Nearest Neighbor", "NN + 2-opt"]
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    for i in range(3):
        trasa = way[i]
        
        
        x = [point[0] for point in trasa]
        y = [point[1] for point in trasa]
        
        
        axes[i].plot(x, y, marker='o', linestyle='-', color='blue', markersize=8)
        
        axes[i].set_title(f"{etykiety[i]}\nDistance: {dist[i]:.2f}")
        axes[i].set_xlabel("x")
        axes[i].set_ylabel("y")
        axes[i].grid(True)
        axes[i].set_aspect('equal')
    
    plt.tight_layout()
    plt.show()