from najblizszy_sasiad import wykonanie
from better import opt2
from brute_force import brute_force
from wykresy import wykres
import time

punkty = [(0, 0), (1, 1), (2, 0), (5, 5), (6, 5), (5.5, 6)]


start_time = time.time()
brute_force([[-1,2],[11,84],[5,6],[1,1],[4,8],[-1,3],[55,66],[12,13],[-10,8]])
print("--- %s seconds ---" % (time.time() - start_time))
brute_force([[-1,2],[11,84],[5,6],[1,1],[4,8],[-1,3],[55,66],[12,13],[-10,8]])

start_time = time.time()
najblizszy_sasiad([[-1,2],[11,84],[5,6],[1,1],[4,8],[-1,3],[55,66],[12,13],[-10,8]])
print("--- %s seconds ---" % (time.time() - start_time))
najblizszy_sasiad([[-1,2],[11,84],[5,6],[1,1],[4,8],[-1,3],[55,66],[12,13],[-10,8]])


c=wykonanie(punkty)
brute_force(punkty)
opt2(c)
