import matplotlib.pyplot as plt
import numpy as np


def wykres(start, way, dist):
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    for i, ax in enumerate(axs.flat):
        # Wyciągamy współrzędne x i y z way[i]
        x_vals = [pt[0] for pt in way[i]]
        y_vals = [pt[1] for pt in way[i]]

        # Rysujemy trasę
        ax.plot(x_vals, y_vals, marker='o', linestyle='-')

        # Rysujemy punkt startowy na czerwono
        ax.plot(start[i][0], start[i][1], 'ro', label='Start')

        # Ustawiamy tytuł z odległością
        ax.set_title(f'Długość: {dist[i]}')

        # (opcjonalnie) dodaj siatkę i legendę
        ax.grid(True)
        ax.legend()

    plt.tight_layout()
    plt.show()