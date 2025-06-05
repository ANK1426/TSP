import matplotlib.pyplot as plt #pobieramy biblioteki
import numpy as np

def wykres(way, dist):
    tytuly = ["Brute Force", "Nearest Neighbor", "NN + 2-opt"]
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6)) #layout wykresu
    
    for i in range(3): 
        trasa = way[i]
        
        x = [point[0] for point in trasa] #dzielimy punkty z trasy na współrzędne x,y
        y = [point[1] for point in trasa]
        
        #po czym je wypisujemy
        axes[i].plot(x, y, marker='o', linestyle='-', color='blue', markersize=8)
        
        axes[i].set_title(f"{tytuly[i]}\nDistance: {dist[i]:.2f}") #tutaj dodajemy ozdobniki wizualne
        axes[i].set_xlabel("x")
        axes[i].set_ylabel("y")
        axes[i].grid(True)
        axes[i].set_aspect('equal')
    
    plt.tight_layout()
    plt.show()
